"""Generate manuscript numbers/ledger only after actual execution completes."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--revision',type=Path,required=True);a=p.parse_args();r=a.revision;out=r/'paper';s=json.loads((r/'results/reduced_stack_results.json').read_text());c=json.loads((r/'results/convergence_results.json').read_text());d=json.loads((r/'results/supporting_checks.json').read_text());e=json.loads((r/'results/exclusion_fixedfold_results.json').read_text());assert s['status']==c['status']==e['status']=='completed'
f=lambda x:f'{x:.6f}'
vals={'RowCI':'['+', '.join(map(f,d['bootstrap']['stratified_row_percentile95']))+']','ClusterCI':'['+', '.join(map(f,d['bootstrap']['exact_raw_text_cluster_percentile95']))+']','CleanDuplicateGroups':str(d['notebook_cleaner']['groups']),'CleanCrossGroups':str(d['notebook_cleaner']['cross_fold_groups']),'CleanConflictGroups':str(d['notebook_cleaner']['conflicting_groups']),'NonNested':f(s['nonnested_macro_f1']),'Nested':f(s['nested_macro_f1']),'StackDifference':f(s['nonnested_minus_nested']),'LBGlobal':f(c['arms']['global']['macro_f1']),'LBFold':f(c['arms']['within_fold']['macro_f1']),'GroupFone':f(c['arms']['cleaner_group']['macro_f1']),'ExcludedFone':f(e['macro_f1'])}
(out/'new-evidence.tex').write_text('% Generated from completed execution records; N evidence.\n'+'\n'.join('\\newcommand{\\'+k+'}{'+v+'}' for k,v in vals.items())+'\n')
lines=[r'\begin{table*}[t]',r'\small\centering',r'\caption{LBFGS sensitivity diagnostics (N). The maximum absolute gradient is for the class-weight-normalized penalized objective. No fit reaches its 2,000-iteration cap.}',r'\begin{tabular}{lrrr}',r'\toprule',r'Arm & Pooled macro-F1 & Iterations (folds 1/2/3) & Largest objective gradient \\',r'\midrule']
labels={'global':'Global TF-IDF','within_fold':'Fold-fitted TF-IDF','cleaner_group':'Cleaner-group split','raw_excluded':'Raw cross-fold rows excluded'}
for k,rec in c['arms'].items():
 assert all(not z['hit_iteration_limit'] for z in rec['folds']);n='/'.join(str(z['n_iter'][0]) for z in rec['folds']);grad=max(z['penalized_objective_gradient_max_abs'] for z in rec['folds']);assert grad<=1e-6
 lines.append(labels[k]+' & '+f(rec['macro_f1'])+' & '+n+' & '+f'{grad:.3e}'+r' \\')
n='/'.join(str(z['n_iter'][0]) for z in e['folds']);grad=max(z['penalized_objective_gradient_max_abs'] for z in e['folds']);assert grad<=1e-6 and all(not z['hit_iteration_limit'] for z in e['folds']);lines.append('Exclusion, original folds & '+f(e['macro_f1'])+' & '+n+' & '+f'{grad:.3e}'+r' \\')
lines.extend([r'\bottomrule',r'\end{tabular}',r'\end{table*}']);(out/'convergence-table.tex').write_text('\n'.join(lines)+'\n')
items={}
for root in [r/'scripts',r/'results']:
 for path in sorted(root.rglob('*')):
  if path.is_file() and '__pycache__' not in path.parts and path.name not in ['artifact_ledger.json']:
   items[str(path.relative_to(r))]=hashlib.sha256(path.read_bytes()).hexdigest()
for rel in ['data/herwill_2026/train.csv','data/herwill_2026/test.csv','audit/updated_notebook_source.py','notebooks/ai-for-digital-safety-101.ipynb','data/herwill_2026/submission_updated.csv','revision_2026-10-11/audit/lr_comparison/global_oof.npz','revision_2026-10-11/audit/lr_comparison/within_fold_oof.npz']:
 items['repository/'+rel]=hashlib.sha256((a.repo/rel).read_bytes()).hexdigest()
items['author_replication.ipynb']=hashlib.sha256((r/'author_replication.ipynb').read_bytes()).hexdigest();(r/'results/artifact_ledger.json').write_text(json.dumps({'algorithm':'SHA-256','scope':'Scientific inputs, scripts, predictions and diagnostics; generated PDF/ledger files excluded to avoid circular hashes.','files':items},indent=2)+'\n')
selected=[('Training CSV','repository/data/herwill_2026/train.csv'),('Updated notebook source','repository/audit/updated_notebook_source.py'),('Initial global LR probabilities','repository/revision_2026-10-11/audit/lr_comparison/global_oof.npz'),('Initial fold LR probabilities','repository/revision_2026-10-11/audit/lr_comparison/within_fold_oof.npz'),('Nonnested stack probabilities','results/reduced_nonnested_oof.npz'),('Nested stack probabilities','results/reduced_nested_oof.npz'),('Reduced-stack execution record','results/reduced_stack_results.json'),('Convergence record','results/convergence_results.json'),('Duplicate/bootstrap checks','results/supporting_checks.json'),('Reduced-stack script','scripts/run_reduced_stack.py')]
lines=[r'\begin{table*}[t]',r'\small\centering',r'\caption{Selected full SHA-256 digests. The JSON ledger contains the complete scientific inventory.}',r'\begin{tabularx}{\textwidth}{P{4cm}X}',r'\toprule',r'Artifact & SHA-256 \\',r'\midrule']
for label,key in selected:lines.append(label+' & '+r'\texttt{'+items[key][:32]+r'}\allowbreak\texttt{'+items[key][32:]+'}'+r' \\')
lines.extend([r'\bottomrule',r'\end{tabularx}',r'\end{table*}']);(out/'ledger-table.tex').write_text('\n'.join(lines)+'\n')
print(json.dumps({'macros':vals,'scientific_ledger_files':len(items)},indent=2))
