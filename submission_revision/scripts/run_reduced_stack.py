"""Full-data reduced stacking comparison. No historical results are overwritten.

Three bases: LR_C3, isotonic-calibrated SGD and CNB; nine meta inputs.
Both outer assessments use identical base predictions fitted on the outer
training subset. Nested meta-training probabilities are regenerated inside
that subset; nonnested training uses the shared outer-OOF matrix.
All TF-IDF fits/class weights use the corresponding allowed training subset.
"""
import argparse,gc,hashlib,json,os,platform,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np,pandas as pd,scipy,sklearn
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.utils.class_weight import compute_class_weight
import lr_preprocessing_comparison as lib


def class_weights(y):
 return dict(zip([0,1,2],map(float,compute_class_weight('balanced',classes=np.arange(3),y=y))))


def fit_bases(a,b,y,widths):
 cw=class_weights(y);start=time.monotonic();lr=lib.make_lr(cw);lr.fit(a,y)
 p=[lr.predict_proba(b)];metadata={'lr_n_iter':lr.n_iter_.tolist(),'lr_cap_reached':bool((lr.n_iter_>=lr.max_iter).any())}
 sgd=CalibratedClassifierCV(SGDClassifier(loss='modified_huber',alpha=1e-4,max_iter=200,class_weight=cw,random_state=42,n_jobs=1),cv=2,method='isotonic',ensemble=True,n_jobs=1)
 sgd.fit(a,y);p.append(sgd.predict_proba(b))
 char=slice(widths[0],widths[0]+widths[1]+widths[2]);cnb=CalibratedClassifierCV(ComplementNB(alpha=.05,norm=True),cv=2,method='isotonic',ensemble=True,n_jobs=1)
 cnb.fit(a[:,char],y);p.append(cnb.predict_proba(b[:,char]))
 for estimator in [lr,sgd,cnb]:assert estimator.classes_.tolist()==[0,1,2]
 metadata['sgd_iterations']=[c.estimator.n_iter_ for c in sgd.calibrated_classifiers_];metadata['fit_seconds']=time.monotonic()-start
 return np.hstack(p),metadata


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);ap.add_argument('--jobs',type=int,default=3);args=ap.parse_args();base=Path(args.repo);out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
 tr=pd.read_csv(base/'data/herwill_2026/train.csv');y=tr.y.to_numpy();n=len(y);rules=lib.load_rules(base/'audit/updated_notebook_source.py');views=lib.feature_views(tr.text.fillna('').astype(str).tolist(),rules);folds=list(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(n),y));fid=np.zeros(n,int)
 for k,(_,e) in enumerate(folds):fid[e]=k
 start=time.monotonic();state={'status':'running','evidence':'N: assistant-executed new run; not an author-independent rerun','environment':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,'sklearn':sklearn.__version__},'train_sha256':hashlib.sha256((base/'data/herwill_2026/train.csv').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_order':['LR_C3','SGD','CNB'],'outer_inference':'one base fit on all outer training rows, identical outer base probabilities in both arms','feature_and_weight_scope':'each permitted base fitting subset; meta weights from outer training labels','outer_folds':3,'inner_folds':3,'seed':42,'base_max_iter':2000,'meta_max_iter':500,'calibration_cv':2,'calibration_ensemble':True,'base_records':[],'nested_records':[]}
 def save():state['elapsed_seconds']=time.monotonic()-start;(out/'reduced_stack_results.json').write_text(json.dumps(state,indent=2)+'\n')
 save();base_oof=np.full((n,9),np.nan)
 def outer_base(k,t,e):
  print('OUTER BASE',k+1,flush=True);a,b,widths=lib.build_features(views,t,e);p,meta=fit_bases(a,b,y[t],widths);meta.update(fold=k+1,widths=widths);print('OUTER COMPLETE',k+1,json.dumps(meta),flush=True);return e,p,meta
 with ThreadPoolExecutor(max_workers=args.jobs) as pool:
  for fut in as_completed([pool.submit(outer_base,k,t,e) for k,(t,e) in enumerate(folds)]):
   e,p,m=fut.result();base_oof[e]=p;state['base_records'].append(m);save()
 assert np.isfinite(base_oof).all();np.savez_compressed(out/'reduced_base_oof.npz',id=tr.id.to_numpy(),y=y,fold=fid,prob=base_oof)
 nonnested=np.full((n,3),np.nan)
 for k,(t,e) in enumerate(folds):
  meta=lib.make_lr(class_weights(y[t]),C=10,meta=True);meta.fit(base_oof[t],y[t]);nonnested[e]=meta.predict_proba(base_oof[e])
 state['nonnested_macro_f1']=float(f1_score(y,nonnested.argmax(1),average='macro'));print('NONNESTED F1',state['nonnested_macro_f1'],flush=True);save();np.savez_compressed(out/'reduced_nonnested_oof.npz',id=tr.id.to_numpy(),y=y,fold=fid,prob=nonnested)
 gc.collect();nested=np.full((n,3),np.nan)
 def outer_nested(k,t,e):
  print('NESTED OUTER',k+1,flush=True);inner_oof=np.full((len(t),9),np.nan);records=[]
  inner=list(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(t)),y[t]))
  for j,(uf,vf) in enumerate(inner):
   u,v=t[uf],t[vf];print('INNER',k+1,j+1,flush=True);a,b,widths=lib.build_features(views,u,v);p,m=fit_bases(a,b,y[u],widths);inner_oof[vf]=p;m.update(inner_fold=j+1,widths=widths);records.append(m);del a,b;gc.collect();print('INNER COMPLETE',k+1,j+1,json.dumps(m),flush=True)
  assert np.isfinite(inner_oof).all();meta=lib.make_lr(class_weights(y[t]),C=10,meta=True);meta.fit(inner_oof,y[t]);p=meta.predict_proba(base_oof[e]);np.savez_compressed(out/f'inner_meta_training_outer_{k+1}.npz',id=tr.id.to_numpy()[t],y=y[t],prob=inner_oof)
  return e,p,{'outer_fold':k+1,'inner_base_records':records,'meta_n_iter':meta.n_iter_.tolist()}
 with ThreadPoolExecutor(max_workers=args.jobs) as pool:
  for fut in as_completed([pool.submit(outer_nested,k,t,e) for k,(t,e) in enumerate(folds)]):
   e,p,m=fut.result();nested[e]=p;state['nested_records'].append(m);save()
 assert np.isfinite(nested).all();state['nested_macro_f1']=float(f1_score(y,nested.argmax(1),average='macro'));state['nonnested_minus_nested']=state['nonnested_macro_f1']-state['nested_macro_f1'];state['status']='completed';save();np.savez_compressed(out/'reduced_nested_oof.npz',id=tr.id.to_numpy(),y=y,fold=fid,prob=nested);print(json.dumps(state),flush=True)

if __name__=='__main__':main()
