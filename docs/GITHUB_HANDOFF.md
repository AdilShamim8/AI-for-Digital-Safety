# GitHub publication and review

Repository: https://github.com/AdilShamim8/AI-for-Digital-Safety

Publication branch: lightbanglahc-major-revision-20261011

The branch is based on remote main a134892 and includes the measured paper
revision, both PDF options, the source ZIP, datasets, notebooks, audit outputs
and repository verification improvements. The previous GitHub plugin HTTP 403
response is retained in the dated audit report as historical provenance.

Checks: make verify; make verify-probabilities; make paper; make paper-anonymized.
The first command does not train models or need scientific Python dependencies.
The probability check uses the pinned LR environment and saved OOF arrays.

Review the draft PR before merging. Scientific and author TODOs are explicit;
repository publication does not constitute conference submission or approval.
The root repository.bundle and older source ZIP are historical records.
Use releases/LightBanglaHC_Revised_Overleaf.zip for the revised paper.
A delivery patch can be generated with git diff --binary main...HEAD; generated
patches are omitted from version control to avoid duplicating the repository.
