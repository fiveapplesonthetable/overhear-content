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

## s01e04
- Episode title: none in the sidecar: `title: null`.
- 30 scenes in scenes.json, 28 scripted, 2 merged:
  - 5 (under Devil's Bridge Ilona tricks taxi driver Arturik into stepping out and drives off in his car) `prev` into 4;
  - 27 (outside the restaurant Nina scolds Samson for drinking and he persuades her to let him drive 400 metres through
    the courtyards) `next` into 28.
- Continuity with s01e02/s01e03:
  - At the end of s01e03 Samson punched Arkady; in s01e04 Arkady has a bandaged head / bruised eye after a night in the
    hospital, and Samson has lost his job and faces viral fame because Yulia uploaded the video from s01e01 of Samson
    throwing the mayor out the window.
  - The two men in scene 30 (cues 1135-1151) who play fake airport background noise and phone Pasha ("Мы ему только три
    дня дали") are the Moscow cluster-deal partners from s01e02 scene 11: Степан Геннадьевич and his calm partner, now
    named Фёдор Григорьевич.
- Clean retelling of adult/crude content:
  - In scene 2 (and merged scene 5, and scene 26), Ilona's past in Sineozersk is referred to cleanly as working as a
    club dancer («танцевала в клубе»); Arturik's propositions and Pasha's crude slurs in scene 26 (1074-1078) are
    cleaned up.
  - In scene 6, Golovkin's confession that he has loved Nina since first grade is kept clean (Arkady's crude guesses in
    159-160 and phrase in 163 are simplified to «Ты влюблён в чужую жену!» / «я расскажу Самсону, что ты любишь его
    жену»).
  - In scene 8, Pasha's crude prison threats (226-228) are omitted cleanly.
  - In scene 16, Klavdia's vulgar details about Samson's drunken behaviour (624, 628) and silicone joke (634) are
    omitted; "3D" and "Smart TV" are written in Cyrillic in story lines («три-дэ», «смарт-телевизор» / «большой
    телевизор»).
- Viewpoint (`anya`) when Arkady is absent: Ilona (2, 13, 26), Samson (4, 7, 9, 19, 22, 25, 29), Pasha (14), Fyodor
  Grigoryevich (30).
- Scene 1: Ilona's brief taxi lines (7-10) are told by the narrator and the opening song (33-45) is omitted; garbled
  «Самсун» (1) -> «Самсон», «Маша» (4, 6) -> «Нина», «чебуречка» (12) -> «чебуречная»; crude toilet details (14-17,
  30) and prison nightmare details (23) omitted or retold cleanly («Ему снятся страшные сны»). Scene 2: «зажигалки
  стриптиз танцевала» (46) -> «у нас в клубе танцевала»; slang and insults in 49, 56-57, 62 simplified to A1; slip «по
  чёртов мост» (66) -> «под Чёртов мост».
- Scene 3: curses and vulgarities in 83 («алкаша»), 88-90 («Чтоб ты сдох», «сожрал»), and 101-105 («говно»,
  «подавились») replaced with clean A1 language; numbers «150» and «12» written out as words; Samson's brief entrance
  (96) and the TV news report (108-112) narrated and folded into Nina's final line. Scene 4: slang «кобыл в аппарате»
  (119) -> «сил в этой машине», «аппарат» (122) -> «машина»; merged scene 5 (129-141) is told in the outro.
- Scene 6: guard's lines (142-143, 169-172) narrated; insults and swearing in 144, 147, 153, 159-160, 162, 163, 168
  cleaned up («Чтобы мне ещё десять лет дали?», «Ты любишь чужую жену!», «В тайне? А ты мою тайну вчера сохранил?»).
  Scene 7: chain name «Пятёрочки» (188) -> «в магазине», «Зазывать ... в ростовом костюме» (195) -> «Звать ... В
  костюме», slang «Да нафиг, Нина, я вафли не буду» (196) -> «Нина, я вафлей не буду!», numbers in 199 written out as
  words, «обозналась» (207) -> «ошиблась», garbled cues 205 and 209 omitted.
- Scene 8: slang in 220 («лямов и плюс условка» -> «миллионов и условный срок»), 225 («на зоне» -> «В тюрьме»), and
  242 («ржет» -> «смеётся») cleaned up; crude lines 226-228, 235, 248, and 252 («Пиздец тебе, Паша» -> «Конец тебе,
  Паша!») omitted or retold cleanly; numbers «5» and «10» written out as words. Scene 9: slips «вафлями» (260 ->
  «вафлей»), «Инна» (262 -> «Нина»), and «Солсон» (264, 267 -> «Самсон») corrected; «уволишься» (261) -> «уйдёшь».
- Scene 10: Lavrov and Zavarzin watching Arkady through binoculars (289-291) narrated in the intro, and reporters
  outside (297-305) summarised in Samson's line; view count «4» (318) written out as «четыре» and spoken by Yulia; slip
  «выложил-то» (321) -> «выложила». Scene 11: Yulia reading online comments (370-377) folded into Nina's role; crude
  expressions and insults omitted or retold cleanly.
- Scene 12: «урод» (391) dropped and «нюх потеряли, оборзели» (396-397) -> «совесть потеряли»; Nina giving reporters
  the campaign phone number (418-424) and the TV news / agents in their car (425-430) covered in the walkthrough and
  outro. Scene 13: focus-group presentation and staff lines (431-442) consolidated into Ksyusha's role; «перепридумать»
  (441) -> «переделать», «форс-мажор» (464) -> «большая проблема»; Pasha's corridor outburst (453) and «дебил» (467)
  omitted.
- Scene 14: insults in 490, 496, 499, 513 dropped; the governor's staged winter jogging photo op in the park (506-514)
  narrated in the walkthrough; mistranscribed «а не Киева» (522) -> «Аникеева»; cues 523-525 omitted cleanly. Scene 15:
  Yulia answering voter calls (531-535, 554-556) and Slavik bringing the free brewery beer (579-582) narrated;
  «зажравшегося» (544) -> «богатого»; crude words in 550, 557-559, 563-564 omitted; slip «проконтролируйте меня» (597)
  -> «проконтролируйте его».
- Scene 16: cue 618 normalised to neuter «Настроение ... хорошее»; crude cues 624, 628, 634 omitted; «в Лах-Ньюс залью»
  (635) -> «в новости отправлю»; «15» (636) written out as «пятнадцать»; «3D и смарт-ТВ» (646) -> «три-дэ и
  смарт-телевизор». Scene 17: Nina's greeting narrated; slip «Каникееву» (661) -> «к Аникееву».
- Scene 18: slip «Мыло-гонно» (689) omitted; «Элончик» (698, 709) -> «Илона»; crude «вертепа» (713) and «Ни хрена»
  (720) cleaned up; Lavrov and Zavarzin watching through binoculars (721-725) narrated in the walkthrough. Scene 19:
  crude words in 767, 773-775 omitted; «на семь косарей» (770) -> «на семь тысяч».
- Scene 20: Golovkin carrying in the 47,000-rouble TV (782-784, 812) narrated («47» written out as «сорок семь»);
  «посетители» (786) -> «гости»; «обязательства» (814) -> «обещания»; long cues 803 and 818 split into short sentences.
  Scene 21: «мордатый» (828) and «Прониктоненно» (834) dropped; «пододвигай» (832) -> «двигай»; garbled «А я мне
  мерзость» (835) -> «А по-моему, это гадость! Я не буду давать взятку.»; «150» (842) -> «сто пятьдесят»; garbled
  «Пользуйтесь, мой слабый» (844) -> «Вы пользуетесь моей слабостью!».
- Scene 22: «предоставить вам этот автомобиль на эксклюзивный» (862) -> «дать вам эту машину на»; «10» (864) ->
  «десяти»; «отечественных автомобилях» (867) -> «русских машинах»; slang «аппарат» (869, 890) -> «машина», «спятил»
  (889) -> «с ума сошёл», «круче» (902) -> «лучше»; Samson's brief chat outside the water kiosk (880-885) narrated.
  Scene 23: Golovkin's single-word reply («Хотел», 918) narrated; Ilona's church decree (928-934) simplified to «Вот
  документ. Место в главном соборе нашего города.»; slip «Мой ЛК» (948) -> «Мой Гриша».
- Scene 24: Lev Leshchenko's warm greeting on the phone (973-980) narrated around Klavdia's responses; «на химкомбинате»
  (997) -> «на заводе»; crude words in 1009, 1017-1018 cleaned up («Даже мне сейчас стыдно», «Ах ты обманщица! Ты
  успела переслать видео!»). Scene 25: slips «депозит на святых» (1020 -> «на семь тысяч»), «А не кейв» (1023-1024 ->
  «Аникеев»), and «Бен» (1047 -> «Вань») corrected; menu items (1031-1043) and slang (1048-1049) simplified to A1.
- Scene 26: «Давай-ка заливает в сеть» (1055) -> «Сейчас мы выложим это видео в интернет»; slip «Никеева» (1058) ->
  «Аникеева»; «нечеловеческих» (1060) -> «ужасных»; Pasha's crude slurs and sexual remarks in 1074-1078 and 1081
  cleaned up («Ты кто такая?» / «Я в клубе танцевала.» / «Привезёшь ему подушку — сразу уволю!»). Scene 28: merged
  scene 27 (1085-1091) covered in the intro bridge; slips «Санова» (1093 -> «снова») and «Пошла» (1101 -> «Пошёл»)
  fixed; «бабки» (1115) -> «деньги»; Lavrov and Zavarzin groaning at their post (1108-1110) narrated.
- Scene 29: slang «эти, вертолеты» (1118) -> «уже голова кружится»; garbled 1119 -> «Нам надо сдать машину до десяти
  часов»; «Резонно. Гони самцов» (1124) -> «Правда. Давай быстрее, Самсон!»; garbled 1127-1128 and 1132-1133 simplified
  cleanly. Scene 30: «Вруби ... фон» (1136) -> «Включи ... шум», «прикалываешься» (1138) -> «шутишь»; «готовы дать вам
  отсрочку» (1145) -> «даём вам ещё немного времени»; «средства» (1146) -> «деньги»; closing song (1152-1170) covered
  in the outro.
- Validator for s01e04: `OK: 0 errors, 18 warnings`, all "gap between scenes" in scenes.json (silences with no
  subtitles between scenes). `qa.py`: QA OK (28 scenes).

## s01e05
- Episode title: none in the sidecar: `title: null`.
- 30 scenes in scenes.json, 29 scripted, 1 merged:
  - 13 (Ilona slips into the City Hall archive and convinces archivist Lydia Alexeyevna to give her five minutes because
    she is working for Arkady Borisovich) `next` into 14.
- Continuity with s01e04:
  - At the end of s01e04 Samson launched the test-drive SUV (`БМВ` / `машина`) over a ramp; s01e05 reveals he crashed straight
    into the Sineozersk branch of the All-Russian Society of the Blind (`Всероссийское общество слепых`), where workers
    were packing dried sage (`шалфей`).
  - The young archive lieutenant whom General Kruglov asks about in scene 11 (cues 420-426, "А где этот карлик, который
    из архива?") is Lyova Sokolov (`Лёва`), Mikhail Mikhailovich's nephew from s01e02/s01e03.
  - Lavrov's first name and patronymic (used as a cover in scenes 20 and 24) is Всеволод Алексеевич (garbled in subtitles
    as «Селд Алексеевич»).
- Clean retelling of adult/crude content:
  - In scenes 3, 15, 16, 19, 20, 26, 29, 30: Nina's story about restaurant hooligans (107-111) avoids «шлюхой» / «лапать»
    (using «оскорбляли» / «приставали»); Uncle Grisha's crude threats to Arkady with a bottle (578-581, 620, 750) are
    retold cleanly as threatening to beat him up; Ilona's marijuana plant in scenes 23 and 25 is kept light and matter-of-fact
    as in the TV news report («трава» / «конопля»), without glorifying drugs; the governor's crude banya insults in scene 29
    (1114-1116, 1122, 1131-1134, 1142-1143) are replaced with clean A1 scolding.
- Viewpoint (`anya`) when Arkady is absent: Marina (6, 10, 24), Uncle Grisha (7), Ilona (9, 21), Mikhail Mikhailovich (11),
  Samson (12, 18, 22, 23, 25), Pasha (17, 29), Lavrov (20), Larisa (26).
- Scene 1: traffic police prompts (1, 8, 10, 17) are echoed by Samson, TV news lines (40-44) are voiced by Arkady watching
  the broadcast, the opening song (47-56) is skipped, and crude slang in 45 («полярный лис / песец») is replaced with «кошмар».
  Scene 2: morning TV news (57-60), Yulia's dishwashing complaint (67-68), and Danila's remark (69) are folded into narrator
  context; crude words («дебил» in 70, «помрет» -> «умрёт» in 80, «бухать» in 81) and brand name «БМВ» in 73 are cleaned up or
  omitted.
- Scene 3: crude words («рожа» -> «лицо» in 96-97, «лапать» in 107, «шлюхой» in 110, «уроды конченые» in 127) and the English
  phrase «Take your time» in 145 are cleaned up or omitted; Ilona's brief greeting (142) is folded into narrator context.
  Scene 4: Nina's warning in 147-148 is folded into Arkady's realization and Samson's brief corridor exchange in 158-159 is
  narrated for the three-role limit; slang «алкашандра» (157) -> «пьяница».
- Scene 5: «себя в конце концовку» (200) omitted for clean A1 retelling. Scene 6: Arkady's brief remark in 233-235 is narrated
  in the walkthrough so Marina and the two debt collectors hold the three voices; kidney threat in 210, «аппетитная» in 213,
  and crude insults in 231, 234, 238-239 omitted; spoken numbers written out in Cyrillic («двадцать тысяч», «тридцать», «сто
  пятьдесят тысяч»).
- Scene 7: «надо отжимать» (243) -> «Надо её забирать»; crude threats and curses in 248-252, 255-256, 260, 265 omitted or
  cleaned up. Scene 8: spoken numbers written out in Cyrillic; colloquial «одалживала» (298) -> «давала в долг».
- Scene 9: Andryusha's remarks are narrated within the three-role limit; slips «а не Кей» (328) -> «Аникеев» and «Юрий
  Часипенко» (343) -> «Юрьевич» corrected; slang «бред» (351) / «бабки спер» (354) -> «глупости» / «деньги украл». Scene 10:
  cues 360-362 skipped; «подонков» in 364, Chechen students joke in 384-385, and condom callback in 393 omitted; digits «150»
  and «20» written out as words; «узурпировала» -> «забрала»; «в шпаковку» -> «в деревню».
- Scene 11: «выбьет деньги из мэра» -> «заберёт деньги у мэра»; «будет баллотироваться в мэры» -> «пойдёт в мэры»;
  «приостановился» -> «остановился»; «Тупец я» in 409 and «Сгинь» in 429 omitted; «карлик» in 420 -> «маленький». Scene 12:
  Marina's voicemail to Lavrov (430-432) bridged in the intro; garbled «ж уж дом» (434) -> «скажешь тоже, дом»; crude toilet
  joke (448-451), «дуру-то не включай» (460), and «ментов вырубили» (470) omitted; slang «быху/Бэху» -> «машину/на машине»;
  «Минты, чего он гонит-то?» (463) -> «Нин, что он говорит?».
- Scene 14: merged scene 13 (485-500, Ilona sneaking into the City Hall archive and convincing Lydia Alexeyevna to give her
  five minutes because she is working for Arkady Borisovich) is covered in the intro bridge; slips «договориться» (506) ->
  «договорится», «Анифеева» (511) -> «Аникеева», and «уторяйся» (514) -> «Смотри» corrected; «мариновал-то» (508) -> «виноват
  он»; insults and crude phrasing in 504, 517-519 cleaned up. Scene 15: Lyosha's brief lines in 546-551 are narrated in the
  intro and walkthrough for the three-role limit; slips «Детей бежать» (568) -> «детей обижать» and «Здесь Гриша» (569) ->
  «Дядя Гриша» corrected; bottle threats and curses in 578-589 cleaned up.
- Scene 16: Kostik's lines are folded into Uncle Grisha's or narrated; digits written out as words; crude insults and threats
  in 599, 608-611, 619-620, 628, 639-646 cleaned up. Scene 17: lines about varicose veins, hives, and sex in 661, 664, 666-670
  omitted for clean A1 retelling.
- Scene 18: cutaway cues 726-730 where Pasha phones the governor about shredding the archive folder are covered in the outro;
  slip «Что они в школе?» (705) -> «Почему ты не в школе?»; crude «рот закрыла» (716) omitted. Scene 19: Lyosha's opening
  protest (731) is narrated; «несёте» (745) -> «говорите»; second clause of 746 adapted to «Они тогда мальчика пугали!»; crude
  bottle threat in 750-752 and «к чёрту» in 754 omitted.
- Scene 20: Zavarzin accompanies Lavrov and is narrated within the three-role limit; slang/obscenities cleaned for A1 («загоним
  и бабки поделим» in 765 -> «продадим их? И деньги поделим?», «ссыкло» in 779-780 -> «трус», spine threat in 799 omitted);
  «150» written out as «сто пятьдесят»; slip «Ромавира» (792) -> «Армавира»; «погасила» (797) -> «закрыла». Scene 21: «по
  поводу вашего здания» (811) -> «про ваше здание»; «Подписанные Аникейовым» (814) -> «Его подписал Аникеев»; «до адресата»
  (818) -> «до вас»; «СМУ №2... троюродного брата Осипенко» (823-825) -> «А это компания брата Осипенко!»; insults in 834 and
  836 cleaned to «Ваш кандидат слабый».
- Scene 22: Yulia's and Nina's panic as the dacha stove smokes and catches fire; slips and colloquialisms simplified to short
  A1 sentences. Scene 23: Golovkin's dacha burning down and the discovery of the marijuana greenhouse inside the Society of
  the Blind; crude expletives omitted. Scene 24: Lavrov returns Marina's canceled loan contract and tries to kiss her;
  «Селд Алексеевич» corrected to «Всеволод Алексеевич». Scene 25: the family watching the TV news report showing Samson hailed
  as a hero for exposing the drug lab inside the Society of the Blind.
- Scene 26: live TV debate between Pasha Osipenko and Ilona hosted by Larisa, where Ilona presents the two documents proving
  Pasha stole the blind society's building money. Scene 27: colloquial «Вань» -> «Ваня»; «ДТП» (1039) -> «Это авария!»; crude
  words in 1041 and 1044 cleaned up; slips «А Никеев? К себе?» (1045) -> «Аникеев, иди к себе», «Никееву он» (1052) ->
  «Осипенко», and «сам расскажешь» (1060) -> «сама им всё расскажешь» corrected; Klavdia mocking Arkady's pyjamas (1061-1067)
  summarised in the outro.
- Scene 28: Ilona's farewell exchange with Arkady (1068-1081) and Golovkin's goodbye to Nina (1089-1097) narrated within the
  three-role limit; slips «Виссамсонов» (1070) -> «наш Самсонов», «Дедушка» (1098) -> «Нина», «от золу» (1099) -> «за ум»,
  and «Давно, парень» (1104) -> «Давно пора, Ваня» corrected; «блин» (1108) omitted. Scene 29: crude insults and profanity in
  1111-1116, 1121-1122, 1131-1134, 1142-1143 cleaned up; «ёрничаешь/ёрничаю» (1127-1130) -> «шутишь/шучу»; slip «пробуешь»
  (1144) -> «паришься». Scene 30: «отблагодарить» (1154) -> «поблагодарить»; «Дай Бог» (1157), «Господи» (1159), and «Вот
  мразь» (1171) dropped; «Вот вы сдурели» (1173) -> «Вот вы с ума сошли!»; cues 1175-1193 (the bruised debt collectors forced
  by Arkady's guards to attend Marina's university lectures) and the closing song (1194-1221) summarised in the outro.
- Validator for s01e05: `OK: 0 errors, 17 warnings`, all "gap between scenes" in scenes.json (silences with no
  subtitles between scenes). `qa.py`: QA OK (29 scenes).

## s01e06
- Episode title: none in the sidecar: `title: null`.
- 31 scenes in scenes.json, 29 scripted, 2 merged:
  - 14 (behind Colonel Mikhail Mikhailovich's back, Major Lavrov and Captain Ovechkin persuade diminutive Lieutenant Lyova
    Sokolov to dress up as a schoolboy and provoke Samsonov on camera) `next` into 15;
  - 24 (fired up by Ilona's reverse-psychology insult, Galina Ignatyeva dances brilliantly at the ballet audition, while
    Marina brings bruised Arkady a slice of cake made with jam instead of the exploded condensed milk) `next` into 25.
- Continuity with s01e05:
  - At the end of s01e05 Arkady advised Samsonov to read books to improve his diction; in s01e06 scene 1 Samsonov finishes
    Machiavelli's *The Prince* («Государь») at dawn and asks Arkady what to read next, prompting Arkady to recommend Sun Tzu's
    *The Art of War* («Искусство войны», Сунь-цзы).
  - In scene 2, bruised debt collectors Uncle Grisha and Kostik from s01e05 apologize to Marina at her door, cancel her loan,
    and deliver flowers and a message from Eduard Valentinovich.
- Clean retelling of adult/crude content:
  - Arkady's dream in scene 1 (1-3, 35), his phone call to Lyolya and banter with Ilona in scene 7 (241, 282-284), his request
    for 5,000 roubles in scenes 11 and 15 (413-415, 424, 429, 540-551), the FSB brainstorming in scene 9 (321-330), Yulya's
    bluff in scene 10 (365), Klavdia Viktorovna's third task in scene 18 (670, 989, retold cleanly as knocking neighbor's trash
    off the tree branch outside the kitchen window), Nina's outburst in scene 20 (763-767), and Samson confronting Ignatyev in
    scene 26 (957, 966) are all kept clean and free of obscenities or sexual slurs.
