# Evidence ledger: updated notebook

Canonical source: `notebooks/ai-for-digital-safety-101.ipynb`. The exact current
Drive bytes match the attached snapshot. `updated_notebook_source.py` is its
verbatim code-cell text (971 lines); source line numbers below refer to that file.
Full file digests and origins are in `manifest.json`. No training was run.

| Claim | Source / output | Finding and limit |
| --- | --- | --- |
| Task and supports | Lines 63–112; smaller raw CSVs; output stream | S/R/D: 3 classes, 3 folds, 47,817 / 11,955 rows; supports 23,756 / 18,163 / 5,898. No input hashes recorded during historical training. |
| Global class weights | Lines 104–112 | S: computed before folds; affect LR/SVC/SGD/Meta-LR and LGB sample weights. Impact not quantified. |
| Cleaning and cue rules | Lines 118–255 | S: 73 explicit strings, 25 subtle entries; substring presence. No validated language or intent measurement. |
| Global feature fitting | Lines 291–342 | S/R: four widths 100,000 / 80,000 / 50,000 / 105; total 230,105. Fitted arrays and versions absent. |
| Numerical features | Lines 350–388 | S/R: 20 fixed features; LGB input 230,125. Others use TF-IDF only. |
| Base fitting / calibration | Lines 404–551 | S: six candidates, three fits each; test averages; isotonic CV=2 for SVC/CNB/SGD. Internal fitted object counts depend on missing versions. |
| LGB early stopping | Lines 527–548; output | S/R: assessment labels select stopping; rounds 149 / 173 / 182. No bias magnitude inferred. |
| Meta dependency | Lines 573–595 | S: 18-feature matrix reused across meta folds; other rows' base fits include the meta validation labels. |
| Learned ensemble weights | Lines 618–620 | S: normalized squared pooled F1 across seven candidates. Not a prespecified average. |
| Threshold and candidate selection | Lines 648–697 | S/R: 900 pairs per ensemble; unadjusted pair omitted; four variants compared on pooled labels; weighted selected. |
| Pooled/fold scores | First output stream | R: weighted .5314; LR_C3 .5221. No row-level OOF arrays supplied. |
| Confusion matrix | Embedded figure; extracted original PNG | R: [[16464,6331,961],[7502,9039,1622],[1360,2292,2246]]. Integer transcription visually checked. |
| Metric reconstruction | `verification.json` | A: F1 .5314177984731835, accuracy .5803166237948847. Internal consistency, not prediction replay. |
| Selected predictor | Lines 618–620, 683–697 | S: six base averages plus Meta-LR average, weighted argmax. Identity module absent from path. |
| Identity profile | Lines 710–737; output | S/R: separate no-parameter identity; count initialized/defaulted to zero; successful THOP branch line absent. Final zero does not prove successful profiling. |
| Fractional NOP | Lines 919–928; output | S/R: round(F1/2.9,3)=.183. Target-derived denominator, not parameter cardinality. |
| Zero-file inconsistency | Lines 890–929; final report | S/R: duplicate guard skips zero entries, although summary recommends a zero filename. Save text is not platform acceptance. |
| Updated test counts | Second output stream | R: 6,414 / 4,401 / 1,140, declared NOP .183. Full generated CSVs not supplied. |
| Supplied older CSV | `data/herwill_2026/submission.csv` | D: 5,501 / 4,139 / 2,315, NOP39, IDs/order match. Different version from canonical notebook. |
| LR scalar inventory | Configs, input routing, recorded width | A: six base LR fits 4,141,908 scalars; three Meta-LR fits 171. Excludes other models/state; not measured total NOP or memory. |
| Timing | Output sections and metadata | R/A: LR+LR+LGB 9,029.5s; metadata 9,142.89s; 25–35min summary contradicted. Not a controlled benchmark. |
| Hardware/runtime | Metadata versus output | S/R: GPU-enable flag false but output cuda; Python3.12.12; package versions missing. |
| Exact text overlap | Smaller raw CSVs | D: 621 train repeats, 54 test repeats, 254 distinct shared texts. No near-duplicate/group or split-effect analysis. |
| Older versions | Larger CSVs, former notebook and manuscripts | Separate historical resources. Do not combine their scores/dimensions/NOP with current run. |
| Scoring contract | Pasted description / supplied DOCX | Conflicting weighted-log and ratio expressions; original formula image/log base/scorer absent. Notebook ratio is local projection. |
| Licensing | Supplied DOCX | Describes HerWILL and CC BY-NC-ND4.0; original permission records and extra-row terms unverified. Root MIT does not relicense data. |
| Authorship | User confirmation | Shamim Hasan first; two additional authors intended. Names/emails/affiliations, approval and disclosures missing. |

Evidence types: S source, R recorded output, D direct data check, A arithmetic,
X external unverified, P prospective. Retained notebook instructions about
fractional NOP are preserved as evidence; this package does not endorse them.
No new prediction labels, training result, platform submission, or claimed rank
was created.
