# Exhaustive proof and licensing audit

Credited author and project lead: **Maseeh Ghodsi**. Audit cutoff: 2026-09-06T14:12:06.328618+00:00.
Reviewed manuscript: v010; corrected publication: version 1.0.2.

## 1. Executive assessment

**No substantive mathematical error was found in the finite-box argument.**
The audit checked all 19 numbered results, repeated the complete finite audit,
independently inspected every actual reduction certificate, and freshly
recomputed all **358,952 complete residual polynomials**. All **2,745,084 exact
rational coefficients** matched. A separate portable validator rebuilt the
entire source catalog and read every saved raw record, returning COMPLETE.

Four publication corrections are recorded explicitly: integral complement
width, positive ambient rank, an overstatement about arbitrary malformed-input
rejection, and the author of one reference in the frozen specification. None
changes a coefficient, reduction formula, residual set, or finite-box conclusion.
The original frozen manuscript, specification and evidence remain unchanged;
the corrected public paper adds an identified errata/clarification page.

The conventional proof is complete **under its stated exact-software trust
assumptions**. This audit does not prove Normaliz's implementation correct,
complete the Lean development, guarantee the absence of every possible error,
or establish external acceptance. [Epoch's page](https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients)
still displayed **Unsolved** when checked on 6 September 2026. Its
[FAQ](https://epoch.ai/frontiermath/open-problems/about/faq) requires community
acceptance for a negative resolution; local computation is not that acceptance.

The licensing inventory found no concrete incompatibility in the supplied
aggregate. Maseeh Ghodsi is the credited author/project lead; substantial AI
assistance and prior mathematical/software authorship are disclosed. Standard
CC BY 4.0 and GPL-3.0-or-later grants apply only to rights actually held. They
do not guarantee exclusive scientific credit or ownership of mathematical facts.

The required progress metric is **100.0% of the conventional E/R/P obligations
under that trust model**, with a subjective evidence-credit sensitivity range
of **85.5–100.0%**; remaining **0.0%**, sensitivity **0.0–14.5%**. This is an
obligation-accounting model, not an error probability, a Lean score, an
acceptance score or a mathematical lower bound. Scoring confidence is medium.
The audit covered **21/21 normalized claims in its declared universe**, including
19 numbered results and two concrete prose/attribution assertions. That
coverage percentage is distinct from mathematical progress.

## 2. Scope, snapshot, and method

The starting checkpoint was `40fc43d59b9ad29715b41eaa5f54549336959b99`.
The working tree contained pre-existing unrelated edits and untracked research
artifacts; they were not adopted as proof evidence. The direct inputs were the
frozen v010 manuscript/specification, the actual v1.0.1 public ZIP, its complete
132-file source archive, and directly checked mathematical/license sources.
Previous attempts, obsolete manuscripts, the paused Lean campaign and unrelated
harness changes are outside this final paper audit. It is not a claim to have
read every assertion in the research history.

- Frozen specification SHA-256: `2b9f91614a3e5aa0af887391442819935a5e45d8198edb086bfdca19f99111b0`.
- v010 TeX SHA-256: `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45`.
- Frozen PDF SHA-256: `af943049949e274712dc362dbaa10469144f779ff4b4519f27e6ebadc7b18ff6`.
- Original evidence ZIP SHA-256: `299489ce594f54e3ff0278cb6927b40e03959e528cbe8c57d561466d8aa6cd44`.
- Top source manifest SHA-256: `f835cbc7ae315eb181139a812d24c11ee29bd747735311eb510bcd09b0aa56f3`.

The fresh mathematical and code referees received frozen inputs without
handoffs or previous opinions. A fresh Fable other-family full-scope session
also reviewed those bound inputs. The root supervisor adjudicated their
findings using their witnesses and primary sources. The licensing reviewer
was a supervisory audit, not another independent-family mathematical vote.

No frozen mathematical workflow artifact was changed. The user's explicit
publication instruction authorized a new release addendum, verification tools,
raw-evidence supplement and updated handoff/provenance. The review skill's
documentation-only convention did not prohibit those separately authorized
publication changes. No new campaign, acceptance transition, publication,
email or upload was performed. Harness state remains FROZEN, not DONE.

## 3. Independent problem ground truth

For every balanced partition triple $(\lambda,\mu,\nu)$ with each length at
most seven and $|\lambda|=|\mu|+|\nu|\leq30$, let
$P^\lambda_{\mu\nu}(t)=c^{t\lambda}_{t\mu,t\nu}$ for all positive integer $t$.
The target is nonnegativity of **every ordinary monomial coefficient** of this
polynomial. The original partitions satisfy the box bounds; their stretched
versions need not. This excludes a counterexample in the entire stated Epoch
box. It does not establish unrestricted KTT coefficient positivity.

The empty triple has polynomial 1. Zero base multiplicity gives the zero
polynomial by saturation and polynomial uniqueness; its extrapolated value
at zero is not confused with the all-empty LR coefficient. Base values one
and two are settled by the cited published stretching results. The positive
residual cases use nonempty bounded hives in their full integer coordinate
lattice. No unproved size-23 baseline, coefficient-positivity conjecture, or
bounded set of stretch evaluations is assumed to establish the whole result.

Primary inputs checked include [Rassart polynomiality](https://pi.math.cornell.edu/~rassart/pub/LRstretch.pdf),
[Knutson–Tao saturation](https://arxiv.org/abs/math/9807160),
[Knutson–Tao–Woodward §6.1](https://arxiv.org/abs/math/0107011),
[Ikenmeyer's value-two theorem](https://arxiv.org/abs/1209.1521),
[CJM's precise Horn/second-reduction statements](https://dmtcs.episciences.org/3592/pdf),
and [Milne's characteristic-zero representation theory](https://www.jmilne.org/math/CourseNotes/RG.pdf).
The detailed hypothesis and source-access audit is in `paper_audit/audit_report.md`.

## 4. Claim-audit summary

| Class | Count | Claims | Meaning |
|---|---:|---|---|
| V | 14 | C01–C13, C17 | Conventional deductions checked directly with the stated definitions and known inputs |
| VC | 5 | C14–C16, C18–C19 | Conditional implication or exact-software/finite-execution dependency explicitly retained |
| U | 0 | — | No unresolved deduction in the declared 21-claim universe |
| F | 2 | C20–C21 | Original general-parser wording and archival reference authorship; corrected publicly |
| I | 0 | — | No malformed item in the normalized claim universe |

The universe consists of the manuscript's 19 numbered results and two specific
assertions actually present in its surrounding proof/specification material.
Operational tests and licensing checks are inventoried separately below. The
absence of a U row is not a claim of formally proved software or universal
copyright clearance: those limits are explicit premises and scope exclusions.

## 5. Verified solid and conditional mathematical results

| Claim | Result | Validity | Novelty | Evidence and implication |
|---|---|---|---|---|
| C01 | Array description | V | N0 | Row fillings, lattice prefixes, column endpoints, triangular support, deficit and row-length bounds. |
| C02 | Strengthened shortening | V | N2 | The two threshold regimes cover every changed crossing inequality; inverse increases all changed slacks. |
| C03 | Empty-row deletion | V | N0 | Disjoint column ranges across the empty row; positive deletion gives strict outer-size decrease. |
| C04 | Initial-sum factorization | V | N0 | Exhausted upper label range; concatenation cross-label comparison uses the partition inequality. |
| C05 | Full columns and scaling | V | N0 | Translation by t at stretch t; positive g^i preserves signs. |
| C06 | Rectangular complement | V | N0 | Complement and reverse columns is a weight-reversing involution. Explicitly type M as integer. |
| C07 | Six polynomial-preserving representatives | V | N0 | Three permutations and three determinant-adjusted dual permutations; width bounds and sizes correct. Explicit n>=1 removes unused empty-rank ambiguity. |
| C08 | Necessary conditions | V | N2 | Every failed necessary condition gives smaller in-box negative witness. |
| C09 | Containing partition and deficit | V | N2 | Coordinatewise ceilings, exact sum and zero/one deficit descriptions. |
| C10 | Array bounds | V | N2 | Telescoping suffix, iterated diagonal and consequent Weyl bound. |
| C11 | Rectangular shortening | V | N2 | Forced entries, full slack changes and their bounds, unconditional algebraic inverse, uniform ta subtraction. |
| C12 | Essential Horn factorization | V | N0 | Exact subset orientation and hypotheses verified; no regularity/other-strictness assumption in operative theorem. |
| C13 | Second reduction at all stretches | V | N0 | Rectangle parameters match; t unit steps retain positive gaps and unit excess; lost containment remains lost. |
| C14 | Finite cover implication | VC | N0 | Least normalized key survives only into residual sets; endpoint must lie in box, no assumed baseline positivity. |
| C15 | Finite dependency E | VC | N3 | Complete finite-domain replay and independent strict journal/source inventory passed; exact domain and residual source bindings were checked. |
| C16 | Finite dependency R | VC | N3 | Every actual path/exclusion, target, accumulated scale and fixed/residual set was independently checked; all supplied edges meet strict validity requirements. |
| C17 | Literal array-hive correspondence | V | N0 | Literal boundaries, three slack families, omitted cases, diagonal nonnegativity and full integer-lattice inverse verified. |
| C18 | Finite dependency P | VC | N3 | Every complete source polynomial was freshly recomputed, then its literal hive input and full rational output vector were independently parsed and matched; Normaliz remains trusted. |
| C19 | Computed finite-box positivity | VC | N3 | C14 together with the checked E, R and P establishes the exact finite-box conclusion under the explicitly stated software assumptions. |


For C14 the named premises are E, R and P. For C15/C16/C18/C19 the conventional
computational conclusion retains correct exact LR/Normaliz software and the
observed source-bound execution. These are not presented as Lean theorems.
Known inputs and unresolved standalone novelty receive zero progress credit.
Only the exact new finite E/R/P corpus and its resulting box theorem receive
N3 credit within the documented literature-search scope.

The sensitive all-stretch arguments were checked as proofs, independently of
their bounded numerical tests: both directions of the shortening bijections,
all exceptional array slacks, the determinant dualities, all Horn hypotheses,
the iterative unit second reduction including zero/noncontained targets, and
the exact integer array–hive inverse. Paths may leave the finite box because
the identities are unrestricted in size; only the final smaller endpoint is
used for in-box minimality. Every actual endpoint and accumulated scale was
checked. The proof does not require greedy-path termination or a globally
canonical normal form.

## 6. Confirmed errors, corrections, and excluded inferences

| Location | Finding | Disposition and mathematical effect |
|---|---|---|
| Lemma 6, lines 248–252 | Complement width is implicitly integral | Add $M\in\mathbb{Z}_{\ge0}$, $M\ge\alpha_1$. Every actual application already satisfies it. |
| Theorem 7, lines 279–283 | Rank-zero notation would leave $\lambda_n$ undefined | Specify integer $n\ge1$ at least the three lengths; empty triple separately has P=1. |
| C20, lines 932–933 | Original parser removes internal zeros and defaults an unknown inner selector to nu | Replace blanket rejection claim with strict certificate-validity requirements plus the new exhaustive check of every actual raw edge. No actual invalid edge was found. |
| C21, spec.json:83 | arXiv:2211.06810 attributed to R. Wong | Correct to Warut Thawinrak in an archival erratum. Current v010 bibliography was already free of this error. |

The explicit witness $Q(t)=P(t)+\binom{t}{4}$ can survive the original
sparse-value checker after its redundant fields are recomputed. It changes the
t=4 value from 25,100 to 25,101 for small:29034 and from 1,068,801 to 1,068,802
for large:989721; independent fresh t=4 LR counts reject it. This is a real
limitation of sparse validation, not an actual changed polynomial in the frozen
archive. The fixed manifest rejects changed archived bytes, and the new full
raw computation/portable comparison checks every coefficient directly.

An additional historical `degree12_full_latte.json` record refers to source
files absent from the 132-file ZIP. It is not credited here as a separately
inspectable extra full LattE proof. The corresponding Normaliz source-bound
core polynomial is present and included in the full new computation. Likewise,
the original 23,808 LattE comparisons are not described as a second complete
358,952-case run. No unrestricted conjecture, completed Lean proof, sole legal
credit, guaranteed error-freedom or external acceptance is inferred.

## 7. Prior art and novelty review

| Result family | Closest documented work | Difference and credit |
|---|---|---|
| Polynomiality, saturation, low base values | Rassart; Knutson–Tao; Knutson–Tao–Woodward; Ikenmeyer | Published dependencies, N0, zero novelty credit |
| Rectangular complements, determinant translations, six symmetries | Briand–Orellana–Rosas, *Rectangular Symmetries for Coefficients of Symmetric Functions*, 2014/2015 | Same general symmetry mechanism; N0, not a new discovery |
| Horn and second reduction | CJM and cited KTT/Roth results | Exact operative hypotheses checked; published inputs, N0 |
| Strengthened/local rectangular shortening and necessary-domain formulas | Targeted searches and manuscript citations | Standalone novelty not conclusively determined; N2, zero novelty credit |
| Exact seven-row/size-thirty finite E/R/P cover and core | Epoch target and 13 documented targeted queries | No substantive full-box match found; N3 only within this search scope |

[Briand–Orellana–Rosas](https://arxiv.org/pdf/1410.8017) explicitly document the
rectangular/determinant/S3 symmetry family. The 2026
[Ferudun preprint](https://arxiv.org/html/2607.22301v1) states positivity through
length four without a size cutoff and selected higher-rank coefficient results;
it does not supply this full length-seven/size-thirty theorem. It is a prior-art
comparison, not an input used to justify v010, and its whole proof was not
independently audited here. [Thawinrak's official arXiv record](https://arxiv.org/abs/2211.06810)
confirms the corrected attribution. The full search log lists exact queries,
dates, URLs, negative results and one discarded wrong-identifier lookup.
N3 is a conservative search-scoped classification, not a priority certificate.

## 8. Facts and questions after the audit

Established independent facts are the cited polynomiality, saturation, low-c
stretching and representation/reduction results. The six-symmetry algebra is
an online-documented known consequence. The credited new material is the
specific complete finite enumeration/reduction/polynomial combination, yielding
the stated finite-box exclusion under the declared computation assumptions.

The complete original necessary domain has **1,292,758** rows: **37,530** in
the small band and **1,255,228** at sizes 24–30. The physical large-domain file
also contains 16,153 size-23 rows; those are not double-counted in the latter
proof band. The residual core is **12,415 small + 346,537 large = 358,952**.
The whole journal inventory checks **522,245 computed records**, including
source/degree/value consistency and the unique resolution of the historical
hard-case engine error.

Open obligations outside this conventional target remain a sorry-free full
Lean theorem with statement fidelity and axiom census, formal verification or
independent certificates for the exact engines, any second full-engine corpus
comparison, and external expert/community acceptance. Unrestricted KTT
positivity remains outside the claimed result.

## 9. Percentage derivation

| Obligation | Weight | Lower | Point | Upper | Point contribution | Credited claims |
|---|---:|---:|---:|---:|---:|---|
| E: Complete necessary finite domain and base-count coverage | 25.0 | 0.90 | 1.00 | 1.00 | 25.0% | C15 |
| R: Strictly valid reductions and exhaustive residual coverage | 30.0 | 0.90 | 1.00 | 1.00 | 30.0% | C16 |
| P: Entire source-bound core polynomial vectors and finite-box consequence | 45.0 | 0.80 | 1.00 | 1.00 | 45.0% | C18, C19 |


For weights $w_i$ and attainment $a_i$, the reported model is
$100\sum_i w_i a_i/\sum_i w_i$, with normalized weight total 100.
Thus the point calculation is $25+30+45=100.0$; the conservative sensitivity
calculation is $25(0.9)+30(0.9)+45(0.8)=85.5$. Remaining is the complement:
0.0 at the point, and 0.0–14.5 across those sensitivity choices.

P receives the largest weight because a complete whole-polynomial computation
was the main unclosed empirical trust step; R carries the coverage and sound
descent burden; E carries finite universality. These weights are judgmental.
N0/N2 lemmas receive no separate attainment, and C19 is not counted again in
addition to its E/R/P dependencies. The range is not a probability of correctness
or a bound over all possible software failures; a serious undiscovered common
failure can invalidate the claimed conclusion. Changing to a Lean-verified or
externally accepted goal would require a different obligation set and score.

## 10. Exhaustive checks, licensing findings, and residual risks

| Check | Scope | Result |
|---|---|---|
| Actual original public ZIP replay | All seven finite-audit stages, all 358,952 core records | PASS; no reliance on an older receipt |
| Mathematical reading | All 19 numbered results and their published hypotheses | No substantive error found; two explicit typing conventions added |
| Bounded identity falsification | 529,944 exact stretching equalities | All pass; these tests support, but do not replace, all-stretch proofs |
| Independent direct tableau controls | 1,776 paper-audit counts and 16,461 separate code-audit counts | All matched within their separately stated domains; counts are not claimed disjoint |
| Symbolic algebra | 3,787 identities through ranks 1–7 | All pass, including 3,248 rectangular slack changes |
| Strict reduction paths | 1,255,228 first-path and 559,665 later-path source records | All actual raw partitions, parameters, targets, scales and endpoints valid |
| Horn exclusions | 200,638 large + 17,883 small; 437,042 fresh factor LR calls | All pass; subset catalogs rebuilt independently |
| Low-c controls | 32,918 t=2/t=3 checks | All pass in the bounded control universe |
| Actual Normaliz controls | Negative-coordinate interval, period-two interval and point, ambient-lattice segment, empty polytope, and Reeve negative-coefficient example | Expected positive/negative outcomes observed |
| Whole new computation | 358,952 source-bound full polynomials; 2,745,084 rational coefficients | COMPLETE; all matched, raw inputs/outputs retained |
| Independent portable raw read | All 358,952 source rows rebuilt; all raw batches read | COMPLETE; no arithmetic engine executed by validator |
| Portable validator hostile tests | 40 tests including forged completion, modified catalog and changed prior batch | All pass within the bounded adversarial suite |
| Original public licensing inventory | 163 file instances: 31 outer + 132 inner; 29 Python sources | No concrete license conflict or missing distributed project source found |
| Standard license texts | GNU GPL v3 and CC BY 4.0 | Byte-identical to official source texts |

The paper and eligible documentation/data rights use
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en); original
software uses [GPL version 3 or later](https://www.gnu.org/licenses/gpl-3.0.html).
The grants do not relicense dependency software, published mathematics or
third-party material. No installed packages or dependency binaries are bundled.
The public notices identify Epoch-derived statement material, the modifications
to its formal conventions, PDF font families, and carrying applicable notices
when redistributing subsets. AI contribution is described without falsely
claiming the human personally derived or checked every step.

Licensing confidence is high for the exact grant texts and internal scope
consistency, conditional for underlying title/provenance. The audit did not
adjudicate account/employment assignments, jurisdiction-specific AI copyright,
unmarked copying outside its inspected sources, or court enforceability.
Licenses cannot own a mathematical fact or force scientific attribution beyond
applicable legal terms. Citation and priority are separate scholarly matters.

| Severity/type | Location | Residual issue | Practical consequence |
|---|---|---|---|
| Material trust assumption | E/P exact computation | Normaliz/lrcalc implementations remain trusted | Full raw reproduction strengthens execution evidence; it is not a proof of the engines |
| Corrected minor error | Parser prose and archival author | Concrete discrepancies described above | Publish the addendum with the untouched historical bytes |
| Source-access limitation | KTT09 printed Theorem 1.4 | Direct full text was restricted | Exact operative CJM theorem was read and suffices; later authored citation corroborates locator |
| Supplementary archival limitation | Extra degree-12 LattE record | Referenced source files absent | No additional completeness credit from that record |
| Portability limit | Original frozen seven-stage program | Native Windows path behavior differs | New standard-library unpack/raw-validation route avoids executing that code; original mathematical replay documented for macOS/Linux |
| Formalization incomplete | Full Lean box theorem | `sorry` remains in Complete.lean | No DONE, full Lean claim or axiom-census certification |
| Acceptance/credit unresolved | Publication beyond local workspace | No external adjudication or public priority timestamp | User publication and community assessment remain separate |

## 11. Manageable next steps — documentation only

| Priority | Target | Method and completion test | Expected information gain |
|---|---|---|---|
| 1 | External evaluation | Publish the corrected paper, original evidence and fresh raw supplement; obtain expert scrutiny of E/R/P and the software trust model | Determines community acceptance, not just internal consistency |
| 2 | Full formal statement | Finish the box theorem in Lean with no sorry/custom assumed conclusion, then run statement-fidelity and axiom gates | Removes the remaining formalization gap |
| 3 | Independent exact computation | Recompute the remaining Normaliz-only cases with a distinct implementation or independently checkable cone certificates | Reduces shared-engine failure risk |
| 4 | Bibliographic precision | Obtain authorized KTT09 full text and inspect the printed locator | Closes a minor direct-access limitation without changing the operative theorem |

These proposed next steps were not executed as part of this final audit. The
authorized local audit and publication corrections described elsewhere were
executed; no mathematical campaign or external publication was started.

## 12. Execution history, limitations, and confidence

The initial draft raw-resume checker admitted a deliberately rehashed wrong
input/output pair. It was corrected before the complete run; its failed witness
is preserved. A later real Normaliz format produced `10 (maximal)` rather than
`10` for full-dimensional rank-six hives. The run stopped visibly, with matching
polynomial coefficients; the parser was corrected to accept that exact suffix
only when degree equals ambient dimension. All **15,872** already completed
fresh cases were semantically revalidated before migration. Earlier code,
failure receipts and migration provenance remain distinct. No failure was
silently converted into a successful polynomial result.

The final producing wrapper is pinned to
`9e33a4732f075ea6eab2f1c27378cd11c6c37d0cb88774b968d8669a82073662`;
the portable validator is pinned to
`13706acbdfa99a3bd20c6f2c857a2a410cbe0d3be477a8b007e624ad60f7f0d9`.
The portable implementation independently constructs the literal hive input
and parses the full output using rational arithmetic. It reuses the exact
pinned pure source-catalog builder, and does not claim a wholly independent
implementation of every enumeration function. It never executes Normaliz or
opens recorded runtime binaries. Every batch is read and hash-rechecked.

The new Fable full-scope report returned **MINOR**, with **28/28 requested
checks** and no protocol errors, at a logged cost of **USD 17.607496**. Its
appendix activity included one complete finite replay and six fresh selected
whole-polynomial regenerations. Fourteen later requested polynomial checks
used cached results; 28/28 does not mean 28 fresh regenerations. Some numeric
theorem locators in that report are mistaken; the supervisor maps them by
exact title and frozen source. Primary-source checks resolve its access-related
questions. The original report remains unchanged.

The earlier frozen two-family acceptance was MINOR/FLAWLESS with 24 checks;
this new audit does not rewrite that history or create another harness state
transition. All such referees are AI systems. Correlated reasoning errors,
ordinary programming errors, host/runtime failures and incomplete literature
coverage remain possible. Confidence is high in the observed exact matches and
specific checked deductions, medium in the broader novelty/progress assessment.

## 13. Conclusion

The declared universe contains **19 checked mathematical results** (14 V and
5 explicitly conditional VC), **four N3 results within the search scope**, and
**two corrected prose/attribution errors**. The conventional E/R/P obligation
model is 100.0% complete, sensitivity 85.5–100.0%, remaining 0.0% with sensitivity
0.0–14.5%. The central remaining barrier to an unconditional verification claim
is the exact-software trust base and unfinished Lean development; external
acceptance and discovery priority also remain separate from this audit.

## Appendix A. Complete normalized claim ledger

The statements below reproduce the exact numbered environments from frozen
v010. Their notation and referenced hypotheses are defined by the indicated
frozen manuscript sections and the dependencies in each record. Read C06/C07
with the explicit publication conventions above. The machine-readable ledger
includes every required source, premise, method, evidence, novelty and credit
field, including both false assertions.

### C01: Array description

Source: `manuscript/v010.tex:94`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: LR tableau rule.

```tex
\begin{lemma}[Array description]\label{lem:arrays}
Suppose \(\mu\subseteq\lambda\) and all partitions have length at most \(n\). At stretch \(t\ge1\), LR tableaux correspond to nonnegative integer arrays \(x_{j,i}\), \(1\le j,i\le n\), satisfying
\begin{align}
\sum_i x_{j,i}&=t(\lambda_j-\mu_j),
&
\sum_j x_{j,i}&=t\nu_i,                                      \label{eq:margins}\\
x_{j,i}&=0\quad(i>j),                                        \label{eq:support}\\
\sum_{h<j}x_{h,i}-\sum_{h\le j}x_{h,i+1}&\ge0
\quad(1\le i<n),                                            \label{eq:lattice}\\
t(\mu_{j-1}-\mu_j)+\sum_{i<b}x_{j-1,i}
-\sum_{i\le b}x_{j,i}&\ge0
\quad(2\le j\le n,\ 1\le b\le n).                            \label{eq:columns}
\end{align}
Define
\[
q_k=\sum_{j\le k}(\mu_j+\nu_j-\lambda_j).
\]
The number of labels at most \(k\) below the first \(k\) rows is \(tq_k\). Existence of a tableau therefore implies \(q_k\ge0\). It also implies
\[
\lambda_j-\mu_j\le\nu_1.
                                                               \tag{5}
\]
\end{lemma}
```

Verification: Row fillings, lattice prefixes, column endpoints, triangular support, deficit and row-length bounds. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C02: Strengthened shortening

Source: `manuscript/v010.tex:145`. Validity **V**; novelty **N2**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, polynomial uniqueness.

```tex
\begin{theorem}[Strengthened shortening]\label{thm:shortening}
Let \(\mu\subseteq\lambda\), with all partitions of length at most \(n\). Fix \(1\le k<n\), suppose \(q_k\ge0\), and put
\[
r_{k+1}=\lambda_{k+1}-\mu_{k+1},\qquad
b_k=\min(q_k,r_{k+1}).
\]
If an integer \(a\ge0\) satisfies
\[
a\le\lambda_k-\lambda_{k+1},\qquad
a\le\mu_k-\mu_{k+1}-b_k,
                                                               \tag{6}
\]
define
\[
\lambda^-_j=\lambda_j-a\,1_{\{j\le k\}},\qquad
\mu^-_j=\mu_j-a\,1_{\{j\le k\}}.
\]
These are partitions after zero parts are dropped, and
\[
P^\lambda_{\mu\nu}=P^{\lambda^-}_{\mu^-,\nu}.
                                                               \tag{7}
\]
The analogous exchanged-inner identity holds.
\end{theorem}
```

Verification: The two threshold regimes cover every changed crossing inequality; inverse increases all changed slacks. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standalone novelty unresolved; no novelty or progress credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C03: Empty-row deletion

Source: `manuscript/v010.tex:188`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: LR tableau rule, polynomial uniqueness.

```tex
\begin{lemma}[Empty-row deletion]\label{lem:emptyrow}
If \(\mu\subseteq\lambda\) and \(\lambda_j=\mu_j\), deleting part \(j\) from both gives
\[
P^\lambda_{\mu\nu}
=
P^{\widehat\lambda}_{\widehat\mu,\nu}.
                                                               \tag{8}
\]
If \(j\le\ell(\lambda)\), the outer size decreases by \(\lambda_j>0\).
\end{lemma}
```

Verification: Disjoint column ranges across the empty row; positive deletion gives strict outer-size decrease. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C04: Initial-sum factorization

Source: `manuscript/v010.tex:205`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, polynomial uniqueness.

```tex
\begin{theorem}[Initial-sum factorization]\label{thm:factor}
Suppose explicitly that $|\lambda|=|\mu|+|\nu|$,
$\mu\subseteq\lambda$, and $1\le k<n$ for a rank $n$, with $q_k=0$.
Splitting all three partitions after part $k$ gives
\[
P^\lambda_{\mu\nu}
=
P^{\lambda_{\le k}}_{\mu_{\le k},\nu_{\le k}}\,
P^{\lambda_{>k}}_{\mu_{>k},\nu_{>k}}.
                                                               \tag{9}
\]
Both triples are balanced. If \(1\le k<\ell(\lambda)\), both outer sizes are strictly smaller.
\end{theorem}
```

Verification: Exhausted upper label range; concatenation cross-label comparison uses the partition inequality. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C05: Full columns and scaling

Source: `manuscript/v010.tex:229`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: LR tableau rule, polynomial uniqueness.

```tex
\begin{lemma}[Full columns and scaling]\label{lem:basic}
If $\ell(\lambda),\ell(\mu),\ell(\nu)\le n$,
$\mu\subseteq\lambda$, and $\lambda_n,\mu_n\ge1$, subtracting $1$
from all $n$ parts of $\lambda$ and $\mu$ preserves $P$.
The exchanged-inner version holds as well. If all parts are divisible by \(g\ge1\), and \(Q\) is the divided triple's polynomial, then
\[
P(t)=Q(gt),\qquad [t^i]P=g^i[t^i]Q.
                                                               \tag{10}
\]
\end{lemma}
```

Verification: Translation by t at stretch t; positive g^i preserves signs. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C06: Rectangular complement

Source: `manuscript/v010.tex:248`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: Schur character rule, complete reducibility.

```tex
\begin{lemma}[Rectangular complement]\label{lem:complement}
For \(\ell(\alpha)\le n\) and \(M\ge\alpha_1\), put
\[
\alpha^{c,M}=(M-\alpha_n,\ldots,M-\alpha_1).
\]
Then
\[
s_{\alpha^{c,M}}(x_1,\ldots,x_n)
=(x_1\cdots x_n)^M s_\alpha(x_1^{-1},\ldots,x_n^{-1}),
                                                               \tag{11}
\]
and consequently
\[
V_\alpha^*\cong\det^{-M}\otimes V_{\alpha^{c,M}}.
                                                               \tag{12}
\]
\end{lemma}
```

Verification: Complement and reverse columns is a weight-reversing involution. Explicitly type M as integer. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C07: Six polynomial-preserving representatives

Source: `manuscript/v010.tex:279`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, 6, tensor-Hom, complete reducibility.

```tex
\begin{theorem}[Six polynomial-preserving representatives]\label{thm:six}
Suppose \(c^\lambda_{\mu\nu}>0\), pad to \(n\), and assume \(\mu_n=\nu_n=0\). Write
\[
N=|\lambda|,\ m=|\mu|,\ v=|\nu|,\quad
L=\lambda_1,\ h=\lambda_n,\ u=\mu_1,\ w=\nu_1.
\]
Six balanced partition triples of length at most \(n\) have polynomial \(P^\lambda_{\mu\nu}\) and outer sizes
\[
N,\quad nL-m,\quad nL-v,\quad n(u+w)-N,\quad
n(u-h)+v,\quad n(w-h)+m.
                                                               \tag{13}
\]
\end{theorem}
```

Verification: Three permutations and three determinant-adjusted dual permutations; width bounds and sizes correct. Explicit n>=1 removes unused empty-rank ambiguity. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C08: Necessary conditions

Source: `manuscript/v010.tex:343`. Validity **V**; novelty **N2**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, 2, 3, 4, 5, 7, saturation, finite minimality.

```tex
\begin{theorem}[Necessary conditions]\label{thm:domain}
Assume \(\mathcal B_B\), and choose a counterexample of minimum outer size \(N\), if one exists. Put \(n=\ell(\lambda)\). Then:
\begin{enumerate}
\item \(B<N\le30\), the base multiplicity is positive, and the gcd of all positive parts is one.
\item \(\mu_n=\nu_n=0\), and \(q_k>0\) for \(1\le k<n\).
\item \(\lambda_j>\mu_j,\nu_j\) for every \(j\le n\).
\item \(\mu_k,\nu_k\le\lambda_{k+1}\) for \(k<n\).
\item For every $1\le k<n$ with $\lambda_k>\lambda_{k+1}$,
\[
\begin{split}
\mu_k-\mu_{k+1}&\le\min(q_k,\lambda_{k+1}-\mu_{k+1}),\\
\nu_k-\nu_{k+1}&\le\min(q_k,\lambda_{k+1}-\nu_{k+1}).
\end{split}                                                    \tag{16}
\]
\item All six sizes in (13) are at least \(N\), equivalently
\[
\max(m,v)\le nL-N,\quad 2N\le n(u+w),\quad
m\le n(u-h),\quad v\le n(w-h).
                                                               \tag{17}
\]
\end{enumerate}
\end{theorem}
```

Verification: Every failed necessary condition gives smaller in-box negative witness. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standalone novelty unresolved; no novelty or progress credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C09: Containing partition and deficit

Source: `manuscript/v010.tex:384`. Validity **V**; novelty **N2**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 8.

```tex
\begin{corollary}[The containing partition and deficit]\label{cor:kappa}
Under Theorem~\ref{thm:domain}, put \(\lambda_{n+1}=0\) and
\[
\kappa_j=\min(\lambda_j-1,\lambda_{j+1}),\qquad
e=\#\{j<n:\lambda_j=\lambda_{j+1}\}.
\]
Then \(\kappa\) is a partition with last part zero,
\[
\mu,\nu\subseteq\kappa,\qquad |\kappa|=N-L-e,
                                                               \tag{18}
\]
and
\[
s=N-2(L+e)\ge0,\qquad
(|\kappa|-|\mu|)+(|\kappa|-|\nu|)=s.
                                                               \tag{19}
\]
If \(s=0\), necessarily \(\mu=\nu=\kappa\). If \(s=1\), up to exchange, one inner partition is \(\kappa\) and the other is obtained by removing one removable corner.
\end{corollary}
```

Verification: Coordinatewise ceilings, exact sum and zero/one deficit descriptions. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standalone novelty unresolved; no novelty or progress credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C10: Array bounds

Source: `manuscript/v010.tex:426`. Validity **V**; novelty **N2**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1.

```tex
\begin{lemma}\label{rect:lem:bounds}
For an array in Lemma~\ref{lem:arrays}, put
\[
R_j(b)=\sum_{i=b}^{n}x_{j,i}.
\]
Then
\begin{equation}\label{rect:eq:suffix}
R_j(b)\le S_{j,b}\le\nu_b.
\end{equation}
Whenever $j>b$,
\begin{equation}\label{rect:eq:diagonal}
y_{j,b}\le\mu_{j-b}.
\end{equation}
Consequently, for $p,q\ge1$,
\begin{equation}\label{rect:eq:weyl}
\lambda_{p+q+1}\le\mu_{p+1}+\nu_{q+1},
\end{equation}
where a part beyond the chosen length is zero.
\end{lemma}
```

Verification: Telescoping suffix, iterated diagonal and consequent Weyl bound. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standalone novelty unresolved; no novelty or progress credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C11: Rectangular shortening

Source: `manuscript/v010.tex:483`. Validity **V**; novelty **N2**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, 10, polynomial uniqueness.

```tex
\begin{theorem}\label{rect:thm:rectangle}
Suppose $\lambda,\mu,\nu$ are balanced partitions with
$\mu,\nu\subseteq\lambda$. Let $p,q\ge1$, put $r=p+q$,
and let $a\ge1$ be an integer satisfying
\begin{equation}\label{rect:eq:hypotheses}
\mu_p-a\ge\mu_{p+1},\qquad
\nu_q-a\ge\nu_{q+1},\qquad
\lambda_r-a\ge
\max\{\lambda_{r+1},\mu_{p+1}+\nu_{q+1}\}.
\end{equation}
Define
\[
\widehat\lambda=\lambda-a(1^r),\qquad
\widehat\mu=\mu-a(1^p),\qquad
\widehat\nu=\nu-a(1^q).
\]
These are balanced partitions, and
\begin{equation}\label{rect:eq:identity}
P^\lambda_{\mu\nu}
 =
P^{\widehat\lambda}_{\widehat\mu\,\widehat\nu}.
\end{equation}
\end{theorem}
```

Verification: Forced entries, full slack changes and their bounds, unconditional algebraic inverse, uniform ta subtraction. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standalone novelty unresolved; no novelty or progress credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C12: Essential Horn factorization

Source: `manuscript/v010.tex:659`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: CJM Definition 1.2/Theorem 1.3, saturation, polynomial uniqueness.

```tex
\begin{theorem}[Essential Horn factorization]\label{thm:horn}
Let $n\ge2$, $|\lambda|=|\mu|+|\nu|$,
$\max(\ell(\lambda),\ell(\mu),\ell(\nu))\le n$, and
$c^\lambda_{\mu\nu}>0$.
For $1\le r<n$ and $r$-subsets $I,J,K$ of $[n]=\{1,\ldots,n\}$,
write $I=\{i_1<\cdots<i_r\}$ and
$\tau(I)=(i_r-r,\ldots,i_1-1)$, dropping zeros; define $\tau(J)$ and
$\tau(K)$ in the same way. Suppose
\[
 c^{\tau(K)}_{\tau(I),\tau(J)}=1,\qquad
 \sum_{k\in K}\lambda_k=\sum_{i\in I}\mu_i+\sum_{j\in J}\nu_j.
\]
For a subset, parts are selected in increasing index order; complements
are taken in $[n]$. Then
\[
 P^\lambda_{\mu\nu}
 =P^{\lambda_K}_{\mu_I,\nu_J}
  P^{\lambda_{K^c}}_{\mu_{I^c},\nu_{J^c}}.
\]
Both factors are balanced.
\end{theorem}
```

Verification: Exact subset orientation and hypotheses verified; no regularity/other-strictness assumption in operative theorem. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C13: Second reduction at all stretches

Source: `manuscript/v010.tex:708`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: CJM BKMS Theorem 2.6, CJM FPSAC Theorem 3.1, polynomial uniqueness.

```tex
\begin{theorem}[Second reduction at all stretches]\label{thm:second}
Let $\lambda,\mu,\nu$ be balanced partitions with
$\mu,\nu\subseteq\lambda$. Let $p,q\ge1$, set $r=p+q$, and choose
an integer $n\ge\max\{\ell(\lambda),\ell(\mu),\ell(\nu),r+1\}$.
Assume
\[
 \mu_p>\mu_{p+1},\qquad \nu_q>\nu_{q+1},\qquad
 \lambda_r>\lambda_{r+1},\qquad
 \mu_p+\nu_q\ge\lambda_1+\lambda_{r+1}+1.
\]
Then $\lambda^- =\lambda-(1^r)$,
$\mu^- =\mu-(1^p)$ and $\nu^- =\nu-(1^q)$ are balanced partitions,
and
\[
 \forall t\ge1,\quad
 c^{t\lambda}_{t\mu,t\nu}=c^{t\lambda^-}_{t\mu^-,t\nu^-},
 \qquad P^\lambda_{\mu\nu}=P^{\lambda^-}_{\mu^-,\nu^-}.
\]
Here $t$ is an integer. Padding to $n$ changes no coefficient.
\end{theorem}
```

Verification: Rectangle parameters match; t unit steps retain positive gaps and unit excess; lost containment remains lost. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C14: Finite cover implication

Source: `manuscript/v010.tex:831`. Validity **VC**; novelty **N0**.

Premises/scope: Explicit finite obligations E, R and P in the manuscript. Dependencies: 8, 11, 12, 13, E, R, P, finite minimality.

```tex
\begin{theorem}[Finite cover implication]\label{thm:globalcover}
Suppose the two enumerations are complete, every certificate just
specified is valid, and every polynomial attached to
$\mathcal C_{\rm small}\cup\mathcal C_{\rm large}$ has nonnegative
monomial coefficients. Then every stretched Littlewood--Richardson
polynomial in the frozen box has nonnegative monomial coefficients.
\end{theorem}
```

Verification: Least normalized key survives only into residual sets; endpoint must lie in box, no assumed baseline positivity. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High in the checked deduction; conditional on the named software/finite-execution premises.

### C15: Finite dependency E

Source: `manuscript/v010.tex:916`. Validity **VC**; novelty **N3**.

Premises/scope: Correct exact LR/Normaliz software and source-bound observed finite execution, as applicable. Dependencies: 1, 8, 9, complete domain enumeration, exact base LR engine.

```tex
\begin{proposition}[Finite dependency E]\label{comp:E}
The supplied small and large domain lists have no duplicate normalized
triple and equal $\mathcal D_{\rm small}$ and $\mathcal D_{\rm large}$,
respectively. Their cardinalities are $37,530$ and $1,255,228$.
\end{proposition}
```

Verification: Complete finite-domain replay and independent strict journal/source inventory passed; exact domain and residual source bindings were checked. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`, `replay/verification.json`, `computational_audit/corpus_inventory.json`, `computational_audit/horn_and_final_cover.json`.

Prior art: Complete finite-box E/R/P corpus and resulting theorem: no substantive match found in the documented search. Progress credit: Supports the E/R/P obligations; the same conclusion is not counted twice. Confidence: High in the checked deduction; conditional on the named software/finite-execution premises.

### C16: Finite dependency R

Source: `manuscript/v010.tex:958`. Validity **VC**; novelty **N3**.

Premises/scope: Correct exact LR/Normaliz software and source-bound observed finite execution, as applicable. Dependencies: 2, 3, 4, 5, 7, 11, 12, 13, 15, path checker, source coverage.

```tex
\begin{proposition}[Finite dependency R]\label{comp:R}
Every source index in E occurs exactly once in the appropriate coverage
stage; the stages define the residual sets as in
Theorem~\ref{thm:globalcover}. All local rule, path endpoint and
factorization checks pass. The counts are the following.
\[
\begin{array}{lrr}
\toprule
\text{Small domain stage}&\text{excluded}&\text{remaining}\\
\midrule
\text{Initial domain}&&37,530\\
\text{Horn factorization}&17,883&19,647\\
\text{Rectangular shortening}&6,300&13,347\\
\text{Second reduction}&932&12,415\\
\midrule
\text{Large domain stage}&\text{excluded}&\text{remaining}\\
\midrule
\text{Initial domain}&&1,255,228\\
\text{First paths with smaller endpoint key}&494,925&760,303\\
\text{Horn factorization}&200,638&559,665\\
\text{Second paths with smaller endpoint key}&196,934&362,731\\
\text{Second reduction}&16,194&346,537\\
\bottomrule
\end{array}
\]
In particular $|\mathcal C_{\rm small}|=12,415$,
$|\mathcal C_{\rm large}|=346,537$, and their disjoint union has
$358,952$ members.
\end{proposition}
```

Verification: Every actual path/exclusion, target, accumulated scale and fixed/residual set was independently checked; all supplied edges meet strict validity requirements. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`, `replay/verification.json`, `computational_audit/corpus_inventory.json`, `computational_audit/horn_and_final_cover.json`.

Prior art: Complete finite-box E/R/P corpus and resulting theorem: no substantive match found in the documented search. Progress credit: Supports the E/R/P obligations; the same conclusion is not counted twice. Confidence: High in the checked deduction; conditional on the named software/finite-execution premises.

### C17: Literal array-hive correspondence

Source: `manuscript/v010.tex:1013`. Validity **V**; novelty **N0**.

Premises/scope: Standard cited mathematical inputs and the publication typing conventions. Dependencies: 1, integer cumulative sums and mixed differences.

```tex
\begin{lemma}[Literal array--hive correspondence]\label{lem:hivebinding}
For every integer $t\ge1$,
\[
 \#(tH_T\cap\mathbb Z^D)=c^{t\lambda}_{t\mu,t\nu}.
\]
\end{lemma}
```

Verification: Literal boundaries, three slack families, omitted cases, diagonal nonnegativity and full integer-lattice inverse verified. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`.

Prior art: Standard published input, known-consequence symmetry/array calculation, or logical implication; no novelty credit assigned. Progress credit: 0 Confidence: High within this conventional mathematical audit; not formally verified.

### C18: Finite dependency P

Source: `manuscript/v010.tex:1077`. Validity **VC**; novelty **N3**.

Premises/scope: Correct exact LR/Normaliz software and source-bound observed finite execution, as applicable. Dependencies: 17, Rassart polynomiality/degree, Normaliz exact execution, LattE counts on declared subset, record source binding.

```tex
\begin{proposition}[Finite dependency P]\label{comp:P}
For each $T\in\mathcal C_{\rm small}\cup\mathcal C_{\rm large}$,
the supplied record contains a rational coefficient vector
$(a_{T,0},\ldots,a_{T,d_T})$, $d_T\le15$, which the specified exact
Ehrhart computation identifies with $P_T$. Every entry is nonnegative.
There is one accepted polynomial for every residual triple and no
unresolved or mismatched source. Consequently
\[
 \forall T\in\mathcal C_{\rm small}\cup\mathcal C_{\rm large},\quad
 \forall t\in\mathbb Z_{\ge1},\quad
 c^{t\lambda}_{t\mu,t\nu}=\sum_{i=0}^{d_T}a_{T,i}t^i,
 \qquad a_{T,i}\ge0.
\]
\end{proposition}
```

Verification: Every complete source polynomial was freshly recomputed, then its literal hive input and full rational output vector were independently parsed and matched; Normaliz remains trusted. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`, `full_regeneration/complete.json`, `portable_full_validation.json`, `computational_audit/COMPUTATIONAL_AUDIT.md`.

Prior art: Complete finite-box E/R/P corpus and resulting theorem: no substantive match found in the documented search. Progress credit: Supports the E/R/P obligations; the same conclusion is not counted twice. Confidence: High in the checked deduction; conditional on the named software/finite-execution premises.

### C19: Computed finite-box positivity

Source: `manuscript/v010.tex:1209`. Validity **VC**; novelty **N3**.

Premises/scope: Correct exact LR/Normaliz software and source-bound observed finite execution, as applicable. Dependencies: 14, 15, 16, 18.

```tex
\begin{theorem}[Computed finite-box positivity]\label{thm:box}
For every balanced triple
$T=(\lambda,\mu,\nu)$ of partitions satisfying
\[
 \max\{\ell(\lambda),\ell(\mu),\ell(\nu)\}\le7,
 \qquad\max\{|\lambda|,|\mu|,|\nu|\}\le30,
\]
every coefficient of $P^\lambda_{\mu\nu}$ in the monomial basis is
nonnegative. Thus no triple requested by the bounded problem exists.
\end{theorem}
```

Verification: C14 together with the checked E, R and P establishes the exact finite-box conclusion under the explicitly stated software assumptions. Evidence: `paper_audit/audit_report.md`, `paper_audit/claim_inventory.json`, `full_regeneration/complete.json`, `portable_full_validation.json`, `computational_audit/COMPUTATIONAL_AUDIT.md`.

Prior art: Complete finite-box E/R/P corpus and resulting theorem: no substantive match found in the documented search. Progress credit: Supports the E/R/P obligations; the same conclusion is not counted twice. Confidence: High in the checked deduction; conditional on the named software/finite-execution premises.

### C20: General parser rejects all invalid certificate inputs

Source: `manuscript/v010.tex:932`. Validity **F**; novelty **N0**.

Premises/scope: Universal statement over arbitrary submitted records. Dependencies: original local parser.

```tex
The general-purpose checker rejects every malformed partition and invalid reduction parameter before relying on a certificate.
```

Verification: Constructed accepted internal-zero and invalid-selector mutations; inspected every actual frozen edge with a strict independent parser. Evidence: `computational_audit/parser_and_reduction_mutations.json`, `computational_audit/corpus_inventory.json`.

Prior art: Software behavior, not a novel theorem. Progress credit: 0 Confidence: Definite wording error; every actual supplied certificate passed the stricter requirement.

Correction: ARCHIVAL_ERRATA.md item 3; distinguishes validity requirement from original parser behavior.

### C21: Archived polynomiality-paper authorship

Source: `spec.json:83`. Validity **F**; novelty **N0**.

Premises/scope: Bibliographic attribution. Dependencies: none.

```tex
The author of arXiv:2211.06810 is R. Wong.
```

Verification: Direct official arXiv metadata and bibliography inventory. Evidence: `licensing_audit/arxiv_primary_receipt.json`, `licensing_audit/result.json`.

Prior art: The paper is by Warut Thawinrak, first submitted 2022 and revised 2024. Progress credit: 0 Confidence: Definite archival attribution error, absent from v010 bibliography.

Correction: ARCHIVAL_ERRATA.md item 4; frozen bytes preserved.

## Appendix B. Source and search log

`prior_art_search_log.json` records all 13 root queries, access cutoff, URLs,
publication dates, bounded negative finding and discarded lookup. The primary
mathematical source log is `paper_audit/sources.json`; the KTT09 followup has
its own source/access record. Licensing primary URLs, exact-license hashes and
retrieval dispositions are in `licensing_audit/PRIMARY_SOURCES.md` and its JSON
receipts. No restricted-source access was bypassed. Downloaded third-party
papers and provider conversations are excluded from the public audit payload.

Local evidence includes `replay/verification.json`, the complete computational
and paper-audit results, `full_regeneration/complete.json`, and
`portable_full_validation.json`. The corrected release's FRESH_EVIDENCE.json
binds the raw supplement, its complete file manifest, the full producer and
portable-check receipts, source identity, exact counts and validator code.
The actual final ZIP extraction, rendering, licensing and seven-stage replay
are recorded separately after packaging; this mathematical audit does not
pre-assert those later publication checks.
