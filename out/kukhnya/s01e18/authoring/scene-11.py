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
     "'Well what, we arrived?' The question word for 'what' comes right at the start, followed directly by 'we've arrived'."),
    (1, None,
     "'Yes, we are in place.' Notice the word order: 'we' comes first, and 'place' finishes the sentence."),
    (2, None,
     "'Are they waiting for us already?' Here 'us' sets up the idea, while 'are waiting' comes at the end for emphasis. Kostya answers straight away."),
    (3, None,
     "'Yes, they are waiting for us.' Here 'they' sets up the idea, while 'are waiting' comes at the end for emphasis."),
    (4, None,
     "'Let's go find out how things are.' Listen for the word meaning 'let's go' right alongside 'will find out' in this line."),
    (5, None,
     "'I am a little worried.' Kostya starts with 'I' and pairs it with 'a bit' to make the point clear. Then Max replies."),
    (6, None,
     "'Guys, listen to me.' Listen for the word meaning 'the boys' right alongside 'listen' in this line."),
    (7, None,
     "'I want to tell you something.' In Russian, 'I' leads into 'tell' in a very natural everyday phrasing."),
    (8, None,
     "'In the last days I went overboard.' The first content word means 'last', and 'stick' rounds out the thought."),
    (9, None,
     "'I behaved very badly.' A compact expression built around 'I' and 'badly'."),
    (10, None,
     "'We understand you.' Listen for the word meaning 'we' right alongside 'to understand' in this line."),
    (11, None,
     "'Thank you for the support.' In Russian, 'thank you' leads into 'support' in a very natural everyday phrasing."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "They gather their courage and finally walk into the room together."
CLOSING = ("anya", "Спасибо вам за поддержку.")
