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

## s01e03
- Episode title: none in the sidecar: `title: null`.
- 36 scenes in scenes.json, 33 scripted, 3 merged:
  - 17 (Arkady smugly asks Marina in the kitchen if she is offended by his refusal) `next` into 18;
  - 33 (outside court Judge Berg asks about his dog and learns it is at the communal flat) `next` into 34;
  - 36 (after Samson hits Arkady, a paramedic tells him not to move + closing song) `prev` into 35.
- Continuity with s01e02: the "stranger with a business proposal" at the end of s01e02 (cue 1222) and the man who
  shows Samson and Nina the three-room flat in s01e03 scene 4 (and returns in scene 25) is Pasha (Павел Юрьевич
  Осипенко; Arkady guesses his surname in cue 233, «Осипенко», garbled as «А Сипенко», and in cue 891 Pasha threatens
  Samson with "my guards").
- The bug disguised inside a condom wrapper (cues 210, 356, 561, 591) is referred to neutrally by the narrator as a
  small foil packet / wrapper; in story lines the word «презерватив» is avoided (replaced by «это» / «подарок» /
  «сюрприз»), and Arkady's crude sexual boast in scene 10 (352-357) is retold cleanly as him assuming Marina came to
  flirt with him and turning her down ("Вы не в моём вкусе").
- Slavik's school nickname from his classmates (cues 324, 654, 682-691) is vulgar in the source; story lines use clean
  phrasing («плохое прозвище», «смешное имя», «врунишка» / «слабак») while keeping the childhood nickname «очкарик» for
  Arkady (garbled as «очконавт» in cues 255, 677, 796).
- The public defender Данила Головкин introduces himself with a stutter as «ваш авокадо» (cue 365); story lines use
  «ваш адвокат» while the narrator explains the stutter joke.
- Non-linear editing around the court hearing: scenes 29 (1001-1021) and 32 (1072-1092) are the two halves of the
  court session; scene 30 (1022-1042, Marina untying Arkady and planting the bug) happens earlier, before Arkady goes
  to court, and is intercut as a flashback reveal when Golovkin appears as a surprise witness.
- Viewpoint (`anya`) when Arkady is absent: Lavrov (3, 24), Samson (4, 8, 12, 19), Marina (5, 22), Pasha (7), Slavik
  (9, 28), Judge Berg (14), Nina (15), Lyolya (31).
- Scene 1: station announcements/crowd chatter (cues 1-13), the court secretary's line (19-20), and the opening song
  (61-77) are left out; the three lawyers from "Mishkin and Sons" speak as one role (`mishkin`); legal phrasing in
  cues 39 and 48-51 is simplified to A1 («грубых ошибок», «подписка о невыезде»). Scene 2: opening YouTube vlog
  chatter (78-82) and crude cues 109-113 are skipped; cue 95's garbled «Это Юля» restored to «Это Лёля»; slang in
  91-94 («фотки попер», «отжали», «не ной») simplified to A1.
- Scene 3: crude jokes in cues 121 («бубенцы») and 134 («через жопу» -> «очень плохо слышно») and constipation details
  in cue 140 cleaned up; transcription slips in 127 («ставил» -> «оставил»), 128 («чайки» -> «чайник»), and 149
  («вставить» -> «поставить») normalised; Marina's overheard phone line (139) is narrated so Klavdia takes the third
  voice. Scene 4: technical renovation terms (155, 161-165) simplified and crude cue 185 («хреначишь») omitted.
- Scene 5: garbled cue 204 («его кураулить, что ли?») -> «Мне что, ждать у двери?»; cue 210 retold cleanly as «Что
  это? Зачем мне это?». Scene 6: Nina pushing Samson (215-218) is told in the intro; garbled «Санцовчик» (219) ->
  «Самсон», «замуж ему деньги отдал» (225) -> «деньги отдал», «А Сипенко» (233) -> «Осипенко», «очканавт» (255) ->
  «очкарик»; crude callback (248-249) and swearing (256-257) omitted.
