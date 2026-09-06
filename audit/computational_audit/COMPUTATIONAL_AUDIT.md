# Fresh adversarial computational audit of the v010 stretched-LR proof

Date: 2026-09-06. This is the independent computational sub-audit requested by the supervisor. Its proof inputs were the frozen specification, manuscript v010, and the exact released ZIP. No earlier referee report, HANDOFF, ledger, attempt transcript, or campaign state was consulted. Archived program source, data, producing metadata and raw control outputs were allowed inputs. The supervisor subsequently requested a separate review of the newly written parallel regeneration wrapper; that supplementary review is distinguished below.

**Finding:** I found no inconsistent polynomial in the frozen data, uncovered residual member, invalid actual reduction edge, bad endpoint, or incorrect hive-sign convention. I independently rechecked every recorded path and final exclusion, the complete Horn catalog, all journal records and their source binding, and all residual coverage. Several adversarial examples demonstrate exactly what the saved-record and raw-receipt checkers do not establish. In particular, a saved-record audit is not a fresh full-polynomial computation. Nothing in this sub-audit is a completed Lean proof or an independent verification of Normaliz's implementation.

## Evidence identity and execution scope

The local specification and manuscript were byte-identical to their copies extracted from the exact release archive:

| Input | SHA-256 |
|---|---|
| spec.json | `2b9f91614a3e5aa0af887391442819935a5e45d8198edb086bfdca19f99111b0` |
| manuscript/v010.tex | `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45` |
| frozen verifier/verify.py | `65220dd44908959312cc38fbc0ec6bd55c292e193fe074ffd69a6854298312a8` |
| released top manifest | `f835cbc7ae315eb181139a812d24c11ee29bd747735311eb510bcd09b0aa56f3` |

I extracted only under this audit directory and separately ran the release's manifest-only command on that extraction. It verified all 131 top-manifest entries, the exact file inventory, all five nested manifests, and both source-binding manifests before and after the check. See `extracted_integrity.json`. This was an integrity check; its `ehrhart_computations_repeated` field is false.

The new code is `adversarial_checks.py`. Its corpus pass completed in approximately 135 seconds, with a separate final-cover pass taking approximately 7 seconds. The latter rebuilt the catalog using a literal cell-filling routine, made 437,042 fresh LR factor calls, and independently checked the final reductions. The bounded engine controls are six actual Normaliz executions with retained inputs and outputs. There was no full corpus Ehrhart regeneration in this sub-agent. The supervisor's independent release replay and any subsequent full regeneration have separate receipts and must be reported separately.

## E: enumeration and excluded low base counts

The formal domain requires outer size 1 through 30, rank at most seven, positive primitive parts, normalized inner order, no full-column reduction, strict containments, positive proper deficits, the strengthened-shortening inequalities, and all six representative sizes at least the source size. The base coefficient must be at least three.

I inspected both enumeration implementations against these literal requirements:

* The coin dynamic program processes available part sizes in increasing order, uses ascending totals for unlimited multiplicity, and appends a part only when the tail has fewer than seven parts. The resulting reversed tuples enumerate partitions, not arbitrary compositions. A separate recursive partition generator gave exactly the same sets, without duplicates, for every size 0 through 30.
* The length `< n` restriction for inner partitions is precisely the zero last-part condition at the outer rank. Strict containment and interlacing are imposed coordinatewise. They are equivalent to containment in the manuscript's kappa; neither imposes an extra heuristic cutoff.
* The vectorized shortening filter checks the deficit side of the minimum bound. Its other side is exactly the separately checked interlacing inequality, so it has not silently dropped half of condition (16).
* The vectorized six-size tests use the six actual sizes from equation (13). The original contained-partition implementation uses their rearranged form (17). I checked the algebraic equivalence.
* At equal inner sizes, the tuple comparison retains one exchange representative. Zero padding preserves this order. Primitive-gcd filtering, size balance and base-count filtering are applied after these exact necessary tests.
* For rank zero, the empty triple is separately settled. Rank one cannot survive the balanced strict-containment necessary domain. There is no missing low-rank residual case.

Every stored domain row passed a fresh independent implementation of the literal necessary conditions, strict input types, partition monotonicity, balance and normalized order. The small file has 37,530 distinct rows. The file used for the large scan contains **1,271,381** rows because it also retains 16,153 size-23 rows; the large proof domain is precisely its 1,255,228 size-24-through-30 rows. Treating the whole physical file as the large domain would double-count size 23. The actual scripts consistently restrict the large scope.

