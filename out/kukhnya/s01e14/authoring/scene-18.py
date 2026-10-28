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
     "'Guys, let's work faster.' Lyova puts 'the boys' up front so the listener immediately catches the tone, followed by 'let's'."),
    (1, None,
     "'We still have three dishes.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'us' straight to 'of dish'."),
    (2, None,
     "'We will do everything now.' Here 'now' sets up the idea, while 'we'll do' comes at the end for emphasis."),
    (3, None,
     "'Well, why are you standing?' Senya starts with 'what?' and pairs it with 'you' to make the point clear."),
    (4, None,
     "'The chef said to work faster.' — Notice the proper name meaning 'chef, boss' paired with the verb for 'said'."),
    (5, None,
     "'Well done, Leva.' Senya starts with 'well done' and pairs it with 'Lyova' to make the point clear."),
    (6, None,
     "'You are a good chef.' Senya uses the casual singular 'you' with 'you', as close colleagues and friends do. And Lyova jumps in."),
    (7, None,
     "'Yes, well done.' In Russian, 'well done' leads into 'well done' in a very natural everyday phrasing."),
    (8, None,
     "'Well, are we switching on Terminator mode?' The first content word means 'what', and 'Terminator' rounds out the thought."),
    (9, None,
     "'Yes, we are switching it on.' Lyova starts with 'we're switching on' and pairs it with 'we're switching on' to make the point clear. Senya answers straight away."),
    (10, None,
     "'Then faster to work.' Listen for the word meaning 'back then' right alongside 'faster' in this line."),
    (11, None,
     "'The terminator is ready to cook food.' The key word here means 'Terminator', which Fedya combines with 'ready'."),
    (12, None,
     "'Excellent, let's go faster.' Here 'perfect' sets up the idea, while 'faster' comes at the end for emphasis. Then Senya replies."),
    (13, None,
     "'Everything will be ready on time.' You'll hear 'will be' all the time in the show, here connected with 'at the right time'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around terminator mode, and for the words meaning 'the boys' and 'let's'. You'll catch them now. See you next time."
CLOSING = ("leva", "Всё будет готово вовремя.")