- Scene 7: slip «мне послушать» (271) -> «меня послушать»; «процессуальных нарушений» (287) -> «ошибок», «меру
  пресечения не меняй» (290) -> «оставь его дома». Scene 8: «выковырю» (294) -> «достану», «лыбится» (295) -> «и
  улыбается», «сурово» (298) -> «строго»; cue 305 («Чё?») expanded to «Что сделать? Пойдём в магазин.» to set up
  scene 12.
- Scene 9: crude nickname in 324 replaced with «плохое прозвище»; garbled «Слайка» (335) -> «Славик»; sexual boast in
  333 and insult in 337 replaced with «Ты скажи пацанам, что она с тобой гуляла» and «Если соврёшь, я всем скажу, что
  ты обманщик». Scene 10: transcription slip «У меня прощение» (340) -> «Прошу прощения»; sexual propositions and
  condom jokes (352-357) retold cleanly («Не надо, вы совсем не в моём вкусе»); Klavdia's off-screen complaint (360)
  narrated.
- Scene 11: Mishkin's phone call (361-363, 377-379) has no separate voice (role limit), so Arkady speaks his side into
  the phone; «авокадо» (365) -> «адвокат»; Golovkin's long introduction (367-374) split into two short sentences;
  Klavdia's interruption (382-384) narrated; crude insults in 391-395 replaced with «Что вы здесь делаете? Кто вас
  сюда прислал?». Scene 12: shopkeeper's cues (407-410) narrated; crude line 404 («Долбоёб с секатором!») -> «Смотри,
  какие большие ножницы!».
- Scene 13: «хищение в особо крупном размере» (414) -> «кражу больших денег»; crude insults in 425-426, 439, 444, 456
  cleaned («Вы с ума сошли?», «Вы плохой человек!», «До свидания, глупый человек!»); «по УДО выйдете» (433) -> «выйдете
  раньше»; «пошли бы на...» (449) -> «Уходите отсюда»; «терпилой» (461) -> «слабым». Scene 14: Polina's crying (466)
  narrated; «по-маленькому и по-большому» (471) -> «гулять во двор»; slip «Позвони» (487) -> «Позвоню».
- Scene 15: Golovkin's stutter (492-493) smoothed in story lines; «выдра» (512) -> «кто это»; threat in 515 cleaned to
  «Ещё слово скажешь — пожалеешь!». Scene 16: «кисонька» (521) -> «дорогая»; cues 526-527 split into short A1 lines;
  crude cues 533-534 retold cleanly as «И что мне делать? Соглашаться или нет?»; «на одну тысячу сто рублей» (537)
  shortened to «На тысячу рублей».
- Scene 18: merged scene 17 (539-545) is covered in the intro bridge; cue 575 («Эдуард Валентинович») normalised to
  «Эдуард Владимирович»; crude cues 586 («бастард») and 591 («презервативом») omitted cleanly («Марина, это что, для
  него?»). Scene 19: corridor scuffle (623-627) told in the intro bridge; «При тебе же все покупало» (629) -> «Ты же
  сам всё покупал»; «ущербный нарисовался» (631) -> «Кто этот тип в коридоре?»; mistranscribed «Дальше что ли?» (634)
  -> «Даня, что ли?»; «придурок» (639) and crude cue 646 dropped; «Винникееву-то» (649) -> «Аникееву».
- Scene 20: vulgar nickname in 654, 682-691 replaced with «врунишка»; «очконавт» (677-678) -> «очкарик»; «кресть»
  (670) -> «красть», «тачку» (686) -> «машину»; cutaway 657-664 (Lavrov and Zavarzin eating dry bread rings at their
  post) told in the intro and walkthrough. Scene 21: «бабки» (706, 713) -> «деньги»; mistranscribed «Синуль» (709) ->
  «Нинуль»; two short lines given to Nina; cues 725-727 (muffled screams at the listening post) covered in the
  walkthrough.
