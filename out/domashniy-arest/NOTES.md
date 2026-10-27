# domashniy-arest: notes and decisions

## Show-wide
- Names follow the subtitles: the hero is **Аркадий Борисович Аникеев**, the **mayor** (мэр) of Синеозерск
  (cue 113: "four years as mayor"; cue 593: "задержан мэр города ... Аркадий Аникеев"). The task brief called him
  "Ankudinov, deputy mayor"; the sidecar is authoritative, so he is Anikeev, the mayor, and Pasha is his deputy.
  The subtitles are machine transcriptions with some garbled names (Аникеев / Ганекеев / Никеев, Синеозерск /
  Синей Озерск / Синьозерский, Аракелян / Рокелян / Саракелян); scripts use the standard forms Аникеев,
  Синеозерск, Аракелян. Fragments in `source.lines` are always copied from the cue as written.
- Protagonist key `anya` (voice alisa, female) = the viewpoint character. Arkady is the viewpoint character in every
  scene he is in (child or adult), with `LABELS["anya"] = "Аркадий"`; where he is absent the scene's viewpoint
  character takes `anya` and `LABELS["anya"]` names them. `tools/compose.py` hardcodes the display label "Аня" for
  `anya` in REVIEW.md only (we may not edit tools); the scene JSON `labels` are authoritative.
- Grammar follows the character, not the voice: Arkady's lines are masculine (я родился, я вырос, я рад) even though
  the protagonist voice is female.
- Other roles use descriptive keys (`samson`, `nina`, `pasha`, `vika`, `marina`, ...) with voices anja/angelina, at
  most two besides `anya` per scene (each role needs its own voice).
- The source is very crude (constant swearing, a humiliating "kiss my backside" deal, sex talk, a flooded toilet).
  Story lines never contain obscenities or sexual content: the plot is kept true but retold cleanly; the narrator
  mentions the humiliating deal neutrally ("a humiliating condition", "a silly, humiliating kiss"). Slang and
  abbreviations from the cues (пучком, бабки, мент, СИЗО, СМУ...) are replaced with plain A1 words.
- Child Arkasha (flashback) and adult Arkady share one look link: round glasses (the bully calls him "очкарик").

## s01e01
- Episode title: not given in the sidecar (the series' episodes are numbered, not named): `title: null`.
- 28 scenes in scenes.json; merged: 10 (Arkady on the phone planning City Day, a monologue with no second
  speaker, `next` into 11), 23 (the Samsonovs admire the Cayenne and Vika takes the keys back, `next` into 24),
  28 (Nina complains on the phone + closing song, `prev` into 27).
- Opening song (cues 1-9) is inside scene 1; closing song (1070-1093) inside merged scene 28.
- Scene 15: Arkady is absent; Samson is `anya` (label Самсон), the TV newsreader is a voiced role (`newsreader`,
  Диктор). Cue 588 ("even a kid knows") is unattributed in the subtitles; given to Nina. Yulia has no voice.
- Scene 16: the two prison-service officers are one role; cue 619 ("door behind the wardrobe") given to the old
  neighbour (speaker unclear); the officer's joke at 645 and the detention-centre threat are left out.
- Scene 17: "личный раб" (personal slave) retold as "личный слуга" (personal servant), which also sets up the
  "servant of the people" line.
- Scene 5: the caller is a woman (feminine «сама», cue 200) whom Arkady calls "Виктор Степанович" so that Vika
  thinks it is an official; role `caller` with that label. Innuendo («с собой») and the crude cue 208 left out.
- Scene 6: the secretary's name is garbled as «Олегия Алексеевна» in cue 216; scripts use Лидия Алексеевна (cues
  324, 353, 455). Golovamzyuk (cue 262) and Nikolai Filippovich (cue 280) are the same boss. The stress
  Головамзю́к is a guess (garbled surname).
- Scene 21: "Я тебя закопаю" -> "Ты ещё пожалеешь!"; бабки -> деньги, кинул -> обманул; "Тихо, тихо" (cue 849,
  speaker unclear) given to Pasha.
- Scene 22: "любовники" -> "вместе"; "козёл" -> "ужасный человек"; the sex lines 893-897 are left out.
- Scene 24: Samson tearing off the pipe and the flood are told by the narrator plus a new line ("Ваня, вода!");
  the crude cues 933-934 are replaced by Arkady's refusal. Garbled «Спана» -> «Спа», «общательный» -> «общий».
