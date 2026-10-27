ID = "domashniy-arest-s01e03-scene-24"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 24
TITLE = "Дворники на задании  (Janitors on a Mission)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "zavarzin": "anja", "lyova": "angelina"}
LABELS = {"anya": "Лавров", "zavarzin": "Заварзин", "lyova": "Лёва"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Arkady is absent: Major Lavrov is the viewpoint character (`anya`, label Лавров), with Captain "
               "Zavarzin (`zavarzin`, label Заварзин) and Lieutenant Lyova Sokolov (`lyova`, label Лёва). "
               "Cue 827 garbled 'был мой дыре' (slang 'мой косяк') -> 'была моя ошибка'; insult in 831 ('придурку') "
               "and the crude dwarf/racial jokes and swearing in 848-850 are dropped, replaced by a clean line in 14.")

INTRO = ("Across the courtyard, in the cold surveillance room, Major Lavrov and Captain Zavarzin are still waiting "
         "for Marina to plant the listening bug, now dressed in bright orange janitor vests as a disguise. Last "
         "time, back in the flat, Nina accidentally nicked Arkady's ear with her scalpel. Here, hungry Zavarzin "
         "wants to order pizza, when an uninvited guest knocks on the door. We'll hear it in Russian first; don't "
         "worry about catching every word.")

STORY = [
 ("zavarzin", "Анатолий Иванович, тут доставка пиццы. Пишут, доставим за десять минут.",
  "Anatoly Ivanovich, there's pizza delivery here. They write: we'll deliver in ten minutes.",
  [(820, "Анатолий Иванович, тут"), (820, "доставка"), (821, "Пишут, доставим за")],
  "'пиццы' from 822; '10 минут' written out as words"),
 ("zavarzin", "Если опоздают, пицца бесплатно. Может, закажем?",
  "If they're late, the pizza is free. Maybe we should order?",
  [(822, "Если"), (822, "пицца"), (823, "Может, закажем")],
  "'опоздаем' -> 'опоздают', 'бесплатна' -> 'бесплатно'"),
 ("anya", "Нельзя. Не по инструкции.",
  "Not allowed. It's against regulations.",
  [(825, "Нельзя. Не по инструкции")], ""),
 ("zavarzin", "А как же тогда в Омске? Тоже не по инструкции.",
  "What about that time in Omsk? That wasn't by the book either.",
  [(826, "А как же тогда в Омске? Тоже не по инструкции")], ""),
 ("anya", "Тогда была моя ошибка. И мы были пьяные.",
  "Back then it was my mistake. And we were drunk.",
  [(827, "Тогда"), (828, "И мы были пьяные")],
  "cue 827 garbled 'был мой дыре' (slang 'мой косяк') -> 'была моя ошибка'"),
 ("anya", "Мы с тобой тогда договорились. Первый и последний раз.",
  "You and I made a deal back then. First and last time.",
  [(829, "Мы с тобой тогда договорились"), (830, "Первый и последний раз")], ""),
 ("lyova", "Здравия желаю! Как вы тут?",
  "Good health to you, sir! How are things here?",
  [(832, "Здравия желаю. Как вы тут")], ""),
 ("lyova", "А я вот вам чаю с сушками принёс.",
  "I've brought you some tea and bread rings.",
  [(833, "А я вот вам чаю с"), (833, "принес")],
  "cue 833 'сушки' -> 'сушками'"),
 ("zavarzin", "О, спасибо.",
  "Oh, thank you.",
  [(834, "О, спасибо")], ""),
 ("lyova", "Нормально у вас тут, просторно. И маскировка хорошая, на дворников похожи.",
  "It's nice in here, roomy. And good disguises—you look like janitors.",
  [(835, "нормально у вас тут"), (836, "Просторно"), (838, "На дворников похожи")],
  "cue 837 'Прикольно, маскировочка' -> 'И маскировка хорошая'"),
 ("anya", "Лейтенант, вы не знаете, что мы на задании? К нам нельзя просто так приходить.",
  "Lieutenant, don't you know that we're on a mission? You mustn't just walk in on us.",
  [(839, "Лейтенант"), (839, "вы не знаете, что мы на задании"), (840, "к нам"), (840, "нельзя")],
  "cue 840 'без предварительного звонка нельзя являться' simplified"),
 ("lyova", "Я по делу. Я в группу к вам хочу.",
  "I'm here on business. I want to join your group.",
  [(842, "Я по делу"), (843, "В группу к вам хочу")],
  "slang 'не парьтесь' in 841 dropped"),
 ("anya", "Нет, это невозможно. Мы из разных управлений.",
  "No, that's impossible. We're from different departments.",
  [(844, "Нет, это невозможно"), (846, "мы из разных управлений")],
  "Lyova's question in 846 given to Lavrov as his answer"),
 ("lyova", "Понятно. Значит, я вам не нужен.",
  "I see. So you don't need me.",
  [(848, "понятно")], "clean stand-in for the crude jokes in 848-850"),
 ("anya", "Стоять! Всё чисто, теперь иди.",
  "Freeze! All clear, now go.",
  [(851, "Стоять! Все чисто. Теперь иди")], ""),
]

