"""Fail-closed source and raw-evidence checks shared by publication builders."""
from hashlib import file_digest, sha256
import json
from pathlib import Path, PurePosixPath
import re
import sqlite3
import stat
import sys
import zipfile

TOTAL = 358952
COEFFICIENTS = 2745084
VALIDATOR_SHA = '13706acbdfa99a3bd20c6f2c857a2a410cbe0d3be477a8b007e624ad60f7f0d9'
WRAPPER_SHA = '9e33a4732f075ea6eab2f1c27378cd11c6c37d0cb88774b968d8669a82073662'
PRE_MAXIMAL_SHA = 'fdc1a6997fb3a66e4071cf5358e3c9cf53cc4108ab9e666af7ac28b2f92877cc'
MANIFEST_SHA = 'f835cbc7ae315eb181139a812d24c11ee29bd747735311eb510bcd09b0aa56f3'
ARCHIVE_SHA = '299489ce594f54e3ff0278cb6927b40e03959e528cbe8c57d561466d8aa6cd44'
SUPPLEMENT = 'stretched-lr-fresh-evidence'
MIGRATED_CASES = 15872
UNPACK_SHA = '3fa46dbcf51f52d971384ac212211266c5955dfc37e3fd5e8a6a64152ba4b719'
CATALOG_FILES = ('catalog.sqlite', 'catalog.json', 'binding.json', 'engines.json')
PRODUCER_FILES = ('parallel_regenerate.py', 'parallel_regenerate_initial.py',
                  'parallel_regenerate_pre_maximal_label.py', 'migrate_verified_batches.py',
                  'maximal_label_migration.json', 'dimension_format_failure.json')


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(path):
    with Path(path).open('rb') as stream:
        return file_digest(stream, 'sha256').hexdigest()


def load(path):
    return strict_json(Path(path).read_bytes())


def strict_json(value):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f'Duplicate JSON key: {key}')
            result[key] = value
        return result
    def nonfinite(value):
        raise ValueError('Nonfinite JSON number: ' + value)
    return json.loads(value, object_pairs_hook=unique, parse_constant=nonfinite)


def relative_name(name):
    require(type(name) is str and bool(name) and '\\' not in name and ':' not in name,
            'Unsafe supplement member name.')
    path = PurePosixPath(name)
    require(not path.is_absolute() and '..' not in path.parts and name != '.' and
            path.as_posix() == name, 'Noncanonical supplement member name.')
    return name


def valid_pin(value):
    return (type(value) is dict and set(value) == {'bytes', 'sha256'} and
            type(value['bytes']) is int and value['bytes'] >= 0 and
            type(value['sha256']) is str and re.fullmatch('[0-9a-f]{64}', value['sha256']))


def pin(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), f'Missing/nonregular payload: {path}')
    return {'bytes': path.stat().st_size, 'sha256': digest(path)}


