# Fresh adversarial mathematical audit of v010

Audit date: 6 September 2026. This report is confined to the frozen specification, the frozen manuscript, the primary mathematical sources cited there, and fresh isolated tests. It did not consult handoffs, ledgers, previous referee reports, or research transcripts. The declared computational archive was only listed for possible primary-source files; its computational implementation and execution are the responsibility of the separate computation audit.

Frozen inputs:

- `problems/stretched-lr-coefficients/spec.json`, SHA-256 `2b9f91614a3e5aa0af887391442819935a5e45d8198edb086bfdca19f99111b0`.
- `problems/stretched-lr-coefficients/manuscript/v010.tex`, SHA-256 `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45`.

All manuscript line references below refer to that exact TeX file. This report does not authorize a harness transition, does not assert acceptance by two independent families, and does not assert Lean completion.

## Assessment

I found no substantive mathematical counterexample or unrepaired inference gap in the reductions or in the conditional finite-cover argument. All 19 numbered results are inventoried below. The two shortening bijections, the six representation symmetries, the full integer-lattice array–hive correspondence, the published Horn hypotheses, and the iterative second reduction withstand the checks described here.

This is a positive assessment of the mathematical implication **E + R + P implies the finite-box conclusion**. It is not an independent establishment of E, R, or P. In particular, the saved polynomial vectors at ranks six and seven must still be justified by the asserted exact Normaliz executions or by complete regeneration; a few LR values, checksums, and an audit of the stored vectors cannot by themselves establish P. The manuscript says this explicitly at lines 1066–1075, 1179–1185 and 1198–1207.

Two minor formal points should be cleaned up when convenient: explicitly type the complement width as an integer in Lemma 6, and restrict the rank in Theorem 7 to a positive integer, or separately define its empty rank-zero case. The exact Theorem 1.4 numbering in the inaccessible KTT09 full text was not independently verified; the operative, accessible CJM statement was verified and suffices mathematically. None of these is an identified counterexample to the finite-box conclusion.

## Statement fidelity and quantifiers

The statement at lines 28–55 and Theorem 19 at lines 1209–1226 matches the negative-resolution success criterion in the frozen specification. The outer partition remains λ; the inner partitions are μ and ν. Balance implies that bounding the outer size by 30 bounds the two inner sizes. Length counts positive parts, and trailing zeros are harmless. Coefficients are in the ordinary monomial basis in the original stretching variable. The theorem concerns every positive integer stretch of every original in-box triple, regardless of the sizes of the stretched partitions.

The all-empty input has polynomial 1. A nonempty balanced triple with zero base multiplicity has polynomial 0 by saturation and polynomial uniqueness. The manuscript correctly avoids equating the latter polynomial’s value at zero with the LR coefficient of the all-empty triple. The use of t = 0 in interpolation is restricted to positive-base residuals, where the hive is nonempty. No positivity claim for ranks at most four, no previous sweep through size 23, and no unproved coefficient-positivity conjecture is imported.

The theorem does not claim unrestricted KTT positivity. This restriction is explicit at lines 860–865. The frozen problem permits a computer-assisted proof of nonexistence in the box; consequently the direction of the proposed resolution is in scope.

## Inventory of all 19 results

