# Three-class competition files

The train/test/sample CSVs are verbatim from the original 2026 archive.
`submission.csv` is the older NOP-39 export (5,501 /4,139 /2,315 labels).
`submission_updated.csv` is the newly supplied export checked on 11 October2026:
11,955 rows; correct test IDs/order; 6,414 /4,401 /1,140 labels; constant0.183.
It matches the canonical notebook's recorded aggregate export, but prediction
origin and exact platform upload identity are not authenticated. The fractional
field is target-derived, not a measured parameter count. Both originals remain
unchanged. Do not treat either file as a corrected official parameter report.
