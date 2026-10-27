ID = "kukhnya-s01e10-scene-29"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 29
TITLE = "Щучья икра  (Pike Caviar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 204-206. Senya opens the container to reveal five kilograms of inexpensive pike caviar, "
    "prompting Chef Viktor to devise a daring plan to disguise its bright yellow color."
)

INTRO = (
    "In the quiet back room of Claude Monet, Senya opens the delivery container to display "
    "five kilograms of freshly bought pike caviar. While the price is extraordinarily low, "
    "the bright golden grains look nothing like the costly black sturgeon caviar expected by diners. "
    "Let us listen to their discussion in Russian first."
)

STORY = [
    ("anya", "Вот товар, как вы заказывали, шеф.",
     "Here is the goods, as you ordered, chef.",
     [(204, "вы заказывали")], "adapted"),
    ("chef", "Открывай коробку и покажи мне икру.",
     "Open the box and show me the caviar.",
     [], "new"),
    ("anya", "Это отличная щучья икра, пять килограммов.",
     "This is excellent pike caviar, five kilograms.",
     [(205, "Икра щучья. Пять кило")], "adapted"),
    ("chef", "Она выглядит очень красиво и аппетитно.",
     "It looks very beautiful and appetizing.",
     [], "new"),
    ("anya", "Цена всего двести рублей за килограмм.",
     "The price is only two hundred rubles per kilogram.",
     [(206, "Двести рублей килограмм")], "adapted"),
    ("chef", "Это действительно очень дешёвая цена.",
     "This is indeed a very cheap price.",
     [], "new"),
    ("anya", "Мы сохранили ресторану очень много денег.",
     "We saved the restaurant a lot of money.",
     [], "new"),
    ("chef", "Но цвет этой икры слишком жёлтый.",
     "But the color of this caviar is too yellow.",
     [], "new"),
    ("anya", "Щучья икра всегда бывает жёлтого цвета.",
     "Pike caviar is always yellow in color.",
     [], "new"),
    ("chef", "А гости ждут дорогую чёрную икру.",
     "And the guests expect expensive black caviar.",
     [], "new"),
    ("anya", "Что же нам делать с этим цветом?",
     "What are we to do with this color?",
     [], "new"),
    ("chef", "У меня появился один хитрый план.",
     "I have got a clever plan.",
     [], "new"),
    ("anya", "Я готов помочь вам в этом деле.",
     "I am ready to help you in this business.",
     [], "new"),
]

OPENER = "Now let us examine Senya and Viktor's discussion about the caviar line by line."

WALK = [
    (0, None,
     "'Here is the goods, as you ordered, chef.' -- Senya presents the delivery exactly as instructed."),
    (1, None,
     "'Open the box and show me the caviar.' -- Viktor asks to inspect the product visually."),
    (2, None,
     "'This is excellent pike caviar, five kilograms.' -- Senya proudly specifies the type and weight of the roe."),
    (3, None,
     "'It looks very beautiful and appetizing.' -- The chef acknowledges the appealing quality of the food."),
    (4, None,
     "'The price is only two hundred rubles per kilogram.' -- Senya highlights the amazingly low cost."),
    (5, None,
     "'This is indeed a very cheap price.' -- Viktor agrees that the bargain was exceptional."),
    (6, None,
     "'We saved the restaurant a lot of money.' -- Senya praises their thrifty financial accomplishment."),
    (7, None,
     "'But the color of this caviar is too yellow.' -- Viktor identifies an obvious problem with the color."),
    (8, None,
     "'Pike caviar is always yellow in color.' -- The cook explains that pike roe naturally has golden shades."),
    (9, None,
     "'And the guests expect expensive black caviar.' -- The head chef points out the expectations of wealthy diners."),
    (10, None,
     "'What are we to do with this color?' -- Senya wonders how they will solve the chromatic mismatch."),
    (11, None,
     "'I have got a clever plan.' -- Viktor hints at a cunning scheme to disguise the fish eggs."),
    (12, None,
     "'I am ready to help you in this business.' -- The loyal cook pledges full cooperation in the trick."),
]

TRANSITION = "Now let us listen to the conversation about the pike caviar once more."
OUTRO = (
    "With five kilograms of bright yellow pike caviar before them, Viktor and Senya prepare "
    "to embark on a daring culinary experiment to fool the restaurant's discerning guests."
)
CLOSING = ("chef", "У меня появился один хитрый план.")
