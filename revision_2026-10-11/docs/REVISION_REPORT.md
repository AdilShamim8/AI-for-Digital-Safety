# LightBanglaHC major-revision report

Prepared 11 October 2026. This is an author revision package, not confirmation of conference submission or acceptance. Original notebook/data files remain unchanged. All unperformed or unverified claims remain labeled.

## 1. Cross-check and mismatch list

The current GitHub paper was read and compared with the supplied notebook and raw three-class CSVs. The active original manuscript already described the updated three-fold pipeline correctly. Its main problems were evidence availability, interpretation and unfinished declarations, rather than broken arithmetic.

| Original section / claim | Cross-check finding | Revision |
|---|---|---|
| Abstract / contribution | The audit framing is correct, but the abstract was too long and the title could imply a model proposal. | 191-word final abstract including paired LR evidence; audit title. |
| 3.2 / execution metadata | 9,142.886868 s is notebook metadata; new author runtime is 9,157 s. GPU metadata conflicts with CUDA output. | Retain metadata as R; author runtime, T4 x2 and platform scores are X. Difference is 14.113132 s (A). |
| 3.2 / version history | TinyLinear, four-class files and NOP-39 export are other records. | Move detail to S1; add prior-manuscript status TODO. |
| 3.3 / duplicate analysis | 621 training repeats was correct, but cross-fold allocation and conflicting labels had not been checked. | Regenerate seed-42 folds: 308 cross-fold groups/771 rows; 52 conflicting groups/130 rows; 36 groups have both properties. |
| 4.1 / sala example | Substring behavior is correct, but the lexical example was unexplained. | Explain abusive/context-dependent transliteration and the false trigger inside salad. |
| 5.3 / updated CSV missing | Now outdated: a new Drive CSV was supplied. | Verify 11,955 rows, IDs/order, counts 6,414/4,401/1,140, parameters 0.183; no claim that its historical prediction origin or platform upload is authenticated. |
| NOP terminology | First use lacked an explicit definition. | Define number of parameters (NOP) at first substantive use. |
| 6.1 / flattened severity | Exposure paths were traced correctly but their structural scopes differ. | Add six-row taxonomy and small stratified class-weight diagnostic. |
| 6.3 / F1-squared weights | Near-uniform weights and 0.0008 observed gain lacked quantitative emphasis. | Compute approximate weights from printed scores; explicitly reject calling the gap a bound on leakage bias. |
| 6.4 / fold indices | Missing saved historical folds do not prevent a new deterministic reconstruction. | Save regenerated indices with sklearn version; do not relabel them as authenticated historical folds. |
| No rerun / impossible replay | Missing fitted objects prevent replay of original states, not training a new model. | Execute budgeted LR experiment; explain why the complete nested-stack comparison is still prospective. |
| 7.3 / NOP provenance | F/2.9 rounding to 0.183 is in the source and now the supplied CSV. | Retain the technical finding, avoid intent/organizer allegations, and provide both named and public-datathon versions. |
| 7.4 / platform quantities | Old external values are not the new author-reported 3.78469/3.78930. | Keep old values in S1; add current reports as X. No conversion to hidden-set F1 or scoring-rule inference. |
| Declarations / header | Disclosure asks authors to finalize; blank publication fields produce meaningless commas. | Use explicit TODO-AUTHOR fields and neutral submission headers. Publication metadata is publisher-assigned, not invented. |
| Related work / artifacts | Super Learner and assessment-chapter references and an availability section were missing. | Add verified sources and clearly labeled operational-source citation; add anonymous/public availability TODOs. |
| Venue fit | A vision-centered title alone does not define the journal scope. | Official scope includes AI/ML; official homepage says not currently Scopus-indexed. Flag authors’ institutional/index requirements without selecting for them. |

### Values/settings verified and deliberately unchanged

| Item | Verified value / source |
|---|---|
| Training/test rows | 47,817 / 11,955, raw CSVs and retained output (D/R) |
| Class supports | 23,756 / 18,163 / 5,898 (D/R) |
| Balanced class weights | 0.670946 / 0.877553 / 2.702442 when rounded to six decimals (A/S) |
| Sparse widths | 100,000 + 80,000 + 50,000 + 105 = 230,105; LGB +20 = 230,125 (R/S/A) |
| CV | Three shuffled stratified folds, seed 42; isotonic calibration CV=2 (S) |
| LR | C=8 or 3, SAGA, multinomial, max_iter=2000, tol=0.001; global weights (S) |
| SVC/CNB/SGD | C=0.5 / alpha=0.05 norm=True / modified_huber alpha=0.0001 max_iter=200; settings match source (S) |
| LightGBM | 63 leaves, rate 0.1, feature fraction 0.7, bagging 0.8/frequency5, min_child20, L1=0.1/L2=0.5, global sample weights, max1000 rounds/patience80; iterations149/173/182 (S/R) |
| Meta-LR | 18 input probabilities; C=10; max_iter=500; multinomial/global weights; three fits (S) |
| Final predictor | Six averaged base outputs plus averaged Meta-LR, F1-squared normalized weights, unadjusted argmax (S/R) |
| Recorded F1 | Weighted 0.5314, average0.5306, LR_C3 0.5221, Meta-LR 0.5218; all candidate/fold values retained (R) |
| Threshold search | Two 30x30 grids, 900 pairs each; unadjusted (1,1) omitted; four variants compared (S) |
| Confusion rows | [16464,6331,961]; [7502,9039,1622]; [1360,2292,2246] (R) |
| Reconstructed metrics | F1=0.5314177984731835; accuracy=0.5803166237948847 (A) |
| LR structural subtotal | 6 x (3 x 230105 + 3) = 4,141,908; three Meta-LR objects =171 (A) |
| Timing subtotal | 2601.7 +2625.0 +3802.8 =9029.5s =150.4916667min; 150.5min remains correct (R/A) |
| Local ratio | 0.5314177984731835/(0.183+5e-16)=2.9039223960283174; not a platform score (A) |
| Identity profiling | Unconnected identity operation; initialized/fallback zero; no successful THOP branch line in retained output (S/R) |

## 2. New evidence, results and pending protocols

| Check | Result | Evidence / limit |
|---|---|
| LR_C3: global TF-IDF | 0.5220608957 | New-run R; global class weights held fixed |
| LR_C3: fold-fitted TF-IDF | 0.5188715616 | New-run R; global class weights held fixed |
| Global minus fold-fitted F1 | 0.0031893341 | A from paired new runs; no general bias bound |
| Non-nested / nested stacking | Historical Meta-LR 0.5218 / [TODO-AUTHOR: execute matched new arms] | Historical R / prospective P; no corrected score invented |
| Repeated raw-text groups | 461 groups; 1082 rows; 621 repeats beyond first | D |
| Cross-fold repeated groups | 308 groups; 771 rows | D; regenerated indices, not historical authentication |
| Conflicting-label repeated groups | 52 groups; 130 rows | D; 36 groups also span folds |
| Weighted minus average ensemble | 0.5314 -0.5306 =0.0008 | A/R; observed gain, not a bound on leakage optimism |
| Max relative fold/global class-weight change | 0.005506002% | A; not a measured prediction effect |
| New CSV consistency | 11,955 rows, matching IDs/order and class totals, constant0.183 | D; no proof of platform upload identity |

### Ensemble-weight calculation

$\alpha_j=F_j^2/\sum_k F_k^2$. Only rounded printed scores are available, so these are approximate reconstructions.

| Member | Printed F | Reconstructed weight |
|---|---:|---:|
| LR_C8 | 0.5169 | 0.154990963 |
| LR_C3 | 0.5221 | 0.158125058 |
| SVC | 0.4824 | 0.134991962 |
| CNB | 0.4391 | 0.111845930 |
| SGD | 0.4691 | 0.127650987 |
| LightGBM | 0.5160 | 0.154451708 |
| Meta-LR | 0.5218 | 0.157943392 |

Uniform weight is 1/7=0.142857143. Maximum absolute deviation is 0.031011213. The observed gain is 0.0008 macro-F1, or 0.08 percentage points. Calling it a leakage bound would be incorrect: the score difference combines a true predictor difference and a difference in biases; shared bias can cancel. Neither individual bias is identified by this subtraction.

