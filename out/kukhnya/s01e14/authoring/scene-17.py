ID = "kukhnya-s01e14-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 17
TITLE = "Защитник Лёва  (Defender Leva)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Лёва', 'leva': 'Луи', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the dining room, an angry guest complains to the pastry chef Louis about finding something hard in his dessert. Louis is terrified. Leva bravely steps in, claims to be the head chef, and takes responsibility. Let us listen to their conversation in Russian first."
)

STORY = [
    ("guest", "Что это у меня в десерте?",
     "What is this in my dessert?",
     [(253, 'Че за хрень у меня в десерте?')], "adapted"),
    ("guest", "Я из-за вас чуть зуб не сломал!",
     "I almost broke a tooth because of you!",
     [(254, 'А? Из-за тебя?'), (255, 'Я еще зуба не лишился.')], "adapted"),
    ("leva", "Простите нас, пожалуйста.",
     "Please forgive us.",
     [(256, 'Простите меня, пожалуйста.')], "adapted"),
    ("guest", "Ты сначала по-русски говорить научись!",
     "First, learn to speak Russian!",
     [(256, 'Ты сначала научись по-русски разговаривать.')], "adapted"),
    ("guest", "Зачем ты сюда приехал?",
     "Why did you come here?",
     [(257, 'Ты чего сюда приехал, а?')], "adapted"),
    ("guest", "Чтобы люди ломали зубы?",
     "So people would break their teeth?",
     [(258, 'Чтобы народ зубы ломал?')], "adapted"),
    ("leva", "Я кондитер, это моя вина.",
     "I am the pastry chef, it is my fault.",
     [], "new"),
    ("anya", "Оставьте кондитера в покое.",
     "Leave the pastry chef alone.",
     [(264, 'Оставьте в покое кондитера.')], "adapted"),
    ("guest", "А ты кто такой?",
     "And who are you?",
     [(265, 'А ты кто такой?')], "adapted"),
    ("anya", "Я шеф-повар этого ресторана.",
     "I am the head chef of this restaurant.",
     [(265, 'Я шеф-повар.')], "adapted"),
    ("anya", "Я отвечаю за всё на кухне.",
     "I am responsible for everything in the kitchen.",
     [(266, 'И я несу ответственность за все, что происходит на кухне.')], "adapted"),
    ("anya", "У вас есть претензии ко мне?",
     "Do you have complaints against me?",
     [(267, 'И если у вас есть какие-то претензии...')], "adapted"),
    ("guest", "Вот моя претензия, держите.",
     "Here is my complaint, hold it.",
     [(269, 'Вот.')], "adapted"),
    ("leva", "Вкусный десерт, большое спасибо.",
     "Delicious dessert, thank you very much.",
     [(272, 'Вкусный десерт с коньяком.')], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'What is this in my dessert?' -- The speaker makes the statement."),
    (1, None,
     "'I almost broke a tooth because of you!' -- The speaker makes the statement."),
    (2, None,
     "'Please forgive us.' -- The speaker makes the statement."),
    (3, None,
     "'First, learn to speak Russian!' -- The speaker makes the statement."),
    (4, None,
     "'Why did you come here?' -- The speaker makes the statement."),
    (5, None,
     "'So people would break their teeth?' -- The speaker makes the statement."),
    (6, None,
     "'I am the pastry chef, it is my fault.' -- The speaker makes the statement."),
    (7, None,
     "'Leave the pastry chef alone.' -- The speaker makes the statement."),
    (8, None,
     "'And who are you?' -- The speaker makes the statement."),
    (9, None,
     "'I am the head chef of this restaurant.' -- The speaker makes the statement."),
    (10, None,
     "'I am responsible for everything in the kitchen.' -- The speaker makes the statement."),
    (11, None,
     "'Do you have complaints against me?' -- The speaker makes the statement."),
    (12, None,
     "'Here is my complaint, hold it.' -- The speaker makes the statement."),
    (13, None,
     "'Delicious dessert, thank you very much.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Вкусный десерт, большое спасибо.")
