# Overhear Originals — Progress & Review Log

All new authoring and rendering work is strictly under `originals/<show>/` and released as `original-<episode>` (`spec/ORIGINALS.md`).

## 1. Season 1 Master Story & 10-Language Show Bibles — Originality Review (2026-11-06)

- **Reviewer:** Independent `research-google` subagent (`0722bc2e-59be-48f9-99a8-73cd0c808949`).
- **Premise & Script Finding:** Master English Season 1 (`originals/_english/bible.md`, `s01e01.json`–`s01e06.json`, 6 episodes × 8 scenes = 48 scenes, 576 dialogue lines) verified original, warm, and CEFR A1-appropriate with zero lifted lines, plot points, or jokes from `out/` or real TV/film/books.
- **Issues Flagged & Fixed Before Localized Scene Authoring:**
  1. **Russian Title & Cast Collision with *Hotel Eleon* & `out/` (`otel-dvorik`):** Renamed show to **`dvorik-u-mosta`** (*Дворик у моста* / *Bridge Courtyard Inn*) and replaced cast keys with zero-collision Russian names (`kira`, `matvey`, `zoya`, `yaroslav`, `larisa`, `roman`, `gleb`).
  2. **Same-Language & Cross-Pair `out/` Cast Collisions + Invented Guesthouse Names:**
     - `fr-en` → **`hotel-du-tilleul`** (*Hôtel du Tilleul*, Lyon): renamed `bernard/colette/julien/marc` → `etienne/odette/antoine/thibault`.
     - `es-en` → **`posada-del-limonero`** (*Posada del Limonero*, Valencia): renamed `diego` → `javier`.
     - `it-en` → **`locanda-del-tiglio`** (*Locanda del Tiglio*, Bologna): renamed `elena` → `chiara`.
     - `pt-en` → **`pousada-do-cajueiro`** (*Pousada do Cajueiro*, Recife): renamed `lucas` → `tiago`.
     - `de-en` → **`pension-sonnenhof`** (*Pension Sonnenhof*, Leipzig): renamed `jonas/felix` → `lukas/moritz`.
     - `ar-en` → **`bayt-al-yasmin`** (*بيت الياسمين*, Amman): `nour, tariq, salma, mazen, suad, rami, ziad` (0 `out/` overlap).
     - `ja-en` → **`hidamari-ryokan`** (*ひだまり旅館*, Osaka): `mio, kenji, yuka, takashi, kazuko, haruto, daiki` (0 `out/` overlap).
     - `ko-en` → **`haessal-guesthouse`** (*햇살 하우스*, Seoul): renamed `taeho` → `sungmin`.
     - `zh-en` → **`xiaoyuan-kezhan`** (*小院客栈*, Chengdu): renamed `lin/fang` → `qing/song`.
     - Verified across all 11 `out/*/cast.json` files: **0/70 cast collisions**.
  3. **Continuity & Cultural Localization Fixes:**
     - Updated childhood piano-lesson memory from `"forty years ago"` → `"twenty-five years ago"` (`s01e02`, `s01e04`, `s01e05`, `s01e06`, `bible.md`) to match 30-something brothers (`M3`, `M4`) and 60s teacher (`F3`).
     - Added explicit `"On Wednesday evening"` transition in `s01e02` Scene 8 so Monday (`E1`), Tuesday (`E2` S1–S7), Wednesday (`E2` S8–`E3`), Thursday (`E4`), and Friday (`E5`–`E6`) align seamlessly.
     - Aligned breakfast start time (`seven thirty to ten` in `s01e01` S4), guest count (`Eight guests` in `s01e02` S2), and acoustic notebook phrasing (`decibels and quietness` in `s01e03` S6 / `s01e04` S6).
     - Replaced hardcoded street/initial tokens with `{STREET}` and localized character names across all 10 show bibles and `scenes.json` files; added explicit climate/geography notes for Amman (`bayt-al-yasmin`), Recife (`pousada-do-cajueiro`), Osaka (`hidamari-ryokan`), Seoul (`haessal-guesthouse`), and Chengdu (`xiaoyuan-kezhan`).

## 2. Season 1 Authoring Matrix (All 10 Languages — 480 Scenes)