- Scene 25: cues 970-974 read as Arkady showing the old neighbour (вы) how to hold the latchless toilet door shut;
  she has no voice (role limit), her sarcastic thanks are narrated. «ЗАГС» dropped from Nina's line.
- Scene 26: "Очень плохая водка" (speaker unclear) given to Arkady; cue 1016 «мы все воры» -> «Вы все воры» (Samson
  means the officials); the "bloodsucker" line and crude cues 1003/1014 left out; the governor anecdote narrated.
- Scene 27: merged scene 28 (Nina's phone complaint + closing song) is covered in the OUTRO.
- Lexicon: «должен» is entered as adj with a "Short forms" table (no long forms); «нужный» has full declension plus
  short forms in moreForms.
- Samson's art look: most generated pictures give him a short stubbly beard, so characters.md now says so.
- Scene 7: the demand is retold as "Поцелуй меня" (only the clean part of cue 298 is cited); the narrator calls it
  a crude, humiliating kind of kiss. "Через трусы" (313-315) and Samson's swearing (303) left out.
- Scene 8: the sex talk (363-371) is skipped (narrated as teasing); lines reordered so the greed line answers
  "we're in business" and cue 362 is the punchline.
- Scene 9: Arkady absent: Nina is `anya` (label Нина), Samson anja, Yulia angelina. "Тише" (378, speaker unclear)
  given to Nina. Стояк -> труба; misheard «беде» -> «биде»; "Про гугли узнаешь" -> "В интернете посмотри".
- Scene 18: cue 716 ("Всё, что захотим, говоришь?", speaker unclear) given to Nina; Arkady's crude refusal (706)
  -> «я это делать не буду»; repair orders 699-702 summed up as «чинить трубу».
- Scene 19: «Немец / Бэха» -> «Немецкая (машина)»; «мне» in cue 772 is a transcription slip for «меня»; «А мне
  что?» (774) given to Samson.
- Scene 20: the car is spelled «Кайен» (Porsche Cayenne); the cues have «каен/Каен» and the mistranscribed «На
  колене» (792), so that line is uncited. Pasha only mentioned (role limit).
- Scenes 1-2 (flashback): the child Samson's role key is `samson` but its label is "Ваня" (he is little Vanya
  there); in scene 1 it uses voice angelina because the father (`father`, Отец Самсона) has anja. The dunking is
  told only by the narrator; the taunt "очкарик" (four-eyes) is kept as mild schoolyard language (the cues spell it
  «очканак/очканав», so it is not cited). Cue 27 ("Как там в Венгрии?", a neighbour) is given to Arkasha; the adult
  who says "Уроки учи" (66) is not identified. «Мафон» -> магнитофон, «валюты» -> денег, «Это НЗ» -> «Это моё».
  Cues 76-82 (an adult shouting for a broom) are unclear and left out.
- Scene 3: the reporters are one role (`reporter`, Журналистка). «процветал» -> «люблю наш город»; «выдвигаю свою
  кандидатуру» -> «иду на второй срок». Town name stress Синеозе́рск (by analogy with Белозе́рск).
- Scene 11: the "kiss" never appears in a story line; it happens off stage and the narrator names it neutrally.
  Lines 8-9 ("вы всё видели?" / "Всё видела") are clean stand-ins for cues 463-464. Merged scene 10 (City Day plans)
  is told in the bridge.
- Register follows the source: Arkady says ты to Arakelyan (who says вы); the dean says ты to Marina, Marina says
  вы (her switches to ты at 536/553 are normalised to вы).
- Scene 13: Arkady absent: Marina is `anya` (label Марина). "I love you" (550), "Идите к черту" and the secretary
  Lena Viktorovna left out. Scene 14: «Ара» (an ethnic nickname) dropped; "в особо крупных размерах" -> "очень
  большую взятку"; Arkady's "Что? За что?" is new.
- The image generator hit quota (429) errors several times during the run; retries worked.
- Name lemmas (pos "name") are lowercase in all notes files, following spec/annotations.md ("lemma ... lowercase").
  Аникеев is stressed Анике́ев (uncertain, as is Головамзю́к).
- Validator: `OK: 0 errors, 19 warnings`. All 19 are "gap between scenes" warnings in scenes.json: silences with no
  subtitles (music, action, the cut between flashback and present) between the end of one scene's last cue and the
  next scene's first cue. Each scene's `end` is the end of its last cue, as the spec requires, so these are expected.
- Status: all 25 non-merged scenes are complete (script, REVIEW, notes, art); `qa.py` prints QA OK (25 scenes).