$\Delta_{\mathrm{observed}}=(F_w-F_a)+(b_w-b_a)$ does not bound $b_w$ or $b_a$.

Class-weight diagnostic: for each regenerated training subset T and class c, compute w(T,c)=|T|/(3n(T,c)), then max_{T,c}|w(T,c)/w(I,c)-1|. Multiplying by 100 gives 0.005506001542%. All exact values are in audit/checks.json.

### Execution scope and remaining work

The LR script uses all rows and exact four-branch source settings. Its API compatibility adjustment omits removed multi_class under sklearn 1.8; three-class SAGA still fits multinomial loss. The historical version is unknown. All six fits reached max_iter=2000; the comparison is under that training budget, not between converged optima. All convergence limits are saved and accompany the result. The six-base original/nested comparison was not run; its54 nested base-candidate objects versus18 original objects, stopping refits and calibration internals require a larger training budget. This is a stated resource/session decision, not a claim that training is impossible.

A sequential LR attempt was interrupted to restart independent folds in parallel. Only the final paired run is used. LightGBM 4.7.0 was downloaded into a task-local package directory; it is a new-environment option, not a recovered historical version. PyTorch profiling is irrelevant to training the actual classical predictor.

See STACKING_PROTOCOL.md for the complete steps, inference policies, required controls and pending result fields. New nested-versus-current scores compare multiple protocol changes jointly unless a separate nesting-only sensitivity study holds the others fixed.

### Three-bullet rerun plan

- Freeze the CSV, seed-42 folds and source rules; retain the completed paired global/fold-fitted LR comparison, keeping global weights fixed and preserving probabilities, versions and iteration warnings.
- Execute the original non-nested and fully corrected nested six-base Meta-LR arms in one pinned environment; protect outer labels from all fitting/stopping/selection, and name the inference procedure explicitly.
- Retain duplicate/conflict groups and fold hashes; after author-approved treatment, conduct a separately labeled group-aware evaluation and whole-pipeline serialization/resource measurement.

Original notebook source: https://drive.google.com/file/d/11-Cj5i_WoMq3APdwO41M0tdtS3Lk-ck5/view?usp=drivesdk

## 3. Full revised paper, section by section

The complete named-case text follows. The PDFs/LaTeX preserve exact equation numbering and the supplied IJCVSP template. The public-datathon version changes the title/case naming and omits the named competition citation; all numerical findings and limitations are retained. Both options are supplied, without choosing for the authors.

# LightBanglaHC Audit: Evaluation Validity, Inference Reconstruction, and Accounting Boundaries in Harmful-Content Classification

Author revision draft; complete TODO fields before submission. PDF/LaTeX are authoritative for layout and equation numbering.


# Abstract

We audit a stacked TF-IDF ensemble for harmful-content classification and trace how evaluation and parameter accounting relate to the predictor actually used. The recorded three-fold run contains 47,817 labeled training rows, 11,955 test rows, 230,105 TF-IDF features, six base candidates, and a logistic regression stacker. The selected weighted ensemble records pooled out-of-fold macro-F1 0.5314, compared with 0.5221 for the strongest base candidate. We distinguish label-free representation fitting, aggregate class statistics, supervised meta-feature dependencies, stopping, and selection. Regenerated seed-42 folds place 308 exact-text groups across folds; 52 repeated-text groups contain conflicting labels. Reconstructed ensemble weights range approximately from 0.111846 to 0.158125. Their observed advantage over uniform averaging is 0.0008, not a bound on selection bias. The separately profiled identity module is absent from the prediction path. Six base logistic regression fits imply 4,141,908 coefficients and intercepts, while the exported value 0.183 is derived from a target ratio. Source observations, retained outputs, data checks, and arithmetic are labeled separately. A paired LR comparison yields macro-F1 0.522061 with global TF-IDF and 0.518872 with fold-fitted TF-IDF, holding class weights fixed. The audit supplies controlled rerun protocols. It introduces no new classifier or measured deployment advantage.

#### Keywords.

Harmful-content classification ; Evaluation validity ; Stacked generalization ; Accounting boundaries ; Reproducibility.

# Introduction

A harmful content classifier’s reported accuracy and efficiency are interpretable only when they refer to a specified prediction procedure. In sparse ensembles, predictions can depend on fitted representations, calibrated base estimators, and a second-stage head. Counting the head alone does not describe the system that produces its inputs (Schwartz et al. 2020).

We distinguish three objects: the *inference object*, which maps raw text to predictions; the *evaluation object*, which includes fitting, validation, and selection; and the *accounting object*, which defines the artifacts and computation included in a resource claim. Stacking (Wolpert 1992) makes their relationship consequential: excluding a row from its own base fit does not necessarily isolate the full procedure when meta training features depend on meta validation labels. Global preprocessing and repeated selection create additional dependencies (Varma and Simon 2006; Cawley and Talbot 2010; Kapoor and Narayanan 2023).

We examine one recorded implementation from the HerWILL AI for Digital Safety Datathon 2026. The supplied competition description is cited as an operational source (HerWILL 2026). The updated notebook, retained outputs, competition description, and raw CSVs permit source inspection, data checks, inference reconstruction, and arithmetic accounting. Historical row-level OOF predictions and fitted artifacts remain unavailable. We execute new data checks and a controlled LR comparison; these are distinct from replaying the original predictions. Documentation describes a mixed Bangla, English, and Banglish corpus; preprocessing alone would not establish this scope.

The contribution is an inspectable audit linking the three objects within one artifact, followed by a corrected prospective protocol. It is not a new algorithm, a demonstration of predictive superiority, or a measured deployment advantage. Section 3 defines the evidence categories and verification limits used throughout.

# Related Work

Hate speech, offensive language and implicit harm require documented annotation decisions (Davidson et al. 2017). Functional tests probe negation and counter speech (Röttger et al. 2021); harm and bias analysis requires stating whose interests are considered (Blodgett et al. 2020). BD-SHS (Romim et al. 2022) and BanglaBERT (Bhattacharjee et al. 2022) provide Bangla context, not directly comparable scores or verified source datasets for this corpus. Data statements help document population and curation scope (Bender and Friedman 2018).

Stacked generalization learns from base predictions (Wolpert 1992). Super Learner studies cross-validated combination and risk minimization (Laan, Polley, and Hubbard 2007); the source’s squared-F1 heuristic is different. Hastie et al., Section 7.10.2 (Hastie, Tibshirani, and Friedman 2009), explain why model assessment must include preparation and selection within permitted training data. Their supervised-selection example is not a numerical estimate of label-free TF-IDF bias here. Selection bias (Varma and Simon 2006; Cawley and Talbot 2010) and leakage (Kapoor and Narayanan 2023) motivate tracing full feature ancestry. Calibration adds fitted state (Niculescu-Mizil and Caruana 2005) and requires separate reliability diagnostics (Vaicenavicius et al. 2019). Overlapping folds complicate uncertainty (Bengio and Grandvalet 2004); paired tests require retained predictions and an appropriate design (Dror et al. 2018).

Green AI (Schwartz et al. 2020), energy reporting (Henderson et al. 2020), reproducibility (Pineau et al. 2021), and model cards (Mitchell et al. 2019) distinguish computation, replay and intended use. This study applies those established principles to one prediction and accounting record.

# Study Design, Evidence, and Dataset Scope

## Design and Audit Method

The unit of analysis is the relationship among the implementation, retained outputs, and supported claims. We trace invoked fitting, prediction, selection, profiling, and saving operations through their inputs; comments do not establish execution. We inspect the supplied updated notebook and check raw CSV shapes, labels, identifiers, and exact text duplication. We also reconstruct metrics from its embedded confusion figure. These checks substantiate source structure and internal consistency, not authenticated historical execution.

Each claim has an evidence type: S (source observation), R (retained historical output or explicitly identified new execution), D (direct CSV check), A (arithmetic reconstruction), X (unverified external quantity), or P (prospective proposal). An unperformed experiment is stated as such. New checks regenerate fold indices and inspect duplicates, export structure, and weight arithmetic. The LR comparison uses a new software environment; the six-candidate historical pipeline and nested stack are not replayed. Source locations, full file digests, regenerated folds, and execution status are supplied in the artifact ledger and supplement. The availability statement identifies the review copy.

## Available Artifacts and Version Boundaries

