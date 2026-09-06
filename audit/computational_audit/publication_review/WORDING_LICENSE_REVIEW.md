# PUB2 wording and licensing-scope review

6 September 2026. Only the three assigned publication sources were read. No release code, expensive inventory, prior review, handoff, state, or active regeneration data was used. The longer scope record is in `PUBLICATION_WORDING_REVIEW.md`.

Exact reviewed SHA256 values:

- `build_tools/build_release.py`: `9e19adf284c3bae2e0ca0534870a1d9fc6a1c6c56f8474f0cd76d7e7e5b7769c`
- `release_additions/ARCHIVAL_ERRATA.md`: `253a03c9a192d42523e0d7acbe20a59b780328d179784c63af79666526b0decd`
- `release_additions/clarifications.tex`: `3da39993a46dd380d43f142692a84c254e1f48b5b31b7b1ffcdf8e7b8c8a2279`

## Required publication fixes

1. **Bind the actual fresh asset before presenting the generated release as complete.** The README template, lines 95–99, asserts full fresh recomputation and distribution of the separate raw asset. The builder's visible prerequisites, lines 37–43, check only a completion-summary JSON's flags/counts and existence of `FINAL_AUDIT.md`. They do not require the raw asset, its complete portable-validation receipt, an asset manifest/hash, or the linked `audit/FRESH_EVIDENCE.md`. The final asset gate must enforce those bindings and document availability. A successful intermediate build alone does not establish the claims. This review did not inspect the actual corpus and does not assert that it is incomplete.

2. **Complete the upload recipe.** The generated numbered steps, lines 238–257, direct the operator to upload the main folder, publish a release, and optionally attach the main ZIP. Add a required step to attach the separate fresh-polynomial asset and its manifest/checksum before publication, or explicitly state its alternative delivery location. Otherwise following the recipe can omit evidence the README says is distributed.

## Wording and scope that passed this review

The Markdown errata and TeX addendum agree, retain the finite-box scope, preserve frozen bytes, distinguish new audit evidence from historical reports, and avoid claiming finished Lean verification or external acceptance. The mathematical audit and internal-referee verdict claims still require their separately checked evidence.

No internal licensing-scope contradiction was found. Original prose and eligible data rights use CC-BY-4.0; original software, including embedded program listings, uses GPL-3.0-or-later; third-party terms and rights not held by the licensor are excluded. The detailed scope covers the unchanged inner archive and separates requested scholarly citation from license obligations. This is a consistency review, not a determination of ownership or a completed third-party inventory.

Reproduction prose correctly separates the archived seven-stage replay, fresh raw validation, integrity-only checks, and unpack-only mode. Actual execution, resource limits, file sizes, pagination, and final link targets were not tested here.

## Official-source checks

The author correction and submission/revision years match [arXiv](https://arxiv.org/abs/2211.06810). The box bounds and linked [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/) match [Epoch's page](https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients). The lrcalc version-2 prerequisite and GPL-3.0-or-later wording match [PyPI](https://pypi.org/project/lrcalc/2.1/). The 25 MiB browser limit and Zenodo guidance match [GitHub's size documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) and [citation documentation](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

Publication readiness is conditional on the final asset gate and upload-instruction fixes above.
