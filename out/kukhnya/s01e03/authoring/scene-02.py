# Authoring module for kukhnya-s01e03-scene-02.
ID = 'kukhnya-s01e03-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'Обед персонала  (Staff Lunch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Staff lunch in the back room. Nastya, the waitress, turns down the meat cutlets, and Ainura, who cleans the kitchen, wants to know why. Nastya explains that she is a vegetarian, and Ainura has a story about hard times. Here is the talk in Russian first.'
OPENER = "Now let's go through the lunch table."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nastya doesn\'t touch the cutlets, and Ainura has nothing to say to a cow\'s right to life. If you remember anything, remember how to say "because".'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('ainura', 'Настя, почему ты не кушаешь мясо?', 'Nastya, why do you not eat meat?', [(83, 'А почему ты мясо не кушаешь, Тян')], ''),
    ('nastya', 'Потому что я строгая вегетарианка.', 'Because I am a strict vegetarian.', [(84, 'А я вегетарианка')], ''),
    ('ainura', 'Да ты что? А я думала, ты русская.', 'Really? And here I thought you were Russian.', [(85, 'Да ты что, вегетарианка'), (86, 'А это, думала, ты русская')], ''),
    ('nastya', 'Вегетарианцы — это люди, которые не едят мясо.', 'Vegetarians are people who do not eat meat.', [(87, 'Вегетарианцы – это люди, которые мясо не едят')], ''),
    ('ainura', 'Раньше я тоже была вегетарианкой.', 'I used to be a vegetarian too.', [(88, 'Раньше я тоже была вегетариантой')], ''),
    ('nastya', 'Правда? Когда вы не ели мясо?', 'Really? When did you not eat meat?', [], ''),
    ('ainura', 'В девяностые годы совсем не было денег.', 'In the nineties there was no money at all.', [(88, 'в 90-е годы'), (89, 'Денег не было')], ''),
    ('ainura', 'Я целый год ела только картошку.', 'I ate only potatoes for a whole year.', [(89, 'одну картошку ела')], ''),
    ('nastya', 'Я считаю недопустимым убивать животных.', 'I consider killing animals unacceptable.', [(91, 'считаю недопустимым убивать животных')], ''),
    ('ainura', 'Но сочные мясные котлеты такие вкусные!', 'But juicy meat cutlets are so tasty!', [(94, 'вот таких вот сочных')], ''),
    ('nastya', 'Каждая коровка имеет право на жизнь.', 'Every cow has the right to life.', [(92, 'была милая коровка')], ''),
    ('ainura', 'Ой, бай! Ты так красиво рассказываешь!', 'Oh my! You tell stories so beautifully!', [(96, 'Ой, бай! Ты так вкусно рассказываешь')], ''),
    ('nastya', 'Надеюсь, вы меня наконец поняли.', 'I hope you finally understood me.', [], ''),
]
WALK = [
    (0, None, [
        "'Nastya, why do you not eat meat?' Ainura uses ",
        ('ainura', 'кушаешь'),
        ', a soft, homely action word for eating, often used with children. The word for meat is ',
        ('ainura', 'мясо?')
    ]),
    (1, None, [
        "'Because I am a strict vegetarian.' The phrase for because, ",
        ('nastya', 'Потому'),
        ('nastya', 'что'),
        ', answers why. In the word for vegetarian, ',
        ('nastya', 'вегетарианка.'),
        ', the ending marks a woman.'
    ]),
    (2, None, [
        "'Really? And here I thought you were Russian.' The phrase ",
        ('ainura', 'Да'),
        ('ainura', 'ты'),
        ('ainura', 'что?'),
        ' is a very Russian "you don\'t say!", literally "yes, you what?". The action word for thought, ',
        ('ainura', 'думала,'),
        ', ends that way because Ainura is a woman.'
    ]),
    (3, None, [
        "'Vegetarians are people who do not eat meat.' The word for people is ",
        ('nastya', 'люди,'),
        ' a shape for more than one person. The word for who is ',
        ('nastya', 'которые'),
        ', and ',
        ('nastya', 'не'),
        ('nastya', 'едят'),
        ' translates to "do not eat".'
    ]),
    (4, None, [
        "'I used to be a vegetarian too.' The word for earlier, ",
        ('ainura', 'Раньше'),
        ', gives you "used to". After the word for was, ',
        ('ainura', 'была'),
        ', the word changes to ',
        ('ainura', 'вегетарианкой.'),
        ' because of how it connects in the sentence.'
    ]),
    (5, None, [
        "'Really? When did you not eat meat?' Nastya uses the respectful word for you, ",
        ('nastya', 'вы'),
        ', to the older Ainura. The word for when is ',
        ('nastya', 'Когда'),
        ', and the action word for ate, ',
        ('nastya', 'ели'),
        ', has an ending that matches the respectful you.'
    ]),
    (6, None, [
        "'In the nineties there was no money at all.' The phrase for in the nineties, ",
        ('ainura', 'В'),
        ('ainura', 'девяностые'),
        ('ainura', 'годы'),
        ', translates to "in the ninetieth years". The phrase for there was no money is ',
        ('ainura', 'не'),
        ('ainura', 'было'),
        ('ainura', 'денег.'),
        ', literally "there was not of money".'
    ]),
    (7, None, [
        "'I ate only potatoes for a whole year.' The phrase for a whole year is ",
        ('ainura', 'целый'),
        ('ainura', 'год'),
        '. Russian uses a shape for just one when talking about potatoes as food, so it is ',
        ('ainura', 'картошку.'),
        ' here.'
    ]),
    (8, None, [
        "'I consider killing animals unacceptable.' The word for animals, ",
        ('nastya', 'животных.'),
        ', is built from the idea of being alive. The word for unacceptable, ',
        ('nastya', 'недопустимым'),
        ', changes its ending to match the action word for I consider, ',
        ('nastya', 'считаю'),
        '.'
    ]),
    (9, None, [
        "'But juicy meat cutlets are so tasty!' The word for juicy, ",
        ('ainura', 'сочные'),
        ', is built from the word for juice, and the word for meaty, ',
        ('ainura', 'мясные'),
        ', is built from meat. The phrase for so tasty, ',
        ('ainura', 'такие'),
        ('ainura', 'вкусные!'),
        ', uses a shape for more than one to match cutlets.'
    ]),
    (10, None, [
        "'Every cow has the right to life.' The word for cow, ",
        ('nastya', 'коровка'),
        ', makes the animal sound small and dear. The phrase for has the right to life translates to ',
        ('nastya', 'имеет'),
        ('nastya', 'право'),
        ('nastya', 'на'),
        ('nastya', 'жизнь.'),
        ', using a formal word for having.'
    ]),
    (11, None, [
        "'Oh my! You tell stories so beautifully!' The phrase ",
        ('ainura', 'Ой,'),
        ('ainura', 'бай!'),
        " is a cry of surprise from Ainura's homeland. The word for beautifully is ",
        ('ainura', 'красиво'),
        ', and the action word for you tell is ',
        ('ainura', 'рассказываешь!')
    ]),
    (12, None, [
        "'I hope you finally understood me.' The respectful you, ",
        ('nastya', 'вы'),
        ', matches the ending on the action word for understood, ',
        ('nastya', 'поняли.'),
        ' The word for I hope, ',
        ('nastya', 'Надеюсь,'),
        ', is one word, and it ends with a short sound to flow better.'
    ]),
]