The canonical notebook has one code cell, 971 source lines, execution count one, two output streams, and one figure (S). Metadata records execution on 20 April 2026 for 9,142.89 seconds (R). Python metadata lists 3.12.12; historical package versions are absent. Output reports `Device: cuda`, while notebook metadata disables GPU. These retained fields are not independently authenticated execution records.

The author now reports runtime 2 h 32 min 37 s on GPU T4 $\times2$, public score 3.78469, and private score 3.78930 (X). These were supplied in correspondence, without a linked scoring receipt or execution record. The reported duration is 9,157 seconds, approximately 14.11 seconds longer than notebook metadata (A). GPU allocation does not show that the classical estimators used GPU acceleration; the source sets no GPU device for LightGBM. The platform scores are neither macro-F1 measurements nor evidence resolving the missing scorer.

We use only the three-class 2026 archive. Historical variants are separated in Supplement S1. They do not support claims about this selected path.

## Task and Checked Corpus

The supplied competition description maps 0 to Explicitly Toxic/Hateful, 1 to Subtly Toxic, and 2 to Non-toxic/Neutral. Training columns are `id`, `text`, and `y`; test columns are `id` and `text`. Shapes are (47,817, 3) and (11,955, 2) before processed columns are added (D), totaling 59,772 rows. Table 1 reports the class supports, which also match the updated notebook’s printed counts.

<div id="tab:supports">

| Class    | Support | Proportion (%) |   Weight |
|:---------|--------:|---------------:|---------:|
| Explicit |  23,756 |         49.681 | 0.670946 |
| Subtle   |  18,163 |         37.984 | 0.877553 |
| Neutral  |   5,898 |         12.335 | 2.702442 |
| Total    |  47,817 |        100.000 |          |

Directly checked supports (D); proportions and globally balanced class weights (A). The source computes weights before splitting (S).

</div>

The source uses $w_c=n/(3n_c)$ for LR, SVC, SGD, Meta-LR, and LightGBM sample weights. CNB has no explicit class weight argument. Since weights depend on every training label, they also depend on each fold subsequently used for assessment. The test rows have no labels and support no accuracy measurement.

Exact raw-string checks find 621 repeated training rows and 54 repeated test rows beyond first occurrences, and 254 distinct texts shared between train and test (D). New regenerated-fold counts are reported in Section 6.5. Identifiers are unique within each three-class file and disjoint between its train and test sets. Text overlap and identifier uniqueness are different properties. We neither estimate the effect of duplication nor perform a near-duplicate, shared-author, or thread analysis.

## Documentation and Population Scope

The supplied description calls the corpus manually annotated Bangla, English and Banglish social-media content, emphasizing subtle toxicity, code mixing and noise. Language proportions and annotation agreement are not measured. Its details document lists CC BY-NC-ND 4.0, but supplies no full annotation manual, consent records or annotator-welfare documentation. Label names and script cues do not validate sarcasm detection or language identification. We describe the supplied documentation, not whether the original release had additional records.

# Audited Prediction Pipeline

## Cleaning, Signals, and Numerical Features

Let $x$ be the original string after missing-value handling. The combined processed text is $$s(x)=C(x)\,\|\,\texttt{SSEP}\,\|\,H(x),$$ where $C$ cleans text and $H$ produces signal tokens from the original input. The cleaner applies NFKC normalization, lowercasing, URL and mention substitutions, hashtag-marker removal, emoji substitution, repeated-letter reduction, repeated-punctuation markers, and whitespace compression (S). Signals retain access to original capitalization and punctuation rather than only the cleaned string.

The explicit lexical union contains 21 Bangla, 23 transliterated, and 29 English entries, totaling 73 distinct strings; the subtle inventory contains 25 entries (S). Lexical detection tests substring presence, counting each distinct entry at most once per text, rather than counting every occurrence. Signals include capped repetition of explicit, subtle, sarcasm, threat, identity-related, script, capitalization, punctuation, length, and neutral markers. The string “this is a salad” activates `sala`, a transliterated term used abusively in Bangla and Hindi; it also has benign and kinship uses. Here it is a substring inside “salad”, not an abusive utterance. The match records a lexical condition rather than intent.

Twenty numerical features are generated without fitted scaling. They cover length, word count, lexical diversity, punctuation, emoji runs, Bangla regex runs, script indicators, capitalization, lexical hits, pattern flags, a combined cue count, and short/long indicators. One feature divides the number of Bangla regex runs by character length; it is not a measured fraction of Bangla characters. Numerical features are supplied to LightGBM only. A marker named for hate or neutrality is a code identifier, not a validated social construct.

## Four Globally Fitted Sparse Branches

Table 2 lists the feature branches and recorded widths. All use sublinear term frequency and are fitted on all processed training texts before the three-fold split. Test texts are transformed, not fitted on (S). Under the documented default interpretation of omitted smoothed-IDF and normalization options, a branch computes $$\begin{aligned}
u_{ij}&=(1+\ln t_{ij})\left[1+\ln\frac{n+1}{\mathrm{df}_j+1}\right],\quad t_{ij}>0,\\
\phi(x_i)&=u_i/\|u_i\|_2,
\end{aligned}$$ with $u_{ij}=0$ otherwise. Historical package versions and fitted arrays are absent; current documentation is not evidence of the original runtime.[^1]

<div id="tab:features">

| Branch          | Input              | Analyzer                    | Grams / document frequency  |     Cap |   Width |
|:----------------|:-------------------|:----------------------------|:----------------------------|--------:|--------:|
| Word            | $s(x)$             | Word; non-whitespace tokens | 1–3; min 1, max 0.98        | 100,000 | 100,000 |
| Character       | $s(x)$             | `char_wb`                   | 2–5; min 2                  |  80,000 |  80,000 |
| Clean character | $C(x)$             | `char`                      | 1–4; min 2                  |  50,000 |  50,000 |
| Signal          | $H(x)$             | Word; non-whitespace tokens | 1–2; min 1                  |  10,000 |     105 |
| Combined TF-IDF |                    |                             |                             | 240,000 | 230,105 |
| LightGBM input  | TF-IDF + numerical |                             | 20 fixed numerical features |         | 230,125 |

Source settings (S) and realized widths printed by the updated notebook (R). Numerical features are appended only for LightGBM.

</div>

CNB receives both character branches, totaling 130,000 columns. LR, SVC, and SGD receive the 230,105-column TF-IDF matrix. LightGBM receives that matrix plus 20 numerical columns. The global map $\phi$ exposes validation covariates to vocabulary construction, document-frequency filtering, feature caps, and IDF. A later estimator fit that excludes a row cannot undo this earlier representation fitting.

## Base Candidates and Stacker

The source forms shuffled stratified three-fold splits with seed 42. Six base candidates are trained: two LR configurations, calibrated SVC, calibrated CNB, calibrated SGD, and LightGBM (Ke et al. 2017). Table 3 gives explicit settings. The two LR candidates share an estimator family; six candidates do not imply six distinct algorithmic families.

<div id="tab:configs">

| Candidate    | Input                  | Explicit configuration                                                                                                                                                                                                                              |
|:-------------|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LR_C8, LR_C3 | TF-IDF                 | $C=8$ or 3; saga; multinomial; max. 2,000 iterations; tolerance $10^{-3}$; global class weights; seed 42.                                                                                                                                           |
| SVC          | TF-IDF                 | LinearSVC, $C=0.5$; max. 3,000 iterations; global class weights; seed 42; isotonic calibration, CV $=2$.                                                                                                                                            |
| CNB          | Two character branches | $\alpha=0.05$; `norm=True`; isotonic calibration, CV $=2$; no explicit class weights.                                                                                                                                                               |
| SGD          | TF-IDF                 | Modified Huber; $\alpha=10^{-4}$; max. 200 iterations; global class weights; seed 42; isotonic calibration, CV $=2$.                                                                                                                                |
| LightGBM     | TF-IDF + 20 numerical  | Multiclass log loss; 63 leaves; rate 0.1; feature fraction 0.7; bagging fraction 0.8, frequency 5; min. child samples 20; $L_1=0.1$, $L_2=0.5$; `is_unbalance=True`; global sample weights; seed 42; max. 1,000 rounds; early-stopping patience 80. |
| Meta-LR      | 18 probabilities       | $C=10$; max. 500 iterations; multinomial; global class weights; seed 42; solver not overridden.                                                                                                                                                     |