def require_completed_audit(here, repository):
    require(__debug__ and not sys.flags.optimize, 'Publication requires assertions enabled.')
    config = load(here / 'build_config.json')
    require(config['source_archive_sha256'] == ARCHIVE_SHA, 'Wrong frozen source archive identity.')
    audit = repository / config['audit_run']
    raw = audit / 'full_regeneration'
    producer_path = raw / 'complete.json'
    portable_path = audit / 'portable_full_validation.json'
    producer, portable = load(producer_path), load(portable_path)
    for report in (producer, portable):
        require(report['status'] == 'COMPLETE' and report['all_core_regeneration_complete'] is True,
                'Both producer and portable verification must be COMPLETE.')
        require(type(report['verified_cases']) is int and report['verified_cases'] == TOTAL
                and type(report['total']) is int and report['total'] == TOTAL,
                'Both complete receipts must cover the exact full corpus.')
        require(report['full_latte'] is False, 'Unexpected computation policy.')
    require(portable['validator_sha256'] == VALIDATOR_SHA and
            digest(audit / 'computational_audit/portable_validator/validate_raw_supplement.py') == VALIDATOR_SHA,
            'Portable verifier source differs from its reviewed code.')
    require(portable['packet_manifest_sha256'] == MANIFEST_SHA and
            portable['source_catalog_rebuilt_and_compared'] is True and
            portable['source_catalog_rows'] == TOTAL and
            portable['normaliz_executed_by_validator'] is False and portable['lean_verification'] is False,
            'Incomplete or misstated portable verification scope.')
    identity = load(raw / 'identity.json')
    require(producer['identity'] == portable['identity'] == identity and
            identity['wrapper_sha256'] == WRAPPER_SHA and
            digest(audit / 'parallel_regenerate.py') == WRAPPER_SHA,
            'Producer, portable check and actual source identities differ.')
    require(portable['complete_receipt_sha256'] == digest(producer_path) and
            portable['raw_identity_sha256'] == digest(raw / 'identity.json') and
            portable['verified_case_order_sha256'] == identity['case_order_sha256'],
            'Portable result does not bind these exact complete receipts.')
    catalog = audit / 'regeneration/catalog.sqlite'
    require(digest(catalog) == identity['catalog_sha256'], 'Catalog changed after verification.')
    for name, key in (('binding.json', 'binding_sha256'), ('engines.json', 'engines_sha256')):
        value = load(audit / 'regeneration' / name)
        canonical = json.dumps(value, sort_keys=True, separators=(',', ':')).encode('utf-8')
        require(sha256(canonical).hexdigest() == identity[key], 'Catalog metadata changed after verification.')
    catalog_info = load(audit / 'regeneration/catalog.json')
    require(catalog_info['sha256'] == identity['catalog_sha256'] and catalog_info['total'] == TOTAL
            and catalog_info['counts'] == {'large': 346537, 'small': 12415},
            'Catalog metadata does not match the verified universe.')
    db = sqlite3.connect(catalog.resolve().as_uri() + '?mode=ro&immutable=1', uri=True)
    try:
        counts = db.execute('SELECT count(*),sum(degree+1) FROM cases').fetchone()
    finally:
        db.close()
    require(counts == (TOTAL, COEFFICIENTS), 'Wrong complete coefficient cardinality.')
    expected = set()
    cases = 0
    size = identity['batch_size']
    require(type(size) is int and 1 <= size <= 256, 'Invalid source batch size.')
    require(type(portable['verified_batches']) is list and
            len(portable['verified_batches']) == (TOTAL + size - 1) // size,
            'Wrong complete batch census.')
    for index, batch in enumerate(portable['verified_batches']):
        require(type(batch['batch_index']) is int and batch['batch_index'] == index,
                'Portable batch list is not contiguous.')
        meta = raw / f'batch-{index:05d}.json'
        stream = raw / f'batch-{index:05d}.jsonl.gz'
        require(digest(meta) == batch['metadata_sha256'] and digest(stream) == batch['raw_sha256'],
                'Raw bytes changed since portable verification.')
        record = load(meta)
        require(type(batch['cases']) is int and batch['cases'] == min(size, TOTAL - index * size) and
                type(record['count']) is int and record['count'] == batch['cases'] and
                record['status'] == 'PASS' and type(record['batch_index']) is int and
                record['batch_index'] == index and record['identity'] == identity,
                'Portable/raw batch cardinality or identity mismatch.')
        cases += batch['cases']
        expected.update((meta.name, stream.name))
    actual = {p.name for p in raw.iterdir() if p.name.startswith('batch-')}
    require(actual == expected and cases == TOTAL, 'Incomplete, extra, or failed raw batch remains.')
    require(digest(repository / config['source_archive']) == config['source_archive_sha256'],
            'Frozen original archive changed.')
    return config, audit, producer, portable


