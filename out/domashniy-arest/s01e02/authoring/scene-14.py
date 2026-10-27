ID = "domashniy-arest-s01e02-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 14
TITLE = "Агенты из Москвы  (The Agents from Moscow)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chief": "anja", "lavrov": "angelina"}
LABELS = {"anya": "Лёва", "chief": "Михаил Михайлович", "lavrov": "Лавров"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"

INTRO = ("Now we go somewhere new: the headquarters of the local security service. Last time, Samson begged his old "
         "boss for his job back, and ended up offering to carry a load of heavy radiators by himself. Here, a young "
         "lieutenant called Lyova is pestering his uncle, the chief, and then two agents from Moscow walk in. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("chief", "Ну что ты опять пришёл? Ты не видишь, я работаю?", "What have you come for again? Can't you see I'm working?",
  [(400, "Ты не видишь, я работаю")],
  "first sentence new: a plain stand-in for the idiom in cue 399 ('why are you rubbing my eyes again')"),
 ("anya", "Извини. Дядь Миш, переведи в опергруппу, а?", "Sorry. Uncle Misha, move me to the field team, would you?",
  [(402, "Извини"), (403, "Дядь Миш, переведи в опергруппу, а")], ""),
 ("anya", "Надоело мне в этом архиве сидеть.", "I'm tired of sitting in this archive.",
  [(404, "в этом архиве сидеть")], "slangy 'Достало меня уже' -> 'Надоело мне'"),
 ("chief", "Какая тебе опергруппа? Мне твоя мать голову оторвёт.",
  "What field team? Your mother will tear my head off.",
  [(406, "Какая тебе опергруппа"), (407, "Мне твоя мать голову оторвет")],
  "'если с тобой что-нибудь случится' (if anything happens to you) dropped; the narrator gives it"),
 ("anya", "Ты же глава управления, а женщину боишься.",
  "You're the head of the department, and you're afraid of a woman.",
  [(408, "Ты же глава управления, а женщину боишься")], ""),
 ("chief", "Разговорчики, лейтенант Соколов! Быстро на рабочее место.",
  "That's enough talk, Lieutenant Sokolov! Back to your desk, quickly.",
  [(409, "Разговорчики, лейтенант Соколов"), (410, "быстро на рабочее место")], "'А ну-ка давай' dropped"),
 ("lavrov", "Разрешите? Здравия желаю.", "May we come in? Good day, sir.",
  [(411, "Разрешите"), (412, "Здравия желаю")], "both agents greet the chief; given to Lavrov"),
 ("chief", "О, Джеймсы Бонды явились.", "Oh, the James Bonds have turned up.",
  [(414, "явились")], "'О,' added; the cue's 'Джеймсы Бонда' corrected to the plural 'Бонды'"),
 ("chief", "В Москве вам дают деньги на дорогую одежду, а мозги не дают.",
  "In Moscow they give you money for expensive clothes, but they don't give you brains.",
  [(417, "деньги")],
  "simplified from cues 416-417 ('in the capital they allot money for fancy gear, but don't put a brain in'); "
  "'шмотки' -> 'одежду'; the crude cue 415 left out"),
 ("lavrov", "Генерал Круглов ждёт звонка. Будьте любезны.", "General Kruglov is waiting for a call. If you'd be so kind.",
  [(418, "Генерал Круглов"), (419, "Будьте любезны")],
  "'ждет выхода на связь' (is waiting to make contact) -> 'ждёт звонка'"),
 ("chief", "Ты посмотри на этих москвичей, лейтенант. А сами операции проваливают.",
  "Just look at these Moscow types, Lieutenant. And they're the ones who mess up operations.",
  [(421, "Ты посмотри на этих"), (424, "А сами операции проваливают")],
  "'столичных' -> 'москвичей'; the colourful insults of cues 422-423 dropped"),
 ("chief", "Дима, соедини меня с Москвой. С генералом Кругловым.",
  "Dima, put me through to Moscow. To General Kruglov.",
  [(426, "Дима, соедини меня с Москвой"), (427, "с генералом Кругловым")], "'с четвертым отделом' dropped"),
 ("anya", "Дядь Миш, а можно я останусь?", "Uncle Misha, can I stay?",
  [], "new: Lyova sits in on the secret call in the next scene"),
 ("chief", "Ладно, сиди. Только тихо.", "All right, sit down. Just keep quiet.",
  [], "new: the chief lets him stay"),
]

