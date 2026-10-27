# Authoring module for kukhnya s01e17 scene 23 (cues 327-331).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-23.py --out out/kukhnya/s01e17/scene-23.json

ID = "kukhnya-s01e17-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 23
TITLE = "Тайна паспорта  (The Secret of the Passport)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "senya": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 327-331. Chef Viktor looks at Max's passport and discovers that his birthday is actually in February."
)

INTRO = (
    "During the celebration in the kitchen, Chef Viktor examines Max's passport on the counter. "
    "Looking at the official stamp, Viktor notices that Max's birthday is actually in February, "
    "uncovering Max's well-intentioned lie. Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this surprising revelation line by line."

STORY = [
    ("chef", "Покажи мне свой паспорт, Макс.", "Show me your passport, Max.",
     [(327, "Паспорте!")], "adapted"),
    ("anya", "Вот мой паспорт, шеф.", "Here is my passport, chef.",
     [(327, "Паспорте!")], "adapted"),
    ("chef", "А почему день рождения в феврале?", "And why is the birthday in February?",
     [(327, "А что это тебе день рождения в феврале, а?")], "adapted"),
    ("senya", "Твой день рождения не сегодня?", "Your birthday is not today?",
     [(327, "день рождения в феврале")], "adapted"),
    ("anya", "Я хотел сделать вам приятное.", "I wanted to please you.",
     [(329, "чтобы сделать тебе приятное")], "adapted"),
    ("chef", "Ты соврал нам про праздник?", "Did you lie to us about the holiday?",
     [(330, "немножко соврать")], "adapted"),
    ("anya", "Я хотел забыть все обиды.", "I wanted to forget all grudges.",
     [(328, "забыть свои обиды")], "adapted"),
    ("senya", "Но врать друзьям нельзя.", "But one must not lie to friends.",
     [(330, "соврать")], "adapted"),
    ("chef", "Любая ложь — это плохо.", "Any lie is bad.",
     [(331, "за любое вранье")], "adapted"),
    ("anya", "Я очень виноват перед вами.", "I am very guilty before you.",
     [(331, "приходится платить")], "adapted"),
    ("chef", "За любой обман надо отвечать.", "For any deceit one must answer.",
     [(331, "за любое вранье рано или поздно приходится платить.")], "adapted"),
    ("senya", "Правда всегда открывается.", "The truth always reveals itself.",
     [(331, "Правда")], "adapted"),
    ("anya", "За любой обман приходится платить.", "For any deceit one has to pay.",
     [(331, "за любое вранье рано или поздно приходится платить.")], "adapted"),
]

WALK = [
    (0, None,
     "'Show me your passport, Max.' -- Chef Viktor asks to inspect the document."),
    (1, None,
     "'Here is my passport, chef.' -- Max hands over his official ID to the boss."),
    (2, None,
     "'And why is the birthday in February?' -- The chef spots the contradictory date in the passport."),
    (3, None,
     "'Your birthday is not today?' -- Senya expresses surprise at the sudden revelation."),
    (4, None,
     "'I wanted to please you.' -- Max explains his benevolent motivation to them."),
    (5, None,
     "'Did you lie to us about the holiday?' -- The chef questions his honesty with concern."),
    (6, None,
     "'I wanted to forget all grudges.' -- Max admits that he sought peace."),
    (7, None,
     "'But one must not lie to friends.' -- Senya reminds him of the importance of loyalty."),
    (8, None,
     "'Any lie is bad.' -- Viktor states a fundamental moral truth to the team."),
    (9, None,
     "'I am very guilty before you.' -- Max takes responsibility for his mistake."),
    (10, None,
     "'For any deceit one must answer.' -- The chef insists on accountability for the act."),
    (11, None,
     "'The truth always reveals itself.' -- Senya notes that secrets are revealed in the end."),
    (12, None,
     "'For any deceit one has to pay.' -- Max accepts the difficult lesson."),
]

TRANSITION = "Now let's listen to the passport discovery again without interruption."
OUTRO = (
    "Faced with the undeniable proof in his passport, Max realizes that even a lie told "
    "for good reasons carries serious consequences."
)
CLOSING = ("anya", "За любой обман приходится платить.")