| No. | Result; manuscript lines | Mathematical assessment | Dependencies and specific audit finding |
|---|---|---|---|
| 1 | Array description; 94–143 | Checked directly | Row counts determine a unique weakly increasing filling. The lattice prefix has its minimum after the row’s i+1 entries and before its i entries. The column endpoint inequality is equivalent to strictness because the removed inner cells constitute an allowed prefix. Triangular support follows by induction on the row. The deficit and row-length bounds follow by counting and telescoping. |
| 2 | Strengthened shortening; 145–184 | Checked directly | Only the column inequalities at the cut change. For thresholds at most k, the lower prefix is bounded by both tq_k and the lower row length. For thresholds at least k+1, support makes both prefixes whole rows. Both inequalities in (6) are needed. The reverse direction increases each changed slack by ta, so no positivity hypothesis is missing. |
| 3 | Empty-row deletion; 188–203 | Checked directly | The empty row separates skew cells in disjoint column ranges. Deleting it creates no comparison between overlapping columns, and keeps the reading word. Its inverse is insertion. The decrease in outer size is strict only when the deleted part is positive, as stated. |
| 4 | Initial-sum factorization; 205–227 | Checked directly | q_k = 0 exhausts all labels at most k above the cut. The lower labels can be shifted down by k. On concatenation the only cross-range lattice comparison is controlled by ν_k ≥ ν_{k+1}. Both factors are balanced; proper positive cuts give smaller positive outer sizes. |
| 5 | Full columns and scaling; 229–244 | Checked directly | At stretch t the column translation is by t cells. Division gives P(t) = Q(gt), with a positive coefficient multiplier g^i. A negative sign therefore survives division. |
| 6 | Rectangular complement; 248–277 | Checked directly, with minor implicit integer typing | The prefix dominance criterion for adjacent column sets is equivalent to row weak increase, including unequal column heights and empty columns. Complementation reverses this dominance and reversing column order restores it. The operation is involutive, and the weight of label i changes from e_i to M−e_i. Schur characters and complete reducibility identify the dual representation. Explicitly state M ∈ Z_{≥0}. |
| 7 | Six polynomial-preserving representatives; 279–339 | Checked directly, with minor rank-zero scope point | Tensor–Hom identifies the LR multiplicity with the determinant multiplicity in three factors. Permuting those factors gives three representatives. Dualizing and twisting gives K* = u+w−h and three more. The row bound and exchanged row bound establish all widths required to form partitions. Each operation commutes with uniform stretching. Explicitly state n ≥ 1. |
| 8 | Necessary conditions; 343–382 | Checked directly | Every forbidden configuration produces a strictly smaller in-box negative witness through a proved identity or factorization. The strengthened gap inequalities imply interlacing; at a zero outer gap ordinary containment suffices. A smaller six-symmetry representative stays in the box by balance and its length bound. Rearrangement of all six size comparisons gives (17) exactly. |
| 9 | Containing partition and deficit; 384–410 | Checked directly | κ is decreasing and nonnegative over the positive outer rows. At strict gaps its part is λ_{j+1}; at equalities it is λ_{j+1}−1. Its total is N−L−e. Subtracting the two inner sizes yields s; deficit zero and one have precisely the descriptions stated. |
| 10 | Array bounds; 426–476 | Checked directly | Summing lattice inequalities telescopes to the suffix bound. Iterating column inequalities gives the diagonal bound. Their sum is the displayed Weyl-type inequality; if its index is beyond n, the left side is zero. The later use with q = 1 is separately identified as an identity, so a b = 0 application is not smuggled in. |
| 11 | Rectangular shortening; 483–656 | Checked directly | The forced columns supply all q subtracted entries. Margins, support, and every exceptional lattice and column slack were checked. The two exceptional families have at least a slack. The inverse adds a at the same cells and restores every inequality. Stretching requires subtraction ta, which the proof expressly uses. Includes r = n, q = 1, zero multiplicity, and equality in the numerical bound. |
| 12 | Essential Horn factorization; 659–701, application 702–706 | Published input matched to primary statement | CJM Definition 1.2 and Theorem 1.3 use exactly the same τ convention, multiplicity-one subset condition, positive base coefficient, proper subset size and boundary equality after renaming their inner/outer variables. There is no required regularity or strictness of the other inequalities in that operative theorem. Homogeneity and positive stretching give the polynomial identity. At n = ℓ(λ), both proper selected outer parts have positive smaller size. |
| 13 | Second reduction at all stretches; 708–774 | Published unit input matched; iteration checked directly | CJM BKMS Theorem 2.6 gives the rectangle formulation; CJM FPSAC Theorem 3.1 gives the coefficient formulation. The paper’s indices and strict gaps match. At stage s<t all gaps remain at least t−s and the numerical excess is tΔ−s ≥ 1. A first noncontained target has coefficient zero; loss of containment persists, making all later comparisons zero. |
| 14 | Finite cover implication; 831–858, definitions 776–829 | Checked as a conditional theorem | A least normalized key exists in the finite box. Its first coordinate makes it a minimum-size witness and puts it in D by Theorem 8. A smaller endpoint or smaller factor contradicts minimality. Equal key means exactly the same normalized triple and is not an exclusion. Every survivor belongs to one residual set. No greedy-completeness or size-23 positivity premise is used. |
| 15 | Finite dependency E; 916–920 | Computational assertion, not discharged in this report | The literal recursion enumerates all bounded partitions once. The finite array definition makes the LR filter exact and terminating. κ is an admissible acceleration because it follows from the literal domain conditions. Equality of complete sets and base counts—not matching cardinalities alone—is the requisite computation. The stated 37,530 and 1,255,228 counts require the separate replay. |
| 16 | Finite dependency R; 958–986 | Computational assertion, not discharged in this report | The declared certificate format is sufficient in principle: source/target equality, each local premise, positive scale, final in-box key, exact Horn factors, and exactly-once source coverage. Stage subtractions and total residual arithmetic are internally consistent. Greedy discovery does not affect validity if every recorded path passes and every source is accounted for. |
| 17 | Literal array–hive correspondence; 1013–1046 | Checked directly | The forward cumulative map and inverse mixed difference have integer coefficients and are inverse on the balanced boundary space. All three rhombus slacks match the asserted array slacks. Missing lattice inequalities vanish; missing columns are outer-part gaps. Diagonal nonnegativity follows from ν_n and successive lattice inequalities. Thus the lattice really is the full Z^D, including lower-dimensional hives. |
| 18 | Finite dependency P; 1077–1090 | Computational assertion, not discharged in this report | Polynomiality identifies every true Ehrhart constituent from its infinite residue class. For positive-base hives, t = 0 contributes 1. A separately computed degree-bounded polynomial agreeing at D+1 arguments is determined. At ranks six and seven, a few LR values do not identify the polynomial; trust in complete exact Normaliz execution remains. Residual coverage, source binding and signs must all be checked. |
| 19 | Computed finite-box positivity; 1209–1226 | Correct consequence conditional on E, R and P | Its mathematical implication is Theorem 14. The sentence that exact computation establishes all three dependencies must be evaluated by the separate source/execution audit. This report independently verifies neither all residual Ehrhart computations nor the historical execution attribution. |

