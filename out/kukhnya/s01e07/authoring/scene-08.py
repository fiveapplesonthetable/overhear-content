"""s01e07 scene 08: Совет от Макса (Advice from Max)."""

ID = "kukhnya-s01e07-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 8
TITLE = "Совет от Макса  (Advice from Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "anja"}
LABELS = {"anya": "Макс", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"

INTRO = (
    "In the dining room between shifts, Max asks waitress Nastya if she knows of any cheap rooms for rent in Moscow. "
    "To his horror, she reveals that Kostya just invited her to move into their shared flat. "
    "Desperate to protect his living space, Max cleverly persuades Nastya that living with Kostya would be a noisy nightmare. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Настя, ты знаешь, где сдать квартиру?",
     "Nastya, do you know where to rent a flat?",
     [(86, "Настя, тебя никто знакомый квартиру не сдает")], "inquiring about housing"),
    ("nastya", "Сама искала жильё сегодня утром.",
     "I was looking for a place myself this morning.",
     [(88, "Сама только утром искала")], "sharing her own housing search"),
    ("anya", "И тебе удалось найти комнату?",
     "And did you manage to find a room?",
     [], "asking about her search result"),
    ("nastya", "Мне помог Костик, я переезжаю к нему.",
     "Kostik helped me, I am moving to his place.",
     [(89, "Ну, предложил у него пожить")], "announcing her move"),
    ("anya", "Погоди, Костя позвал тебя жить вместе?",
     "Wait, Kostya invited you to live together?",
     [(91, "Погоди. То есть, Костя тебя позвал, да")], "reacting in shock"),
    ("nastya", "Да, мы ведь с ним встречаемся.",
     "Yes, after all he and I are dating.",
     [(90, "Мы вообще встречаемся")], "justifying the decision"),
    ("anya", "Честно говоря, я тебе совсем не завидую.",
     "To be honest, I do not envy you at all.",
     [(93, "Хотя, не завидую я тебе")], "sowing doubt"),
    ("nastya", "Почему? Костя такой милый парень.",
     "Why? Kostya is such a sweet guy.",
     [], "defending Kostya"),
    ("anya", "Он ночью страшно и громко храпит!",
     "At night he snores terribly and loudly!",
     [(94, "просто он храпит по-конски")], "inventing a terrible flaw"),
    ("nastya", "Ой, я совсем не выношу храп!",
     "Oh, I cannot stand snoring at all!",
     [(104, "Все-таки не люблю, когда храпят")], "revealing her intolerance to noise"),
    ("anya", "Подумай хорошо, прежде чем соглашаться.",
     "Think well before agreeing.",
     [(103, "Знаешь, наверное, не буду у Кости жить")], "giving cautionary advice"),
    ("nastya", "Ты прав, поищу другой вариант.",
     "You are right, I will look for another option.",
     [(107, "Спасибо, Макс")], "deciding against moving in"),
]

OPENER = "Let's review this sneaky and hilarious conversation line by line."

WALK = [
    (0, None,
     "'Nastya, do you know where to rent a flat?' Max casually asks if she has any apartment leads."),
    (1, None,
     "'I was looking for a place myself this morning.' Nastya explains that she was recently displaced herself."),
    (2, None,
     "'And did you manage to find a room?' Max asks whether she had any luck on the rental market."),
    (3, None,
     "'Kostik helped me, I am moving to his place.' Nastya happily drops the bombshell news."),
    (4, None,
     "'Wait, Kostya invited you to live together?' Max freezes upon realizing his flatmate offered up their shared apartment."),
    (5, None,
     "'Yes, after all he and I are dating.' Nastya treats moving in together as the natural next step."),
    (6, None,
     "'To be honest, I do not envy you at all.' Max adopts a serious tone to discourage her."),
    (7, None,
     "'Why? Kostya is such a sweet guy.' Nastya is taken aback by Max's warning."),
    (8, None,
     "'At night he snores terribly and loudly!' Max fabricates a severe sleep disruption to scare her off."),
    (9, None,
     "'Oh, I cannot stand snoring at all!' Nastya admits that nighttime noise is her biggest pet peeve."),
    (10, None,
     "'Think well before agreeing.' Max feigns brotherly concern as he protects his bachelor pad."),
    (11, None,
     "'You are right, I will look for another option.' Nastya gratefully takes his advice and cancels her move."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Relieved that his bachelor apartment is safe, Max smiles as Nastya decides to find alternative lodging. "
    "See you next time!"
)

CLOSING = ("nastya", "Ты прав, поищу другой вариант.")
