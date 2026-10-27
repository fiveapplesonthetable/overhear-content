ID = "kukhnya-s01e15-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 9
TITLE = "Без Макса  (Without Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Сеня', 'leva': 'Федя'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the kitchen, the cooks are enjoying a rare moment of peace and quiet. Senya notes how great the atmosphere is today, and Fedya quickly points out the reason. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Я не думал, что тут так классно.",
     "I didn't think it was so great here.",
     [(170, 'Я не думал, что на кухне так классно.')], "adapted"),
    ("leva", "Везде классно, когда нет Макса.",
     "It is great everywhere when there is no Max.",
     [(171, 'Без Макса везде классно.')], "adapted"),
    ("anya", "Да, сегодня очень тихо.",
     "Yes, it is very quiet today.",
     [], "new"),
    ("leva", "Нам надо работать.",
     "We need to work.",
     [], "new"),
    ("anya", "Я просто отдыхаю.",
     "I am just resting.",
     [], "new"),
    ("leva", "Шеф может прийти.",
     "The chef can come.",
     [], "new"),
    ("anya", "Шеф сейчас занят.",
     "The chef is busy now.",
     [], "new"),
    ("leva", "Всё равно, давай работать.",
     "Anyway, let's work.",
     [], "new"),
    ("anya", "Хорошо, я иду.",
     "Good, I am coming.",
     [], "new"),
    ("leva", "Где мой нож?",
     "Where is my knife?",
     [], "new"),
    ("anya", "Он на столе.",
     "It is on the table.",
     [], "new"),
    ("leva", "Спасибо, я вижу.",
     "Thank you, I see it.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'I didn't think it was so great here.' -- The speaker makes the statement."),
    (1, None,
     "'It is great everywhere when there is no Max.' -- The speaker makes the statement."),
    (2, None,
     "'Yes, it is very quiet today.' -- The speaker makes the statement."),
    (3, None,
     "'We need to work.' -- The speaker makes the statement."),
    (4, None,
     "'I am just resting.' -- The speaker makes the statement."),
    (5, None,
     "'The chef can come.' -- The speaker makes the statement."),
    (6, None,
     "'The chef is busy now.' -- The speaker makes the statement."),
    (7, None,
     "'Anyway, let's work.' -- The speaker makes the statement."),
    (8, None,
     "'Good, I am coming.' -- The speaker makes the statement."),
    (9, None,
     "'Where is my knife?' -- The speaker makes the statement."),
    (10, None,
     "'It is on the table.' -- The speaker makes the statement."),
    (11, None,
     "'Thank you, I see it.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Спасибо, я вижу.")