## Detailed checks of the sensitive steps

### Strengthened shortening

The first potential failure is an unexamined column comparison at threshold k or k+1. The split used in lines 175–181 is correct at both endpoints. At b = k, the relevant lower entries are among the labels at most k below the first k rows, so their count is at most tq_k. At b = k+1, the upper prefix uses labels at most k and is the entire upper row, while the lower prefix uses labels at most k+1 and is the entire lower row. Their difference with the shifted inner boundaries is exactly t(λ_k−λ_{k+1}−a).

There is no need to assume positive base multiplicity: an original feasible array gives a target feasible array, and a target feasible array gives an original array by increasing the only altered crossing slacks. Empty polytopes therefore correspond as well. The hypotheses also ensure that the modified parts are nonnegative and decreasing: the upper prefixes preserve their internal gaps, and the single changed boundary gap remains nonnegative.

The term b_k cannot simply be discarded. For λ=(3,2,1), μ=ν=(2,1), k=1 and a=1, the weaker gap-only subtraction produces ((2,2,1),(1,1),(2,1)). The original LR values at t=1,2,3 are 2,3,4, while the target values are 1,1,1. The manuscript’s actual condition forbids this move because q_1=b_1=1 and the allowed a is zero.

### Rectangular shortening

Write M=μ_{p+1}, N=ν_{q+1}. The forced-column argument genuinely produces a copies of label i in row p+i: the bottom-row prefix of labels at most q reaches column M+a, and every row p+1 through p+q contains a skew cell in each of the selected columns. Strictness of a column of q positive labels ending at most q forces its exact sequence 1 through q. This works even if there are additional cells above or below that block.

