# render: Overhear scene rendering

Turns every renderable scene of `overhear-content` into audio + word timing, locally, incrementally and unattended.
Target-language (ru) sentences: ESpeech-TTS-1 RL-V2 (F5, `settings.json ttsRu`, `espeech.py`, venv-f5). English narrator: F5-TTS v1 Base, 16 NFE (`settings.json ttsEn`, `f5en.py`, venv-f5). French and the pilot languages: Qwen3-TTS-12Hz-1.7B-Base (`tts{}`); Arabic: Chatterbox multilingual (`ttsAr`). Pick the language profile with `OVERHEAR_RENDER_SETTINGS` (repo README, "Settings per language").

```
overhear-content/out/<show>/sNNeNN/scene-NN{.json,.notes.json}
        │  content.py   light ingest; anything unrenderable becomes a Skip with a reason (never aborts the run)
        ▼
pipeline.py (system python, no torch)   plan: render key per scene, priority queue, state, --status
        │  one process + one gpurun VRAM reservation per step per scene (steps of different scenes overlap)
        ├─ stage.py synth   gpurun 4800  Qwen3-TTS-12Hz-1.7B-Base ICL clone, per-sentence cache      (tts.py)
        ├─ stage.py finish  gpurun 1500  MMS_FA align → stress check → loudness/assemble → mp3 → store (align.py, stresscheck.py, audio.py)
        └─ stage.py retake  gpurun 4800  only when the stress check flags sentences: other seeds/temperatures; best take kept
        ▼
$OVERHEAR_HOME/render-store/<sceneId>/{audio.mp3, spans.json, timing.json, report.json, meta.json}   ← publisher ingests this
```

