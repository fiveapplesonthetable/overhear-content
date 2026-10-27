"""s01e07 scene 13: Старый архив (FSB basement archive)."""

ID = "domashniy-arest-s01e07-scene-13"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 13
TITLE = "Старый архив  (The Old Archive)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lavrov": "anja", "zavarzin": "angelina"}
LABELS = {"anya": "Лёва", "lavrov": "Лавров", "zavarzin": "Заварзин"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 7"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = "Cues 505-527 (00:22:57-00:24:12). Lieutenant Lyova Sokolov leads Lavrov and Zavarzin into the paper archive."

INTRO = (
    "Previously, at the hospital, Arkady emerged into the hallway with plaster casts on both of his healthy arms "
    "just as Marina and Eduard were getting ready to leave. "
    "Meanwhile, back at the local FSB building, young Lieutenant Lyova Sokolov leads Major Lavrov and Captain Zavarzin "
    "down into a dusty basement room packed with paper folders."
)

STORY = [
    ("anya", "Я вас проведу. Осторожно!",
     "I'll lead you through. Careful!",
     [(506, "Я вас проведу"), (507, "Осторожно")],
     "combined cues 506-507"),
    ("lavrov", "А у вас это в компьютере есть?",
     "Do you have this on a computer?",
     [(512, "У вас")],
     "simplified в цифре нет to в компьютере есть"),
    ("anya", "Здесь вам не Москва!",
     "This isn't Moscow for you!",
     [(513, "Здесь вам не")],
     "replaced abbreviation ЦРУ with Москва"),
    ("zavarzin", "Мы за два года тут не справимся.",
     "We won't finish here in two years.",
     [(514, "Мы за два года тут не")],
     "simplified colloquial управимся to справимся"),
    ("anya", "Конечно, не справитесь. Вы же не я.",
     "Of course you won't manage. You're not me, after all.",
     [(515, "Конечно, не"), (516, "Вы же не я")],
     "simplified управитесь to справитесь"),
    ("zavarzin", "Ну так помогай! Чего зря болтать?",
     "Well then help us! Why chatter for nothing?",
     [(517, "Ну так помогай, чего зря болтать")], ""),
    ("anya", "А вы генералу Круглову скажете про меня?",
     "Will you tell General Kruglov about me?",
     [(518, "А вы генералу Круглову скажете")],
     "split cues 518-519 into two short sentences"),
    ("anya", "Пусть он меня к вашей группе прикрепит официально!",
     "Let him attach me to your group officially!",
     [(519, "он меня к вашей группе прикрепил официально")],
     "adapted subordinate clause into a standalone sentence"),
    ("lavrov", "Нет.",
     "No.",
     [(520, "Нет")], ""),
    ("anya", "Почему?",
     "Why?",
     [(521, "Почему?")], ""),
    ("lavrov", "Потому что мы работаем в другом отделе. И в другом городе.",
     "Because we work in a different department. And in a different city.",
     [(522, "Потому что мы работаем в другом отделе и в другом городе")],
     "split into two short sentences"),
    ("anya", "Ну и что? Я всё равно переезжать собираюсь.",
     "So what? I'm planning to move anyway.",
     [(523, "Ну и что? Я все равно переезжать собираюсь")], ""),
    ("anya", "Мне здесь тесно.",
     "It's too cramped for me here.",
     [(524, "Мне здесь тесно")], ""),
    ("zavarzin", "По-моему, ты нормально помещаешься.",
     "In my opinion, you fit in just fine.",
     [(525, "По-моему, нормально помещаешься")], "added ты"),
    ("anya", "Тогда ищите всё сами!",
     "Then look for everything yourselves!",
     [(526, "тогда сами")],
     "omitted rude Да пошли вы; fixed ASR езжите to ищите"),
    ("zavarzin", "Лёва, ты куда? Полковник сказал, чтобы ты нам помог!",
     "Lyova, where are you going? The colonel said you had to help us!",
     [(527, "ты куда? Полковник сказал, чтобы ты нам помог")],
     "replaced nickname Сиплый with Лёва"),
]

OPENER = "Let's break down the argument in the dusty FSB archive."

WALK = [
    (0, None,
     "'I will lead you through. Careful!' Lyova guides the two Moscow officers between the shelves."),
    (1, None,
     "'Do you have this on a computer?' Lavrov hopes the records are digitized."),
    (2, None,
     "'This is not Moscow for you!' Lyova points to the endless rows of paper folders."),
    (3, None,
     "'We will not manage to finish here in two years.' Zavarzin looks at the shelves in dismay."),
    (4, None,
     "'Of course you will not manage. You are not me, after all.' Lyova brags about his skills."),
    (5, None,
     "'Well then help us! Why chatter for nothing?' Zavarzin tells him to get to work."),
    (6, None,
     "'Will you tell General Kruglov about me?' Lyova wants a reward for his help."),
    (7, None,
     "'Let him attach me to your group officially!' He dreams of joining the Moscow team."),
    (10, None,
     "'Because we work in a different department. And in a different city.' Lavrov explains the reality."),
    (11, "Я всё равно переезжать собираюсь.",
     "'I am planning to move anyway.' Literally, I am gathering myself to relocate."),
    (12, None,
     "'It is too cramped for me here.' He feels too big for this provincial town."),
    (13, None,
     "'In my opinion, you fit in just fine.' Zavarzin jokes about the narrow aisle."),
    (14, None,
     "'Then look for everything yourselves!' Offended, Lyova turns around to leave."),
    (15, None,
     "'Lyova, where are you going? The colonel said that you had to help us!'"),
]

TRANSITION = "Now listen to the archive scene from start to finish."
OUTRO = "Offended that Lavrov won't take him to Moscow, young Lyova storms out of the paper archive."
CLOSING = ("anya", "Мне здесь тесно!")