The lattice changes telescope along the diagonal of modified entries. For i<q, the entry lost in column i enters the earlier-row sum precisely when the entry lost in column i+1 enters the current-row sum. Only label q below the block loses a in its slack. Its available slack is bounded from below by λ_r−M−N using the suffix bound and the content cap.

For columns, the change at row p+1 is cancelled by the change to μ_p. In interior block rows the two affected prefixes change simultaneously. At row r+1 and thresholds at least q+1, the upper prefix alone loses a. The estimate at lines 618–627 is exact: summing the intermediate lattice inequalities gives the bound involving S_{r+1,q+1}−S_{r,b}; adding the upper-row suffix cancels the latter cap. This proves the needed a slack. The b=q+1 sum is empty but yields equality, as the manuscript says. For r=n there is no exceptional inequality.

The inverse is justified by algebraic change identities that do not assume feasibility. Adding at the same positions preserves triangular support because p+i≥i; it restores the original margins and only increases the two exceptional families. Uniform stretching uses ta, so the argument proves a polynomial identity rather than merely equality at t=1.

The tail-sum bound is essential. For λ=(3,2,1), μ=ν=(2,1), p=q=a=1, the three gap conditions alone would permit the target ((2,1,1),(1,1),(1,1)); its values 1,1,1 disagree with the original 2,3,4. The actual condition λ_2−1 ≥ μ_2+ν_2 fails and excludes it.

### Six symmetries

Let A=μ, B=ν and C=λ^{c,L}. The determinant multiplicity in A⊗B⊗C equals the original tensor multiplicity by the tensor–Hom identity and V_C ≅ det^L⊗V_λ*. Complete reducibility is available over C, so this is equality of actual multiplicities. Permutation of three tensor factors produces the first three displayed sizes without requiring conjugation of Young diagrams.

For any zero-last-part W, W* has first part W_1 and size nW_1−|W|. The sum of the twists introduced by dualizing A,B,C is u+w+L−h. Dualizing det^L then leaves exponent u+w−h. Its differences from u,w,L−h are w−h,u−h,u+w−L. The array row bound gives all three nonnegative quantities, with exchange used for h≤u. The resulting complement widths therefore produce ordinary partitions, not arbitrary rational highest weights.

The resulting outer sizes are N, nL−m, nL−v, n(u+w)−N, n(u−h)+v, and n(w−h)+m. Their comparison with N gives precisely the three groups of inequalities at lines 359–360. Since the operations are linear and their width choices scale with the boundary, they commute with stretching. Conjugation/stretching commutation is never assumed.

### Published reductions and the second-reduction boundary

The operative Horn result has the exact subset test and equality needed by the certificate description. In particular, the source of positivity for a factor does not have to be proved separately: the positive source coefficient and the factorization make both base factor counts positive. Proper subsets of a strictly positive outer partition have smaller positive sizes. Horn catalog completeness is unnecessary for sound exclusion, though the paper also reports a complete catalog reconstruction.

For the second reduction, the rectangle height is the paper’s chosen n and the rectangle width is λ_1. The source theorem’s third index is n−p−q, which is positive because the paper pads to at least p+q+1. Complementation turns its boundary condition into the paper’s numerical inequality and its third gap into the outer gap. The all-stretch proof then performs t unit steps; it does not infer stretching from an isolated unit equality.

The plus one is essential. λ=(3,1), μ=(1), ν=(2,1), p=q=1 satisfies the strict gap conditions and the weakened excess-zero condition. The source coefficient is 1, whereas the candidate target ((2),(),(1,1)) has coefficient 0. Both remain respectively 1 and 0 at t=2,3. The actual theorem rejects this move.

