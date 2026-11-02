# Authoring module for kukhnya-s01e05-scene-04.
ID = 'kukhnya-s01e05-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = 'Неловкое расставание  (An Awkward Breakup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = 'Back at Claude Monet, Max, the young cook, has promised Kostya that Nastya literally translates to nothing to him, while Nastya is already planning children. Something has to give. Max finds her in the vegetable storeroom and tries to be clear without being cruel. Here it is in Russian.'
OPENER = "Let's slow it down. Listen for how many different ways Max finds to say 'not'."
TRANSITION = "Here's the breakup from beginning to end."
OUTRO = 'Count the negatives you just heard. Russian piles them up without cancelling anything, and Max needed every one.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Настя, что ты сейчас делаешь?', 'Nastya, what are you doing now?', [(50, 'Что ты делаешь')], ""),
    ('nastya', 'Ну, у нас же настоящее свидание!', 'Well, we are on a real date!', [(50, 'Ну, у нас же свидание')], ""),
    ('max', 'Нет, Настя, у нас не свидание.', 'No, Nastya, we are not on a date.', [(51, 'Нет, Настя, у нас не свидание')], ""),
    ('max', 'Ты вчера всё не так поняла.', 'You understood everything wrong yesterday.', [(52, 'Ты вчера все не так поняла')], ""),
    ('max', 'Мы с тобой совсем не встречаемся.', 'You and I are not dating at all.', [(53, 'Мы с тобой не встречаемся')], ""),
    ('max', 'Я не твой парень.', 'I am not your boyfriend.', [(53, 'Я не твой парень')], ""),
    ('max', 'А ты не моя девушка.', 'And you are not my girlfriend.', [(53, 'а ты не моя девушка')], ""),
    ('nastya', 'Ты что, меня сейчас бросаешь?', 'Are you dumping me right now?', [(54, 'Ты что, меня бросаешь')], ""),
    ('max', 'Это вовсе не глупые шутки.', 'These are not silly jokes at all.', [(55, 'шуточки'), (56, 'Это не шутки, Настя')], ""),
    ('max', 'Между нами никогда ничего не было.', 'Nothing ever happened between us.', [(58, 'Между нами ничего не было')], ""),
    ('nastya', 'А как же наш поцелуй?', 'And what about our kiss?', [(60, 'А поцелуй')], ""),
    ('nastya', 'А наши будущие дети?', 'And what about our future children?', [(61, 'А наши дети')], ""),
    ('max', 'Какие ещё дети, Настя?', 'What children, Nastya?', [(62, 'Какие дети')], ""),
    ('max', 'Да, если хочешь, я тебя бросаю!', 'Yes, if you want, I am dumping you!', [(63, 'да, я тебя бросаю')], ""),
]
WALK = [
    (0, None, [
        "'Nastya, what are you doing now?' A plain question to set up the shock. ",
        ('max', 'делаешь?'),
        ", 'you do', ends in -esh, the regular ending when you talk to one person as ",
        ('max', 'ты'),
        "."
    ]),
    (1, None, [
        "'Well, we are on a real date!' adds 'obviously', as if Max ought ",
        ('nastya', 'же'),
        ' to know. ',
        ('nastya', 'свидание!'),
        ", 'a date', shares its root with the phrase for 'goodbye': both are about seeing each other."
    ]),
    (2, None, "'No, Nastya, we are not on a date.' No 'are' anywhere. Russian drops 'is' and 'are' in the present, so it's just 'at us not a date'."),
    (3, None, [
        "'You understood everything wrong yesterday.' is 'not so', not the way ",
        ('max', 'не'),
        ('max', 'так'),
        ' it really was. ',
        ('max', 'поняла.'),
        " ends in -a because the person who got it wrong is a woman."
    ]),
    (4, None, [
        "'You and I are not dating at all.' 'You and I' comes out as ",
        ('max', 'Мы'),
        ('max', 'с'),
        ('max', 'тобой'),
        ", 'we with you'. ",
        ('max', 'встречаемся.'),
        ", 'we're dating', literally is used for 'we meet each other'."
    ]),
    (5, None, [
        "'I am not your boyfriend.' is the ordinary word for 'guy', ",
        ('max', 'парень.'),
        " and also 'boyfriend', similar to how the word for 'girl' works."
    ]),
    (6, None, [
        "'And you are not my girlfriend.' The mirror of the last line, with ",
        ('max', 'моя'),
        ", 'my', in its feminine form to go with ",
        ('max', 'девушка.')
    ]),
    (7, None, [
        "'Are you dumping me right now?' literally means 'you throw', and Russians ",
        ('nastya', 'бросаешь?'),
        ' use it for dumping someone. ',
        ('nastya', 'Ты'),
        ('nastya', 'что,'),
        " at the front is a shocked 'what, are you...?'."
    ]),
    (8, None, [
        "'These are not silly jokes at all.' is a stronger 'not at all', ",
        ('max', 'вовсе'),
        ('max', 'не'),
        ' a cousin of the phrase from a few lines ago. ',
        ('max', 'шутки.'),
        ", 'jokes', is plural, and so is ",
        ('max', 'глупые'),
        ", 'silly'."
    ]),
    (9, None, [
        "'Nothing ever happened between us.' Three negatives at once, ",
        ('max', 'никогда'),
        ", ",
        ('max', 'ничего'),
        " and ",
        ('max', 'не'),
        ". Russian needs all three and none of them cancels another."
    ]),
    (10, None, [
        "'And what about our kiss?' A ",
        ('nastya', 'как'),
        ('nastya', 'же'),
        " is literally 'and how then', the standard way to say 'but what about'. ",
        ('nastya', 'поцелуй?'),
        ", 'a kiss', comes from the same root as the verb 'to kiss'."
    ]),
    (11, None, [
        "'And what about our future children?' , 'future', has the same root ",
        ('nastya', 'будущие'),
        " you find in the word for 'I will be'. Its ending matches ",
        ('nastya', 'дети?'),
        " perfectly."
    ]),
    (12, None, [
        "'What children, Nastya?' normally expresses 'still' or 'more', but ",
        ('max', 'ещё'),
        ' in ',
        ('max', 'Какие'),
        ('max', 'ещё'),
        " it translates to 'what on earth'."
    ]),
    (13, None, [
        "'Yes, if you want, I am dumping you!' Max takes her own word and says ",
        ('max', 'бросаю!'),
        ", 'I'm dumping'. ",
        ('max', 'если'),
        ('max', 'хочешь,'),
        ", 'if you want', is a phrase you'll hear everywhere."
    ]),
]
