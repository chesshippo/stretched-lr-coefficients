# Independent proposed fresh-evidence gate review

6 September 2026. Bounded read-only source review. No actual full gate, builder, arithmetic engine, test suite, raw batch, or migration record was run/read. This review does not report an actual-corpus PASS.

Final reviewed private proposal: `proposed/fresh_evidence_gate.py`, SHA256 `b0c24239b6446ba2cb9acf0aac89dc5accef0643f63d71bd09de1b615e537641`.

Compared against PUB2 `build_tools/build_fresh_supplement.py`, SHA256 `902fc0b2abf451853e12705469c48fdc8ed94ba0dbaa547d835bf7f5d5b5caf6`. Historical serialization was checked against `migrate_verified_batches.py` (`2769ffe61c1a82321e87c7194cc7dda11276abd1dd9d5dec127d7845ae1401b7`) and the pinned pre-maximal wrapper (`fdc1a6997fb3a66e4071cf5358e3c9cf53cc4108ab9e666af7ac28b2f92877cc`).

**No remaining serious wrong-PASS or false-rejection issue found within this source-review scope.** The conclusion presumes the declared trusted local audit receipts; this publication gate binds those receipts and their actual payload bytes rather than rerunning the full raw semantic validator itself.

## Two issues found and corrected during review

1. The earlier checksum check compared literal line order. The builder sorts `Path` objects by components, whereas the earlier gate sorted slash-joined names. A sibling file such as `validator/review.md` and descendant such as `validator/review/REPORT.md` exhibit different orders. The final gate parses SHA256SUMS into a strict unique name-to-hash map and requires the exact non-self census, hashes, byte length, canonical names, and final newline. This accepts either incidental ordering while still rejecting omitted, duplicated, or incorrect entries.

2. The earlier historical reconstruction obtained the old identity object's insertion order from the final producer receipt. Semantically equal JSON objects may have different key orders, causing a spurious historical hash mismatch. The final gate instead uses `dict(current['identity'], wrapper_sha256=PRE_MAXIMAL_SHA)`, retaining the order present in the migrated metadata itself.

Both corrections were inspected in the final source above. The parent owns the separate mocked-test execution; those results are not claimed as this reviewer's tests.

## Checks that survived independent inspection

- Full producer and portable receipts must both assert COMPLETE, exact integer totals of 358,952, and the stated computation policy. Pinned validator/wrapper identities and the frozen archive identity are checked. The portable result binds the actual completion, identity, catalog, ordered case universe, and every raw/metadata batch hash. Contiguous batch sizes and the exact raw batch census are enforced. Historical/bounded evidence cannot substitute for those full receipts.
- The expected ZIP payload map is derived from the checked audit sources, with raw hashes coming from the portable result. It includes all canonical raw batches, the four catalog files, complete validation and coefficient-inventory records, validator sources, producer sources, initial-512 fixture, both license texts, and the pinned unpack helper. Mandatory source-bound namespaces cannot carry unverified extra members. The public main-release unpack helper must match the same inspected source pin.
- The actual ZIP must have the exact unique regular, nonencrypted member census. Every member is read and checked against its size/hash; the embedded manifest must match the publication-pinned manifest. The manifest's complete totals, validator, source archive, and producer identity must match the checked audit. The checksum file includes all payload members and MANIFEST.json, but intentionally excludes itself, matching the builder.
- Migration remains explicitly bounded: its status, false full-completion flag, old/new identities, contiguous batch indices, origin fields, raw hashes, current metadata hashes, and total of 15,872 migrated cases are checked. With the historical 128-case batch size this entails 124 migrated batches. Each current record must retain its migration origin.
- The pinned old wrapper writes metadata with `json.dumps(value, indent=2) + '\n'`, preserving insertion order. The migration script replaces identity in place and appends `revalidated_from`. Removing that field and changing only the nested wrapper identity, while preserving its current key order, reconstructs the old serialized metadata as intended. No old raw tree is needed for this check.
- ZIP/manifest and complete-receipt bytes are rebound after ZIP inspection. Publication claims still require the actual successful full gate and presence of the required publication documents. Documentation presence checks are not a new prose audit, and receipt provenance remains within the explicit trusted-execution model.

The proposal is suitable to proceed to the parent's actual final gate and asset checks. This source review neither asserts that the active full computation is finished nor authorizes publication independently of those checks.