Invoked settings in the updated source (S). Unspecified settings depend on the unrecorded historical library versions.

</div>

Calibration adds fitted state to the probability path (Niculescu-Mizil and Caruana 2005). SVC and SGD use global class weights, whereas CNB does not. Their calibration fits remain inside each base fitting subset but share globally fitted features. No proper-score or reliability diagnostic evaluates these probabilities (Vaicenavicius et al. 2019). LightGBM’s stopping criterion uses the same validation fold later scored for macro-F1; log loss and macro-F1 are different objectives.

## OOF Features and Selected Test Predictor

Let $V_1,V_2,V_3$ partition $I=\{1,\ldots,n\}$, and let $f(i)$ identify row $i$’s fold. For base candidate $b$, let $h_b^{(-f)}$ be its probability-producing fit excluding $V_f$, with calibration or early stopping as specified. Training and test meta features differ: $$\begin{aligned}
z_i&=\left[h_b^{(-f(i))}(\phi(x_i))\right]_{b=1}^{6}\in\mathbb{R}^{18},\\
\bar z(x)&=\left[\frac{1}{3}\sum_{f=1}^{3}h_b^{(-f)}(\phi(x))\right]_{b=1}^{6}.
\end{aligned}$$ LightGBM additionally receives the numerical features, suppressed in this notation for readability. The notation excludes a fold from its base estimator fit, not from global preprocessing, class weights, or LightGBM stopping selection.

Three Meta-LR fits are trained from the single global OOF feature matrix using the same split scheme. Their test probabilities are averaged. The selected final predictor combines six averaged base outputs and the averaged Meta-LR output, so Meta-LR is an active component rather than merely an alternative candidate. If $F_j$ is candidate $j$’s pooled OOF macro-F1 and $p_j(x)$ its test probability vector, then $$\alpha_j=\frac{F_j^2}{\sum_{k=1}^{7}F_k^2},\qquad
\hat y(x)=\arg\max_c\sum_{j=1}^{7}\alpha_j p_j(x)_c.
$$ These weights use labeled development outcomes rather than a prespecified average. Figure 1 separates this prediction path from the independent profiling operation.

#### Figure 1.

The selected prediction path uses globally fitted features, six three-fold base candidates, averaged base probabilities, three Meta-LR fits and the weighted seven-member ensemble. See the vector diagram in the PDF.

# Recorded Results and Submission Provenance

## Candidate and Ensemble Results

Table 4 preserves printed candidate scores and fold values. LR_C3 is the strongest base candidate. The weighted ensemble has pooled OOF macro-F1 0.5314, compared with 0.5306 for the simple average and 0.5221 for LR_C3 (R). The rounded weighted-versus-base difference is 0.0093, or 0.93 percentage points (A). It is descriptive; the source selects weights, stopping points, and candidates using evaluation information, and no untouched comparison or paired prediction file is supplied.

<div id="tab:results">

| Candidate             | Role                      | Pooled | Fold 1 | Fold 2 | Fold 3 |
|:----------------------|:--------------------------|-------:|-------:|-------:|-------:|
| LR_C8                 | Base                      | 0.5169 | 0.5158 | 0.5122 | 0.5227 |
| LR_C3                 | Base                      | 0.5221 | 0.5209 | 0.5171 | 0.5281 |
| SVC                   | Base                      | 0.4824 | 0.4860 | 0.4827 | 0.4782 |
| CNB                   | Base                      | 0.4391 | 0.4403 | 0.4356 | 0.4414 |
| SGD                   | Base                      | 0.4691 | 0.4675 | 0.4719 | 0.4678 |
| LightGBM              | Base                      | 0.5160 | 0.5154 | 0.5136 | 0.5191 |
| Meta-LR               | Stacker / ensemble member | 0.5218 | 0.5183 | 0.5169 | 0.5299 |
| Weighted              | Selected ensemble         | 0.5314 |      – |      – |      – |
| Simple average        | Alternative               | 0.5306 |      – |      – |      – |
| Weighted + thresholds | Alternative               | 0.5300 |      – |      – |      – |
| Average + thresholds  | Alternative               | 0.5287 |      – |      – |      – |

Recorded pooled and fold macro-F1 (R). Ensemble variants are scored on the same pooled OOF rows; no uncertainty interval is inferred from dependent folds.

</div>

Pooled F1 is computed once from all OOF rows, not averaged over fold F1. OOF prediction uses a single held-out fit, whereas test prediction averages three fits at both levels. Assessing the latter requires a matched frozen procedure.

The threshold search evaluates $30\times30=900$ pairs for each of the two ensemble probability arrays, adjusting classes 0 and 1 while leaving class 2’s divisor at one (S). Its search interval is 0.1 to 0.9, omitting the unadjusted pair $(1,1)$. A lower best threshold score than the unadjusted score is therefore possible without a contradiction. The final source compares four variants and selects the unadjusted weighted ensemble. The displayed weighted thresholds 0.90, 0.87, and 1.00 are not on that selected prediction path.

## Confusion Counts and Error Structure

Table 5 transcribes the nine integer annotations in the updated notebook’s embedded confusion figure. Row sums match the raw CSV supports and total 47,817. Reconstruction yields macro-F1 0.5314177985 and accuracy 0.5803166238 (A), consistent with the printed 0.5314. The three classwise values agree with the figure’s four-decimal labels.

<div id="tab:confusion">

| Actual    | Explicit | Subtle | Neutral | Support |             Precision | Recall |     F1 |
|:----------|---------:|-------:|--------:|--------:|----------------------:|-------:|-------:|
| Explicit  |   16,464 |  6,331 |     961 |  23,756 |                0.6501 | 0.6930 | 0.6709 |
| Subtle    |    7,502 |  9,039 |   1,622 |  18,163 |                0.5118 | 0.4977 | 0.5046 |
| Neutral   |    1,360 |  2,292 |   2,246 |   5,898 |                0.4651 | 0.3808 | 0.4188 |
| Predicted |   25,326 | 17,662 |   4,829 |  47,817 | Macro-F1 0.531418 (A) |        |        |

Selected weighted-ensemble OOF confusion counts (R), with classwise metrics reconstructed from the displayed counts (A). Rows are actual labels; columns predicted labels.

</div>

Neutral has the lowest F1 and recall. Of 4,829 examples predicted Neutral, 2,583 have a toxic label; 3,652 actual Neutral examples are assigned a toxic label. The largest off-diagonal count is 7,502 Subtle examples predicted Explicit. Without paired row-level outputs, causes and joint candidate errors remain unknown. An always-Explicit predictor has arithmetic macro-F1 $2n_0/[3(n+n_0)]=0.221275$ (A), not a measured baseline experiment.

## Test Export and Platform Claims

The updated notebook prints 6,414 Explicit, 4,401 Subtle, and 1,140 Neutral test predictions (R). A newly supplied CSV contains exactly these class counts, 11,955 rows, columns `id,y_pred,parameters`, IDs matching the three-class test file in order, and constant `parameters`=0.183 (D). This establishes aggregate and schema consistency with the recorded export. Without fitted states or row-level historical probabilities, it does not authenticate the origin of every prediction.

The source writes additional files with declared NOP values 0.1, 0.3, and 1. Number of parameters (NOP) means a count under a stated model boundary, not a freely chosen denominator. A zero-valued loop entry is skipped because it equals the initial profiled value; a later summary recommends that filename despite no matching save. We distinguish these source operations from platform acceptance. The new author-reported public/private scores remain X evidence.

## Timing and Retained State

The recorded LR training sections take 2,601.7 and 2,625.0 seconds, and LightGBM takes 3,802.8 seconds (R). These three sections alone total 9,029.5 seconds, about 150.5 minutes (A), before other work. The notebook metadata reports about 152.4 minutes. Thus its concluding “25–35 minutes” claim is inconsistent with its retained timings. Those timings are historical output, not a newly controlled runtime benchmark, and no inference latency measurement is supplied.

LightGBM reports best iterations 149, 173, and 182 (R). The inspected source serializes no fitted vectorizers, base models, boosters, meta estimators, or historical OOF arrays. In-memory test arrays are generated before export, but the absence of saved model files prevents fresh-process raw-text replay. Historical environment uncertainty remains even though the source and recorded dimensions can now be inspected.

