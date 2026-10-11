# S1. Version history and external records

This supplement preserves provenance that was moved out of the main paper.
It is an author handoff and contains identifying links. Prepare a separate
anonymous review supplement before uploading it for double-blind review.

## Canonical current record

- Notebook: `notebooks/ai-for-digital-safety-101.ipynb`.
- Snapshot SHA-256: `1dcbb4150a296155e713fdf51af349d151c874c916190edee29a27931c587f25`.
- Source SHA-256: `b1bf6978a045cb0abed587b7f2924095432098173497e4a6c29d7014588ebf4d`.
- Training/test rows: 47,817 / 11,955; three classes; three shuffled seed-42 folds.
- Four TF-IDF branches: 230,105 columns; LightGBM adds 20 numerical columns.
- Six base candidates plus Meta-LR; selected weighted ensemble macro-F1 0.5314.
- Current Drive notebook source, verified provider URL:
  https://drive.google.com/file/d/11-Cj5i_WoMq3APdwO41M0tdtS3Lk-ck5/view?usp=drivesdk
- Current repository: https://github.com/AdilShamim8/AI-for-Digital-Safety

## Updated submission now supplied

Drive folder listing revealed a new `submission.csv`, size 165,183 bytes,
which was retrieved and checked in this revision. Source:
https://drive.google.com/file/d/1BmDkolnPwhN4NImy7hpgMDZysf3qqU5a/view?usp=drivesdk

SHA-256: `2282e24132cf84e75dafe15a50ccba79b5ee9ce96e3755d3e2443deb34e3c4a2`.
Its 11,955 rows and ID order match the three-class test set. Counts are
6,414 Explicit, 4,401 Subtle and 1,140 Neutral; its constant `parameters` field
is 0.183. These match retained aggregate export output. Without historical
row-level probabilities/fitted states, this is consistency evidence, not
authentication of model provenance or of the file uploaded to Kaggle.

## Earlier three-class CSV and TinyLinear manuscript

The separately supplied earlier `data/herwill_2026/submission.csv` has NOP 39
and counts 5,501 / 4,139 / 2,315. It is not the new notebook's export. Its IDs
match the same test set but labels differ. Preserve it as a historical file.

An older manuscript describes five folds, 254,983 TF-IDF features, 12 meta
inputs, TinyLinear head count 39, five heads totaling 195, and macro-F1 0.5295
versus LR 0.5246. Its matching historical execution record is not established
by the current notebook. The main paper now focuses on one selected pipeline.

[TODO-AUTHOR: state whether the older manuscript was only an internal draft,
submitted, withdrawn, under review, accepted or published; give venue/date/ID
where applicable, and disclose overlap. Do not assume an archived ZIP means
publication or simultaneous review.]

## Four-class materials

Loose files contain 54,817 training rows and 14,955 test rows with four labels.
They include 5,630 repeated training IDs and 620 repeated test IDs beyond first
occurrences. The smaller three-class files are exact trailing tabular subsets.
The larger version is not interchangeable with the three-class task.

`notebooks/AI_for_Digital_Safety_Notebook.ipynb` records four classes, 255,081
features, a 68-parameter head and selected SVC score 0.6536. These are separate
recorded claims, not current results. The 2024 archive is preserved separately.

## Historical external scores and newly reported platform record

Earlier notebook figure annotations mix public values 0.24877, 0.25711 and
0.37286 with OOF macro-F1 0.5314 on one `Score / F1` axis. Another earlier
private value 0.37500 was reported. These do not make a verified F1 trajectory.

On 11 October 2026 the author supplied:

| Field | Author report | Evidence |
|---|---|---|
| Runtime | 2 h 32 min 37 s | X: no linked run receipt |
| Allocation | GPU T4 x2 | X: not proof classical estimators used GPU |
| Public score | 3.78469 | X: metric/receipt and file linkage unverified |
| Private score | 3.78930 | X: metric/receipt and file linkage unverified |

Metadata duration 9,142.886868 s and the new runtime 9,157 s differ by
14.113132 s (A). The notebook prints CUDA while its GPU metadata is false.
The author report does not erase that retained metadata discrepancy.

[TODO-AUTHOR: provide screenshot or export of the run/submission receipt,
competition URL, submission identifier, timestamp, scoring rules and exact
uploaded-file hash. Hidden-set labels are neither requested nor required.]

## Naming choices

Option A names the competition and retains the LightBanglaHC audit title.
Option B describes the case as `a public datathon` and uses a generic audit title.
Both disclose the target-derived 0.183 field and identical technical limitations.
Choosing B does not alter facts, settle permissions, or guarantee anonymity:
distinctive dimensions/scores may still identify the case. Authors must choose
deliberately after checking applicable rules; no organizer ruling is asserted.

The public competition rules/scorer could not be retrieved during this revision.
The supplied DOCX's two conflicting formula descriptions remain unresolved.
