# Review of the proposed publication erratum

Reviewed on 6 September 2026 against frozen `manuscript/v010.tex`, SHA-256 `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45`. No frozen source was changed.

The proposed erratum is mathematically correct. The partition letter in Lemma 6 is **α**, not η. The following wording uses the manuscript's exact notation:

> In Lemma 6 (Rectangular complement), the complement width satisfies \(M\in\mathbb Z_{\ge0}\) and \(M\ge\alpha_1\). In Theorem 7 (Six polynomial-preserving representatives), the ambient rank is an integer \(n\ge1\), with all three partitions padded to that rank. The all-empty input at rank zero is handled separately by \(P_{(\varnothing,\varnothing,\varnothing)}(t)=1\). Every nonempty least-witness application uses integer widths and positive rank.

The zero-padding convention already supplies \(\alpha_1=0\) when α is empty. The existing requirement that the chosen rank contain all three partitions remains in force; explicitly, \(n\ge\max\{\ell(\lambda),\ell(\mu),\ell(\nu)\}\).

These are typing and degenerate-rank clarifications. Integer widths make the complement an ordinary partition and the determinant power an integer power. Positive rank makes \(h=\lambda_n\) well-defined. In the proof, the widths are integer expressions in partition parts, and their required inequalities are already proved. A nonempty least witness has positive outer size and hence positive outer length. The all-empty polynomial is already treated separately at manuscript lines 79–83.

No mathematical identity, numerical bound, residual count, or finite-box conclusion changes. No further weakening of an assertion was identified by this mathematical audit. The separate E, R and P execution requirements and the disclosed software trust boundary remain exactly as stated; this erratum does not discharge them or establish proof-assistant completion.
