# Stretched Littlewood–Richardson coefficients: complete finite-box proof

**Credited author and project lead: Maseeh Ghodsi.** Version 1.0.2, prepared 2026-09-06.

[Read the paper](paper.pdf) · [Errata](ARCHIVAL_ERRATA.md) · [Exhaustive audit](audit/FINAL_AUDIT.md) · [Citation](CITATION.cff) · [License scope](LICENSING.md)

This release presents a computer-assisted proof that every ordinary monomial
coefficient of the stretched Littlewood–Richardson polynomial is nonnegative
for every balanced partition triple with lengths at most 7 and sizes at most 30.
It covers the entire box in [Epoch's problem](https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients).
The unrestricted positivity conjecture is outside this result.

The proof reduces a complete necessary domain to 358,952 residual polynomials.
The complete finite audit checks enumeration, local reduction certificates,
coverage and all residual records, including fresh LR base counts. It relies
on exact Normaliz and lrcalc computations. The exhaustive audit additionally
recomputed all 358,952 whole polynomials, matched every rational coefficient,
and retained actual engine inputs, outputs and execution receipts. Those new
raw records are distributed as a separate release asset; see
[fresh evidence and verification](audit/FRESH_EVIDENCE.md). The default
seven-stage command below checks the frozen archive's records; the fresh raw
evidence has its own validator.

Two independent AI referee sessions returned MINOR and FLAWLESS; all 24
requested computational checks passed. These were internal automated reviews.
No human peer-review, Epoch endorsement, completed Lean verification or DOI is
claimed by this release. AI assistance is described in AUTHORS.md.

Version 1.0.2 includes explicit integer-width and positive-rank conventions,
a correction to the general parser description, and an archival reference
attribution correction. Every actual certificate passed the independent strict
audit. The unchanged 19-page frozen manuscript follows the cover and addendum.

## Reproduce

Use Python 3.11 or newer with assertions enabled:

    python3 -m pip install -r requirements-audit.txt
    python3 reproduce.py --workdir ../stretched-lr-verification

The working directory must be new. The script reconstructs the original
reviewed archive, checks its SHA-256, extracts it, and invokes its complete
seven-stage audit. Allow approximately 2 GB of RAM and several GB of free disk
space; the audit took about two minutes on the validation host. Dependency
installation may require the lrcalc library; see UPLOAD_AND_REPRODUCE.md.

For an integrity check without extraction or mathematical replay:

    python3 reproduce.py --manifest-only

All six parts must be present. Each is at most 20 MiB so it fits GitHub's
browser-upload limit. Do not push the original research workspace, whose
history contains larger files. Upload the contents of this extracted release
to a new repository. See UPLOAD_AND_REPRODUCE.md.

## Credit and reuse

Please cite Maseeh Ghodsi and the title/version in CITATION.cff when discussing or
building on this work. Original paper, documentation and eligible data rights
are licensed under CC BY 4.0; original project software is GPL-3.0-or-later.
Preserve attribution and applicable notices when those licenses require it.
Cited mathematics and third-party software retain their existing credit.

Licensing applies to rights in the covered material. It does not establish
ownership of mathematical facts or guarantee discovery priority or acceptance.
