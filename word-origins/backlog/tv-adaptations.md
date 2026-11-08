# Word-history coverage

Target: a sourced, reviewed Origin entry for every served dictionary word. An origin described as unknown or disputed still needs a specific supporting source. A source link alone does not verify the accompanying claim.

| Pair | Dictionary words | Sourced histories | Still to review |
| --- | ---: | ---: | ---: |
| ru-en | 4107 | 22 | 4085 |
| fr-en | 2888 | 179 | 2709 |
| es-en | 1279 | 61 | 1218 |
| de-en | 410 | 24 | 386 |
| it-en | 287 | 20 | 267 |
| ja-en | 1757 | 13 | 1744 |
| zh-en | 2721 | 65 | 2656 |
| ko-en | 3176 | 12 | 3164 |
| ar-en | 260 | 7 | 253 |
| pt-en | 137 | 17 | 120 |

Counts describe the serving catalogue used for this report; they are not a claim of full coverage. The queue includes grammar words, names and phrases rather than silently excluding them. Refresh it as episodes or dictionary entries are added.

## Every published season

| Pair | Season | Audio scenes | Learning notes | Resolved headwords | Histories | Missing | Unresolved forms |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ru-en | domashniy-arest/s01 | 284 | 0 | 2900 | 22 | 2878 | 467 |
| ru-en | kukhnya/s01 | 397 | 20 | 2745 | 22 | 2723 | 271 |
| fr-en | dix-pour-cent/s01 | 153 | 11 | 1424 | 175 | 1249 | 361 |
| fr-en | dix-pour-cent/s02 | 161 | 0 | 1674 | 160 | 1514 | 296 |
| fr-en | dix-pour-cent/s03 | 152 | 0 | 1653 | 156 | 1497 | 215 |
| es-en | paquita-salas/s01 | 77 | 0 | 1279 | 61 | 1218 | 18 |
| de-en | die-discounter/s01 | 19 | 0 | 409 | 23 | 386 | 0 |
| it-en | boris/s01 | 11 | 0 | 287 | 20 | 267 | 30 |
| ja-en | the-naked-director/s01 | 124 | 0 | 1649 | 13 | 1636 | 236 |
| ja-en | the-naked-director/s02 | 10 | 0 | 412 | 11 | 401 | 41 |
| zh-en | behind-the-scenes/s01 | 170 | 0 | 2721 | 65 | 2656 | 70 |
| ko-en | the-producers/s01 | 244 | 0 | 3176 | 12 | 3164 | 100 |
| ar-en | alrawabi-school/s01 | 11 | 0 | 254 | 1 | 253 | 20 |
| pt-en | porta-dos-fundos/s01 | 5 | 0 | 137 | 17 | 120 | 6 |

The season audit includes spoken words, episode vocabulary and published learning-note target text. A row with learning notes and zero audio scenes does not mean episode audio is published. Unresolved or ambiguous forms, including teaching fragments that need classification, are reported separately and prevent a completeness pass; they are not silently omitted. Unpublished draft episodes do not enter the report.

## Next words: ru-en

что, в, это, весь, и, а, на, с, у, да, очень, этот, сейчас, ну, мой, так, же, наш, нет, хотеть

## Next words: fr-en

tout le monde, il y a, me, toi, plus, maintenant, votre, quoi, pourquoi, agent, grand, regarder, rôle, aimer, vrai, toujours, trop, comment, ils, travailler

## Next words: es-en

te, qué, hacer, ver, por, bueno, saber, se, para, tú, bien, mucho, ya, aquí, este, mirar, sí, si, pasar, pues

## Next words: de-en

das, haben, du, ein, und, kommen, mal, wir, machen, gehen, jetzt, was, bitte, sie, auf, in, es, er, da, wie

## Next words: it-en

uno, la, che, fare, di, avere, andare, dire, ti, a, il, dovere, per, scusare, bene, con, io, sapere, tutto, anno

## Next words: ja-en

は, て, する, よ, が, ます, を, た, か, ない, な, で, と, も, いい, こと, ん, やる, のだ, んで

## Next words: zh-en

吗, 在, 有, 我们, 也, 一, 要, 您, 个, 人, 跟, 去, 什么, 现在, 老大, 还, 没有, 她, 事, 想

## Next words: ko-en

나, 있다, 너, 되다, 안, 보다, 아니다, 가다, 신디, 우리, 뭐, 그러다, 없다, 오다, 알다, 좀, 피디, 그렇다, 지금, 그

## Next words: ar-en

ما, كان, يا, كل, مع, بنت, أنا, إشي, بس, حكى, عمل, شو, على, هون, إل, شاف, عرف, كتير, مش, اللي

## Next words: pt-en

que, o, um, ter, ela, outro, e, em, olhar, bom, agora, aqui, coisa, entrar, isso, achar, dentro, fazer, lá, querer

Regenerate from a verified serving build:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/out --markdown /path/to/coverage.md --json /path/to/review-queue.json
```

Before publishing a new or expanded season, require a complete audited candidate:

```sh
python3 tools/origin_coverage.py --serving-out /path/to/verified/candidate --season dix-pour-cent/s01 --require-complete
```

Omit `--season` to require complete coverage of every served dictionary and season. The command exits unsuccessfully while any requested scope has gaps.
