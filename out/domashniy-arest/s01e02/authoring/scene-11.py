ID = "domashniy-arest-s01e02-scene-11"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = "Партнёры из Москвы  (The Moscow Partners)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "partner": "anja", "stepan": "angelina"}
LABELS = {"anya": "Паша", "partner": "Партнёр", "stepan": "Степан Геннадьевич"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
SOURCE_NOTE = ("Cues 288-338, plus merged scene 12 (cues 339-344, a radio voice calls off an undercover "
               "operation: 'Отбой операции... Пропустите их'), told in the outro. Arkady is absent: Pasha is the "
               "viewpoint (anya, label Паша). The polite, unnamed Moscow partner is 'partner'; the angry Stepan "
               "Gennadyevich says ты to Pasha, the partner says вы. Insults ('чудила', 'валенок', 'приперся', "
               "'сопли жует') are cleaned or dropped. Who says cues 299-301 and 330 is not certain; they are "
               "given to Stepan, whose tone they match.")

INTRO = ("Now we leave the flat for an airport lounge. Last time, Samson's dream of running for mayor came to "
         "nothing, and Arkady, with his own phone blocked, couldn't even borrow one to call the governor. Here "
         "Pasha, Arkady's deputy and now the acting mayor, meets two businessmen from Moscow who have flown in "
         "for the big cluster deal, and he doesn't have their money. We'll hear it in Russian first; don't worry "
         "about catching every word.")

STORY = [
 ("anya", "Добрый день! С прилётом.", "Good afternoon! Welcome.",
  [(288, "Добрый день"), (290, "С прилетом")], "two cues joined"),
 ("partner", "Добрый день. Спасибо.", "Good afternoon. Thank you.",
  [(291, "Спасибо")], "'Добрый день' echoes cue 288-289"),
 ("anya", "Господа, прошу прощения. Деньги будут.", "Gentlemen, I apologise. The money will be there.",
  [(293, "господа, прошу прощения"), (294, "Деньги будут")],
  "'Я' and 'произошла техническая задержка' (there's been a technical delay) dropped; the narrator mentions it"),
 ("partner", "Будут когда?", "And when will it be there?", [(295, "Будут когда")], ""),
 ("anya", "Мне нужно немножко поработать с бывшим мэром.", "I need to do a little work on the former mayor.",
  [(296, "Мне нужно немножко поработать с бывшим мэром")], ""),
 ("partner", "Вы мне сказали, деньги будут сегодня.", "You told me the money would be here today.",
  [(297, "Вы мне сказали, деньги будут сегодня")], ""),
 ("stepan", "Мы сюда зачем прилетели? Я сразу сказал: с ним ничего не получится.",
  "What did we even fly out here for? I said from the start: nothing will come of it with him.",
  [(299, "Мы сюда зачем прилетели"), (301, "Я сразу сказал")],
  "'вообще' dropped; 'с ним ловить нечего' (slang) -> 'с ним ничего не получится'"),
 ("partner", "Мы всё подготовили и прилетели на сделку.", "We got everything ready and flew in for the deal.",
  [(307, "подготовили"), (308, "Прилетели на сделку")],
  "simplified from cues 306-308 ('we cleared it with the ministry, prepared all the documents')"),
 ("anya", "Я прекрасно понимаю.", "I understand perfectly.", [(309, "Я прекрасно понимаю")], ""),
 ("stepan", "Зачем ты сюда приехал? Пустой!", "Why did you even come here? Empty-handed!",
  [(316, "сюда"), (316, "Пустой")], "the rude 'Чего ты ... приперся' -> 'Зачем ты ... приехал'"),
 ("anya", "Степан Геннадьевич, я же внёс аванс!", "Stepan Gennadyevich, I did pay the advance!",
  [(315, "Степан Геннадьевич"), (315, "я же внес аванс")], "'почему чудила?' (why a clown?) dropped"),
 ("partner", "Давайте так: два дня. Или мы переводим проект в Калугу.",
  "Here's what we'll do: two days. Or we move the project to Kaluga.",
  [(324, "Давайте так"), (325, "два дня"), (325, "мы переводим проект в Калугу")],
  "the 'if... then' of cue 325 simplified to 'two days, or...'"),
 ("stepan", "А аванс остаётся у нас.", "And the advance stays with us.",
  [(326, "остается у нас")], "from cue 326 ('ваш аванс, конечно же'), given to Stepan"),
 ("anya", "Подождите! Два дня — это же очень мало.", "Hold on! Two days is far too little.",
  [(327, "Подождите"), (329, "Это же очень мало")], "'Как два дня?' (328) folded in"),
 ("stepan", "Мало для тех, кто ничего не делает.", "Too little for people who do nothing.",
  [(330, "Для тех, кто")], "the idiom 'кто сопли жует' (who dawdle) -> 'кто ничего не делает'"),
 ("anya", "Хорошо, давайте три. Под мою личную ответственность.",
  "All right, let's say three. On my personal responsibility.",
  [(332, "Хорошо, давайте три"), (333, "Под мою личную ответственность")], ""),
 ("partner", "Три дня. Больше не могу.", "Three days. I can't give you more.",
  [(336, "Три дня. Больше не могу")], ""),
]

OPENER = ("Let's take it from the top. Pasha greets his guests very warmly, as a host should.")

WALK = [
 (0, "Добрый день!",
  "'Good afternoon!' Literally, 'good day'. It's the standard polite greeting for most of the day."),
 (0, "С прилётом.",
  "'Welcome.' Word for word, 'with the arrival by air'. Russians greet people who have just flown in with this "
  "little phrase. The partner is polite too."),
 (1, None,
  "'Good afternoon. Thank you.' So far, so friendly. But Pasha has to confess something."),
 (2, "Господа, прошу прощения.",
  "'Gentlemen, I apologise.' Literally, 'I ask forgiveness'. It's a formal, businesslike way to say sorry. He "
  "calls it a technical delay."),
 (2, "Деньги будут.",
  "'The money will be there.' The word for money is always plural in Russian, so the verb 'will be' is plural too. "
  "The partner wants a date."),
 (3, None,
  "'And when will it be there?' He puts the question word last, which makes it sound sharp and impatient. Pasha "
  "has an excuse ready."),
 (4, None,
  "'I need to do a little work on the former mayor.' After the word for 'with', both 'former' and 'mayor' take the "
  "instrumental case endings. The former mayor is Arkady, and Pasha's 'work' means squeezing the money out of him. "
  "The partner reminds him of his promise."),
 (5, None,
  "'You told me the money would be here today.' In Russian you keep the tense of the original promise: word for "
  "word, 'you told me, the money will be today'. Then Stepan Gennadyevich, the older partner, loses patience."),
 (6, "Мы сюда зачем прилетели?",
  "'What did we even fly out here for?' The verb means 'to arrive by flying'; the same root was in the greeting at "
  "the start."),
 (6, "Я сразу сказал: с ним ничего не получится.",
  "'I said from the start: nothing will come of it with him.' He means Pasha. The partner explains how much they "
  "have already done."),
 (7, None,
  "'We got everything ready and flew in for the deal.' Two past-tense verbs, both in the plural because the subject "
  "is 'we'. Pasha tries to calm them down."),
 (8, None,
  "'I understand perfectly.' The adverb in the middle comes from the word for 'beautiful', so literally 'I "
  "understand beautifully'. Stepan isn't impressed."),
 (9, None,
  "'Why did you even come here? Empty-handed!' Notice he says the informal 'you' to Pasha, not the polite one, "
  "which is a sign of contempt here. The last word is literally 'empty'. Pasha reminds him that he has already "
  "paid something."),
 (10, None,
  "'Stepan Gennadyevich, I did pay the advance!' A first name and a patronymic, the respectful way to address an "
  "older man. The little word after 'I' adds stress, like 'I did'. Now the partner names his terms."),
 (11, "Давайте так: два дня.",
  "'Here's what we'll do: two days.' Literally 'let's do it like this', the usual way to announce a decision. "
  "After the number two, the word for 'day' takes a special ending."),
 (11, "Или мы переводим проект в Калугу.",
  "'Or we move the project to Kaluga.' Kaluga is another town, not far from Moscow. The present tense here is used "
  "for a firm plan. And Stepan adds the painful part."),
 (12, None,
  "'And the advance stays with us.' The phrase at the end, literally 'at us', is how Russians say 'we have it' or "
  "'with us'. Pasha panics."),
 (13, "Подождите!",
  "'Hold on!' The polite form, because he's begging important people. Then his complaint."),
 (13, "Два дня — это же очень мало.",
  "'Two days is far too little.' The word for 'little' here means 'not enough' when it describes time or money. "
  "Stepan has a nasty answer."),
 (14, None,
  "'Too little for people who do nothing.' Literally 'for those who do nothing'. In Russian, 'nothing' needs a "
  "'not' before the verb as well: a double negative that is perfectly correct. Pasha makes an offer."),
 (15, None,
  "'All right, let's say three. On my personal responsibility.' He puts his own name on the line. And the partner "
  "gives in, a little."),
 (16, None,
  "'Three days. I can't give you more.' Literally 'more I can't'. With that, the meeting is over."),
]

TRANSITION = "Here's the whole scene once more, from the beginning."

OUTRO = ("Pasha now has three days to find the money, but as the partners walk away, a voice on a secret radio calls "
         "off an undercover operation and orders the team to let them go, so somebody has been watching this "
         "meeting all along. See you next time.")
CLOSING = ("stepan", "Время пошло!")
