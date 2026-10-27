ID = "kukhnya-s01e17-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 1
TITLE = "Уроки на рынке  (Market Lessons)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja"}
LABELS = {"anya": "Макс", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-32. Viktor takes Max to the fish market to teach him how to identify fresh produce. "
    "By observing the seller's nervous body language, Viktor reveals that the fish is several days old."
)

INTRO = (
    "Early in the morning, Viktor takes Max along to the bustling fish market. "
    "Determined to teach his young apprentice a vital culinary skill, Viktor demonstrates how to detect stale fish from a vendor's subtle gestures. "
    "Let's listen to their lesson in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("anya", "Я наступил в гнилую сливу, шеф.",
     "I stepped in a rotten plum, chef.",
     [(1, "Я только чувствую, что я в гнилую сливу наступил.")], "adapted"),
    ("shef", "Хватит ныть, у меня хорошее настроение.",
     "Quit whining, I am in a good mood.",
     [(2, "Хватит ныть. У меня хорошее настроение.")], "adapted"),
    ("shef", "Сегодня ты узнаешь искусство покупать рыбу.",
     "Today you will learn the art of buying fish.",
     [(3, "Поэтому ты познаешь сейчас древнее искусство покупать на рынке.")], "adapted"),
    ("shef", "Сколько дней этой рыбе, Макс?",
     "How many days old is this fish, Max?",
     [(4, "Как ты думаешь, сколько дней этой треске?")], "adapted"),
    ("anya", "Продавец говорит, что привезли сегодня.",
     "The seller says they brought it today.",
     [(7, "Один. Сегодня привезли.")], "adapted"),
    ("shef", "Смотри внимательно, он поджал губы.",
     "Watch closely, he pursed his lips.",
     [(8, "Смотри внимательно."), (10, "Смотри, губы поджал.")], "adapted"),
    ("shef", "Значит, этой рыбе минимум три дня.",
     "That means this fish is at least three days old.",
     [(11, "Это значит, что рыбе не менее трех дней.")], "adapted"),
    ("shef", "А сейчас он почесал нос.",
     "And now he scratched his nose.",
     [(13, "О, нос почесал.")], "adapted"),
    ("shef", "Этой рыбе уже пять дней.",
     "This fish is already five days old.",
     [(13, "Это значит, что рыбе не меньше пяти дней.")], "adapted"),
    ("shef", "И её точно замораживали раньше.",
     "And it was definitely frozen before.",
     [(14, "Да еще ее замораживали.")], "adapted"),
    ("anya", "Шеф, вы настоящий мастер своего дела.",
     "Chef, you are a true master of your craft.",
     [], "new"),
    ("shef", "Учись у меня, пока я добрый.",
     "Learn from me while I am kind.",
     [], "new"),
    ("anya", "Спасибо за этот важный урок, шеф.",
     "Thank you for this important lesson, chef.",
     [], "new"),
]

WALK = [
    (0, None,
     "'I stepped in a rotten plum, chef.' -- Max complains about the dirty market floor."),
    (1, None,
     "'Quit whining, I am in a good mood.' -- Viktor cuts off the complaint cheerfully."),
    (2, None,
     "'Today you will learn the art of buying fish.' -- The chef announces their practical lesson."),
    (3, None,
     "'How many days old is this fish, Max?' -- Viktor quizzes his young apprentice."),
    (4, None,
     "'The seller says they brought it today.' -- Max repeats the vendor's claim innocently."),
    (5, None,
     "'Watch closely, he pursed his lips.' -- Viktor highlights the seller's guilty expression."),
    (6, None,
     "'That means this fish is at least three days old.' -- The chef explains the hidden meaning of the gesture."),
    (7, None,
     "'And now he scratched his nose.' -- Viktor spots another clear sign of deception."),
    (8, None,
     "'This fish is already five days old.' -- The chef calculates the true age of the product."),
    (9, None,
     "'And it was definitely frozen before.' -- Viktor notes the poor condition of the fish."),
    (10, None,
     "'Chef, you are a true master of your craft.' -- Max praises his mentor's sharp observation."),
    (11, None,
     "'Learn from me while I am kind.' -- Viktor tells him to appreciate the advice."),
    (12, None,
     "'Thank you for this important lesson, chef.' -- Max expresses genuine gratitude to the head chef."),
]

TRANSITION = "Now let's listen to the market lesson once more without interruption."

OUTRO = (
    "Having exposed the vendor's dishonest sales tactics, Viktor and Max continue through the market, "
    "ready to return to Claude Monet with fresh knowledge."
)

CLOSING = ("anya", "Спасибо за этот важный урок, шеф.")
