# LightBanglaHC harmful-content classification audit

This repository preserves the supplied HerWILL notebooks and datasets and records a retrospective audit of evaluation, inference and parameter accounting. The current paper uses the supplied ICIEV/IJCVSP two-column template.

## Current paper and reproduction files

- [Main paper source](paper/iciev/main.tex) and [ten-page PDF](paper/iciev/main.pdf), including Supplements S1/S2.
- [Detailed supplement source](paper/iciev/supplement.tex) and [three-page PDF](paper/iciev/supplement.pdf).
- [Overleaf upload ZIP](releases/LightBanglaHC_Revised_Overleaf.zip): choose `main.tex` and pdfLaTeX; choose `supplement.tex` for the companion.
- [Revision report](submission_revision/docs/REVISION_REPORT.md): mismatches, changes, evidence limits and remaining author requirements.
- [Author replication notebook](submission_revision/author_replication.ipynb): intentionally unexecuted; embeds the experiment scripts for an independent rerun.
- [Scientific results](submission_revision/results/) and [SHA-256 ledger](submission_revision/results/artifact_ledger.json): saved folds, probabilities, diagnostics and actual execution records.

`notebooks/ai-for-digital-safety-101.ipynb` is the updated historical notebook. Original CSVs and notebooks are retained unchanged. `revision_2026-10-11/` and older archives preserve earlier versions; their editorial reports are superseded by the current revision report. `submission_revision/paper/` retains the source copy of the current paper; `paper/iciev/` is the submission entry point.

## Results and evidence boundaries

The source-budget LR comparison scored 0.522061 with globally fitted TF-IDF and 0.518872 with fold-fitted TF-IDF. All six SAGA fits reached the iteration cap. The LBFGS sensitivity scored 0.523143 and 0.521393, respectively, with all fits below the cap and recorded objective-gradient checks. The reduced nonnested and nested stacks scored 0.517144 and 0.515690. These are controlled comparisons of the documented audit configurations, not a replay of the full historical ensemble.

New experiments carry evidence tag N and were executed by the assistant. The repository does not claim independent author replication. The small weighted-versus-uniform historical difference is not an upper bound on evaluation bias. Platform scores have no supplied receipt and are excluded from the main results; [conditional scorer arithmetic](submission_revision/docs/SCORER_RECONSTRUCTION.md) is kept separate.

## Verify without retraining

From the repository root:

```bash
make verify
python3 -m pip install -r submission_revision/scripts/requirements-audit.txt
make verify-probabilities
make verify-followup
```

`make verify` uses only Python's standard library and checks source citations, original data, ZIP contents, the complete payload manifest and the scientific ledger. The two scientific checks rescore retained predictions; `verify-followup` also refits the small meta models and checks saved probability equivalence and convergence diagnostics. They do not retrain TF-IDF base models.

Build the supplied sources with pdfLaTeX/BibTeX through latexmk:

```bash
make paper
make paper-supplement
```

`make paper-anonymized` is a compatibility entry point for the same anonymous manuscript. Publication volume, pages and dates are assigned by the publisher and suppressed during review.

## Independently rerun the experiments

Use the replication notebook or, in the pinned scientific environment:

```bash
python3 submission_revision/scripts/run_all.py --repo . --out independent_replication_results --jobs 1
```

The runner executes comparisons sequentially and writes to a separate directory. Keep the saved historical and assistant-run results intact; compare the independently generated records before certifying replication. Training takes substantial time and memory. No Kaggle run or screenshot is fabricated.

## Submission and third-party material

Follow [the submission guide](docs/SUBMISSION_GUIDE.md). Enter all three authors accurately in CMT; the initial review PDF is anonymous. Exact ethics/data-permission wording and independent author replication remain unresolved author requirements. The package is not certified for direct submission.

Read [dataset attribution](data/ATTRIBUTION.md). The repository's MIT license does not grant rights to third-party datasets or template material. Dataset redistribution permission is not established by the presence of these files.

Ledger keys starting with `repository/` resolve from the repository root; other scientific ledger keys resolve from `submission_revision/`. Generated LaTeX intermediates and independent rerun outputs are excluded from Git.