def expected_payload_pins(here, audit, producer, portable):
    """Bind indispensable ZIP payloads to the completed, pinned audit sources.

    Batch hashes come directly from the portable result, not the supplement's
    self-written manifest. Other source metadata is rechecked by the common
    completed-audit gate before these exact byte pins are captured.
    """
    expected = {}
    def add(source, name, known_sha=None):
        actual = pin(source)
        require(known_sha is None or actual['sha256'] == known_sha,
                f'Payload differs from the portable/source identity: {name}')
        expected[name] = actual
    add(audit / 'full_regeneration/complete.json', 'raw/complete.json', portable['complete_receipt_sha256'])
    add(audit / 'full_regeneration/identity.json', 'raw/identity.json', portable['raw_identity_sha256'])
    for batch in portable['verified_batches']:
        for suffix, key in (('json', 'metadata_sha256'), ('jsonl.gz', 'raw_sha256')):
            name = f"batch-{batch['batch_index']:05d}.{suffix}"
            add(audit / 'full_regeneration' / name, 'raw/' + name, batch[key])
    for name in CATALOG_FILES:
        add(audit / 'regeneration' / name, 'catalog/' + name,
            producer['identity']['catalog_sha256'] if name == 'catalog.sqlite' else None)
    add(audit / 'portable_full_validation.json', 'validation/portable-complete.json')
    add(audit / 'coefficient_inventory.json', 'validation/coefficient-inventory.json')
    validator_root = audit / 'computational_audit/portable_validator'
    for source in sorted(validator_root.rglob('*')):
        require(not source.is_symlink(), 'Symlink in validator sources.')
        if source.is_file():
            require('__pycache__' not in source.parts and source.suffix != '.pyc', 'Bytecode in validator sources.')
            name = source.relative_to(validator_root).as_posix()
            add(source, 'validator/' + name, VALIDATOR_SHA if name == 'validate_raw_supplement.py' else None)
    require('validator/validate_raw_supplement.py' in expected, 'Required validator source is absent.')
    for name in PRODUCER_FILES:
        known = {'parallel_regenerate.py': WRAPPER_SHA, 'parallel_regenerate_pre_maximal_label.py': PRE_MAXIMAL_SHA}
        add(audit / name, 'producer/' + name, known.get(name))
    # The main release and raw supplement must carry the same inspected,
    # standard-library extractor. Its local source pin is included in the
    # mandatory payload map and publication report.
    add(here / 'release_additions/audit/code/unpack_frozen_packet.py', 'tools/unpack_frozen_packet.py', UNPACK_SHA)
    initial = audit / 'full_regeneration_initial_validation'
    for source in sorted(initial.iterdir()):
        if source.name.startswith(('batch-', 'bounded-')) or source.name == 'identity.json':
            add(source, 'tests/initial-512/' + source.name)
    initial_names = {name.removeprefix('tests/initial-512/') for name in expected
                     if name.startswith('tests/initial-512/')}
    required_initial = {'identity.json'} | {f'batch-{i:05d}.{ext}' for i in range(4) for ext in ('json', 'jsonl.gz')}
    require(required_initial <= initial_names and
            {n for n in initial_names if n.startswith('batch-')} == required_initial - {'identity.json'},
            'Historical test fixture must contain exactly four initial raw batches.')
    add(here / 'licenses_source/GPL-3.0.txt', 'LICENSE')
    add(here / 'licenses_source/CC-BY-4.0.txt', 'LICENSES/CC-BY-4.0.txt')
    return expected


def verify_migration(audit, producer, portable):
    """Check retained migration provenance without reading the old raw tree."""
    migration = load(audit / 'maximal_label_migration.json')
    identity = producer['identity']
    old_identity = dict(identity, wrapper_sha256=PRE_MAXIMAL_SHA)
    require(migration['status'] == 'MIGRATED_READY_TO_RESUME' and
            migration['all_core_regeneration_complete'] is False and
            type(migration['migrated_cases']) is int and migration['migrated_cases'] == MIGRATED_CASES and
            migration['new_identity'] == identity and migration['old_identity'] == old_identity,
            'Migration receipt identity or bounded scope differs.')
    batches = migration['batches']
    require(type(batches) is list and batches, 'Missing migration batch provenance.')
    cases = 0
    for index, batch in enumerate(batches):
        require(type(batch['batch']) is int and batch['batch'] == index and
                index < len(portable['verified_batches']), 'Missing, duplicated or extra migration batch.')
        verified = portable['verified_batches'][index]
        require(type(batch['cases']) is int and batch['cases'] > 0 and batch['cases'] == verified['cases'] and
                batch['new_metadata_sha256'] == verified['metadata_sha256'], 'Migrated batch differs from portable result.')
        origin = batch['origin']
        require(type(origin) is dict and set(origin) == {'wrapper_sha256','metadata_sha256','raw_sha256','correction'} and
                origin['wrapper_sha256'] == PRE_MAXIMAL_SHA and origin['raw_sha256'] == verified['raw_sha256'] and
                type(origin['metadata_sha256']) is str and re.fullmatch('[0-9a-f]{64}',origin['metadata_sha256']) and
                origin['correction'] == 'Accept the literal maximal-dimension annotation only at full ambient dimension',
                'Wrong migrated raw/source origin.')
        path = audit / 'full_regeneration' / f'batch-{index:05d}.json'
        require(digest(path) == verified['metadata_sha256'], 'Current migrated metadata changed.')
        current = load(path)
        require(current['revalidated_from'] == origin and current['identity'] == identity,
                'Current metadata lost its historical origin.')
        # The hash-pinned old producer serializes exactly indent=2 plus newline.
        # Migration changes identity in place and appends revalidated_from, so
        # its old metadata bytes can be reconstructed without opening old data.
        previous = dict(current)
        del previous['revalidated_from']
        previous['identity'] = dict(current['identity'], wrapper_sha256=PRE_MAXIMAL_SHA)
        previous_bytes = (json.dumps(previous,indent=2) + '\n').encode('utf-8')
        require(sha256(previous_bytes).hexdigest() == origin['metadata_sha256'],
                'Retained historical metadata hash cannot be reconstructed.')
        cases += batch['cases']
    require(cases == MIGRATED_CASES, 'Wrong migration case total.')
    return migration