- Viewpoint (`anya`) when Arkady is absent: Marina (2, 8, 25), Pasha (3), Yulya (4, 5, 10, 12, 26), Zina (6), Mikhail Mikhailovich
  (9), Nina (13, 21, 31), Librarian (16), Anna (17), Ilona (19, 23, 28), Kapustina (20).
- Scene 1: slips «маки Авели» (23 -> «Макиавелли»), «с дикцией ненормально было» (21 -> «чтобы дикция была нормальная»),
  «Захарий, потом» (39 -> «заходи, потом»), and «Суньдзы» (43 -> «Сунь-цзы») restored; slang/obscenities in 3 («припёрлась» ->
  «пришла»), 18 (omitted), 28 («тварь» -> «злодеи»), and 45 («Сунь что? Тебе что там снится?») cleaned; opening song (47-50)
  skipped. Scene 2: Lyosha's brief remark (79) narrated; slips «Кастет, дай цветы» (55 -> «Константин, дай цветы»), «Он же без вас
  не может» (63 -> «Он жить без вас не может»), and «Да вы унижаетесь» (74 -> «Долго унижаться?») restored; «Хрен вам» (73) ->
  «Нет уж!».
- Scene 3: second businessman's lines (93-94, 112-115) folded into Sizov's role; slip «эсперкоме» (103) -> «избиркоме»; «18»
  written out as «восемнадцать». Scene 4: businessmen Sizov and Gaponenko backing out (123-126) narrated; slip «кандидат Самсонова
  в подписи подался» (98) -> «Кандидат Самсонов подал подписи с нарушениями»; «из центра избиркома» (106) -> «из Москвы»; Joker /
  Heath Ledger reference (134-137) covered in the outro.