| Pair | Show Slug | Season 1 Scenes (`s01e01`–`s01e06`) | Notes & Word Tables | Native Readings (`span`+`reading`) | `dictionary/` + `word-origins/` + `learn/` | Status |
|---|---|---|---|---|---|---|
| `ru-en` | `dvorik-u-mosta` | 48 | `Declension` / `Present` / `Past` + U+0301 | n/a | `ru-en` | Done, 0 errors |
| `fr-en` | `hotel-du-tilleul` | 48 | `Forms` / `Present` / `Passé composé` + IPA | n/a | `fr-en` | Done, 0 errors |
| `es-en` | `posada-del-limonero` | 48 | `Forms` / `Present` / `Preterite` + IPA | n/a | `es-en` | Done, 0 errors |
| `it-en` | `locanda-del-tiglio` | 48 | `Forms` / `Present` / `Passato prossimo` + IPA | n/a | `it-en` | Done, 0 errors |
| `pt-en` | `pousada-do-cajueiro` | 48 | `Forms` / `Present` / `Preterite` + IPA | n/a | `pt-en` | Done, 0 errors |
| `de-en` | `pension-sonnenhof` | 48 | `Declension` / `Forms` / `Present` / `Past` + IPA | n/a | `de-en` | Done, 0 errors |
| `ar-en` | `bayt-al-yasmin` | 48 | `Forms` / `Present` / `Past` | 100% Jordanian ASCII | `ar-en` | Done, 0 errors |
| `ja-en` | `hidamari-ryokan` | 48 | `Forms` (verb/adj/noun) | 100% spoken Katakana | `ja-en` | Done, 0 errors |
| `ko-en` | `haessal-guesthouse` | 48 | `Forms` (verb/adj/noun) | 100% Revised Romanization | `ko-en` | Done, 0 errors |
| `zh-en` | `xiaoyuan-kezhan` | 48 | `forms: null` + measure words | 100% toned Pinyin | `zh-en` | Done, 0 errors |

## 3. Season 1 Independent Linguistic Audits & Fixes (2026-11-06)

- **ru, fr, it, de, ja, ko, zh** (auditor `05b94083`): 0 word-table errors and 100% `span`+`reading` coverage. Fixed: Korean honorific `지훈 님`, German `ʃt` compound IPA, Chinese `一楼`/`露出来` tones, Italian `camminare`, two French CNRTL URLs, and `learn/` single-`*` markup.
- **es, ar** (auditor `eeefbf03`): originality and dialect PASS, 0 `out/` leaks. Fixed:
  - Spanish: colleague-to-colleague `ustedes` → Peninsular `vosotros` in 6 scenes; `uy` IPA `uj`; imperative tags; 3 word-origin glosses.
  - Arabic: unvocalized homographs (`قبل` 'before', `بعد` 'after', `غير`, `بين`, `ترك`, `وعدت`, `بتعرف`). All 87 `-t` past verbs re-checked by context: 13 are 3rd feminine `-at` and 35 are 2nd masculine 'you'. Also: `-ak` when addressing men, construct-state `-it`/`-at` readings, imperative `تفضل`/`تذكر`, `توفى`, the `صبّح`/`بدأ`/`هم`/`شاء` tables, `طال`→`طوّل`, `آرمة` spelling, 7 repetitive narrator lines, and "we was" → "we were".
- **Dictionary examples:** removed 525 quotes from TV adaptations (`fr-en` had 524 from `dix-pour-cent`), 194 Spanish slot-filled templates and 170 Italian fillers. Replaced them with real dialogue lines from each show plus hand-written sentences, and re-synced every scene `lexicon{}`. Now 0 `out/` quotes and 0 templates in all 10 dictionaries, and every `learn/` citation points at an Originals scene.

## 4. Voices (2026-11-06)

All voices are synthetic (Qwen3-TTS VoiceDesign; Arabic through Chatterbox). Every reference clip passes Whisper CER ≤ 0.05.

