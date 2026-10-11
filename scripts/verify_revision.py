"""Verify the delivered revision without training models or changing artifacts."""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = ROOT / 'revision_2026-10-11'


def verify(probabilities=False):
    paper = ROOT / 'paper/iciev'
    manuscript = '\n'.join(path.read_text() for path in paper.glob('*.tex'))
    references = (paper / 'references.bib').read_text()
    citation_keys = set()
    for group in re.findall(r'\\cite\w*\*?(?:\[[^]]*\])?\{([^}]+)\}', manuscript):
        citation_keys.update(key.strip() for key in group.split(','))
    bibliography_keys = re.findall(r'@\w+\s*\{\s*([^,]+),', references)
    missing = citation_keys - set(bibliography_keys)
    if missing:
        raise ValueError('Missing bibliography entries: ' + ', '.join(sorted(missing)))
    if len(bibliography_keys) != len(set(bibliography_keys)):
        raise ValueError('Duplicate bibliography keys')
    result_path = REVISION / 'audit/lr_comparison/results.json'
    result = json.loads(result_path.read_text())
    if result['status'] != 'completed':
        raise ValueError('Paired experiment is incomplete')
    for arm in ['global', 'within_fold']:
        record = result['arms'][arm]
        if not record['completed'] or len(record['folds']) != 3:
            raise ValueError('Incomplete arm: ' + arm)
    calculated_delta = (result['arms']['global']['pooled_macro_f1']
                        - result['arms']['within_fold']['pooled_macro_f1'])
    if abs(calculated_delta - result['global_minus_within_fold']) > 1e-14:
        raise ValueError('Inconsistent paired delta')
    for name, digest in json.loads((result_path.parent / 'OUTPUT_HASHES.json').read_text()).items():
        if hashlib.sha256((result_path.parent / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Changed OOF artifact: ' + name)
    raw_train = ROOT / 'data/herwill_2026/train.csv'
    if hashlib.sha256(raw_train.read_bytes()).hexdigest() != result['train_sha256']:
        raise ValueError('Training data do not match the measured comparison')
    with zipfile.ZipFile(ROOT / 'releases/LightBanglaHC_Revised_Overleaf.zip') as bundle:
        if bundle.testzip() is not None:
            raise ValueError('Corrupt source ZIP')
        for name in ['main.tex', 'main_anonymized.tex', 'references.bib',
                     'ijcvsplatex.cls', 'ijcvsplatex-num.bst', 'LogoIJCVSP.pdf',
                     'main.pdf', 'main_anonymized.pdf', 'supplement.tex', 'supplement.pdf',
                     'new-evidence.tex', 'supplement-summary.tex', 'convergence-table.tex',
                     'ledger-table.tex']:
            if bundle.read(name) != (paper / name).read_bytes():
                raise ValueError('Stale Overleaf file: ' + name)
    if probabilities:
        import numpy as np
        from sklearn.metrics import f1_score
        arrays = []
        for arm in ['global', 'within_fold']:
            with np.load(result_path.parent / (arm + '_oof.npz')) as data:
                if data['prob'].shape != (47817, 3):
                    raise ValueError('Unexpected probability shape')
                if not np.isfinite(data['prob']).all() or not np.allclose(data['prob'].sum(1), 1):
                    raise ValueError('Invalid probabilities')
                score = float(f1_score(data['y'], data['prob'].argmax(1), average='macro'))
                if abs(score - result['arms'][arm]['pooled_macro_f1']) > 1e-14:
                    raise ValueError('OOF score mismatch: ' + arm)
                arrays.append(tuple(data[key].copy() for key in ['id', 'y', 'fold']))
        if not all(np.array_equal(a, b) for a, b in zip(*arrays)):
            raise ValueError('Arms do not have identical row/fold alignment')
    print('Revision checks passed: citations, paired records, data/output hashes and source ZIP'
          + ('; pooled probability scores and alignment' if probabilities else ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--probabilities', action='store_true',
                        help='Also recompute pooled F1; requires the LR environment dependencies')
    verify(parser.parse_args().probabilities)
