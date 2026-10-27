"""Scene 32 — The Whole World Against Us (s01e08, 00:21:40–00:22:00)."""

ID = "kukhnya-s01e08-scene-32"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 32
TITLE = "Весь мир против нас  (The Whole World Against Us)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
}

INTRO = (
    "In his private office at Claude Monet, Chef Viktor Barinov fumes alone in deep suspicion. "
    "Watching his boss stew over imagined enemies, Max reflects on how people mistakenly believe the world is plotted against them."
)

STORY = [
    ("chef", "Кругом одни предатели и шпионы!",
     "Traitors and spies are all around!",
     [], "Chef rants in office"),

    ("anya", "Шеф, никто против вас не замышляет зла.",
     "Chef, nobody is plotting evil against you.",
     [], "Max tries to calm him"),

    ("chef", "Ты ничего не понимаешь в людях, огузок!",
     "You understand nothing about people, runt!",
     [], "Chef snaps"),

    ("anya", "Люди часто сами создают себе проблемы.",
     "People often create problems for themselves.",
     [], "Max observes"),

    ("anya", "Третьи ошибочно думают, что весь мир против них.",
     "Others mistakenly think the whole world is against them.",
     [(362, "Третьи ошибочно думают, что весь мир настроен против них.")], "Max notes paranoia"),

    ("chef", "Они просто завидуют моему великому таланту!",
     "They are simply jealous of my great talent!",
     [], "Chef boasts"),

    ("anya", "Но постоянные подозрения только портят жизнь.",
     "But constant suspicions only ruin life.",
     [], "Max reasons"),

    ("chef", "Осторожность на кухне никогда не бывает лишней.",
     "Caution in the kitchen is never unnecessary.",
     [], "Chef defends distrust"),

    ("anya", "Иногда полезно просто доверять своим поварам.",
     "Sometimes it is useful to simply trust your cooks.",
     [], "Max advises"),

    ("chef", "Я доверяю только своей родной сковородке.",
     "I trust only my own frying pan.",
     [], "Chef grumbles"),

    ("anya", "С таким настроением трудно радоваться жизни.",
     "With such a mood it is hard to enjoy life.",
     [], "Max reflects"),

    ("chef", "Хватит читать мне лекции, иди нарезать лук!",
     "Enough lecturing me, go chop onions!",
     [], "Chef orders"),

    ("anya", "Слушаюсь, шеф, уже бегу на кухню.",
     "Right away, chef, I am already running to the kitchen.",
     [], "Max complies"),

    ("anya", "Страх мешает людям видеть правду вокруг.",
     "Fear prevents people from seeing the truth around them.",
     [], "Max concludes"),
]

OPENER = "Let's explore Chef Barinov's paranoid brooding and Max's thoughts on distrust."

WALK = [
    (0, None,
     "'Traitors and spies are all around!' Chef Barinov paces furiously in his private office."),
    (1, None,
     "'Chef, nobody is plotting evil against you.' Max tries to calm his temperamental boss."),
    (2, None,
     "'You understand nothing about people, runt!' The head chef brushes off his advice immediately."),
    (3, None,
     "'People often create problems for themselves.' Max observes human nature with a clear eye."),
    (4, None,
     "'Others mistakenly think the whole world is against them.' Max reflects on self-destructive paranoia in people."),
    (5, None,
     "'They are simply jealous of my great talent!' Barinov claims his culinary skill invites jealousy."),
    (6, None,
     "'But constant suspicions only ruin life.' Max urges openness instead of perpetual distrust."),
    (7, None,
     "'Caution in the kitchen is never unnecessary.' The chef defends his paranoid habits on the job."),
    (8, None,
     "'Sometimes it is useful to simply trust your cooks.' Max advocates for genuine teamwork in the restaurant."),
    (9, None,
     "'I trust only my own frying pan.' Barinov grumbles about depending on other people in life."),
    (10, None,
     "'With such a mood it is hard to enjoy life.' Max notes that cynicism darkens every single day."),
    (11, None,
     "'Enough lecturing me, go chop onions!' The chef abruptly terminates the philosophical discussion."),
    (12, None,
     "'Right away, chef, I am already running to the kitchen.' Max hurries out to complete the prep."),
    (13, None,
     "'Fear prevents people from seeing the truth around them.' Max concludes his thoughts on trust."),
]

TRANSITION = "Now let's listen to the heated office dialogue and Max's reflection once more."

OUTRO = "Even amid Barinov's loud suspicions, Max holds on to the value of trust and openness."

CLOSING = ("anya", "Страх мешает людям видеть правду вокруг.")
