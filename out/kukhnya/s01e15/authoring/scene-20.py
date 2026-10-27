ID = "kukhnya-s01e15-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 20
TITLE = "Ожидание Макса  (Waiting for Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Илья', 'leva': 'Сеня'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Back at the restaurant, the staff is waiting to see if Max will finally return to work after everything that happened. They discuss his possible arrival. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Тебя это тоже волнует?",
     "Does this worry you too?",
     [(372, 'Тебя это тоже воспринимает?')], "adapted"),
    ("leva", "Что именно?",
     "What exactly?",
     [], "new"),
    ("anya", "Например, Макс придёт или нет?",
     "For example, will Max come or not?",
     [(373, 'Например, зайдет Макс или нет?')], "adapted"),
    ("leva", "Я думаю, он придёт.",
     "I think he will come.",
     [], "new"),
    ("anya", "Он любит нашу кухню.",
     "He loves our kitchen.",
     [], "new"),
    ("leva", "И он любит работать.",
     "And he loves to work.",
     [], "new"),
    ("anya", "А как же шеф?",
     "And what about the chef?",
     [], "new"),
    ("leva", "Шеф его простит.",
     "The chef will forgive him.",
     [], "new"),
    ("anya", "Они помирятся.",
     "They will make peace.",
     [], "new"),
    ("leva", "Конечно помирятся.",
     "Of course they will make peace.",
     [], "new"),
    ("anya", "Тогда всё будет хорошо.",
     "Then everything will be fine.",
     [], "new"),
    ("leva", "Да, просто ждём.",
     "Yes, we are just waiting.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Does this worry you too?' -- The speaker makes the statement."),
    (1, None,
     "'What exactly?' -- The speaker makes the statement."),
    (2, None,
     "'For example, will Max come or not?' -- The speaker makes the statement."),
    (3, None,
     "'I think he will come.' -- The speaker makes the statement."),
    (4, None,
     "'He loves our kitchen.' -- The speaker makes the statement."),
    (5, None,
     "'And he loves to work.' -- The speaker makes the statement."),
    (6, None,
     "'And what about the chef?' -- The speaker makes the statement."),
    (7, None,
     "'The chef will forgive him.' -- The speaker makes the statement."),
    (8, None,
     "'They will make peace.' -- The speaker makes the statement."),
    (9, None,
     "'Of course they will make peace.' -- The speaker makes the statement."),
    (10, None,
     "'Then everything will be fine.' -- The speaker makes the statement."),
    (11, None,
     "'Yes, we are just waiting.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Да, просто ждём.")
