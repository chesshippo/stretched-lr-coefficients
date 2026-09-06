# Bounded PUB2 publication review

Reviewed 2026-09-06 UTC. **Verdict: publication gates need correction before
sealing or distributing the version that asserts complete fresh regeneration.**
This is a review of supplementary release code and wording; it identifies no
new counterexample to the frozen finite-box proof. No engine, complete raw
validation, repeated corpus inventory, or publication build was run. Active raw
data and shared source were not changed. All probe outputs are private to this
directory. See `bounded_probe_results.json` for exact reviewed source hashes.

## Required corrections

1. **Fresh-completion claims are gated only by a producer summary.**
   `build_release.py:38–43` accepts four fields in the producer's `complete.json`
   and requires only that `audit/FINAL_AUDIT.md` exists. The sealer repeats those
   status/count assertions at lines 63–65. Neither verifies a portable COMPLETE
   result, the fresh supplement's actual bytes, its manifest, or even the
   existence of the generated `audit/FRESH_EVIDENCE.json` and Markdown target.
   Nevertheless the README says every whole polynomial was recomputed and its
   raw records are distributed, and RELEASE.json sets
   `full_core_ehrhart_regenerated=True`.

   The bounded probe executes the exact four builder-gate statements with zero
   raw cases, no portable receipt or asset, a synthetically claimed COMPLETE,
   and a placeholder report. Those gates accept. This is an isolated gate
   counterexample, not a claim that an actual publication was built.

   Require a shared fail-closed gate in both builder and sealer. It should bind
   the exact frozen archive, source/catalog/engine/producer identities, the
   pinned portable validator, a portable result with `status=COMPLETE`,
   `all_core_regeneration_complete=true`, all 358,952 IDs and exact batches,
   the genuine producer completion receipt, and the actual supplement
   manifest/asset hashes. In particular, match the portable receipt's raw and
   metadata batch hashes to the supplement manifest so a separately valid
   receipt cannot accompany different raw files. A bounded receipt must never
   authorize these publication claims. Require every public audit/evidence
   document that the generated release references. The supervisor has agreed
   to implement this gate; revised bytes need a separate check.

2. **The sealer does not establish the six evidence parts' identity.**
   `seal_release.py:49` compares only PARTS.json with a previous publication's
   metadata. The later ZIP/extraction loop proves that the ZIP contains the
   same current bytes as its source tree. It does not prove those current part
   bytes match PARTS.json or the frozen archive. A changed part therefore
   leaves all the relevant sealer checks unchanged, yet the receipt still says
   `frozen_proof_and_evidence_unchanged=True`.

   The isolated production assertion accepted an unchanged part manifest with
   corrupted part bytes. Re-run the pinned public reproducer's
   `--manifest-only` check on the independently extracted release, or perform
   the equivalent ordered six-part size/hash and concatenated archive check,
   before SEALED. The current public `reproduce.py` already implements those
   strong checks; use them at sealing, not solely as a reader's later task.

3. **Optimized Python removes the sealer's safety and accuracy gates.**
   The sealer uses `assert` for author metadata, PDF identity, frozen proof
   hashes, evidence metadata, completion, symlink exclusion, size limits and
   extraction comparison, without an optimization guard. Its exact completion
   assertions reject a bounded receipt normally and accept it when compiled
   with optimization level 2. Reject optimized execution before any mutations
   in both publication programs, and preferably express essential release
   checks as explicit exceptions. The public reproducer and new strict-corpus
   script already reject optimized execution.

4. **Strict-audit startup executes unverified packet code.**
   `strict_corpus_audit.py:37–41` hashes the top manifest but runs
   `packet/verify.py` before checking that program against the manifest. A
   malicious or accidentally replaced verifier can therefore be executed by
   a command presented as checking the packet. The bounded witness copied the
   genuine manifest into a deliberately incomplete fixture and supplied a
   harmless replacement verifier that wrote a marker. The marker was written
   before the strict program later failed on its missing mathematical module.
   This demonstrates the startup boundary; it is not a false inventory PASS.

   Check every top-manifest entry and the exact safe file inventory with local
   trusted code before executing/importing anything inside the packet. At
   minimum, pin the top verifier before invoking its checks; the full local
   inventory approach also covers symlink and unexpected-file handling. Keep
   all output/scratch outside the packet, as the current new CLI already does.