- Scene 5: slips «Две стенок» (144 -> «Две тонны»), «красавицы таких набираешь» (154 -> «красавиц таких берёшь»), «Отец Горя ...
  осеганул» (161 -> «А отец с двадцатого этажа прыгнул»), «оболеет» (163 -> «болеет»), and «Сиротой» (166 -> «С сиротой»)
  restored; slang in 148-149, 156, 160-163 simplified for A1. Scene 6: Colonel Mikhail Mikhailovich's and Lyova's brief lines
  (192, 217-219, 237-239) narrated; slip «частный ход выборов» (228) -> «честный ход выборов»; «гипертонический криз» (212) ->
  «больное сердце», «дискредитировать» (223) -> «остановить»; dark joke in 232-233 omitted.
- Scene 7: slips «Энигейв» (254 -> «Аникеев») and «Усипенко» (269 -> «Осипенко») restored; «50» written out as «пятьдесят»;
  «сволочь» (252) -> «подлец», «жопа» (283) -> «беда». Scene 8: Lyosha's brief remark (312) narrated; slips «Эдик» (289), «Мы на
  вас с мамой расписали» (297 -> «Мы с мамой всё обсудили»), and «Я с тобой очень проголодаюсь» (310 -> «Я ведь очень
  проголодаюсь») restored; «сгущёнки» (307) -> «сгущёнкой».
