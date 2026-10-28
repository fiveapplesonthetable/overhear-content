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
     "'Guys, let's work faster.' — Notice the noun meaning 'the boys, the lads' paired with the verb for 'let's (do it)'."),
    (1, None,
     "'We still have three dishes.' — Notice the pronoun meaning 'us' paired with the adverb for 'more, still'."),
    (2, None,
     "'We will do everything now.' — Notice the adverb meaning 'now' paired with the pronoun for 'we'."),
    (3, None,
     "'Well, why are you standing?' — Notice the pronoun meaning 'what?' paired with the pronoun for 'you'."),
    (4, None,
     "'The chef said to work faster.' — Notice the proper name meaning 'chef, boss' paired with the verb for 'said'."),
    (5, None,
     "'Well done, Leva.' — Notice the noun meaning 'well done, good boy' paired with the proper name for 'Lyova'."),
    (6, None,
     "'You are a good chef.' — Notice the pronoun meaning 'you' paired with the adjective for 'good'."),
    (7, None,
     "'Yes, well done.' — Built around the key noun meaning 'well done, good boy'."),
    (8, None,
     "'Well, are we switching on Terminator mode?' — Notice the pronoun meaning 'what' paired with the pronoun for 'we'."),
    (9, None,
     "'Yes, we are switching it on.' — Built around the key verb meaning 'we're switching on'."),
    (10, None,
     "'Then faster to work.' — Notice the adverb meaning 'back then' paired with the adverb for 'faster'."),
    (11, None,
     "'The terminator is ready to cook food.' — Notice the noun meaning 'Terminator' paired with the adjective for 'ready'."),
    (12, None,
     "'Excellent, let's go faster.' — Notice the adverb meaning 'perfect, great' paired with the verb for 'let's (do it)'."),
    (13, None,
     "'Everything will be ready on time.' — Notice the det meaning 'everything' paired with the verb for 'will be'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Всё будет готово вовремя.")
