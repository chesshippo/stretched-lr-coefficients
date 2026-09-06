The article's propositions E, R and P have the following concrete evidence.
Paths below are relative to the extracted packet. Set
`OLD=problems/stretched-lr-coefficients/runs/20260905T173132Z` and
`NEW=problems/stretched-lr-coefficients/runs/20260906T041206Z` when reading them.

| Obligation | Evidence and replay |
| --- | --- |
| E: exhaustive necessary domains | `$OLD/independent_full_domain_enumeration.py` and `enumerate_small_minimum_domain.py`, their complete output files, and the original domain lists. The replay compares all prescribed counts, size distributions and source hashes. |
| R: checked reductions and complete residual cover | `$OLD/audit_core_certificates.py`, `audit_combined_core_cover.py`, `audit_small_minimum_cover.py`, all path and boundary JSONL certificates, index lists and reports. Every recorded local premise and the complete cover are checked. |
| P: exact nonnegative core polynomials | Complete `$OLD/conditional_scan/results.jsonl` and `small_minimum_signs/results.jsonl`, their manifests, and `audit_core_polynomial_records.py` / `audit_small_polynomial_records.py`. The cores number 346,537 large and 12,415 small, totaling 358,952. The separately source-bound recovery of original large index 1104809 is in `hard_case_current_source.json`. |
| Additional E/R checks | `$NEW/proof_supervisor/fresh_er_manifest.json` binds all six auxiliary enumeration/reduction scripts and result files. They use new enumerator/checker implementations but share the lrcalc backend; they are not an independent LR implementation. |
| Exact model and engine controls | `$NEW/certificate_closure/audit_binding.py`, `binding_result.json`, dependency snapshots, and all retained Normaliz `.in`/`.out` controls. The controls include nontrivial quasiperiods, a negative-coordinate interval, empty/lower-dimensional examples, and a negative monomial coefficient. |
| Independent degree-12 calculation | `$NEW/computational_appendix/degree12_full_latte.json` records the completed independent LattE cross-check. This is one additional case, not a complete second-engine corpus computation. |
| Fresh exact P regeneration | `$NEW/certificate_closure/recompute_core_polynomials.py` and `RECOMPUTE.md` provide the supported optional route, with exact source-ID/triple/coefficient matching and retained fresh raw outputs. |

The seven-stage audit is the original source-bound
`$OLD/replay_full_box_certificate.py`, called by the top `verify.py` in a
private temporary working directory. It does not read earlier review opinions
to decide any mathematical comparison. Fresh reports have distinct output paths.

`MANIFEST.json` binds every file in this packet. It explicitly declares and
checks these five nested file manifests: the original 53-file manifest;
`FROZEN_READABLE_MANIFEST.json` (93 files);
`mathematical_appendix_extra_manifest.json` (44 extra files);
`$NEW/certificate_closure/MANIFEST.json` (36 local files); and
`$NEW/proof_supervisor/fresh_er_manifest.json` (six local files).
The two scan manifests also have their input, verifier and specification
hashes checked. The frozen readable-manifest SHA-256 is
`0c0cf5e476155d11228259ae515827179023f01e3aede851fd2bb6d35e663465`.

Preserving the original 53-file manifest requires three older manuscript files
and historical composition/admission metadata. The closure manifest also
requires its historical `REPORT.md` and an earlier incorrect interval control;
the corrected control is `negative_interval_fixed/`. These files remain
archival and outside the 93-file readable appendix. The historical
`manuscript/v008.tex` is included because `independent_e.py` records its hash.
Historical prose mentioning partial coverage or obsolete positivity assumptions
describes earlier stages; the present theorem and its dependencies are in v010.

The full finite replay verifies records, coverage and fresh base counts. It
does not identify a polynomial from a few values. P relies on exact Normaliz
Ehrhart output for the literal lattice/hive model and the mathematical
polynomiality argument in the article. The historical journals preserve exact
coefficient records, but most historical raw Normaliz temporary files were not
retained. Later executable censuses are historical metadata, not retroactive
per-case execution attestations. These are explicit conventional-software trust
limits; hashes alone do not prove the correctness of an Ehrhart algorithm.
