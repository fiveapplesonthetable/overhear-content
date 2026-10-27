ID = "kukhnya-s01e12-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 12
TITLE = "Ссора понарошку  (Pretend Quarrel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 101-111. Nastya convinces Kostya that Victoria's workplace romance ban is aimed at them, "
    "and proposes staging a fake argument to fool her."
)

INTRO = (
    "In the restaurant dining room, Nastya is terrified that the sudden ban on workplace romances "
    "was provoked by her relationship with Kostya. She urges Kostya to stage a fake quarrel "
    "to convince management that they are no longer together. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, этот новый запрет из-за нас!",
     "Kostya, this new ban is because of us!",
     [(101, "Это из-за нас.")], "adapted"),
    ("kostya", "Но с чего ты это взяла?",
     "But what makes you think that?",
     [(103, "С чего ты взяла?")], "adapted"),
    ("anya", "Потому что только у нас тайные отношения.",
     "Because only we have a secret relationship.",
     [(103, "Потому что только у нас отношения.")], "adapted"),
    ("kostya", "Виктория просто заботится о дисциплине зала.",
     "Victoria simply cares about the dining room discipline.",
     [], "new"),
    ("anya", "Она очень подозрительно посмотрела на нас.",
     "She looked at us very suspiciously.",
     [(104, "она вот так посмотрела.")], "adapted"),
    ("kostya", "Тебе показалось, она смотрела на всех.",
     "You imagined it, she was looking at everyone.",
     [], "new"),
    ("anya", "Я прекрасно знаю этот строгий взгляд!",
     "I know that strict look very well!",
     [(105, "Я знаю этот взгляд.")], "adapted"),
    ("kostya", "И что же нам теперь делать?",
     "And what should we do now?",
     [], "new"),
    ("anya", "Нам нужно срочно поругаться перед ней.",
     "We need to quarrel in front of her right away.",
     [(106, "Нам надо поругаться.")], "adapted"),
    ("kostya", "Зачем нам ругаться в ресторане?",
     "Why should we quarrel in the restaurant?",
     [(106, "Как поругаться?")], "adapted"),
    ("anya", "Мы поругаемся понарошку, только для вида.",
     "We will quarrel in pretend, only for show.",
     [(107, "Ну, понарошку..."), (108, "а сейчас поругаемся понарошку.")], "adapted"),
    ("kostya", "Ты уверена, что это хороший план?",
     "Are you sure that this is a good plan?",
     [], "new"),
    ("anya", "Вика должна поверить, что мы расстались.",
     "Vika must believe that we broke up.",
     [(109, "Но главное, чтобы Виктория Сергеевна подумала, что мы не встречаемся.")], "adapted"),
    ("kostya", "Хорошо, давай устроим этот спектакль.",
     "All right, let us put on this show.",
     [(110, "Давай.")], "adapted"),
]

OPENER = "Now let us examine Nastya and Kostya's secret plan line by line."

WALK = [
    (0, None,
     "'Kostya, this new ban is because of us!' -- Nastya is convinced that the announcement targets their romance."),
    (1, None,
     "'But what makes you think that?' -- Kostya questions her assumption with surprise."),
    (2, None,
     "'Because only we have a secret relationship.' -- Nastya points out that they are the only couple."),
    (3, None,
     "'Victoria simply cares about the dining room discipline.' -- Kostya believes it is just general management."),
    (4, None,
     "'She looked at us very suspiciously.' -- Nastya describes the pointed glance from the manager."),
    (5, None,
     "'You imagined it, she was looking at everyone.' -- Kostya tries to calm her down with reason."),
    (6, None,
     "'I know that strict look very well!' -- Nastya insists that she correctly read the expression of the manager."),
    (7, None,
     "'And what should we do now?' -- Kostya asks what action they should take next."),
    (8, None,
     "'We need to quarrel in front of her right away.' -- Nastya proposes staging an argument before Victoria."),
    (9, None,
     "'Why should we quarrel in the restaurant?' -- Kostya does not understand the point of fighting in public."),
    (10, None,
     "'We will quarrel in pretend, only for show.' -- Nastya explains that it is purely an act."),
    (11, None,
     "'Are you sure that this is a good plan?' -- Kostya expresses slight doubt about the risky scheme."),
    (12, None,
     "'Vika must believe that we broke up.' -- Nastya wants the manager to think they are no longer dating."),
    (13, None,
     "'All right, let us put on this show.' -- Kostya finally agrees to participate in the act."),
]

TRANSITION = "Now let us listen to Nastya and Kostya once again."
OUTRO = (
    "Worried about losing their jobs, Nastya convinces Kostya to pretend to fight, "
    "setting up their comedic performance in front of Victoria at the bar."
)
CLOSING = ("kostya", "Хорошо, давай устроим этот спектакль.")
