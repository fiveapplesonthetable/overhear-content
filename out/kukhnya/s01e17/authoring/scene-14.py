# Authoring module for kukhnya s01e17 scene 14 (cues 231-240).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-14.py --out out/kukhnya/s01e17/scene-14.json

ID = "kukhnya-s01e17-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 14
TITLE = "Подарок на день рождения  (A Birthday Gift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "nastya": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 231-240. At Claude Monet, Kostya and Nastya wish Max a happy birthday and give him a ticket "
    "to a DJ concert so the three of them can celebrate together tonight."
)

INTRO = (
    "In the kitchen at Claude Monet, Kostya and Nastya approach Max with warm smiles to celebrate his birthday. "
    "They hand him a special concert ticket so the three friends can go out and party together tonight. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("kostya", "Макс, поздравляю тебя с днём рождения!",
     "Max, happy birthday to you!",
     [(231, "Макс. С днем рождения")], "adapted"),
    ("anya", "Большое спасибо тебе, мой верный друг.",
     "Thank you very much, my loyal friend.",
     [(232, "Спасибо. Старик")], "adapted"),
    ("nastya", "Я тоже от души поздравляю тебя!",
     "I also congratulate you from the heart!",
     [(233, "Поздравляю")], "adapted"),
    ("anya", "Спасибо, Настя, мне очень приятно.",
     "Thank you, Nastya, I am very pleased.",
     [(233, "спасибо")], "adapted"),
    ("kostya", "А вот этот подарок для тебя.",
     "And here is this gift for you.",
     [(234, "А вот это тебе")], "adapted"),
    ("anya", "Что это за красивые билеты?",
     "What kind of nice tickets are these?",
     [(235, "Билеты на концерт")], "adapted"),
    ("kostya", "Это билеты на хороший вечерний концерт.",
     "These are tickets to a good evening concert.",
     [(235, "Билеты на концерт")], "adapted"),
    ("nastya", "Мы отлично повеселимся сегодня вечером вместе.",
     "We will have a great time together tonight.",
     [(236, "Отлично повеселимся")], "adapted"),
    ("kostya", "Пойдём туда ты, я и Настя.",
     "You, me, and Nastya will go there.",
     [(236, "Ты, я и Настя")], "adapted"),
    ("nastya", "Мы будем танцевать там всю ночь!",
     "We will dance there all night!",
     [(237, "Оторвемся по полной")], "adapted"),
    ("anya", "Спасибо, ребята, вы настоящие друзья.",
     "Thanks, guys, you are real friends.",
     [(238, "Спасибо. Ребята")], "adapted"),
    ("kostya", "Да ладно, у тебя же праздник!",
     "Come on, it is your holiday after all!",
     [(238, "да ладно")], "adapted"),
    ("nastya", "Ведь у тебя сегодня день рождения.",
     "After all, today is your birthday.",
     [(239, "У тебя же день рождения")], "adapted"),
    ("kostya", "Ещё раз с днём рождения, Макс!",
     "Happy birthday once again, Max!",
     [(240, "С днем рождения")], "adapted"),
]

WALK = [
    (0, None,
     "'Max, happy birthday to you!' -- Kostya greets his best friend and roommate on his special day."),
    (1, None,
     "'Thank you very much, my loyal friend.' -- Max warmly thanks Kostya for the greeting."),
    (2, None,
     "'I also congratulate you from the heart!' -- Nastya joins in with an enthusiastic birthday wish."),
    (3, None,
     "'Thank you, Nastya, I am very pleased.' -- Max expresses his gratitude to the kind waitress."),
    (4, None,
     "'And here is this gift for you.' -- Kostya hands over a birthday surprise."),
    (5, None,
     "'What kind of nice tickets are these?' -- Max looks curiously at the printed passes."),
    (6, None,
     "'These are tickets to a good evening concert.' -- Kostya explains that they are for a popular music show."),
    (7, None,
     "'We will have a great time together tonight.' -- Nastya looks forward to celebrating after work."),
    (8, None,
     "'You, me, and Nastya will go there.' -- Kostya confirms that the three of them are going as a group."),
    (9, None,
     "'We will dance there all night!' -- Nastya promises an energetic night on the dance floor."),
    (10, None,
     "'Thanks, guys, you are real friends.' -- Max is touched by their thoughtful present."),
    (11, None,
     "'Come on, it is your holiday after all!' -- Kostya brushes off the thanks with friendly warmth."),
    (12, None,
     "'After all, today is your birthday.' -- Nastya reminds him that the occasion calls for a party."),
    (13, None,
     "'Happy birthday once again, Max!' -- Kostya gives his friend one more celebratory cheer."),
]

TRANSITION = "Now let's listen to the whole birthday celebration scene again without interruption."
OUTRO = (
    "Delighted by the concert ticket from Kostya and Nastya, Max looks forward to celebrating his birthday "
    "with his closest friends after their shift."
)
CLOSING = ("kostya", "Ещё раз с днём рождения, Макс!")
