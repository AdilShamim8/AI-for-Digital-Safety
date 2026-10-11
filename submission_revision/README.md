# LightBanglaHC audit revision package

- `paper/main.tex`: anonymous main manuscript in the supplied two-column ICIEV/IJCVSP class.
- `paper/main.pdf`: compiled main manuscript, with Supplements S1/S2 included.
- `paper/supplement.tex` and `paper/supplement.pdf`: detailed reproducibility supplement.
- `scripts/`: executable new-experiment and verification code.
- `results/`: actual new execution records, fold IDs and OOF probabilities.
- `author_replication.ipynb`: unexecuted notebook for an independent author rerun, with embedded scripts.
- `docs/REVISION_REPORT.md`: mismatch/change list and remaining factual requirements.
- `docs/SCORER_RECONSTRUCTION.md`: conditional arithmetic, excluded from headline results.

The main manuscript removes editorial prompts and placeholder strings. Missing ethics/permission records are described accurately rather than replaced with invented approvals. New executions were performed by the assistant; an author-independent rerun is not claimed. Review the report before certifying direct submission.

For Overleaf, use the dedicated `LightBanglaHC_Overleaf.zip`, select `main.tex`, and compile with pdfLaTeX. It includes the original class/style/logo assets, bibliography and source companion files. Select `supplement.tex` to build the detailed supplement. Publication volume/pages/acceptance dates are assigned by the publisher and suppressed during review.

For reproducibility, use the full repository ZIP. Its updated main paper is `paper/iciev/main.tex`. The original notebooks and CSVs are retained; `revision_2026-10-11/` records the earlier audit, and `submission_revision/` contains this follow-up. Do not infer a public data redistribution licence from the presence of a private author-delivery copy.

CMT main-paper uploads use PDF. ZIPs are for Overleaf/source/reproduction, or a supplementary field if the portal explicitly permits them.
