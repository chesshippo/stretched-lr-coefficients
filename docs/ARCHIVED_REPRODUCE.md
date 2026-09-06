Run the supported finite audit with Python 3.11 or newer:

```sh
python3 -m pip install -r requirements-audit.txt
python3 verify.py --output ../v010-verification.json
```

Keep the directory structure unchanged and do not use Python `-O` or set
`PYTHONOPTIMIZE`. The top verifier rejects symlinks, changed bytes, missing or
unexpected files, and inconsistent nested bindings. It checks every manifest
before and after the audit. Its JSON receipt and the separate
`v010-verification.finite-replay.json` record actual results and timings. The
seven-stage audit checks 358,952 core polynomial records with fresh LR base
counts; it does not launch the historical Ehrhart computations again.

For optional fresh exact Ehrhart regeneration, install Normaliz 3.11.1 and
lrcalc 2.1. Engine binaries are not distributed. Put Normaliz on PATH or set
`NORMALIZ` as supported by the frozen verifier. From the extracted packet:

```sh
python3 problems/stretched-lr-coefficients/runs/20260906T041206Z/certificate_closure/recompute_core_polynomials.py --root . --output ../v010-fresh-core --case large:16427 --timeout 30
```

To select the entire corpus, use a fresh or compatible resumable output
directory and omit `--case` and `--limit`:

```sh
python3 problems/stretched-lr-coefficients/runs/20260906T041206Z/certificate_closure/recompute_core_polynomials.py --root . --output ../v010-all-core --timeout 1800
```

The route uses the unchanged frozen verifier's hive model and exact Normaliz
parser. It rebuilds a source-bound SQLite catalog, matches each original ID and
triple, compares every rational coefficient exactly, and preserves fresh raw
inputs, outputs and dependency hashes. Completed cases are validated before
resume skips. `--limit 0` builds/checks the full catalog without new Ehrhart
computations; `--limit 2` limits each invocation to two new cases.

Read the complete `$NEW/certificate_closure/RECOMPUTE.md` (where
`$NEW=problems/stretched-lr-coefficients/runs/20260906T041206Z`) for selection,
resume, failure, timeout, dependency-binding and optional full LattE behavior.
The command is sequential with one Normaliz thread. It does not impose a
portable memory ceiling, and the largest cases require appropriate separately
controlled resources. The full 358,952-case regeneration was not launched for
this release. Archived controls and bounded tests do not imply that it was.

Original scanner drivers and their `scan_conditional_domain_combined_core.py`
helper are included for inspection. They refer to historical absolute paths,
campaign locks and mutable journals; they are archival sources, not supported
commands for an extracted packet. The supported full recomputation route is
the regenerator above. The auxiliary E/R scripts likewise retain their exact
historical behavior: they refuse overwriting adjacent reports, and the R
dependency census references a macOS lrcalc dylib path. Repeating them requires
a separate working copy and compatible environment. Their complete sources
and results are included without claiming cross-platform launcher support.

The exact original 53 files, both complete journals and all nested manifest
dependencies are present. Historical absolute JSON paths remain unchanged as
provenance; top verification and core regeneration locate their immutable
inputs relative to the extracted root. No network or provider credentials are
needed by these mathematical replay commands.
