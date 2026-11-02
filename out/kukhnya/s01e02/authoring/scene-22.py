# Authoring module for kukhnya-s01e02-scene-22.
ID = 'kukhnya-s01e02-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = 'Ищите везде  (Look Everywhere)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "The chef is in a terrible mood, and he is stomping round the kitchen picking at things. A dirty box is in the wrong place, and he still hasn't found his knife. Lyova, his sous-chef, has to answer for it. Here is the exchange in Russian first."
OPENER = "Now the chef's questions again."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Lyova hurries off to keep looking, and he has no idea where the knife actually is. You have heard the command for a group to look!'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ты почему тут поставил грязную коробку?', 'Why did you put a dirty box here?', [(235, 'коробку грязную поставил')], ''),
    ('barinov', 'Убери её отсюда очень быстро!', 'Remove it from here very quickly!', [(236, 'Убери давай быстро.')], ''),
    ('barinov', 'Лёва, вы уже нашли мой нож?', 'Lyova, have you already found my knife?', [(237, 'Лёва, нож нашли?')], ''),
    ('lyova', 'Мы ещё не нашли его, шеф.', 'We have not found it yet, Chef.', [(238, 'Ещё нет, шеф.')], ''),
    ('barinov', 'Вы точно везде хорошо искали?', 'Did you definitely look well everywhere?', [(238, 'Везде смотрели?')], ''),
    ('lyova', 'Да, мы всё проверили на кухне.', 'Yes, we checked everything in the kitchen.', [(239, 'Везде.')], ''),
    ('barinov', 'Значит, продолжайте искать дальше!', 'Then continue to look further!', [(239, 'Ну ищите.')], ''),
    ('barinov', 'Кто-то мог случайно оставить нож внутри.', 'Someone could have accidentally left the knife inside.', [(240, 'оставил там нож')], ''),
    ('barinov', 'Например, кто-то забыл нож в рыбе.', 'For example, someone forgot the knife in the fish.', [(241, 'Ну, в рыбе, например.')], ''),
    ('lyova', 'В рыбе? Это невозможно, шеф!', 'In the fish? That is impossible, Chef!', [(242, 'В рыбе?')], ''),
    ('barinov', 'Я не знаю. Ищите везде!', 'I do not know. Look everywhere!', [(243, 'Ищите везде.')], ''),
    ('lyova', 'Хорошо, шеф, мы всё найдём.', 'Alright, Chef, we will find everything.', [(244, 'Да, шеф.')], ''),
    ('barinov', 'Без ножа мы не сможем работать!', 'Without the knife we will not be able to work!', [], ''),
]
WALK = [
    (0, None, [
        '\'Why did you put a dirty box here?\' The word for put is ',
        ('barinov', 'поставил'),
        ' which literally means "made stand", so a box is stood somewhere. The describing words for dirty box change to ',
        ('barinov', 'грязную коробку?'),
        ' because it is the thing being put.'
    ]),
    (1, None, [
        '\'Remove it from here very quickly!\' The word for it translates to the "her" word, ',
        ('barinov', 'её'),
        ' because the word for box is a girl word. The action word for remove is the friendly take away, ',
        ('barinov', 'Убери')
    ]),
    (2, None, [
        '\'Lyova, have you already found my knife?\' The chef uses the word for you all, ',
        ('barinov', 'вы'),
        ' referring to the whole kitchen team. The action word for found translates to ',
        ('barinov', 'нашли'),
        ' ending in a group sound.'
    ]),
    (3, None, [
        '\'We have not found it yet, Chef.\' The phrase for not yet is literally built from still not, ',
        ('lyova', 'ещё не'),
        ' The little word for it, ',
        ('lyova', 'его,'),
        ' never changes.'
    ]),
    (4, None, [
        '\'Did you definitely look well everywhere?\' The chef asks the whole team again, so the action word for looked, ',
        ('barinov', 'искали?'),
        ' ends in a group sound to match. The word for definitely translates to for sure here: ',
        ('barinov', 'точно')
    ]),
    (5, None, [
        '\'Yes, we checked everything in the kitchen.\' The action word for checked, ',
        ('lyova', 'проверили'),
        ' ends in a group sound for "we". The word for everything is ',
        ('lyova', 'всё')
    ]),
    (6, None, [
        '\'Then continue to look further!\' The word for then is literally it means, ',
        ('barinov', 'Значит,'),
        ' The action word for continue is keep on, ',
        ('barinov', 'продолжайте'),
        ' and the word for further is ',
        ('barinov', 'дальше!')
    ]),
    (7, None, [
        '\'Someone could have accidentally left the knife inside.\' The word for could is ',
        ('barinov', 'мог'),
        ' The word for accidentally translates to by accident, ',
        ('barinov', 'случайно'),
        ' built from a chance. And the word for inside is ',
        ('barinov', 'внутри.')
    ]),
    (8, None, [
        '\'For example, someone forgot the knife in the fish.\' The phrase for for example literally translates to on example, ',
        ('barinov', 'Например,'),
        ' The action word for forgot is ',
        ('barinov', 'забыл'),
        ' and placing it in the fish puts a changing sound on the end of fish, ',
        ('barinov', 'в рыбе.')
    ]),
    (9, None, [
        '\'In the fish? That is impossible, Chef!\' Lyova repeats in the fish as a question. The word for impossible is built from not plus possible, ',
        ('lyova', 'невозможно,')
    ]),
    (10, None, [
        '\'I do not know. Look everywhere!\' The action word for look is ',
        ('barinov', 'Ищите'),
        ' spoken to a group. The word for everywhere is ',
        ('barinov', 'везде'),
        ' exactly what Lyova said.'
    ]),
    (11, None, [
        '\'Alright, Chef, we will find everything.\' The action word for we will find is ',
        ('lyova', 'найдём.'),
        ' The word for everything translates to ',
        ('lyova', 'всё')
    ]),
    (12, None, [
        '\'Without the knife we will not be able to work!\' Saying without the knife, ',
        ('barinov', 'Без ножа'),
        ' makes the word for knife change its ending. The phrase for will not be able translates to ',
        ('barinov', 'не сможем')
    ]),
]
