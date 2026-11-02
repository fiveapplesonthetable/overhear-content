# Authoring module for kukhnya-s01e02-scene-05.
ID = 'kukhnya-s01e02-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Японский нож  (The Japanese Knife)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "While everyone searches, Nastya asks Senya why the chef can't just buy another knife. Senya explains what makes this one so special. Here is their talk in Russian first."
OPENER = "Now let's see why this knife is special."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So it\'s a very sharp, very expensive Japanese knife, and the chef has every reason to panic. Listen for the command to look for it, because it comes back.'
CLOSING = ("nastya", "Счастливо!")
STORY = [
    ('nastya', 'Почему нельзя купить такой нож?', "Why can't we buy such a knife?", [], ''),
    ('senya', 'По-быстрому такой нож купить не получится.', "You can't buy such a knife in a hurry.", [(95, 'быстрому такой нож купить не получится')], ''),
    ('nastya', 'А сколько он стоит?', 'And how much does it cost?', [], ''),
    ('senya', 'Это дорогой японский нож.', 'This is an expensive Japanese knife.', [], ''),
    ('senya', 'Шеф заказывал его очень долго.', 'The chef ordered it for a very long time.', [], ''),
    ('nastya', 'И он очень острый?', 'And is it very sharp?', [], ''),
    ('senya', 'Самый острый нож на кухне.', 'The sharpest knife in the kitchen.', [], ''),
    ('nastya', 'Где же он может быть?', 'Where could it possibly be?', [], ''),
    ('senya', 'Мы уже везде искали.', 'We already looked everywhere.', [], ''),
    ('nastya', 'Может, кто-то взял его домой?', 'Maybe someone took it home?', [], ''),
    ('senya', 'Никто не посмеет это сделать.', 'Nobody would dare do that.', [], ''),
    ('senya', 'Шеф сразу всех уволит.', 'The chef will fire everyone immediately.', [], ''),
    ('senya', 'Давай нож ищи скорее.', 'Come on, look for the knife quickly.', [(97, 'Давай нож ищи')], ''),
    ('nastya', 'Хорошо. Я посмотрю здесь.', 'All right. I will look here.', [], ''),
]
WALK = [
    (0, None, ['\'Why can\'t we buy such a knife?\' The word for "it\'s not allowed" or "it\'s impossible" is ', ('nastya', 'нельзя'), '. Put ', ('nastya', 'Почему'), ' in front and you can ask why anything can\'t be done.']),
    (1, None, ['\'You can\'t buy such a knife in a hurry.\' ', ('senya', 'По-быстрому'), ' translates to "in a quick way", built from the word for "quickly". Then ', ('senya', 'не получится.'), ', literally "it won\'t work out", which Russians say whenever something can\'t be done.']),
    (2, None, ['\'And how much does it cost?\' ', ('nastya', 'сколько он стоит?'), ' literally translates to "how much costs", the shop question. Nastya calls the knife ', ('nastya', 'он'), ', the term for "he", because the Russian language treats some objects like people.']),
    (3, None, ['\'This is an expensive Japanese knife.\' The word for expensive, ', ('senya', 'дорогой'), ', does two jobs: it also translates to "dear", as in a dear friend. And there is no "is", just ', ('senya', 'Это'), ', literally "this", and the rest.']),
    (4, None, ['\'The chef ordered it for a very long time.\' The action word ', ('senya', 'заказывал'), ', literally "ordered", is built from the term for an order. ', ('senya', 'его'), ', meaning "it", is the same word as "him" and "his", and it never changes.']),
    (5, None, ['\'And is it very sharp?\' ', ('nastya', 'острый?'), ' translates to "sharp" and also "spicy", so the describing word is good for knives and for food. Context tells you which.']),
    (6, None, ['\'The sharpest knife in the kitchen.\' Put ', ('senya', 'Самый'), ' in front of a describing word and it translates to "the most": ', ('senya', 'Самый острый'), ' literally translates to "the most sharp". It works with any describing word.']),
    (7, None, ['\'Where could it possibly be?\' The word for maybe is ', ('nastya', 'может быть?'), ', but here the two words literally translate to "can be". Adding the little word ', ('nastya', 'же'), ' after ', ('nastya', 'Где'), ' adds the "possibly".']),
    (8, None, ['\'We already looked everywhere.\' ', ('senya', 'уже'), ', the term for already, and ', ('senya', 'везде'), ', the term for everywhere, are small words you will use constantly. ', ('senya', 'искали.'), ', literally "looked for", is built from ', ('senya', 'искали.'), ', the same action word as the command below.']),
    (9, None, ['\'Maybe someone took it home?\' ', ('nastya', 'может'), ' on its own translates to "maybe". ', ('nastya', 'кто-то'), ' translates to "someone", built from the word for "who".']),
    (10, None, ['\'Nobody would dare do that.\' ', ('senya', 'Никто не'), ' literally translates to "nobody not", which is how Russians say nobody. ', ('senya', 'посмеет'), ', meaning "will dare", is built from ', ('senya', 'посмеет'), ', the term for to dare.']),
    (11, None, ['\'The chef will fire everyone immediately.\' ', ('senya', 'сразу'), ' is the term for the everyday "immediately". The word for "everyone", ', ('senya', 'всех'), ', takes a special ending because they are the ones receiving the action.']),
    (12, None, ['\'Come on, look for the knife quickly.\' ', ('senya', 'Давай'), ' translates to a friendly "come on". ', ('senya', 'ищи'), ' is the term for the command "look for", and ', ('senya', 'скорее.'), ' translates to "quicker".']),
    (13, None, ['\'All right. I will look here.\' The first part of ', ('nastya', 'посмотрю'), ', literally "I will look", gives it the sense of a quick look. The word for "here" is ', ('nastya', 'здесь.'), '.']),
]
