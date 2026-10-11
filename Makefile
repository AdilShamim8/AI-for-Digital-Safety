.PHONY: verify verify-probabilities paper paper-anonymized
verify:
	python3 scripts/verify_artifacts.py
	python3 scripts/verify_revision.py
verify-probabilities: verify
	python3 scripts/verify_revision.py --probabilities
paper:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
paper-anonymized:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error main_anonymized.tex
