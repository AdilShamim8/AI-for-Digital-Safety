"""Exclude original raw cross-fold groups while preserving original fold IDs."""
import argparse,json,time,hashlib,gc
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np,pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import f1_score
import lr_preprocessing_comparison as lib
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--jobs',type=int,default=2);args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True);df=pd.read_csv(args.repo/'data/herwill_2026/train.csv');y=df.y.to_numpy();raw=df.text.fillna('').astype(str).tolist();fold=np.empty(len(y),int)
for k,(_,v) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y)):fold[v]=k
g=pd.DataFrame({'text':raw,'fold':fold}).groupby('text').fold.nunique();exclude=pd.Series(raw).isin(g[g>1].index).to_numpy();keep=np.flatnonzero(~exclude);assert len(keep)==47046;assert pd.DataFrame({'text':np.array(raw,dtype=object)[keep],'fold':fold[keep]}).groupby('text').fold.nunique().max()==1
views=lib.feature_views(raw,lib.load_rules(args.repo/'audit/updated_notebook_source.py'));pred=np.full((len(y),3),np.nan);start=time.monotonic();state={'status':'running','evidence':'N: assistant execution; not author-independent replication','policy':'Remove all 771 rows in original spanning raw-text groups; retain original seed-42 stratified fold IDs on remaining rows. No resplit.','rows':len(keep),'excluded_rows':int(exclude.sum()),'raw_cross_fold_groups_after_exclusion':0,'C':3,'solver':'lbfgs','tol':1e-6,'max_iter':2000,'class_weight_scope':'per retained training subset','folds':[],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
def save():state['elapsed_seconds']=time.monotonic()-start;(args.out/'exclusion_fixedfold_results.json').write_text(json.dumps(state,indent=2)+'\n')
def fit(k):
 t=keep[fold[keep]!=k];v=keep[fold[keep]==k];a,b,w=lib.build_features(views,t,v);cw=dict(zip([0,1,2],map(float,compute_class_weight('balanced',classes=np.arange(3),y=y[t]))));m=LogisticRegression(C=3,solver='lbfgs',tol=1e-6,max_iter=2000,class_weight=cw,random_state=42);now=time.monotonic();m.fit(a,y[t]);prob=m.predict_proba(b);res=m.predict_proba(a)-np.eye(3)[y[t]];sw=np.array([cw[int(c)] for c in y[t]]);res*=sw[:,None]/sw.sum();grad=np.asarray(a.T@res).T+m.coef_/(3*sw.sum());record={'fold':k+1,'n_iter':m.n_iter_.tolist(),'hit_iteration_limit':bool((m.n_iter_>=m.max_iter).any()),'penalized_objective_gradient_max_abs':float(max(abs(grad).max(),abs(res.sum(0)).max())),'fit_seconds':time.monotonic()-now,'rows_train':len(t),'rows_assessment':len(v),'widths':w};print(json.dumps(record),flush=True);return v,prob,record
save()
with ThreadPoolExecutor(max_workers=args.jobs) as pool:
 for f in as_completed([pool.submit(fit,k) for k in range(3)]):v,prob,record=f.result();pred[v]=prob;state['folds'].append(record);save()
assert np.isfinite(pred[keep]).all();state['folds'].sort(key=lambda x:x['fold']);state['macro_f1']=float(f1_score(y[keep],pred[keep].argmax(1),average='macro'));state['status']='completed';np.savez_compressed(args.out/'lbfgs_exclusion_fixedfold_oof.npz',id=df.id.to_numpy()[keep],y=y[keep],fold=fold[keep],prob=pred[keep]);save();print(json.dumps(state),flush=True)