## Wording and usability

- The separate supplement is not part of the main six historical evidence
  parts. The upload recipe currently tells the operator to upload the main
  folder and publish its tag, but never makes uploading the separate fresh
  asset/checksum a required step. Add that step with exact asset names and
  checksums, before publication. Root's planned `FRESH_EVIDENCE.json` and
  instructions should identify the two validation routes clearly.
- All final audit files and referred evidence are still staging prerequisites
  at this review point. Require the known public targets, and check their links
  against the final package. When including the historical computational
  sub-audit, preserve its explicit statement that it did not itself run full
  regeneration and its dated earlier-wrapper hashes. Describe the later
  corrected producer and complete run in the new final report; do not silently
  rewrite the historical review into an approval of later bytes.
- `strict_corpus_audit.py` prints `status=COMPLETE` even for `controls` or
  `extra`; the accompanying `mode` is essential scope. A publication gate
  should not treat that status alone as evidence of exhaustive inventory or
  final-cover checks. A less ambiguous public receipt would name the completed
  modes and explicitly state that this script does not freshly regenerate all
  residual Ehrhart polynomials.
- If a failed sealing attempt leaves SHA256SUMS, the current next attempt
  includes the old SHA256SUMS in its own input list and rewrites it, leaving a
  stale self-entry. Exclude SHA256SUMS from its own file census and fail early
  on pre-existing final outputs, or document one-shot staging. This is a retry
  usability issue, separate from the proof's mathematical validity.

## Checks supporting the intended release

The exact frozen archive is hashed before building, frozen TeX/PDF are retained
separately, and the sealer pins both original proof hashes. It compares the
included mathematical PDF body by non-whitespace extracted text. That is a
text-content comparison, not a general proof of visual identity; its receipt
accurately names the comparison mode. The generated cover includes the frozen
PDF through the intended `pdfpages` route. Citation metadata is checked against
the CFF schema and explicit author name. Main release creation and fresh
extraction use new paths, preventing accidental overwrite of an existing
publication. The main reproducer enforces ordered parts, fixed archive hash,
safe member paths, and scope-specific replay outcomes.

All **16 mathematical audit function bodies** in the packaged
`strict_corpus_audit.py` are AST-identical to the original
`adversarial_checks.py`; only copyright/license headers, CLI/setup and the mode
selection changed. Therefore this packaging diff introduces no altered
enumeration, reduction formula, final-cover condition or hostile mathematical
control. Its newly introduced trust boundary is the startup issue above.

The addendum correctly distinguishes the original parser's over-broad
description from the actual frozen records, states the integer-width and
positive-rank conventions, and leaves the original manuscript bytes intact.
The correction of the archived Thawinrak attribution is presented as archival
errata, without rewriting the frozen specification or referee bindings.

The original software GPL-3.0-or-later / explanatory text and eligible data
CC-BY-4.0 split is internally consistent with the SPDX header, mixed-archive
exceptions, third-party notices and limitation to rights actually held. The
wording disclaims ownership of mathematical facts and external acceptance.
This is a scope-consistency review, not a determination of copyright ownership
or a guarantee that every possible redistribution complies with law. Narrow
official-source checks are recorded separately in
`WORDING_LICENSE_REVIEW.md`.

## Exact evidence and limits

`bounded_probes.py` records small synthetic gate/startup witnesses and compares
the function ASTs. It executes neither the full builder/sealer nor mathematical
inventory and does not use active raw regeneration data. The reviewed builder,
sealer and strict-script SHA-256 values are respectively
`9e19adf284c3bae2e0ca0534870a1d9fc6a1c6c56f8474f0cd76d7e7e5b7769c`,
`8b1609800311c27a2dd3cce858e2aed3d5653edb7c2ae2f931217362393d5168`, and
`8c93eb53f26ffa7851bb774bf8587d9727915d14e83dbf848756fdd83485b397`.
These findings do not pre-approve revised source, an unbuilt release, an
unfinished raw supplement, full Lean verification, or external acceptance.