A valid hypothesis can yield a noncontained target when the source coefficient is already zero. For λ=(3,2,1,1), μ=(2), ν=(3,2), p=q=1, the actual hypotheses hold, and the target is ((2,1,1,1),(1),(2,2)). Its second inner partition is not contained in the outer one. The source and target coefficients are zero at t=1,2,3. The proof’s monotonicity argument at lines 762–770 is necessary for its stated zero-case scope and is valid.

### Array–hive integer lattice

The proof supplies more than equality of counts in a familiar unnamed hive convention. It specifies the boundary and the coordinate map. With F(b,j) as the cumulative row-and-label sum, setting h(a,b)=F(b,a+b) produces the μ, μ+ν and λ boundary sums in the indicated order. Extending F beyond its triangular range by taking min(b,j) forces entries above the array diagonal to vanish. Mixed differences recover all array entries, and summation recovers F and h.

The three displayed rhombus families correspond respectively to C_{s+2,b+1}, L_{s+1,b}, and x_{s+1,b+1}. The third family yields off-diagonal nonnegativity; it does not directly yield the diagonal entries. The separate argument x_{n,n}=ν_n and x_{r,r}≥x_{r+1,r+1} supplies exactly this missing point. No diagonal inequality has been lost. The omitted high-label lattice cases are zero, and high-threshold column cases are the fixed outer gaps.

Both maps have integer coefficients and integer boundary constants, and they are inverses. They therefore identify the full ambient integer-coordinate lattice of the free h variables with the affine integer array solutions. This addresses potential finite-index or rescaled-grading errors at the mathematical level. Positivity of row sums bounds the array coordinates; hence the hive is bounded. Homogeneity of the right-hand sides identifies the t-th boundary hive with tH for every t>0. Software must still implement these literal formulas and the same lattice.

### Minimum-key cover

The key includes the full normalized triple after size and outer length. Equal key therefore really means equal normalized triple; it does not merely mean equal size and length. This is sufficient to handle paths whose last triple has the same size but is smaller lexicographically. Every identity edge has either scale one or the positive integer scale of division, and composition multiplies the scales. The direction P_source(t)=P_target(gt) preserves a negative coefficient of any degree.

Larger intermediate outer sizes do not invalidate an identity, because the reduction theorems have no size-30 hypothesis. They cannot by themselves contradict minimality. The final target is expressly checked to return to the original box with smaller key; this is exactly what minimality needs. A loop with equal key is retained. For a Horn product, at least one factor has a negative coefficient, since products of polynomials with nonnegative coefficients have nonnegative coefficients.

The least witness belongs to the necessary domain, and the staged accounting must place every such source in either a valid exclusion or one of the two residual sets. A recorded “baseline” endpoint is useful only because its outer size is smaller; no independent theorem through size 23 is assumed. The argument does not depend on discovering all possible moves, reaching a globally canonical representative, or proving termination of an unrestricted greedy algorithm. It needs only the finite recorded paths and complete source coverage.

## Primary-source checks

