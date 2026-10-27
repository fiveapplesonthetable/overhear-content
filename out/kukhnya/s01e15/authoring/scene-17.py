ID = "kukhnya-s01e15-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 17
TITLE = "Желание переехать  (Desire to Move In)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Макс', 'leva': 'Вика'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Max arrives at Victoria's apartment and awkwardly asks to move in with her. He tries to sound independent, but eventually admits his true feelings. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Привет, макс.",
     "Hi, my friend.",
     [(335, 'Привет.')], "adapted"),
    ("leva", "Привет.",
     "Hi.",
     [(335, 'Привет.')], "adapted"),
    ("anya", "Я хочу переехать к тебе.",
     "I want to move to your place.",
     [(336, 'Я хочу переехать к тебе.')], "adapted"),
    ("leva", "Тебе негде жить?",
     "Do you have nowhere to live?",
     [(337, 'Что, негде жить?')], "adapted"),
    ("anya", "Нет, у меня миллион вариантов.",
     "No, I have a million options.",
     [(337, 'Да нет, просто...'), (338, 'Да миллион вариантов.')], "adapted"),
    ("anya", "Костя зовёт меня назад.",
     "Kostya is calling me back.",
     [(338, 'Просто Костя назад зовет,')], "adapted"),
    ("anya", "Лёва тоже приглашает жить.",
     "Leva is also inviting me to live.",
     [(338, 'Лёва тоже приглашает,')], "adapted"),
    ("anya", "Но я готов жить с тобой.",
     "But I am ready to live with you.",
     [(339, 'Но я готов жить с тобой.')], "adapted"),
    ("leva", "Что ты хочешь сказать?",
     "What do you want to say?",
     [], "new"),
    ("anya", "Я хочу жить с тобой.",
     "I want to live with you.",
     [(340, 'В смысле, хочу.')], "adapted"),
    ("anya", "Я не хочу быть без тебя.",
     "I do not want to be without you.",
     [(341, 'В смысле, не хочу без тебя.')], "adapted"),
    ("leva", "Это очень приятно слышать.",
     "That is very pleasant to hear.",
     [], "new"),
    ("anya", "Правда?",
     "Really?",
     [], "new"),
    ("leva", "Да, я тебе верю.",
     "Yes, I believe you.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Hi, my friend.' -- The speaker makes the statement."),
    (1, None,
     "'Hi.' -- The speaker makes the statement."),
    (2, None,
     "'I want to move to your place.' -- The speaker makes the statement."),
    (3, None,
     "'Do you have nowhere to live?' -- The speaker makes the statement."),
    (4, None,
     "'No, I have a million options.' -- The speaker makes the statement."),
    (5, None,
     "'Kostya is calling me back.' -- The speaker makes the statement."),
    (6, None,
     "'Leva is also inviting me to live.' -- The speaker makes the statement."),
    (7, None,
     "'But I am ready to live with you.' -- The speaker makes the statement."),
    (8, None,
     "'What do you want to say?' -- The speaker makes the statement."),
    (9, None,
     "'I want to live with you.' -- The speaker makes the statement."),
    (10, None,
     "'I do not want to be without you.' -- The speaker makes the statement."),
    (11, None,
     "'That is very pleasant to hear.' -- The speaker makes the statement."),
    (12, None,
     "'Really?' -- The speaker makes the statement."),
    (13, None,
     "'Yes, I believe you.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Да, я тебе верю.")