| Voice | CER | median F0 | Voice | CER | median F0 |
|---|---|---|---|---|---|
| fr-f3 | 0.0 | 156 Hz | fr-m3 | 0.0 | 98 Hz |
| pt-f1 | 0.0 | 225 Hz | pt-m1 | 0.0 | 93 Hz |
| pt-f2 | 0.021 | 213 Hz | pt-m2 | 0.0 | 99 Hz |
| pt-f3 | 0.0 | 145 Hz | pt-m3 | 0.0 | 101 Hz |
| ar-f1 | 0.0 | 159 Hz | ar-m1 | 0.0 | 100 Hz |
| ar-f2 | 0.0 | 207 Hz | ar-m2 | 0.0 | 98 Hz |
| ar-f3 | 0.0 | 166 Hz | ar-m3 | 0.0 | 112 Hz |

Portuguese is now designed directly in Brazilian Portuguese. Arabic references use vocalized Jordanian text. Both sets replace the earlier shrill or English-speaking references that the owner complained about.

## 5. Multi-Season Authoring Summary (108 Complete Episodes / 864 Scenes)

- **English Master (`originals/_english/`):** Seasons 1–5 complete (`s01e01`–`s05e06`, 30 episodes / 240 master scenes).
- **Localized & Validated Episodes in `originals/<show>/` (108 episodes / 864 scenes):**
  - `ru-en` (`dvorik-u-mosta`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e06`), S3 (`s03e01`–`s03e03`) — **15 episodes (120 scenes)**
  - `fr-en` (`hotel-du-tilleul`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e06`), S3 (`s03e01`–`s03e02`) — **14 episodes (112 scenes)**
  - `es-en` (`posada-del-limonero`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `it-en` (`locanda-del-tiglio`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `pt-en` (`pousada-do-cajueiro`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `de-en` (`pension-sonnenhof`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `ar-en` (`bayt-al-yasmin`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `ja-en` (`hidamari-ryokan`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `ko-en` (`haessal-guesthouse`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e04`) — **10 episodes (80 scenes)**
  - `zh-en` (`xiaoyuan-kezhan`): S1 (`s01e01`–`s01e06`), S2 (`s02e01`–`s02e03`) — **9 episodes (72 scenes)**

## 6. Rendered & Released Audio Packages (`original-<episode>` on GitHub Releases)

Following strict 3-2-1 cycle priority (`3 RU -> 2 FR -> 1 ES -> 1 IT -> 1 PT -> 1 DE -> 1 AR -> 1 JA -> 1 KO -> 1 ZH`):

### Cycle 1 (13 / 13 Released — All 10 Languages Live)
1. `original-dvorik-u-mosta-s01e01` (`ru-en`)
2. `original-dvorik-u-mosta-s01e02` (`ru-en`)
3. `original-dvorik-u-mosta-s01e03` (`ru-en`)
4. `original-hotel-du-tilleul-s01e01` (`fr-en`)
5. `original-hotel-du-tilleul-s01e02` (`fr-en`)
6. `original-posada-del-limonero-s01e01` (`es-en`)
7. `original-locanda-del-tiglio-s01e01` (`it-en`)
8. `original-pousada-do-cajueiro-s01e01` (`pt-en`)
9. `original-pension-sonnenhof-s01e01` (`de-en`)
10. `original-bayt-al-yasmin-s01e01` (`ar-en`)
11. `original-hidamari-ryokan-s01e01` (`ja-en`)
12. `original-haessal-guesthouse-s01e01` (`ko-en`)
13. `original-xiaoyuan-kezhan-s01e01` (`zh-en`)

### Cycle 2 (13 / 13 Released — All 10 Languages Complete!)
14. `original-dvorik-u-mosta-s01e04` (`ru-en`) — Released
15. `original-dvorik-u-mosta-s01e05` (`ru-en`) — Released
16. `original-dvorik-u-mosta-s01e06` (`ru-en`) — Released (completes RU Season 1!)
17. `original-hotel-du-tilleul-s01e03` (`fr-en`) — Released
18. `original-hotel-du-tilleul-s01e04` (`fr-en`) — Released
19. `original-posada-del-limonero-s01e02` (`es-en`) — Released
20. `original-locanda-del-tiglio-s01e02` (`it-en`) — Released
21. `original-pousada-do-cajueiro-s01e02` (`pt-en`) — Released
22. `original-pension-sonnenhof-s01e02` (`de-en`) — Released (`8 scenes, 6,011 files, 81.2 MB`)
23. `original-hidamari-ryokan-s01e02` (`ja-en`) — Released (`8 scenes, 3,492 files, 64.2 MB`)
24. `original-xiaoyuan-kezhan-s01e02` (`zh-en`) — Released (`8 scenes, 742 files, 36.1 MB`)
25. `original-haessal-guesthouse-s01e02` (`ko-en`) — Released (`8 scenes, 3,770 files, 70.2 MB`)
26. `original-bayt-al-yasmin-s01e02` (`ar-en`) — Released (`8 scenes, 3,880 files, 61.7 MB`)

### Cycle 3 (In Progress on A100)
27. `original-hotel-du-tilleul-s01e05` (`fr-en`) — Released (`8 scenes, 6,929 files, 90.4 MB`)
28. `original-hotel-du-tilleul-s01e06` (`fr-en`) — Released (`8 scenes, 6,851 files, 91.8 MB` — completes FR Season 1!)
29. `original-locanda-del-tiglio-s01e03` (`it-en`) — Released
30. `original-pousada-do-cajueiro-s01e03` (`pt-en`) — Released
31. `original-posada-del-limonero-s01e03` (`es-en`) — Released
- `pension-sonnenhof-s01e03` (`de-en`), `bayt-al-yasmin-s01e03` (`ar-en`), `hidamari-ryokan-s01e03` (`ja-en`) — Rendering on A100

## 7. Hindi (`hi-en`) & English Target-Language Pairs (`en-es`, `en-pt` Pilot & Output-Contract Notes)

### 7a. Hindi Originals (`aangan-haveli`, `hi-en` — `spec/NEW-PAIRS.md` §1b)
- **Setting & Cast:** *आँगन हवेली* (*Aangan Haveli*), **Jaipur, Rajasthan** — natural everyday spoken Hindi (`बोलचाल की हिंदी`) in NFC Devanagari (`0` digits). Invented cast `kavya, pratap, diya, mohan, sudha, kabir, dev` — **0 collisions** across all 21 shows / 502 characters in `out/` and `originals/`.
- **Authoring & Learning Layer (Full Season 1 `s01e01`–`s01e06` COMPLETE — 48 scenes):**
  - 48 scenes (`s01e01`–`s01e06`) with 100% explicit `[start, end]` Devanagari spans + 100% reviewed ISO-15919/IAST vowel-length `reading` (`mms-uroman` `hin` verified across all 1,776 dialogue segments / 22,302 tokens).
  - `dictionary/hi-en.json` (**974 lemmas** with 5 Hindi verb tables, noun `Forms` + `gender`, inflecting `-आ` adjective `Forms`, postpositions, and 1,948 non-templated Hindi examples), `word-origins/hi-en.json` (**974/974 = 100%** sourced etymologies), and 10 `learn/hi-en/*.json` notes (`three-levels-of-you`, `postpositions-and-oblique-case`, `gender-and-agreement`, `numbers-prices-and-money`, etc.).

### 7b. English Target-Language Pairs (All 11 `en-<native>` Pairs Active — `en-es`, `en-pt` & `en-hi` Full Season 1 Complete, 8 Remaining Pairs at S1E1–E2 — `spec/NEW-PAIRS.md` §2)
- **Setting & Shared Dialogue:** *Linden Courtyard Inn*, 38 Linden Street, **Portland, Maine** (General American English + US spelling). Spoken dialogue lines across all scenes are 100% byte-identical across all 11 `en-<native>` pairs while all narrator lines, translations, word glosses/grammar tags, dictionary definitions/notes, word-origins, and `learn/` notes are written fresh in `<native>`:
  - **Full Season 1 (`s01e01`–`s01e06`, 48 scenes, 1,057 lemmas, 10 `learn/` notes each):** `en-es` (`originals/linden-courtyard-es`), `en-pt` (`originals/linden-courtyard-pt`), `en-hi` (`originals/linden-courtyard-hi`).
  - **S1E1–S1E2 (`s01e01`–`s01e02`, 16 scenes, 580 lemmas, 10 `learn/` notes each; `s01e03`–`s01e06` authoring in progress):** `en-fr` (`originals/linden-courtyard-fr`), `en-de` (`originals/linden-courtyard-de`), `en-it` (`originals/linden-courtyard-it`), `en-ru` (`originals/linden-courtyard-ru`), `en-ar` (`originals/linden-courtyard-ar`), `en-ja` (`originals/linden-courtyard-ja`), `en-ko` (`originals/linden-courtyard-ko`), `en-zh` (`originals/linden-courtyard-zh`).
- **Cast Collision Audit:** `hannah, graham, tessa, arthur, evelyn, caleb, owen` — **0 collisions** across all 21 existing shows in `out/*/cast.json` and `originals/*/cast.json`.
- **Synthetic Voices (Qwen3-TTS VoiceDesign -> Base, 0 real-person audio):**
  - `en-f1` (`CER=0.0`, median F0 `184 Hz`), `en-f2` (`CER=0.0`, `192 Hz`), `en-f3` (`CER=0.0`, `158 Hz`), `en-m1` (`CER=0.0`, `106 Hz`), `en-m2` (`CER=0.0`, `101 Hz`), `en-m3` (`CER=0.0`, `109 Hz`), `en-m4` (`CER=0.0`, `114 Hz`), `es-narr` (`CER=0.0`, `170 Hz`), `pt-narr` (`CER=0.0`, `196 Hz`).
- **Pronunciation & Word Tables:** 100% General American bare IPA in `stress` (`ˈmɔɹnɪŋ`, `ˈkɔfi`, `ɝb`, `θɹi`, `ðə`); 5-row English verb tables (`base / 3rd sg / past / past participle / -ing`), 2-row irregular plural noun tables, and 3-row irregular comparative adjective tables.

### 7c. Output-Contract Audit for Non-English Native Languages (`spec/OUTPUT-CONTRACT.md` -> App / Publisher Owner Notes)
All existing `-en` outputs remain 100% byte-identical. For `en-<native>` pairs (`en-es` pilot first), the app and publisher (`publish/rulisten_pub/`) should note the following contract conventions where English was previously assumed to be the sole native language:
1. **`show.json` (`title`, `summary`, `seasons[].title`):** Keyed by `{"<target>": ..., "<native>": ...}` (e.g. `{"en": "Linden Courtyard Inn", "es": "Posada del Patio del Tilo"}`). Both `"en"` and `"<native>"` are present on `en-<native>` shows, with `"en"` representing the target title/summary and `"<native>"` representing the learner's UI language.
2. **`cast.json` (`cast[].ru` and `cast[].en`):** Retains legacy field names `"ru"` (target-language display name, e.g. `"Hannah"`) and `"en"` (list of allowed narrator name tokens in `<native>`, e.g. `["Hannah"]`) for schema compatibility.
3. **`scene-NN.notes.json` & `dictionary/<pair>.json` (`meanings[].en`):** Retains literal property key `"en"` inside `lexicon.<lemma>.meanings[]` for schema/UI compatibility, while storing the `<native>` definition string (`es` in `en-es`, `pt` in `en-pt`, etc.). Likewise `lines[].trans`, `words[].gloss`, `words[].gram`, `meanings[].note`, and `examples[].trans` hold `<native>` text.
4. **`spans.json` & Published `transcript.lines[].lang`:** Narrator segments (`v == "narrator"`) now carry `"lang": "<native>"` (`"es"`, `"pt"`, `"hi"`, etc.) rather than `"en"`, while studied dialogue segments carry `"lang": "en"`. Any app/publisher filter that previously checked `line.lang != "en"` to mean "studied target line" MUST instead check `line.lang == pair.target` (or `v != "narrator"`).
5. **`learn/<pair>/*.json` & `word-origins/<pair>.json`:** `learn` articles store localized maps `{"<native>": "..."}` (`{"es": "..."}`, `{"pt": "..."}`), and `word-origins` stores `etymology` and `notes` in `<native>`.
6. **Future CJK Native Narrators (`en-ja`, `en-zh`):** In `spec/OUTPUT-CONTRACT.md` §2, narrator segments in `timing.json` tokenize by whitespace rather than `native_text` spans. On unspaced Japanese/Chinese narrator text, whitespace tokenization produces clause-level tokens rather than word-level tokens unless the app highlights narrator segments at sentence level (`spans.json`) or segments CJK narrator strings.
