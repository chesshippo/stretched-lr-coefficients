# Publication-gate recheck and proposed correction

2026-09-06 UTC. **The earlier publication findings are resolved or have a tested
proposed correction ready for integration.** The proposal is
`proposed/fresh_evidence_gate.py`, SHA-256
`b0c24239b6446ba2cb9acf0aac89dc5accef0643f63d71bd09de1b615e537641`.
No complete gate, build, engine call or repeated mathematical corpus inventory
was run. No active raw batch was read or modified. The migration receipt and
producing source were read as expressly authorized; migration batches themselves
were represented by tiny private fixtures for tests.

## Concrete review outcome

The revised common gate now requires both producer and portable COMPLETE
receipts, precise cardinality and source identities, the pinned validator and
producer code, current raw batch hashes, and complete batch coverage. The
supervisor additionally fixed canonical hashes for binding.json/engines.json
and exact catalog.json metadata. Both publication programs call the common
gate before mutation, so its explicit rejection of optimized execution
protects their remaining assertions. The sealer now checks the actual evidence
parts through the unchanged reproducer before and after fresh ZIP extraction,
and excludes SHA256SUMS from its own census.

The strict audit now verifies the entire frozen packet locally before executing
or importing any packet program. The old harmless replacement-verifier witness
is rejected before its marker can be written. All 16 mathematical audit function
bodies remain AST-identical to the original adversarial_checks.py.

One remaining asset-binding defect was confirmed in the revised current gate
SHA `545ad5f1710f4e986d13b245e4585791bad8761a1b0cdc63497b90bdb8517ed3`:
it compares the fresh ZIP's outer hash with FRESH_EVIDENCE.json but never opens
the ZIP. With the completed-audit prerequisite mocked as a previously verified
oracle, replacing the asset by a one-file unrelated ZIP and updating only its
outer pin passes that gate while the original loose supplement manifest remains.
The proposed gate rejects the same witness. This is a synthetic gate witness,
not an allegation that an actual supplied archive is wrong.

## Proposed gate behavior

The proposed module preserves the supervisor's new metadata checks and adds:

- A pinned exact source-archive identity and strict duplicate-free finite JSON.
- Exact batch cardinality, index, PASS status and expected last-batch size.
- An exact required payload map whose raw batch hashes come from the portable
  result. It binds the producer completion and identity, all four catalog files,
  portable completion receipt, coefficient inventory, validator files, producing
  and migration sources, initial-512 fixture, and exact upstream license texts.
- A pin for the inspected portable extractor, plus equality of its main-release
  copy and supplement copy. Extractor SHA-256 is
  `3fa46dbcf51f52d971384ac212211266c5955dfc37e3fd5e8a6a64152ba4b719`.
- Reading the actual ZIP: exact unique member census, canonical paths,
  nonregular/encrypted-member rejection, equality of its embedded manifest with
  the pinned loose manifest, each member's exact size/hash, and the complete
  SHA256SUMS mapping with no self-entry, duplicate, omission or wrong digest.
  Checksum ordering has no semantic effect.
- Exact source-bound namespaces, rejecting additional raw/catalog/validator/
  producer/test/tool records that are not in the expected map.
- Migration receipt agreement: bounded migration status, exactly 15,872 cases,
  case sum and contiguous prefix, current new identity and pinned old identity,
  every portable/current metadata hash and raw hash, and preserved
  revalidated_from. The old metadata SHA is checked by reconstructing its bytes
  using the pinned producer's indent=2 plus newline serialization. Its nested
  identity order comes from the actual current metadata, so reordering a
  logically equal completion-receipt object does not cause rejection.
- End-of-check rehashes of the whole asset, loose manifest and completion
  receipts. This supplements the assumption that finalized audit inputs remain
  immutable while publication is staged.

The gate streams ZIP members and does not decode every raw polynomial again:
that semantic work is bound through the separately executed, pinned portable
COMPLETE result. Thus it does not replace or skip the portable complete run.

## Integration instructions

Copy the proposed module into PUB2/build_tools after reviewing it. Its existing
public APIs `require_completed_audit` and `require_fresh_evidence` retain their
call signatures. Both main builder and sealer already invoke the latter.

For the fresh-supplement builder's own final status, also use
`expected_payload_pins`, `verify_migration` and `verify_supplement_zip` on the
finished ZIP and constructed result before emitting a final COMPLETE artifact
declaration. The full `require_fresh_evidence` gate will repeat those bindings
at main publication/sealing, after all public audit documents are present.
This makes a supplementary builder COMPLETE mean its actual source-bound ZIP
has passed, not only that it round-tripped its current staging files.

Run the actual full gate only after regeneration and portable complete
validation have finished, with their inputs held unchanged. Check the final
packaged reproduction and all links separately. This report does not pre-approve
the bytes of an unbuilt ZIP or a future final verification receipt.

## Bounded validation

`test_gate.py` passed **31 tests**, with zero failures or errors. Tests cover the
rehashed unrelated-ZIP witness, full mandatory-file hash changes, missing/extra/
duplicate/symlink/traversal/corrupt members, checksum ordering, altered public
extractor/license, bounded or numerically malformed completion receipts,
missing portable receipt, migration links, fully rehashed false historical
origin, reordered completion-identity keys, optimized execution, and strict
startup before packet-code execution. The standalone actual-source gate was
not invoked. ZIP tests explicitly mock the completed-audit prerequisite and
the expected payload map; migration tests lower only the migration count in
memory for a one-batch synthetic control. They are not proof evidence.

An independent bounded code review found no remaining serious issue in the
final proposed SHA. It caught and confirmed corrections to checksum-order and
historical JSON key-order false-rejection edges; see PROPOSED_GATE_REVIEW.md.
The test source and exact outcomes are retained in test_gate.py,
test_result.json and tests.log.

## Reproduction and licensing

The new standard-library `unpack_frozen_packet.py` verifies the hardcoded
archive and manifest, safe POSIX member names and all 132 extracted files,
without executing packet code. Static inspection supports its intended
portable integrity-only scope; the supervisor performs its actual extraction
test separately. The supplement builder now copies this tool and documents
using it before the portable validator. It also instructs readers to run the
hostile suite in a disposable supplement copy, preserving the distributed
test receipts that the suite would otherwise overwrite. The existing main
archival seven-stage reproducer has not been altered.

The raw supplement retains source and code provenance, required original
licenses and third-party notices; it does not include arithmetic-engine
binaries. Its producer scripts are clearly labelled historical execution
provenance with the original path arrangement, and the portable validator is
the supported no-engine inspection route. No internal software/prose/data
licensing-scope contradiction was found. The final common gate now verifies
the exact copied license bytes against the designated upstream license files.
This remains a scope-consistency assessment, not a copyright-ownership opinion.

WORDING_USABILITY.md records the earlier documentation findings. The new
extractor and disposable-copy instructions address the two concrete issues in
that note. Resource estimates and final link/package usability still require
the supervisor's actual completed-artifact checks.

Final reviewed source hashes are recorded in SOURCE_HASHES.json. The proposal,
tests and review evidence are entirely confined to this recheck directory.
