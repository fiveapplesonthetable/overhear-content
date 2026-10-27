ID = "kukhnya-s01e10-scene-30"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 30
TITLE = "Хитрый рецепт  (A Tricky Recipe)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 207-209. Viktor and Senya mix dark food coloring into the yellow pike caviar to disguise "
    "it as expensive black caviar, jokingly dubbing their culinary secret 'Pike Easter'."
)

INTRO = (
    "In the kitchen workspace behind closed doors, Chef Viktor and Senya commence their "
    "bold culinary deception. Armed with dark natural food dye, they set out to tint the yellow "
    "pike caviar into convincing black pearls, joking that it feels like decorating eggs for Easter. "
    "Let us listen to their conspiratorial dialogue in Russian first."
)

STORY = [
    ("chef", "Давай начнём красить эту щучью икру.",
     "Let us start dyeing this pike caviar.",
     [(207, "Давай"), (208, ",кращусь")], "adapted"),
    ("anya", "Вы хотите превратить её в чёрную?",
     "Do you want to turn it into black?",
     [], "new"),
    ("chef", "Да, мы покрасим всю эту икру.",
     "Yes, we will dye all of this caviar.",
     [], "new"),
    ("anya", "Это прямо настоящая щучья пасха получается.",
     "This turns out to be a real pike Easter.",
     [(209, "Щучья пасха")], "adapted"),
    ("chef", "Неси сюда чёрный краситель.",
     "Bring black food dye here.",
     [], "new"),
    ("anya", "Я нашёл на полке отличный краситель.",
     "I found an excellent dye on the shelf.",
     [], "new"),
    ("chef", "Добавляй краситель медленно и аккуратно.",
     "Add the dye slowly and carefully.",
     [], "new"),
    ("anya", "Икра уже становится совсем чёрной.",
     "The caviar is already becoming completely black.",
     [], "new"),
    ("chef", "Теперь хорошо помешай ложкой всю икру.",
     "Now stir all the caviar well with a spoon.",
     [], "new"),
    ("anya", "Она выглядит прямо как дорогая чёрная.",
     "It looks just like expensive black caviar.",
     [], "new"),
    ("chef", "Ни один гость ресторана ничего не заметит.",
     "Not a single guest of the restaurant will notice anything.",
     [], "new"),
    ("anya", "Вы просто гений кулинарных секретов, шеф.",
     "You are simply a genius of culinary secrets, chef.",
     [], "new"),
    ("chef", "Этот секрет никто не должен знать.",
     "No one must know this secret.",
     [], "new"),
]

OPENER = "Now let us examine Viktor and Senya's secret recipe step by step."

WALK = [
    (0, None,
     "'Let us start dyeing this pike caviar.' -- Viktor instructs Senya to begin coloring the roe."),
    (1, None,
     "'Do you want to turn it into black?' -- Senya asks if their goal is to make it look like sturgeon caviar."),
    (2, None,
     "'Yes, we will dye all of this caviar.' -- The chef insists on dyeing all of the fish eggs."),
    (3, None,
     "'This turns out to be a real pike Easter.' -- Senya humorously compares the task to painting Easter eggs."),
    (4, None,
     "'Bring black food dye here.' -- Viktor calls for black food coloring."),
    (5, None,
     "'I found an excellent dye on the shelf.' -- Senya locates suitable black coloring in the pantry."),
    (6, None,
     "'Add the dye slowly and carefully.' -- The chef gives precise instructions on adding the pigment."),
    (7, None,
     "'The caviar is already becoming completely black.' -- Senya watches the golden pearls turn pitch black."),
    (8, None,
     "'Now stir all the caviar well with a spoon.' -- Viktor directs him to blend the mixture evenly."),
    (9, None,
     "'It looks just like expensive black caviar.' -- Senya marvels at the convincing transformation."),
    (10, None,
     "'Not a single guest of the restaurant will notice anything.' -- Viktor confidently assures him that patrons will be fooled."),
    (11, None,
     "'You are simply a genius of culinary secrets, chef.' -- The admiring cook praises Viktor's inventive craft."),
    (12, None,
     "'No one must know this secret.' -- The chef insists on absolute confidentiality."),
]

TRANSITION = "Now let us listen to the conspiratorial exchange between Viktor and Senya once more."
OUTRO = (
    "With the pike caviar successfully dyed a glistening black, Viktor and Senya admire their "
    "handiwork, confident that no patron will discover their culinary ruse."
)
CLOSING = ("chef", "Этот секрет никто не должен знать.")
