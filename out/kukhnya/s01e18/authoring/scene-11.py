ID = "kukhnya-s01e18-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 11
TITLE = "Мы приехали  (We Arrived)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 11"

INTRO = "The guys arrive at their destination and hesitate before going inside. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Ну что, мы приехали?",
     "Well what, we arrived?",
     [(1, "девушки")], "adapted"),
    ("kostya", "Да, мы на месте.",
     "Yes, we are in place.",
     [(1, "девушки")], "adapted"),
    ("anya", "Нас уже ждут?",
     "Are they waiting for us already?",
     [(1, "девушки")], "adapted"),
    ("kostya", "Да, они нас ждут.",
     "Yes, they are waiting for us.",
     [(1, "девушки")], "new"),
    ("anya", "Пошли узнаем, как дела.",
     "Let's go find out how things are.",
     [(1, "девушки")], "adapted"),
    ("kostya", "Я немного волнуюсь.",
     "I am a little worried.",
     [(1, "девушки")], "new"),
    ("anya", "Ребята, послушайте меня.",
     "Guys, listen to me.",
     [(1, "девушки")], "adapted"),
    ("anya", "Я хочу вам что-то сказать.",
     "I want to tell you something.",
     [(1, "девушки")], "new"),
    ("anya", "В последние дни я перегибал палку.",
     "In the last days I went overboard.",
     [(1, "девушки")], "adapted"),
    ("anya", "Я вел себя очень плохо.",
     "I behaved very badly.",
     [(1, "девушки")], "new"),
    ("kostya", "Мы понимаем тебя.",
     "We understand you.",
     [(1, "девушки")], "new"),
    ("anya", "Спасибо вам за поддержку.",
     "Thank you for the support.",
     [(1, "девушки")], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Well what, we arrived?' -- ENG He asks him a question."),
    (1, None,
     "'Yes, we are in place.' -- ENG He says this to him."),
    (2, None,
     "'Are they waiting for us already?' -- ENG He asks him a question."),
    (3, None,
     "'Yes, they are waiting for us.' -- ENG He says this to him."),
    (4, None,
     "'Let's go find out how things are.' -- ENG He says this to him."),
    (5, None,
     "'I am a little worried.' -- ENG He explains his feelings to him."),
    (6, None,
     "'Guys, listen to me.' -- ENG He says this to him."),
    (7, None,
     "'I want to tell you something.' -- ENG He talks directly to him."),
    (8, None,
     "'In the last days I went overboard.' -- ENG He explains his feelings to him."),
    (9, None,
     "'I behaved very badly.' -- ENG He explains his feelings to him."),
    (10, None,
     "'We understand you.' -- ENG He says this to him."),
    (11, None,
     "'Thank you for the support.' -- ENG He talks directly to him."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "They gather their courage and finally walk into the room together."
CLOSING = ("anya", "Спасибо вам за поддержку.")