# Evaluation Validity

## Different Types of Evaluation Exposure

The retained score describes development predictions. Table 6 separates mechanisms by the information they use and their structural reach. The tiers prioritize validation work; they are not measured effect sizes or a universal ordering of harm.

<div id="tab:taxonomy">

| Mechanism / tier                                    | Information and reach                                                                | Interpretation and required control                                                                                                                                 |
|:----------------------------------------------------|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TF-IDF / covariate exposure                         | Label-free validation text enters vocabulary, frequency filters, caps and IDF.       | Transductive representation exposure. Fit each branch on the permitted training subset; compare with the global arm. No label-path claim.                           |
| Class weights / aggregate exposure                  | Three class counts include validation labels; fitting sample weights inherit them.   | Low-dimensional label statistics. Here stratification makes fold-local values differ by at most 0.005506% relatively (A); measure any prediction effect separately. |
| Early stopping / supervised selection               | LightGBM assessment labels select boosting rounds through log loss.                  | Reuse of assessment outcomes. Use a stopping partition inside the training subset, then assess the frozen fit.                                                      |
| Meta-stacking / supervised feature ancestry         | Meta-training features are generated by base fits containing meta-assessment labels. | Full supervised dependency path. Rebuild inner OOF features within every outer training subset.                                                                     |
| Ensemble weights / aggregate selection              | Seven pooled F1 scores determine normalized squared weights.                         | Near-uniform weights; observed gain 0.0008. Estimate optimism only with protected assessment labels.                                                                |
| Threshold and candidate choice / repeated selection | Two grids of 900 choices and four final variants use the same labeled OOF rows.      | Multiple adaptive comparisons. Freeze decisions within training-only selection partitions.                                                                          |

Structural exposure taxonomy (S/A/P). Magnitude is unmeasured unless an observed diagnostic is stated; an observed score gap is not a bias bound.

</div>

The TF-IDF fits precede fold construction, but test text is only transformed. Thus this is intra-training covariate exposure, not fitting on the unlabeled test set. Global class weights use $w_{I,c}=|I|/(3n_{I,c})$. Regenerated fold-local weights differ from these global values by at most 0.005506% relatively (A), reflecting the close stratified class counts. This small statistic difference should not be presented as equivalent in scope to the meta learner’s full supervised ancestry. It does not by itself prove a negligible prediction effect.

## Nonnested Meta-Training Dependencies

For a meta learner $q^{(-a)}$ trained on $\{(z_i,y_i):i\notin V_a\}$ and evaluated on $V_a$, take a meta-training row $i\in V_b$, $b\ne a$. Its features came from base fits on $I\setminus V_b$, a set containing $V_a$. Thus $$\begin{aligned}
y_{V_a}&\longrightarrow h_m^{(-b)}\longrightarrow z_i\\
&\longrightarrow\text{meta-training data}\longrightarrow q^{(-a)}.
\end{aligned}
$$ A row in $V_a$ does receive base features from an estimator fit excluding $V_a$. However, the meta model evaluating that row was trained on other features whose construction used $y_{V_a}$. Row-level OOF exclusion therefore does not isolate the complete stacker. This structural dependency remains even if global preprocessing and class weights are provisionally accepted.

Rebuilding base OOF features only once for all meta folds preserves this path. It must instead be regenerated within the training partition of each outer assessment split, and again within the allowed fitting subset of each selection split. Equation 5 establishes missing isolation, not the magnitude or direction of score distortion. The nested comparison in the supplement is prospective; its result remains an explicit author task.

## Stopping, Near-Uniform Weights, and Selection

LightGBM uses its assessment labels for stopping and later reports macro-F1 on the same rows. Reporting a different objective does not create a new assessment sample. Ensemble weights are functions of the pooled OOF F1 values, so each evaluation label can also affect the aggregation rule.

Using the seven printed four-decimal candidate scores in Equation 4 gives approximate weights 0.154991, 0.158125, 0.134992, 0.111846, 0.127651, 0.154452, and 0.157943 for LR_C8, LR_C3, SVC, CNB, SGD, LightGBM, and Meta-LR respectively (A). Uniform weight is $1/7=0.142857$; the largest absolute departure is about 0.031011. The source used unrounded scores, so these are reconstructed approximations, not recovered fitted weights.

The recorded weighted score 0.5314 exceeds the simple average 0.5306 by 0.0008, or 0.08 percentage points (A). This is a small observed development-set gain. It is *not* an upper bound on leakage or selection optimism: both probability arrays share other evaluation dependencies, and no untouched paired comparison is available. We therefore give this mechanism narrower emphasis than meta-feature ancestry.

Each threshold grid assesses 900 choices on the same OOF labels. Their selected results and unadjusted alternatives are then compared to choose one of four final variants. These are selection opportunities (Varma and Simon 2006; Cawley and Talbot 2010); no measured bias is assigned to them or to the rounded 0.0093 ensemble-versus-base difference.

## Dependence and Uncertainty

The three fitting subsets overlap: each pair shares roughly one-third of the full corpus, or half of either fitting subset. They are not independent repetitions. Stratification addresses class balance but does not protect against duplicates, shared authors, threads, or temporal dependence. Seed-42 fold indices are now regenerated from the supplied CSV using scikit-learn 1.8.0. They are saved with IDs and labels. They are a new reconstruction, not an authenticated historical fold file; their duplicate counts appear below.

There is no universally unbiased K-fold variance estimator based only on observed fold errors (Bengio and Grandvalet 2004). Paired comparisons also require retained row level predictions and a procedure appropriate to the data’s independent units (Dror et al. 2018). We report neither a naive fold-based interval nor a significance claim. Such an interval would not resolve the fitting and selection exposures already traced.

## New Checks and Controlled Comparisons

We regenerate `StratifiedKFold(3, shuffle=True, random_state=42)` without changing row order. A repeated-text group means two or more rows with exactly the same raw string. Of 461 such training groups containing 1,082 rows, 308 groups containing 771 rows span multiple regenerated folds (D). Conflicting labels occur in 52 repeated-text groups containing 130 rows; 36 of those groups span folds. These counts reveal split and annotation dependence, not its effect on macro-F1. No normalization or near-duplicate criterion is used.

<div id="tab:newchecks">

| Check / comparison                       | Result                                                    | Evidence and interpretation                                                                     |
|:-----------------------------------------|:----------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| LR_C3, global TF-IDF                     | New pooled F1 0.522061                                    | New R; same full CSV and folds as the paired arm.                                               |
| LR_C3, training-fold TF-IDF              | New pooled F1 0.518872                                    | New R; fixed global class weights and source solver/settings.                                   |
| Global minus fold-fitted LR              | 0.003189 macro-F1                                         | A; difference in this paired run, not a general bias bound.                                     |
| Non-nested / nested Meta-LR              | Historical 0.5218 / **\[TODO-AUTHOR: run nested stack\]** | R/P; compare newly executed matched arms, not one historical score against one new environment. |
| Exact-text groups spanning folds         | 308 groups; 771 rows                                      | D; regenerated seed-42 indices.                                                                 |
| Repeated-text groups with label conflict | 52 groups; 130 rows                                       | D; 36 groups also span folds.                                                                   |
| Squared-F1 weight range                  | Approx. 0.111846–0.158125                                 | A; computed from rounded scores.                                                                |
| Weighted minus uniform ensemble          | 0.0008 macro-F1                                           | A/R; observed development difference, not a bias bound.                                         |
| Updated CSV consistency                  | 11,955 rows; NOP field 0.183                              | D; IDs/order and class counts match the recorded export.                                        |

New evidence and pending comparisons. D/A results are checks or calculations; new LR scores are explicitly distinguished from historical R. No missing result is inferred from the 0.5314 record.

</div>

The LR script fits all four branches globally in one arm and only on each training fold in the other. Both retain the original global class weights to isolate TF-IDF scope. They use $C=3$, SAGA, multinomial loss, tolerance $10^{-3}$, maximum 2,000 iterations, and seed 42. Software versions, warnings, iterations, probabilities and fold IDs are saved. All six LR fits reach the 2,000-iteration cap and emit convergence warnings (new R). Thus the result describes the source training budget, not converged optima. The global score rounds to the historical 0.5221, but does not authenticate that unknown environment. A fully corrected arm should additionally recompute class weights within each training subset.

