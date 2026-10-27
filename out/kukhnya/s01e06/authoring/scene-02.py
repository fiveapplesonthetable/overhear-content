ID = "kukhnya-s01e06-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = "Финальный штрих  (The Final Touch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 4. In the kitchen, Chef Viktor Barinov inspects a finished dish at the pass "
    "and instructs Max on the art of garnishing plates before they reach the dining room."
)

INTRO = (
    "At the Claude Monet kitchen pass, Chef Viktor Barinov inspects a hot dish before it leaves for the dining room. "
    "He teaches young cook Max how the final touch of fresh herbs elevates a plate into an appetizing masterpiece. "
    "Let's listen to their exchange in Russian first."
)

STORY = [
    ("chef", "Огузок, посмотри на эту тарелку.",
     "Oguzok, look at this plate.",
     [], "new"),
    ("anya", "Шеф, это блюдо уже готово?",
     "Chef, is this dish already ready?",
     [], "new"),
    ("chef", "Осталось главное: украсить его зеленью.",
     "The main thing remains: to garnish it with herbs.",
     [(4, "Его украшают")], "adapted"),
    ("anya", "Каждая деталь имеет важное значение.",
     "Every detail has important meaning.",
     [], "new"),
    ("chef", "Еда обязана выглядеть красиво и аппетитно.",
     "Food is obliged to look beautiful and appetizing.",
     [(4, "украшают")], "adapted"),
    ("anya", "Положим сюда свежую зелень?",
     "Shall we put fresh herbs here?",
     [], "new"),
    ("chef", "Аккуратно! Не испорти дорогую подачу.",
     "Carefully! Do not ruin the expensive presentation.",
     [], "new"),
    ("anya", "Я делаю всё очень аккуратно, шеф.",
     "I do everything very carefully, chef.",
     [], "new"),
    ("chef", "Красивая подача очень важна для гостей.",
     "Beautiful presentation is very important for guests.",
     [], "new"),
    ("anya", "Официанты уже ждут на кухне.",
     "The waiters are already waiting in the kitchen.",
     [], "new"),
    ("chef", "Зови официанта, пусть несут заказ.",
     "Call the waiter, let them carry the order.",
     [], "new"),
    ("anya", "Саша, забери готовое горячее блюдо!",
     "Sasha, take the ready hot dish!",
     [], "new"),
    ("chef", "Отлично, продолжаем работать дальше.",
     "Great, we continue working further.",
     [], "new"),
]

OPENER = "Now let's examine Barinov and Max's kitchen instructions line by line."

WALK = [
    (0, None,
     "'Oguzok, look at this plate.' Barinov calls Max over with his trademark nickname and an imperative verb."),
    (1, None,
     "'Chef, is this dish already ready?' Max asks about the state of preparation with a short adjective."),
    (2, None,
     "'The main thing remains: to garnish it with herbs.' Barinov states the final requirement using an infinitive verb."),
    (3, None,
     "'Every detail has important meaning.' Max agrees using a feminine adjective and neuter noun."),
    (4, None,
     "'Food is obliged to look beautiful and appetizing.' Barinov insists on high culinary standards using adverbs of manner."),
    (5, None,
     "'Shall we put fresh herbs here?' Max suggests the placement using a 1st person plural future verb."),
    (6, None,
     "'Carefully! Do not ruin the expensive presentation.' Barinov cautions against clumsy plating with a negative imperative."),
    (7, None,
     "'I do everything very carefully, chef.' Max reassures his superior using an adverb of manner."),
    (8, None,
     "'Beautiful presentation is very important for guests.' Barinov emphasizes customer perception with a predicate adjective."),
    (9, None,
     "'The waiters are already waiting in the kitchen.' Max notes service readiness using a present imperfective verb."),
    (10, None,
     "'Call the waiter, let them carry the order.' Barinov issues orders to dispatch the meal using an imperative and particle."),
    (11, None,
     "'Sasha, take the ready hot dish!' Max calls the waitress using an imperative verb and compound accusative phrase."),
    (12, None,
     "'Great, we continue working further.' Barinov moves on to the next task with an adverb of approval."),
]

TRANSITION = "Now let's listen to the kitchen instructions again without interruption."
OUTRO = (
    "The beautifully decorated dish is carried out to the dining room, satisfying the chef's exacting standards. "
    "In the next scene, the cooks continue their prep work before Barinov heads to the market."
)
CLOSING = ("chef", "Отлично, продолжаем работать дальше.")