- Scene 9: Captain Ovechkin's lines folded into Lavrov's role; slips «дискредитации» (316), «Вон Лёва, смотрите» (332), and
  «Утопили» (336) restored; crude brainstorming (321-330) omitted; «отхватит» (346) -> «получит». Scene 10: «На апорт» (365)
  cleaned to «На операцию»; slips «Мне какая-то небеременная» (373 -> «Никакая ты не беременная»), «выкладываем» (376 ->
  «выкладывай»), «не плевать» (379 -> «плевать»), and «Зачемник» (388 -> «Начальник») restored; crude words in 378 and 380
  cleaned.
- Scene 11: Lyosha's protest (390-402) narrated; crude lines in 413-415 and 424-429 cleaned to «Я подругу приглашу» and «На
  подружку твою!». Scene 12: slips «Испанские» (440 -> «Испанский»), «к Лоджицам» (445 -> «в Ложкино»), and «год три» (473 ->
  «год») restored; «твари» (451) -> «люди»; «15» written out as «пятнадцать»; «пунктик» (464-465) -> «слабое место».
- Scene 13: Slavik's outbursts (508, 520) narrated; slips «дочерью» (481 -> «сестры»), «областных клиник» (485 -> «областной
  клиники»), «собираетесь» (500 -> «избираетесь»), and «четвертной контрольной» (510 -> «контрольную за четверть») restored; crude
  lines cleaned; «2» written out as «два». Scene 15: merged scene 14 (528-531) covered in the intro bridge; Sergei's remarks
  (564-569) narrated; slips «сгущенка» (562 -> «сгущёнку»), «Ебославской» (574 -> «югославской»), and «Придикюр» (580 ->
  «педикюр») restored; curses in 570-571 and 578 cleaned; «45» and «2» written out as words.
