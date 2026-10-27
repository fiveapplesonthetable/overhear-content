ID = "kukhnya-s01e03-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = "Обед персонала  (Staff Lunch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ainura": "anja"}
LABELS = {"anya": "Настя", "ainura": "Айнура"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 83-96. In the staff dining area during lunch, waitress Nastya explains her strict vegetarianism "
    "to cleaner Ainura, who nostalgically recounts eating only potatoes during the nineties."
)

INTRO = (
    "During staff lunch in the restaurant backroom, waitress Nastya refuses the meat cutlets on offer. "
    "Cleaner Ainura is puzzled by her choice and asks why she avoids meat. "
    "Nastya passionately explains her vegetarian philosophy, while Ainura recalls having lived on potatoes alone during hard times. "
    "Let's listen to their amusing exchange in Russian first."
)

STORY = [
    ("ainura", "Настя, почему ты не кушаешь мясо?",
     "Nastya, why do you not eat meat?",
     [(83, "А почему ты мясо не кушаешь, Тян")], "adapted"),
    ("anya", "Потому что я строгая вегетарианка.",
     "Because I am a strict vegetarian.",
     [(84, "А я вегетарианка")], "adapted"),
    ("ainura", "Да ты что? А я думала, ты русская.",
     "Really? And here I thought you were Russian.",
     [(85, "Да ты что, вегетарианка"), (86, "А это, думала, ты русская")], ""),
    ("anya", "Вегетарианцы — это люди, которые не едят мясо.",
     "Vegetarians are people who do not eat meat.",
     [(87, "Вегетарианцы – это люди, которые мясо не едят")], "adapted"),
    ("ainura", "Раньше я тоже была вегетарианкой.",
     "I used to be a vegetarian too.",
     [(88, "Раньше я тоже была вегетариантой")], "adapted"),
    ("anya", "Правда? Когда вы не ели мясо?",
     "Really? When did you not eat meat?",
     [], "new"),
    ("ainura", "В девяностые годы совсем не было денег.",
     "In the nineties there was no money at all.",
     [(88, "в 90-е годы"), (89, "Денег не было")], "adapted"),
    ("ainura", "Я целый год ела только картошку.",
     "I ate only potatoes for a whole year.",
     [(89, "одну картошку ела")], "adapted"),
    ("anya", "Я считаю недопустимым убивать животных.",
     "I consider killing animals unacceptable.",
     [(91, "считаю недопустимым убивать животных")], "adapted"),
    ("ainura", "Но сочные мясные котлеты такие вкусные!",
     "But juicy meat cutlets are so tasty!",
     [(94, "вот таких вот сочных")], "adapted"),
    ("anya", "Каждая коровка имеет право на жизнь.",
     "Every cow has the right to life.",
     [(92, "была милая коровка")], "adapted"),
    ("ainura", "Ой, бай! Ты так красиво рассказываешь!",
     "Oh my! You tell stories so beautifully!",
     [(96, "Ой, бай! Ты так вкусно рассказываешь")], "adapted"),
    ("anya", "Надеюсь, вы меня наконец поняли.",
     "I hope you finally understood me.",
     [], "new"),
]

OPENER = "Now let's examine Nastya and Ainura's discussion line by line."

WALK = [
    (0, None,
     "'Nastya, why do you not eat meat?' Ainura asks her colleague curiously with a question word."),
    (1, None,
     "'Because I am a strict vegetarian.' Nastya explains her diet using an adjective and predicate noun."),
    (2, None,
     "'Really? And here I thought you were Russian.' Ainura expresses genuine surprise at the foreign concept."),
    (3, None,
     "'Vegetarians are people who do not eat meat.' Nastya defines the word using an explanatory clause."),
    (4, None,
     "'I used to be a vegetarian too.' Ainura relates her own past experience using a temporal adverb."),
    (5, None,
     "'Really? When did you not eat meat?' Nastya inquires about the past using a time conjunction."),
    (6, None,
     "'In the nineties there was no money at all.' Ainura explains the economic hardship using an impersonal negative past."),
    (7, None,
     "'I ate only potatoes for a whole year.' Ainura describes her involuntary diet with an emphatic particle."),
    (8, None,
     "'I consider killing animals unacceptable.' Nastya states her moral stance using a predicative adjective."),
    (9, None,
     "'But juicy meat cutlets are so tasty!' Ainura defends traditional cooking with descriptive adjectives."),
    (10, None,
     "'Every cow has the right to life.' Nastya advocates for animals using a dative noun and possessive verb."),
    (11, None,
     "'Oh my! You tell stories so beautifully!' Ainura compliments Nastya's passionate storytelling."),
    (12, None,
     "'I hope you finally understood me.' Nastya wraps up the conversation with a hopeful present verb."),
]

TRANSITION = "Now let's listen to Nastya and Ainura's dialogue again without interruption."
OUTRO = (
    "Ainura enjoys her meal while Nastya remains true to her principles. "
    "In the next scene, Max searches for someone capable of finishing off the live goose."
)
CLOSING = ("anya", "Надеюсь, вы меня наконец поняли.")
