# Authoring module for kukhnya-s01e02-scene-06.
ID = 'kukhnya-s01e02-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'Новый бармен  (The New Bartender)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Max has agreed to help out behind the bar, and he is quietly amazed by the cash register. Then Nastya comes in to order two espressos, and is very surprised to see a cook behind the counter. Here is their exchange in Russian first.'
OPENER = 'Now the exchange again, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max is a cook who says he\'s a bartender at heart, and nobody believes him. At least you\'ve learned "I thought" and "right away".'
CLOSING = ("nastya", "Счастливо!")
STORY = [
    ('max', 'Так вот как выглядит эта система.', 'So this is what this system looks like.', [], ''),
    ('max', 'Я думал, это просто касса.', 'I thought it was just a cash register.', [(100, 'Я думал, это касса')], ''),
    ('nastya', 'Сделай два эспрессо, пожалуйста.', 'Make two espressos, please.', [(101, 'два эспрессо сделай, пожалуйста')], ''),
    ('nastya', 'Что ты тут делаешь?', 'What are you doing here?', [(102, 'что ты тут делаешь')], ''),
    ('max', 'А я теперь новый бармен.', 'And I am now the new bartender.', [(102, 'А я новый бармен')], ''),
    ('nastya', 'Да ладно тебе выдумывать.', 'Oh, stop making things up.', [(104, 'Да ладно')], ''),
    ('nastya', 'Я тебя на кухне видела.', 'I saw you in the kitchen.', [(104, 'Я тебя на кухне видела')], ''),
    ('nastya', 'Ты же повар.', 'You are a cook after all.', [(105, 'Ты повар')], ''),
    ('max', 'У меня очень много талантов.', 'I have very many talents.', [(105, 'А у меня много талантов')], ''),
    ('max', 'А в душе я бармен.', 'And at heart I am a bartender.', [(105, 'в душе я бармен')], ''),
    ('nastya', 'Костя уже починил аппарат?', 'Did Kostya already fix the machine?', [], ''),
    ('max', 'Конечно, всё прекрасно работает.', 'Of course, everything works wonderfully.', [], ''),
    ('nastya', 'Тогда быстрее вари кофе.', 'Then make coffee faster.', [(107, 'сделай два эспрессо, пожалуйста')], ''),
    ('max', 'Сию секунду. Всё будет готово.', 'Right away. Everything will be ready.', [], ''),
]
WALK = [
    (0, None, [
        '\'So this is what this system looks like.\' ',
        ('max', 'Так вот'),
        ' is a pair of little words for "so here is". Inside the action word for "looks", ',
        ('max', 'выглядит'),
        ', you\'ll recognise the term for "to look".'
    ]),
    (1, None, [
        '\'I thought it was just a cash register.\' ',
        ('max', 'Я думал,'),
        ' translates to "I thought", and Russian leaves out "it was", so it is literally "I thought, this just a till". The word for the cash register, and the till in any shop, is ',
        ('max', 'касса.'),
        '.'
    ]),
    (2, None, [
        '\'Make two espressos, please.\' The friendly word for "make" is ',
        ('nastya', 'Сделай'),
        '. The word espresso doesn\'t change after ',
        ('nastya', 'два'),
        ', which translates to two, because borrowed words ending in the "o" sound never change. The describing word ',
        ('nastya', 'пожалуйста.'),
        ' does the work of "please".'
    ]),
    (3, None, [
        '\'What are you doing here?\' Nastya says ',
        ('nastya', 'тут'),
        ', the casual word for "here", which is shorter than other ways to say it. She\'s using the friendly "you" with Max.'
    ]),
    (4, None, [
        '\'And I am now the new bartender.\' A cheeky ',
        ('max', 'А я'),
        ', which translates to "and I", begins it. The word for "now", in the sense of "from now on", is ',
        ('max', 'теперь'),
        ', and the describing word for "new" is ',
        ('max', 'новый'),
        '.'
    ]),
    (5, None, [
        '\'Oh, stop making things up.\' The phrase ',
        ('nastya', 'Да ладно тебе'),
        ' translates to "oh, come on". The action word for "to make up", ',
        ('nastya', 'выдумывать.'),
        ', is built from the action word for "to think": you think something out of nothing.'
    ]),
    (6, None, [
        '\'I saw you in the kitchen.\' The ending on the action word for "saw", ',
        ('nastya', 'видела.'),
        ', shows Nastya is a woman. And Russian always says ',
        ('nastya', 'на кухне'),
        ', which translates to "on the kitchen", where English says "in".'
    ]),
    (7, None, [
        '\'You are a cook after all.\' The phrase ',
        ('nastya', 'Ты же повар.'),
        ' literally has no "are", just "you cook". The little word ',
        ('nastya', 'же'),
        ' brings in "after all".'
    ]),
    (8, None, [
        '\'I have very many talents.\' The phrase ',
        ('max', 'У меня'),
        ' literally means "at me", and is the "I have" pattern. After the term for many, ',
        ('max', 'много'),
        ', the term for talent takes a special ending.'
    ]),
    (9, None, [
        '\'And at heart I am a bartender.\' The phrase ',
        ('max', 'в душе'),
        ' translates to "in the soul", built from the term for soul. Russians use it like English "deep down".'
    ]),
    (10, None, [
        '\'Did Kostya already fix the machine?\' The action word for "fixed" is ',
        ('nastya', 'починил'),
        '. The word for any machine or gadget is ',
        ('nastya', 'аппарат?'),
        ', and here it means the coffee machine.'
    ]),
    (11, None, [
        '\'Of course, everything works wonderfully.\' It\'s spelled with a "ch" sound but said differently. And the term for "everything" is ',
        ('max', 'всё'),
        '.'
    ]),
    (12, None, [
        '\'Then make coffee faster.\' Russians boil coffee, so the command is the action word ',
        ('nastya', 'вари'),
        ', which translates to "boil". The describing word for "faster" is ',
        ('nastya', 'быстрее'),
        '.'
    ]),
    (13, None, [
        '\'Right away. Everything will be ready.\' The phrase ',
        ('max', 'Сию секунду.'),
        ' is an old-fashioned "this very second", what a waiter says. The describing word for "ready" is ',
        ('max', 'готово.'),
        ', ending in a certain sound to agree with the term for everything.'
    ]),
]
