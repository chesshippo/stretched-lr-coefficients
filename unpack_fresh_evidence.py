#!/usr/bin/env python3
# Copyright (C) 2026 Maseeh Ghodsi
# SPDX-License-Identifier: GPL-3.0-or-later
"""Reconstruct and extract the exact audited fresh-evidence archive."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
import zipfile

ARCHIVE_SHA256 = 'a4578424a704ac961786072b7694f58eaa071b24304ba64183f868a51ba028f1'
ARCHIVE_BYTES = 372649196
MEMBERS = 5666
EXPANDED_BYTES = 449101401
PART_BYTES = 20 * 1024 * 1024


def digest(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def regular(root, name):
    rel = PurePosixPath(name)
    if not name or rel.is_absolute() or '..' in rel.parts or '\\' in name or ':' in name:
        raise ValueError('Unsafe path: ' + name)
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('Symlink refused: ' + name)
    if not path.is_file():
        raise ValueError('Missing regular file: ' + name)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workdir', type=Path, help='New directory for the reconstructed ZIP and extracted evidence.')
    parser.add_argument('--manifest-only', action='store_true', help='Verify all parts and the complete archive hash without extraction.')
    args = parser.parse_args()
    if sys.version_info < (3, 11) or sys.flags.optimize:
        raise SystemExit('Use Python 3.11 or later without optimization.')
    root = Path(__file__).resolve().parent
    manifest = json.loads(regular(root, 'fresh-evidence/PARTS.json').read_text())
    if manifest.get('archive_sha256') != ARCHIVE_SHA256 or manifest.get('archive_bytes') != ARCHIVE_BYTES:
        raise ValueError('Unexpected fresh-evidence archive identity.')
    parts = manifest.get('parts', [])
    if len(parts) != 18:
        raise ValueError('Exactly 18 ordered fresh-evidence parts are required.')
    combined = hashlib.sha256()
    total = 0
    for index, part in enumerate(parts):
        name = f'fresh-evidence/parts/fresh-evidence.zip.part-{index:03d}'
        if part.get('path') != name:
            raise ValueError('Unexpected part name or order.')
        path = regular(root, name)
        size = path.stat().st_size
        expected_size = min(PART_BYTES, ARCHIVE_BYTES - index * PART_BYTES)
        if size != expected_size or size != part.get('bytes') or digest(path) != part.get('sha256'):
            raise ValueError('Fresh-evidence part differs: ' + name)
        with path.open('rb') as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b''):
                combined.update(chunk)
        total += size
    if total != ARCHIVE_BYTES or combined.hexdigest() != ARCHIVE_SHA256:
        raise ValueError('The parts do not reconstruct the audited archive.')
    if args.manifest_only:
        print(json.dumps({'status': 'PASS', 'scope': 'fresh archive integrity', 'sha256': ARCHIVE_SHA256}))
        return
    work = (args.workdir or root.parent / 'stretched-lr-fresh-inspection').resolve()
    if work == root or work in root.parents or root in work.parents:
        raise ValueError('Choose a new working directory outside the repository.')
    work.mkdir(parents=True, exist_ok=False)
    archive = work / 'stretched-lr-fresh-evidence.zip'
    with archive.open('xb') as target:
        for part in parts:
            with regular(root, part['path']).open('rb') as source:
                shutil.copyfileobj(source, target, length=1024 * 1024)
    if digest(archive) != ARCHIVE_SHA256:
        raise ValueError('Archive changed during reconstruction.')
    with zipfile.ZipFile(archive) as zipped:
        entries = zipped.infolist()
        if len(entries) != MEMBERS or len({e.filename for e in entries}) != MEMBERS:
            raise ValueError('Unexpected archive entry count or duplicate entry.')
        if sum(e.file_size for e in entries) != EXPANDED_BYTES:
            raise ValueError('Unexpected archive expansion size.')
        for entry in entries:
            rel = PurePosixPath(entry.filename)
            if (rel.is_absolute() or '..' in rel.parts or '\\' in entry.filename or ':' in entry.filename
                    or rel.parts[0] != 'stretched-lr-fresh-evidence' or entry.is_dir()
                    or stat.S_ISLNK(entry.external_attr >> 16) or entry.flag_bits & 1):
                raise ValueError('Unsafe archive entry.')
        for entry in entries:
            target = work.joinpath(*PurePosixPath(entry.filename).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(entry) as source, target.open('xb') as destination:
                shutil.copyfileobj(source, destination, length=1024 * 1024)
    result = {'status': 'PASS', 'scope': 'exact archive reconstruction and extraction',
              'archive_sha256': ARCHIVE_SHA256, 'files': MEMBERS,
              'evidence_directory': str(work / 'stretched-lr-fresh-evidence'),
              'mathematical_validation_run': False}
    (work / 'unpack-result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
