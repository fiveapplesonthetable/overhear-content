# Arabic taster: complete authored word-history review

Scope: all 14 ordinary dictionary lemmas in the frozen four-line salary taster, plus every italic native word in its two Learn articles. This review changes metadata only; accepted script and notes hashes remain unchanged.

| Lemma | Checked claim | Specific source |
| --- | --- | --- |
| راتب | regularity and salary | [Cairo Arabic Language Academy: رتب, especially الراتب and المرتب](https://www.arabicacademy.gov.eg/ar/search_engine/roots/رتب) |
| مصروف | spending root and participle pattern | [Cairo Arabic Language Academy: صرف, especially spending money and المصرف](https://www.arabicacademy.gov.eg/ar/search_engine/roots/صرف) |
| شهري | month and relational adjective | [Cairo Arabic Language Academy: شهر, especially الشهر, الشهري and الشهرية](https://www.arabicacademy.gov.eg/ar/search_engine/roots/شهر) |
| مسؤول | questioning and accountability | [Cairo Arabic Language Academy: سأل, especially المسؤول and المسؤولية](https://www.arabicacademy.gov.eg/ar/search_engine/roots/سأل) |
| يعني | verb lexicalised as a discourse marker | [Cairo Arabic Language Academy: عنى, especially intending something by speech](https://www.arabicacademy.gov.eg/ar/search_engine/roots/عني); [Yahya Mobarki, Yaʕni as an Evaluative Discourse Marker, Arabic Linguistics Journal 15 (2022),250–276](https://library.ksaa.gov.sa/links/emags/lesaneyat_15.pdf); [Getting to the point: The discourse marker yaʕni in unplanned discourse in Cairene Arabic (2016)](https://www.sciencedirect.com/science/article/pii/S0378216616300340) |
| قصد | direction, intention and possessive source form | [Cairo Arabic Language Academy: قصد, especially قصد بقولِه and the noun القصد](https://www.arabicacademy.gov.eg/ar/search_engine/roots/قصد) |
| احتاج | weak-root derived verb | [Cairo Arabic Language Academy: حاج, احتاج, الحاجة and محتاج in the أحوج definition](https://www.arabicacademy.gov.eg/ar/search_engine/roots/حوج) |
| اسم | traditional derivation debate and the paper’s assessment | [Cairo Arabic Language Academy: الاسم and أسماء](https://www.arabicacademy.gov.eg/ar/search_engine/roots/سمو); [Simona Olivieri, The ism in the Arabic Grammatical Tradition, JAIS 17, especially pp. 337–342](https://journals.uio.no/JAIS/article/view/6124) |
| أنا | inherited short pronoun; reconstructed versus written forms | [Ahmad Al-Jallad, A Manual of the Historical Grammar of Arabic, version 2019-1,§ 2.1, p. 47](https://almuslih.org/wp-content/uploads/Library/Jallad,%20A%20al%20-%20A%20Manual%20of%20the%20Historical%20Grammar%20of%20Arabic.pdf); [Cairo Arabic Language Academy: أنا](https://www.arabicacademy.gov.eg/ar/search_engine/roots/أنا) |
| عن | older relational and responsibility constructions | [Cairo Arabic Language Academy: عن](https://www.arabicacademy.gov.eg/ar/search_engine/roots/عن); [Cairo Arabic Language Academy: المسؤول and its quoted responsibility construction](https://www.arabicacademy.gov.eg/ar/search_engine/roots/سأل) |
| كل | totality and the related time expression | [Cairo Arabic Language Academy: كل, especially totality and the time expression with ما](https://www.arabicacademy.gov.eg/ar/search_engine/roots/كلل); [Abdelkader Fassi Fehri, Hidden Trilogies of Universal Quantifiers (2020)](https://doi.org/10.1111/stul.12131) |
| ناس | competing traditional derivations, explicitly attributed | [Cairo Arabic Language Academy: الناس](https://www.arabicacademy.gov.eg/ar/search_engine/roots/نوس); [Edward William Lane, Arabic–English Lexicon: نوس, entry ناس and its competing derivations](https://www.arabic-english-dictionary.com/content/25_n/291_nws) |
| اللي | relative-paradigm levelling, without a fabricated contraction | [Mohamed Galal, Relativizer illi in Arabic Dialects (2004),especially pp. 44–46](https://journals.ku.edu/kwpl/article/view/17173) |
| برا | older spatial adverb and reported register judgement | [Edward William Lane, Arabic–English Lexicon: بر,especially برّ signification B6](https://www.arabic-english-dictionary.com/content/02_b/057_br); [Cairo Arabic Language Academy: البر and البراني](https://www.arabicacademy.gov.eg/ar/search_engine/roots/برر) |

The name entry reports the old school dispute and also Olivieri’s conclusion against the marking analysis; it does not present the old proposals as equally supported. The people entry attributes competing explanations to lexicographers rather than choosing one from spelling alone. Starred pronoun forms are reconstructions, and vowel-length hypotheses are not pronunciation instructions for the actor. The outside entry distinguishes a reported register judgement from a dated first attestation.

Authored audit: **14/14 dictionary lemmas have sourced histories; 27/27 italic Learn word occurrences resolve uniquely; zero missing or ambiguous Learn words.** Extra practice terms were removed from the Learn text; useful written forms remain available in the dictionary drawer. No serving build was fabricated for this audit.

Validation: metadata-only validator prints `OK: 0 errors`; strict scene/teaching validation remains `OK: 0 errors, 1 warnings`, with the documented short-taster warning. Private evidence: `/mnt/agent/pilot-source-discovery/arabic-research/authored-origin-coverage-complete.json`. The actual deep-verified serving candidate must still pass:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/candidate --content-dir /path/to/integrated/content --season al-maktab/s01 --require-complete
```
