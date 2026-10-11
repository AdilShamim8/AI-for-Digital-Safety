# LightBanglaHC audit: major revision

Both IJCVSP-template review PDFs are 10 pages, including references:

- Named case A: paper/iciev/main.tex and main.pdf.
- Public-datathon case B: paper/iciev/main_anonymized.tex and main_anonymized.pdf.

**Status: measured LR revision; author facts and nested stacking still need completion.**

Full-data LR_C3 macro-F1 is 0.5220608957 with global TF-IDF and 0.5188715616
with training-fold TF-IDF (difference 0.0031893341). Identical seed-42 folds
and global class weights are fixed. All six fits reached max_iter=2000;
these are training-budget results, not converged optima. Historical ensemble
F1 0.5314 and coefficient subtotal 4,141,908 remain unchanged. No corrected
full-ensemble result is inferred.

Regenerated folds contain 308 exact-text groups spanning folds (771 rows).
52 repeated groups have conflicting labels (130 rows); 36 also span folds.
The observed weighted-minus-uniform gain of 0.0008 is not a leakage-bias bound.

## Revision contents

- revision_2026-10-11/docs/REVISION_REPORT.md: mismatch list, results, pending protocols, full paper text, change log, author checklist and references.
- revision_2026-10-11/audit/lr_comparison/: completed records and paired OOF arrays.
- revision_2026-10-11/scripts/: evidence checks and runnable LR comparison.
- revision_2026-10-11/docs/STACKING_PROTOCOL.md: matched non-nested/nested design; no nested score invented.
- revision_2026-10-11/LightBanglaHC_Revision_Rerun.ipynb: new unexecuted companion notebook.
- docs/GITHUB_HANDOFF.md: publication branch and review instructions. The earlier plugin write failure is documented in the historical revision report.

## Data and version boundaries

| Record | Role |
|---|---|
| data/herwill_2026/ | Active 47,817/11,955-row three-class data. |
| data/herwill_2026/submission_updated.csv | New CSV: matching test IDs/order, class totals 6,414/4,401/1,140, constant parameters=0.183. Audited export, not a validated count or proof of platform upload. |
| data/herwill_2026/submission.csv | Older NOP-39 export, unchanged. |
| data/four_class_version/ | Separate 54,817/14,955-row four-class record; not used for the active paper. |
| notebooks/ai-for-digital-safety-101.ipynb | Canonical updated notebook, preserved byte-for-byte. |
| Other notebooks and archives/ | Historical records preserved. |

Earlier TinyLinear/NOP-39/four-class history is in Supplement S1. The unchanged
root repository.bundle is historical and predates this revision. Use current
files or the supplied revision patch. Original fitted states/OOF rows remain
unavailable; new LR arrays do not recover them.

## Verify and build

```sh
make verify
# Requires the pinned LR dependencies:
make verify-probabilities
make paper
make paper-anonymized
```

The default verification runs without training or scientific Python dependencies.
`verify-probabilities` also recomputes both pooled scores and checks row/fold alignment.
Install the pinned packages in revision_2026-10-11/scripts/requirements-lr.txt first.

For B, compile paper/iciev/main_anonymized.tex with pdfLaTeX/BibTeX. For
Overleaf, import the revised source ZIP and choose the main file. Supplied
class, bibliography style and assets are unchanged. New training has a
documented new environment; historical package versions were not recovered.

## Before submission

Complete every TODO-AUTHOR field, select naming, obtain all-author approval,
provide actual funding/ethics/permissions/prior-manuscript facts and an
anonymous artifact URL, and run the pending matched stacking comparison
or resolve the narrower scope with the authors/editor. See
docs/REVISION_CHECKLIST.md. Platform scores/runtime/hardware remain
author reports (X).

ICIEV initial review requests an anonymous PDF. Enter all three authors in CMT;
Shamim Hasan is the confirmed first author and two coauthors remain unknown.
Use an existing submission if one exists. No portal upload occurred here.

Portal: https://cmt3.research.microsoft.com/ICIEV2026/Submission/Index

Instructions: https://cennser.org/ICIEV/paper-submission.html

The root MIT license is preserved; it does not relicense third-party data or
templates. See data/ATTRIBUTION.md. Original CSVs/notebooks were not edited
or deduplicated. Public repository files are not anonymous review supplements.
