ID = "kukhnya-s02e03-scene-18"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 18
TITLE = 'Ремень в салате  (A Belt in the Salad)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "guest": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"
SOURCE_NOTE = "Scene 18"

INTRO = 'A furious customer calls the waitress over after finding something completely unacceptable hidden inside his fancy turkey salad. He demands an immediate explanation for the horrible mistake.'

STORY = [
    ('guest', 'Официант, подойдите сюда.',
     'Waiter, come here.',
     [], 'new'),
    ('vika', 'Да.',
     'Yes?',
     [(282, 'Да')], 'adapted'),
    ('guest', 'Посмотрите в мою тарелку.',
     'Look into my plate.',
     [], 'new'),
    ('vika', 'Извините, в чём проблема?',
     'Excuse me, what is the problem?',
     [], 'new'),
    ('guest', 'Это что?',
     'What is this?',
     [(283, 'Это что')], 'adapted'),
    ('vika', 'Салат из индейки.',
     'Turkey salad.',
     [(284, 'Салат из индейки')], 'adapted'),
    ('guest', 'Вы смеётесь надо мной?',
     'Are you laughing at me?',
     [], 'new'),
    ('guest', 'А индейка была в брюках и ремне?',
     'Was the turkey wearing pants and a belt?',
     [(285, 'индейка была в брюках и ремне')], 'adapted'),
    ('vika', 'Я сейчас позову администратора.',
     'I will call the manager right now.',
     [], 'new'),
    ('guest', 'Мне не нужен администратор.',
     'I do not need the manager.',
     [], 'new'),
    ('guest', 'Ну-ка, давай зови сюда ущербного, который ты готовила.',
     'Go get the idiot who made this.',
     [(286, 'зови сюда ущербного, который ты готовила')], 'adapted'),
    ('anya', 'Что здесь происходит?',
     'What is happening here?',
     [], 'new'),
    ('vika', 'Гость нашёл ремень в салате.',
     'The guest found a belt in the salad.',
     [], 'new'),
    ('anya', 'Я сейчас разберусь с этим.',
     'I will sort this out now.',
     [], 'new'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (4, None,
     "'What is this?' In Russian, 'this' leads into 'what' in a very natural everyday phrasing. Vika answers straight away."),
    (5, None,
     "'Turkey salad.' Notice the word order: 'salad' comes first, and 'turkey' finishes the sentence."),
    (7, None,
     "'Was the turkey wearing pants and a belt?' the guest starts with 'turkey' and pairs it with 'was' to make the point clear."),
    (10, None,
     "'Go get the idiot who made this.' the guest puts 'let's' up front so the listener immediately catches the tone, followed by 'call'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = 'The waitress runs to the kitchen to fetch the person responsible for this cooking disaster.'
CLOSING = ('anya', 'Я сейчас разберусь с этим.')
