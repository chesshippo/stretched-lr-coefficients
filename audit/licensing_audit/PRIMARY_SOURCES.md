# Primary-source log

Access date: **2026-09-06 UTC**. Only upstream, author, publisher, provider, government or official project sources support this licensing report. Web references below were inspected during this audit; a link is not a claim that its complete contents are archived locally. Retained downloads are audit-local and are not release files. No downloaded third-party paper is added to the public package.

`primary_fetch_log.json` records initial local certificate-chain failures. `primary_fetch_log_tls.json` and `primary_fetch_log_extra.json` record later fetches using verified TLS with the installed CA bundle. A direct PyPI request returned a challenge page; its saved HTML is **not** evidence for the package license. The working browser tool's rendered maintainer page supplied that evidence. The CC text endpoint rejected one direct request; the official CC repository supplied the exact comparable text. These failures were not interpreted as substantive answers.

## Licenses, dependencies and statements

| Primary source | Observation / use | Local evidence when retained |
| --- | --- | --- |
| [GNU GPLv3 text](https://www.gnu.org/licenses/gpl-3.0.txt) | Exact outer LICENSE comparison; source, output and aggregate provisions | `primary_sources/gnu_gpl3.txt`; `license_text_comparison.json` |
| [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html) | Output and aggregation explanation; separate-process use distinguished from linking | `primary_sources/gnu_faq.txt` |
| [CC-BY-4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en) | Attribution, modification indication, restrictions, scope, database rights | Browser inspection |
| [Official CC text repository](https://raw.githubusercontent.com/creativecommons/cc-legal-tools-data/main/legacy/legalcode/by_4.0.txt) | Exact outer CC text comparison | `primary_sources/cc_by4_upstream.txt`; comparison receipt |
| [Epoch problem page](https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients) | Statement attribution and page's CC-BY license link | `primary_sources/epoch.txt` |
| [lrcalc 2.1 maintainer page](https://pypi.org/project/lrcalc/2.1/) | GPLv3-or-later wording and package identity | Browser inspection; saved direct-request challenge is unusable |
| [Buch's LR Calculator page](https://sites.math.rutgers.edu/~asbuch/lrcalc/) | Upstream author/project/source | Browser inspection |
| [Normaliz v3.11.1 header](https://raw.githubusercontent.com/Normaliz/Normaliz/v3.11.1/source/libnormaliz/libnormaliz.h) | Named authors, GPLv3-or-later and additional permission | `primary_sources/normaliz_header.txt` |
| [Normaliz v3.11.1 COPYING](https://raw.githubusercontent.com/Normaliz/Normaliz/v3.11.1/COPYING) | Actual upstream distribution license | `primary_sources/normaliz_license.txt` |
| [Normaliz v3.11.1 README](https://raw.githubusercontent.com/Normaliz/Normaliz/v3.11.1/README.md) | Engine/project identity | Browser inspection |
| [LattE project](https://www.math.ucdavis.edu/~latte/) | Release's upstream attribution link resolves | Browser inspection |
| [LattE COPYING](https://raw.githubusercontent.com/latte-int/latte/master/COPYING) | GPLv2 text; current master does not pin the historical installed binary's complete source | `primary_sources/latte_license.txt` |
| [LattE source header](https://raw.githubusercontent.com/latte-int/latte/master/code/latte/ReadLatteStyle.cpp) | GPL version 2 wording and Matthias Köppe copyright; avoid blanket later-version claim | `primary_sources/latte_header.txt`; comparison fetch receipt |
| [NumPy 2.3 license](https://numpy.org/doc/2.3/license.html) | BSD-style upstream terms and developer attribution | Browser inspection |
| [PyYAML 6.0.3 LICENSE](https://github.com/yaml/pyyaml/blob/6.0.3/LICENSE) | MIT and Kirill Simonov attribution | Browser inspection |
| [CTAN Latin Modern](https://ctan.org/pkg/lm), [GUST license](https://ctan.org/license/gfl) | Font family and upstream license pointer | Browser inspection |
| [Latin Modern upstream README on CTAN mirror](https://ctan.math.illinois.edu/fonts/lm/README) | Upstream author and license statements | `primary_sources/lm_readme.txt` |
| [AMSFonts CTAN](https://ctan.org/pkg/amsfonts), [upstream README](https://ctan.math.illinois.edu/fonts/amsfonts/README) | Type 1 font and support-file license distinctions | `primary_sources/ams_readme.txt` |
| [OFL FAQ](https://openfontlicense.org/ofl-faq/), [LPPL 1.3c](https://www.latex-project.org/lppl/lppl-1-3c/) | Font/document distinction and upstream terms; exact embedded builds not reconstructed | `primary_sources/lppl.txt` plus browser inspection |

## Authorship, providers and publication metadata

| Primary source | Observation / use |
| --- | --- |
| [OpenAI Terms of Use](https://openai.com/policies/terms-of-use/) | Output interest assignment subject to law; nonuniqueness and third-party rights; human/AI representation |
| [OpenAI Services Agreement](https://openai.com/policies/services-agreement/) | Customer-output terms; customer identity is not determined by this archive |
| [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms) | Output rights assignment if any, subject to contract |
| [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms) | Customer-content and output provisions |
| [U.S. Copyright Office AI copyrightability report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | January 2025 primary government discussion of human contribution; U.S. jurisdiction, case-specific |
| [GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) | Public hosting is not a substitute for a license; recognizable root license text |
| [GitHub citation files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) | Preferred citation and `unpublished` type |
| [GitHub Terms, user content](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content) | Content rights and hosting/fork permissions |
| [GitHub large-file documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) | Browser-upload size guidance checked against six ≤20 MiB parts |
| [GitHub citation/archive guidance](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) | A later Zenodo DOI can identify a public archive; no own DOI presently asserted |

## Bibliographic identity checks

These checks establish source identities/metadata for attribution. They do not substitute for the mathematical referee's theorem-hypothesis audit.

| Citation | Primary identity source and observation |
| --- | --- |
| Archived short proof, arXiv:2211.06810 | [Official arXiv](https://arxiv.org/abs/2211.06810): **Warut Thawinrak**, 2022 first submission / 2024 revision. Frozen spec's “R. Wong” is incorrect. Saved `primary_sources/arxiv_2211_06810.html`, SHA256 `fd56a4d5ef03f0d8747c210dec99ac60d5f597a6cdbda6f3b12d70192367abdd`, and `arxiv_primary_receipt.json`. |
| Rassart | [Author publications](https://pi.math.cornell.edu/~rassart/publications.html), [author PDF](https://pi.math.cornell.edu/~rassart/pub/LRstretch.pdf): title, author, JCTA 107 (2004), 161–179. |
| Knutson–Tao | [arXiv math/9807160](https://arxiv.org/abs/math/9807160): author/title identity for honeycomb I. |
| Knutson–Tao–Woodward | [arXiv math/0107011](https://arxiv.org/abs/math/0107011): author/title identity for honeycomb II. |
| Ikenmeyer | [arXiv 1209.1521](https://arxiv.org/abs/1209.1521): *Small Littlewood–Richardson coefficients*, Christian Ikenmeyer. |
| Buch / Fulton | [Buch's author copy](https://sites.math.rutgers.edu/~asbuch/papers/sat.pdf): saturation article and appendix attribution. |
| Milne | [Author's Reductive Groups notes](https://www.jmilne.org/math/CourseNotes/RG.pdf): v2.00 dated 10 March 2018. |
| King–Tollu–Toumazet 2009 | [Publisher metadata](https://www.sciencedirect.com/science/article/pii/S0097316508000939), [Southampton author repository](https://eprints.soton.ac.uk/66211/): JCTA 116, 314–333, DOI 10.1016/j.jcta.2008.06.005. Direct full text was restricted; theorem number not independently certified here. |
| Roth | [arXiv 1004.5133](https://arxiv.org/abs/1004.5133): *Reduction rules for Littlewood–Richardson coefficients* identity. |
| Cho–Jung–Moon, second reduction | [Author institution record](https://sejong.elsevierpure.com/en/publications/a-bijective-proof-of-the-second-reduction-formula-for-littlewood-/): BKMS 45 (2008), 485–494, DOI 10.4134/BKMS.2008.45.3.485. |
| Cho–Jung–Moon, FPSAC | [DMTCS publisher](https://dmtcs.episciences.org/3592): author/title/2008 proceedings identity. |
| Sherman, archived specification | [arXiv 1505.06551](https://arxiv.org/abs/1505.06551): author and title agree. |
| Ferudun, archived specification | [arXiv 2607.22301](https://arxiv.org/abs/2607.22301): Alper Ferudun, July 2026; existing primary record, not an invented future citation. |
| Epoch / Normaliz | Official project sources logged above; included among the 12 current formal bibliography entries. |

## Retention and legal limits

Saved upstream license texts and metadata were downloaded to inspect the actual conditions and identities. Their presence in this **private audit directory** is not a recommendation to redistribute all of them with the release. PDF metadata/font inventories pertain to the distributed project PDFs. Prior mathematical reviews and their verdicts were not used as source evidence for this audit. Contract applicability, employment assignments, jurisdiction-specific protectability and unmarked copying cannot be conclusively established from a package scan.
