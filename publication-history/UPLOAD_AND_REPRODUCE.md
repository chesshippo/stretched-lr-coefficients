# Upload and citation

1. Extract stretched-lr-github-release.zip. Create a new GitHub repository and
   upload the contents of its stretched-lr-full-proof folder. Include both
   LICENSES and evidence/parts. The six parts are individually at most 20 MiB;
   every included file fits the documented 25 MiB browser-upload limit.
2. Keep README.md, AUTHORS.md, NOTICE, LICENSE, LICENSING.md, CITATION.cff and
   CITATION.bib at the repository root. GitHub can display its Cite this
   repository control from CITATION.cff. The supplied author credit is Maseeh Ghodsi.
3. Publish a release tagged v1.0.2. For a durable citable record, connect
   the public repository to Zenodo before publishing a release; Zenodo can
   archive it and issue a DOI. No DOI or public timestamp is invented here.
4. Add the actual repository URL and issued DOI to the citation metadata after
   publication. That creates a new metadata revision; preserve the frozen proof,
   six evidence parts and archive identity. Reissue checksums for changed files.
5. Attach stretched-lr-fresh-evidence.zip and its .sha256 file as assets of the
   same GitHub release. Include stretched-lr-github-release.zip and its .sha256
   file there as well. The fresh evidence is larger than repository-file upload
   limits and belongs in release assets. Verify its hash against
   audit/FRESH_EVIDENCE.json. The full new raw computation requires this asset.

The supplied ZIP can also be attached as a GitHub release asset. A ZIP stored
as a single repository file does not expose README/CITATION to GitHub. For a
normal browsable repository, upload the extracted contents instead. Do not
push the original research repository history, which contains oversized files.

## Reproduce the reviewed audit

Python 3.11 or newer is required. Install the pinned Python dependencies:

    python3 -m pip install -r requirements-audit.txt

The lrcalc Python bindings may need the LR Calculator C library version 2
installed first; follow https://sites.math.rutgers.edu/~asbuch/lrcalc/ and
https://pypi.org/project/lrcalc/ if a wheel is unavailable on your platform.

    python3 reproduce.py --workdir ../stretched-lr-verification

This verifies every part and the reconstructed archive SHA-256, extracts the
unchanged archive, and invokes its original top verifier. The verifier checks
all manifests and the complete seven-stage finite audit. Results are saved in
the new working directory. Existing working directories are never overwritten.
Roughly 2 GB of memory and several GB of free disk space are needed. Do not use
Python -O or set PYTHONOPTIMIZE.

    python3 reproduce.py --manifest-only
    python3 reproduce.py --unpack-only --workdir ../stretched-lr-inspection

The first command checks only integrity. The second reconstructs the packet
and checks all nested manifests without the finite audit. Neither is reported
as a passing full mathematical replay. After extraction, the original
REPRODUCE.md gives the separate full Ehrhart-regeneration route. That route
requires additional exact engines and substantially more computation.

The separate fresh-polynomial evidence asset retains the exhaustive audit's
raw outputs. Its validator and instructions are in audit/FRESH_EVIDENCE.md.
If redistributing an extracted subset of this mixed archive, carry the
applicable LICENSE, LICENSES/CC-BY-4.0.txt, LICENSING.md, NOTICE and third-party
credit with it. The historical inner ZIP's lack of redundant license files
does not remove the outer grant or its applicable notice requirements.

Primary documentation:
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
