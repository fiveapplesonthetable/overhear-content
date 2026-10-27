ID = "kukhnya-s01e15-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 12
TITLE = "Выселение шефа  (Evicting the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Лёва', 'leva': 'Виктор'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Still furious about the deception, Leva confronts Chef Victor through a closed door. He firmly demands that Victor pack his bags and move out of his and his mother's apartment immediately. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Открывай, нам надо поговорить.",
     "Open up, we need to talk.",
     [(288, 'Открывай, поговорить надо.')], "adapted"),
    ("leva", "Лёва, что ты хочешь?",
     "Leva, what do you want?",
     [(289, 'Лёва, что ты хочешь, Лёва?')], "adapted"),
    ("anya", "Я хочу сказать тебе одну вещь.",
     "I want to tell you one thing.",
     [(291, 'Я хочу сказать.')], "adapted"),
    ("anya", "Чтобы ноги твоей больше не было в моём доме.",
     "So that your foot is no longer in my house.",
     [(292, 'Чего? Чтобы ноги вашей больше в моем доме не было.')], "adapted"),
    ("anya", "Сегодня же собирай вещи и уезжай.",
     "Today pack your things and leave.",
     [(293, 'Сегодня же собираете вещи и уезжаете.')], "adapted"),
    ("anya", "Больше ты у нас с мамой не живёшь.",
     "You no longer live with me and Mom.",
     [(294, 'Больше вы у нас с мамой не живете.')], "adapted"),
    ("anya", "Тебе это ясно?",
     "Is that clear to you?",
     [(295, 'Ясно?')], "adapted"),
    ("leva", "Да пожалуйста.",
     "Yes, sure.",
     [(295, 'Да пожалуйста.')], "adapted"),
    ("leva", "Очень мне надо.",
     "As if I need it.",
     [(296, 'Больно надо.')], "adapted"),
    ("anya", "Я жду, пока ты уйдёшь.",
     "I am waiting until you leave.",
     [], "new"),
    ("leva", "Я уже ухожу.",
     "I am already leaving.",
     [], "new"),
    ("anya", "Ключи оставь на столе.",
     "Leave the keys on the table.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Open up, we need to talk.' -- The speaker makes the statement."),
    (1, None,
     "'Leva, what do you want?' -- The speaker makes the statement."),
    (2, None,
     "'I want to tell you one thing.' -- The speaker makes the statement."),
    (3, None,
     "'So that your foot is no longer in my house.' -- The speaker makes the statement."),
    (4, None,
     "'Today pack your things and leave.' -- The speaker makes the statement."),
    (5, None,
     "'You no longer live with me and Mom.' -- The speaker makes the statement."),
    (6, None,
     "'Is that clear to you?' -- The speaker makes the statement."),
    (7, None,
     "'Yes, sure.' -- The speaker makes the statement."),
    (8, None,
     "'As if I need it.' -- The speaker makes the statement."),
    (9, None,
     "'I am waiting until you leave.' -- The speaker makes the statement."),
    (10, None,
     "'I am already leaving.' -- The speaker makes the statement."),
    (11, None,
     "'Leave the keys on the table.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Ключи оставь на столе.")
