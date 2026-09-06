# Disposition of the fresh Fable full-scope report

The fresh other-family reviewer returned **MINOR**, with 28 of 28 requested
computational checks passing and no protocol errors. Recorded model:
`claude-fable-5-1`, effort `max`, cost USD17.607496, wall time2086s. This is
an additional isolated audit, not a replacement of frozen review013 or a
harness acceptance/state transition.

The input context binds exactly the v010 TeX hash
`3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45` and frozen
specification `2b9f91614a3e5aa0af887391442819935a5e45d8198edb086bfdca19f99111b0`.
The reviewer received the frozen specification, manuscript and declared
computational appendix, without handoffs or earlier referee opinions.
Its appendix transcript records40 reads, one complete seven-stage replay
and six selected fresh polynomial regenerations. The28 later requested
checks include14 cached polynomial results; they must not be described as
28 fresh whole-polynomial calculations. Other requested checks and the six
separate raw-retaining regenerations are identified in the saved transcripts.

The report's internal theorem numbers are sometimes mistaken, despite the
correct input hashes and matching statements. In v010 the six representatives
are Theorem7, rectangular shortening is Theorem11, the array–hive bridge is
Lemma17, and the final computed conclusion is Theorem19. Refer to the exact
titles/statements and `../paper_audit/claim_inventory.json`, not the report's
inconsistent numeric locators. The unmodified report remains preserved.

| Comment | Evidence and disposition |
|---|---|
| Noncontained targets in the second reduction | The direct primary CJM coefficient theorem and rectangle theorem were checked in the separate fresh paper audit, including the precise zero-case formulation. Its bounded test contains1,164 valid second-reduction targets that lose containment, all with zero coefficients as stated. The manuscript's monotonicity argument covers successive zero cases. The full finite cover uses positive sources anyway. No theorem weakening is required on this evidence. See `../paper_audit/audit_report.md`, the second-reduction analysis and primary-source inventory. |
| Essential Horn subset formulation | The exact operative CJM Definition1.2/Theorem1.3 was read and matched directly by the fresh paper audit. It requires the same multiplicity-one subset condition, positive source and equality. KTT09's locator remains inaccessible directly, but is corroborated by an authored later paper, as recorded in `ktt09_citation_followup.md`. Abstract-only access in this Fable session is an access limitation, not a counterexample to the cited theorem. |
| Positive stretching attributed to saturation | Positive hive dilation suffices and is the elementary direction of the saturation equivalence. The statement made is true; no extra conjecture is assumed and no mathematical correction is needed. |
| Milne and KTW locators | The fresh paper audit directly checked Milne17.14/20.35 and KTW§6.1. Their hypotheses and the characteristic-zero application match. This resolves the locator access limitation in the Fable session. |
| Normaliz trust and sparse cross-checks | Correct and material. Sparse LR values do not identify the full residual polynomial. The supervisor has launched a separate complete raw-retaining Normaliz regeneration; its completion must be assessed from its own receipt, not this report. A second full Ehrhart implementation for every residual and formal verification of the engine remain outside this audit. |

The additional source checks resolve the report's source-access concerns.
The declared exact-software dependency remains visible. No completed Lean
proof, universal KTT positivity, external endorsement, or error-free software
implementation follows from this internal report.