This sub-audit independently checked the full partition universe and every retained row. It did not write a third full all-pairs enumeration of every possible inner pair. Complete set reconstruction is performed by the archived independent enumerator in the supervisor's seven-stage replay. My source inspection found no omission in that enumerator's acceleration, and the new partition-set equality check independently validates its universe.

The c=0,1,2 exclusions are mathematical inputs, not empirically inferred positivity thresholds. I implemented an independent literal cell-filling LR routine: fill the skew diagram in reverse reading order, directly check the already filled right and upper neighbors, content bounds and every lattice-word prefix. It agrees with lrcalc on **all 16,461 normalized balanced triples** of outer size 0 through 10 and lengths at most seven. These include 13,738 zero cases, 2,602 value-one cases, 119 value-two cases, and two larger cases. Fresh lrcalc evaluations at t=2 and t=3 passed all **32,918** controls predicted by the low-c theorems. This is a bounded cross-check of the implementations and theorem application, not a proof of the all-stretch theorems. See `partition_low_c_controls.json`.

## R: every identity edge and endpoint

The new edge checker uses strict integer and partition validation and reconstructs every exact target. It separately checks containment of both source inners in the outer partition and the rank bound. Its checks are not calls to the archived edge checker.

| Rule | Premises and target independently checked |
|---|---|
| gcd | Positive integer scale at least two, equal to the gcd of all parts; every part divided by that scale. |
| full columns | Removed inner column counts equal the padded last parts, positive total removal, outer last part large enough; subtract the sum from the outer and the separate amounts from the respective inners. |
| empty row | Valid row index, equality with the selected inner part, positive deleted outer part; delete the same index from those two partitions only. |
| strengthened shortening | Integer a and proper cut k; literal q and b; both inequalities in (6); subtract a from the first k outer and selected-inner parts. |
| six representatives | Zero last parts in both inners; construct C as the outer complement, then construct the three starred partitions and determinant weight from the symmetric tensor invariant. Select the relevant outer complement and two inners. This avoids copying the archived five closed target formulas. |
| rectangular shortening | p,q,a positive, p+q within the rank; both inner gaps; outer gap and the sum-of-next-inner-parts bound; subtract a from precisely p+q, p and q parts. |

Every local edge preserves the polynomial except gcd, whose positive scale is accumulated. The source of each edge must equal the previous normalized target. The final target and total scale must equal the record. Every endpoint is in the original box and has key at most the source key. Equality is checked as equality of normalized triples, so a nontrivial loop cannot become an exclusion merely because it has a favorable status label.

The complete path results are:

| Stage | Sources | Fixed | Strictly smaller endpoint | Out-of-box intermediate paths | Largest intermediate outer size | Maximum path length |
|---|---:|---:|---:|---:|---:|---:|
| First paths | 1,255,228 | 760,303 | 494,925 | 415,847 | 89 | 11 |
| Second paths | 559,665 | 362,731 | 196,934 | 1,532 | 45 | 7 |

The first stage contains 106,732 full-column, 1,433 gcd, 428,840 row-deletion, 470,514 shortening and 865,549 six-representative edges. The second contains 217,415 rectangular edges plus 24 full-column, 62 gcd, 7,592 row-deletion, 5,859 shortening and 19,024 six-representative edges. All passed.

Accumulated scales are also nontrivial data: first-stage counts are 1,253,795 with scale one, 1,373 with scale two, 57 with scale three and three with scale four. Second-stage counts are 559,603, 58, two and two respectively. Every factor is a positive integer, as required for coefficient-sign preservation. Out-of-box intermediate sizes therefore do not invalidate the proof: the identities are unrestricted in size, lengths remain at most seven, and every actual final exclusion returns to the box with a smaller key.

The old `REACHES_BASELINE` and `BASELINE` labels mean only that the final outer size is at most 23. The proof's least-key argument uses a smaller witness there and does not require an earlier positivity baseline. Some archived report prose still mentions Pos23; that stale explanation is not a premise of the checked v010 cover.

## R: Horn catalog, factors, and final second reductions

