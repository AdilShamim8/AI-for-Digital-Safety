.PHONY: verify verify-probabilities paper paper-anonymized
verify:
	python3 scripts/verify_artifacts.py
	python3 scripts/verify_revision.py
	python3 scripts/verify_release.py
verify-probabilities: verify
	python3 scripts/verify_revision.py --probabilities
paper:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
paper-anonymized:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error main_anonymized.tex

.PHONY: paper-supplement verify-followup
paper-supplement:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error supplement.tex
verify-followup:
	python3 submission_revision/scripts/verify_followup.py --repo . --revision submission_revision
