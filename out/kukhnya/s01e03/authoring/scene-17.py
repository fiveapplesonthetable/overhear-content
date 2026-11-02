# Authoring module for kukhnya-s01e03-scene-17.
ID = 'kukhnya-s01e03-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 17
TITLE = 'Опасная ссора  (A Dangerous Quarrel)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vadim': 'Вадим', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "Behind the restaurant, Max catches Vika alone and apologises for his clumsy behaviour. Their uneasy talk is cut short when Vadim arrives, demanding to know what is going on, and things turn dangerous. Here's the Russian first."
OPENER = 'Now the quarrel.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'A threat, a gun, and one very brave cook. Remember the command to step away from her, something you hope never to need to say.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, пожалуйста, прости меня за всё.', 'Vika, please forgive me for everything.', [(298, 'ну прости меня')], ''),
    ('vika', 'Почему я всегда верю не тем людям?', 'Why do I always trust the wrong people?', [(301, 'Ну почему меня тянет')], ''),
    ('max', 'Каждый человек может совершить ошибку.', 'Every person can make a mistake.', [(304, 'все ошибаются')], ''),
    ('vika', 'Я сама виновата в этой ситуации.', 'I myself am to blame for this situation.', [(306, 'это я виновата')], ''),
    ('vadim', 'Так значит, это правда, вы вместе?', 'So that means it is true, you are together?', [(310, 'Так значит, это правда')], ''),
    ('vika', 'Вадим, что ты здесь делаешь?', 'Vadim, what are you doing here?', [(309, 'Вадик')], ''),
    ('vadim', 'Я пришёл поговорить с тобой прямо сейчас.', 'I came to talk with you right now.', [], ''),
    ('vadim', 'А этот парень должен немедленно уйти!', 'And this guy must leave immediately!', [], ''),
    ('max', 'Выбирай слова, когда говоришь с ней!', 'Choose your words when talking with her!', [(312, 'подбирай выражение')], ''),
    ('max', 'Ты разговариваешь с красивой девушкой.', 'You are talking to a beautiful girl.', [(313, 'с девушкой разговариваешь')], ''),
    ('vadim', 'Ты что мне сейчас сказал, щенок?', 'What did you just say to me, pup?', [(314, 'Ты что сказал')], ''),
    ('max', 'Я сказал тебе: отойди от неё!', 'I told you: step away from her!', [(315, 'отстань от неё сказал')], ''),
    ('vika', 'Макс, прекрати, у него есть пистолет!', 'Max, stop, he has a gun!', [(318, 'Прячь мушку')], ''),
]
WALK = [
    (0, None, [
        "'Vika, please forgive me for everything.' The word for forgive is ",
        ('max', 'прости'),
        ", which is the informal shape for the action. And ",
        ('max', 'за всё.'),
        " translates to 'for everything'."
    ]),
    (1, None, [
        "'Why do I always trust the wrong people?' The word for trust, ",
        ('vika', 'верю'),
        ", also means 'believe'. The phrase ",
        ('vika', 'не тем'),
        " literally translates to 'not to those', which is how you say 'the wrong ones'."
    ]),
    (2, None, [
        "'Every person can make a mistake.' The phrase ",
        ('max', 'совершить ошибку.'),
        " translates to 'commit a mistake', a slightly formal way to say it. Notice the ending changes because it is the target of the action."
    ]),
    (3, None, [
        "'I myself am to blame for this situation.' The word for to blame is ",
        ('vika', 'виновата'),
        ", which is built from the word for fault, with a woman's ending. The word for myself, ",
        ('vika', 'сама'),
        ", also has a matching ending."
    ]),
    (4, None, [
        "'So that means it is true, you are together?' The phrase ",
        ('vadim', 'Так значит,'),
        " translates to 'so it means', used for putting two and two together. And ",
        ('vadim', 'вы'),
        " is the shape for more than one person here, for both of them."
    ]),
    (5, None, [
        "'Vadim, what are you doing here?' The phrase ",
        ('vika', 'что ты здесь делаешь?'),
        " literally translates to 'what you here do?'. The language has no action shape for '-ing', so the plain present action word does the job."
    ]),
    (6, None, [
        "'I came to talk with you right now.' The action word ",
        ('vadim', 'пришёл'),
        " is the shape for a man and translates to 'came on foot'. The phrase ",
        ('vadim', 'поговорить с тобой'),
        " translates to 'to talk with you'."
    ]),
    (7, None, [
        "'And this guy must leave immediately!' The word for a guy is ",
        ('vadim', 'парень'),
        ", while ",
        ('vadim', 'должен'),
        " is the word for 'must' with a man's ending, and ",
        ('vadim', 'уйти!'),
        " literally translates to 'to go away'."
    ]),
    (8, None, [
        "'Choose your words when talking with her!' Max now uses the informal shape to Vadim, saying ",
        ('max', 'Выбирай'),
        " and ",
        ('max', 'говоришь'),
        " instead of the formal ones. The phrase ",
        ('max', 'с ней!'),
        " translates to 'with her'."
    ]),
    (9, None, [
        "'You are talking to a beautiful girl.' The word for 'you are talking', ",
        ('max', 'разговариваешь'),
        ", is built from the word for a conversation. The phrase ",
        ('max', 'с красивой девушкой.'),
        " has matching endings on both words after the word for 'with'."
    ]),
    (10, None, [
        "'What did you just say to me, pup?' The word for puppy is ",
        ('vadim', 'щенок?'),
        " which is an insult for a young man here. The phrase ",
        ('vadim', 'Ты что'),
        " at the start translates to a challenge."
    ]),
    (11, None, [
        "'I told you: step away from her!' The word for the command to step away is ",
        ('max', 'отойди'),
        ", while ",
        ('max', 'от неё!'),
        " translates to 'from her', where the word for 'her' picks up an extra sound after the word for 'from'."
    ]),
    (12, None, [
        "'Max, stop, he has a gun!' The language has no simple way to say 'he has'. Instead, the phrase ",
        ('vika', 'у него есть'),
        " literally translates to 'at him there is', followed by the thing. And ",
        ('vika', 'прекрати,'),
        " is a sharp informal command that translates to 'cut it out'."
    ]),
]
