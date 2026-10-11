# LightBanglaHC audit: revision and submission checks

The revised source preserves the supplied ICIEV/IJCVSP class, bibliography style, logo, font size and column dimensions. The review PDF is anonymous. It uses one named competition case consistently and includes Supplements S1 and S2 in the main PDF, with a separate detailed supplement and execution package.

## Cross-check and changes

| Finding | Correction | Priority |
|---|---|---|
| Attached PDF is the older ten-page export, not the revision containing the paired LR run | Work from the current revised LaTeX; preserve the attachment as the historical reference | P1 |
| Historical and new executions share the tag R | Reserve R for historical output; label new execution N | P2 |
| Nested stack table missing | Execute the full-data reduced LR_C3/SGD/CNB/Meta-LR comparison; report the actual matched outputs | P1 |
| All six initial SAGA LR fits hit 2,000 iterations | Retain the cap warning and run a separate LBFGS sensitivity for the same C=3 multinomial L2 objective | P1 |
| Saved probabilities not used for uncertainty | Add conditional paired row and raw-text cluster bootstrap intervals, with limits stated | P1 |
| Duplicate checks use only raw strings | Apply the notebook cleaner C(x), construct group-aware folds, and execute exclusion/group sensitivities | P2 |
| Scorer plausibility treated as evidence of the official formula | Keep reconstruction conditional; do not infer an official formula from valid implied F1 values | P1 |
| Platform scores have no linked receipt | Remove them from the main paper | P2 |
| Prompt text and naming alternatives remain | Remove editorial instructions and use one naming version | P1 |
| Blank publication fields or invented volume/year/page metadata | Suppress publisher-assigned metadata in the review header; retain the provided template | P1 |
| Supplement and ledger references lack attachments | Include S1/S2 summaries in the main PDF, plus detailed supplement, scripts, outputs and full SHA-256 ledger | P1 |
| No funding, conflict, prior-draft statements | Use the author's confirmations: no funding or conflicts; TinyLinear was an internal draft, never submitted or published; all authors approve | P1 |
| Ethics and permissions wording not provided | State accurately that these identifiers/records are absent from the available audit record; do not invent approval or a licence grant | P1 |
| AI disclosure says only drafting | Disclose that the assistant also executed the new experiments | P2 |
| Related work thin | Add verified Breiman (1996), Ting and Witten (1999), Kaufman et al. (2012), and prior Bengali data work (2020) | P2 |
| Abstract too long and conclusions omit empirical result | Shorten abstract below 200 words and include the paired LR and reduced stacking results in the conclusion | P3 |

## Confirmations actually received

The author selected: no funding or conflicts; the earlier manuscript was an internal draft and all authors approve. The author also selected “confirmed records available” for ethics/data permissions and then “provide exact wording,” but did not supply any approval/exemption wording, identifier, issuing body or actual permission document. These selections alone do not establish the contents of those records.

## Author requirements before calling this ready for direct submission

1. Supply and check the actual ethics approval/exemption and dataset-use/redistribution permission. The current paper openly states what the available audit record lacks. If records exist, replace that sentence with the accurate documented statement.
2. Execute and inspect `author_replication.ipynb` in the author's own environment. The saved assistant-executed predictions reproduce the two numerical scores when rescored; that is not independent author execution. No author Kaggle link or screenshots are fabricated.
3. Enter all three authors, in the agreed order, with correct affiliations and emails in the submission portal. Author identities remain excluded from the double-blind review PDF.
4. Verify the current conference edition, deadline, track and supplementary-file policy in the live portal. Upload the review PDF, not the entire repository ZIP, as the main manuscript. The ZIP is the Overleaf/reproducibility package.
5. Check the official scoring formula and scalar-count boundary before claiming any platform score or organizer ruling. The main paper omits unreceipted leaderboard values.
6. Confirm any scholarship/employment indexing requirements independently. Do not assume ICIEV proceedings and IJCVSP journal indexing are interchangeable.

## Venue fit and indexing

Checked 11 October 2026: the ICIEV submission page recommends 6–10 pages in the two-column template and requires double-blind review, with author details entered in CMT. IJCVSP's scope includes machine learning/AI as well as vision and signal processing, so an ML evaluation audit has a possible scope connection; this is not an acceptance prediction. The journal's own website says it is not currently indexed in Scopus. Conference proceedings indexing must be checked separately for the actual edition and track.

