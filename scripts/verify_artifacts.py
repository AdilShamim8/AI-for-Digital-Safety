#!/usr/bin/env python3
"""Verify supplied artifacts without training or changing original data.

Only Python's standard library is required. This script verifies file content
and arithmetic; it does not authenticate notebook execution or hidden labels.
"""
import argparse
import collections
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify():
    data = ROOT / "data/herwill_2026"
    train_cols, train = csv_rows(data / "train.csv")
    test_cols, test = csv_rows(data / "test.csv")
    sample_cols, sample = csv_rows(data / "sample_submission.csv")
    sub_cols, sub = csv_rows(data / "submission.csv")
    assert train_cols == ["id", "text", "y"]
    assert test_cols == ["id", "text"]
    assert sample_cols == sub_cols == ["id", "y_pred", "parameters"]
    assert len(train) == 47817 and len(test) == len(sample) == len(sub) == 11955
    supports = dict(collections.Counter(r["y"] for r in train))
    predictions = dict(collections.Counter(r["y_pred"] for r in sub))
    assert supports == {"0": 23756, "1": 18163, "2": 5898}
    assert predictions == {"0": 5501, "1": 4139, "2": 2315}
    assert {r["parameters"] for r in sub} == {"39"}
    assert [r["id"] for r in test] == [r["id"] for r in sample] == [r["id"] for r in sub]
    assert not (set(r["id"] for r in train) & set(r["id"] for r in test))
    for rows in [train, test]:
        assert len(set(r["id"] for r in rows)) == len(rows)
        assert not any(v == "" for r in rows for v in r.values())
    train_texts = set(r["text"] for r in train)
    test_texts = set(r["text"] for r in test)
    exact_text = {
        "training_repeats_beyond_first": len(train) - len(train_texts),
        "test_repeats_beyond_first": len(test) - len(test_texts),
        "distinct_texts_shared_between_train_test": len(train_texts & test_texts),
    }
    assert exact_text == {"training_repeats_beyond_first": 621,
                          "test_repeats_beyond_first": 54,
                          "distinct_texts_shared_between_train_test": 254}
    versions = {}
    for name, original in [("train.csv", train), ("test.csv", test), ("sample_submission.csv", sample)]:
        cols, larger = csv_rows(ROOT / "data/four_class_version" / name)
        assert larger[-len(original):] == original
        versions[name] = {"rows": len(larger), "columns": cols,
                          "three_class_exact_trailing_subset": True,
                          "duplicate_id_rows_beyond_first": len(larger) - len(set(r["id"] for r in larger))}
        if name == "train.csv":
            versions[name]["class_supports"] = dict(collections.Counter(r["y"] for r in larger))
            assert versions[name]["class_supports"] == {"0":25567,"1":20250,"2":7789,"3":1211}
    notebook_path = ROOT / "notebooks/AI_for_Digital_Safety_Notebook.ipynb"
    notebook = json.loads(notebook_path.read_text())
    code_cells = [(i,c) for i,c in enumerate(notebook["cells"]) if c["cell_type"] == "code"]
    source = "\n\n".join("".join(c["source"]) for _,c in code_cells)
    outputs = "\n".join("".join(o.get("text", o.get("data",{}).get("text/plain",[])))
                        for _,c in code_cells for o in c.get("outputs",[]))
    assert len(notebook["cells"]) == 37 and len(code_cells) == 18
    assert re.search(r"NUM_CLASSES\s*=\s*4",source)
    assert "Train shape: (54817, 3)" in outputs
    assert "Feature matrix: (54817, 255081)" in outputs
    assert "Manual NOP : 68" in outputs and "WINNER: SVC" in outputs
    notebook_info = {"total_cells":37,"code_cells":18,"sha256":sha256(notebook_path),
                     "metadata_papermill":notebook["metadata"]["papermill"],
                     "matches_three_class_paper_execution":False}
    # These nine counts are manuscript-reported inputs, not verified OOF rows.
    updated_path=ROOT / 'notebooks/ai-for-digital-safety-101.ipynb'
    updated=json.loads(updated_path.read_text())
    assert len(updated['cells']) == 1 and updated['cells'][0]['execution_count'] == 1
    updated_source=''.join(updated['cells'][0]['source'])
    updated_outputs='\n'.join(''.join(o.get('text',o.get('data',{}).get('text/plain',[])))
                              for o in updated['cells'][0]['outputs'])
    assert len(updated_source.splitlines()) == 971
    assert re.search(r'NUM_CLASSES\s*=\s*3',updated_source)
    assert re.search(r'N_FOLDS\s*=\s*3',updated_source)
    for value in ['Train: 47,817 | Test: 11,955','Combined: (47817, 230105)',
                  'Shape: (47817, 230125)','Best: weighted F1=0.5314',
                  'Manual NOP: 0','submission.csv (NOP=0.183)']:
        assert value in updated_outputs, value
    assert 'return x  # pure identity' in updated_source
    assert 'nop_for_target = final_f1 / 2.9' in updated_source
    assert [r['id'] for r in test[:5]] == ['7891','58497','8995','17207','3148']
    current_info={'sha256':sha256(updated_path),'source_sha256':hashlib.sha256(updated_source.encode()).hexdigest(),
                  'cells':1,'source_lines':971,'folds':3,'base_candidates':6,
                  'metadata_papermill':updated['metadata']['papermill'],
                  'recorded_test_predictions':{'0':6414,'1':4401,'2':1140},
                  'recorded_main_export_nop':.183,'recorded_profiled_identity_nop':0,
                  'generated_csvs_supplied':False,'fresh_prediction_replay_performed':False}
    # Counts transcribed from the retained updated-notebook figure. No row-level replay.
    cm = [[16464,6331,961],[7502,9039,1622],[1360,2292,2246]]
    rows = [sum(r) for r in cm]
    cols = [sum(cm[i][j] for i in range(3)) for j in range(3)]
    f1 = [2*cm[c][c]/(rows[c]+cols[c]) for c in range(3)]
    macro = sum(f1)/3
    assert rows == [23756,18163,5898] and cols == [25326,17662,4829]
    assert abs(macro-.5314177984731835)<1e-15
    arithmetic = {"input_provenance":"updated notebook retained confusion figure; no historical prediction replay",
                  "confusion_matrix":cm,"class_f1":f1,"macro_f1":macro,
                  "accuracy":sum(cm[i][i] for i in range(3))/47817,
                  "one_base_lr_scalars_width_230105":3*230105+3,
                  "six_base_lr_scalars_width_230105":6*(3*230105+3),
                  "three_meta_lr_scalars_18_inputs":3*(3*18+3),
                  "local_ratio_at_zero":macro/5e-16,
                  "local_ratio_at_exported_fraction":macro/(.183+5e-16),
                  "target_derived_export":round(macro/2.9,3),
                  "three_major_training_sections_seconds":2601.7+2625.0+3802.8}
    manuscript=(ROOT / "paper/iciev/main.tex").read_text()
    assert not any(m in manuscript for m in ["\\verifyauthor","\\needexp","\\notestablished","citationneeded"])
    assert manuscript.count("\\begin{table") == 5
    assert manuscript.count("\\begin{equation}") == 6
    # Verify verbatim archive extraction and ZIP integrity.
    with zipfile.ZipFile(ROOT / "archives/her-will-ai-for-digital-safety-datathon-2026.zip") as z:
        assert z.testzip() is None
        for name in ["train.csv","test.csv","sample_submission.csv"]:
            assert z.read(name) == (data/name).read_bytes()
    for archive in (ROOT / "archives").rglob("*.zip"):
        with zipfile.ZipFile(archive) as z: assert z.testzip() is None, str(archive)
    return {"verification_scope":"artifact consistency and arithmetic; no model training or historical authentication",
            "three_class_dataset":{"training_rows":len(train),"test_rows":len(test),"supports":supports,
                                   "submission_predictions":predictions,"submission_nop":39,
                                   "submission_ids_and_order_match":True,"exact_text_overlap":exact_text},
            "larger_four_class_files":versions,"legacy_four_class_notebook":notebook_info,
            "updated_notebook":current_info,
            "manuscript_arithmetic":arithmetic,
            "unresolved":["updated generated submission CSVs and row-level OOF probabilities not supplied",
                          "authoritative scoring equation/log base and parameter-count boundary",
                          "updated fitted artifacts, historical runtime/package versions, and prediction replay",
                          "two coauthor names, emails/affiliations, author approval, and disclosures"]}


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--write-report",action="store_true")
    args=parser.parse_args()
    report=verify()
    if args.write_report:
        (ROOT/"audit/verification.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
