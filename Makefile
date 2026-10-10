.PHONY: verify paper
verify:
	python3 scripts/verify_artifacts.py
paper:
	cd paper/iciev && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
