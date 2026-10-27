"""Scene 22 — Everyone Is Safe (s01e12, 00:22:00–00:22:19)."""

ID = "kukhnya-s01e12-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 22
TITLE = "Все в безопасности  (Everyone Is Safe)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
    "guest": "angelina",
}

LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
    "guest": "Гость",
}

INTRO = (
    "After a sudden kitchen fire breaks out in the rival dining establishment next door, Kostya bravely guides the panicking crowd onto the sidewalk. "
    "Relieved to see her boyfriend unhurt, Nastya embraces him proudly as the hungry patrons turn to Claude Monet for dinner."
)

STORY = [
    ("kostya", "Настя, не бойся, огонь уже потушили.",
     "Nastya, do not be afraid, they already put out the fire.",
     [], "Kostya reassures Nastya"),

    ("kostya", "Все люди здесь сейчас в безопасности.",
     "All the people here are safe now.",
     [(281, "Все здесь в безопасности.")], "Kostya checks crowd"),

    ("anya", "Костя, огромное спасибо тебе за помощь.",
     "Kostya, thank you so much for the help.",
     [(282, "Спасибо тебе.")], "Nastya hugs Kostya"),

    ("anya", "Ты у меня такой смелый парень!",
     "You are such a brave guy to me!",
     [(282, "Ты у меня такой смелый.")], "Nastya praises boyfriend"),

    ("kostya", "Я просто помог людям выйти на улицу.",
     "I simply helped the people go outside.",
     [], "Kostya shrugs modestly"),

    ("anya", "Ты настоящий герой нашего ресторана!",
     "You are a real hero of our restaurant!",
     [], "Nastya beams with pride"),

    ("guest", "Просим прощения за эти неудобства.",
     "We ask for forgiveness for this inconvenience.",
     [(283, "неудобства.")], "Guest overhears announcement"),

    ("guest", "Соседнее кафе закрыто по техническим причинам.",
     "The neighboring cafe is closed for technical reasons.",
     [(284, "по техническим причинам.")], "Guest shakes head"),

    ("guest", "А где же нам теперь поужинать?",
     "And where do we have dinner now?",
     [], "Hungry guest wonders"),

    ("guest", "Слушайте, пойдём лучше в тот ресторан!",
     "Hey, let's go to that other restaurant instead!",
     [(285, "Слушайте, пойдем лучше в тот ресторан.")], "Guest points to Claude Monet"),

    ("anya", "Все гости идут прямо к нам!",
     "All the guests are coming straight to us!",
     [], "Nastya notices influx"),

    ("kostya", "Сегодня наш зал будет полон людей.",
     "Today our dining room will be full of people.",
     [], "Kostya smiles warmly"),

    ("anya", "Пойдём скорее на работу, любимый бармен!",
     "Let's go quickly to work, beloved bartender!",
     [], "Nastya urges Kostya inside"),
]

OPENER = "Let's join Kostya and Nastya outside on the sidewalk as displaced guests decide where to dine."

WALK = [
    (0, None,
     "'Nastya, do not be afraid, they already put out the fire.' Kostya reassures his anxious girlfriend on the street."),
    (1, None,
     "'All the people here are safe now.' He checks that everyone escaped the smoke safely."),
    (2, None,
     "'Kostya, thank you so much for the help.' Nastya embraces him with heartfelt relief."),
    (3, None,
     "'You are such a brave guy to me!' She praises his quick thinking and courage."),
    (4, None,
     "'I simply helped the people go outside.' Kostya modestly downplays his rescue effort."),
    (5, None,
     "'You are a real hero of our restaurant!' Nastya looks at him with pure admiration."),
    (6, None,
     "'We ask for forgiveness for this inconvenience.' The neighboring venue announces its sudden closure."),
    (7, None,
     "'The neighboring cafe is closed for technical reasons.' A displaced diner reads the hasty warning sign."),
    (8, None,
     "'And where do we have dinner now?' Hungry patrons look around for an open kitchen."),
    (9, None,
     "'Hey, let's go to that other restaurant instead!' A cheerful diner spots the inviting lights of Claude Monet."),
    (10, None,
     "'All the guests are coming straight to us!' Nastya watches the crowd cross the street eagerly."),
    (11, None,
     "'Today our dining room will be full of people.' Kostya welcomes the unexpected wave of evening customers."),
    (12, None,
     "'Let's go quickly to work, beloved bartender!' Nastya leads the way back inside the lively dining room."),
]

TRANSITION = "Now let's listen to the bustling conversation outside the restaurant once again."

OUTRO = "Thanks to Kostya's brave evacuation and the rival kitchen's mishap, Claude Monet fills with eager dinner guests."

CLOSING = ("anya", "Пойдём скорее на работу, любимый бармен!")