The complete notebook is not claimed impossible to rerun. Its historical outputs cannot be replayed from saved fitted objects because those objects and versions were not retained. This audit environment has an 8 GiB memory limit, CPU execution and scikit-learn 1.8.0. LightGBM 4.7.0 was made available for a new run; PyTorch profiling is separate from the classical predictor. The full-data paired LR comparison is completed here. The 54 nested base-candidate objects, stopping refits and matched non-nested arm exceed this revision’s training budget; the supplemental protocol leaves its result as **\[TODO-AUTHOR: execute both stacking arms and insert paired macro-F1 results\]**. A new training run is replication evidence, not recovery of the original fitted states.

# Parameter Boundaries and Score Provenance

## The Identity Module Is a Different Object

The source defines `ZeroParamNet.forward(x)` to return $x$ unchanged. It has no trainable parameters. Profiling, when available, calls this module on a random three-element vector after the selected predictions already exist (S). No invocation applies the module to raw text, base probabilities, meta features, or selected outputs. Its zero count therefore describes a separate identity operation, not the harmful-content predictor.

The retained output prints `Manual NOP: 0` and `Final thop NOP: 0`, without the success line printed by the successful profiling branch. The variable is initialized to zero and remains zero when THOP is unavailable or fails. Consequently, the final printed zero alone cannot establish successful profiling. The source uses one positional input to this separate module, whereas the supplied competition description illustrates a two-input model call with token IDs and an attention mask. These interfaces do not determine a whole-system accounting boundary.

## Structural Inventory of the Selected Predictor

The selected path needs six three-fold base candidates, three Meta-LR fits, seven weights, four fitted vocabularies/IDF arrays and fixed text/numerical rules. No learned PyTorch head is invoked.

At recorded TF-IDF width $D=230{,}105$, each three-class multinomial LR fit has $3D$ coefficients and three intercepts. The two LR candidates each require three fits for their stored test averages. Meta-LR has 18 input probabilities and three output scores: $$\begin{aligned}
N_{\mathrm{one\ base\ LR}}&=3D+3=690{,}318,\\
N_{\mathrm{six\ base\ LR}}&=6(3D+3)=4{,}141{,}908,\\
N_{\mathrm{three\ Meta\ LR}}&=3(3\times18+3)=171.
\end{aligned}
$$ These are arithmetic scalar inventories for specified matrices (A), not measured memory occupancy or a complete contest NOP. Coefficients for SVC and SGD, CNB state, calibrators, LightGBM trees, vocabularies, and IDF arrays remain outside this subtotal. Internal calibration can retain multiple fitted classifiers/functions per outer object; historical defaults and fitted internals are unknown (Pedregosa et al. 2011).

No complete serialized artifact, peak RAM measurement, raw-text inference latency, or energy benchmark is available. Scalar counts, fitted state, bytes, RAM, latency and energy are distinct (Henderson et al. 2020). Comparisons need the same boundary and models that generate probabilities for unseen text.

## Fractional Export Values Are Not Measurements

For the named the HerWILL AI for Digital Safety Datathon 2026 record, the source sets the main export field by rounding $F/2.9$ to three decimal places (S), producing 0.183 (R/D).

This is a target-derived denominator, not a structural parameter measurement. The assigned values 0.183, 0.1, and 0.3 are fractional, whereas a count of scalar parameters is an integer. The separate identity operation has zero trainable parameters; the selected fitted ensemble has additional state. These observations describe implementation and measurement provenance, not a verified organizer ruling or a claim about author intent.

With $F=0.5314177984731835$ and $\epsilon=5\times10^{-16}$, the local ratio $F/(N+\epsilon)$ gives about $1.0628\times10^{15}$ at $N=0$ and 2.9039 at $N=0.183$ (A). These are arithmetic projections, not the new author-reported public/private platform scores. Changing the case name does not change the technical facts or remove the need to document the applicable accounting rules.

## Authoritative Scoring Remains Unresolved

The supplied details document gives $0.4F+0.6/[\log(N+1)+\epsilon]$ without a log base, but later quotes $F/(N+\epsilon)$. The original formula image, official scoring code, and classical-model count boundary remain unavailable. The notebook’s local ratio is source evidence, not verification of the contest contract. Public and private platform values 3.78469 and 3.78930 are author reports (X); hidden-set macro-F1, uploaded-file identity, and acceptance are not inferred from them. Earlier scores from other versions are confined to Supplement S1.

**\[TODO-AUTHOR: provide the scorer and count rule, plus a receipt linked to the submitted file hash\]**. Both naming versions retain these limitations. The anonymized version describes the case as a public datathon; it does not conceal a changed accounting calculation.

# Corrected Prospective Protocol

Freeze data bytes, label meanings, sampling units and permitted uses before assessment. Inspect duplicate/conflict groups; grouping protects repeated text while label conflicts require documented treatment. Keep the regenerated row-stratified comparison separate from a future group-aware evaluation.

For each outer training subset $T_a$ and assessment subset $E_a$, build new inner three-fold base OOF features using only $T_a$. Fit the four TF-IDF branches and class weights within permitted fitting subsets. Calibration remains inside each base fitting subset. LightGBM stopping uses a further training-only partition, never $E_a$. Fit Meta-LR on the new inner OOF features, and generate $E_a$ base features by averaging the same inner fits. This evaluates a specified fold-averaged base predictor. It does not silently equate it with a different final deployment ensemble.

Run the original non-nested arm in the same new environment and save its paired probabilities. The fully corrected nested arm changes preprocessing, class statistics, stopping and feature ancestry jointly; its score difference is a protocol comparison, not a causal estimate of stacking alone. A separate nesting-only sensitivity study must hold the other operations fixed. Reserve ensemble weights, threshold search and candidate choice for training-only selection if evaluating the full selected ensemble. The requested Meta-LR comparison does not automatically validate that full ensemble.

Preserve IDs, labels, folds, probabilities, versions, convergence warnings, fitted objects and stopping choices. Serialize/reload the complete raw-text predictor and check probability equivalence before measuring bytes, peak RAM, latency or energy (Pineau et al. 2021). Define contest NOP using its original rules. Supplement S2 supplies the runnable LR script and complete stacking protocol; unperformed studies retain explicit author tasks.

# Limitations and Responsible Interpretation

The updated source and retained outputs are inspectable, and the supplied CSVs agree with its printed supports. However, no hash recorded during the historical run establishes that those exact bytes were used. The audit regenerates folds, checks a new export, and executes a controlled LR comparison. It does not recover historical OOF rows, inspect historical fitted states, or verify platform acceptance. Unknown package versions and contradictory device metadata limit replay. Exact-string duplication, conflicting labels and regenerated cross-fold allocation are checked. Semantic duplicates and shared-user/thread structure remain unexamined.

The threats are distinct: internal, because fitting and selection use evaluation information; external, because one record does not establish a population claim; construct-related, because label definitions lack a complete annotation manual; statistical, because folds and selection outcomes are dependent; and measurement-related, because the counted identity object differs from the selected predictor. Neither the direction of score distortion nor deployment cost is measured.

The three-way argmax is a research prediction, not a moderation policy. Substring matching can activate inside benign words, and identity-related cues do not model whether a speaker endorses, condemns, quotes, or reclaims an expression (Blodgett et al. 2020; Röttger et al. 2021). No operating threshold, contextual safety, appeal process, or deployment benefit has been established. No legal basis, consent, ethics approval, or independent redistribution permission is inferred from public-source collection or from a supplied license description.

# Conclusion

This case study reconstructs the updated ensemble record: 47,817 training rows, four fitted TF-IDF branches, six base candidates, a Meta-LR component, and a selected weighted ensemble. Its reconstructed macro-F1 0.531418 agrees with the notebook’s 0.5314; the rounded comparison with LR_C3 at 0.5221 remains descriptive. Regenerated folds reveal repeated and conflicting text groups; the new CSV matches recorded export structure and class totals. Historical versions remain supplemental.

Three findings transfer. Row-level OOF exclusion does not isolate a full procedure when evaluation labels remain ancestors of meta-training features, stopping choices, or combination weights. A zero-parameter identity operation does not account for the fitted state that produces harmful-content predictions. A fractional denominator selected to achieve a desired score is not a parameter measurement. Every predictive or efficiency claim should name its inference object, fitting and selection ancestry, accounting boundary, and supporting evidence. This remains an inspectable methodological case, not a validated deployment system.

