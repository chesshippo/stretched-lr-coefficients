# Fresh-supplement publication usability review

6 September 2026. Read-only source inspection; no builder, arithmetic engine, test suite, active batch, or raw record was run/read. Parent is separately reviewing asset/identity gate relationships.

## Reviewed sources

- PUB2 `build_tools/build_fresh_supplement.py`: SHA256 `da94848ee98b310934d243ce0679ca2ac17ca26b254549569d0687df2c54207b`.
- PUB2 `build_tools/reproduce.py`: `4462c6301b35888a7bdfddc15d7ba204993246451c7bcf59f64af3a6f1eec369`.
- Frozen replay packet `verify.py`: `14572ca1a3118e5b8bb18ad01199520b5c7407e51bc1ef6e67896489163d540a`.
- Delivered-source `portable_validator/test_validator.py`: `f33db195f84504a7641b79c8f514398c52ea6b250efd15a7e36ad930670e6322`.
- Delivered-source `portable_validator/validate_raw_supplement.py`: `13706acbdfa99a3bd20c6f2c857a2a410cbe0d3be477a8b007e624ad60f7f0d9`.
- Delivered-source `portable_validator/README.md`: `bfe1e15e629d925a60b5d462eb7cf581a0a34d70257ddfdab1dbab77fe6fb025`.

## Required usability corrections

1. **The documented end-to-end portable route fails on Windows before reaching the portable validator.** The recommended main-release `reproduce.py --unpack-only` command invokes the frozen `packet/verify.py --manifest-only`. That branch uses only standard-library imports and does not launch arithmetic engines. However, its `integrity()` builds the actual file census with `str(path.relative_to(root))`, whereas the frozen manifest has slash-separated names. Windows produces backslashes, so its census comparison fails. Fix the outer reproducer's manifest-only route using portable path handling without changing frozen bytes, or explicitly limit that preparation route to POSIX and provide a Windows extraction/verification alternative. This conclusion is static; no native Windows test was run.

2. **The documented hostile-suite command writes inside the packaged, hashed validator tree.** The builder recursively includes all files below `portable_validator`, including historical `test_artifacts`. The delivered suite fixes its artifacts directory at `HERE/test_artifacts` and rewrites `genuine_512_api.json` and `test_result.json`. Running the advertised command can therefore alter files pinned in the supplement manifest and needs a writable installation. Put test outputs in an explicitly separate fresh work directory, or instruct readers to run a disposable copy of the validator. State where results are written; preserve shipped historical receipts.

## Checks that passed source review

- Both the outer unpack-only program and the frozen manifest-only branch have standard-library-only imports. The unpack command launches another Python process for manifest checking, but no Normaliz, lrcalc, LattE, NumPy, or network operation appears on that branch.
- The fresh full-validator command supplies all three explicit input locations. Its standard `sqlite3` requirement is stated in the packaged validator README; recorded engine paths remain provenance strings. No producer installation is needed for raw validation.
- The builder supplies the initial fixture under `tests/initial-512`; the printed hostile-suite command uses that exact path and all arguments required by the delivered test parser. The genuine-fixture test demands 512 cases and BOUNDED_VALIDATION. There are exactly 40 test methods. The bounded tests are clearly distinguished from complete-corpus verification.
- The README identifies the main packet as a required companion and treats archived producer scripts as execution provenance, not a portable launcher. It points fresh arithmetic-engine runs to the original packet's reproduction instructions.
- License placement and scope are internally consistent: original software/configuration uses GPL-3.0-or-later; explanatory material and eligible dataset rights use CC-BY-4.0; third-party notices and rights not held by the licensor are excluded. Both full license texts and separate NOTICE/scope/third-party documents are copied or generated. This is source-level consistency, not an executed inventory or ownership determination.
- The prose preserves the exact-software/execution trust boundary and disclaims full LattE repetition, Lean completion, and external acceptance.

## Minor wording qualifications

The packaged validator README says its suite reconstructs the complete catalog once, but the self-rehashed-catalog test intentionally calls source preparation again and rebuilds it a second time. Remove “once” or explain that additional rebuild. The hardcoded migration count of 15,872 and resource estimates require support from the separate final execution records; this task did not inspect those records. The old layout-dependent `review/static_probes.py` is explicitly identified as historical review evidence, while the advertised delivered test takes explicit paths, so those two entry points are not silently conflated.

No other source-level wording, fixture-interface, or licensing-scope blocker was found. The two corrections above and the separately reviewed asset/identity gates remain prerequisites for an unqualified portable-publication claim.
