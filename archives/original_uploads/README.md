# LightBanglaHC — Springer LNCS submission package

Converted from the supplied Elsevier CAS assembly (32 pages) into the supplied
official Springer LNCS template (`llncs.cls` v2.25, `splncs04.bst`), compressed
to **12 pages including references**.

## Files

| File | Role |
|---|---|
| `main.tex` | Complete manuscript (single file; LNCS `runningheads` class option). |
| `references.bib` | Bibliography, 25 entries, all cited. |
| `llncs.cls` | Springer LNCS document class (from the supplied template package). |
| `splncs04.bst` | Springer LNCS BibTeX style (from the supplied template package). |
| `pipeline.pdf` | Figure 1, the source-derived pipeline schematic (unchanged from the original package). |
| `main.pdf` | Compiled 12-page PDF for visual verification. |

## Build

```sh
tectonic main.tex          # tested: Tectonic 0.15.0, clean build
# or
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

No external files beyond those listed are required.

## What changed in the conversion

- Document class, front matter, citation style, float style and bibliography
  converted from Elsevier CAS to LNCS. `\citet`/`\citep` (natbib) were replaced
  by plain `\cite` as `splncs04` expects.
- Length reduced from ~16,200 words of body text to ~3,700 by removing
  repetition and enumerated audit scaffolding, not by removing findings.
  All recorded values, arithmetic reconstructions, equations, evidence
  classes and epistemic qualifications are preserved.
- Floats reduced from 15 tables + 2 figures to 3 tables + 1 figure. The
  dataset-support table, evidence-type table and accounting table were folded
  into prose (all numbers retained); the recorded-results and per-fold tables
  were merged; the confusion matrix and classwise metrics were merged. The
  prospective nested-protocol figure (`nested_protocol.pdf` in the original
  package) was dropped for space; its content is retained as prose in Sect. 8.
- References reduced from 29 to 25 (all cited, none invented, none altered).
  Removed: `vanderlaan2007superlearner`, `guo2017calibration`,
  `gebru2021datasheets`, `wang2012baselines` — each had a surviving
  substitute citation in the same argument.
- Classwise precision/recall/F1 in Table 3 are shown to 4 decimals (they were
  6 in the source) purely to fit the LNCS text width; the exact values follow
  from the tabulated counts and the pooled 0.529547 is still given at full
  precision.

## Verification performed

- Every numeric claim was recomputed from the recorded counts
  (supports, shares, balanced weights, confusion margins, classwise P/R/F1,
  pooled macro-F1 0.529547, accuracy 0.563544, the 0.221275 reference,
  parameter counts 39 / 195 / 764,952 / 3,824,760, all score-provenance
  values and the 1/39 bound). All agree with the source manuscript.
- No undefined citations or references; every table and the figure are cited
  in the text; no multiply-defined labels; worst remaining overfull box is
  2.5 pt (≈0.9 mm, not visible).

## Required before submission (not resolvable from the supplied material)

1. **Authors, affiliations, corresponding e-mail and ORCIDs.** The author block
   is intentionally unfilled and marked `[AUTHOR TO VERIFY]`; the source package
   states author facts must not be inferred. Replace the block in `main.tex`
   (lines under "AUTHOR BLOCK") and the `\authorrunning` entry.
2. **Declarations**: funding, competing interests, ethics status, data
   permissions, annotator-welfare documentation, acknowledgements, and the
   venue's generative-AI disclosure.
3. **Venue rules**: LNCS is a series, not a conference. Confirm the specific
   conference's page limit, whether references count toward it, whether a
   blinded version is required, and whether supplementary material is allowed.
4. **Evidence markers**: the `[REQUIRES NEW EXPERIMENT]`, `[AUTHOR TO VERIFY]`
   and `[NOT ESTABLISHED BY AVAILABLE EVIDENCE]` markers are deliberate and were
   retained as instructed. They can be resolved only by supplying the missing
   experiments, artifacts and governance records — not by editing the text.
