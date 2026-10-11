"""Run auditable comparisons sequentially to limit peak memory."""
import argparse, subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--jobs',type=int,default=1);a=p.parse_args();scripts=Path(__file__).resolve().parent
commands=[['lr_preprocessing_comparison.py','--train',str(a.repo/'data/herwill_2026/train.csv'),'--source',str(a.repo/'audit/updated_notebook_source.py'),'--out',str(a.out/'paired_saga'),'--wall-seconds','14400','--jobs',str(a.jobs)],['run_reduced_stack.py','--repo',str(a.repo),'--out',str(a.out),'--jobs',str(a.jobs)],['convergence_sensitivity.py','--repo',str(a.repo),'--out',str(a.out),'--jobs',str(a.jobs)],['exclusion_fixed_folds.py','--repo',str(a.repo),'--out',str(a.out),'--jobs',str(a.jobs)],['supporting_checks.py','--repo',str(a.repo),'--out',str(a.out),'--paired',str(a.out/'paired_saga')]]
for cmd in commands:subprocess.run([sys.executable,str(scripts/cmd[0]),*cmd[1:]],check=True)
