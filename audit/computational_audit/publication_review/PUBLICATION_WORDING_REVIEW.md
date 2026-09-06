# PUB2 publication wording and scope review

Prepared 6 September 2026. This is a bounded, read-only publication-source review, not a mathematical acceptance or legal-ownership determination.

## Exact local inputs

Only these three PUB2 files were read; no release program was executed, no expensive inventory was run, and no prior review, handoff, state, active regeneration output, or generated asset was inspected:

| File under `runs/20260906T123424Z_exhaustive_release/` | SHA256 |
| --- | --- |
| `build_tools/build_release.py` | `9e19adf284c3bae2e0ca0534870a1d9fc6a1c6c56f8474f0cd76d7e7e5b7769c` |
| `release_additions/ARCHIVAL_ERRATA.md` | `253a03c9a192d42523e0d7acbe20a59b780328d179784c63af79666526b0decd` |
| `release_additions/clarifications.tex` | `3da39993a46dd380d43f142692a84c254e1f48b5b31b7b1ffcdf8e7b8c8a2279` |

## Findings requiring publication-gate coverage

1. **The generated fresh-evidence claims exceed this builder's visible prerequisites.** The README template at lines 95–99 says all 358,952 whole polynomials were recomputed and that their retained raw records are distributed as a separate release asset. The builder at lines 37–43 requires a completion-summary JSON with the expected flags/counts and existence of `FINAL_AUDIT.md`. It does not require the raw asset, a matching complete portable-validation receipt, an asset hash/manifest, or even the linked `audit/FRESH_EVIDENCE.md`. Therefore a successful builder invocation alone would not justify the distribution claim or establish that its fresh-evidence instructions are usable. This is not a finding that the actual corpus is incomplete: its state and assets were outside this review. It is a concrete condition the separately reviewed final gate must enforce. Before distribution, bind the full raw asset and its validation receipt, check the referenced documentation, and require the exact final audit bytes. If the intermediate built folder can be presented before that gate, label it as a staging build rather than a complete public release.

2. **The upload recipe omits a required fresh-asset step.** `UPLOAD_AND_REPRODUCE.md` as generated at lines 238–257 tells the operator to upload the main folder, publish a tag, and optionally attach the main ZIP. It does not explicitly instruct the operator to attach the separate fresh-polynomial asset that the README says is distributed. Add a required step naming that asset and its accompanying manifest/checksum before publication. A link to its instructions later in the document is useful but does not make the current numbered publication recipe complete. If the raw asset has a different delivery location, state that location and its binding in the recipe.

Neither observation requires changing the frozen mathematical statement. Their importance is the alignment of unconditional release prose with what a reader can actually download and validate.

## Internal wording and licensing consistency

No contradictory licensing scope was found in the three assigned sources. The README, NOTICE, cover, and detailed `LICENSING.md` consistently assign original explanatory material and eligible data rights to CC-BY-4.0, original software to GPL-3.0-or-later, and preserve third-party terms. The detailed scope explicitly handles the unchanged inner archive and treats embedded program listings as software. The qualification to rights actually held, the exclusion of mathematical facts and inapplicable AI-generated rights, and the separation of requested scholarly citation from license obligations are consistent. This review does not determine who owns any particular material or certify that all distributed source/font/license notices are present; doing so would require the actual asset inventory.

The Markdown errata and TeX addendum agree on the integer complement width, positive ambient rank, original parser limitation, and reference correction. Both preserve the frozen manuscript and distinguish new audit evidence from historical referee reports. Their prose confines the mathematical result to the stated finite box and preserves the unfinished Lean and unestablished external-acceptance status. The claims that every actual raw certificate passes and that the listed internal review checks passed require their separate computational/report evidence; those reports were intentionally not read here.

The default reproduction instructions clearly distinguish the historical seven-stage archive audit from the separate fresh raw validator. They also separate integrity-only and unpack-only modes from mathematical replay, require a new work directory and enabled Python assertions, identify the pinned Python requirements, and point to the native lrcalc dependency instructions. A virtual-environment example would be an optional usability improvement, not a blocking correction. Actual command behavior, resource bounds, nested manifests, PDF pagination/fonts, and all emitted link targets were not executed or inventoried in this task.

## Narrow official-source checks

- The Thawinrak author correction and the 2022 initial submission / 2024 revision dates agree with the [official arXiv record](https://arxiv.org/abs/2211.06810).
- The finite-box wording matches the bounds on [Epoch's problem page](https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients), whose own attribution-license link resolves to [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Thus the release's specific attribution of that source license is supported.
- The lrcalc 2.1 Python package's GPL version 3-or-later description and its LR Calculator version 2 prerequisite agree with its [official PyPI project page](https://pypi.org/project/lrcalc/2.1/).
- The claimed 25 MiB browser-upload limit agrees with [GitHub's current large-file documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). Whether every actual final release file fits that limit remains a separate inventory check.
- The suggestion to link a public repository to Zenodo and obtain release DOIs is supported by [GitHub's archival/citation documentation](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content). No issued DOI is claimed in these templates.

The observations were sent promptly to the supervising reviewer. Publication readiness remains conditional on the separately reviewed asset/gate checks and completion of the upload recipe.