- Scene 16: Colonel Mikhail Mikhailovich's phone replies narrated around Lavrov's lines; slips «Воробьянином» (586 ->
  «Воробьянинов»), «отнёс эти книги» (600 -> «относился к книге»), and «злостные должны» (608 -> «злостный должник») restored;
  numbers written out as words. Scene 17: Lavrov and Ovechkin's comments from the bushes narrated; crude insults in 610-664
  cleaned; «гном» kept as the comic trigger for Lyova leaping into the river.
- Scene 18: Klavdia Viktorovna's third task (670) retold cleanly as knocking trash off the tree branch outside the kitchen window.
  Scene 19: Galina's stage fright at the Moscow ballet audition; slips and choreographer lines smoothed for A1.
- Scene 20: Samson's brief lines narrated; slips «Юлька» -> «Юля», «Астра-медицинская помощь» (722 -> «Нужна скорая помощь?»),
  «секиры башка» (732 -> «плохо будет»), «училки» (733 -> «учителя»), and «напиздела» (743 -> «соврала») cleaned/restored; Nina's
  crude insults in 763-767 cleaned to «Зачем она всем так врала?». Scene 21: Slavik's reaction (781-784) narrated as the condensed
  milk can explodes on the stove while Arkady falls from the window; slips «Во мне» (769 -> «Ваня») and «мать-приступница» (809 ->
  «мать-преступница») restored; «срач» (806) -> «грязь».