I reconstructed the entire essential Horn catalog independently with the literal cell-filling routine, rather than the archived row-array DP. The subset-partition formula is tau(I)=(i_r-r,...,i_1-1), with the adjustment for stored zero-based indices. Balance allows most subset triples to be rejected without a count. The **5,521** remaining independent cell counts reproduce exact catalog sets of size **3, 12, 41, 142, 521, 2,042** at ranks 2 through 7, with no duplicates.

Every used Horn record then passed literal boundary equality, exact selected-index factor construction, balanced factor sizes, positive smaller outer sizes and the box constraints. Fresh factor coefficients agree with the records and multiply to the source coefficient. There are 200,638 large and 17,883 small Horn exclusions, hence 437,042 fresh factor LR evaluations in this check. I also separately compared **every explicitly stored small Horn factor pair** with its literal target. Those factor fields are redundant in the original checker, which recomputes the factors without comparing the stored `factors` field; the actual fields are correct.

For the final second reduction, I independently searched integer p,q for the three strict gaps and the inequality mu_p+nu_q >= lambda_1+lambda_(p+q+1)+1. I rebuilt the target, checked it is a balanced partition triple in the box with smaller outer size, and recomputed its base LR coefficient. The 16,194 exclusions actually used after the second path stage all pass. The small stage similarly contains 6,300 rectangular and 932 second-reduction exclusions, all checked from their literal parameters and exact targets.

One attempted extra validation intentionally surfaced a scope subtlety: `classical_second_affected_core_indices.json` has **83,494** entries, not 16,194. It was probed on the earlier Horn core; 67,300 entries had already been excluded by the second paths. I initially asserted that this file was a subset of the later fixed points, which is stronger than the manuscript and is false. `final_cover.log` retains that audit failure. Inspection established the correct relationship: the file is a subset of the earlier Horn core, its intersection with the later fixed points has size 16,194, and the final core is exactly `rectangular_fixed - second_probe`. I corrected my audit scope, independently checked all 83,494 probe premises and target coefficients, and retained the successful corrected run separately. This is not a defect in the frozen cover.

The final disjoint cover unions and all source index sets agree. They leave 12,415 small and 346,537 large residual triples. See `corpus_inventory.json` and `horn_and_final_cover.json`.

## Hive coordinates, lattice, and signs

The source's `hive_system` uses the boundaries and all three rhombus families displayed in v010, orders free vertices by increasing a then b, and stores each inequality as `(constant, coefficient_vector)` meaning constant plus dot product is nonnegative. The Normaliz serializer moves only the constant to the last column. No variable scaling or sublattice is supplied.

I tested the manuscript's array-to-hive transformation directly, not just two row builders. At each rank 1 through 7 I chose every basis vector and zero in the space consisting of the padded inner partition and all triangular array entries. I formed the outer boundary from row sums, the content boundary from column sums, and all hive coordinates from F. I evaluated the actual source inequalities and compared them with the literal column, lattice and off-diagonal nonnegativity slacks in their exact source order. I also applied the manuscript's inverse difference formula to every coordinate, including the diagonal and triangular-support zeros.

All **119 basis-plus-zero cases** passed. These are exact linear-map identities, not random partition samples: the maps being compared are linear, so agreement on a basis and zero proves agreement throughout the corresponding real coordinate space. At rank seven the coordinate dimension is 35, equal to 20 balanced boundary degrees of freedom plus 15 free hive coordinates. The array/hive forward and inverse maps have integer coefficients. This establishes the asserted full integer-coordinate correspondence at the level of the written formulas; no lattice index or sign correction appeared.

The separate proof that the omitted diagonal inequalities follow from the content boundary and adjacent lattice inequalities is mathematically consistent with this mapping. The array row-sum bounds give boundedness. Positive-base hives have the expected origin-dilation constant term; zero-base cases use the separately stated saturation interpretation rather than identifying P(0) with the all-empty triple's coefficient.

## Actual bounded engine controls

I invoked the frozen Normaliz entrypoint with six elementary integer inequality systems, changing only the supplied system in memory and retaining the genuine input and output files. Each call had a 20-second bound and one Normaliz thread. The executable was Normaliz 3.11.1, SHA-256 `b09969f149e1d1f39aad3b1a60595553e9dad81792a7f94a9d903da5e066241d`, matching the historical later-snapshot hash.

