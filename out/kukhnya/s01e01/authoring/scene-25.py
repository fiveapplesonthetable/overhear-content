"""Scene 25 — A Second Chance (s01e01, 00:23:56–00:24:56)."""

ID = "kukhnya-s01e01-scene-25"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 25
TITLE = "Второй шанс  (A Second Chance)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "ainura": "angelina",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "ainura": "Айнура",
}

INTRO = (
    "Late at night after the restaurant closes, Chef Viktor Barinov makes an unexpected decision "
    "about Max's future at Claude Monet, prompting Max to reflect on second chances."
)

STORY = [
    ("chef", "Огузок, ты всё ещё здесь стоишь?",
     "Runt, are you still standing here?",
     [(356, "ты еще здесь?")], "Chef notices Max"),

    ("anya", "Шеф, пожалуйста, не надо меня больше унижать.",
     "Chef, please, do not humiliate me anymore.",
     [(357, "Шеф, я все понял, не надо меня больше унижать.")], "Max asks for mercy"),

    ("chef", "Завтра утром приходи на работу вовремя.",
     "Tomorrow morning come to work on time.",
     [], "Chef gives order"),

    ("anya", "Вы меня оставляете работать в ресторане?",
     "Are you letting me stay to work in the restaurant?",
     [(360, "Вы меня оставляете?")], "Max surprised"),

    ("anya", "Шеф, но почему вы передумали?",
     "Chef, but why did you change your mind?",
     [(360, "Ну почему?")], "Max asks why"),

    ("chef", "Не задавай глупых вопросов, а то передумаю!",
     "Do not ask foolish questions, or I'll change my mind!",
     [(361, "я тебя точно уволю.")], "Chef's warning"),

    ("ainura", "Шеф, вы правда его оставляете?",
     "Chef, are you really letting him stay?",
     [(362, "Шеф, вы что, его оставляете?")], "Ainura wonders"),

    ("chef", "Я поспорил, что он сбежит сам!",
     "I bet that he will run away on his own!",
     [(363, "он сбежит сам.")], "Chef's wager"),

    ("chef", "Через неделю этот парень сам уйдёт.",
     "In a week this guy will leave on his own.",
     [(363, "что через неделю")], "Chef's prediction"),

    ("anya", "Каждый человек имеет право на шанс.",
     "Every person has the right to a chance.",
     [(365, "Каждый человек имеет право на второй шанс.")], "voiceover begins"),

    ("anya", "Некоторым сама жизнь даёт второй шанс.",
     "To some, life itself gives a second chance.",
     [(367, "Некоторым сама жизнь дает второй шанс.")], "voiceover continues"),

    ("anya", "Я обязательно докажу своё кулинарное мастерство.",
     "I will definitely prove my culinary mastery.",
     [], "determination expressed"),

    ("anya", "В общем, наша жизнь полна сюрпризов.",
     "In short, our life is full of surprises.",
     [(369, "В общем, жизнь..."), (370, "Полна сюрпризов.")], "iconic closing quote"),

    ("anya", "И главное приключение ещё только начинается!",
     "And the main adventure is only just beginning!",
     [], "looking forward"),
]

OPENER = "Let's explore Max's unexpected second chance and his closing philosophical reflection."

WALK = [
    (0, None,
     "'Runt, are you still standing here?' Barinov finds Max waiting outside the kitchen late at night."),
    (1, None,
     "'Chef, please, do not humiliate me anymore.' Max humbly asks for mercy after an exhausting first day."),
    (2, None,
     "'Tomorrow morning come to work on time.' The chef unexpectedly tells him to report for duty."),
    (3, None,
     "'Are you letting me stay to work in the restaurant?' Max is astonished by the unexpected reprieve."),
    (4, None,
     "'Chef, but why did you change your mind?' Max seeks to understand Barinov's motivation."),
    (5, None,
     "'Do not ask foolish questions, or I'll change my mind!' Barinov cuts him off with typical gruff humor."),
    (6, None,
     "'Chef, are you really letting him stay?' Ainura wonders why the temperamental chef yielded."),
    (7, None,
     "'I bet that he will run away on his own!' Barinov insists he only kept him to win a wager."),
    (8, None,
     "'In a week this guy will leave on his own.' The chef predicts Max won't survive the grueling kitchen."),
    (9, None,
     "'Every person has the right to a chance.' Max begins his philosophical closing reflection."),
    (10, None,
     "'To some, life itself gives a second chance.' Max reflects on the fortuitous turn of events."),
    (11, None,
     "'I will definitely prove my culinary mastery.' The young cook resolves to become a great chef."),
    (12, None,
     "'In short, our life is full of surprises.' The iconic closing phrase wraps up the pilot episode."),
    (13, None,
     "'And the main adventure is only just beginning!' Max looks ahead with excitement to his culinary journey."),
]

TRANSITION = "Now let's listen to the final scene of the pilot episode once more."

OUTRO = "Given a second chance in the prestigious kitchen, Max takes his first real step toward culinary greatness."

CLOSING = ("anya", "И главное приключение ещё только начинается!")
