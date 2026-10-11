"""LBFGS sensitivity for the same C=3 multinomial L2 objective.

Different optimizer from historical SAGA; never labelled an exact replay.
Original comparison class weights remain fixed; group/exclusion arms use
weights from each permitted training fold. Saves fixed OOF predictions.
"""
import argparse,gc,hashlib,json,platform,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np,pandas as pd,scipy,scipy.sparse as sp,sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold,StratifiedGroupKFold
from sklearn.utils.class_weight import compute_class_weight
import lr_preprocessing_comparison as lib

def weights(y):return dict(zip([0,1,2],map(float,compute_class_weight('balanced',classes=np.arange(3),y=y))))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--jobs',type=int,default=2);ap.add_argument('--arms',nargs='+',default=['global','within_fold','cleaner_group','raw_excluded']);args=ap.parse_args();out=args.out;out.mkdir(parents=True,exist_ok=True)
 df=pd.read_csv(args.repo/'data/herwill_2026/train.csv');y=df.y.to_numpy();texts=df.text.fillna('').astype(str).tolist();rules=lib.load_rules(args.repo/'audit/updated_notebook_source.py');views=lib.feature_views(texts,rules);cw=weights(y);start=time.monotonic();state={'status':'running','optimizer':'LBFGS','C':3,'tol':1e-6,'max_iter':2000,'seed':42,'evidence':'N: assistant execution, not author-independent replication','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sklearn':sklearn.__version__},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arms':{}}
 def save():state['elapsed_seconds']=time.monotonic()-start;(out/'convergence_results.json').write_text(json.dumps(state,indent=2)+'\n')
 for arm in args.arms:
  keep=np.arange(len(y))
  if arm=='raw_excluded':
   d=pd.DataFrame({'text':texts});fid=np.zeros(len(y),int)
   for k,(_,v) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y)):fid[v]=k
   d['fold']=fid;g=d.groupby('text').fold.nunique();keep=np.flatnonzero(~d.text.isin(g[g>1].index).to_numpy())
  if arm=='cleaner_group':splits=list(StratifiedGroupKFold(3,shuffle=True,random_state=42).split(np.zeros(len(keep)),y[keep],groups=pd.factorize(pd.Series(views[2]),sort=False)[0][keep]))
  else:splits=list(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(keep)),y[keep]))
  splits=[(keep[t],keep[v]) for t,v in splits];rec={'rows':len(keep),'folds':[],'class_weight_scope':'global fixed' if arm in ['global','within_fold'] else 'training fold','completed':False};state['arms'][arm]=rec;save();pred=np.full((len(y),3),np.nan);fid=np.full(len(y),-1,int)
  if arm=='global':mats=[v.fit_transform(raw) for v,raw in zip(lib.vectorizers(),views)];X=sp.hstack(mats,format='csr');del mats;gc.collect()
  def fit(k,t,v):
   if arm=='global':a,b=X[t],X[v];wid=[X.shape[1]]
   else:a,b,wid=lib.build_features(views,t,v)
   localcw=cw if arm in ['global','within_fold'] else weights(y[t]);model=LogisticRegression(C=3,solver='lbfgs',tol=1e-6,max_iter=2000,class_weight=localcw,random_state=42);now=time.monotonic();print('LBFGS',arm,k+1,a.shape,flush=True);model.fit(a,y[t]);p=model.predict_proba(b)
   q=model.predict_proba(a);resid=q-np.eye(3)[y[t]];sw=np.array([localcw[int(c)] for c in y[t]]);resid*=sw[:,None]/sw.sum();grad=np.asarray(a.T@resid).T+model.coef_/(3*sw.sum());gradmax=float(max(abs(grad).max(),abs(resid.sum(0)).max()));r={'fold':k+1,'n_iter':model.n_iter_.tolist(),'hit_iteration_limit':bool((model.n_iter_>=model.max_iter).any()),'penalized_objective_gradient_max_abs':gradmax,'macro_f1':float(f1_score(y[v],p.argmax(1),average='macro')),'fit_seconds':time.monotonic()-now,'widths':wid};print(json.dumps(r),flush=True);return k,v,p,r
  with ThreadPoolExecutor(max_workers=args.jobs) as pool:
   for f in as_completed([pool.submit(fit,k,t,v) for k,(t,v) in enumerate(splits)]):k,v,p,r=f.result();pred[v]=p;fid[v]=k;rec['folds'].append(r);save()
  assert np.isfinite(pred[keep]).all();rec['folds'].sort(key=lambda x:x['fold']);rec['macro_f1']=float(f1_score(y[keep],pred[keep].argmax(1),average='macro'));rec['completed']=True;np.savez_compressed(out/f'lbfgs_{arm}_oof.npz',id=df.id.to_numpy()[keep],y=y[keep],fold=fid[keep],prob=pred[keep]);save()
  if arm=='global':del X;gc.collect()
 state['status']='completed';save();print(json.dumps(state),flush=True)
if __name__=='__main__':main()
