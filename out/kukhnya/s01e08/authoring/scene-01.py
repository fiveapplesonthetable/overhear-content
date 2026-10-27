ID = "kukhnya-s01e08-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 1
TITLE = "Лицо ресторана  (The Face of the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiev": "anja"}
LABELS = {"anya": "Шеф", "nagiev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-10. Backstage at the morning cooking show, restaurant owner Dmitry Nagiev "
    "forces a reluctant Chef Barinov to go on air as the public face of Claude Monet."
)

INTRO = (
    "Backstage at the television studio of a morning culinary program, restaurant owner Dmitry Nagiev "
    "corners Chef Viktor Barinov. Barinov grumbles that he is a professional cook rather than a television star, "
    "but Nagiev insists that as the face of Claude Monet, he must represent the establishment on air. "
    "Let's listen to their backstage argument in Russian first."
)

STORY = [
    ("anya", "Дима, зачем ты позвал меня сюда?",
     "Dima, why did you call me here?",
     [(1, "Дим, ну в каком хрен я здесь")], "adapted"),
    ("nagiev", "Ты будешь выступать на телевидении, Виктор.",
     "You will perform on television, Viktor.",
     [(3, "Ты не только повар, ты лицо нашего ресторана")], "adapted"),
    ("anya", "Я шеф-повар, а не известный актёр!",
     "I am a head chef, not a famous actor!",
     [(2, "Я же не актер, я повар")], "adapted"),
    ("nagiev", "Ты главное лицо нашего дорогого ресторана.",
     "You are the main face of our expensive restaurant.",
     [(3, "ты лицо нашего ресторана")], "adapted"),
    ("anya", "Моё место на кухне у плиты.",
     "My place is in the kitchen at the stove.",
     [], "new"),
    ("nagiev", "Зрители хотят видеть настоящего шефа.",
     "The viewers want to see a real chef.",
     [(4, "этим лицом светить")], "adapted"),
    ("anya", "Отпусти меня обратно в Клод Моне.",
     "Let me go back to Claude Monet.",
     [(5, "Давай в ресторан поеду")], "adapted"),
    ("nagiev", "Перестань спорить и иди вперёд.",
     "Stop arguing and go forward.",
     [(10, "Все, в тени живот и вперед")], "adapted"),
    ("anya", "Там будет выступать эта Соколова?",
     "Will that Sokolova perform there?",
     [(17, "Елена Соколова")], "adapted"),
    ("nagiev", "Да, Елена Соколова из ресторана Аркабалено.",
     "Yes, Elena Sokolova from Arcobaleno restaurant.",
     [(16, "шеф-повар ресторана Арка Баляна"), (17, "Елена Соколова")], "adapted"),
    ("anya", "Я докажу всем свой высокий класс.",
     "I will prove my high caliber to everyone.",
     [], "new"),
    ("nagiev", "Вот это отличный настрой, шеф!",
     "Now that is a great attitude, chef!",
     [], "new"),
    ("anya", "Прямой эфир начинается прямо сейчас.",
     "Live broadcast begins right now.",
     [(19, "Итак, мы начинаем")], "adapted"),
]

OPENER = "Now let's examine Barinov and Nagiev's backstage argument line by line."

WALK = [
    (0, None,
     "'Dima, why did you call me here?' Barinov questions the restaurant owner's sudden summons."),
    (1, None,
     "'You will perform on television, Viktor.' Nagiev announces the PR appearance using a future verb."),
    (2, None,
     "'I am a head chef, not a famous actor!' Barinov protests his suitability for television."),
    (3, None,
     "'You are the main face of our expensive restaurant.' Nagiev flatters the chef with a status metaphor."),
    (4, None,
     "'My place is in the kitchen at the stove.' Barinov insists on his true culinary workstation."),
    (5, None,
     "'The viewers want to see a real chef.' Nagiev explains the public demand for authenticity."),
    (6, None,
     "'Let me go back to Claude Monet.' Barinov attempts to leave with an imperative verb."),
    (7, None,
     "'Stop arguing and go forward.' Nagiev cuts off debate and pushes him toward the studio stage."),
    (8, None,
     "'Will that Sokolova perform there?' Barinov discovers his competitor's presence on the show."),
    (9, None,
     "'Yes, Elena Sokolova from Arcobaleno restaurant.' Nagiev confirms the rival head chef's participation."),
    (10, None,
     "'I will prove my high caliber to everyone.' Barinov's competitive pride is instantly triggered."),
    (11, None,
     "'Now that is a great attitude, chef!' Nagiev praises the chef's fighting spirit."),
    (12, None,
     "'Live broadcast begins right now.' Barinov prepares for airtime as cameras roll."),
]

TRANSITION = "Now let's listen to the backstage argument again without interruption."
OUTRO = (
    "With seconds to spare before the live broadcast begins, Chef Barinov steps out under the studio lights "
    "ready to defend his restaurant's prestige against rival chef Elena Sokolova."
)
CLOSING = ("anya", "Прямой эфир начинается прямо сейчас.")
