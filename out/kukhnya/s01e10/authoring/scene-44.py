"""Scene 44 — The Chef's Fury (s01e10, 00:22:38–00:22:39)."""

ID = "kukhnya-s01e10-scene-44"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 44
TITLE = "Гнев шефа  (The Chef's Fury)"
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
    "anya": "Макс",
    "chef": "Шеф",
}

INTRO = (
    "Following Spartak's bitter failure on the pitch, Chef Barinov retreats into his private office in sheer fury. "
    "When Max walks in with fresh kitchen aprons, Barinov explodes with anger and drives him straight back to the prep line."
)

STORY = [
    ("anya", "Шеф, вы почему так громко кричите?",
     "Chef, why are you shouting so loudly?",
     [], "Max enters office"),

    ("chef", "Быстро уйди отсюда и закрой дверь!",
     "Quickly get out of here and close the door!",
     [(323, "Уйди отсюда!")], "Chef yells furious"),

    ("anya", "Я просто принёс чистые поварские фартуки.",
     "I just brought clean chef aprons.",
     [], "Max explains"),

    ("chef", "Мне сейчас не нужны никакие фартуки, огузок!",
     "I do not need any aprons right now, runt!",
     [], "Chef rages"),

    ("anya", "Неужели Спартак опять проиграл этот матч?",
     "Did Spartak really lose this match again?",
     [], "Max guesses"),

    ("chef", "Они пропустили гол на последней минуте!",
     "They conceded a goal in the last minute!",
     [], "Chef recounts agony"),

    ("anya", "Шеф, это всего лишь обычная спортивная игра.",
     "Chef, it is only an ordinary sports game.",
     [], "Max consoles"),

    ("chef", "Для меня футбол — это вся моя жизнь!",
     "For me football is all my life!",
     [], "Chef roars"),

    ("anya", "Но гости в зале ждут горячие блюда.",
     "But guests in the hall are waiting for hot dishes.",
     [], "Max reminds of work"),

    ("chef", "Пусть Лёва сам командует на горячем цеху!",
     "Let Lyova command the hot station himself!",
     [], "Chef snaps"),

    ("anya", "Лёва очень волнуется без ваших строгих указаний.",
     "Lyova is very anxious without your strict instructions.",
     [], "Max urges"),

    ("chef", "Ладно, иди чистить картошку и не мешай!",
     "Fine, go peel potatoes and do not bother me!",
     [], "Chef commands"),

    ("anya", "Слушаюсь, шеф, уже бегу обратно на кухню.",
     "Right away, chef, I am already running back to the kitchen.",
     [], "Max retreats"),
]

OPENER = "Let's witness Barinov's explosive office rage after his favorite football team concedes a heartbreaking goal."

WALK = [
    (0, None,
     "'Chef, why are you shouting so loudly?' Max steps cautiously into the office hallway."),
    (1, None,
     "'Quickly get out of here and close the door!' Barinov barks with furious indignation."),
    (2, None,
     "'I just brought clean chef aprons.' The young cook tries to justify his presence."),
    (3, None,
     "'I do not need any aprons right now, runt!' The head chef brushes him aside fiercely."),
    (4, None,
     "'Did Spartak really lose this match again?' Max correctly deduces the source of the anger."),
    (5, None,
     "'They conceded a goal in the last minute!' Barinov recounts the tragic finish in horror."),
    (6, None,
     "'Chef, it is only an ordinary sports game.' Max tries to offer gentle perspective."),
    (7, None,
     "'For me football is all my life!' Barinov insists with fiery devotion."),
    (8, None,
     "'But guests in the hall are waiting for hot dishes.' Max gently points toward restaurant priorities."),
    (9, None,
     "'Let Lyova command the hot station himself!' The chef abdicates duties in his foul mood."),
    (10, None,
     "'Lyova is very anxious without your strict instructions.' Max advocates for the nervous sous-chef."),
    (11, None,
     "'Fine, go peel potatoes and do not bother me!' Barinov assigns a menial chore instead."),
    (12, None,
     "'Right away, chef, I am already running back to the kitchen.' Max beats a hasty retreat."),
]

TRANSITION = "Now let's listen to Barinov's fiery office venting and Max's quick retreat one more time."

OUTRO = "Even as sports heartbreak shakes Barinov's world, dinner service at Claude Monet moves relentlessly forward."

CLOSING = ("anya", "Слушаюсь, шеф, уже бегу обратно на кухню.")
