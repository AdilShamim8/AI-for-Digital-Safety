#!/usr/bin/env python3
"""Check the delivered payload and scientific ledger without training models.

Refreshing the payload manifest is an explicit maintainer operation and uses
Git's tracked/unignored file list. Ordinary verification never updates hashes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'audit/manifest.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_entry(base, relative):
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError('Manifest path leaves its declared directory')
    if not path.is_file():
        raise ValueError('Missing artifact: ' + relative)
    return path


def refresh():
    names = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
        cwd=ROOT).decode().split('\0')
    files = []
    for name in sorted(set(filter(None, names))):
        path = ROOT / name
        if path.is_file() and path != MANIFEST:
            files.append({'path': name, 'bytes': path.stat().st_size,
                          'sha256': digest(path)})
    MANIFEST.write_text(json.dumps({
        'scope': 'Repository payload; this manifest itself and ignored build/rerun files excluded',
        'files': files}, indent=2) + '\n')


def verify():
    entries = json.loads(MANIFEST.read_text())['files']
    names = [entry['path'] for entry in entries]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate manifest paths')
    for entry in entries:
        path = resolve_entry(ROOT, entry['path'])
        if path.stat().st_size != entry['bytes'] or digest(path) != entry['sha256']:
            raise ValueError('Payload digest/size mismatch: ' + entry['path'])
        if re.search(rb'ghp_[A-Za-z0-9]{20,}', path.read_bytes()):
            raise ValueError('Credential pattern found; publication blocked')
    revision = ROOT / 'submission_revision'
    ledger = json.loads((revision / 'results/artifact_ledger.json').read_text())
    for name, expected in ledger['files'].items():
        base, relative = ((ROOT, name[len('repository/'):])
                          if name.startswith('repository/') else (revision, name))
        if digest(resolve_entry(base, relative)) != expected:
            raise ValueError('Scientific ledger mismatch: ' + name)
    for name in ['main.tex', 'main.pdf', 'supplement.tex', 'supplement.pdf',
                 'references.bib', 'new-evidence.tex', 'supplement-summary.tex',
                 'convergence-table.tex', 'ledger-table.tex']:
        if (ROOT / 'paper/iciev' / name).read_bytes() != (revision / 'paper' / name).read_bytes():
            raise ValueError('Current paper copies differ: ' + name)
    print(f'Release checks passed: {len(entries)} payload files, '
          f'{len(ledger["files"])} scientific digests, current paper copies and credential scan')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-manifest', action='store_true',
                        help='Explicitly refresh hashes after reviewed repository changes')
    args = parser.parse_args()
    if args.write_manifest:
        refresh()
    verify()
