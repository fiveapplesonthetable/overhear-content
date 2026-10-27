"""Scene 41 — Suspicious Caviar (s01e10, 00:20:57–00:21:14)."""

ID = "kukhnya-s01e10-scene-41"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 41
TITLE = "Подозрительная икра  (Suspicious Caviar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Нагиев",
    "chef": "Шеф",
}

INTRO = (
    "In the lavish dining hall of Claude Monet, restaurant owner Dmitry Nagiyev summons Chef Viktor Barinov to his table. "
    "Eyeing a plate of strangely colored black caviar intended for wealthy guests, Nagiyev demands an immediate and honest explanation."
)

STORY = [
    ("anya", "Витя, иди скорее сюда к столу!",
     "Vitya, come quickly here to the table!",
     [], "Nagiyev calls"),

    ("chef", "Что случилось, Дмитрий Владимирович, в чём дело?",
     "What happened, Dmitry Vladimirovich, what is the matter?",
     [], "Barinov asks"),

    ("anya", "Витя, скажи мне прямо, это чего?",
     "Vitya, tell me straight, what is this?",
     [(293, "Вить, это чего?")], "Nagiyev points"),

    ("chef", "Чего? Вот это на тарелке чего?",
     "What? What is this on the plate?",
     [(294, "Чего? Вот это чего?")], "Chef acts dumb"),

    ("chef", "Это самая настоящая свежая русская икра.",
     "This is real fresh Russian caviar.",
     [(295, "Икра.")], "Chef claims"),

    ("chef", "Причём очень дорогая и очень хорошая икра!",
     "And very expensive and very good caviar!",
     [(296, "Причем очень хорошая.")], "Chef praises"),

    ("anya", "Витя, ты совсем дурак или притворяешься?",
     "Vitya, are you a complete fool or pretending?",
     [(297, "Вить, ты дурак?")], "Nagiyev fumes"),

    ("chef", "В каком смысле дурак, не понимаю вас!",
     "In what sense a fool, I do not understand you!",
     [(297, "В смысле?")], "Chef defends"),

    ("anya", "Вот это чего, я тебя строго спрашиваю?!",
     "What is this, I am strictly asking you?!",
     [(298, "Вот это чего я тебя спрашиваю?")], "Nagiyev demands"),

    ("chef", "Гости просили чёрную икру к праздничному столу.",
     "The guests asked for black caviar for the holiday table.",
     [], "Chef explains request"),

    ("anya", "Но цвет у этой икры странный и подозрительный.",
     "But the color of this caviar is strange and suspicious.",
     [], "Nagiyev inspects"),

    ("chef", "Особый свет в зале меняет все оттенки.",
     "Special lighting in the hall changes all shades.",
     [], "Chef makes excuse"),

    ("anya", "Не ври мне, говори сейчас всю правду!",
     "Do not lie to me, tell the whole truth now!",
     [], "Nagiyev insists"),
]

OPENER = "Let's watch Nagiyev confront Chef Barinov over suspicious caviar served in the main dining hall."

WALK = [
    (0, None,
     "'Vitya, come quickly here to the table!' Nagiyev calls the head chef into the dining room."),
    (1, None,
     "'What happened, Dmitry Vladimirovich, what is the matter?' Barinov asks with a nervous smile."),
    (2, None,
     "'Vitya, tell me straight, what is this?' Nagiyev points grimly at the plate."),
    (3, None,
     "'What? What is this on the plate?' Chef Viktor pretends not to understand."),
    (4, None,
     "'This is real fresh Russian caviar.' Barinov maintains his innocent facade."),
    (5, None,
     "'And very expensive and very good caviar!' The chef insists on the quality."),
    (6, None,
     "'Vitya, are you a complete fool or pretending?' Nagiyev snaps with rising frustration."),
    (7, None,
     "'In what sense a fool, I do not understand you!' Barinov feigns deep offense."),
    (8, None,
     "'What is this, I am strictly asking you?!' Nagiyev demands an honest explanation."),
    (9, None,
     "'The guests asked for black caviar for the holiday table.' The chef describes the special order."),
    (10, None,
     "'But the color of this caviar is strange and suspicious.' The restaurant owner leans in close."),
    (11, None,
     "'Special lighting in the hall changes all shades.' Barinov invents a clumsy excuse."),
    (12, None,
     "'Do not lie to me, tell the whole truth now!' Nagiyev gives his chef a final warning."),
]

TRANSITION = "Now let's listen to Nagiyev's sharp interrogation and Barinov's awkward excuses once more."

OUTRO = "Cornered by his sharp-eyed boss in front of empty tables, Barinov realizes his culinary deception cannot last."

CLOSING = ("anya", "Не ври мне, говори сейчас всю правду!")
