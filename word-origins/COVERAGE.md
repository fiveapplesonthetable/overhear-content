# Word-history coverage

Target: a sourced, reviewed Origin entry for every served dictionary word. An origin described as unknown or disputed still needs a specific supporting source. A source link alone does not verify the accompanying claim.

| Pair | Dictionary words | Sourced histories | Still to review |
| --- | ---: | ---: | ---: |
| ru-en | 2105 | 22 | 2083 |
| fr-en | 103 | 22 | 81 |

Counts describe the serving catalogue used for this report; they are not a claim of full coverage. The queue includes grammar words, names and phrases rather than silently excluding them. Refresh it as episodes or dictionary entries are added.

## Every published season

| Pair | Season | Audio scenes | Learning notes | Resolved headwords | Histories | Missing | Unresolved forms |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ru-en | kukhnya/s01 | 214 | 20 | 2105 | 22 | 2083 | 187 |
| fr-en | dix-pour-cent/s01 | 0 | 11 | 25 | 10 | 15 | 37 |

The season audit includes spoken words, episode vocabulary and published learning-note target text. A row with learning notes and zero audio scenes does not mean episode audio is published. Unresolved or ambiguous forms, including teaching fragments that need classification, are reported separately and prevent a completeness pass; they are not silently omitted. Unpublished draft episodes do not enter the report.

## Next words: ru-en

на, и, весь, это, что, в, с, этот, а, очень, мой, у, наш, сейчас, пока, повар, за, да, просто, уже

## Next words: fr-en

accord, ah, aide, aider, allô, alors, appeler, assistant, attendre, au, avec, beau, beaucoup, bien, bientôt, bon, ce, cent, compter, content

Regenerate from a verified serving build:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/out --markdown word-origins/COVERAGE.md --json /path/to/review-queue.json
```

Before publishing a new or expanded season, require a complete audited candidate:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/candidate --season dix-pour-cent/s01 --require-complete
```

Omit `--season` to require complete coverage of every served dictionary and season. The command exits unsuccessfully while any requested scope has gaps.
