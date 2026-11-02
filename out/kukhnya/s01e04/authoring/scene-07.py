# Authoring module for kukhnya-s01e04-scene-07.
ID = 'kukhnya-s01e04-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Костя влюбился  (Kostya Is in Love)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Max notices that Kostya keeps staring at Nastya, and he decides to help. He teases his friend until Kostya admits he likes her, and then pushes him into giving her a compliment. Here's the Russian first."
OPENER = "Let's go through the matchmaking."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya gets a compliment back, and a lot more confidence than before. Remember the phrase meaning "I like her", which literally translates to "she is pleasing to me".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, посмотри на Настю.', 'Kostya, look at Nastya.', [(59, 'Костян, смотри')], ''),
    ('kostya', 'Она очень красивая девушка.', 'She is a very pretty girl.', [(61, 'Красивое')], ''),
    ('max', 'Она тебе нравится? Признайся честно!', 'Do you like her? Admit it honestly!', [(62, 'Она чё, тебе нравится')], ''),
    ('kostya', 'Ну ладно, она мне очень нравится.', 'Well all right, I like her very much.', [(64, 'Костян втюрился')], ''),
    ('max', 'Тогда скажи ей приятный комплимент.', 'Then give her a nice compliment.', [(68, 'хочет сказать')], ''),
    ('kostya', 'Я боюсь, я не умею говорить.', 'I am afraid, I cannot talk smoothly.', [(67, 'Зачем')], ''),
    ('nastya', 'Привет, мальчики! О чём вы говорите?', 'Hi, boys! What are you talking about?', [(69, 'Чё надо')], ''),
    ('max', 'Костя хочет сказать тебе важные слова.', 'Kostya wants to tell you important words.', [(68, 'Тебе тут Костян что-то хочет сказать')], ''),
    ('kostya', 'Настя, у тебя очень красивая причёска!', 'Nastya, you have a very pretty hairstyle!', [(71, 'очень красивая')], ''),
    ('nastya', 'Спасибо, Костя! Ты очень милый парень.', 'Thank you, Kostya! You are a very sweet guy.', [], ''),
    ('kostya', 'Ты слышал? Она назвала меня милым!', 'Did you hear? She called me sweet!', [], ''),
    ('max', 'Видишь? Главное — всегда быть смелым!', 'See? The main thing is to always be brave!', [(74, 'будь смелее')], ''),
]
WALK = [
    (0, None, [
        "'Kostya, look at Nastya.' ",
        ('max', 'посмотри на'),
        ' translates to "look at", and the name changes to ',
        ('max', 'Настю.'),
        ' as the one looked at.'
    ]),
    (1, None, [
        "'She is a very pretty girl.' The expression for a girl or young woman is ",
        ('kostya', 'девушка.'),
        ' And ',
        ('kostya', 'Она очень красивая девушка.'),
        ' translates to "She is a very pretty girl", needing no little word for "is".'
    ]),
    (2, None, [
        "'Do you like her? Admit it honestly!' ",
        ('max', 'Она тебе нравится?'),
        ' literally means "she to you is pleasing". The phrase for admit, ',
        ('max', 'Признайся'),
        ' carries a little ending that means confess yourself.'
    ]),
    (3, None, [
        "'Well all right, I like her very much.' ",
        ('kostya', 'Ну ладно,'),
        ' translates to "well, fine". In ',
        ('kostya', 'она мне очень нравится.'),
        ' the girl does the pleasing, and the one who likes her is ',
        ('kostya', 'мне'),
        ' literally "to me".'
    ]),
    (4, None, [
        "'Then give her a nice compliment.' The speaker literally says ",
        ('max', 'скажи ей приятный комплимент.'),
        ' say her a nice compliment. The translation for "to her" is ',
        ('max', 'ей')
    ]),
    (5, None, [
        "'I am afraid, I cannot talk smoothly.' ",
        ('kostya', 'боюсь,'),
        ' translates to "I fear". The expression ',
        ('kostya', 'не умею'),
        ' translates to "I don\'t know how", referring to a skill you lack.'
    ]),
    (6, None, [
        "'Hi, boys! What are you talking about?' ",
        ('nastya', 'Привет,'),
        ' translates to a casual "hi". ',
        ('nastya', 'мальчики!'),
        ', built from the Russian term for boy. And ',
        ' And ',
        ('nastya', 'О чём'),
        ' translates to "about what".'
    ]),
    (7, None, [
        "'Kostya wants to tell you important words.' ",
        ('max', 'важные слова.'),
        ' translates to "important words", with matching endings on the describing word and the multiple things. The Russian expression for "to you" is ',
        ('max', 'тебе')
    ]),
    (8, None, [
        "'Nastya, you have a very pretty hairstyle!' ",
        ('kostya', 'у тебя'),
        ' literally "at you", is the way to say "you have". The expression for hairstyle, ',
        ('kostya', 'причёска!'),
        ' is built from an action word meaning "to comb".'
    ]),
    (9, None, [
        "'Thank you, Kostya! You are a very sweet guy.' ",
        ('nastya', 'милый'),
        ' translates to "sweet" or "nice". The Russian expression for "guy" is ',
        ('nastya', 'парень.')
    ]),
    (10, None, [
        "'Did you hear? She called me sweet!' The action word ",
        ('kostya', 'назвала'),
        ' translates to "called", ending in an "a" sound for a woman. When naming someone this way, the describing word gets a special ending, turning into ',
        ('kostya', 'милым!')
    ]),
    (11, None, [
        "'See? The main thing is to always be brave!' ",
        ('max', 'Видишь?'),
        ' translates to "you see?". After the Russian expression for "be", ',
        ('max', 'быть'),
        ' the term for brave changes to ',
        ('max', 'смелым!')
    ]),
]
