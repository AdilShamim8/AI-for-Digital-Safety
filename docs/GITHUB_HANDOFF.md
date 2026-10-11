# GitHub revision handoff

Repository: https://github.com/AdilShamim8/AI-for-Digital-Safety

The first audit revision was merged through PR #1 (main commit bb20034). The completed follow-up is prepared on `lightbanglahc-completed-audit-20261011`, based on that merged commit. It adds the actual reduced nested-stacking experiment, convergence and duplicate sensitivities, conditional bootstrap records, the current main paper and attached supplements.

Use `paper/iciev/main.tex`, `paper/iciev/main.pdf` and `releases/LightBanglaHC_Revised_Overleaf.zip`. Earlier archives and `repository.bundle` are historical records. New scientific records and replication scripts are under `submission_revision/`.

Checks: `make verify`, `make verify-probabilities`, `make verify-followup`, `make paper`, `make paper-supplement`. The standard-library check validates both manifests and packaged sources. Scientific checks use the pinned environment and retained probabilities; they do not retrain the base models.

Publishing this branch does not submit the paper to a conference. Exact ethics/data-permission wording and independent author replication remain factual author requirements. Review the current revision report before certifying submission.