- Scene 22: Marina scolding Arkady and Klavdia Viktorovna after the condensed milk explosion; Klavdia insists she only owes 3,300
  roubles because Arkady didn't finish the third task, and Marina refuses to take any money for cleaning her own kitchen. Scene 23:
  Samson and Nina calling Arkady (856-880) voiced by Samson with Arkady's phone promise narrated; Ilona uses reverse psychology on
  Galina (881-912) by telling her she has no talent so she will dance out of defiance.
- Scene 25: merged scene 24 (913-918) covered in the intro bridge; Eduard arrives at Marina's room claiming he told his wife Alla
  Evgenyevna everything, only for Alla to phone him from the airport with food poisoning so he runs back home («Прости меня, я
  немножко преувеличил»). Scene 26: Yulya begs Ignatyev for 157,600 roubles (written out in words) for her invented grandmother's
  operation and claims the man downstairs (her father Samson) is her abusive ex-boyfriend; Samson punches Ignatyev before Yulya
  runs out and confesses the truth.
- Scene 27: «оказался не такой отвратительный» (975) -> «не такой плохой»; cue 989 cleaned («на меня упал мусор с ветки»); «с
  вашим тортиком средней паршивости» (993) -> «с тортом»; slips «Ливайте» (1000 -> «Наливайте»), «Алина» (1020 -> «Марина»), and
  «чужой металл» (1032 -> «тяжёлый металл») restored; «из Иванушек... на гастроли» (1021-1024) -> «певца! Они приезжали к нам на
  концерт»; «мразота» (1030) -> «подлец». Scene 28: «ворюгой» (1040) -> «вором»; slips «Агнатила» (1045 -> «Игнатьев») and
  «объясняйте отношения» (1046 -> «выясняйте отношения») restored.