### Data and Code Availability.

The review artifact contains source, CSV checks, fold indices, scripts, outputs and a digest ledger. **\[TODO-AUTHOR: insert an anonymous review-artifact URL and permanent dataset citation permitted by its terms\]**. **\[TODO-AUTHOR: insert the approved public code/archive URL after blind review\]**. The publicly named repository is documented in the author revision report; it is not substituted for an anonymous review link. Release availability does not itself establish redistribution permission.

### Author Declarations.

**\[TODO-AUTHOR: state actual funding or an author-confirmed no-funding declaration\]**. **\[TODO-AUTHOR: state competing interests\]**. **\[TODO-AUTHOR: state documented ethics approval/exemption, collection basis, data-use and redistribution permissions\]**. **\[TODO-AUTHOR: disclose the prior manuscript’s venue/status, overlap and any simultaneous consideration\]**. AI assistance was used for literature organization, source inspection, arithmetic/data checks, drafting and typesetting. **\[TODO-AUTHOR: all authors approve this disclosure and the final text; document any additional AI use\]**.

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-bender2018datastatements" class="csl-entry">

Bender, Emily M., and Batya Friedman. 2018. “Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science.” Edited by Lillian Lee, Mark Johnson, Kristina Toutanova, and Brian Roark. *Transactions of the Association for Computational Linguistics* 6: 587–604. <https://doi.org/10.1162/tacl_a_00041>.

</div>

<div id="ref-bengio2004variance" class="csl-entry">

Bengio, Yoshua, and Yves Grandvalet. 2004. “No Unbiased Estimator of the Variance of K-Fold Cross-Validation.” *Journal of Machine Learning Research* 5: 1089–1105. <https://www.jmlr.org/papers/v5/grandvalet04a.html>.

</div>

<div id="ref-bhattacharjee2022banglabert" class="csl-entry">

Bhattacharjee, Abhik, Tahmid Hasan, Wasi Ahmad, Kazi Samin Mubasshir, Md Saiful Islam, Anindya Iqbal, M. Sohel Rahman, and Rifat Shahriyar. 2022. “BanglaBERT: Language Model Pretraining and Benchmarks for Low-Resource Language Understanding Evaluation in Bangla.” In *Findings of the Association for Computational Linguistics: NAACL 2022*, edited by Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz, 1318–27. Seattle, United States: Association for Computational Linguistics. <https://doi.org/10.18653/v1/2022.findings-naacl.98>.

</div>

<div id="ref-blodgett2020language" class="csl-entry">

Blodgett, Su Lin, Solon Barocas, Hal Daumé III, and Hanna Wallach. 2020. “Language (Technology) Is Power: A Critical Survey of ‘Bias’ in NLP.” In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*, edited by Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, 5454–76. Online: Association for Computational Linguistics. <https://doi.org/10.18653/v1/2020.acl-main.485>.

</div>

<div id="ref-cawley2010overfitting" class="csl-entry">

Cawley, Gavin C., and Nicola L. C. Talbot. 2010. “On over-Fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation.” *Journal of Machine Learning Research* 11 (70): 2079–2107. <https://jmlr.org/papers/v11/cawley10a.html>.

</div>

<div id="ref-davidson2017automated" class="csl-entry">

Davidson, Thomas, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. “Automated Hate Speech Detection and the Problem of Offensive Language.” *Proceedings of the International AAAI Conference on Web and Social Media* 11 (1): 512–15. <https://doi.org/10.1609/icwsm.v11i1.14955>.

</div>

<div id="ref-dror2018significance" class="csl-entry">

Dror, Rotem, Gili Baumer, Segev Shlomov, and Roi Reichart. 2018. “The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing.” In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, edited by Iryna Gurevych and Yusuke Miyao, 1383–92. Melbourne, Australia: Association for Computational Linguistics. <https://doi.org/10.18653/v1/P18-1128>.

</div>

<div id="ref-hastie2009elements" class="csl-entry">

Hastie, Trevor, Robert Tibshirani, and Jerome Friedman. 2009. *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. 2nd ed. New York: Springer. <https://doi.org/10.1007/978-0-387-84858-7>.

</div>

<div id="ref-henderson2020systematic" class="csl-entry">

Henderson, Peter, Jieru Hu, Joshua Romoff, Emma Brunskill, Dan Jurafsky, and Joelle Pineau. 2020. “Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning.” *Journal of Machine Learning Research* 21 (248): 1–43. <https://jmlr.org/papers/v21/20-312.html>.

</div>

<div id="ref-herwill2026materials" class="csl-entry">

HerWILL. 2026. “<span class="nocase">HerWILL: AI for Digital Safety Datathon 2026</span>: Supplied Competition Description and Dataset Materials.”

</div>

<div id="ref-kapoor2023leakage" class="csl-entry">

Kapoor, Sayash, and Arvind Narayanan. 2023. “Leakage and the Reproducibility Crisis in Machine-Learning-Based Science.” *Patterns* 4 (9): 100804. <https://doi.org/10.1016/j.patter.2023.100804>.

</div>

<div id="ref-ke2017lightgbm" class="csl-entry">

Ke, Guolin, Qi Meng, Thomas Finley, Taifeng Wang, Wei Chen, Weidong Ma, Qiwei Ye, and Tie-Yan Liu. 2017. “LightGBM: A Highly Efficient Gradient Boosting Decision Tree.” In *Advances in Neural Information Processing Systems*. Vol. 30. <https://papers.neurips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html>.

</div>

<div id="ref-vanderlaan2007super" class="csl-entry">

Laan, Mark J. van der, Eric C. Polley, and Alan E. Hubbard. 2007. “Super Learner.” *Statistical Applications in Genetics and Molecular Biology* 6 (1). <https://doi.org/10.2202/1544-6115.1309>.

</div>

<div id="ref-mitchell2019modelcards" class="csl-entry">

Mitchell, Margaret, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. 2019. “Model Cards for Model Reporting.” In *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220–29. Association for Computing Machinery. <https://doi.org/10.1145/3287560.3287596>.

</div>

<div id="ref-niculescumizil2005probabilities" class="csl-entry">

Niculescu-Mizil, Alexandru, and Rich Caruana. 2005. “Predicting Good Probabilities with Supervised Learning.” In *Proceedings of the 22nd International Conference on Machine Learning*, 625–32. ICML ’05. Association for Computing Machinery. <https://doi.org/10.1145/1102351.1102430>.

</div>

<div id="ref-pedregosa2011scikit" class="csl-entry">

Pedregosa, Fabian, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, et al. 2011. “Scikit-Learn: Machine Learning in Python.” *Journal of Machine Learning Research* 12 (85): 2825–30. <https://jmlr.org/papers/v12/pedregosa11a.html>.

</div>

<div id="ref-pineau2021reproducibility" class="csl-entry">

Pineau, Joelle, Philippe Vincent-Lamarre, Koustuv Sinha, Vincent Larivière, Alina Beygelzimer, Florence d’Alché-Buc, Emily Fox, and Hugo Larochelle. 2021. “Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program).” *Journal of Machine Learning Research* 22 (164): 1–20. <https://jmlr.org/papers/v22/20-303.html>.

</div>

<div id="ref-romim2022bdshs" class="csl-entry">

Romim, Nauros, Mosahed Ahmed, Md Saiful Islam, Arnab Sen Sharma, Hriteshwar Talukder, and Mohammad Ruhul Amin. 2022. “BD-SHS: A Benchmark Dataset for Learning to Detect Online Bangla Hate Speech in Different Social Contexts.” In *Proceedings of the Thirteenth Language Resources and Evaluation Conference*, edited by Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, et al., 5153–62. Marseille, France: European Language Resources Association. <https://aclanthology.org/2022.lrec-1.552/>.

</div>

<div id="ref-rottger2021hatecheck" class="csl-entry">

Röttger, Paul, Bertie Vidgen, Dong Nguyen, Zeerak Waseem, Helen Margetts, and Janet Pierrehumbert. 2021. “HateCheck: Functional Tests for Hate Speech Detection Models.” In *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, edited by Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli, 41–58. Online: Association for Computational Linguistics. <https://doi.org/10.18653/v1/2021.acl-long.4>.

</div>