- [Rassart, Corollary 4.2](https://pi.math.cornell.edu/~rassart/pub/LRstretch.pdf): checked polynomiality and the stated rank degree bound. The adjoining remark expressly separates polynomiality from coefficient positivity. The citation supports the manuscript’s use.
- [Knutson–Tao](https://arxiv.org/abs/math/9807160): checked the saturation input. Its contrapositive supplies the zero-polynomial case. Positive base hives also dilate directly to integral hives, so the positive-stretch direction is available without an additional positivity conjecture.
- [Knutson–Tao–Woodward, §6.1](https://arxiv.org/abs/math/0107011): checked that this section states and proves Fulton’s multiplicity-one stretching assertion, rather than merely restating its conjectural form.
- [Ikenmeyer, Theorem 1.1](https://arxiv.org/abs/1209.1521): checked the value-two stretching assertion. Its numbering matches.
- [Buch, Theorem 1 and Fulton’s appendix](https://sites.math.rutgers.edu/~asbuch/papers/sat.pdf): checked the standard integral hive interpretation. The paper’s own coordinate calculation is what fixes its literal orientation and lattice.
- [Milne, 17.14 and 20.35](https://www.jmilne.org/math/CourseNotes/RG.pdf): these establish reductivity of GL_n and complete reducibility in characteristic zero. The latter section lies in the characteristic-zero discussion. The application over C meets that condition.
- [CJM, Definition 1.2 and Theorems 1.3 and 3.1](https://dmtcs.episciences.org/3592/pdf): checked all hypotheses, outer/inner renaming, subset ordering, and unit target operation. The text supports both cited uses. The definition tests multiplicity exactly one, and the Horn theorem assumes a positive source. The second-reduction coefficient formulation includes the three strict gaps and the extra unit numerical margin. It has no added requirement that the target skew containment hold.
- [CJM, BKMS Theorem 2.6, author-uploaded primary text](https://www.researchgate.net/publication/228361141_A_BIJECTIVE_PROOF_OF_THE_SECOND_REDUCTION_FORMULA_FOR_LITTLEWOOD-RICHARDSON_COEFFICIENTS): checked the rectangle formulation and the translation used at lines 733–742. The paper’s DOI was reachable as a redirect but its target timed out during this audit; the authored primary text was readable.
- [Roth, Reduction Theorem (3.1.1)](https://arxiv.org/abs/1004.5133): checked the existence and nature of the cited general reduction and its identification of the type-A KTT application. As the manuscript says, this is supporting evidence, not a replacement for verifying the exact subset formulation.
- [KTT09 publisher record](https://www.sciencedirect.com/science/article/pii/S0097316508000939) and [author institution record](https://eprints.soton.ac.uk/66211/): bibliographic title, year, pages and DOI match. Full-text retrieval was blocked/restricted, so I did not independently verify the printed Theorem 1.4 numbering. This is an access limitation, not a found citation mismatch. The accessible operative CJM theorem supplies the mathematical assertion.
- The Epoch page is the external problem reference; statement fidelity in this fresh audit was assessed against the operator’s frozen specification, which is authoritative. The Normaliz manual and executable semantics remain within the separate computation audit. No legal licensing conclusion is made here.

The downloaded primary PDFs and their SHA-256 hashes are recorded in `sources.json`. The PDF text files are convenience extractions; their mathematical equations were cross-checked against readable primary-source renderings where extraction was ambiguous. No substantial unattributed prose copying was detected in the portions checked. A complete copyright/license decision belongs to the separate licensing audit.

## Fresh exact tests and their limits

`exact_boundary_audit.py` imports no proof implementation. It independently constructs all balanced contained ordered triples of outer size at most 12 and length at most 6. LR comparison uses lrcalc; for all such triples through outer size 8 it independently counts tableaux by assigning individual cells in reverse reading order and enforcing row, column and prefix conditions.

| Check | Exact scope/count | Outcome |
|---|---:|---|
| Balanced contained source triples | 29,859 | Complete for the stated small domain |
| Independent direct cell/tableau base counts | 1,776 | All matched lrcalc |
| Strengthened shortening parameter instances | 34,936 | 104,808 stretch equalities at t=1,2,3 passed |
| Rectangular shortening parameter instances | 19,222 | 57,666 stretch equalities passed |
| Rectangular cases with r=n | 9,556 | Included in those passing comparisons |
| Rectangular cases with q=1 | 11,461 | Included in those passing comparisons |
| Second reduction parameter instances | 10,315 | 30,945 stretch equalities passed |
| Second reductions with noncontained targets | 1,164 | Included; all zero as required |
| Six-representative instances | 64,188 | 192,564 stretch equalities passed |

`horn_boundary_audit.py` independently enumerates every proper subset triple at ranks 2 through 7, filters the balanced τ triples, and evaluates their LR coefficient. It reproduces the catalog counts 3, 12, 41, 142, 521, 2,042. On every positive contained source through outer size 10 and length 5, it checks every catalog entry satisfying the boundary equality. There are 4,374 positive sources and 47,987 such factorizations; all 143,961 comparisons at t=1,2,3 pass, and both outer factors have smaller positive size.

`symbolic_hive_audit.py` checks the coordinate inverse, margins, support, all literal rhombus identities, omitted inequalities, diagonal argument and rectangular slack changes by exact symbolic expansion over arbitrary balanced boundary variables and arbitrary free hive coordinates at each rank 1 through 7. It verifies 3,787 identities, including 3,248 rectangular slack-change identities. This is identity verification on the full relevant linear spaces at those ranks, not random numerical sampling. It does not independently prove the inequality implications; those were checked in the mathematical reasoning above.

The total number of tested stretching equalities across the four identity families and Horn products is 529,944. They are falsification tests on specified finite domains. They do not prove equality for every stretch and do not establish the manuscript’s full size-30 E, R, or P assertions. The all-stretch justification remains the checked mathematical proof and cited theorems.

The deliberately weakened-hypothesis examples are exact failures of different statements. They are recorded in `weakened_hypothesis_counterexamples.json` and `exact_boundary_results.json`. They show that the tested inequalities protect real boundaries; they are not counterexamples to v010.

## Outstanding issues and trust dependencies

1. **Minor formal typing, lines 248–252.** Require an integer rectangle width M. Without that implicit convention, a real M would generally fail to define a partition or a Schur polynomial. The proof’s use of M columns already presumes integrality. All applications use integer partition parts as widths.
2. **Minor rank-zero scope, lines 279–283.** Explicitly require n≥1, or define the all-empty n=0 convention. The current standing rank convention permits zero, whereas h=λ_n then refers to a part indexed zero. Every nonempty minimum-witness application has n≥1, so this does not affect the cover.
3. **Unverified citation locator, lines 681 and 1268–1271.** Direct KTT09 Theorem 1.4 numbering was not accessible. The exact operative CJM formulation was independently matched, so this is not an unsupported reduction hypothesis.
4. **E execution dependency, lines 916–925.** The paper’s literal finite set is well-defined, but the claimed complete enumerated sets and base counts were not replayed by this referee. No count-only acceptance is sufficient.
5. **R execution dependency, lines 927–989.** The certificate conditions are mathematically sufficient, but every actual edge, Horn factor, source index, endpoint and residual partition must be checked against the frozen artifacts. This report does not infer that coverage from the stated stage counts.
6. **P execution dependency, lines 1048–1098 and 1179–1207.** Exact Normaliz execution is trusted for 335,144 residuals as sole full-polynomial engine, while the paper reports 23,808 complete independent LattE reproductions. The later binary census cannot attest which executable ran at each historical call. Most historical raw Normaliz I/O is absent. These limitations are disclosed; they prevent treating the saved vectors and base checks as independent cone certificates or a formal proof of the engine.
7. **Source/lattice implementation dependency, lines 991–1011.** The paper’s literal mathematical lattice is correct. The code must actually construct it without implicit coordinate nonnegativity, a different sublattice, shifted origin, or grading rescale. This report checks the formulas, not the archived backend invocation.
8. **Arithmetic and runtime dependency.** lrcalc, Python integer/rational operations, LattE, Normaliz, the parser, source indexing, interpreter, compiler, libraries and ordinary execution correctness remain software trust assumptions to the extent used. Our own finite corroboration also trusts its execution and lrcalc, except for the independently counted small tableau cases.
9. **No formal closure implied.** There is no sorry-free Lean term, pinned axiom census, or statement-fidelity audit established by this report. The manuscript expressly claims a conventional computer-assisted result rather than proof-assistant verification.

There is no discovered substantive mathematical error to repair before applying Theorem 14 conditionally. Whether the complete computational evidence discharges its premises, and whether the distribution satisfies its licenses and the workflow’s final gates, must be decided from the separate audits. The appropriate mathematical conclusion of this fresh pass is that the reduction proofs and conditional cover survive adversarial scrutiny, with the specified minor formal clarifications and explicit computational trust dependencies.