def verify_supplement_zip(asset, manifest_bytes, expected, config, producer, evidence):
    """Stream every actual ZIP member and bind it to verified audit payloads."""
    require(len(manifest_bytes) <= 32 * 1024**2, 'Oversized supplement manifest.')
    manifest = strict_json(manifest_bytes)
    require(manifest['schema'] == 'complete-raw-polynomial-supplement-v1' and
            manifest['status'] == 'COMPLETE' and type(manifest['polynomials']) is int and
            manifest['polynomials'] == TOTAL and type(manifest['rational_monomial_coefficients']) is int and
            manifest['rational_monomial_coefficients'] == COEFFICIENTS and
            manifest['source_archive_sha256'] == config['source_archive_sha256'] == ARCHIVE_SHA and
            manifest['validator_sha256'] == VALIDATOR_SHA and manifest['identity'] == producer['identity'],
            'Supplement manifest identity/scope differs from the completed audit.')
    payload = manifest['files']
    require(type(payload) is dict and payload, 'Missing supplement payload census.')
    for name, value in payload.items():
        relative_name(name)
        require(name not in ('MANIFEST.json', 'SHA256SUMS') and valid_pin(value), 'Invalid supplement file pin.')
    for name, value in expected.items():
        require(payload.get(name) == value, f'Supplement payload is missing or differs from verified audit: {name}')
    # These namespaces contain source-bound records; no unverified extras may
    # accompany an apparently complete set of canonical batch names.
    for prefix in ('raw/', 'catalog/', 'validation/', 'validator/', 'producer/', 'tests/initial-512/', 'tools/'):
        require({n for n in payload if n.startswith(prefix)} == {n for n in expected if n.startswith(prefix)},
                f'Unexpected source-bound payload in {prefix}')
    for name in ('README.md', 'LICENSING.md', 'NOTICE', 'THIRD_PARTY_NOTICES.md'):
        require(name in payload and payload[name]['bytes'] > 100, f'Missing supplement instructions/notices: {name}')
    checksum_pins = dict(payload)
    checksum_pins['MANIFEST.json'] = {'bytes': len(manifest_bytes), 'sha256': sha256(manifest_bytes).hexdigest()}
    sums = ''.join(f"{value['sha256']}  {name}\n" for name, value in checksum_pins.items()).encode('utf-8')
    members = set(payload) | {'MANIFEST.json', 'SHA256SUMS'}
    require(type(evidence['files']) is int and evidence['files'] == len(members), 'Wrong supplement ZIP member count.')
    with zipfile.ZipFile(asset) as zipped:
        infos = zipped.infolist()
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)) == len(members), 'Duplicate or missing supplement ZIP member.')
        require(set(names) == {SUPPLEMENT + '/' + n for n in members}, 'Unexpected supplement ZIP census.')
        for info in infos:
            name = info.filename
            relative_name(name)
            mode = info.external_attr >> 16
            require(not info.is_dir() and stat.S_IFMT(mode) in (0, stat.S_IFREG) and
                    not (info.flag_bits & 1), 'Nonregular or encrypted supplement ZIP member.')
            relative = name.removeprefix(SUPPLEMENT + '/')
            if relative == 'MANIFEST.json':
                require(info.file_size == len(manifest_bytes) and zipped.read(info) == manifest_bytes,
                        'ZIP embedded manifest differs from the publication-pinned manifest.')
            elif relative == 'SHA256SUMS':
                require(info.file_size == len(sums), 'ZIP SHA256SUMS has the wrong size.')
                raw_sums = zipped.read(info)
                require(raw_sums.endswith(b'\n'), 'ZIP SHA256SUMS lacks its final newline.')
                seen = {}
                for line in raw_sums.decode('utf-8').splitlines():
                    match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
                    require(match is not None, 'Malformed ZIP SHA256SUMS line.')
                    hashed, named = match.groups()
                    relative_name(named)
                    require(named not in seen, 'Duplicate ZIP SHA256SUMS entry.')
                    seen[named] = hashed
                require(seen == {n: p['sha256'] for n, p in checksum_pins.items()},
                        'ZIP SHA256SUMS does not describe the exact non-self payload.')
            else:
                require(info.file_size == payload[relative]['bytes'], f'Wrong ZIP member size: {relative}')
                with zipped.open(info) as stream:
                    require(file_digest(stream, 'sha256').hexdigest() == payload[relative]['sha256'],
                            f'ZIP member bytes differ from manifest: {relative}')
    return manifest


