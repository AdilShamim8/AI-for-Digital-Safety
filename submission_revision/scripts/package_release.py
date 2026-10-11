"""Build Overleaf and complete author-delivery repository archives."""
import argparse,hashlib,json,re,shutil,zipfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--revision',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();out=a.out;out.mkdir(parents=True,exist_ok=True);stage=out/'AI-for-Digital-Safety';shutil.copytree(a.repo,stage,dirs_exist_ok=True,ignore=shutil.ignore_patterns('.git','__pycache__','*.aux','*.log','*.bbl','*.blg','*.fdb_latexmk','*.fls','*.spl'))
shutil.copytree(a.revision,stage/'submission_revision',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.aux','*.log','*.bbl','*.blg','*.fdb_latexmk','*.fls','*.spl'))
paper=stage/'paper/iciev'
for path in (a.revision/'paper').iterdir():
 if path.is_file() and path.suffix in ['.tex','.bib','.cls','.bst','.sty','.pdf','.eps']:shutil.copy2(path,paper/path.name)
(paper/'main_anonymized.tex').write_text('% Compatibility entry point: this is the same anonymous review manuscript.\n\\input{main}\n');shutil.copy2(paper/'main.pdf',paper/'main_anonymized.pdf')
(paper/'README.md').write_text('Compile main.tex with pdfLaTeX/BibTeX. This is the current anonymous review manuscript. Its ten pages include Supplements S1/S2. Compile supplement.tex for the detailed companion. The provided class/style/logo assets are unchanged. main_anonymized.tex is a compatibility alias of the same manuscript. See ../../submission_revision/docs/REVISION_REPORT.md for factual submission requirements.\n')
(stage/'docs/REVISION_CHECKLIST.md').write_text((a.revision/'docs/REVISION_REPORT.md').read_text())
(stage/'docs/SUBMISSION_GUIDE.md').write_text('Import LightBanglaHC_Overleaf.zip into Overleaf and compile main.tex with pdfLaTeX. Review the ten-page anonymous main PDF and companion supplement. Upload the main PDF in the current ICIEV2026 CMT submission: https://cmt3.research.microsoft.com/ICIEV2026/Submission/Index . Enter all three authors in the correct order in CMT; names/affiliations stay absent from the initial review PDF. Check the active track/deadline and supplement policy after login. This package is not certified for direct submission until actual ethics/data-permission wording and the independent author rerun are resolved. See submission_revision/docs/REVISION_REPORT.md.\n')
(stage/'docs/PULL_REQUEST_DESCRIPTION.md').write_text('Complete the reduced nonnested/nested stacking comparison and add solver, duplicate-split and fixed-prediction uncertainty sensitivities. Preserve the supplied template and historical data/notebooks, distinguish assistant-executed N evidence from historical R, attach S1/S2 and the full scientific ledger, and remove editorial placeholders from the current paper.\n\nValidation: manual rescoring/alignment, meta-only refit probability equivalence, convergence/gradient checks, unchanged template assets, ten-page main PDF and visually verified companion. Exact ethics/data permissions and independent author replication remain factual author requirements; no readiness certification or platform-score receipt is invented.\n')
(stage/'README.md').write_text((a.revision/'README.md').read_text()+'\nLedger keys starting with repository/ resolve from this repository root; remaining scientific ledger keys resolve from submission_revision/. Historical reports under revision_2026-10-11 are superseded by submission_revision/docs/REVISION_REPORT.md.\n')
with (stage/'Makefile').open('a') as f:f.write('\n.PHONY: paper-supplement verify-followup\npaper-supplement:\n\tcd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error supplement.tex\nverify-followup:\n\tpython3 submission_revision/scripts/verify_followup.py --repo . --revision submission_revision\n')
shutil.copy2(a.revision/'paper/main.pdf',out/'LightBanglaHC_Audit.pdf');shutil.copy2(a.revision/'paper/supplement.pdf',out/'LightBanglaHC_Supplement.pdf');shutil.copy2(a.revision/'docs/REVISION_REPORT.md',out/'Revision_Report.md')
legacy_author=paper/'author-details.tex'
if legacy_author.exists():
 (stage/'archives/older-review').mkdir(exist_ok=True);shutil.move(str(legacy_author),str(stage/'archives/older-review/author-details.tex'))
sourcefiles=[p for p in paper.iterdir() if p.is_file() and p.suffix in ['.tex','.bib','.cls','.bst','.sty','.pdf','.eps']]+[paper/'README.md']
with zipfile.ZipFile(out/'LightBanglaHC_Overleaf.zip','w',zipfile.ZIP_DEFLATED) as z:
 for pth in sorted(sourcefiles):z.write(pth,pth.name)
shutil.copy2(out/'LightBanglaHC_Overleaf.zip',stage/'releases/LightBanglaHC_Revised_Overleaf.zip')
manifest={'scope':'Delivered repository payload; this manifest itself excluded','files':[]}
for pth in sorted(stage.rglob('*')):
 if pth.is_file() and pth!=stage/'audit/manifest.json':manifest['files'].append({'path':str(pth.relative_to(stage)),'bytes':pth.stat().st_size,'sha256':hashlib.sha256(pth.read_bytes()).hexdigest()})
(stage/'audit/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(out/'AI-for-Digital-Safety_Updated.zip','w',zipfile.ZIP_DEFLATED) as z:
 for pth in sorted(stage.rglob('*')):
  if pth.is_file():
   if re.search(rb'ghp_[A-Za-z0-9]{20,}',pth.read_bytes()):raise ValueError('Credential pattern found; release blocked without printing it.')
   z.write(pth,'AI-for-Digital-Safety/'+str(pth.relative_to(stage)))
for name in ['LightBanglaHC_Overleaf.zip','AI-for-Digital-Safety_Updated.zip']:
 with zipfile.ZipFile(out/name) as z:assert z.testzip() is None
print(json.dumps({'files':[{'name':p.name,'bytes':p.stat().st_size} for p in sorted(out.iterdir()) if p.is_file()],'repository_files':len(manifest['files'])+1},indent=2))