- Scene 22: Lyova has no voice (tea and bread rings in 729 offered by the chief, Marina's exit in 730 moved to the
  end); slips fixed: «А Никеев» (736) -> «Аникеев», «тахария» (739) -> «я очень волнуюсь», «налог, платильщиков» (749)
  -> «налогоплательщиков»; «бабку» (753) -> «бабушку». Scene 23: «бабки» (756) -> «деньги», «разводят» (759) ->
  «обманывают», «дебил» (757, 778, 784) -> dropped / «глупый», crude 802 and insult in 814 dropped; «Очконавт» (796)
  -> «очкарик».
- Scene 24: garbled «был мой дыре» (827, for «мой косяк») -> «была моя ошибка», «сушки» (833) -> «сушками», «Прикольно,
  маскировочка» (837) -> «И маскировка хорошая»; Lyova's question in 846 («мы из разных управлений») given to Lavrov;
  insult in 831 and crude dwarf/racial jokes in 848-850 dropped («Понятно. Значит, я вам не нужен.»). Scene 25: Nina's
  defensive remarks (853-854, 865-866) narrated so Samson and Pasha take the two other roles; slips fixed: «Денис»
  (863) -> «Нина», «вишню варежем» (873) -> «Вишнёвое варенье», «Нинокому реально ух» (882) -> «Нина ему чуть ухо»,
  «душевого» (884) -> «живого»; crude/swearing lines 876, 886, 888, 894, 897 dropped or retold cleanly.
- Scene 26: Nina has no voice, so cue 901 («А что это ты в квартиру принёс?») is given to Samson; slip «принеси» (903)
  -> «он собаку принёс»; crude «гнида» (914) -> «малыш». Scene 27: Polina's crying narrated; slips «виновата» (928) ->
  «виноват» and «семье» (934) -> «семьи»; crude stomach-upset words (942) and pruning-shears threat (955-959) omitted.
- Scene 28: crude sex/rocket lines (975-978, 981, 988) retold cleanly as «Я твоя девушка, мы встречаемся уже месяц»
  and «И через десять минут я ухожу»; «Да не ссы» (984) -> «Не бойся»; «бойфренда» (987) -> «парня». Scene 29: long
  legal ruling in 1001-1012 simplified into four short A1 sentences; short bridging lines added before cue 1021
  («Вы?!»).
- Scene 30: non-linear flashback bridge explained in the intro; typos «Разведите» (1024) and «разовяжу» (1025)
  corrected to «Развяжите» and «развяжу»; «затек совсем» (1027) -> «я устал сидеть»; «бабка» (1040) -> «старушка»;
  Klavdia's question (1038) narrated and Lavrov's pizza line (1041-1042) folded into Zavarzin's role. Scene 31: slang
  in 1048 replaced with «обманщики», «бойфренд» (1060) with «парень», «убила» (1049) with «потеряла»; crude remarks in
  1054-1057 and 1064-1065 retold cleanly («Ты же ещё мальчик!»).
- Scene 32: formal legal phrasing in 1074-1078 simplified; insult in 1080 and crude opening of 1081 dropped; «15»
  written out as «пятнадцать»; typo «Соседание» (1083) corrected to «Заседание»; reporters and police escort outside
  the courthouse (1084-1092) narrated around Arkady's closing lines.
- Scene 34: merged scene 33 (1093-1099) covered in the intro bridge; Slavik's brief cue (1111) narrated for the
  three-role limit; «Не ссы, прорвёмся» (1117) -> «Не бойся, всё будет хорошо»; «Чё мы, мы» (1118) -> «Что мы, мы?»;
  «Чё я, рэкетир тебе, что ли» (1120) -> «Я тебе не бандит»; «Заебись» (1122) dropped; «на хрен» (1123) -> «уже».
  Scene 35: Slavik's short protest (1133) narrated; «малолетку» (1139) -> «в колонию»; «Ты чё творил, скотина?»
  (1150) -> «Что ты делал?!»; merged scene 36 (1152-1169) told in the outro.
- Validator for s01e03: `OK: 0 errors, 25 warnings`, all "gap between scenes" in scenes.json (silences with no
  subtitles between scenes). `qa.py`: QA OK (33 scenes).