Primary venue sources:
- https://cennser.org/ICIEV/paper-submission.html
- https://cennser.org/IJCVSP/
- https://cennser.org/IJCVSP/scope.html

## Verified additional references

- Leo Breiman. Stacked Regressions. Machine Learning 24, 49–64 (1996). DOI: 10.1023/A:1018046112532. Primary publisher record: https://link.springer.com/article/10.1023/A:1018046112532
- Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. Journal of Artificial Intelligence Research 10, 271–289 (1999). DOI: 10.1613/jair.594. Primary record: https://jair.org/index.php/jair/article/view/10228
- Shachar Kaufman, Saharon Rosset, Claudia Perlich and Ori Stitelman. Leakage in Data Mining: Formulation, Detection, and Avoidance. ACM Transactions on Knowledge Discovery from Data 6(4), Article 15, pp. 15:1–15:21 (2012). DOI: 10.1145/2382577.2382579. Primary record: https://dl.acm.org/doi/10.1145/2382577.2382579
- Nauros Romim, Mosahed Ahmed, Hriteshwar Talukder and Md Saiful Islam. Hate Speech Detection in the Bengali Language: A Dataset and Its Baseline Evaluation. arXiv:2012.09686 (2020), preprint. DOI: 10.48550/arXiv.2012.09686. Primary record: https://arxiv.org/abs/2012.09686

## References and provenance still to verify

The competition documentation is an operational source retained with the artifacts, not an independently verified permanent dataset publication. Its scoring image/implementation, actual dataset licence grant, annotation manual, consent/ethics records and score receipt remain absent from the supplied audit record. No DOI or official scorer URL has been invented. Published venue metadata is assigned by the publisher and should not be filled with guesses.

Verified portal link from the live ICIEV page: https://cmt3.research.microsoft.com/ICIEV2026/Submission/Index . The page routes to login; this does not verify that submissions are currently open or that supplementary ZIPs are accepted.

## Important new sensitivity finding

The optimizer sensitivity changes the headline gap. Source-budget SAGA gives global-minus-fold-fitted F1 0.003189334107. LBFGS, with all six original-corpus fits stopping below the iteration cap and recorded objective gradients below 1e-6, gives 0.523142776830 versus 0.521393154554: difference 0.001749622276. The “four times 0.0008” comparison therefore applies only to the source-budget SAGA contrast. It must not be presented as a converged, optimizer-independent leakage magnitude. The abstract, discussion and conclusion now state this qualification.

The author's reported runtime 2 h 32 min 37 s equals 9,157 s; the notebook metadata gives 9,142.89 s, a difference of 14.11 s. The reported T4 ×2 allocation and runtime are unreceipted X evidence. They do not demonstrate GPU use by the sklearn estimators or LightGBM. The paper retains historical section timings and their correct 9,029.5 s (about 150.5 min) subtotal.

## Completed new results

| Comparison | Pooled macro-F1 | Qualification |
|---|---:|---|
| SAGA LR, global TF-IDF | 0.522060895664 | Original source iteration budget; cap reached |
| SAGA LR, fold-fitted TF-IDF | 0.518871561557 | Same folds/global class weights; cap reached |
| LBFGS LR, global TF-IDF | 0.523142776830 | Stopped below cap; objective gradient below 1e-6 |
| LBFGS LR, fold-fitted TF-IDF | 0.521393154554 | Same penalized objective and global weights |
| Reduced nonnested stack | 0.517144287830 | Same outer assessment base probabilities as nested arm |
| Reduced nested stack | 0.515690484873 | Inner OOF rebuilt within each outer training subset |
| LBFGS LR, cleaner-group split | 0.519044181991 | Zero cleaned-text group overlap; local TF-IDF/weights |
| LBFGS LR, raw-crossing rows excluded, original folds retained | 0.518443086953 | Remove all 771 crossing rows; 47,046 rows remain; zero raw group overlap |
| LBFGS LR, excluded corpus then resplit | 0.517604025178 | Additional sensitivity; 101 raw groups cross the new folds |

All results are assistant-executed N evidence, not an independently run author notebook. A separate verification script passed 106 checks: manual confusion-matrix rescoring, row/fold identity, probability validity, both meta-only refits matching saved predictions, optimizer diagnostics and unchanged template assets. The main PDF is ten pages; the separate detailed supplement is three pages. Both were visually inspected. Neither current manuscript source/PDF contains TODO-AUTHOR strings or unfinished naming alternatives.
