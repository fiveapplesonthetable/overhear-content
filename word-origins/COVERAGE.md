# Word-history coverage

Target: a sourced, reviewed Origin entry for every served dictionary word. An origin described as unknown or disputed still needs a specific supporting source. A source link alone does not verify the accompanying claim.

| Pair | Dictionary words | Sourced histories | Still to review |
| --- | ---: | ---: | ---: |
| ru-en | 2105 | 22 | 2083 |
| fr-en | 103 | 22 | 81 |

Counts describe the serving catalogue used for this report; they are not a claim of full coverage. The queue includes grammar words, names and phrases rather than silently excluding them. Refresh it as episodes or dictionary entries are added.

## Next words: ru-en

на, и, весь, это, что, в, с, этот, а, очень, мой, у, наш, сейчас, пока, повар, за, да, просто, уже

## Next words: fr-en

accord, ah, aide, aider, allô, alors, appeler, assistant, attendre, au, avec, beau, beaucoup, bien, bientôt, bon, ce, cent, compter, content

Regenerate from a verified serving build:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/out --markdown word-origins/COVERAGE.md --json /path/to/review-queue.json
```
