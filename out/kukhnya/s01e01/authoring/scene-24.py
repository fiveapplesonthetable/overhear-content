"""Scene 24 — This Is My Kitchen (s01e01, 00:21:18–00:23:42)."""

ID = "kukhnya-s01e01-scene-24"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 24
TITLE = "Это моя кухня  (This Is My Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "vika": "angelina",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "vika": "Вика",
}

INTRO = (
    "In the kitchen of Claude Monet, chaos erupts when a VIP guest suffers a severe allergic reaction "
    "to an unauthorized dish served by novice cook Max."
)

STORY = [
    ("vika", "Шеф, в зале гостю стало очень плохо!",
     "Chef, a guest in the hall became very ill!",
     [(324, "гость отравился.")], "Vika reports emergency"),

    ("chef", "Что случилось? Это не моё блюдо!",
     "What happened? This is not my dish!",
     [(326, "Что случилось?"), (329, "Это не мое блюдо.")], "Chef inspects plate"),

    ("anya", "Шеф, это блюдо приготовил я.",
     "Chef, I cooked this dish.",
     [(332, "Это мое блюдо.")], "Max confesses"),

    ("anya", "Я заменил ваше блюдо на своё.",
     "I replaced your dish with mine.",
     [(333, "Я заменил ваше блюдо на свое.")], "Max explains swap"),

    ("chef", "Ты вообще как посмел такое сделать?",
     "How did you dare do such a thing?",
     [(340, "Ты вообще как посмел")], "Chef's fury"),

    ("chef", "Запомни раз и навсегда: это моя кухня!",
     "Remember once and for all: this is my kitchen!",
     [(342, "Это моя кухня!")], "Chef asserts domain"),

    ("chef", "Ты поставил под угрозу жизнь человека!",
     "You endangered a human being's life!",
     [(343, "поставил под угрозу жизни,")], "moral rebuke"),

    ("chef", "Пошёл вон отсюда прямо сейчас!",
     "Get out of here right now!",
     [(346, "Пошел вон!")], "Chef fires Max"),

    ("chef", "Алло? Да, Дима, я слушаю.",
     "Hello? Yes, Dima, I'm listening.",
     [(346, "Алло."), (347, "Да, Дима.")], "Nagiyev calls"),

    ("chef", "Какие новости из больницы, говори скорее.",
     "What news from the hospital, speak quickly.",
     [(348, "для тебя хорошие новости.")], "Chef asks"),

    ("chef", "Что? Врачи обнаружили у него аневризму?",
     "What? The doctors discovered an aneurysm in him?",
     [(349, "обнаружили аневризму,")], "surprise medical discovery"),

    ("chef", "Значит, это спасло ему жизнь?",
     "Does that mean this saved his life?",
     [(352, "ты ему жизнь спас.")], "miraculous outcome"),

    ("anya", "Шеф, так значит, никто не умер?",
     "Chef, does that mean nobody died?",
     [], "Max relieved"),

    ("chef", "Молчи, сегодня тебе просто невероятно повезло.",
     "Keep quiet, today you were simply incredibly lucky.",
     [], "Chef's warning"),
]

OPENER = "Let's explore the high-stakes kitchen crisis and its miraculous resolution."

WALK = [
    (0, None,
     "'Chef, a guest in the hall became very ill!' Vika rushes into the kitchen with alarming news."),
    (1, None,
     "'What happened? This is not my dish!' The head chef angrily inspects the returned plate."),
    (2, None,
     "'Chef, I cooked this dish.' Max steps forward to take full personal responsibility."),
    (3, None,
     "'I replaced your dish with mine.' Max confesses his arrogant unauthorized swap."),
    (4, None,
     "'How did you dare do such a thing?' Chef Barinov is incensed by the cook's insolence."),
    (5, None,
     "'Remember once and for all: this is my kitchen!' The head chef fiercely reasserts absolute authority."),
    (6, None,
     "'You endangered a human being's life!' Barinov emphasizes the gravity of the medical emergency."),
    (7, None,
     "'Get out of here right now!' The chef fires the young novice on the spot."),
    (8, None,
     "'Hello? Yes, Dima, I'm listening.' Barinov answers a sudden phone call from the restaurant owner."),
    (9, None,
     "'What news from the hospital, speak quickly.' The chef braces himself for disastrous news."),
    (10, None,
     "'What? The doctors discovered an aneurysm in him?' The examination unexpectedly revealed a hidden condition."),
    (11, None,
     "'Does that mean this saved his life?' The allergic reaction led to timely medical intervention."),
    (12, None,
     "'Chef, does that mean nobody died?' Max breathes a tremendous sigh of relief."),
    (13, None,
     "'Keep quiet, today you were simply incredibly lucky.' Barinov sternly warns Max of his lucky escape."),
]

TRANSITION = "Now let's listen to the tense kitchen confrontation and sudden twist once more."

OUTRO = "Saved by an astonishing coincidence, Max escapes disaster on his first chaotic day."

CLOSING = ("chef", "Молчи, сегодня тебе просто невероятно повезло.")