- Scene 29: slips «Я лет двадцать с ней играла» (1047 -> «Я двадцать лет в карты не играла»), «Турацкая» (1067 -> «Глупая»), and
  «выпил» (1083 -> «выпьем») restored; «пневматическая винтовка» (1058) -> «ружьё»; «цирроза печени» (1063) -> «болезни печени»;
  «стопочек» (1081) -> «маленьких рюмок». Scene 30: «Здрасте... Чемпотичненько» (1091, 1093) -> «Здравствуйте! У вас тут очень
  мило.»; «обиженку включил» (1109) -> «на меня обиделся»; brand name «шанель» (1118) -> «духи».
- Scene 31: TV news report (1129-1134), Lavrov's excuses (1139-1152), and Yulya's pout (1166-1168) narrated within the three-role
  limit; «угробили» (1142) -> «погубили»; «весь мозг проест» (1146) -> «всю голову заморочит»; «100» and «300» written out as
  «сто» and «триста»; «наплевать» (1168, 1170) -> «всё равно»; slip «дядя Даня» (1172-1173) restored to «дядя Аркадий».
- Validator for s01e06: `OK: 0 errors, 20 warnings`, all "gap between scenes" in scenes.json (silences with no
  subtitles between scenes). `qa.py`: QA OK (29 scenes).