## Files
| file | role |
|---|---|
| `pipeline.py` | CLI: `--changed` (the timer), `--episode/--scene/--show/--season`, `--status`, `--dry-run`, `--force`, `--limit`, `--max-minutes`, `--retry-failed`, `--pull` (off by default: the content checkout belongs to the content agent) |
| `stage.py` | one GPU step of one scene (`synth`, `retake`, `finish`) |
| `voices.json` | the voice pool: key → reference clip + transcript + language + gender |
| `casting/<show>.json`, `casting.py` | **character → voice, persisted in git**, append-only. Built from `overhear-content/out/<show>/cast.json` by gender; distinct voices within shared scenes where the pool allows; `designedFor` pins a voice-lab voice to its character. Edit by hand to re-cast (scenes re-render by themselves). Scripts carry no `voices` map (contract P-1) and there is no fallback to one |
| `refs/*.flac`, `refs.plan.json` | the cloned-voice references (provenance in voices.json) |
| `settings.json` | everything that changes audio (model, LoRA switch, stress policy, loudness, gaps, retake budget, GPU reservations, priority order) |
| `content.py`, `plan.py`, `store.py`, `voices.py`, `config.py` | ingest, render key, store/state, voice resolution, paths |
| `textprep.py` | sentence split (the content's regex) and stress injection (`stress` fields only; RuAccent for uncovered homographs) |
| `tts.py`, `align.py`, `stresscheck.py`, `audio.py`, `render_scene.py` | the stages |
| `bench.py/.sh`, `smoke.py/.sh`, `asr_cer.py`, `listen_page.py` | throughput, smoke test (CER via Whisper), ear-check page |
| `tests/` | pytest (`tests/run_all.sh`); GPU tests are the smoke/bench scripts |

## Incremental by content hash
A scene is up to date when `<store>/<id>/meta.json.renderKey` equals
`sha256(contentHash, tts signature (model, dtype, sampling, LoRA tag, stress policy), assembly signature, [voice, refVersion] per role)`
where `contentHash = sha256(script bytes + notes bytes)` and `refVersion = sha256(ref clip bytes + ref text)[:8]`.
Edit a scene → only that scene re-renders; change one voice's reference or casting → only scenes using it. Sentences are cached at
`cache/tts/<sha256(signature, voice, refVersion, language, text)>.flac`, so repeated lines (the second story pass, replays) are synthesised once.
Failures are kept in `state.json` (3 attempts per render key, then blocked until the inputs change or `--retry-failed`).

## Stress
Russian marks come only from the notes' `words[].stress` (U+0301). Policy (`settings.json stress.policy`): `auto` = `all` with the LoRA, otherwise
`homographs` (marks only on RuAccent homograph forms: the base model garbles text with a mark on every word, WER 0.84 in the qwen-ft eval).
Tokens the notes do not cover go through RuAccent (separate venv, cached). The LoRA is `settings.json lora.enabled` (default **false** until run 4 is judged;
`local` path wins over the HF repo `zimuzostanley/qwen3-tts-ru-stress-lora`).
Check: MMS_FA vowel durations (duration-only, the best feature in `stress-check/auto/summary.md`); in-scope words (homographs) whose longest vowel is not the intended one
(ratio ≥ 1.25) flag the sentence. Flagged sentences get up to `stressRetry.attempts` local retakes (other seeds / temperatures); the best take is kept (and stays cached).
Still-flagged sentences are listed in `report.json.stress.unresolved` and counted per scene.

## Output shapes
* `spans.json` (publisher `render_source.py` shape plus extras): `{version, sceneId, sampleRate, durationSec, segs:[{seg, start, end, nextStart, v, voice, lang, sentences:[{i, start, end, text, engine}]}]}`; seconds in `audio.mp3`, sample exact by construction (decoded mp3 length checked within 50 ms).
* `timing.json`: `{"<seg>": [{t, s, e, ok, why}]}` for every segment (narrator too), one entry per publisher token (`tokens.tokenize`: whitespace tokens with a letter or digit); `ok:false` (`missing`, `zero-length`) carries interpolated times. Nothing else at the top level (the aligner is in `meta.align`).
* `report.json`: stress counters + unresolved sentences, retakes, timing not-ok count, loudness.
* `meta.json`: `renderKey, contentHash, contentCommit, tts{model,lora,stressPolicy}, voicesVersion, voices{role:{voice,refVersion}}, align, pipelineVersion, renderedAt, durationSec, audioSha256, ...`.
* Audio: 24 kHz mono, per-sentence −20 LUFS, uniform 20 ms edges, constant-gain master to −16 LUFS, peak limiter −2 dB, 96 kbps LAME with Xing/LAME tag (gapless).

## Runbook
```
python3 -I pipeline.py --status                      # done/pending/failed/skipped, measured rate, ETA
python3 -I pipeline.py --episode kukhnya-s01e01      # render one episode
python3 -I pipeline.py --scene kukhnya-s01e01-scene-02 --force     # re-render one scene
sh smoke.sh /tmp/smoke ; sh bench.sh /tmp/bench      # GPU smoke (CER) and throughput
tests/run_all.sh                                     # unit tests
```
Re-casting a character: edit its `voice` in `casting/<show>.json`. New reference clip: replace `refs/<key>.flac` and its `text` (refVersion changes by itself).

## Russian engine (ESpeech)
`settings.json ttsRu` switches Russian sentences to ESpeech-TTS-1 RL-V2 (reference-cloned from `voices.json`, batched per voice, `espeech.py`).
* Sentence cache keys for `lang == ru` hash **only `ttsRu`** (`config.sentence_signature`), not `tts{}`: changing the English/narrator engine never invalidates Russian audio, and Russian can be pre-rendered ahead of the scene render.
* `stage.py synth-ru` (venv-f5, `gpu.ruMiB`) fills the scene's missing Russian sentences (instant when cached), `stage.py synth` then does the rest with Qwen; `retake` uses ESpeech for Russian (other seeds). `pipeline.py` runs `synth-ru` -> `synth` in lane A.
* Text for ESpeech: RUAccent on the sentence, with the notes' homograph stress winning. Duration is F5's bytes-ratio rule / speed; implausible lengths retry at slower speeds.

## English narrator engine (F5-TTS v1 Base)

`settings.json ttsEn` (model `F5TTS_v1_Base`, `nfe` 16, cfg 2, sway -1) is the narrator default; `f5en.F5EnEngine` subclasses the ESpeech engine (same batched sampler, `generate`/`synth_many`/retake interface), clones the voice's `voices.json` reference, English text as written.
* Cache keys for `lang == en` hash **only `ttsEn`** (+ voice, ref version, text); French keys ignore it, Russian keys ignore it. `render_key` includes it.
* `stage.py synth-en` (venv-f5, `gpu.enMiB`, batch `tts.batchEn`) fills English sentences; `stage.py missing` (no GPU) lets `pipeline.py` skip the `synth-ru` / `synth-en` / `synth` reservations that have nothing to do; `retake` picks the engine per language.
* `ttsEn.refTrim = {voice: {seconds, text}}` shortens the reference prompt (cheaper per step). Measured on the 33-sentence narrator set (shared GPU): 5.8 s trim = -19% wall but WER 9.2% -> 10.6% (4.7 s: 14.3%), so it is off by default.
Re-casting a character: edit `casting/<show>.json`. New reference clip: replace `refs/<key>.flac` and its `text` (refVersion changes by itself).

## Example clips (audio for the lexicon's written examples)
`clips.py`, `clip_asr.py`, `stage.py clips`, lane C of `pipeline.py`. The sentences a scene's notes write for a word (`lexicon.*.examples[].text`)
get one clip each, `<store>/clips/<id>.mp3` + `<id>.json`, `id = sha256(pair NUL text)[:16]` (the publisher derives the same id). Voice: one neutral
reader per language, `settings.json clips.voices` (`ru-f1`, a calm hostess, for Russian; `lucie` for French). Same Qwen3-TTS, stress policy (RuAccent for
homographs), sentence cache and scene mp3 format as scenes; per-sentence -20 LUFS, then the clip is mastered to -16 LUFS with 80 ms of silence at each end.
Check: Whisper large-v3-turbo CER against the text as written <= `clips.cerMax` (0.15); a failure is re-synthesised with another seed/temperature up to
`clips.retakes` (2) times, then recorded as `status: failed` (no mp3, the app shows no speaker icon; retried only when its inputs change).
A clip is current when `ckey` (its sentences' tts cache keys + assembly settings) matches. After each scene renders, lane C batches the scenes
that have finished (up to `clips.scenesPerRun`, 2: a group holds the GPU for ~10 minutes, so the scene lanes interleave) into one low-priority (`GPURUN_PRIO -1`) Qwen step and one Whisper step, so scene lanes are served first.
`pipeline.py --clips-only` backfills the already rendered scenes without taking `pipeline.lock`; `--no-clips` turns the stage off. A `clips.lock` keeps
two clip runs from overlapping. RuAccent runs once, on the CPU, before any GPU reservation is taken.

## Form clips
`forms.py` plans audio for the written table cells, with slot identities shared with the publisher.
Russian forms use `ru-f1` with the Russian stress LoRA; French forms use `lucie` on base Qwen,
with a maximum batch of four. Forms in ar, hi, ja, ko and fr are judged by sound, not spelling (`form_gate.py`; its `GATE_VERSION` makes failures of an older gate stale; see `FORM-GATE-FIX.md`). A mixed-language forms stage loads each model configuration separately.
French shared subjects such as `il/elle est` are read as complete alternatives (`il est, elle est`).
Unexplained parentheses and bound elisions are held for review instead of producing misleading audio.
The ASR comparison uses the declared spoken alternatives, with the same CER gate; Russian numeral
expansion, vowel folding and forced-score exceptions do not apply to French.

Form plans and review files are shared across languages. A selected run replaces only its own current
slots and preserves all other records, including checked Russian clips. Adding a new voice does not
change another language's cache keys. All production runs still require serialization through
`forms.lock`; scene-only renders can pass `--no-forms` while a separate forms batch is managed.

## Voices (pool in `voices.json`)
Male Russian voices do not exist among the old ElevenLabs clips, so the male pool and three extra female voices are the voice-lab's synthetic VoiceDesign voices (no show audio); the rest are cloned from the old ElevenLabs clips with their exact transcripts.
| key | lang | gender | designed for | length | source | reference transcript |
|---|---|---|---|---|---|---|
| `alisa` | ru | f |  | 7.8 s | old ElevenLabs clips (ru-podcast/cache): `2abff6f03d3c61d7.mp3`, `8bfcf04610e645df.mp3`, `23c9c7cff482038a.mp3` | Хорошо, шеф. Я всегда знала, что буду поваром. Сегодня у подруги день рождения. |
| `anja` | ru | f |  | 9.25 s | old ElevenLabs clips (ru-podcast/cache): `f80b745fc5453782.mp3`, `6aa7bd5d6a8c8723.mp3`, `a1dc388f4733f978.mp3` | Сегодня обед для персонала готовит Аня. Я тоже иду туда. Сегодня у Кати день рождения. |
| `angelina` | ru | f |  | 6.78 s | old ElevenLabs clips (ru-podcast/cache): `8f09d27c95a9fc6f.mp3`, `c035ed60633bff98.mp3`, `41151c07883270e6.mp3`, `822534217c4645f4.mp3`, `224b8a952231ed13.mp3`, `aed2449ec8d30307.mp3` | Ты, главное, не торопись. Давай ещё разок. Не переживай. Подвинься. Ладно. Что? |
| `ru-m1` | ru | m | max | 8.24 s | voice-lab VoiceDesign take `max_t4.wav` (synthetic) | Привет, я только вчера приехал в Москву из Воронежа. Работа мечты уже рядом, и я сегодня невероятно счастлив. |
| `ru-m2` | ru | m | barinov | 10.08 s | voice-lab VoiceDesign take `chef_pp.wav` (synthetic) | Слушайте меня внимательно, инвалиды. Сегодня в зале сидит очень важный гость, и я не хочу слышать ни одной жалобы. |
| `ru-m3` | ru | m | kostya | 7.04 s | voice-lab VoiceDesign take `kostya_t2.wav` (synthetic) | Макс, ты можешь жить у меня сколько захочешь. Только, пожалуйста, не трогай мои бутылки на барной стойке. |
| `ru-m4` | ru | m | senya | 9.2 s | voice-lab VoiceDesign take `senya_t2.wav` (synthetic) | Тише, тише, не шуми. Я принёс отличный кусок мяса, только шефу об этом знать совсем не обязательно. |
| `ru-m5` | ru | m | fedya | 7.76 s | voice-lab VoiceDesign take `fedya_t3.wav` (synthetic) | Когда я служил на флоте, я каждый день готовил рыбу для всей команды. Такую уху ты нигде больше не попробуешь. |
| `ru-m6` | ru | m | lyova | 8.48 s | voice-lab VoiceDesign take `lyova_t4.wav` (synthetic) | Простите, шеф, я всё проверил два раза. Я думаю, что сегодня на кухне всё будет хорошо, правда. |
| `ru-m7` | ru | m | nagiyev | 9.76 s | voice-lab VoiceDesign take `nagiyev_t2.wav` (synthetic) | Друзья мои, этот ресторан носит моё имя. Поэтому здесь всё должно быть просто идеально, и даже лучше. |
| `ru-f1` | ru | f | vika | 7.84 s | voice-lab VoiceDesign take `vika_t3.wav` (synthetic) | Добрый вечер, ваш столик уже готов. Пожалуйста, следуйте за мной, я покажу вам лучшее место в нашем зале. |
| `ru-f2` | ru | f | nastya | 9.84 s | voice-lab VoiceDesign take `nastya_pp.wav` (synthetic) | Пожалуйста, не выбрасывайте эту еду. Рядом на улице живёт человек, и ему сегодня очень нужен тёплый ужин. |
| `ru-f3` | ru | f | ainura | 7.68 s | voice-lab VoiceDesign take `ainura_t2.wav` (synthetic) | Не ругайся, сынок, кушай лучше. Хороший человек всегда найдёт дорогу домой, и на кухне тоже. |
| `sky` | en | f |  | 8.08 s | old ElevenLabs clips (ru-podcast/cache): `aa148b7095764097.mp3` | When you watch the second episode, listen for the chef asking where his knife is, and for the one word he shouts when he's in a hurry. |
| `lucie` | fr | f |  | 9.02 s | old ElevenLabs clips (ru-podcast/cache): `49edbef6db86fcdc.mp3`, `e85aa402bc646ecc.mp3`, `60c1c0f720921cec.mp3`, `25712cbb1771b8cb.mp3` | Je suis un peu stressée. Il est dix heures. De rien. Je réserve la salle de réunion. |
| `emilie` | fr | f |  | 5.03 s | old ElevenLabs clips (ru-podcast/cache): `ca908e38712be30f.mp3`, `9992cb6883b1e275.mp3`, `8879fb627f710cc1.mp3`, `9e06f248784cef7d.mp3` | Moi, c'est Arlette. Allez, c'est l'heure. Ce n'est pas un problème. Bienvenue parmi nous! |
| `theo` | fr | m |  | 11.94 s | old ElevenLabs clips (ru-podcast/cache): `ec58b31b30d1f2bd.mp3`, `602e470b2d61a537.mp3`, `14fbab0d1c10a094.mp3`, `b9fe653d1c94b0c6.mp3`, `37244f8a6a15a962.mp3`, `26c1813b483c72c6.mp3`, `c4d116506c68e142.mp3`, `0ce4041d2aba68d7.mp3`, `cdd75cc8a9c47d65.mp3`, `32e0ecf772a911ea.mp3`, `c0e3f242b71e9cfd.mp3` | Ça va, mais je suis en retard. Tu es géniale, Léa. Un café, peut-être? Dis-lui d'attendre. Je n'ai pas le temps. C'est Gabriel. Merci de ton aide. Quelle heure est-il? Quelqu'un m'a appelé? Bonne journée! Léa? |
| `marcel` | fr | m |  | 8.73 s | old ElevenLabs clips (ru-podcast/cache): `4bc4f699b579fc40.mp3`, `06d6266b84ddfced.mp3`, `c8a1149394551f40.mp3`, `1d8cbb9123919958.mp3`, `ddfb239abcef075d.mp3` | C'est avec Madame de Serisy. Ça va être une belle journée. Et deux cafés, s'il vous plaît. Demain, dix heures. Je ne sais pas encore si elle vient. |

New voices for a language: see `../spec/voices.md`. Never clone a voice from show audio.

## Throughput on the A100
`sh bench.sh` measures RTF per batch size. On an A100 40 GB raise `tts.batch` and the gpurun reservations (`GPURUN_BUDGET_MIB=38500`)
until RTF stops improving, run several scenes' steps concurrently, and keep Whisper CER on `sh smoke.sh` unchanged.
Record what you measured in `out/PROGRESS.md`.


## Narrator method B: Russian words in narrator lines (`narrator.py`, settings `narratorRu`)
The narrator (F5, sky) used to read the Latin transliteration of Russian words ("Spasibo za") in an English accent. Now every narrator
sentence that contains Russian words is spliced from parts: English runs by F5/sky as before, each Russian word or phrase in Cyrillic by
Qwen3-TTS 1.7B + the run3 stress LoRA in `ru-f1` (the narrator-specific `narratorRu.lora`; the global `lora.enabled` is untouched), parts
150-250 ms apart and levelled to the sentence they replace. Sentences without Russian are never touched.
* Finding the Russian: a double-quoted Latin run is Russian only if every word resolves to a Russian word the content already has (the
  scene's dialogue, notes words, lexicon forms and examples, then the episode's, then the show's). Matching is STRICT first (`narrator_ru.py`:
  я=ya, ь=', ъ='', ы=y, ий=iy, ый=yy, х=kh ...; a never matches я, gotovit' never matches готовит); then the same without soft/hard-sign marks before
  vowels and with the loosely written endings (-ie, -ye, -ii, -y) read strictly; only then a loose key (ye~e, y~i, no apostrophes, doubled letters).
  Several candidates are narrowed by the Russian words of the dialogue quote the sentence is about (the notes line whose translation the
  sentence quotes, else the nearest earlier Russian line). Still several = AMBIGUOUS: nothing is picked by stress or length, the whole line
  keeps its old sky audio and the run is listed (scene, Latin, candidates) in the plan's `unresolved` / `skipped`. A quote that is only partly
  known does the same. A quote with no match at all ("unknown": mostly English glosses, typos) is listed but does not block the line.
  English glosses are decided per word: the scene's English words, the show's line translations and Russian-looking English phrases ("to
  shake", "oh, come on") are vetoed unless the dialogue quote has the word or the spelling is only a transliteration's (spat', zh, kh, yy ...).
  Fragments like "-sya" are never voiced. Cyrillic is never guessed.
* Stress is automatic (`narratorRu.stress`: `all` = content stress, then RuAccent for the rest; `content`; `none`): the stressed form from
  notes/lexicon when the content agrees with itself, a homograph (several stressed forms in scope) takes the scene's form or goes to RuAccent
  with the dialogue sentence as context, and is listed in `<work>/homographs.json`. Monosyllables get nothing. No hand marking.
* Check: every part is Whisper-checked (Russian runs as Russian, English as English); failing parts get `takesPerRound` more takes, up to
  `rounds` rounds. A line with a part that never passes keeps its old audio; the failure goes to `<store>/narrator-failures.jsonl` (not on a
  `--out` dry run) and is remembered in `<work>/failed.json` per render key, line and version: later runs skip it (no GPU time) until
  `--retry-failed` or a version bump. Takes of one part never share a seed or temperature.
* Splice: every run builds from the scene's ORIGINAL render, kept in `<store>/.narrator-before/<id>/` and keyed to its renderKey (refreshed when
  the scene was re-rendered; a narrated scene without a valid original is left alone), and re-applies all of its lines, so a version bump or a
  changed word never stacks mp3 generations. The decoded file is `ENC_LAG` (119) samples later than `spans.json`; cuts are made on that timeline,
  at a near-silent point of the gap next to each sentence boundary, with an 8 ms equal-power crossfade at both joins (`crossfadeMs`). The result
  is encoded once. The scene's mp3 generation loss (about 0.45 LU) is given back as one uniform gain, clamped to +-1 dB. Then the length
  and the word-time monotonicity are checked, and each replaced line must come out within `lineLoudnessTolLU` = 1.5 LU of the audio it
  replaced; a line that does not keeps its sky audio (remembered as failed for that line) and the scene is built again without it. A take
  that needs more than `maxGainDb` (12) of gain or more than `maxLimiterDb` (3) of limiting to match its line fails that line. Scene-wide
  problems (word times) leave the scene as it was; the second time for the same render and version they are remembered too. Lone
  loose-key (tier 3) transliteration matches are taken only for words of 5+ letters or the allowlist (`nyet`, `tsar`); shorter ones keep sky.
  Word times come from the part offsets (Russian words share their part by syllable weight), later spans and words shift by the length
  change, and the segment's timing tokens must equal the sentences' tokens exactly.
* Content: the content checkout (`OVERHEAR_CONTENT` / `--content`) must be the one the scenes were rendered from: the sha256 of each scene's
  script and notes is compared with the scene's `contentHash`, and a difference aborts the run before any work (`ContentMismatch`).
  `narrator_batch.sh` requires `OVERHEAR_CONTENT` to be set explicitly.
* Locks: the narrator pass holds `pipeline.lock` (`--narrator-only` takes it like a render run and exits 75 when a run is active; the
  pipeline's own post-pass already holds it; `--dry-run` takes none), a flock on the work dir (one run per `<store>/cache/narrator-<version>`),
  and for each scene's commit the publisher's `publish.lock` (`OVERHEAR_PUBLISH_LOCK`, default `$OVERHEAR_HOME/render-store/publish.lock`; plain flock(2),
  exclusive, waits up to `publishLockWaitSec` (3600, as long as the publisher's own wait), then skips the scene for the next run). Inside it the live scene's renderKey and audioSha256 are
  compared with what the build started from; a scene that changed meanwhile is not committed. `Store.commit_scene` swaps the directory
  atomically (`renameat2` RENAME_EXCHANGE) so the publisher's per-scene symlinks never dangle.
* Use: `python3 pipeline.py --narrator-only --scene ID[,ID] | --episode E | --season 1 | --all [--dry-run] [--retry-failed]` (or `narrator.py ...`).
  A normal run applies the pass to the scenes it renders (`--no-narrator` skips it); the outcome of a pass (lines, scenes, failures, error) is in
  `state.json` and shown by `--status`. It does not enter the render key.
* Steps (each its own process under gpurun, nice 19, `taskset -c 36-39`): `narrator_work.py en` (F5, venv-f5), `ru` (Qwen + LoRA), `check`
  (Whisper, ASR venv), `build` (splice, CPU). Parts are content-addressed and cached in `<store>/cache/narrator-<version>/`, so a re-run only makes what is missing.

## Native lexical units (Japanese, Mandarin, Korean, Arabic)

Install the small CPU normalizer in the finish environment with
`pip install -r requirements-alignment.txt` (`uroman==1.3.1.1`). This does not
install model weights. Native MMS targets carry explicit authored word owners.
Japanese/Mandarin annotations require exact half-open code-point `span` values
and reviewed kana/contextual pinyin `reading`; Korean/Arabic may use reviewed
readings or uroman's graphemic whole-context edges. The original written source
is never spaced, romanized or reordered for display. A compound's reading owns
its whole lexical span, not fabricated intervals for its individual characters.

Native `word_times()` aggregates actual CTC target intervals directly. Missing
words, unsupported targets/numbers, target-count mismatch, ownership crossing
selectable words, invalid bounds and overlap stop the render. Legacy RU/FR/EN
character alignment and onset adjustment stay unchanged. Native intervals do
not use those onset/end extensions or interpolated placeholders. Confidence is
recorded for diagnosis; it does not prove pronunciation or calibrated boundary
quality. Production must perform independent native synthesis and acoustic QA.

Timing rows retain `span`, `confidence`, and the normalization convention;
`meta.nativeAlignment` identifies the same convention. Reading/segmentation and
normalizer version enter native cache keys. The publisher requires complete
matching native timing and emits exact `charStart`/`charEnd` code-point ranges
for words and translations, plus optional index word-span arrays. It rejects
old/incomplete native timing instead of proportional fallback. Newly served
native content must be gated on an app supporting these ranges.

## Cached Arabic synthesis

`ttsAr` selects `chatterbox_ar.ChatterboxArEngine` for the separate `synth-ar`
stage, run in `OVERHEAR_VENV_AR` (default `$OVERHEAR_HOME/venv-asr`). Set
`modelLocal` to the complete cached multilingual V2 snapshot, `model` to
`chatterbox-multilingual-v2`, and optionally `temperature`, `cfg_weight`,
`exaggeration`, `repetition_penalty`, `min_p`, `top_p` and `sentence_retries`.
`gpu.arMiB` controls its reservation, falling back to the ordinary TTS budget.
The adapter uses `from_local`, disables downloads, requires a real reviewed
Arabic reference, passes `language_id='ar'`, and keeps the common 24 kHz cache
format. It never pads/repeats reference speech. Arabic engine settings have their
own sentence fingerprint and do not invalidate Russian/French/English caches.
Only the sole production GPU owner may initialize a model or run speech trials.
Saudi dialect and pronunciation are QA requirements, not claims made by the
backend's language flag.

Original show clips remain **private**, including extracted speech embedded in
teaching MP3s. `sourceAudio` is private verification metadata only: the public
renderer and publisher reject it, and reject explicit original-source render
provenance. Final public native dialogue uses independently validated synthesis;
original clips may guide private verification and voice conditioning.
