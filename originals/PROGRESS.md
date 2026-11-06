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
