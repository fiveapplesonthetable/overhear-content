# Authoring module for kukhnya-s01e03-scene-14.
ID = 'kukhnya-s01e03-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 14
TITLE = 'Праздничный гусь  (The Festive Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "The big birthday banquet is about to start, and Vika, the art director, is running through her checklist with Sasha, the waitress. The tables are laid, the champagne is ready, and the roast goose is on its way. Here's the Russian first."
OPENER = "Let's follow the checklist."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The banquet begins, and the goose is on its way, small as it is. You\'ve heard the phrase for "it\'s time to", which is very handy.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Саша, всё готово к праздничному банкету?', 'Sasha, is everything ready for the festive banquet?', [], ''),
    ('sasha', 'Да, гости уже сидят за столом.', 'Yes, the guests are already sitting at the table.', [], ''),
    ('vika', 'Шеф уже закончил готовить главное блюдо?', 'Has the chef already finished cooking the main dish?', [], ''),
    ('sasha', 'Повара как раз несут запечённого гуся.', 'The cooks are just now carrying the roasted goose.', [], ''),
    ('vika', 'Отлично, пора поздравлять именинницу!', 'Excellent, it is time to congratulate the birthday girl!', [(260, 'Пора поздравлять именинницу')], ''),
    ('sasha', 'Мы зажжём красивые свечи на торте?', 'Shall we light beautiful candles on the cake?', [], ''),
    ('vika', 'Да, и откройте самое дорогое шампанское.', 'Yes, and open the most expensive champagne.', [], ''),
    ('sasha', 'Судья сегодня выглядит очень счастливой.', 'The judge looks very happy today.', [], ''),
    ('vika', 'Она строгий человек, но любит внимание.', 'She is a strict person, but loves attention.', [], ''),
    ('sasha', 'Муж подарил ей великолепный букет цветов.', 'Her husband gave her a magnificent bouquet of flowers.', [], ''),
    ('vika', 'Надеюсь, наш ресторан подарит ей радость.', 'I hope our restaurant gives her joy.', [], ''),
    ('sasha', 'Все официанты готовы встречать гостей улыбкой.', 'All the waiters are ready to greet guests with a smile.', [], ''),
    ('vika', 'Тогда начинаем праздник на высшем уровне!', 'Then we begin the celebration at the highest level!', [], ''),
]
WALK = [
    (0, None, [
        "'Sasha, is everything ready for the festive banquet?' Looking closely, ",
        ('vika', 'готово к'),
        ' literally means "ready towards", and after ',
        ('vika', 'к'),
        ' the words change shape: ',
        ('vika', 'к праздничному банкету?'),
        ('vika', 'праздничному'),
        ' is built from ',
        ('vika', 'праздничному'),
        ', the word for a holiday.'
    ]),
    (1, None, [
        "'Yes, the guests are already sitting at the table.' Russians sit ",
        ('sasha', 'за столом.'),
        ' literally behind the table. ',
        ('sasha', 'сидят'),
        ' translates to "they sit".'
    ]),
    (2, None, [
        "'Has the chef already finished cooking the main dish?' Another detail, ",
        ('vika', 'закончил'),
        ', finished, is built from ',
        ('vika', 'закончил'),
        ', the word for end. ',
        ('vika', 'главное блюдо?'),
        ' translates to "main dish".'
    ]),
    (3, None, [
        "'The cooks are just now carrying the roasted goose.' Another detail, ",
        ('sasha', 'как раз'),
        ' turns up again for "right now". ',
        ('sasha', 'запечённого'),
        ' is built from ',
        ('sasha', 'запечённого'),
        ', the word for stove, so it literally means "oven-baked".'
    ]),
    (4, None, [
        "'Excellent, it is time to congratulate the birthday girl!' For this line, ",
        ('vika', 'пора'),
        ' translates to "it is time". ',
        ('vika', 'поздравлять'),
        ' is built from ',
        ('vika', 'здрав'),
        ', health, as in ',
        ('vika', 'поздравлять'),
        '. ',
        ('vika', 'именинницу!'),
        ' comes from ',
        ('vika', 'именинницу'),
        ', the word for a name day.'
    ]),
    (5, None, [
        "'Shall we light beautiful candles on the cake?' As you hear, ",
        ('sasha', 'зажжём'),
        ', we will light, is built from ',
        ('sasha', 'зажжём'),
        ', the word for to burn. ',
        ('sasha', 'свечи'),
        ' translates to candles, and ',
        ('sasha', 'на торте?'),
        ' is "on the cake".'
    ]),
    (6, None, [
        "'Yes, and open the most expensive champagne.' Pay attention to ",
        ('vika', 'откройте'),
        ', the word for open, is said to several people. For ',
        ('vika', 'шампанское.'),
        ' the words for the most expensive change shape to match: ',
        ('vika', 'самое дорогое шампанское.')
    ]),
    (7, None, [
        "'The judge looks very happy today.' After ",
        ('sasha', 'выглядит'),
        ', the word for looks, the next word changes shape for a woman: ',
        ('sasha', 'счастливой.'),
        ' It is built from ',
        ('sasha', 'счастливой'),
        ', the word for happiness.'
    ]),
    (8, None, [
        "'She is a strict person, but loves attention.' For this line, ",
        ('vika', 'человек,'),
        ' the word for person, is a guy word but covers everyone, so ',
        ('vika', 'строгий'),
        ' stays in its original shape. ',
        ('vika', 'любит внимание.'),
        ' translates to "loves attention".'
    ]),
    (9, None, [
        "'Her husband gave her a magnificent bouquet of flowers.' Let us check ",
        ('sasha', 'подарил'),
        ' is built from ',
        ('sasha', 'дар'),
        ', the word for gift, so it literally means "gave as a present". ',
        ('sasha', 'букет цветов.'),
        ' translates to "a bouquet of flowers".'
    ]),
    (10, None, [
        "'I hope our restaurant gives her joy.' What happens here, ",
        ('vika', 'радость.'),
        ' the word for joy, grows from ',
        ('vika', 'рад'),
        ', glad. ',
        ('vika', 'подарит'),
        ' is the same gift action word, which translates to "will give".'
    ]),
    (11, None, [
        "'All the waiters are ready to greet guests with a smile.' Focusing here, ",
        ('sasha', 'встречать гостей'),
        ' translates to "to greet guests", built from ',
        ('sasha', 'встреча'),
        ', the word for a meeting. ',
        ('sasha', 'улыбкой.'),
        ' literally means "with a smile".'
    ]),
    (12, None, [
        "'Then we begin the celebration at the highest level!' Check out how ",
        ('vika', 'на высшем уровне!'),
        ' literally translates to "on the highest level", a stock phrase for top quality. ',
        ('vika', 'высшем'),
        ' is the top shape of ',
        ('vika', 'высшем'),
        ', the word for high.'
    ]),
]
