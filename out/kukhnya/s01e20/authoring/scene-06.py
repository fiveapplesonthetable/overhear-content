ID = "kukhnya-s01e20-scene-06"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 6
TITLE = "Нам надо поговорить  (We Need to Talk)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 6"

INTRO = "In the restaurant, Nastya stops Kostya because she wants to have a very serious conversation, and we will listen to their dialogue in Russian first; do not worry about catching every single word."

STORY = [
    ("anya", "Костя, нам надо поговорить.",
     "Kostya, we have to talk.",
     [], "new"),
    ("kostya", "Это может подождать?",
     "Can it wait?",
     [], "new"),
    ("anya", "Нет, это важно.",
     "No, it is important.",
     [], "new"),
    ("kostya", "Настя, я так по тебе соскучился.",
     "Nastya, I have missed you so much.",
     [], "new"),
    ("anya", "Пожалуйста, послушай меня.",
     "Please, listen to me.",
     [], "new"),
    ("kostya", "Я тебя слушаю.",
     "I am listening to you.",
     [], "new"),
    ("anya", "Наши отношения развиваются быстро.",
     "Our relationship is moving fast.",
     [], "new"),
    ("kostya", "Я думаю, это отлично.",
     "I think this is great.",
     [], "new"),
    ("anya", "Но нам надо обсудить наше будущее.",
     "But we need to discuss our future.",
     [], "new"),
    ("kostya", "У нас есть много времени.",
     "We have a lot of time.",
     [], "new"),
    ("anya", "Нет, время пришло сейчас.",
     "No, the time is now.",
     [], "new"),
    ("kostya", "Хорошо, я готов поговорить.",
     "Okay, I am ready to talk.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Kostya, we have to talk.' -- She tells him this."),
    (1, None,
     "'Can it wait?' -- He asks her a question."),
    (2, None,
     "'No, it is important.' -- She tells him this."),
    (3, None,
     "'Nastya, I have missed you so much.' -- He talks directly to her."),
    (4, None,
     "'Please, listen to me.' -- She tells him this."),
    (5, None,
     "'I am listening to you.' -- He talks directly to her."),
    (6, None,
     "'Our relationship is moving fast.' -- She tells him this."),
    (7, None,
     "'I think this is great.' -- He explains his feelings to her."),
    (8, None,
     "'But we need to discuss our future.' -- She tells him this."),
    (9, None,
     "'We have a lot of time.' -- He says this to her."),
    (10, None,
     "'No, the time is now.' -- She tells him this."),
    (11, None,
     "'Okay, I am ready to talk.' -- He explains his feelings to her."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya finally realizes that he cannot avoid this serious conversation with her."
CLOSING = ("kostya", "Хорошо, я готов поговорить.")
