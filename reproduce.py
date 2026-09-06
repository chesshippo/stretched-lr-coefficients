#!/usr/bin/env python3
# Copyright (C) 2026 Maseeh Ghodsi
# SPDX-License-Identifier: GPL-3.0-or-later
"""Reconstruct the unchanged evidence packet and run its complete finite audit."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import time
import zipfile

ARCHIVE_SHA256 = '299489ce594f54e3ff0278cb6927b40e03959e528cbe8c57d561466d8aa6cd44'
ARCHIVE_BYTES = 112268985
MANUSCRIPT_SHA256 = '3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45'


def digest(path):
    h = sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def regular_file(root, name):
    rel = PurePosixPath(name)
    if not name or rel.is_absolute() or '..' in rel.parts or '\\' in name or ':' in name:
        raise ValueError('Unsafe file name: ' + name)
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('Symlinks are not accepted: ' + name)
    if not path.is_file():
        raise ValueError('Missing regular file: ' + name)
    return path


def verify_parts(root):
    metadata = json.loads(regular_file(root, 'evidence/PARTS.json').read_text())
    if metadata.get('archive_sha256') != ARCHIVE_SHA256 or metadata.get('archive_bytes') != ARCHIVE_BYTES:
        raise ValueError('Evidence archive identity differs from the reviewed release.')
    parts = metadata.get('parts', [])
    if len(parts) != 6:
        raise ValueError('The complete archive requires exactly six ordered parts.')
    h = sha256()
    total = 0
    for i, part in enumerate(parts):
        if part.get('path') != f'evidence/parts/evidence.zip.part-{i:03d}':
            raise ValueError('Part names or order differ from the release.')
        path = regular_file(root, part['path'])
        size = path.stat().st_size
        if size != part.get('bytes') or size > 20 * 1024 * 1024 or digest(path) != part.get('sha256'):
            raise ValueError('Changed evidence part: ' + part['path'])
        with path.open('rb') as source:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                h.update(block)
        total += size
    if total != ARCHIVE_BYTES or h.hexdigest() != ARCHIVE_SHA256:
        raise ValueError('Reconstructed bytes do not identify the reviewed evidence archive.')
    if digest(regular_file(root, 'proof/frozen-proof.tex')) != MANUSCRIPT_SHA256:
        raise ValueError('Frozen manuscript text differs from the reviewed release.')
    return metadata


def reconstruct(root, workdir, metadata):
    # All parts have been checked before any output directory is created.
    workdir.mkdir(parents=True, exist_ok=False)
    archive = workdir / 'reviewed-evidence.zip'
    with archive.open('xb') as target:
        for part in metadata['parts']:
            with regular_file(root, part['path']).open('rb') as source:
                shutil.copyfileobj(source, target, length=1024 * 1024)
    if digest(archive) != ARCHIVE_SHA256:
        raise ValueError('Evidence changed during reconstruction.')
    packet = workdir / 'packet'
    with zipfile.ZipFile(archive) as zipped:
        members = zipped.infolist()
        if len(members) != metadata['archive_entries'] or len({m.filename for m in members}) != len(members):
            raise ValueError('Unexpected or duplicate archive members.')
        if sum(m.file_size for m in members) != metadata['archive_uncompressed_bytes']:
            raise ValueError('Unexpected archive expansion size.')
        for member in members:
            rel = PurePosixPath(member.filename)
            mode = member.external_attr >> 16
            if (rel.is_absolute() or '..' in rel.parts or '\\' in member.filename or ':' in member.filename
                    or stat.S_ISLNK(mode) or member.is_dir()):
                raise ValueError('Unsafe archive member: ' + member.filename)
        packet.mkdir()
        for member in members:
            target = packet.joinpath(*PurePosixPath(member.filename).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(member) as source, target.open('xb') as destination:
                shutil.copyfileobj(source, destination, length=1024 * 1024)
    return packet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workdir', type=Path, help='New directory for the reconstructed packet and receipts.')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--manifest-only', action='store_true', help='Check all six parts and their combined identity; no extraction or finite audit.')
    modes.add_argument('--unpack-only', action='store_true', help='Reconstruct the packet and verify all its manifests; omit the finite audit.')
    args = parser.parse_args()
    if sys.version_info < (3, 11) or sys.flags.optimize:
        raise SystemExit('Use Python 3.11 or newer without -O or PYTHONOPTIMIZE.')
    root = Path(__file__).resolve().parent
    started = time.monotonic()
    metadata = verify_parts(root)
    print('PASS: all six parts reconstruct the original reviewed evidence archive.', flush=True)
    if args.manifest_only:
        print(json.dumps({'status': 'PASS', 'scope': 'parts and manuscript integrity only',
            'archive_sha256': ARCHIVE_SHA256, 'finite_audit_run': False}))
        return
    workdir = (args.workdir or root.parent / 'stretched-lr-verification').resolve()
    if workdir == root or workdir in root.parents:
        raise SystemExit('Choose a new working directory, not the release directory or one of its ancestors.')
    if workdir.exists():
        raise SystemExit('Refusing to overwrite an existing working directory: ' + str(workdir))
    packet = reconstruct(root, workdir, metadata)
    output = workdir / 'verification.json'
    command = [sys.executable, '-B', str(packet / 'verify.py'), '--output', str(output)]
    if args.unpack_only:
        command.append('--manifest-only')
    env = {key: os.environ[key] for key in ('PATH', 'TMPDIR', 'LANG', 'LC_ALL', 'DYLD_LIBRARY_PATH') if key in os.environ}
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    print('Running the frozen verifier; detailed output: ' + str(workdir / 'verification.log'), flush=True)
    with (workdir / 'verification.log').open('x') as log:
        result = subprocess.run(command, cwd=packet, env=env, stdout=log, stderr=subprocess.STDOUT)
    if result.returncode:
        raise SystemExit('Frozen verification failed; inspect ' + str(workdir / 'verification.log'))
    actual = json.loads(output.read_text())
    if actual.get('status') != 'PASS' or actual.get('manuscript_sha256') != MANUSCRIPT_SHA256:
        raise ValueError('Frozen verifier did not validate the expected manuscript.')
    if not args.unpack_only and (actual.get('core_total') != 358952 or actual.get('audit_stages_passed') != 7):
        raise ValueError('The complete finite audit did not pass.')
    receipt = {'status': 'PASS', 'scope': actual['scope'], 'archive_sha256': ARCHIVE_SHA256,
        'verification_receipt_sha256': digest(output), 'verification_receipt': str(output),
        'finite_audit_run': not args.unpack_only, 'core_total': actual.get('core_total'),
        'full_ehrhart_regeneration': False, 'full_lean_verification': False,
        'elapsed_s': time.monotonic() - started}
    with (workdir / 'release-verification.json').open('x') as destination:
        json.dump(receipt, destination, indent=2)
        destination.write('\n')
    print(json.dumps(receipt), flush=True)


if __name__ == '__main__':
    main()
