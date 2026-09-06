# Clarifications and archival errata — version 1.0.2

Credited author and project lead: **Maseeh Ghodsi**. Prepared 6 September 2026.
Read these corrections together with the unchanged v010 manuscript. Its TeX
SHA-256 is `3deebd9376714584ad6f6156d8fed5f26872bdd09541470f408f2403d664fd45`.
No coefficient, reduction formula, residual set, or finite-box conclusion changes.

1. **Lemma 6, complement width** (TeX lines 248–252): explicitly take the
   rectangle width `M` to be a nonnegative integer with `M >= alpha_1`.
   Counting columns already presumes this convention; every application uses
   an integer partition part as its width.
2. **Theorem 7, ambient rank** (lines 279–283): explicitly take an integer
   `n >= 1` at least as large as all three partition lengths. This makes
   `h = lambda_n` well-defined. The all-empty input is separately settled by
   its polynomial `P = 1`. Every nonempty least-witness application has
   positive rank.
3. **Certificate validation description** (lines 932–933): the stated
   rejection of every malformed partition or invalid parameter is a
   certificate-validity requirement, and overstates the behavior of the
   original general-purpose parser. That parser removes internal zero parts
   and interprets an unrecognized inner selector as `nu`. The independent
   exhaustive strict audit checks the original raw frozen records before
   normalization; every actual edge has valid partition order, selector and
   integer parameters, and satisfies its rule and target conditions. Thus
   the required validity of the supplied certificates, and dependency R,
   are unchanged. See `audit/COMPUTATIONAL_AUDIT.md` and its linked evidence.
4. **Archived reference attribution:** in the frozen
   `problems/stretched-lr-coefficients/spec.json:83`, JSON pointer
   `/known_partial_results/0/citation`, the author of arXiv:2211.06810 is
   **Warut Thawinrak**, correcting the recorded name “R. Wong.” The work is
   *A Short Proof for the Polynomiality of the Stretched Littlewood-Richardson
   Coefficients*, first submitted in 2022 and revised in 2024.
   [Official arXiv record](https://arxiv.org/abs/2211.06810).
   The frozen specification SHA-256 is
   `2b9f91614a3e5aa0af887391442819935a5e45d8198edb086bfdca19f99111b0`.
   This erroneous attribution is absent from the current manuscript's
   bibliography. The archived bytes are retained to preserve their bindings.

The new public PDF includes these clarifications before the unchanged
19-page mathematical manuscript. Original frozen files and the six original
evidence parts remain byte-identical. The addendum and new audit evidence
are separately identified; they do not retroactively alter frozen referee
reports or claim a new harness acceptance transition.

Original explanatory text is covered by the release's CC-BY-4.0 grant to the
extent applicable rights exist and are held by the licensor. The cited author
and third-party material retain their own credit and rights.
