#!/usr/bin/env python3
# Copyright (C) 2026 Maseeh Ghodsi, for rights held in original contributions.
# SPDX-License-Identifier: GPL-3.0-or-later
"""Reconstruct and verify the exact frozen packet without executing packet code.

Python 3.11+ standard library only; portable path comparisons use POSIX archive
names. This command establishes byte integrity, not a mathematical audit.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

ARCHIVE_SHA = '299489ce594f54e3ff0278cb6927b40e03959e528cbe8c57d561466d8aa6cd44'
ARCHIVE_BYTES = 112268985
MANIFEST_SHA = 'f835cbc7ae315eb181139a812d24c11ee29bd747735311eb510bcd09b0aa56f3'


def require(value, message):
    if not value:
        raise ValueError(message)


def safe_name(name):
    require(type(name) is str and name and '\\' not in name and ':' not in name,
            'Unsafe archive path.')
    relative = PurePosixPath(name)
    require(not relative.is_absolute() and '..' not in relative.parts and
            relative.as_posix() == name and name != '.', 'Noncanonical archive path.')
    return relative


def regular_file(root, name):
    path = root
    for component in safe_name(name).parts:
        path = path / component
        require(not path.is_symlink(), 'Symlink is forbidden: ' + name)
    require(path.is_file(), 'Missing regular file: ' + name)
    return path


def reconstruct(release, workdir):
    release = release.resolve(strict=True)
    workdir = workdir.resolve()
    require(workdir != release and not workdir.is_relative_to(release),
            'Working directory must be outside the release.')
    require(not workdir.exists(), 'Working directory must be new.')
    metadata = json.loads(regular_file(release, 'evidence/PARTS.json').read_text())
    require(metadata['archive_sha256'] == ARCHIVE_SHA and metadata['archive_bytes'] == ARCHIVE_BYTES,
            'Wrong original archive identity.')
    require(type(metadata['parts']) is list and len(metadata['parts']) == 6,
            'All six ordered parts are required.')
    paths = []
    for index, part in enumerate(metadata['parts']):
        name = f'evidence/parts/evidence.zip.part-{index:03d}'
        require(part['path'] == name and type(part['bytes']) is int and
                0 < part['bytes'] <= 20 * 1024**2, 'Wrong part name, order or size.')
        paths.append(regular_file(release, name))
    workdir.mkdir(parents=True, exist_ok=False)
    archive = workdir / 'reviewed-evidence.zip'
    combined = sha256(); total = 0
    with archive.open('xb') as output:
        for source, part in zip(paths, metadata['parts']):
            current = sha256(); size = 0
            with source.open('rb') as stream:
                for block in iter(lambda: stream.read(1024**2), b''):
                    current.update(block); combined.update(block)
                    size += len(block); total += len(block); output.write(block)
            require(size == part['bytes'] and current.hexdigest() == part['sha256'], 'Changed evidence part.')
    require(total == ARCHIVE_BYTES and combined.hexdigest() == ARCHIVE_SHA, 'Wrong reconstructed archive bytes.')
    packet = workdir / 'packet'
    with zipfile.ZipFile(archive) as z:
        members = z.infolist(); names = [info.filename for info in members]
        require(len(members) == 132 and len(set(names)) == 132,
                'Unexpected or duplicate archive members.')
        require(len({name.casefold() for name in names}) == 132, 'Case-colliding archive paths.')
        for info in members:
            safe_name(info.filename)
            require(not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16), 'Nonregular archive member.')
        manifest_bytes = z.read('MANIFEST.json')
        require(sha256(manifest_bytes).hexdigest() == MANIFEST_SHA, 'Wrong frozen top manifest.')
        manifest = json.loads(manifest_bytes)
        require(set(names) == set(manifest['files']) | {'MANIFEST.json'}, 'Archive manifest census differs.')
        packet.mkdir()
        for info in members:
            target = packet.joinpath(*safe_name(info.filename).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            actual_hash = sha256(); size = 0
            with z.open(info) as source, target.open('xb') as output:
                for block in iter(lambda: source.read(1024**2), b''):
                    actual_hash.update(block); size += len(block); output.write(block)
            expected = ({'sha256': MANIFEST_SHA, 'bytes': len(manifest_bytes)}
                        if info.filename == 'MANIFEST.json' else manifest['files'][info.filename])
            require(size == expected['bytes'] and actual_hash.hexdigest() == expected['sha256'],
                    'Extracted bytes differ: ' + info.filename)
    result = {'status': 'INTEGRITY_VERIFIED', 'archive_sha256': ARCHIVE_SHA,
              'packet_manifest_sha256': MANIFEST_SHA, 'files': 132, 'packet': str(packet),
              'packet_code_executed': False, 'mathematical_audit': False, 'full_lean': False}
    (workdir / 'reconstruction.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', type=Path, required=True)
    parser.add_argument('--workdir', type=Path, required=True)
    arguments = parser.parse_args()
    print(json.dumps(reconstruct(arguments.release, arguments.workdir), indent=2))


if __name__ == '__main__':
    main()
