# Authoring module for kukhnya-s01e03-scene-03.
ID = 'kukhnya-s01e03-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = 'Поиски киллера  (Looking for a Hitman)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'Out in the backyard, Max and Kostya, the bartender, are staring at the goose. Neither of them can bring themselves to kill it, and a few silly ideas fail. Desperate, Max goes to Ainura and asks for help. Here is the conversation in Russian first.'
OPENER = "Let's go through the dilemma."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'A thousand rubles, no questions asked: Ainura has a way of solving problems. You\'ve heard the phrase for "I can\'t", and the word for "agreed".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я не могу убить этого гуся.', 'I cannot kill this goose.', [(116, 'Не могу я')], ''),
    ('kostya', 'Может, ты попробуешь ещё раз?', 'Maybe you will try once more?', [(116, 'Может, ты')], ''),
    ('max', 'Нет, я точно не смогу это сделать.', 'No, I definitely cannot do this.', [(116, 'Нет, я точно не смогу')], ''),
    ('kostya', 'Давай резко напугаем его в темноте!', 'Let us suddenly scare him in the dark!', [(122, 'Давай напугаем его')], ''),
    ('max', 'Костя, это какой-то полный бред.', 'Kostya, this is complete nonsense.', [(117, 'ну это какой-то бред')], ''),
    ('kostya', 'У птиц очень слабое сердце.', 'Birds have a very weak heart.', [(121, 'слабая сердечно-сосудистая система')], ''),
    ('max', 'Видишь, он стоит и громко шипит.', 'See, he is standing and hissing loudly.', [], ''),
    ('max', 'Мне срочно нужен настоящий специалист.', 'I urgently need a real specialist.', [(127, 'Мне нужен киллер, профессионал')], ''),
    ('max', 'Айнура, помоги нам решить проблему!', 'Ainura, help us solve the problem!', [(129, 'помоги гуся убить')], ''),
    ('ainura', 'Что нужно сделать с этой птицей?', 'What needs to be done with this bird?', [], ''),
    ('max', 'Нужно быстро и аккуратно убрать гуся.', 'The goose needs to be removed quickly and neatly.', [], ''),
    ('ainura', 'Тысяча рублей, и вы его никогда не увидите.', 'A thousand rubles, and you will never see him.', [(130, 'Тысяча рублей'), (131, 'никогда')], ''),
    ('max', 'Договорились, вот твои деньги!', 'Deal, here is your money!', [], ''),
]
WALK = [
    (0, None, [
        "'I cannot kill this goose.' Let us review ",
        ('max', 'Я не могу'),
        ' literally translates to "I not can". ',
        ('max', 'этого гуся.'),
        ' puts an object shape ending on the words for "this goose", signaling a living creature.'
    ]),
    (1, None, [
        "'Maybe you will try once more?' Here we see ",
        ('kostya', 'Может,'),
        ' is a clipped word for "maybe", and ',
        ('kostya', 'ещё раз?'),
        ' translates to "once more". ',
        ('kostya', 'попробуешь'),
        ' is the "you" shape for the action word "try".'
    ]),
    (2, None, [
        "'No, I definitely cannot do this.' Here we see ",
        ('max', 'смогу'),
        ' is the finished partner of "can": "I will manage", one time, as opposed to being able in general. ',
        ('max', 'точно'),
        ' translates to "definitely".'
    ]),
    (3, None, [
        "'Let us suddenly scare him in the dark!' Let us check ",
        ('kostya', 'Давай'),
        ' plus a "we" action word, here ',
        ('kostya', 'напугаем'),
        ', gives the word for "let\'s". ',
        ('kostya', 'резко'),
        ' translates to "sharply", and ',
        ('kostya', 'в темноте!'),
        ' is "in the darkness".'
    ]),
    (4, None, [
        "'Kostya, this is complete nonsense.' As you hear, ",
        ('max', 'какой-то'),
        ' translates to "some kind of": the ending makes the word vague. ',
        ('max', 'полный бред.'),
        ' literally means "full nonsense", and the word for nonsense also refers to a fever\'s raving.'
    ]),
    (5, None, [
        "'Birds have a very weak heart.' Let us check ",
        ('kostya', 'У птиц'),
        ' literally translates to "at birds", the usual way to express "have". The "d" in ',
        ('kostya', 'сердце.'),
        ', the word for heart, is silent. ',
        ('kostya', 'слабое'),
        ' means "weak".'
    ]),
    (6, None, [
        "'See, he is standing and hissing loudly.' What happens here, ",
        ('max', 'Видишь,'),
        ' translates to "you see". ',
        ('max', 'шипит.'),
        ', the word for hisses, sounds like what it means, and they say the goose ',
        ('max', 'стоит'),
        ', stands.'
    ]),
    (7, None, [
        "'I urgently need a real specialist.' Focusing here, ",
        ('max', 'Мне'),
        ' and ',
        ('max', 'нужен'),
        ' literally translate to "to me needed", using a matching shape for the specialist. ',
        ('max', 'срочно'),
        ' translates to "urgently", and ',
        ('max', 'настоящий'),
        ' is the word for "real".'
    ]),
    (8, None, [
        "'Ainura, help us solve the problem!' Notice that ",
        ('max', 'помоги нам'),
        ' puts "we" in its "to" shape, because they help "to" someone. ',
        ('max', 'решить'),
        ' translates to both "decide" and "solve".'
    ]),
    (9, None, [
        "'What needs to be done with this bird?' Check out how ",
        ('ainura', 'Что нужно сделать'),
        ' literally translates to "what is needed to do". The word for bird changes its shape in ',
        ('ainura', 'с этой птицей?'),
        ' to match the word for "with".'
    ]),
    (10, None, [
        "'The goose needs to be removed quickly and neatly.' Here we see ",
        ('max', 'убрать'),
        ' translates to "to take away" and also "to tidy up", making it a gentle way to say "get rid of". ',
        ('max', 'аккуратно'),
        ' is the word for "neatly".'
    ]),
    (11, None, [
        "'A thousand rubles, and you will never see him.' After ",
        ('ainura', 'Тысяча'),
        ', the word for thousand, comes ',
        ('ainura', 'рублей,'),
        ' the "of" shape for more than one ruble. ',
        ('ainura', 'никогда не увидите.'),
        ' literally translates to "never not will see".'
    ]),
    (12, None, [
        "'Deal, here is your money!' Focusing here, ",
        ('max', 'Договорились,'),
        ' meaning we have agreed, is the word that seals a deal. ',
        ('max', 'деньги!'),
        ', the word for money, always acts like more than one, so "your" takes the matching shape ',
        ('max', 'твои'),
        '.'
    ]),
]
