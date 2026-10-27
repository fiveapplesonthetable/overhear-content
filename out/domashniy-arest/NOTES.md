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

## s01e02
- Episode title: none in the sidecar: `title: null`.
- 34 scenes in scenes.json, 26 scripted, 8 merged:
  - 4 (Arkady's sleepless night, Klavdia scolds him) `prev` into 3;
  - 5 (Pasha wakes Vika: where's the money?) `next` into 6, told in 6's bridge;
  - 7 (guards drag Arkady out of the toilet) `prev` into 6;
  - 12 (radio: operation called off) `prev` into 11;
  - 19 (governor's judo photo) and 20 (Slavik's iPhone works) both `prev`, folded into 18 (19 is itself merged);
  - 30 (officers come; Arkady thinks he's free) `next` into 31;
  - 34 (a stranger's "business proposal"; Marina agrees to inform; closing song) `prev` into 33.
- Intercuts kept inside one scene rather than split into fragments: scene 25 contains a 14-cue cutaway to Samson's
  crew with the radiators (812-825); scene 28 contains Samson's phone call to Nina about Crimea (1032-1046).
- The real governor is Виктор Степанович (male, cues 539-598). In s01e01 scene 5 Arkady used that name as a cover for
  a woman caller (his phone even shows "Свин" for the governor and the kid says the contact is a woman, cue 512).
- The old neighbour is now named: Клавдия Викторовна (Сопрыкина). Marina lives in the communal flat with her son
  Lyosha (Лёша/Лёха). Politically loaded lines (Crimea, "white ribbon") are mentioned neutrally by the narrator at
  most, never argued in story lines.
- The PSP games console is «приставка» in story lines (Cyrillic only); the narrator may say "PSP".
- Scene 32: Lyosha, Slavik and Marina have no voice (role limit): Lyosha asking about the console and Marina's
  "we'll buy one" (1188) are narrated; cue 1190 ("Это мой айфон") given to Arkady.
- Scene 33: the guards speak as one role (Vitalik); cues 1208 ("но она всё равно умерла") and 1221 ("Шапито" ->
  "Цирк какой-то") given to Pasha. "Денег нет, но вы держитесь" is explained as a much-quoted phrase from Russian
  public life, without naming anyone. Merged scene 34 is told in 33's OUTRO.
- Voice keys follow role availability per scene (e.g. Lavrov is angelina in sc. 14 where the chief has anja, anja in
  sc. 16). Viewpoint (`anya`) when Arkady is absent: Pasha (11), Samson (13, 26), Lyova (14), the chief Mikhail
  Mikhailovich (16, 21), Marina (22, 25).
- Scene 1: cues 27-28 (president's speech, champagne) read as Vika, 29-32 as Arkady; the president is unnamed in
  story lines («президент»). Scene 2: the electricity call (72-77) is Pasha's, following Arkady's order (68);
  "the cat smelled the cream" is Pasha's joke about Arkady. Stress Цыганко́в assumed. Scene 3: cue 99 (garbled) read
  as Arkady taking off his ring ("because I'm not a thief"); «Булька» -> «Живот», State Duma -> «как у депутата».
- Scene 10: cue 278 is a mistranscription of «А Головамзюк ждёт» (-> «Тебя начальник ждёт»); Arkady says вы to
  Nina as in the source (ironic). Scene 11: cues 299-301, 326, 330 (ты, rude) given to Stepan, the polite ones to
  the partner; insults cleaned. Scene 13: cue 360 = «А я тебя уже простил».
- Scene 15: «жлоб» -> «жадина»; Lyosha says «Вы взяточник» (445). Scene 16: cue 461 garbled (opening line new);
  481-483 given to Lavrov, 484 to the general; «ярд» (slang: a billion) and «легенда» (cover story) explained.
- Scene 17: digits of the phone number written as words (uncited). Scene 18: the governor's crude lines cleaned;
  «поклёп» -> «Это неправда»; merged 19 and 20 told in the OUTRO. Scene 21: «пьющая» -> «не очень надёжная»; the
  rector affair, «белоленточница» and Crimea left out (just «активистка»); stress Сопры́кина guessed.
- Scene 25: politics reduced to «про Крым»; «Я не стукачка» -> «Я не продаюсь»; cues 809-811 split between the
  agents. Scene 26: the boss (not Samson) says the "kill me / say it to my face" lines (859-868), per the cues.
  Scene 27: «антикейф» = Аникеев; the crude catchphrase «не всасываешь» replaced by «с первого раза не понимаешь».
- Scenes 28/29: the children's unattributed cues split between Yulia and Lyosha; «лохушка / овца» -> «простая, её
  все обманывают»; Marina's throat-slitting threat -> «Ещё раз подойдёте к моему ребёнку — пожалеете!». Scene 31:
  Arkady's crude insults to the governor (1146-1151) -> «Ты толстый, ты не спортсмен!»; «хэппи-энд» -> «счастливый
  конец»; merged 30 told in the bridge.
- Scene 6: crude cue 154 -> «Взрослые не умеют ждать»; cue 169 «от правителя» -> «к правителю» (per the English);
  «Дура» dropped; merged 7 told in the last walk line, merged 5 in the bridge. Scene 8: Arkady absent, Samson is
  `anya`; slang replaced (полтишку плескани -> налей, бухать -> пить, ВДВ -> армия); crude cue 225 -> «я вчера ради
  вас всё сделал». Scene 9: "and Vika too" (243), «Я тебя закопаю» (248) dropped; лямов -> миллионов, условка ->
  условный срок.
- Scene 22: Marina keeps вы with the dean (her ты in 680-685 normalised); her student is a voiced minor role;
  «Мерзавец» dropped; the garbled «моление» (698) rewritten «Как глупо и смешно» (uncited). Scene 23: only clean
  bits of the Tretyakov impression («бандерлоги» = Kipling's monkey people, kept as mild); the watch bit dropped.
  Scene 24: «сволочи» -> «жулики»; cue 792 «Я не жадин» is a transcription slip, cited as written.
- Lexicon: «пока» is an adverb with senses for now / while / bye (s01e01 had it only as an interjection).
- Validator for s01e02: `OK: 0 errors, 18 warnings`, all "gap between scenes" in scenes.json (silences with no
  subtitles between scenes). `qa.py`: QA OK (26 scenes).
