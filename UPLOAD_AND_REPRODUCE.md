# Upload this single package

1. Unzip **stretched-lr-complete-proof.zip**.
2. Create a new public GitHub repository.
3. Upload everything **inside** the extracted `stretched-lr-complete-proof`
   folder, preserving its folders. `README.md`, `paper.pdf`, `CITATION.cff`,
   `AUTHORS.md`, `LICENSE` and `LICENSING.md` belong at the repository root.
4. For browser uploads, first upload everything except the `audit` folder.
   Commit those files. Then upload the entire `audit` folder and commit again.
   Each of these two batches has at most 100 files; every file is at most
   20 MiB. Keep all files in `evidence/parts` and `fresh-evidence/parts`.

The complete evidence is already included. This publication route uses the
repository's normal file upload; a separate release asset is optional.
Maseeh Ghodsi is the credited author and project lead. The included citation,
authorship and license notices document that attribution. Any later repository
URL or DOI should be the actual published identifier, not an invented one.

## Reproduce the reviewed finite audit

Use Python 3.11 or later, with assertions enabled:

    python3 -m pip install -r requirements-audit.txt
    python3 reproduce.py --workdir ../stretched-lr-verification

The lrcalc Python bindings may require the LR Calculator C library. See
https://sites.math.rutgers.edu/~asbuch/lrcalc/ if installation requires it.
The command reconstructs the original proof packet and runs all seven finite
audit stages. It does not recompute all Ehrhart polynomials or run Lean.

For integrity checks without mathematical replay:

    python3 -I -B reproduce.py --manifest-only
    python3 -I -B unpack_fresh_evidence.py --manifest-only

## Inspect every fresh computation

The fresh evidence was split only for repository upload. Reconstruct and
extract its exact audited ZIP, then reconstruct the frozen source packet:

    python3 -I -B unpack_fresh_evidence.py --workdir ../stretched-lr-fresh-inspection
    python3 -I -B audit/code/unpack_frozen_packet.py --release . --workdir ../stretched-lr-inspection

From this repository directory, run the portable full validator:

    python3 -I -B ../stretched-lr-fresh-inspection/stretched-lr-fresh-evidence/validator/validate_raw_supplement.py --packet ../stretched-lr-inspection/packet --raw ../stretched-lr-fresh-inspection/stretched-lr-fresh-evidence/raw --catalog-dir ../stretched-lr-fresh-inspection/stretched-lr-fresh-evidence/catalog > ../stretched-lr-raw-verification.json

Success reports COMPLETE with 358952 verified cases. This standard-library
route needs no Normaliz, lrcalc, LattE, network service or original machine
path. Use new working directories; the scripts refuse to overwrite existing
ones. Allow several GB of free disk space. Full raw validation took about
139 seconds on the audit host. Full mathematical and software-trust limits
are stated in the paper and audit/FINAL_AUDIT.md.

For redistribution, retain the applicable licenses, authorship and third-party
notices. The previous publication instructions are preserved as history in
publication-history/; follow this file for the current single-repository bundle.

GitHub upload documentation:
https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
