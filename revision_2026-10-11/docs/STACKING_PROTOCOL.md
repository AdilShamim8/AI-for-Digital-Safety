# S2. Controlled replication protocol

Status: the full-data paired LR experiment is complete; the six-base nested-stack comparison remains prospective.
The original notebook remains unchanged. A new run must log its environment. LightGBM 4.7.0 and Narwhals 2.27.1 were installed in a task-local directory; the nested training itself was not executed.

## Three-bullet rerun plan

- Completed: freeze the three-class train CSV and original row order, regenerate three stratified seed-42 folds, and run LR_C3 with global versus training-fold TF-IDF. Hold global class weights fixed for this isolated comparison; save paired OOF probabilities, warnings, iterations and elapsed time.
- In one new environment, execute the original six-base non-nested Meta-LR procedure, then rebuild base OOF features inside each outer training subset. Keep outer labels inaccessible to feature fitting, weights, stopping, meta fitting and any selection. Report both new pooled scores; retain historical 0.5218 only as a separate record.
- Inspect exact-text groups crossing folds and conflicting labels, then save fold IDs and hashes. After author decisions on conflict treatment, perform a separately labeled group-aware evaluation and full-pipeline serialization/resource measurement. Do not infer its results from the row-stratified run.

## LR_C3 comparison (runnable script)

From the full repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 revision_2026-10-11/scripts/lr_preprocessing_comparison.py --wall-seconds 14400
```

Both arms use all 47,817 rows, three seed-42 stratified folds, the original rules,
the four source TF-IDF configurations, C=3, SAGA, multinomial loss, max_iter=2000,
tol=0.001 and seed 42. The installed API may omit removed `multi_class`; the
three-class SAGA fit still uses multinomial loss. This compatibility adjustment
is logged as a new-environment replication, not a historical replay.

Global balanced class weights remain fixed in both arms. This isolates
preprocessing scope while leaving the aggregate label-statistic exposure present.
A third, fully corrected LR arm should recompute class weights from each fitting
subset, and must be reported separately rather than conflated with the paired
TF-IDF comparison.

Read `results.json`: only `status=completed` and both `completed=true` arms
support the requested paired pooled-F1 comparison. An unfinished fold or one
completed arm is not a paired result. The script records every convergence
warning; inspect them before drawing conclusions. Longer wall budgets rerun
from scratch; no fitted-state resume is implemented.

## Six-base stacking comparison

Required: numpy, pandas, scipy, scikit-learn and LightGBM, with exact versions
recorded. Recover historical versions if possible; otherwise pin the new
environment and label it a replication. PyTorch/THOP are only required to replay
the unrelated profiling section, not to fit the actual classical predictor.

Use the six candidates from Table 3 of the manuscript, in order:
LR_C8, LR_C3, calibrated SVC, calibrated CNB, calibrated SGD, LightGBM.
Keep isotonic calibration CV=2; explicitly record its `ensemble` behavior and
the fitted base/calibrator count. Use 18 probability columns, class order 0/1/2,
and Meta-LR C=10, max_iter=500, multinomial loss and seed 42.

### Arm N: current non-nested procedure

1. Fit four TF-IDF branches on all training rows and compute global class weights.
2. For each original outer fold, fit each base candidate excluding that fold;
   LightGBM uses the assessment fold for early stopping, as the source does.
3. Assemble the single n-by-18 base OOF matrix. Fit/evaluate three Meta-LR models
   with the same fold assignments, using global class weights.
4. Save IDs, labels, fold, base/meta probabilities and pooled macro-F1. Record
   base convergence, calibration details and selected LightGBM iterations.
5. Do not select another hyperparameter or threshold on the scored rows.
   Replicating the subsequent ensemble selection is a separate development result.

### Arm C: fully corrected nested procedure

For each outer assessment fold E and training rows T:

1. Create three stratified, shuffled seed-42 inner folds within T. All indices
   saved to the output must refer back to original CSV row IDs.
2. For each inner fitting subset U and inner OOF subset V, fit the four TF-IDF
   branches on U, transform V and E, and compute class weights from U.
3. Fit/calibrate each candidate within U only. Calibration CV=2 is within U.
   The outer fold E and inner OOF labels V must not select boosting rounds.
4. LightGBM stopping: reserve a prespecified 20% stratified seed-42 subset of U
   for stopping; fit its feature map and weights on the remaining stopping-fit
   rows; choose a round count using that stopping subset. Then refit the feature
   map and booster on all U for that fixed round count and predict V and E.
   This is a proposed design choice, not an original notebook setting.
5. Assemble inner OOF features for every row in T. Average the corresponding
   three inner models' E probabilities within each of the six candidates.
6. Fit one Meta-LR on the inner OOF matrix and T labels, with weights from T;
   predict E from its 18 averaged base probabilities. Do not look at E labels.
7. After all outer fits finish, pool each E prediction exactly once. Report
   macro-F1 from pooled probabilities' argmax and save all paired outputs.

Arm C trains 3 outer x 3 inner x 6 = 54 base-candidate objects, versus 18
in Arm N, before calibration internals or stopping refits. A two-LR-candidate
count is 18 LR fits for C and six for N. This is considerably more work than
replaying the original notebook once. Do not assume the author's 2.5-hour
historical runtime applies to this comparison.

The N-versus-C difference changes several validation controls jointly. It is
a protocol contrast, not a causal estimate of meta-stacking leakage alone.
For a nesting-only sensitivity comparison, hold representation scope, class
weights, candidate settings, stopping rules and assessment inference policy
fixed across arms and document any residual exposures explicitly.

The corrected inference policy above averages inner base fits but uses one
outer Meta-LR. It must not be presented as validating the original selected
seven-member, three-meta-fit test ensemble. To assess that exact deployment
object, reconstruct all its averaging/selection inside T and evaluate the
frozen object once on E or a separate protected holdout.

## Pending result fields

- Completed LR result: global 0.5220608956637554; within-fold 0.5188715615569914;
  difference 0.003189334106763919. All six fits reached max_iter=2000.
  Exact fold scores, environment and warnings are in audit/lr_comparison/results.json;
  paired OOF arrays are retained alongside it.
- [TODO-AUTHOR: execute matched N and C arms; insert both new Meta-LR scores
  and paired comparison, with inference policies explicitly named.]
- [TODO-AUTHOR: if claiming a causal nesting effect, execute the separately
  controlled sensitivity study instead of attributing the joint difference.]
- [TODO-AUTHOR: provide an anonymous artifact link and the original scoring
  equation, count rule, and leaderboard receipt tied to a submission hash.]
