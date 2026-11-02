# Authoring module for kukhnya-s01e03-scene-10.
ID = 'kukhnya-s01e03-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 10
TITLE = 'История про гуся  (The Story of the Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Max has quietly swapped the live goose for a ready-plucked one from the market, and now he has to explain to Barinov why his apron is spotless. He tells the chef a story that is more dramatic than the truth. Here is the Russian first.'
OPENER = 'Now the lie, line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max has saved the goose, and he has also saved his job. Remember "not a drop", which is how they say "not even a bit".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок! Где мой свежий гусь?', 'Oguzok! Where is my fresh goose?', [(235, 'Где гусь')], ''),
    ('max', 'Я только что прикончил его!', 'I have just finished it off!', [(236, 'Я его только что прикончил')], ''),
    ('barinov', 'Почему ты такой подозрительно чистый?', 'Why are you so suspiciously clean?', [(237, 'А что ты такой чистенький')], ''),
    ('barinov', 'На тебе нет ни капли крови!', 'There is not a drop of blood on you!', [(237, 'ни капельки крови на тебя не попало')], ''),
    ('max', 'Я его совсем не резал.', 'I did not cut it at all.', [(238, 'Я его не зарезал')], ''),
    ('barinov', 'И как ты его убил?', 'And how did you kill it?', [], ''),
    ('max', 'Шеф, я его просто задушил!', 'Chef, I simply strangled it!', [(239, 'Я его задушил')], ''),
    ('barinov', 'Какой кошмар! Настоящий Отелло на кухне!', 'What a nightmare! A real Othello in the kitchen!', [(240, 'Какой ужас'), (240, 'Ладно, Отелло')], ''),
    ('barinov', 'Тащи свою птицу су-шефу на стол!', "Drag your bird to the sous-chef's table!", [(240, 'тащи свою дездемону с ушефу')], ''),
    ('barinov', 'Лёва, начинай быстро готовить гуся!', 'Lyova, start preparing the goose quickly!', [(241, 'Лёва, начинай готовить гуся')], ''),
    ('lyova', 'Понял, шеф, я включаю духовку.', 'Understood, Chef, I am turning on the oven.', [(242, 'Понял, шеф')], ''),
    ('barinov', 'А я займусь важным комплиментом.', 'And I will take care of an important compliment.', [(243, 'А я займусь комплиментом от шефа')], ''),
    ('max', 'Я спас птицу и свою работу.', 'I saved the bird and my job.', [], ''),
]
WALK = [
    (0, None, [
        "'Oguzok! Where is my fresh goose?' Barinov opens with the nickname. ",
        ('barinov', 'Где'),
        ' is the word for "where", and ',
        ('barinov', 'свежий'),
        ' is the word for "fresh".'
    ]),
    (1, None, [
        "'I have just finished it off!' Another detail, ",
        ('max', 'прикончил'),
        ' is built from the word for "end", so it means "brought to an end". ',
        ('max', 'только что'),
        ' literally means "only what", but translates to "just now".'
    ]),
    (2, None, [
        "'Why are you so suspiciously clean?' Take note of ",
        ('barinov', 'подозрительно'),
        ' is built from the word for "suspicious", changing the ending to make it a how-word. The word for "clean" is ',
        ('barinov', 'чистый?')
    ]),
    (3, None, [
        "'There is not a drop of blood on you!' You will hear ",
        ('barinov', 'ни'),
        ' translates to "not even". The words for "drop" and "blood" both take the "of" shape.'
    ]),
    (4, None, [
        "'I did not cut it at all.' In this sentence, ",
        ('max', 'совсем не'),
        ' translates to "not at all". And the action word for "cut", ending with an "l" sound for a man, is ',
        ('max', 'резал.')
    ]),
    (5, None, [
        "'And how did you kill it?' Another detail, ",
        ('barinov', 'как'),
        ' translates to "how". And built from the same action word we saw in the goose scene is the word for "killed", ',
        ('barinov', 'убил?')
    ]),
    (6, None, [
        "'Chef, I simply strangled it!' Pay attention to ",
        ('max', 'просто'),
        ' translates to "simply". And built from the word for "to choke", adding a starting sound that means bringing it to an end, is the word for "strangled", ',
        ('max', 'задушил!')
    ]),
    (7, None, [
        "'What a nightmare! A real Othello in the kitchen!' The chef is joking because in Shakespeare his wife is strangled by ",
        ('barinov', 'Отелло'),
        '. The phrase for "what a nightmare!" translates to ',
        ('barinov', 'Какой кошмар!')
    ]),
    (8, None, [
        "'Drag your bird to the sous-chef's table!' ",
        ('barinov', 'Тащи'),
        ' is the word for "drag", said of anything heavy. ',
        ('barinov', 'су-шефу'),
        ' translates to "to the sous-chef", taking a "to" ending, and ',
        ('barinov', 'свою птицу'),
        ' translates to "your own bird".'
    ]),
    (9, None, [
        "'Lyova, start preparing the goose quickly!' Let us check ",
        ('barinov', 'начинай'),
        ' is an informal order meaning "start". Changing the ending on the bird, "to cook the goose" translates to ',
        ('barinov', 'готовить гуся!')
    ]),
    (10, None, [
        "'Understood, Chef, I am turning on the oven.' Take note of ",
        ('lyova', 'включаю'),
        ', the word for "I switch on", also translates to "I include", and it works for any switch. Built from the word for "hot air" is the word for oven, ',
        ('lyova', 'духовку.')
    ]),
    (11, None, [
        "'And I will take care of an important compliment.' Take note of ",
        ('barinov', 'займусь'),
        ' translates to "I\'ll take care of". What you take care of changes its shape, so the free little dish becomes an "important compliment", or ',
        ('barinov', 'важным комплиментом.')
    ]),
    (12, None, [
        "'I saved the bird and my job.' You will hear ",
        ('max', 'спас'),
        ', the word for "saved", is related to the word for "thank you", which literally means "may God save you". "My own job" translates to ',
        ('max', 'свою работу.')
    ]),
]
