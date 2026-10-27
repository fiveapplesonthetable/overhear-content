ID = "kukhnya-s01e14-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 19
TITLE = "План Макса  (Max's Plan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Илья', 'guest': 'Саша'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In a brief moment of chaos, Max realizes he needs to take control of a difficult situation. He tells his colleagues that they will figure it out and urges them to go. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ладно, мы разберёмся с этим.",
     "Alright, we will figure this out.",
     [(280, 'Ладно, разберёмся.')], "adapted"),
    ("anya", "Всё будет хорошо.",
     "Everything will be fine.",
     [], "exact"),
    ("leva", "Что нам делать сейчас?",
     "What should we do now?",
     [], "exact"),
    ("anya", "Поехали.",
     "Let's go.",
     [(281, 'Поехали.')], "adapted"),
    ("guest", "Куда мы едем?",
     "Where are we going?",
     [], "exact"),
    ("anya", "Мы никуда не едем.",
     "We are not going anywhere.",
     [], "exact"),
    ("anya", "Это значит, что мы начинаем.",
     "It means that we are starting.",
     [], "exact"),
    ("leva", "Теперь я всё понял.",
     "Now I understand everything.",
     [(282, 'Теперь')], "adapted"),
    ("guest", "Тогда давайте работать.",
     "Then let's work.",
     [], "exact"),
    ("anya", "Да, за работу.",
     "Yes, back to work.",
     [], "exact"),
    ("leva", "У нас мало времени.",
     "We have little time.",
     [], "new"),
    ("guest", "Мы должны успеть.",
     "We must be in time.",
     [], "new"),
    ("anya", "Конечно мы успеем.",
     "Of course we will be in time.",
     [], "new"),
    ("leva", "Тогда начинаем прямо сейчас.",
     "Then we start right now.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Alright, we will figure this out.' -- The speaker makes the statement."),
    (1, None,
     "'Everything will be fine.' -- The speaker makes the statement."),
    (2, None,
     "'What should we do now?' -- The speaker makes the statement."),
    (3, None,
     "'Let's go.' -- The speaker makes the statement."),
    (4, None,
     "'Where are we going?' -- The speaker makes the statement."),
    (5, None,
     "'We are not going anywhere.' -- The speaker makes the statement."),
    (6, None,
     "'It means that we are starting.' -- The speaker makes the statement."),
    (7, None,
     "'Now I understand everything.' -- The speaker makes the statement."),
    (8, None,
     "'Then let's work.' -- The speaker makes the statement."),
    (9, None,
     "'Yes, back to work.' -- The speaker makes the statement."),
    (10, None,
     "'We have little time.' -- The speaker makes the statement."),
    (11, None,
     "'We must be in time.' -- The speaker makes the statement."),
    (12, None,
     "'Of course we will be in time.' -- The speaker makes the statement."),
    (13, None,
     "'Then we start right now.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Тогда начинаем прямо сейчас.")
