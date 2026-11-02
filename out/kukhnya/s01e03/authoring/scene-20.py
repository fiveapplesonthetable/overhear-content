# Authoring module for kukhnya-s01e03-scene-20.
ID = 'kukhnya-s01e03-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 20
TITLE = 'Посвящение на кухне  (Kitchen Initiation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "The kitchen team has gathered around Max for a mock knighting ceremony. The chef solemnly welcomes him to the kitchen, and then Max thinks about everything that has happened to him this week. Here's the Russian first."
OPENER = 'Now the ceremony.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max is now a proper member of the kitchen family, and this is only the beginning. Take away the word for "the main thing" for any conclusion.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, встань перед нами на колено!', 'Oguzok, kneel down on one knee before us!', [(336, 'На колено.')], ''),
    ('max', 'Шеф, что сейчас со мной будет?', 'Chef, what will happen to me now?', [(335, 'принимаем тебя на нашу кухню.')], ''),
    ('barinov', 'Мы торжественно принимаем тебя на кухню!', 'We solemnly accept you into our kitchen!', [(337, 'Отныне и вовеки веков принимаем тебя')], ''),
    ('barinov', 'Во имя горячей духовки и противня!', 'In the name of the hot oven and baking tray!', [(338, 'Во имя духовки и противня,')], ''),
    ('barinov', 'Во имя тяжёлой сковородки и половника!', 'In the name of the heavy frying pan and ladle!', [(339, 'во имя сковородки и')], ''),
    ('senya', 'Поздравляем тебя с боевым кулинарным крещением!', 'Congratulations on your culinary baptism of fire!', [(349, 'прошел этот обряд.')], ''),
    ('max', 'Шеф, вы меня даже не накажете?', 'Chef, are you not even going to punish me?', [(347, 'шеф, меня даже не накажете?')], ''),
    ('barinov', 'Разве этого обряда тебе было мало?', 'Was this ritual not enough for you?', [(348, 'А этого тебе было мало?')], ''),
    ('barinov', 'Ты первый человек, который прошёл посвящение!', 'You are the first person who passed the initiation!', [(349, 'Ты вообще первый человек, который прошел')], ''),
    ('senya', 'Надо будет всех новичков так посвящать!', 'We should initiate all future newcomers like this!', [(351, 'Надо будет всех так посвящать.')], ''),
    ('max', 'Жизнь полна разных потерь и приобретений.', 'Life is full of various losses and gains.', [(341, 'Жизнь – это череда потерь и приобретений.')], ''),
    ('max', 'Одни люди грустят, другие всегда радуются.', 'Some people grieve, while others always rejoice.', [(342, 'Кто-то грустит о потерях,')], ''),
    ('max', 'Но настоящие друзья всегда помогают в беде.', 'But true friends always help in trouble.', [(344, 'Есть те, кто приобретают')], ''),
    ('max', 'Главное понимать, что это только начало!', 'The main thing is to understand that this is only the beginning!', [(354, 'главное понимать, что это только начало.')], ''),
]
WALK = [
    (0, None, [
        "'Oguzok, kneel down on one knee before us!' Getting down on one knee translates to ",
        ('barinov', 'на колено!'),
        ', and ',
        ('barinov', 'встань'),
        ' is the action word to stand up. The phrase for in front of us is ',
        ('barinov', 'перед нами'),
        ' where the word for we takes a special shape after ',
        ('barinov', 'перед'),
        '.'
    ]),
    (1, None, [
        "'Chef, what will happen to me now?' This literally translates to what will be with me, using ",
        ('max', 'что сейчас со мной будет?'),
        ' The word for with, which is usually just s, turns into ',
        ('max', 'со'),
        ' before ',
        ('max', 'мной'),
        '.'
    ]),
    (2, None, [
        "'We solemnly accept you into our kitchen!' The word for solemnly, ",
        ('barinov', 'торжественно'),
        ', is built from the word for a celebration. We accept translates to ',
        ('barinov', 'принимаем'),
        ', and onto the kitchen is ',
        ('barinov', 'на кухню!'),
        '.'
    ]),
    (3, None, [
        "'In the name of the hot oven and baking tray!' The phrase ",
        ('barinov', 'Во имя'),
        ' translates to in the name, which is an old solemn phrase. After it, the words for the hot oven and baking tray, ',
        ('barinov', 'горячей духовки и противня!'),
        ', all take a special ending.'
    ]),
    (4, None, [
        "'In the name of the heavy frying pan and ladle!' The phrase for the heavy frying pan, ",
        ('barinov', 'тяжёлой сковородки'),
        ', takes the matching endings. The word for ladle also changes its shape to ',
        ('barinov', 'половника!'),
        '.'
    ]),
    (5, None, [
        "'Congratulations on your culinary baptism of fire!' Russian literally uses a battle baptism, seen in ",
        ('senya', 'боевым'),
        ' and ',
        ('senya', 'крещением!'),
        ', for a first test. The phrase translates to we congratulate with using ',
        ('senya', 'Поздравляем'),
        ' and ',
        ('senya', 'с'),
        ', which is the frame for any congratulations.'
    ]),
    (6, None, [
        "'Chef, are you not even going to punish me?' The phrase for not even is ",
        ('max', 'даже не'),
        '. The word for you will punish translates to ',
        ('max', 'накажете?'),
        ', which is a future action word with a polite shape.'
    ]),
    (7, None, [
        "'Was this ritual not enough for you?' The word ",
        ('barinov', 'Разве'),
        ' opens a question that expects a no. The phrase ',
        ('barinov', 'тебе было мало?'),
        ' literally translates to to you it was little, meaning it was not enough for you.'
    ]),
    (8, None, [
        "'You are the first person who passed the initiation!' The word for who, ",
        ('barinov', 'который'),
        ', ties the halves together. The action word for passed, ',
        ('barinov', 'прошёл'),
        ', is built from go and through, so it literally translates to went through.'
    ]),
    (9, None, [
        "'We should initiate all future newcomers like this!' The phrase for it will be necessary translates to ",
        ('senya', 'Надо будет'),
        '. The word for newcomers, ',
        ('senya', 'новичков'),
        ', is built from the word for new and changes its shape here.'
    ]),
    (10, None, [
        "'Life is full of various losses and gains.' The word for full, ",
        ('max', 'полна'),
        ', has a matching ending for life. After it come the shapes for more than one loss and gain, seen in ',
        ('max', 'потерь'),
        ' and ',
        ('max', 'приобретений.')
    ]),
    (11, None, [
        "'Some people grieve, while others always rejoice.' The phrase for some and others translates to ",
        ('max', 'Одни'),
        ' and ',
        ('max', 'другие'),
        '. The action word for they grieve, ',
        ('max', 'грустят,'),
        ' is built from sadness, and they rejoice, ',
        ('max', 'радуются.'),
        ', is built from joy.'
    ]),
    (12, None, [
        "'But true friends always help in trouble.' The word for friend has a special shape for more than one, translating to ",
        ('max', 'друзья'),
        '. The phrase for in trouble is ',
        ('max', 'в беде.')
    ]),
    (13, None, [
        "'The main thing is to understand that this is only the beginning!' The word ",
        ('max', 'Главное'),
        ' on its own translates to the main thing. The word for beginning, ',
        ('max', 'начало!'),
        ', is built from the action word to begin.'
    ]),
]
