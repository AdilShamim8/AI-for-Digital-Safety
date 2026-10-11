"""Independent rescore/alignment and release checks for this audit package."""
import argparse,hashlib,json,re,zipfile
from pathlib import Path
import numpy as np,pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.utils.class_weight import compute_class_weight

def manual_f1(y,prob):
 cm=np.bincount(3*y+prob.argmax(1),minlength=9).reshape(3,3);den=cm.sum(0)+cm.sum(1)
 return float(np.divide(2*cm.diagonal(),den,out=np.zeros(3),where=den>0).mean()),cm.tolist()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--revision',type=Path,required=True);args=ap.parse_args();rev=args.revision;df=pd.read_csv(args.repo/'data/herwill_2026/train.csv');y=df.y.to_numpy();ids=df.id.to_numpy();fold=np.empty(len(y),int);splits=list(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y))
 for k,(_,v) in enumerate(splits):fold[v]=k
 report={'status':'passed','checks':[],'probabilities':{},'note':'Independent arithmetic/alignment checks; not independent author execution.'}
 def check(v,name):
  if not v:raise AssertionError(name)
  report['checks'].append(name)
 def assess(path,target=None,expected_ids=ids,expected_y=y,expected_fold=fold):
  a=np.load(path);p=a['prob'];check(np.array_equal(a['id'],expected_ids),path.name+' ID order');check(np.array_equal(a['y'],expected_y),path.name+' labels');check(np.isfinite(p).all() and p.min()>=-1e-12,path.name+' finite nonnegative');check(np.allclose(p.reshape(len(p),-1,3).sum(2),1,atol=1e-8),path.name+' class-probability normalization')
  if expected_fold is not None:check(np.array_equal(a['fold'],expected_fold),path.name+' seed-42 fold identity')
  if p.shape[1]==3:
   score,cm=manual_f1(expected_y,p);report['probabilities'][path.name]={'macro_f1':score,'confusion':cm}
   if target is not None:check(abs(score-target)<1e-12,path.name+' manual pooled score')
 old=args.repo/'revision_2026-10-11/audit/lr_comparison';r=json.loads((old/'results.json').read_text())
 for arm in ['global','within_fold']:assess(old/(arm+'_oof.npz'),r['arms'][arm]['pooled_macro_f1'])
 stack=json.loads((rev/'results/reduced_stack_results.json').read_text());check(stack['status']=='completed','Reduced stack completed');assess(rev/'results/reduced_base_oof.npz')
 for arm in ['nonnested','nested']:assess(rev/f'results/reduced_{arm}_oof.npz',stack[arm+'_macro_f1'])
 for k,(t,_) in enumerate(splits):assess(rev/f'results/inner_meta_training_outer_{k+1}.npz',expected_ids=ids[t],expected_y=y[t],expected_fold=None)
 basep=np.load(rev/'results/reduced_base_oof.npz')['prob'];report['meta_refits']=[]
 for k,(t,v) in enumerate(splits):
  cw=dict(zip([0,1,2],map(float,compute_class_weight('balanced',classes=np.arange(3),y=y[t]))))
  for arm in ['nonnested','nested']:
   trainp=basep[t] if arm=='nonnested' else np.load(rev/f'results/inner_meta_training_outer_{k+1}.npz')['prob'];m=LogisticRegression(C=10,max_iter=500,class_weight=cw,random_state=42);m.fit(trainp,y[t]);saved=np.load(rev/f'results/reduced_{arm}_oof.npz')['prob'][v];delta=float(abs(m.predict_proba(basep[v])-saved).max());check(delta<1e-12,f'{arm} outer {k+1} meta-refit probability identity');check((m.n_iter_<m.max_iter).all(),f'{arm} outer {k+1} meta refit below cap');report['meta_refits'].append({'arm':arm,'outer_fold':k+1,'n_iter':m.n_iter_.tolist(),'max_probability_difference':delta})
 sens=json.loads((rev/'results/convergence_results.json').read_text());check(sens['status']=='completed','Sensitivity completed');savedfold=pd.read_csv(rev/'results/duplicate_folds.csv')
 for arm,rec in sens['arms'].items():
  path=rev/f'results/lbfgs_{arm}_oof.npz';a=np.load(path)
  if arm=='raw_excluded':
   mask=np.load(rev/'results/raw_crossfold_exclusion.npz')['excluded'];ix=np.flatnonzero(~mask);ff=np.empty(len(ix),int)
   for k,(_,v) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(ix)),y[ix])):ff[v]=k
   assess(path,rec['macro_f1'],ids[ix],y[ix],ff)
  else:assess(path,rec['macro_f1'],expected_fold=savedfold.cleaner_group_fold.to_numpy() if arm=='cleaner_group' else fold)
  check(all(not f['hit_iteration_limit'] for f in rec['folds']),arm+' no LBFGS iteration cap')
  check(all(f['penalized_objective_gradient_max_abs']<=1e-6 for f in rec['folds']),arm+' recorded gradient <= 1e-6')
 ex=json.loads((rev/'results/exclusion_fixedfold_results.json').read_text());check(ex['status']=='completed','Fixed-fold exclusion completed');mask=np.load(rev/'results/raw_crossfold_exclusion.npz')['excluded'];ix=np.flatnonzero(~mask);assess(rev/'results/lbfgs_exclusion_fixedfold_oof.npz',ex['macro_f1'],ids[ix],y[ix],fold[ix]);check(all(not z['hit_iteration_limit'] and z['penalized_objective_gradient_max_abs']<=1e-6 for z in ex['folds']),'Fixed-fold exclusion convergence')
 for name in ['ijcvsplatex.cls','ijcvsplatex-num.bst','LogoIJCVSP.pdf','LogoIJCVSP.eps','booktabs.sty','fancyhdr.sty','lastpage.sty','multirow.sty','natbib.sty','sectsty.sty']:
  check((rev/'paper'/name).read_bytes()==(args.repo/'paper/iciev'/name).read_bytes(),name+' unchanged template asset')
 tex=(rev/'paper/main.tex').read_text();check(not re.search(r'TODO|AuthorTodo|naming versions|revision.s training budget|supplied in correspondence',tex),'No editorial placeholders in main source')
 (rev/'results/verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'checks':len(report['checks']),'scores':{k:v['macro_f1'] for k,v in report['probabilities'].items()}},indent=2))
if __name__=='__main__':main()