| Control | Exact expected behavior | Actual result |
|---|---|---|
| Interval [-2,-1] | t+1, using negative coordinates | `[1,1]` |
| Interval [0,1/2] | Genuine period two | Rejected with reported period two |
| Point {1/2} | Genuine period two | Rejected with reported period two |
| Segment {(x,x):0<=x<=2} in the ambient Z² lattice | 2t+1 | `[1,2]` |
| Inconsistent interval x>=2, x<=1 | Empty polytope | Empty coefficient vector |
| Reeve simplex with parameter 13 | 1-t/6+t²+13t³/6 | `[1,-1/6,1,13/6]` |

The last test is an actual negative monomial coefficient from a non-LR polytope, not a synthetic negative LR example. It establishes that the engine/parser route does not mechanically force nonnegative polynomial coefficients. The period-two tests exercise actual quasipolynomial output, and the diagonal segment exercises a lower-dimensional polytope counted in the full ambient lattice. See `actual_engine_controls.json`, `controls/`, and `array_hive_linear_identity.json`.

Source inspection also confirms that the primary path checks process return codes and missing output, rejects nontrivial reported periods, parses integer numerators over a positive common denominator, strips trailing zero coefficients, requires an affine-dimension line and compares it to the polynomial degree. The enclosing polynomial validator checks the rank degree bound, constant term, base LR count, positive leading coefficient and integer nonnegative sampled values. The primary engine is a full Ehrhart calculation; those structural checks are additional consistency tests.

## P: complete journals, exact vectors, and error resolution

I scanned every byte-complete line in both frozen journals. There are 13,139 small computed records in 13,383,091 bytes and 509,106 large records in 544,824,662 bytes, consisting of 509,105 computed records and one historical error. All indices are valid and unique within their journal. Every computed record's lambda, mu, nu and c match its domain row exactly. I checked strict partition formatting, dimensions, degree bounds, coefficient signs, constant/leading/minimum fields, exact value-array length, every saved rational evaluation and uncached-engine flags. The actual saved value arrays all have D+3 entries; none is an empty or truncated value vector.

The separate `check_metadata_supplement.py` pass checked strict rational text syntax, all stored coefficient extrema and their indices, nonnegative integer engine metadata, positive vertex counts, every saved lrcalc/DP cross-check and every full-LattE range field. All **522,245** computed records including the recovery passed in about 14 seconds; see `metadata_supplement.json`.

The large historical error is index **1,104,809**. The separate successful record has the same exact triple, base count 160 and the frozen verifier hash, and its polynomial has degree 13 with nonnegative rational coefficients. It resolves precisely that source and is included once in the residual count. The historical error remains visible. There are no residual omissions after resolution. The small journal has 724 nonresidual computed entries; the large journal plus resolution has 162,569. Those extras do not inflate the core counts.

| Residual scope | Small | Large, including resolution |
|---|---:|---:|
| Members | 12,415 | 346,537 |
| Negative saved coefficients | 0 | 0 |
| Missing/unresolved records | 0 | 0 |
| Saved full LattE reproduction | 2,984 | 20,824 |
| Saved Normaliz-only full-polynomial route | 9,431 | 325,713 |

Every actual residual record has saved lrcalc checks at **all of t=1,2,3**, and every residual has a saved tableau-DP check at t=1. Although the source permits some cross-checks to be skipped, no such skips occur in this core. The seven-stage replay recomputes t=1 afresh; it merely checks the saved t=2,3 assertions for consistency with the coefficient vector. My two targeted adversarial examples also received fresh t=4 checks as described next.

The journals preserve coefficients, values and engine metadata, but most producing temporary Normaliz input/output files are absent. The saved `values` array is computed from the already obtained polynomial. It does not itself store independent LattE output; `latte_crosscheck=full` and the LattE range field attest that the producing code compared the engine's values with that array. Thus even the lower-rank historical LattE checks remain execution records rather than separately retained decomposition/count certificates.

The appendix's extra `degree12_full_latte.json` names a special 12-fold integral-dilation recovery computation and an absolute path ending `latte_check6_d12/result.json`. That recovery artifact and its special-route source are absent from the 132-file ZIP. This is supplementary to the Normaliz residual record, so it is not a missing core member. It should not be counted as independently inspectable extra LattE raw evidence from this release alone.

## Demonstrated blind spots in saved PASS/consistency checks

These tests use isolated copies or hoisted exact checker functions; the frozen data was never modified.

**1. A wrong positive polynomial passes the actual saved-record checker.** For small index 29,034 and large index 989,721, set