<div id="ref-schwartz2020greenai" class="csl-entry">

Schwartz, Roy, Jesse Dodge, Noah A. Smith, and Oren Etzioni. 2020. “Green AI.” *Communications of the ACM* 63 (12): 54–63. <https://doi.org/10.1145/3381831>.

</div>

<div id="ref-vaicenavicius2019calibration" class="csl-entry">

Vaicenavicius, Juozas, David Widmann, Carl Andersson, Fredrik Lindsten, Jacob Roll, and Thomas Schön. 2019. “Evaluating Model Calibration in Classification.” In *Proceedings of the Twenty-Second International Conference on Artificial Intelligence and Statistics*, edited by Kamalika Chaudhuri and Masashi Sugiyama, 89:3459–67. Proceedings of Machine Learning Research. PMLR. <https://proceedings.mlr.press/v89/vaicenavicius19a.html>.

</div>

<div id="ref-varma2006bias" class="csl-entry">

Varma, Sudhir, and Richard Simon. 2006. “Bias in Error Estimation When Using Cross-Validation for Model Selection.” *BMC Bioinformatics* 7 (1): 91. <https://doi.org/10.1186/1471-2105-7-91>.

</div>

<div id="ref-wolpert1992stacked" class="csl-entry">

Wolpert, David H. 1992. “Stacked Generalization.” *Neural Networks* 5 (2): 241–59. <https://doi.org/10.1016/S0893-6080(05)80023-1>.

</div>

</div>

[^1]: Consulted API: <https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html>.


## 4. Change log

| Section | What changed | Why | Priority |
|---|---|---|---|
| Title/abstract | Audit title; abstract under200 words | Clarify contribution and reduce length | P3 |
| Header | Neutral draft header and explicit confirmation marker | No invented publisher metadata or empty commas | P1 |
| Related work | Super Learner/ESL references; focused literature | Ground evaluation arguments without claiming oracle guarantees | P2 |
| Study design | Author runtime/scores marked X; new execution separated | Prevent provenance and metric conflation | P1 |
| Data | Duplicate/conflict reconstruction and new CSV consistency | Replace missing cheap checks and outdated export limitation | P2 |
| Features | Explain sala substring example | Define jargon and mechanism | P2 |
| Evaluation6.1 | Six-level structural taxonomy; class-statistic diagnostic | Avoid flattening distinct exposures | P1 |
| Evaluation6.3 | Approximate seven weights; narrow interpretation of0.0008 | Magnitude is observed, not a leakage bound | P1 |
| Evaluation6.5 | New LR experiment status/results and explicit nested TODO | Provide measurements where executed, never invented values | P1 |
| NOP7.3 | Named/public-datathon options; neutral provenance language | Authors choose disclosure scope; technical facts retained | P1 |
| NOP7.4 | Current score reports separated from local ratio | No unsupported official formula inference | P1 |
| Protocol | Runnable LR script plus nested design/inference policy | Make the requested future work executable/reviewable | P1 |
| Availability | Anonymous/public artifact-link fields | Support reproducibility without exposing authors during review | P2 |
| Declarations | Explicit factual TODO fields and prior-manuscript status | Only authors can attest to funding/ethics/approval | P1/P2 |
| Supplement | Move old TinyLinear/NOP39/four-class provenance | Focus main paper on one pipeline | P2 |
| Venue note | Official scope/indexing and submission rules checked | Flag fit and institutional requirements without selecting venue | P1 |

Repeated phrasing was reduced and long sentences split. Correct arithmetic was retained. The word “establish” and disclaimers were not deleted where they prevent a false scientific interpretation. The final source diff and build record give an inspectable change history.

## 5. Author must do

- [ ] Choose named-case A or public-datathon B; check applicable competition rules. Naming changes cannot settle permissions or hide different mathematics.
- [ ] Supply the other two authors’ exact names/order, all affiliations/emails and corresponding author. Shamim Hasan is the confirmed first author. Keep review PDF anonymous.
- [ ] Obtain all authors’ approval of the audit findings, revised text and AI-assistance statement.
- [ ] State actual funding and competing interests. Do not replace missing information with invented “none” declarations.
- [ ] Supply documented ethics approval/exemption and data-use/redistribution permissions. A copied license description is not independently verified release permission.
- [ ] Disclose the older manuscript’s submission/publication status and overlap; resolve any simultaneous-review issue using the actual facts.
- [ ] Obtain the original F1NOP equation, log base (if applicable), supported classical-model parameter boundary and original rules.
- [ ] Link the author-reported scores/runtime/hardware to a submission/run receipt and the exact uploaded CSV hash. Do not supply hidden test labels.
- [ ] Execute the pending matched non-nested/nested comparison, or deliberately retain a narrower audit and obtain author/editor agreement on its scope. Under the reviewer’s requested empirical standard, this remains a major outstanding item.
- [ ] If LR runs hit iteration limits, report that fact; any longer-training sensitivity experiment is a new result, not a silent replacement of the recorded arithmetic.
- [ ] Add an anonymous review artifact URL and a permanent dataset citation. Use the named public repository link only where blind-review policy permits, or after acceptance.
- [ ] Confirm the neutral review header with venue instructions. Publication volume/issue/page metadata must come from the publisher.
- [ ] Remove every visible TODO only after supplying the underlying information/results, then recompile and inspect page count/layout.
- [ ] Confirm IJCVSP/ICIEV fit and any institutional indexing requirement; the official journal site says it is not currently Scopus-indexed.
- [ ] Enter all authors accurately in the existing CMT submission if one exists; upload the selected anonymous PDF, not the repository ZIP; retain confirmation. No portal action was performed here.

## 6. Verified references and references to verify

### Verified scholarly additions

1. Mark J. van der Laan, Eric C. Polley and Alan E. Hubbard. “Super Learner.” Statistical Applications in Genetics and Molecular Biology 6(1), Article 25 (2007). DOI:10.2202/1544-6115.1309. Author/institutional record verifies journal details; Berkeley working paper verifies authors and cross-validated-combination contribution.
   https://mayoclinic.elsevierpure.com/en/publications/super-learner/
   https://biostats.bepress.com/ucbbiostat/paper222/
2. Trevor Hastie, Robert Tibshirani and Jerome Friedman. The Elements of Statistical Learning: Data Mining, Inference, and Prediction, second edition. Springer, New York (2009). DOI:10.1007/978-0-387-84858-7. Section 7.10.2 discusses the wrong/right way to cross-validate; its supervised-selection example is not itself a measured TF-IDF bias result.
   https://link.springer.com/book/10.1007/978-0-387-84858-7
   https://web.stanford.edu/class/archive/stats/stats202/stats202.1162/content/lec11.pdf

The existing LightGBM primary reference and focused existing citations are retained; unused inherited entries were removed from the revised bibliography. No new DOI, quotation or experimental score was fabricated.

### Operational source and unresolved references

- The supplied HerWILL 2026 competition description/dataset materials are cited as an operational artifact, explicitly not as a verified dataset publication or DOI. [TODO-AUTHOR: supply original release citation, creators/version, permanent URL and terms.]
- [TODO-AUTHOR: authoritative F1NOP scorer, exact equation/log base/count boundary and competition rules.] Public Kaggle overview/rules could not be retrieved during this revision.
- [TODO-AUTHOR: original annotation manual, collection documentation and license/permission record.]
- [TODO-AUTHOR: prior manuscript citation/status if previously submitted/published; otherwise declare its actual internal-draft status.]
- Unverified “related paper” titles in the supplied DOCX were not introduced as scholarly citations. Do not add them without primary bibliographic verification.

### Venue/reference checks

- Scope: https://cennser.org/IJCVSP/scope.html — AI/ML/pattern recognition are expressly listed.
- Indexing statement: https://cennser.org/IJCVSP/ — explicitly not currently Scopus-indexed.
- Conference topics: https://cennser.org/ICIEV/scope-topics.html
- Format/blind review/authors: https://cennser.org/ICIEV/paper-submission.html
- Dates: https://cennser.org/ICIEV/important-dates.html — regular paper 20 October 2026; closing time/timezone unverified.
- sklearn 1.8 multinomial behavior: https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html

GitHub read access worked; creating a revision branch returned403 Resource not accessible by integration. No remote PR, merge or conference submission was created. The prepared local revision files are the reviewable handoff.
