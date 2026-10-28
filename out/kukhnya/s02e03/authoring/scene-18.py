# Authoring module for kukhnya-s02e03-scene-18.
ID = 'kukhnya-s02e03-scene-18'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 18
TITLE = "Ремень в салате  (A Belt in the Salad)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "guest": "anja", "vika": "angelina", "anya": "alisa"}
LABELS = {"guest": "Гость", "vika": "Вика", "anya": "Макс"}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = 'A furious customer calls the waitress over after finding something completely unacceptable hidden inside his fancy turkey salad. He demands an immediate explanation for the horrible mistake.'
OPENER = "Now let's go back through the exchange around A Belt in the Salad line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "The waitress runs to the kitchen to fetch the person responsible for this cooking disaster. Next time you watch the episode, listen for the Russian expressions for 'waiter' and 'to come up' — you will catch every word right away. See you next time!"
CLOSING = ("anya", "Пока!")
STORY = [
    ('guest', 'Официант, подойдите сюда.', 'Waiter, come here.', [], ''),
    ('vika', 'Да.', 'Yes?', [(282, 'Да')], ''),
    ('guest', 'Посмотрите в мою тарелку.', 'Look into my plate.', [], ''),
    ('vika', 'Извините, в чём проблема?', 'Excuse me, what is the problem?', [], ''),
    ('guest', 'Это что?', 'What is this?', [(283, 'Это что')], ''),
    ('vika', 'Салат из индейки.', 'Turkey salad.', [(284, 'Салат из индейки')], ''),
    ('guest', 'Вы смеётесь надо мной?', 'Are you laughing at me?', [], ''),
    ('guest', 'А индейка была в брюках и ремне?', 'Was the turkey wearing pants and a belt?', [(285, 'индейка была в брюках и ремне')], ''),
    ('vika', 'Я сейчас позову администратора.', 'I will call the manager right now.', [], ''),
    ('guest', 'Мне не нужен администратор.', 'I do not need the manager.', [], ''),
    ('guest', 'Ну-ка, давай зови сюда ущербного, который ты готовила.', 'Go get the idiot who made this.', [(286, 'зови сюда ущербного, который ты готовила')], ''),
    ('anya', 'Что здесь происходит?', 'What is happening here?', [], ''),
    ('vika', 'Гость нашёл ремень в салате.', 'The guest found a belt in the salad.', [], ''),
    ('anya', 'Я сейчас разберусь с этим.', 'I will sort this out now.', [], ''),
]
WALK = [
    (0, None, "'What is this?' Russian omits the present-tense verb 'to be' here, linking 'this' directly with 'what', combining 'this' with 'what'."),
    (1, None, "'Turkey salad.' Russian omits the present-tense verb 'to be' here, linking 'salad' directly with 'turkey', combining 'salad' with 'turkey'."),
    (2, None, "'Was the turkey wearing pants and a belt?' , combining 'turkey' with 'was' and 'trousers'."),
    (3, None, "'Go get the idiot who made this.' the guest leads with the direct command form meaning 'let's', pairing it with 'call' and 'here'. Now let's listen to the whole conversation again from start to finish."),
]
