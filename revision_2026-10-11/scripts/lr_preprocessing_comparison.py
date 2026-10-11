"""Full-data LR_C3 preprocessing comparison; no historical score is overwritten.

Global class weights are held fixed in both arms to isolate TF-IDF fit scope.
The current sklearn API omits removed multi_class; SAGA uses multinomial loss
for three classes. This is a new environment comparison, not historical replay.
"""
import argparse, ast, gc, hashlib, inspect, json, os, platform, re, signal, sys, time, unicodedata, warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import numpy as np
import pandas as pd
import scipy
import scipy.sparse as sp
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.utils.class_weight import compute_class_weight

def load_rules(source_path):
    tree = ast.parse(Path(source_path).read_text())
    names = {'BANGLA_RE','EMOJI_RE','BANGLA_TOXIC','TRANSLIT_TOXIC','ENGLISH_TOXIC','ALL_EXPLICIT','SUBTLE_WORDS','SARCASM_RE','THREAT_RE','HATE_RE'}
    funcs = {'clean','signals','process','num_feats_fast'}
    selected = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in node.targets): selected.append(node)
        if isinstance(node, ast.FunctionDef) and node.name in funcs: selected.append(node)
    env = {'re':re,'unicodedata':unicodedata,'np':np}
    exec(compile(ast.Module(body=selected,type_ignores=[]), str(source_path), 'exec'),env)
    assert funcs.issubset(env)
    return env

def feature_views(texts, rules):
    clean = [rules['clean'](s) for s in texts]
    sigs = [rules['signals'](s) for s in texts]
    proc = [c+' SSEP '+s for c,s in zip(clean,sigs)]
    return [proc,proc,clean,sigs]

def vectorizers():
    return [TfidfVectorizer(max_features=100000,ngram_range=(1,3),sublinear_tf=True,min_df=1,max_df=.98,analyzer='word',token_pattern=r'\S+',strip_accents=None),
            TfidfVectorizer(max_features=80000,ngram_range=(2,5),sublinear_tf=True,min_df=2,analyzer='char_wb',strip_accents=None),
            TfidfVectorizer(max_features=50000,ngram_range=(1,4),sublinear_tf=True,min_df=2,analyzer='char',strip_accents=None),
            TfidfVectorizer(max_features=10000,ngram_range=(1,2),sublinear_tf=True,min_df=1,analyzer='word',token_pattern=r'\S+')]

def build_features(views, fit_idx, apply_idx):
    a,b, widths = [],[],[]
    for j,(v,raw) in enumerate(zip(vectorizers(),views)):
        print('feature branch',j+1,'fit rows',len(fit_idx),flush=True)
        x=v.fit_transform([raw[i] for i in fit_idx])
        z=v.transform([raw[i] for i in apply_idx])
        widths.append(x.shape[1]);a.append(x);b.append(z)
    return sp.hstack(a,format='csr'),sp.hstack(b,format='csr'),widths

def make_lr(cw,C=3.,meta=False):
    kw=dict(C=C,max_iter=500 if meta else 2000,class_weight=cw,random_state=42)
    if not meta: kw.update(solver='saga',tol=1e-3)
    if 'multi_class' in inspect.signature(LogisticRegression).parameters:kw['multi_class']='multinomial'
    return LogisticRegression(**kw)

