"""Scene 34 — Outtakes and Bloopers (s01e08, 00:22:24–00:23:29)."""

ID = "kukhnya-s01e08-scene-34"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 34
TITLE = "Неудачные дубли  (Outtakes and Bloopers)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
    "chef": "angelina",
}

LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
    "chef": "Шеф",
}

INTRO = (
    "As the shift winds down and credits roll, the restaurant crew unwinds with playful teasing and hilarious outtakes. "
    "Kostya works up the courage to ask Nastya to the movies, while Chef Barinov vents loudly about his beloved football match."
)

STORY = [
    ("kostya", "Настя, прекрати так громко смеяться на кухне!",
     "Nastya, stop laughing so loudly in the kitchen!",
     [], "Kostya complains"),

    ("anya", "Костя, ты сегодня очень сердитый и смешной.",
     "Kostya, you are very angry and funny today.",
     [], "Nastya teases"),

    ("kostya", "Я просто устал после долгой тяжёлой смены.",
     "I am simply tired after a long hard shift.",
     [], "Kostya explains"),

    ("anya", "Ты всегда сердишься без всякой причины.",
     "You always get angry without any reason.",
     [], "Nastya smiles"),

    ("kostya", "Пойдёшь со мной сегодня вечером в кино?",
     "Will you go to the cinema with me tonight?",
     [(379, "Пойдешь к кино?")], "Kostya asks out"),

    ("anya", "Ну ты настоящий чудак, конечно пойду!",
     "Well you are a real oddball, of course I will go!",
     [(380, "Ну ты придурок.")], "Nastya agrees"),

    ("kostya", "Тогда встречаемся в семь часов около метро.",
     "Then we meet at seven o'clock near the metro.",
     [(381, "Ладно, пойдем. Тогда до вечера.")], "Kostya sets time"),

    ("chef", "Кто опять трогал мою любимую кастрюлю?!",
     "Who touched my favorite pot again?!",
     [(382, "Подонки!")], "Chef shouts from afar"),

    ("chef", "Ты за кого сегодня болел на матче?!",
     "Who were you rooting for today at the match?!",
     [(383, "Ты за кого болел? Ты за кого болел?")], "Chef interrogates"),

    ("kostya", "Шеф опять кричит про свой любимый футбол.",
     "The chef is shouting again about his favorite football.",
     [], "Kostya whispers"),

    ("anya", "Он всегда так громко переживает за Спартак.",
     "He always worries so loudly about Spartak.",
     [], "Nastya giggles"),

    ("chef", "Футбол — это самое главное в жизни!",
     "Football is the most important thing in life!",
     [], "Chef declares"),

    ("kostya", "Пойдём скорее отсюда, пока он спокоен.",
     "Let's go quickly from here while he is calm.",
     [], "Kostya suggests"),

    ("anya", "Да, идём скорее смотреть весёлый фильм!",
     "Yes, let's go quickly to watch a fun movie!",
     [], "Nastya agrees happily"),
]

OPENER = "Let's enjoy the post-shift banter between Kostya and Nastya alongside Chef Barinov's fiery football passion."

WALK = [
    (0, None,
     "'Nastya, stop laughing so loudly in the kitchen!' Kostya grumbles playfully after their shift."),
    (1, None,
     "'Kostya, you are very angry and funny today.' Nastya teases the flustered bartender with a grin."),
    (2, None,
     "'I am simply tired after a long hard shift.' Kostya defends his weary attitude at the bar."),
    (3, None,
     "'You always get angry without any reason.' Nastya laughs at his constant complaints."),
    (4, None,
     "'Will you go to the cinema with me tonight?' Kostya suddenly invites her out on a date."),
    (5, None,
     "'Well you are a real oddball, of course I will go!' Nastya cheerfully accepts the invitation."),
    (6, None,
     "'Then we meet at seven o'clock near the metro.' Kostya confirms their evening rendezvous plans."),
    (7, None,
     "'Who touched my favorite pot again?!' Chef Barinov yells unexpectedly from inside the office."),
    (8, None,
     "'Who were you rooting for today at the match?!' Barinov demands passionate football loyalty from everyone."),
    (9, None,
     "'The chef is shouting again about his favorite football.' Kostya whispers amusedly as the shouting echoes."),
    (10, None,
     "'He always worries so loudly about Spartak.' Nastya giggles at Barinov's fiery sports devotion."),
    (11, None,
     "'Football is the most important thing in life!' Barinov proclaims passionately from down the hall."),
    (12, None,
     "'Let's go quickly from here while he is calm.' Kostya urges a prompt exit before duties resume."),
    (13, None,
     "'Yes, let's go quickly to watch a fun movie!' Nastya smiles as they leave the restaurant together."),
]

TRANSITION = "Now let's listen to the lighthearted conversation and Chef Barinov's shouting one more time."

OUTRO = "A demanding shift at Claude Monet comes to an end with laughter, plans for romance, and endless passion for football."

CLOSING = ("anya", "Да, идём скорее смотреть весёлый фильм!")
