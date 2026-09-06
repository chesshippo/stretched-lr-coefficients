# Mathematical review of the certificate-parser clarification

Reviewed on 6 September 2026 against frozen `manuscript/v010.tex`, SHA-256 `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45`. No frozen source was changed.

**Assessment:** the proposed correction is mathematically appropriate. It corrects an implementation-description overstatement at manuscript lines 932–933. It does not weaken the hypotheses of the finite-cover theorem or change the finite-box conclusion, provided the independent strict scan covers the same complete frozen edge collection used in R, as the code referee reports.

The following factual findings were supplied by the separate code referee; this mathematical review did not independently inspect or rerun that implementation:

- The original parser removes every zero part, including internal zeros, so it can turn `[3,0,2,1]` into `[3,2,1]`.
- For an inner selector it takes `mu` literally and otherwise uses `nu`, rather than rejecting every other selector string.
- The independent strict scan checked every actual archived path and found valid partitions, selectors and parameters throughout. Neither permissive behavior was used to accept a malformed archived edge.

The claim that the original parser rejects all hypothetical malformed inputs is therefore too strong. This is an additional descriptive correction beyond the earlier integer-width and positive-rank clarifications. The earlier mathematical audit expressly left implementation validation to the separate code audit.

Suggested publication wording:

> At lines 932–933, the listed conditions are requirements for a valid certificate. The original parser does not enforce all of these conditions on arbitrary malformed inputs: it removes internal zero parts and defaults an unrecognized inner selector to `nu`. An independent complete strict audit checks these input-validity requirements for every edge in the frozen archived path collection and reports no malformed edge. These checks supplement the original local-rule, target, scale, endpoint and coverage verification. The archived reduction dependency R and the finite-box conclusion are unchanged.

The actual proof needs the validity of its finitely many archived certificates, as stated at lines 831–836. It does not need a universally rejecting parser for every string an external caller could supply. Once each actual raw partition and selector is independently checked, normalization does not alter its mathematical meaning and selector interpretation agrees with the declared rule. The original verified identities, positive scales, final in-box key comparisons and complete coverage can then be used exactly as before.

The strict scan should be cited with its complete scope and frozen-artifact binding. It should be described as supplementary independent evidence, not as a behavior retrospectively attributed to the original parser. A scan of a subset, or a scan only after the permissive normalization, would not justify this clarification; the code referee reports the required complete strict check of the actual records.

No other mathematical assertion needs weakening because of these two parser behaviors. The correction does not excuse a malformed archived certificate, replace the remaining R obligations, establish P, or establish proof-assistant completion. It also does not certify the original parser as sound for arbitrary future submissions.
