ID = "kukhnya-s01e11-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 1
TITLE = "Кто главный в ресторане  (Who Runs the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-23. At the bar, Max and Kostya discuss who really runs the restaurant, "
    "concluding that guests hold ultimate power."
)

INTRO = (
    "At the Claude Monet bar counter, junior cook Max poses a philosophical question to his friend Kostya "
    "about restaurant hierarchy. They consider whether the director, head chef, or wealthy owner holds true power, "
    "before agreeing that the guests ultimately dictate everything. Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, кто самый главный в нашем ресторане?",
     "Kostya, who is the most important in our restaurant?",
     [(1, "кто главный в ресторане?")], "adapted"),
    ("kostya", "Может быть, наш строгий шеф-повар?",
     "Maybe our strict head chef?",
     [(3, "Шеф?")], "adapted"),
    ("anya", "Или богатый хозяин ресторана Дмитрий?",
     "Or the rich restaurant owner Dmitry?",
     [(4, "ресторана?")], "adapted"),
    ("kostya", "А может, наш строгий директор Виктория?",
     "Or maybe our strict director Victoria?",
     [(2, "Директор?")], "adapted"),
    ("anya", "Нет, самые главные здесь — это гости.",
     "No, the most important here are the guests.",
     [(5, "Главный в ресторане — это гости.")], "adapted"),
    ("kostya", "Это правда, наши гости бывают разные.",
     "That is true, our guests can be very different.",
     [(7, "гости бывают разные.")], "adapted"),
    ("anya", "Одни гости бывают слишком жадными.",
     "Some guests can be too stingy.",
     [(8, "Бывают очень жадные.")], "adapted"),
    ("kostya", "Другие гости бывают очень весёлыми.",
     "Other guests can be very cheerful.",
     [(13, "Бывают очень")], "adapted"),
    ("anya", "И они часто обнимают тебя?",
     "And do they often hug you?",
     [], "new"),
    ("kostya", "Да, постоянно говорят разные добрые слова.",
     "Yes, they constantly say various kind words.",
     [(17, "Хороший ты парень, Костя.")], "adapted"),
    ("anya", "Они платят деньги за этот обед.",
     "They pay money for this lunch.",
     [], "new"),
    ("kostya", "Поэтому мы всегда улыбаемся каждому гостю.",
     "Therefore we always smile at every guest.",
     [], "new"),
    ("anya", "Гость всегда остаётся самым главным.",
     "The guest always remains the most important.",
     [], "new"),
]

OPENER = "Now let's examine this barroom discussion line by line."

WALK = [
    (0, None,
     "'Kostya, who is the most important in our restaurant?' -- Max asks his friend a philosophical question."),
    (1, None,
     "'Maybe our strict head chef?' -- Kostya suggests the culinary master at the stove."),
    (2, None,
     "'Or the rich restaurant owner Dmitry?' -- Max wonders about the establishment owner."),
    (3, None,
     "'Or maybe our strict director Victoria?' -- The bartender considers the front-of-house manager."),
    (4, None,
     "'No, the most important here are the guests.' -- Max reveals his surprising conclusion."),
    (5, None,
     "'That is true, our guests can be very different.' -- Kostya agrees with his thoughtful observation."),
    (6, None,
     "'Some guests can be too stingy.' -- Max points out customers who pinch pennies."),
    (7, None,
     "'Other guests can be very cheerful.' -- Kostya recalls patrons who are full of joy."),
    (8, None,
     "'And do they often hug you?' -- Max asks playfully about over-friendly visitors."),
    (9, None,
     "'Yes, they constantly say various kind words.' -- The bartender confirms their affectionate banter."),
    (10, None,
     "'They pay money for this lunch.' -- Max notes that guests fund the restaurant."),
    (11, None,
     "'Therefore we always smile at every guest.' -- Kostya states the golden hospitality rule."),
    (12, None,
     "'The guest always remains the most important.' -- Max concludes that guests hold ultimate authority."),
]

TRANSITION = "Now let's listen to the barroom discussion again without interruption."
OUTRO = (
    "With their philosophical debate settled in favor of the customer, Max and Kostya return "
    "to their duties, ready to accommodate whatever demanding patrons arrive next."
)
CLOSING = ("anya", "Гость всегда остаётся самым главным.")
