"""Scene 17 — Visiting Kostya (s01e07, 00:21:45–00:22:38)."""

ID = "kukhnya-s01e07-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 17
TITLE = "В гостях у Кости  (Visiting Kostya)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 333-342. Nastya visits Kostya's rented apartment, but upon discovering "
    "a mouse in a mousetrap, the horrified vegetarian calls him a murderer and storms out."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
}

INTRO = (
    "Hoping to spend a quiet romantic evening together, bartender Kostya invites waitress Nastya "
    "over to his small rented apartment. "
    "Everything seems promising until the passionate animal lover catches sight of a wooden mousetrap on the floor, "
    "sparking an emotional explosion that shatters their romantic mood. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Настя, добро пожаловать в мою квартиру.",
     "Nastya, welcome to my apartment.",
     [], "Kostya welcomes Nastya"),

    ("anya", "У тебя здесь довольно уютно и чисто.",
     "It is quite cozy and clean here with you.",
     [], "Nastya compliments room"),

    ("kostya", "Ну, точнее, эта квартира съёмная.",
     "Well, more precisely, this apartment is rented.",
     [(333, "не моя съемная")], "Kostya clarifies lease"),

    ("kostya", "Вот диван, стул, мягкая подушка.",
     "Here is a couch, a chair, a soft pillow.",
     [(334, "Диван, стул"), (335, "Подушка")], "Showing furniture"),

    ("anya", "Костя, я всё это отлично вижу.",
     "Kostya, I can see all this perfectly.",
     [(335, "Кость, я вижу")], "Nastya nods"),

    ("kostya", "Проходи скорее и садись на диван.",
     "Come in quickly and sit on the couch.",
     [(336, "Проходи, проходи. Садись")], "Inviting to sit"),

    ("anya", "Ой, а что это там внизу?",
     "Oh, and what is that down there?",
     [(337, "Что это?")], "Noticing floor"),

    ("anya", "Боже мой, это же мёртвая мышь!",
     "My God, that is a dead mouse!",
     [(338, "Это…")], "Spotting mouse"),

    ("anya", "Костя, ты самый настоящий жестокий убийца!",
     "Kostya, you are a real cruel murderer!",
     [(338, "Ты убийца")], "Accusing Kostya"),

    ("anya", "Ты погубил маленькую беззащитную мышь!",
     "You destroyed a little defenseless mouse!",
     [(339, "Убил маленькую ни в чем не повинную мышь")], "Mourning the mouse"),

    ("kostya", "Настя, но это обычная мышеловка!",
     "Nastya, but this is an ordinary mousetrap!",
     [], "Kostya defends trap"),

    ("anya", "Ты ещё сидишь и спокойно улыбаешься?!",
     "You are still sitting and calmly smiling?!",
     [(340, "Еще лыбится сидит")], "Horrified by smile"),

    ("anya", "Ты поступил как настоящий монстр!",
     "You acted like a real monster!",
     [(342, "Ты вообще монстр")], "Nastya condemns Kostya"),
]

OPENER = "Now let's examine Kostya and Nastya's apartment visit line by line."

WALK = [
    (0, None,
     "'Nastya, welcome to my apartment.' Kostya opens the door and welcomes his guest inside."),
    (1, None,
     "'It is quite cozy and clean here with you.' Nastya looks around the small room with genuine curiosity."),
    (2, None,
     "'Well, more precisely, this apartment is rented.' The bartender clarifies the legal status of his modest home."),
    (3, None,
     "'Here is a couch, a chair, a soft pillow.' Kostya enthusiastically lists all the basic furniture in the room."),
    (4, None,
     "'Kostya, I can see all this perfectly.' Nastya interrupts his awkward tour with gentle amusement."),
    (5, None,
     "'Come in quickly and sit on the couch.' Kostya hospitably invites the waitress to make herself comfortable."),
    (6, None,
     "'Oh, and what is that down there?' Nastya suddenly notices a strange object near the baseboard."),
    (7, None,
     "'My God, that is a dead mouse!' She gasps in utter horror upon recognizing the small rodent."),
    (8, None,
     "'Kostya, you are a real cruel murderer!' The passionate animal lover vents her moral fury at the bartender."),
    (9, None,
     "'You destroyed a little defenseless mouse!' Nastya is heartbroken by the tragic fate of the innocent creature."),
    (10, None,
     "'Nastya, but this is an ordinary mousetrap!' Kostya tries to defend himself with practical household logic."),
    (11, None,
     "'You are still sitting and calmly smiling?!' She accuses him of complete callousness and lack of empathy."),
    (12, None,
     "'You acted like a real monster!' Nastya turns on her heel and storms out into the corridor."),
]

TRANSITION = "Now let's listen to Kostya and Nastya once more without interruption."

OUTRO = (
    "What was meant to be a cozy evening turns into a dramatic breakup over a household mousetrap."
)

CLOSING = ("anya", "Ты поступил как настоящий монстр!")
