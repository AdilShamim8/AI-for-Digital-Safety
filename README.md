# LightBanglaHC: AI for Digital Safety

This repository packages the supplied paper, datasets, notebook, competition
details, earlier archives, and an evidence audit for an ICIEV 2026 submission.
The anonymous manuscript is `paper/iciev/main.tex`; its compiled PDF is
`paper/iciev/main.pdf` (10 pages including references, IJCVSP two-column style).

**Status: updated notebook audited; formatting complete; author and submission evidence still require confirmation.**
The paper audits the updated three-class, three-fold execution record.
It does not demonstrate a new algorithm, predictive superiority, competition
victory, or a measured deployment advantage. Authors should resolve the
submission blockers in `docs/REVISION_CHECKLIST.md` before uploading it.

## Choose the correct record

| Resource | Training / test rows | Classes | Role |
| --- | --- | --- | --- |
| `data/herwill_2026/` | 47,817 / 11,955 | 0–2 | Verbatim extraction from the 2026 ZIP; matches the paper and supplied submission. |
| `data/four_class_version/` | 54,817 / 14,955 | 0–3 | Separate loose Drive CSVs; preserve as a different version. IDs contain duplicates. |
| `notebooks/AI_for_Digital_Safety_Notebook.ipynb` | 54,817 / 14,955 in outputs | Four | Supplied notebook, preserved unchanged; reports a 68-parameter head and selects SVC. |
| `notebooks/ai-for-digital-safety-101.ipynb` | 47,817 / 11,955 in outputs | Three | Canonical updated notebook: three folds, weighted ensemble F1 0.5314, separate identity count 0, exported fraction 0.183. |
| Earlier three-class paper | 47,817 / 11,955 | Three | Reports TinyLinear F1 0.5295 and NOP 39; matching execution notebook not supplied. |

The smaller CSVs are exact trailing tabular subsets of the larger files.
That relationship does not make the four-class notebook evidence of the
three-class scores. The canonical updated notebook uses the smaller three-class dataset but a different pipeline from the older TinyLinear paper. No historical run was replayed.

The supplied `submission.csv` matches the smaller test/sample IDs in order,
contains valid labels, and repeats NOP 39. These checks establish local format
consistency, not Kaggle acceptance or compliance with its counting rules.
Its NOP-39 labels/counts differ from the updated notebook output. The updated generated CSVs were not supplied; this file is preserved as an earlier version, not relabeled as the current submission. Do not use it with the larger test file.

## Contents

- `paper/iciev/`: revised anonymous paper, bibliography, vector figure and template dependencies.
- `releases/LightBanglaHC_ICIEV_source.zip`: complete paper build bundle.
- `data/`: both supplied dataset versions and the supplied three-class submission.
- `notebooks/`: unchanged shared notebook, including retained outputs.
- `archives/`: all shared ZIPs, the separate 2024 dataset, and original uploaded paper/template files.
- `docs/`: supplied competition document, submission steps and full revision checklist.
- `audit/`: full-file manifest, claim ledger, verification report and exact source diff.
- `scripts/verify_artifacts.py`: repeatable, read-only artifact and arithmetic checks.

## Verify and build

The artifact checks use Python's standard library and do not train models:

```sh
python3 scripts/verify_artifacts.py
```

Install a LaTeX distribution with `latexmk`, pdfLaTeX, BibTeX, and the packages
used in `main.tex`. Then:

```sh
make paper
```

For Overleaf, upload the source ZIP and select `main.tex`. A color-only fallback
handles the template's unused legacy `pstcol` dependency. The supplied class
and bibliography style are unchanged. There is no validated historical training environment for the updated run; current packages must not be presented as its original environment. The canonical notebook retains invalid fractional NOP exports for audit provenance; the repository does not endorse them as measured parameter counts.

## Submission and attribution

ICIEV initial review is double-blind and requests PDF. Upload only the anonymous
`paper/iciev/main.pdf`; enter all three authors and accurate emails in CMT.
Shamim Hasan is the confirmed first author; the other author details remain
unsupplied. The public repository and original archives identify their owner
and are not anonymous review supplements.

Portal: https://cmt3.research.microsoft.com/ICIEV2026/Submission/Index

Instructions: https://cennser.org/ICIEV/paper-submission.html

The existing root MIT license is preserved. It must not be read as relicensing
third-party data or conference templates. The supplied competition details
document attributes the 2026 data to HerWILL and lists CC BY-NC-ND 4.0; see
`data/ATTRIBUTION.md`. Original data files have not been edited or deduplicated.
Earlier drafts contain superseded claims and are archived for provenance.