## s01e07
- Episode title: none in the sidecar: `title: null`.
- 34 scenes in scenes.json, 32 scripted, 2 merged:
  - 20 (in the courtyard Samsonov mocks lawyer Danya's small city car before setting off for the winter forest) `next` into 22;
  - 26 (in the snowy forest Danya and Slavik bring a limping Samsonov back up from the ravine after he fell showing off a lever
    trick) `next` into 28.
- Continuity with s01e02–s01e06:
  - In s01e07 scene 1 the neighbours celebrate Samsonov's official registration as a candidate for mayor; Nina's handsome lawyer
    acquaintance Даниил («Даня», first seen in s01e02 when Nina brought him to represent Arkady) visits Nina, brings pastries and
    cheese fondue, and sparks fierce jealousy in Samsonov.
  - Reading Sun Tzu's *The Art of War* («Искусство войны», recommended by Arkady in s01e06 sc. 1), Samsonov dreams in scene 15
    that ancient Chinese strategist Sun Tzu (`Сунь-цзы`) advises him to lure Danya onto his own territory—a winter shashlik
    picnic in the forest—where Samsonov's attempts to show off his airborne (`ВДВ` / `десантура`) skills backfire.
  - Meanwhile, to break up Marina and Eduard Valentinovich (who lied to his wife Alla Evgenyevna that he is at a two-day
    symposium in Plyos), Arkady stages a fall down the stairs (sc. 7) and uses the governor's trick—dropping to his knees and
    kissing people's shoes (first Ilona in sc. 6, then the hospital trauma doctor in sc. 11)—to get fake plaster casts on both
    arms so Marina has to wait on him hand and foot.
- Clean retelling of adult/crude content:
  - Arkady's imagined argument with his late grandmother in scene 2 (71-88), Eduard's talk of his potency pill («таблеточка»
    for his «давление» / romance in scenes 6, 16, 19, 25), Arkady banging on the wall in scene 16 (636-637), the bathroom zipper
    scene in scene 27 (998-1073, retold cleanly as slapstick comedy where Arkady cannot manage his zipper with both arms in casts
    and gets his skin pinched), and the ointment misunderstanding in scene 29 (1108-1140) are all retold cleanly for A1 without
    crude or explicit language.
  - In scene 11 cue 475, the political names in Arkady's plea to the doctor are omitted («Ради любви, ради вашего кумира,
    доктор!»).