`Q(t) = P(t) + binomial(t,4) = P(t) + (t^4 - 6t^3 + 11t^2 - 6t)/24`.

Both actual P have large enough positive low-degree coefficients that every coefficient of Q remains nonnegative. Q has the same degree bound, constant term, positive leading coefficient, integer-valued nonnegative samples, base count and values at t=2 and t=3. Replace the saved coefficient vector and its derived value array by Q. The exact archived nested `check_polynomial` function accepts both mutations, even while freshly recomputing the true t=1 LR value.

Fresh independent t=4 lrcalc checks then establish that these accepted mutations are wrong for the actual triples:

| Case | True fresh c at stretch 4 | Mutated Q(4) |
|---|---:|---:|
| small:29034 | 25,100 | 25,101 |
| large:989721 | 1,068,801 | 1,068,802 |

This is a concrete non-identification witness, not merely the observation that there are too few points. See `record_mutations.json` and `mutations_fresh_t4_witnesses.json`. It does not show the original P is wrong or has a negative coefficient. The release hashes prevent unnoticed modification of its fixed bytes. It shows that an erroneous full-polynomial engine output with otherwise consistent recorded metadata could evade the sparse cross-checks, exactly why the proof must trust the full Ehrhart computation or regenerate it.

**2. The record checker accepts an empty value array and nonsensical engine metadata.** Both tested source checkers accept `values=[]`, because the code only requires a prefix of length at most 18 (`audit_core_polynomial_records.py:82`, identically in the small checker). They also ignore forged negative `hive_variables`, `normaliz_vertices` and `triangulation_size`. My complete corpus scan checked the relevant actual fields and found no such malformed record. These are checker-hardening issues, not actual corpus defects.

**3. The old edge normalizer accepts malformed raw partitions.** `audit_core_certificates.py:20` drops every zero before checking monotonicity, so `[3,0,2,1]` becomes the valid partition `[3,2,1]`. This contradicts the manuscript's general statement that malformed partitions are rejected: only trailing zeros should be ignored. At lines 44 and 48 any inner selector other than the literal `mu` is treated as `nu`; an invalid selector was accepted in a real shortening edge. My stricter whole-path scan found no internal-zero partition, invalid selector or bad integer parameter in the frozen path corpus. Unknown rule names and a wrong scale on shortening were correctly rejected in mutation tests.

**4. LattE point-mode equalities are not independently certified consequences of the inequalities.** On deliberately false LattE output reporting `x=1` for the interval `[0,2]`, `_parse_latte_taylor` accepts the feasible integral reported point and returns constant values one. The real interval has values 1,3,5,7,9. The paired correct Normaliz polynomial would reject this discrepancy. This is already disclosed in the verifier source: the point routine checks rank, integrality and feasibility of the reported equality system, while the claim that the original polytope is that point still depends on the engine and the other full-polynomial check. Missing Taylor exponents, duplicate exponents and nonzero exit status were all rejected in my tests.

**5. Local report booleans have narrower meaning than theorem acceptance.** The polynomial audits write `all_record_checks_pass=True` for the records they could parse, while separately reporting core completeness, unresolved errors and negative indices. In isolation that flag does not mean the entire core is covered or positive. The release's top command compares the expected seven stage reports, requires the fixed core total and complete replay, and rejects optimized Python so assertions execute. I found no route in the complete release command that turns one of the isolated examples above into an unnoticed altered frozen proof.

## Supplementary parallel regeneration wrapper

At the supervisor's request I reviewed `parallel_regenerate.py`, initial audited SHA-256 `1c026ad02a3922f628c6b9ccfeaefb2b435f71bf902a65a9a480a0d0e924a780`. This new program is not a frozen manuscript input. The initial findings below were corrected by the supervisor and independently rechecked, as recorded at the end of this section.

I found no direct missing-ID or false-COMPLETE bug in its full-corpus accounting. It requires the catalog hash, all 358,952 unique IDs and the small-band count; assigns each ordered batch once; rereads every compressed batch; checks the exact expected ID list; and only sets full completion when `--batches` is absent and the final verified ID set equals the whole catalog. Input bindings and runtime identities are rechecked at completion. A bounded run remains explicitly bounded.