def require_fresh_evidence(here, repository, public_root):
    config, audit, producer, portable = require_completed_audit(here, repository)
    evidence = load(public_root / 'audit/FRESH_EVIDENCE.json')
    require(evidence['status'] == 'COMPLETE' and evidence['polynomials'] == TOTAL and
            evidence['rational_monomial_coefficients'] == COEFFICIENTS,
            'Fresh evidence declaration is incomplete.')
    require(evidence['portable_validation'] == pin(audit / 'portable_full_validation.json') and
            evidence['producer_completion'] == pin(audit / 'full_regeneration/complete.json') and
            evidence['identity'] == producer['identity'] and
            evidence['validator_sha256'] == VALIDATOR_SHA,
            'Publication evidence does not bind the completed audit.')
    require(evidence['source_archive_sha256'] == config['source_archive_sha256'] and
            evidence['full_latte'] is False and evidence['full_lean'] is False and
            evidence['all_zip_members_byte_verified'] is True,
            'Publication supplement scope or source differs.')
    filename = relative_name(evidence['asset']['filename'])
    require('/' not in filename and filename == SUPPLEMENT + '.zip',
            'Unsafe release-asset name.')
    asset = here / evidence['asset']['filename']
    require(pin(asset) == {k: evidence['asset'][k] for k in ('bytes', 'sha256')},
            'Fresh raw asset is missing or changed.')
    manifest = here / 'stretched-lr-fresh-evidence/MANIFEST.json'
    require(pin(manifest) == evidence['supplement_manifest'], 'Raw supplement manifest changed.')
    manifest_bytes = manifest.read_bytes()
    require({'bytes': len(manifest_bytes), 'sha256': sha256(manifest_bytes).hexdigest()} == evidence['supplement_manifest'],
            'Supplement manifest changed while being read.')
    expected = expected_payload_pins(here, audit, producer, portable)
    verify_migration(audit, producer, portable)
    require(pin(public_root / 'audit/code/unpack_frozen_packet.py') == expected['tools/unpack_frozen_packet.py'],
            'Public extractor differs from the inspected supplement source.')
    require(expected['validation/portable-complete.json'] == evidence['portable_validation'] and
            expected['raw/complete.json'] == evidence['producer_completion'], 'Completion bytes changed during publication gating.')
    verify_supplement_zip(asset, manifest_bytes, expected, config, producer, evidence)
    require(pin(asset) == {k: evidence['asset'][k] for k in ('bytes', 'sha256')} and
            pin(manifest) == evidence['supplement_manifest'] and
            pin(audit / 'portable_full_validation.json') == evidence['portable_validation'] and
            pin(audit / 'full_regeneration/complete.json') == evidence['producer_completion'],
            'Source/asset bytes changed during ZIP validation.')
    for name in ('audit/FRESH_EVIDENCE.md', 'audit/FINAL_AUDIT.md', 'ARCHIVAL_ERRATA.md'):
        require((public_root / name).is_file() and (public_root / name).stat().st_size > 100,
                f'Missing publication document: {name}')
    return evidence
