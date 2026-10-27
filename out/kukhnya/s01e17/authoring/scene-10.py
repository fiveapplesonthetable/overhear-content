ID = "kukhnya-s01e17-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 10
TITLE = "Котлеты со спаржей  (Chops with Asparagus)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Федя", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 134. In the kitchen, a disappointed Fedya shows off his Breton lamb chops with asparagus after Chef Barinov "
    "walks away, while Senya proudly celebrates winning the seasonal menu contest."
)

INTRO = (
    "After Chef Barinov leaves the kitchen without tasting the other dishes, Fedya stands holding his plate of lamb chops. "
    "He complains to Senya that his own creation never even got a fair chance in the contest. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Вот мои вкусные котлеты для шефа.",
     "Here are my tasty chops for the Chef.",
     [(134, "котлеты")], "adapted"),
    ("senya", "Шеф уже выбрал моё мясное блюдо.",
     "The Chef already chose my meat dish.",
     [], "new"),
    ("anya", "Он даже не попробовал мою еду!",
     "He did not even taste my food!",
     [], "new"),
    ("senya", "Потому что мой рецепт самый лучший.",
     "Because my recipe is the very best.",
     [], "new"),
    ("anya", "Я готовил эти котлеты всё утро.",
     "I cooked these chops all morning.",
     [], "new"),
    ("senya", "Не надо так сильно расстраиваться, друг.",
     "Do not be so upset, friend.",
     [], "new"),
    ("anya", "Ты просто был первый в очереди.",
     "You were simply first in line.",
     [], "new"),
    ("senya", "В следующий раз ты точно победишь.",
     "Next time you will definitely win.",
     [], "new"),
    ("anya", "Хочешь попробовать мои новые котлеты?",
     "Do you want to try my new chops?",
     [], "new"),
    ("senya", "Давай, я с удовольствием попробую.",
     "Go ahead, I will gladly try them.",
     [], "new"),
    ("anya", "Ну как тебе вкус, скажи честно?",
     "Well how is the taste to you, tell me honestly?",
     [], "new"),
    ("senya", "Слушай, это действительно очень вкусно!",
     "Listen, this is really very tasty!",
     [], "new"),
    ("anya", "Тогда мы сами съедим это на обед.",
     "Then we will eat this ourselves for lunch.",
     [], "new"),
]

OPENER = "Now let's examine this conversation line by line."

WALK = [
    (0, None,
     "'Here are my tasty chops for the Chef.' -- Fedya presents the plate he worked so hard on."),
    (1, None,
     "'The Chef already chose my meat dish.' -- Senya reminds him that the contest is already over."),
    (2, None,
     "'He did not even taste my food!' -- Fedya is frustrated that Barinov walked away so fast."),
    (3, None,
     "'Because my recipe is the very best.' -- Senya boasts about his winning culinary idea."),
    (4, None,
     "'I cooked these chops all morning.' -- Fedya points out how much effort went into the meal."),
    (5, None,
     "'Do not be so upset, friend.' -- Senya tries to cheer up his kitchen partner."),
    (6, None,
     "'You were simply first in line.' -- Fedya claims that Senya only won by standing closest to the Chef."),
    (7, None,
     "'Next time you will definitely win.' -- Senya offers an encouraging prediction."),
    (8, None,
     "'Do you want to try my new chops?' -- Fedya invites his friend to taste the dish instead."),
    (9, None,
     "'Go ahead, I will gladly try them.' -- Senya happily accepts the offer of free food."),
    (10, None,
     "'Well how is the taste to you, tell me honestly?' -- Fedya waits eagerly for his colleague's verdict."),
    (11, None,
     "'Listen, this is really very tasty!' -- Senya is genuinely impressed by the flavor."),
    (12, None,
     "'Then we will eat this ourselves for lunch.' -- Fedya decides the dish will not go to waste."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = (
    "Rather than letting the Breton lamb chops go to waste, the two friends decide to enjoy the gourmet meal "
    "together for their own lunch."
)
CLOSING = ("senya", "Приятного аппетита, друг!")
