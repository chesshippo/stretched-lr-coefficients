# Bounded KTT09 locator follow-up

Date: 6 September 2026. Search began at 12:33:58 UTC and ended before 12:39 UTC, within the requested ten-minute bound. Only public institutional, author and publisher access routes were used. No access restriction was bypassed and no request was sent to an author.

**Direct verification of KTT09 Theorem 1.4: UNCONFIRMED.** The exact locator is independently corroborated by a later authored paper, but KTT09's own theorem text was not retrieved.

**DOI: CONFIRMED as `10.1016/j.jcta.2008.06.005`.** This is the DOI actually printed at frozen manuscript line 1271. The `.004` suffix mentioned in the follow-up assignment is not the manuscript's DOI. The title, volume 116, issue 2, pages 314–333, year 2009 and `.005` DOI agree with the author-institution record and publisher-deposited Crossref metadata.

Public source checks:

| Source/route | Result |
|---|---|
| [Southampton author-institution record](https://eprints.soton.ac.uk/66211/) | Bibliographic match. Its displayed PDF is explicitly restricted to repository staff; that restricted file was not requested. Public record saved as `ktt09_soton_record.html`. |
| [Crossref record](https://api.crossref.org/works/10.1016/j.jcta.2008.06.005) | Retrieved publisher-deposited metadata, including DOI and advertised Elsevier text-retrieval links. Saved as `ktt09_crossref.json`. |
| [Publisher article page](https://www.sciencedirect.com/science/article/pii/S0097316508000939) and its public `/pdf` link | Both returned HTTP 403. |
| Publisher's advertised XML retrieval link | Returned only 1,950 bytes of core bibliographic/open-access metadata, with no body or theorem text. Saved as `ktt09_publisher_advertised.xml`. Its wrapper name does not make this a retrieved full text. |
| Publisher's explicit FULL view | Returned HTTP 401; no further access attempt was made through that route. |
| Publisher's advertised plain-text retrieval link | Returned HTTP 400. |
| [LIPN author-team publication list](https://www.lipn.fr/pages/fr/research/teams/calin/publications.html) | Contains the exact 2009 title/authors, but the corresponding link cell is empty. Public page saved as `ktt09_author_lipn.html`. |
| [King's Southampton author page](https://www.southampton.ac.uk/maths/about/staff/rck.page) | Public profile retrieved; no public KTT09 manuscript link found. Saved as `ktt09_author_king.html`. |
| HAL public API, exact DOI and exact title queries | Both returned zero matching records. Responses and query URLs saved. |
| OpenAlex location discovery | Points to the same publisher PDF and a non-open Southampton record, with no full-text repository location. Saved as `ktt09_openalex.json`; this is discovery metadata, not mathematical evidence. |

The independent locator corroboration is explicit in Chen, Gibney, Heller, Kalashnikov, Larson and Xu, [*On an equivalence of divisors on M̄₀,ₙ from Gromov–Witten theory and conformal blocks*](https://arxiv.org/pdf/2107.00174), Appendix A.1, proof of Lemma A.1, printed page 18. It attributes the boundary factorization to “Theorem 1.4 of [KTT09]”. The bibliography identifies [KTT09] with the exact King–Tollu–Toumazet 2009 article. The downloaded authored preprint is `ktt09_locator_corroboration_chen_et_al.pdf`; its extracted text has the locator at line 956 and the reference at lines 1364–1365.

This corroboration makes a mistaken locator less likely, but is not a direct inspection of KTT09. It is not substituted for the operative CJM theorem already verified in the fresh mathematical audit. No mathematical conclusion or citation text in frozen v010 was changed.

Search strings included exact-title variants; exact title with “1.4” and “Theorem 1”; DOI and PII searches; author names with the title and “pdf”; and searches restricted to `lipn.univ-paris13.fr`, `lipn.fr`, `hal.science`, and `univ-mlv.fr`. The useful later-paper query result is preserved verbatim in `ktt09_query_evidence.json`. HTTP outcomes and URLs are preserved in `ktt09_download_log.json`, `ktt09_publisher_link_log.json`, `ktt09_hal_query_log.json`, and `ktt09_final_sources_log.json`.

The earlier 2006 KTT paper also appeared in search results, but it is a different article and was not used to confirm a 2009 theorem number. No secondary snippet or metadata record was represented as direct access to the requested theorem.
