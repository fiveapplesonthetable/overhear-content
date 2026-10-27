"""Scene 22 — Take Your Time (s01e05, 00:22:58–00:22:59)."""

ID = "kukhnya-s01e05-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 22
TITLE = "Не торопись  (Take Your Time)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 313. Under Fedya's patient guidance, Max cooks and plates fish with calm focus, "
    "mastering the dinner rush without panicking."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}

LABELS = {
    "anya": "Макс",
    "fedya": "Федя",
}

INTRO = (
    "With orders rolling in during the intense dinner rush at Claude Monet, Max puts Fedya's breathing advice into action. "
    "Working alongside the experienced fish cook, Max stays calm and focused, carefully cooking and plating each order. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("fedya", "Вот так, Макс, держи правильный ритм.",
     "Like that, Max, keep the right rhythm.",
     [], "Fedya sets pace"),

    ("anya", "Рыба почти готова на горячей сковороде.",
     "The fish is almost ready on the hot pan.",
     [], "Max reports status"),

    ("fedya", "Отлично, аккуратно переложи рыбу на тарелку.",
     "Great, carefully transfer the fish to the plate.",
     [], "Fedya gives instruction"),

    ("anya", "Я добавляю свежую зелень и соус.",
     "I add fresh greens and sauce.",
     [], "Max garnishes plate"),

    ("fedya", "Молодец, не торопись.",
     "Well done, take your time.",
     [(313, "Молодец. Не торопись.")], "Fedya coaches calmly"),

    ("fedya", "Каждое блюдо должно выглядеть красиво.",
     "Each dish must look beautiful.",
     [], "Emphasizing presentation"),

    ("anya", "Вдох и выдох, я спокоен.",
     "Inhale and exhale, I am calm.",
     [], "Applying breathing lesson"),

    ("fedya", "Видишь, паника исчезает сама собой.",
     "See, the panic disappears by itself.",
     [], "Noticing progress"),

    ("anya", "Теперь я контролирую весь этот процесс.",
     "Now I control this entire process.",
     [], "Max regains confidence"),

    ("fedya", "Вот этот заказ готов к подаче.",
     "This order is ready to serve.",
     [], "Checking order"),

    ("anya", "Официант уже может забирать тарелку.",
     "The waiter can already take the plate.",
     [], "Ready for dining room"),

    ("fedya", "Ты отлично справляешься сегодня на смене.",
     "You are doing great on the shift today.",
     [], "Praising effort"),

    ("anya", "Спасибо, Федя, я готов к работе!",
     "Thank you, Fedya, I am ready for work!",
     [], "Max thanks Fedya"),
]

OPENER = "Now let's examine Fedya and Max's plating and coaching line by line."

WALK = [
    (0, None,
     "'Like that, Max, keep the right rhythm.' Fedya monitors Max at the station and sets a steady pace."),
    (1, None,
     "'The fish is almost ready on the hot pan.' Max keeps track of the cooking fish with focused attention."),
    (2, None,
     "'Great, carefully transfer the fish to the plate.' Fedya guides the rookie through the delicate plating process."),
    (3, None,
     "'I add fresh greens and sauce.' Max completes the garnishing according to the kitchen's strict standard."),
    (4, None,
     "'Well done, take your time.' Fedya praises Max's focus and reminds him not to rush under pressure."),
    (5, None,
     "'Each dish must look beautiful.' The experienced chef highlights the importance of visual presentation."),
    (6, None,
     "'Inhale and exhale, I am calm.' Max uses the breathing technique to keep his stress under control."),
    (7, None,
     "'See, the panic disappears by itself.' Fedya observes the young cook settling into a smooth flow."),
    (8, None,
     "'Now I control this entire process.' Max feels genuine confidence returning as he manages the station."),
    (9, None,
     "'This order is ready to serve.' Fedya checks the completed plate and gives his professional approval."),
    (10, None,
     "'The waiter can already take the plate.' Max announces that the hot dish is ready for the dining room."),
    (11, None,
     "'You are doing great on the shift today.' Fedya acknowledges the rookie's perseverance and progress."),
    (12, None,
     "'Thank you, Fedya, I am ready for work!' Max expresses his gratitude and looks ahead to the remaining orders."),
]

TRANSITION = "Now let's listen to Fedya and Max working together once more without interruption."

OUTRO = (
    "With Fedya's steady guidance, Max successfully conquers the fish station and plates each dish with pride."
)

CLOSING = ("anya", "Спасибо, Федя, я готов к работе!")
