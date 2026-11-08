# Word-history coverage

Target: a sourced, reviewed Origin entry for every served dictionary word. An origin described as unknown or disputed still needs a specific supporting source. A source link alone does not verify the accompanying claim.

| Pair | Dictionary words | Sourced histories | Still to review |
| --- | ---: | ---: | ---: |
| ru-en | 1750 | 110 | 1640 |
| fr-en | 1393 | 370 | 1023 |
| es-en | 1221 | 292 | 929 |
| de-en | 1444 | 289 | 1155 |
| it-en | 1203 | 135 | 1068 |
| pt-en | 1197 | 49 | 1148 |

Counts describe the serving catalogue used for this report; they are not a claim of full coverage. The queue includes grammar words, names and phrases rather than silently excluding them. Refresh it as episodes or dictionary entries are added.

## Every published season

| Pair | Season | Audio scenes | Learning notes | Resolved headwords | Histories | Missing | Unresolved forms |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ru-en | dvorik-u-mosta/s01 | 24 | 20 | 795 | 67 | 728 | 3 |
| fr-en | hotel-du-tilleul/s01 | 16 | 12 | 544 | 211 | 333 | 36 |
| es-en | posada-del-limonero/s01 | 8 | 10 | 382 | 202 | 180 | 20 |
| de-en | pension-sonnenhof/s01 | 8 | 10 | 377 | 106 | 271 | 13 |
| it-en | locanda-del-tiglio/s01 | 8 | 10 | 374 | 65 | 309 | 35 |
| pt-en | pousada-do-cajueiro/s01 | 8 | 10 | 339 | 15 | 324 | 31 |

The season audit includes spoken words, episode vocabulary and published learning-note target text. A row with learning notes and zero audio scenes does not mean episode audio is published. Unresolved or ambiguous forms, including teaching fragments that need classification, are reported separately and prevent a completeness pass; they are not silently omitted. Unpublished draft episodes do not enter the report.

## Next words: ru-en

в, и, на, а, у, этот, с, что, за, кира, весь, мой, один, вот, как, до, добрый, для, матвей, ой

## Next words: fr-en

bleu, vieux, quatre, sept, garder, matin, nom, numéro, vendredi, voici, bureau, donner, déjà, frais, huit, monsieur, personne, pourquoi, propre, exactement

## Next words: es-en

sí, dos, primero, se, solo, alguien, madera, necesitar, papel, bienvenido, ese, gafas, listo, llegar, mucho, nombre, segundo, sin, tocar, abrigo

## Next words: de-en

und, frau, helga, im, am, danke, klara, klingeln, vier, bis, alle, an, dieser, er, miriam, nur, papier, für, ganz, genau

## Next words: it-en

la, il, di, uno, a, mio, tutto, proprio, signora, blu, che, della, alla, guardare, le, nessuno, quattro, quello, questo, suonare

## Next words: pt-en

o, e, em, um, com, que, mala, ter, meu, bom, senhora, aqui, ficar, para, dia, olhar, obrigado, por, quarto, a

Regenerate from a verified serving build:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/out --markdown /path/to/coverage.md --json /path/to/review-queue.json
```

Before publishing a new or expanded season, require a complete audited candidate:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/candidate --season dix-pour-cent/s01 --require-complete
```

Omit `--season` to require complete coverage of every served dictionary and season. The command exits unsuccessfully while any requested scope has gaps.
