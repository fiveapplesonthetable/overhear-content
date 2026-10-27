ID = "kukhnya-s01e16-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 10
TITLE = "Побег через зал  (Escape Through the Hall)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "dima": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Шеф', 'dima': 'Лановский'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 88-131."

INTRO = (
    "Viktor tells the kitchen staff to leave through the back and front doors. But the back door is blocked. An immigration major introduces himself to Viktor. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Попробуй новый вариант блюда.",
     "Try the new version of the dish.",
     [(88, "попробуй новый вариант, а?")], "adapted"),
    ("anya", "Шеф, выход через зал закрыт.",
     "Chef, the exit through the hall is closed.",
     [(108, "Шеф, с парадом не вариант.")], "adapted"),
    ("leva", "Мы выходим по одному человеку.",
     "We exit one person at a time.",
     [(92, "Не ломимся толпой, выходим по одному человеку.")], "adapted"),
    ("leva", "Половина идёт через зал.",
     "Half goes through the hall.",
     [(97, "Половина через зал.")], "adapted"),
    ("leva", "Что вы за идиоты?",
     "What kind of idiots are you?",
     [(110, "Что вы за инвалиды?")], "adapted"),
    ("leva", "Быстро ко мне в кабинет.",
     "Quickly to my office.",
     [(113, "Ко мне в кабинет, только тихо.")], "adapted"),
    ("dima", "Добрый день, Виктор Петрович.",
     "Good afternoon, Viktor Petrovich.",
     [(117, "О, Виктор Петрович, чрезвычайно рад с вами лично познакомиться.")], "adapted"),
    ("dima", "Я майор миграционной службы.",
     "I am a major of the migration service.",
     [(121, "майор федеральной миграционной службы.")], "adapted"),
    ("dima", "Мы можем пройти в кабинет?",
     "Can we go to the office?",
     [(124, "Виктор Петрович, мы не могли бы пройти в ваш кабинет и обсудить все там?")], "adapted"),
    ("leva", "К сожалению, я не могу.",
     "Unfortunately, I cannot.",
     [(125, "К сожалению, не могу.")], "adapted"),
    ("leva", "Мне нужно готовить для гостей.",
     "I need to cook for the guests.",
     [(127, "Простите, мне нужно готовить для гостей нашего замечательного ареста.")], "adapted"),
    ("dima", "Хорошо, я подожду вас здесь.",
     "Alright, I will wait for you here.",
     [(131, "Я, с вашего позволения, подожду вас здесь.")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Try the new version of the dish.' -- The speaker states this. ENG"),
    (1, None,
     "'Chef, the exit through the hall is closed.' -- The speaker states this. ENG"),
    (2, None,
     "'We exit one person at a time.' -- The speaker states this. ENG"),
    (3, None,
     "'Half goes through the hall.' -- The speaker states this. ENG"),
    (4, None,
     "'What kind of idiots are you?' -- The speaker states this. ENG"),
    (5, None,
     "'Quickly to my office.' -- The speaker states this. ENG"),
    (6, None,
     "'Good afternoon, Viktor Petrovich.' -- The speaker states this. ENG"),
    (7, None,
     "'I am a major of the migration service.' -- The speaker states this. ENG"),
    (8, None,
     "'Can we go to the office?' -- The speaker states this. ENG"),
    (9, None,
     "'Unfortunately, I cannot.' -- The speaker states this. ENG"),
    (10, None,
     "'I need to cook for the guests.' -- The speaker states this. ENG"),
    (11, None,
     "'Alright, I will wait for you here.' -- The speaker states this. ENG"),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("dima", "Хорошо, я подожду вас здесь.")
