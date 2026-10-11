"""Reproduce direct CSV, regenerated-fold and rounded-weight checks."""
import hashlib,json
from pathlib import Path
import numpy as np,pandas as pd,sklearn
from sklearn.model_selection import StratifiedKFold
from sklearn.utils.class_weight import compute_class_weight

def main():
    base=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parents[1]/'audit';out.mkdir(exist_ok=True)
    path=base/'data/herwill_2026/train.csv';tr=pd.read_csv(path);te=pd.read_csv(base/'data/herwill_2026/test.csv');su=pd.read_csv(out/'updated_submission.csv')
    fold=np.empty(len(tr),int);local=[];global_w=compute_class_weight('balanced',classes=np.arange(3),y=tr.y)
    for a,(fit,val) in enumerate(StratifiedKFold(3,shuffle=True,random_state=42).split(tr.id,tr.y)):
        fold[val]=a;local.append(compute_class_weight('balanced',classes=np.arange(3),y=tr.y.iloc[fit]).tolist())
    tr['fold']=fold
    groups=tr.groupby('text',sort=False,dropna=False).agg(rows=('id','size'),folds=('fold','nunique'),labels=('y','nunique'))
    d=groups[groups.rows>1];c=d[d.folds>1];f=d[d.labels>1]
    scores=np.array([.5169,.5221,.4824,.4391,.4691,.5160,.5218]);weights=scores*scores/(scores*scores).sum()
    original=json.loads((base/'audit/verification.json').read_text())
    r={'sklearn_version':sklearn.__version__,'train_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'duplicate_groups':len(d),'duplicate_group_rows':int(d.rows.sum()),'repeats_beyond_first':int((d.rows-1).sum()),'cross_fold_duplicate_groups':len(c),'cross_fold_duplicate_rows':int(c.rows.sum()),'cross_fold_repeats_beyond_first':int((c.rows-1).sum()),'conflicting_label_groups':len(f),'conflicting_label_rows':int(f.rows.sum()),'cross_fold_conflicting_groups':int(((d.labels>1)&(d.folds>1)).sum()),'fold_supports':tr.groupby('fold').y.value_counts().unstack().values.tolist(),'submission':{'shape':list(su.shape),'columns':list(su.columns),'counts':{int(k):int(v) for k,v in su.y_pred.value_counts().items()},'parameters':su.parameters.unique().tolist(),'ids_match_test':bool(su.id.equals(te.id)),'sha256':hashlib.sha256((out/'updated_submission.csv').read_bytes()).hexdigest()},'ensemble':{'rounded_scores':scores.tolist(),'weights_rounded_input':weights.tolist(),'uniform':1/7,'max_absolute_weight_deviation':float(abs(weights-1/7).max()),'observed_gap_rounded':.5314-.5306},'global_class_weights':global_w.tolist(),'regenerated_fold_training_class_weights':local,'max_relative_class_weight_difference':float(np.max(np.abs(np.asarray(local)/global_w-1))),'max_relative_class_weight_difference_percent':float(np.max(np.abs(np.asarray(local)/global_w-1))*100),'arithmetic_unchanged':original['manuscript_arithmetic'],'confusion_matrix':original['manuscript_arithmetic']['confusion_matrix']}
    assert r['repeats_beyond_first']==621
    assert r['submission']['shape']==[11955,3] and r['submission']['ids_match_test']
    assert sorted(su.y_pred.unique().tolist())==[0,1,2] and su.parameters.unique().tolist()==[.183]
    (out/'checks.json').write_text(json.dumps(r,indent=2))
    tr[['id','y','fold']].to_csv(out/'regenerated_folds.csv',index=False)
    print(json.dumps(r,indent=2))

if __name__=='__main__':main()
