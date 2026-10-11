"""Deterministic duplicate checks and conditional paired-prediction bootstrap."""
import argparse, hashlib, json, sys
from pathlib import Path
import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold
from lr_preprocessing_comparison import load_rules

def f1_from_cm(c):
    tp=np.diagonal(c,axis1=-2,axis2=-1)
    den=c.sum(-1)+c.sum(-2)
    return np.divide(2*tp,den,out=np.zeros_like(tp,dtype=float),where=den!=0).mean(-1)

def stats(texts,y,fold):
    df=pd.DataFrame({'text':texts,'y':y,'fold':fold}); groups=df.groupby('text',sort=False).agg(n=('y','size'),labels=('y','nunique'),folds=('fold','nunique'))
    dup=groups.n>1; cross=dup&(groups.folds>1);conflict=dup&(groups.labels>1)
    return {'groups':int(dup.sum()),'rows':int(groups.loc[dup,'n'].sum()),'extra_rows':int((groups.loc[dup,'n']-1).sum()),'cross_fold_groups':int(cross.sum()),'cross_fold_rows':int(groups.loc[cross,'n'].sum()),'cross_fold_row_percent':float(100*groups.loc[cross,'n'].sum()/len(y)),'conflicting_groups':int(conflict.sum()),'conflicting_rows':int(groups.loc[conflict,'n'].sum()),'conflicting_row_percent':float(100*groups.loc[conflict,'n'].sum()/len(y)),'conflicting_cross_fold_groups':int((conflict&cross).sum())}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--paired',type=Path);args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(args.repo/'data/herwill_2026/train.csv');y=df.y.to_numpy();raw=df.text.fillna('').astype(str).tolist();clean=[load_rules(args.repo/'audit/updated_notebook_source.py')['clean'](t) for t in raw] if False else None
    rules=load_rules(args.repo/'audit/updated_notebook_source.py');clean=[rules['clean'](t) for t in raw];fold=np.empty(len(y),int)
    for k,(_,v) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y)):fold[v]=k
    groupfold=np.empty(len(y),int)
    for k,(_,v) in enumerate(StratifiedGroupKFold(3,shuffle=True,random_state=42).split(np.zeros(len(y)),y,groups=pd.factorize(pd.Series(clean),sort=False)[0])):groupfold[v]=k
    pd.DataFrame({'id':df.id,'y':y,'stratified_fold':fold,'cleaner_group_fold':groupfold}).to_csv(args.out/'duplicate_folds.csv',index=False)
    raw_frame=pd.DataFrame({'text':raw,'fold':fold});crossraw=raw_frame.groupby('text').fold.nunique();excluded=raw_frame.text.isin(crossraw[crossraw>1].index).to_numpy()
    np.savez_compressed(args.out/'raw_crossfold_exclusion.npz',id=df.id.to_numpy(),excluded=excluded)
    result={'evidence':'N: assistant executed; not an author-independent replication','raw':stats(raw,y,fold),'notebook_cleaner':stats(clean,y,fold),'cleaner_group_split':stats(clean,y,groupfold),'excluded_raw_crossfold_rows':int(excluded.sum()),'retained_rows':int((~excluded).sum()),'group_fold_class_supports':[[int(np.sum((groupfold==k)&(y==c))) for c in range(3)] for k in range(3)]}
    old=args.paired or args.repo/'revision_2026-10-11/audit/lr_comparison';a=np.load(old/'global_oof.npz');b=np.load(old/'within_fold_oof.npz');assert np.array_equal(a['id'],df.id) and np.array_equal(a['y'],y) and np.array_equal(a['fold'],fold) and all(np.array_equal(a[k],b[k]) for k in ['id','y','fold']);pa=a['prob'].argmax(1);pb=b['prob'].argmax(1);bins=y*9+pa*3+pb;freq=np.bincount(bins,minlength=27).reshape(3,9);rng=np.random.default_rng(42);reps=5000
    sampled=np.stack([rng.multinomial(int(freq[c].sum()),freq[c]/freq[c].sum(),size=reps) for c in range(3)],axis=1).reshape(reps,3,3,3)
    delta=f1_from_cm(sampled.sum(3))-f1_from_cm(sampled.sum(2));observed=float(f1_score(y,pa,average='macro')-f1_score(y,pb,average='macro'))
    result['bootstrap']={'conditioning':'Fixed OOF predictions; training is not resampled. Does not resolve overlapping training folds or user/thread dependence.','global_macro_f1':float(f1_score(y,pa,average='macro')),'fold_macro_f1':float(f1_score(y,pb,average='macro')),'difference':observed,'stratified_row_replicates':reps,'seed':42,'stratified_row_percentile95':np.quantile(delta,[.025,.975]).tolist()}
    codes,_=pd.factorize(pd.Series(raw),sort=False);ng=int(codes.max()+1);mat=sp.csr_matrix((np.ones(len(y),dtype=np.int64),(codes,bins)),shape=(ng,27));cluster_d=[];rng=np.random.default_rng(42)
    for start in range(0,2000,32):
        size=min(32,2000-start);idx=rng.integers(0,ng,size=(size,ng));weights=np.stack([np.bincount(row,minlength=ng) for row in idx]);ct=np.asarray(weights@mat).reshape(size,3,3,3);cluster_d.extend((f1_from_cm(ct.sum(3))-f1_from_cm(ct.sum(2))).tolist())
    result['bootstrap'].update({'exact_raw_text_cluster_replicates':2000,'exact_raw_text_cluster_percentile95':np.quantile(cluster_d,[.025,.975]).tolist(),'cluster_unit':'Unique exact raw text; conflicting labels remain together; corpus size can change across resamples.'})
    newfold=np.empty(int((~excluded).sum()),int);retained=np.flatnonzero(~excluded)
    for k,(_,v) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(np.zeros(len(retained)),y[retained])):newfold[v]=k
    result['raw_excluded_resplit_duplicates']=stats([raw[i] for i in retained],y[retained],newfold)
    result['file_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in [args.repo/'data/herwill_2026/train.csv',args.repo/'audit/updated_notebook_source.py',old/'global_oof.npz',old/'within_fold_oof.npz']}
    (args.out/'supporting_checks.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
