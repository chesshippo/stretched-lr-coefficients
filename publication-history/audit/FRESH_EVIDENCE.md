# Complete fresh computational evidence

All **358,952 complete polynomials** were recomputed with exact Normaliz
arithmetic and matched every one of their **2,745,084 rational monomial
coefficients**. The independent portable validator then rebuilt the complete
source catalog and re-read all actual raw inputs, outputs and receipts.

The separate GitHub release asset is **stretched-lr-fresh-evidence.zip** (372,649,196 bytes).
SHA-256: `a4578424a704ac961786072b7694f58eaa071b24304ba64183f868a51ba028f1`.
Its complete file manifest is pinned in FRESH_EVIDENCE.json. Keep this asset
alongside the main release; attach it through GitHub's release-assets interface.
Its size exceeds ordinary repository-file upload limits. No upload has been
performed by this audit.

Extract the main release and this supplement as sibling directories. From the
supplement directory, reconstruct the frozen source packet without executing
any packet code, then verify the raw evidence:

    python3 -I -B tools/unpack_frozen_packet.py --release ../stretched-lr-full-proof --workdir ../stretched-lr-inspection

    python3 -I -B validator/validate_raw_supplement.py --packet ../stretched-lr-inspection/packet --raw raw --catalog-dir catalog > verification.json

Use Python 3.11 or later. This command needs no Normaliz, lrcalc, LattE, network
service or original runtime path. It checks the full source universe and exact
raw polynomial coefficients. Success requires COMPLETE and 358952 verified
cases; a bounded check never reports completion. The supplement also includes
the 512-case development fixture and the validator's 40 hostile-input tests.

Normaliz algorithm correctness and the observed execution remain part of the
trusted exact-software model. Raw inspection is not a cone-certificate proof,
a second complete LattE run, Lean verification or external acceptance. See
FINAL_AUDIT.md and the supplement README for the execution history and limits.

The original reviewed evidence archive remains byte-identical. This supplement
adds a separately reproducible record of a new full computation; it does not
replace the original source manifest or rewrite historical referee reports.
