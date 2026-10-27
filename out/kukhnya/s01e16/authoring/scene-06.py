ID = "kukhnya-s01e16-scene-06"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 6
TITLE = "Звонок в инспекцию  (Call to the Inspection)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Шеф", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 51. Chef Viktor gloats to Senya as migration inspectors raid rival restaurant Arcobaleno, "
    "pleased with the chaos caused by his anonymous phone call."
)

INTRO = (
    "In the kitchen of Claude Monet, Chef Viktor stands by the window with a triumphant grin. "
    "Senya notices his cheerful mood and asks what is going on. Viktor points to the courtyard, "
    "where migration inspectors are descending upon Arcobaleno. Let us listen to their conversation in Russian first."
)

STORY = [
    ("senya", "Шеф, почему вы так весело улыбаетесь?",
     "Chef, why are you smiling so cheerfully?",
     [], "new"),
    ("anya", "Посмотри во двор на соседний ресторан.",
     "Look into the courtyard at the neighboring restaurant.",
     [], "new"),
    ("senya", "Туда только что приехала строгая проверка!",
     "A strict inspection just arrived over there!",
     [], "new"),
    ("anya", "Да, это специальная служба пришла туда.",
     "Yes, that is a special service arriving.",
     [], "new"),
    ("senya", "Вы сами позвонили в эту инспекцию?",
     "Did you call this inspection yourself?",
     [], "new"),
    ("anya", "Конечно, они должны уважать правила порядка.",
     "Of course, they must respect the rules of order.",
     [], "new"),
    ("senya", "Теперь их повара будут сильно бегать.",
     "Now their cooks will be running around a lot.",
     [], "new"),
    ("anya", "Пусть они быстро бегают вокруг здания!",
     "Let them quickly run around the building!",
     [(51, "Сейчас вы побегаете.")], "adapted"),
    ("senya", "Елена Павловна будет очень сильно злиться.",
     "Elena Pavlovna will be extremely furious.",
     [], "new"),
    ("anya", "Она не должна была ставить машину здесь.",
     "She should not have parked her car here.",
     [], "new"),
    ("senya", "Это действительно очень жестокая маленькая месть.",
     "This is indeed very cruel little revenge.",
     [], "new"),
    ("anya", "Это справедливый урок для наглых соседей.",
     "This is a fair lesson for insolent neighbors.",
     [], "new"),
    ("senya", "Тогда давайте спокойно смотреть в окно!",
     "Then let us calmly watch out the window!",
     [], "new"),
]

OPENER = "Now let us examine Viktor and Senya's conversation at the window line by line."

WALK = [
    (0, None,
     "'Chef, why are you smiling so cheerfully?' -- Senya asks about Viktor's unusually pleased mood in the kitchen."),
    (1, None,
     "'Look into the courtyard at the neighboring restaurant.' -- The chef directs his cook's attention to the outside drama."),
    (2, None,
     "'A strict inspection just arrived over there!' -- Senya notices official cars pulling up outside Arcobaleno."),
    (3, None,
     "'Yes, that is a special service arriving.' -- Viktor explains that an official enforcement service arrived."),
    (4, None,
     "'Did you call this inspection yourself?' -- The cook immediately guesses who was behind the anonymous tip."),
    (5, None,
     "'Of course, they must respect the rules of order.' -- Viktor self-righteously justifies his punitive complaint."),
    (6, None,
     "'Now their cooks will be running around a lot.' -- Senya imagines the panic unfolding inside the rival kitchen."),
    (7, None,
     "'Let them quickly run around the building!' -- The head chef gloats maliciously over their frantic predicament."),
    (8, None,
     "'Elena Pavlovna will be extremely furious.' -- Senya anticipates the rival head chef's inevitable explosion."),
    (9, None,
     "'She should not have parked her car here.' -- Viktor brings up the parking dispute that sparked the war."),
    (10, None,
     "'This is indeed very cruel little revenge.' -- Senya acknowledges the harshness of Viktor's petty retaliation."),
    (11, None,
     "'This is a fair lesson for insolent neighbors.' -- Viktor stands by his action as righteous retribution."),
    (12, None,
     "'Then let us calmly watch out the window!' -- Senya joins Viktor to enjoy watching the chaos next door."),
]

TRANSITION = "Now let us listen to Viktor and Senya once again."
OUTRO = (
    "Satisfied with his successful revenge on Elena Pavlovna, Viktor watches happily "
    "as the migration raid throws the rival restaurant into complete disarray."
)
CLOSING = ("senya", "Тогда давайте спокойно смотреть в окно!")