OPENER = ("Let's walk through it. Captain Zavarzin is looking at a flyer on his phone while Major Lavrov keeps "
          "watch.")

WALK = [
 (0, "Анатолий Иванович, тут доставка пиццы.",
  "'Anatoly Ivanovich, there's pizza delivery here.' Zavarzin uses the major's first name and father's name, "
  "even when they are alone in a cold room."),
 (0, "Пишут, доставим за десять минут.",
  "'They write: we'll deliver in ten minutes.' The preposition before 'ten minutes' is how Russian says within "
  "a set time: 'in ten minutes'. And there's a bonus."),
 (1, "Если опоздают, пицца бесплатно.",
  "'If they're late, the pizza is free.' Literally 'if they will be late, pizza free of charge'."),
 (1, "Может, закажем?",
  "'Maybe we should order?' Literally 'maybe we will order?'. Lavrov is a strict rule-follower."),
 (2, None,
  "'Not allowed. It's against regulations.' Literally 'not according to the instruction'. Zavarzin reminds him "
  "of an old mission."),
 (3, None,
  "'What about that time in Omsk? That wasn't by the book either.' Omsk is a big city in Siberia, where the two "
  "of them clearly broke the rules once. Lavrov shuts that down."),
 (4, "Тогда была моя ошибка.",
  "'Back then it was my mistake.' The verb 'was' is feminine to match 'mistake'."),
 (4, "И мы были пьяные.",
  "'And we were drunk.' Plural past tense, plus a plural adjective. He reminds Zavarzin of their promise."),
 (5, None,
  "'You and I made a deal back then. First and last time.' Notice how Russian says 'you and I': literally "
  "'we with you'. Just then, someone knocks and walks right into the secret post—it's young Lieutenant Lyova "
  "Sokolov, the local chief's nephew."),
 (6, None,
  "'Good health to you, sir! How are things here?' The first two words are the formal military greeting to a "
  "superior officer, literally 'I wish you health'. And Lyova hasn't come empty-handed."),
 (7, None,
  "'I've brought you some tea and bread rings.' Notice the ending on 'tea': instead of the usual object ending, "
  "Russian often uses the '-u' ending for 'some tea'. Hungry Zavarzin is happy to see it."),
 (8, None,
  "'Oh, thank you.' At least it's better than nothing. Lyova looks around the bare room and grins at their "
  "bright orange janitor vests."),
 (9, "Нормально у вас тут, просторно.",
  "'It's nice in here, roomy.' Literally 'normal by you here, spacious'."),
 (9, "И маскировка хорошая, на дворников похожи.",
  "'And good disguises—you look like janitors.' Literally 'similar to courtyard-sweepers'. Lavrov is not "
  "amused."),
 (10, "Лейтенант, вы не знаете, что мы на задании?",
  "'Lieutenant, don't you know that we're on a mission?' Being 'on a mission' uses the preposition 'on'."),
 (10, "К нам нельзя просто так приходить.",
  "'You mustn't just walk in on us.' The two little words in the middle mean 'just like that', without calling "
  "first. Lyova explains why he came."),
 (11, "Я по делу.",
  "'I'm here on business.' A very useful three-word phrase."),
 (11, "Я в группу к вам хочу.",
  "'I want to join your group.' He is tired of sitting in his uncle's archive and wants to be a Moscow agent. "
  "Lavrov refuses at once."),
 (12, "Нет, это невозможно.",
  "'No, that's impossible.' Plain and final."),
 (12, "Мы из разных управлений.",
  "'We're from different departments.' After 'from', both words take the genitive plural ending. Lyova takes "
  "offence."),
 (13, None,
  "'I see. So you don't need me.' Literally 'to you I am not needed', with the short masculine form of 'needed'. "
  "He turns to stomp out, and Lavrov stops him at the door."),
 (14, None,
  "'Freeze! All clear, now go.' Using the infinitive 'to stand!' is how an officer barks 'halt!'. Lavrov checks "
  "the corridor outside first so Lyova doesn't blow their cover."),
]

TRANSITION = "Now let's listen to the scene at the surveillance post again."

OUTRO = ("So Major Lavrov refuses both pizza and young Lyova, and the agents keep waiting for their bug to come "
         "alive. Next time we head back across the courtyard to see how Samson deals with Arkady's bleeding ear.")
CLOSING = ("anya", "Не по инструкции.")