def main():
    base=Path(__file__).resolve().parents[2]
    ap=argparse.ArgumentParser();ap.add_argument('--train',default=str(base/'data/herwill_2026/train.csv'));ap.add_argument('--source',default=str(base/'audit/updated_notebook_source.py'));ap.add_argument('--out',default=str(Path(__file__).resolve().parents[1]/'audit/lr_comparison'));ap.add_argument('--wall-seconds',type=int,default=1800);ap.add_argument('--jobs',type=int,default=1)
    args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();state={'status':'running','environment':{'python':platform.python_version(),'sklearn':sklearn.__version__,'numpy':np.__version__,'scipy':scipy.__version__,'pandas':pd.__version__,'cpu_count':os.cpu_count()},'scope':'Full-data new-run comparison; historical package versions unknown; global class weights held fixed','arms':{},'train_sha256':hashlib.sha256(Path(args.train).read_bytes()).hexdigest()}
    def save():
        state['elapsed_seconds']=time.monotonic()-started
        (out/'results.json').write_text(json.dumps(state,indent=2))
    def stop(signum,frame):
        state['status']='incomplete_wall_budget';save();sys.stdout.flush();sys.stderr.flush();os._exit(124)
    signal.signal(signal.SIGALRM,stop);signal.alarm(args.wall_seconds)
    save()
    try:
        df=pd.read_csv(args.train);texts=df.text.fillna('').astype(str).tolist();y=df.y.to_numpy();rules=load_rules(args.source);views=feature_views(texts,rules)
        folds=list(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y));cw={int(k):float(v) for k,v in zip([0,1,2],compute_class_weight('balanced',classes=np.array([0,1,2]),y=y))}
        fold_ids=np.empty(len(y),int)
        for k,(_,val) in enumerate(folds):fold_ids[val]=k
        pd.DataFrame({'id':df.id,'y':y,'fold':fold_ids}).to_csv(out/'folds.csv',index=False)
        for arm in ['global','within_fold']:
            print('ARM',arm,flush=True);oof=np.full((len(y),3),np.nan);rec={'folds':[],'completed':False};state['arms'][arm]=rec;save()
            if arm=='global':
                mats=[];widths=[]
                for j,(v,raw) in enumerate(zip(vectorizers(),views)):
                    print('global feature branch',j+1,flush=True);m=v.fit_transform(raw);widths.append(m.shape[1]);mats.append(m)
                X=sp.hstack(mats,format='csr');del mats;gc.collect();rec['global_widths']=widths;save()
            def fit_fold(k,tr,val):
                if arm=='global':a,b=X[tr],X[val];wid=widths
                else:a,b,wid=build_features(views,tr,val)
                model=make_lr(cw);t=time.monotonic();print('fit',arm,k+1,a.shape,flush=True)
                model.fit(a,y[tr])
                prob=model.predict_proba(b);assert model.classes_.tolist()==[0,1,2]
                hit_limit=bool(np.any(model.n_iter_>=model.max_iter))
                fr={'fold':k+1,'macro_f1':float(f1_score(y[val],prob.argmax(1),average='macro')),'widths':wid,'n_iter':model.n_iter_.tolist(),'fit_seconds':time.monotonic()-t,'hit_iteration_limit':hit_limit,'warnings':['iteration limit reached; inspect convergence'] if hit_limit else []}
                print(json.dumps(fr),flush=True);return val,prob,fr
            with ThreadPoolExecutor(max_workers=args.jobs) as pool:
                futures=[pool.submit(fit_fold,k,tr,val) for k,(tr,val) in enumerate(folds)]
                for future in as_completed(futures):
                    val,prob,fr=future.result();oof[val]=prob;rec['folds'].append(fr);rec['folds'].sort(key=lambda v:v['fold']);save()
            assert np.isfinite(oof).all();rec['pooled_macro_f1']=float(f1_score(y,oof.argmax(1),average='macro'));rec['completed']=True;np.savez_compressed(out/(arm+'_oof.npz'),id=df.id.to_numpy(),y=y,fold=fold_ids,prob=oof);save()
            if arm=='global':del X;gc.collect()
        state['status']='completed';state['global_minus_within_fold']=state['arms']['global']['pooled_macro_f1']-state['arms']['within_fold']['pooled_macro_f1'];signal.alarm(0);save();print(json.dumps(state),flush=True)
    except SystemExit:raise
    except Exception as e:
        state['status']='failed';state['error']=repr(e);save();raise

if __name__=='__main__':main()
