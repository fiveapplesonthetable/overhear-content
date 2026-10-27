ID = "kukhnya-s01e14-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 18
TITLE = "Режим терминатора  (Terminator Mode)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Лёва', 'leva': 'Сеня', 'guest': 'Федя'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Back in the kitchen, Leva tries to assert his new authority as the temporary head chef. He orders the cooks to work faster. Senya and Fedya support him and joke about switching to Terminator mode. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ребята, давайте работать быстрее.",
     "Guys, let's work faster.",
     [(273, 'Ребят, давайте ускоримся.')], "adapted"),
    ("anya", "У нас ещё три блюда.",
     "We still have three dishes.",
     [(274, 'У нас три блюда еще.')], "adapted"),
    ("guest", "Сейчас мы всё сделаем.",
     "We will do everything now.",
     [(275, 'Сейчас все сделаем.')], "adapted"),
    ("leva", "Ну, чего вы стоите?",
     "Well, why are you standing?",
     [(276, 'Ну что встали?')], "adapted"),
    ("leva", "Шеф сказал работать быстрее.",
     "The chef said to work faster.",
     [(276, 'Шеф сказал ускориться.')], "adapted"),
    ("leva", "Молодец, Лёва.",
     "Well done, Leva.",
     [(277, 'Ай, молодец, Лёва, шеф.')], "adapted"),
    ("leva", "Ты хороший шеф.",
     "You are a good chef.",
     [(277, 'Ай, молодец, Лёва, шеф.')], "adapted"),
    ("anya", "Да, молодец.",
     "Yes, well done.",
     [(278, 'Молодец ты.')], "adapted"),
    ("guest", "Ну что, мы включаем режим терминатора?",
     "Well, are we switching on Terminator mode?",
     [(279, 'Ну что, включаем режим терминатора?')], "adapted"),
    ("anya", "Да, включаем.",
     "Yes, we are switching it on.",
     [], "exact"),
    ("leva", "Тогда быстрее за работу.",
     "Then faster to work.",
     [], "new"),
    ("guest", "Терминатор готов готовить еду.",
     "The terminator is ready to cook food.",
     [], "new"),
    ("anya", "Отлично, давайте быстрее.",
     "Excellent, let's go faster.",
     [], "new"),
    ("leva", "Всё будет готово вовремя.",
     "Everything will be ready on time.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Guys, let's work faster.' -- The speaker makes the statement."),
    (1, None,
     "'We still have three dishes.' -- The speaker makes the statement."),
    (2, None,
     "'We will do everything now.' -- The speaker makes the statement."),
    (3, None,
     "'Well, why are you standing?' -- The speaker makes the statement."),
    (4, None,
     "'The chef said to work faster.' -- The speaker makes the statement."),
    (5, None,
     "'Well done, Leva.' -- The speaker makes the statement."),
    (6, None,
     "'You are a good chef.' -- The speaker makes the statement."),
    (7, None,
     "'Yes, well done.' -- The speaker makes the statement."),
    (8, None,
     "'Well, are we switching on Terminator mode?' -- The speaker makes the statement."),
    (9, None,
     "'Yes, we are switching it on.' -- The speaker makes the statement."),
    (10, None,
     "'Then faster to work.' -- The speaker makes the statement."),
    (11, None,
     "'The terminator is ready to cook food.' -- The speaker makes the statement."),
    (12, None,
     "'Excellent, let's go faster.' -- The speaker makes the statement."),
    (13, None,
     "'Everything will be ready on time.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Всё будет готово вовремя.")