OPENER = ("Let's go back through it slowly. The chief is busy, and his nephew has turned up at his door yet again.")

WALK = [
 (0, "Ну что ты опять пришёл?",
  "'What have you come for again?' Literally, 'well, what have you come again?' The verb is in the past tense, "
  "in the form for a man. And the chief adds a second question."),
 (0, "Ты не видишь, я работаю?",
  "'Can't you see I'm working?' Word for word, 'you don't see, I am working'. Lyova apologises, and then asks for "
  "what he really wants."),
 (1, "Извини.",
  "'Sorry.' This is the friendly form, for someone you call by first name. Then comes the request."),
 (1, "Дядь Миш, переведи в опергруппу, а?",
  "'Uncle Misha, move me to the field team, would you?' Uncle Misha is the chief, Mikhail Mikhailovich. In "
  "everyday speech people clip names when they call someone, so uncle and Misha both lose their last vowel. The "
  "little sound at the end makes the request softer, like 'would you?'. The field team are the agents who go out "
  "on real operations."),
 (2, None,
  "'I'm tired of sitting in this archive.' The first word means 'it has got boring', and the person who is bored "
  "is 'to me', not 'I'. Russian often puts feelings this way round. The chief won't hear of it."),
 (3, "Какая тебе опергруппа?",
  "'What field team?' Literally, 'what kind of field team for you?' It means 'forget it'. And here's his reason."),
 (3, "Мне твоя мать голову оторвёт.",
  "'Your mother will tear my head off.' The verb is perfective, so this present-looking form talks about the "
  "future. He means if anything happens to Lyova. So Lyova teases him."),
 (4, None,
  "'You're the head of the department, and you're afraid of a woman.' The little word after 'you' adds "
  "'after all', and the word for 'and' here has a 'but' in it. That's too much for "
  "the chief."),
 (5, "Разговорчики, лейтенант Соколов!",
  "'That's enough talk, Lieutenant Sokolov!' The first word is a little word for 'chatter', used in the army "
  "to say 'stop talking'. Switching to rank and surname puts the nephew back in his place."),
 (5, "Быстро на рабочее место.",
  "'Back to your desk, quickly.' Literally, 'quickly to your work place'. There's no verb at all, and you don't "
  "need one. Then there's a knock at the door."),
 (6, None,
  "'May we come in? Good day, sir.' Both are formal military phrases. The second one literally wishes the other "
  "person good health. These are the two agents from Moscow, Major Lavrov and Captain Zavarzin. The chief is not "
  "impressed."),
 (7, None,
  "'Oh, the James Bonds have turned up.' He makes the famous spy's name plural, the way you would with any "
  "noun. Then he tells them exactly what he thinks."),
 (8, None,
  "'In Moscow they give you money for expensive clothes, but they don't give you brains.' 'They give' has no "
  "'they' in front of it: the verb alone does the job, like 'people give'. The agents stay calm."),
 (9, "Генерал Круглов ждёт звонка.",
  "'General Kruglov is waiting for a call.' After the verb 'wait', the thing you wait for often takes the "
  "ending for 'of'. Then a very polite phrase."),
 (9, "Будьте любезны.",
  "'If you'd be so kind.' Literally, 'be kind'. Here it's cool and formal: please set up the call. The chief "
  "turns to his nephew."),
 (10, None,
  "'Just look at these Moscow types, Lieutenant. And they're the ones who mess up operations.' The word for "
  "'themselves' points the finger: they are the ones who failed. Their operation at the airport was called off "
  "at the last minute. Still, the chief picks up the phone."),
 (11, None,
  "'Dima, put me through to Moscow. To General Kruglov.' The word for 'with' comes before both Moscow and the "
  "general, and both get the same ending that goes with it. And now Lyova sees his chance."),
 (12, None,
  "'Uncle Misha, can I stay?' The word for 'may I' is followed by 'I stay', in the future form. And the uncle gives "
  "in."),
 (13, None,
  "'All right, sit down. Just keep quiet.' The verb is the one for 'sit', a friendly command. So the young man "
  "from the archive gets a seat at a secret meeting."),
]

TRANSITION = "Here's the whole scene once more, from the top."

OUTRO = ("So the Moscow agents are in town, the chief already thinks they're useless, and Lyova has a seat at the "
         "table. Well done for following it, and see you next time.")
CLOSING = ("chief", "Всё, работаем.")
