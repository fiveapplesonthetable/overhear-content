# German first-day taster: primary-source review

Scope: **one short excerpt from Die Discounter S01E01**, not a complete episode lesson. The story contains five statements by the new employee Titus. No other episode is processed or published by this change.

## Source identity and access

The retained private original is `die-discounter-s01e01.mp4`, 95,377,850 bytes, SHA-256 `96d5d542d9bb17daccea8548267f1e9f6f13cf56a06685313d989e789592aeea`, duration969.015147 s, 1280×720 AV1 with AAC stereo. Its container audio language is undetermined; the spoken language was independently detected from original audio.

Public source: [Die Discounter S01E01 — Der Anfang vom Ende](https://www.youtube.com/watch?v=hdrxW4ybh-Q), uploaded by **SdTvClips, an unofficial uploader**. This is not represented as an official upload. The [official Prime episode listing](https://www.primevideo.com/-/de/detail/0LV55BDXNNNCY90FG1OMZQGLM7?tr=at) independently identifies the series, the E01 title Der Anfang vom Ende, approximately16-minute runtime and new employee Titus. Source picture shows the correct supermarket and characters. No DRM, authentication bypass, source replacement or deletion was used.

`e01.de-orig.auto.vtt` is the downloaded native-language **automatic** caption track. `e01.de.srt` is its complete retained ffmpeg-format conversion, with original numbering and source-relative times; it is not an authored subtitle or a claim of a correct full-episode transcript. Rolling captions contain repetitions and occasional errors. The excerpt hash binds these actual retained SRT bytes. No German text was translated from English.

## Bounded original-audio evidence

An already-cached faster-whisper-small model independently transcribed original source86.3–98.3 s: CPU/int8, two threads, one worker, nice19, local-files-only, automatic language, no initial prompt, no hotwords, no expected transcript, no model/API/GPU use. It detected German at0.9868604541 and ran10.015 s. Exact raw evidence is private at `german-pilot/titus-native-asr.json` in the source-discovery directory.

It recognized these propositions directly from original German:

- Ja, ich bin Titus. Ich hab heute meinen ersten Tag hier.
- Die anderen kenn ich noch nicht so gut.
- Aber ich bin jetzt nicht hier, um Freunde zu finden.
- Ich bin eigentlich eher hier, um Geld zu verdienen.

The automatic captions mostly corroborate these statements but render Die anderen incorrectly as Die ander. The lesson uses the grammatical plural independently recognized from the original audio. This is original-audio/caption corroboration, **not human listening certification, exact time-alignment certification, or full-episode transcript approval**. Production must independently verify the native voice reference and synthesized lesson speech before publication.

## Cast and adaptation

The voice identifies himself as Titus. Original frames show the blond new employee in a gray-blue short-sleeved button-up shirt with a white undershirt and work badge. The source window includes cutaway pictures and another character near him; that does not change the speaker of the continuous introduction. The lesson makes no claim that every source frame is a single uninterrupted talking-head shot.

This is an explicitly simplified introduction. Line2 changes Ich hab heute meinen ersten Tag hier to Heute ist mein erster Tag hier: the intended first-day meaning is unchanged, and the possessive/ordinal endings change correctly with the new construction. Line3 expands spoken kenn to kenne and corrects the automatic-caption plural from original audio. Line4 omits jetzt. Line5 removes the conversational hedges ja, eigentlich and eher. Their removal makes the shorter beginner statement more direct; it does not change his stated earning-money purpose. The omitted Natürlich is not needed to pad the taster. The added farewell Tschüss is clearly lesson closing speech, not a source quote.

Every story line has a citation to an actual source fragment present both in that line and its cited source cue. No source cue ranges were broadened. The full-story replay is exact; all native segments, including the farewell and walkthrough replays, have translations and per-token notes. Notes include24 lemmas, relevant case/gender/number and verb forms, pronunciation, two original examples per lemma, and source-specific histories with uncertainty preserved. Names and grammatical relationships were checked in context: die is plural accusative before anderen; gut describes how well he knows colleagues; um and zu have their purpose-construction senses; Freunde finden naturally translates as making friends.

## Teaching and visual review

Five complete statements form an intentional compact taster; no invented filler is added to meet a whole-scene line target. The English narrator explains German through native replays. Only one of five explanations uses technical grammar labels. The rest teach meaning, contrasts, purpose and useful reuse in plain English. The strict teaching check reports80% of explanations as word teaching.

The illustration uses the app’s house-style contact sheet, not the source frames, as an image-model reference. Inspected the actual output: Titus’s short blond hair and button-up shirt, loading-bay setting, one character, no lettering, no logos. Final asset1024×1024 WebP.

Validation: `python3 tools/validate.py out/die-discounter/s01e01 --require-notes --strict-teaching` passes with0 errors; one expected warning records the deliberate five-line taster length. Metadata-only validation passes with0 errors. Generated-audio, word alignment and native pronunciation QA remain production gates; they are not claimed by this source review.