However, its `verify_batch` checks the raw files only against hashes inside the receipt. It does not reconstruct the expected hive input, parse the retained polynomial output, check the invocation's return code or compare the invocation executable hash with the engine identity. I demonstrated this with a synthetic receipt for the actual small:29034 coefficient vector, paired with genuine retained input/output from the **different Reeve simplex control**. The wrapper accepted the packet because the wrong raw bytes were internally self-hashed. See `wrapper_mutation_result.json`; the fabricated packet is explicitly segregated under `synthetic_wrapper_mutation/` and is not proof evidence.

This is a semantic raw-to-source and raw-to-polynomial binding gap in the resume verifier, not evidence that any genuine producing call returned the wrong result. The per-case producing routine does directly run the frozen verifier and compare its full rational output. Recommended strengthening before an exhaustive independent-receipt claim: reconstruct and compare exact input bytes, parse all full output coefficients independently and match them to the expected vector, reject duplicate/missing/conflicting output blocks, and bind a successful invocation and executable identity. The supervisor was notified promptly.

Two smaller resource issues were reported: `--batches` should reject negative values, and the wrapper initializer does not propagate a timeout greater than 1,800 seconds into the verifier's separate `DIRECT_DEADLINE_S` cap. Default timeout 1,800 is unaffected. Neither issue permits false full-corpus completion.

**Correction independently confirmed.** The supervisor revised the wrapper, preserved the first draft and its 512-case validation separately, and requested a fresh independent check before launching the full corpus. Corrected-wrapper SHA-256 is `fdc1a6997fb3a66e4071cf5358e3c9cf53cc4108ab9e666af7ac28b2f92877cc`. I inspected the new semantic validator: it reconstructs and compares the exact hive input; requires a unique full polynomial block with strict integer numerators and positive denominator; compares every rational coefficient; checks embedding dimension, affine dimension, base lattice-point count and zero recession rays; and binds the successful, one-thread invocation and executable hash. Timeout propagation and negative batch-limit validation were also fixed.

I independently passed the corrected validator over **128 genuine prior computation records**, then rebuilt the wrong-polytope mutation using a genuine complete invocation receipt and rehashed every changed byte. It is now rejected specifically with `Raw input is not the exact source hive`. `wrapper_correction_recheck.json` records the exact code hash and both outcomes. I found no remaining blocking source/coverage/resume issue and notified the supervisor that the authorized full regeneration could proceed. This resolves the identified new-wrapper defect; it does not retroactively add raw engine outputs to the frozen journals, and it does not imply the full regeneration has completed.

## Regeneration effort and the remaining trust boundary

The recorded elapsed times for the core sum to approximately 43,997.216 seconds in the large journal plus 2,311.796 seconds in the small journal; including the separate 35.569-second recovery gives about **46,344.581 seconds**, or **12.87 hours of summed per-case elapsed time**. This is not CPU usage and not the elapsed wall time of the historical parallel run. It includes the producing program's multiple cross-checks and concurrent scheduling effects. The large-core median/p95/p99/max historical times are approximately 0.071/0.387/0.893/57.877 seconds; the small values are 0.104/0.526/0.828/2.525 seconds. They are planning data, not a reliable guarantee of reproduction time or a basis for declaring incomplete work complete.

The dependency chain remaining after the checked finite bookkeeping is explicit:

1. The mathematical all-stretch identities and the cited low-c/Horn/second-reduction theorems must be correct and applicable. This sub-audit compared the code with their v010 statements; independent literature and manuscript proof review belongs to the other audit task.
2. Enumeration relies on correct exact integer execution and LR counting. Independent generators, literal cell counts, fresh factor checks and complete equality audits provide substantial redundancy, not a machine-checked proof of Python or lrcalc.
3. At higher ranks the residual polynomial identification relies on the full Normaliz algorithm and its execution. Sparse values and hashes do not replace it. A fresh exhaustive regeneration can close the historical execution-record gap and retain source-bound raw input/output, but it still trusts Normaliz's exact implementation.
4. Both Ehrhart engines share the hive model; the independent linear array/hive correspondence and the tableau implementations address that common modelling risk.
5. No cone decomposition certificate for every residual, verified exact arithmetic backend, sorry-free Lean development, axiom census or statement-fidelity audit was produced by this sub-audit.

The concrete findings support the finite E/R bookkeeping and the consistency/coverage of P's saved records. They do not justify an invented guarantee that the full P computation has been independently regenerated, that external code cannot be wrong, or that the repository's final Lean DONE gate has been met.
