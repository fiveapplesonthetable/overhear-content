# Authoring module for kukhnya-s01e04-scene-13.
ID = 'kukhnya-s01e04-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 13
TITLE = 'Заказ у бара  (Order at the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "At the bar, Nastya gives Kostya an urgent drinks order. Kostya, who is secretly in love with her, loses track of what she said and has to ask again. Here's the conversation in Russian first."
OPENER = 'Now the drinks order.'
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Kostya makes the drinks, and Nastya hurries off. You've heard the phrase for in the best way, which means he'll do it properly."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, приготовь срочный заказ для гостей.', 'Kostya, prepare an urgent order for the guests.', [(166, 'мне коньяку')], ''),
    ('kostya', 'Я слушаю тебя очень внимательно.', 'I am listening to you very attentively.', [(168, 'Сделаем')], ''),
    ('nastya', 'Мне нужно триста грамм хорошего коньяка.', 'I need three hundred grams of good cognac.', [(166, 'коньяку 300')], ''),
    ('nastya', 'И налей два виски по сто грамм.', 'And pour two whiskeys of a hundred grams each.', [(166, 'виски два по сто')], ''),
    ('nastya', 'А ещё принеси три горячих чайника чая.', 'And also bring three hot pots of tea.', [(167, 'три чайника')], ''),
    ('kostya', 'Конечно, сделаем всё быстро и аккуратно.', 'Of course, we will do everything quickly and neatly.', [(168, 'Сделаем')], ''),
    ('nastya', 'Почему ты стоишь и не работаешь?', 'Why are you standing and not working?', [(169, 'И что мы стоим')], ''),
    ('kostya', 'Настя, я хотел спросить кое-что.', 'Nastya, I wanted to ask something.', [(170, 'Настя, а')], ''),
    ('nastya', 'Что именно ты хочешь узнать?', 'What exactly do you want to find out?', [(170, 'Что')], ''),
    ('kostya', 'Сколько именно виски нужно наливать в стаканы?', 'How much whiskey exactly do I need to pour into the glasses?', [(171, 'Сколько наливать')], ''),
    ('nastya', 'Два раза по сто грамм, как обычно!', 'Two times a hundred grams, as usual!', [(172, 'Два по сто')], ''),
    ('kostya', 'Понял, сейчас всё приготовлю в лучшем виде.', 'Got it, now I will prepare everything in the best way.', [(172, 'так и говори')], ''),
]
WALK = [
    (0, None, [
        "'Kostya, prepare an urgent order for the guests.' The Russian expression for prepare is ",
        ('nastya', 'приготовь'),
        ' The Russian expression for urgent is ',
        ('nastya', 'срочный'),
        ' and literally for the guests translates to ',
        ('nastya', 'для гостей.')
    ]),
    (1, None, [
        "'I am listening to you very attentively.' The phrase for I listen translates to ",
        ('kostya', 'слушаю'),
        ' which also covers I am listening. The phrase for attentively is ',
        ('kostya', 'внимательно.')
    ]),
    (2, None, [
        "'I need three hundred grams of good cognac.' The term for three hundred is ",
        ('nastya', 'триста'),
        ' built from the Russian term for hundred. Literally good cognac translates to ',
        ('nastya', 'хорошего коньяка.')
    ]),
    (3, None, [
        "'And pour two whiskeys of a hundred grams each.' The word for a hundred each is ",
        ('nastya', 'по сто'),
        ' built from the word for each, ',
        ('nastya', 'по'),
        ' The Russian expression for whiskey translates to ',
        ('nastya', 'виски')
    ]),
    (4, None, [
        "'And also bring three hot pots of tea.' The Russian term for pots, as in ",
        ('nastya', 'чайника'),
        ', is built from the word for tea. The expression for three is ',
        ('nastya', 'три горячих')
    ]),
    (5, None, [
        "'Of course, we will do everything quickly and neatly.' The translation for we'll do is ",
        ('kostya', 'сделаем'),
        ' just one word. The Russian expression for neatly translates to ',
        ('kostya', 'аккуратно.')
    ]),
    (6, None, [
        "'Why are you standing and not working?' Literally you stand translates to ",
        ('nastya', 'стоишь'),
        ' often used for being idle. The phrase for not working is ',
        ('nastya', 'не работаешь?')
    ]),
    (7, None, [
        "'Nastya, I wanted to ask something.' The Russian expression for something in particular is ",
        ('kostya', 'кое-что.'),
        ' The phrase for wanted to ask translates to ',
        ('kostya', 'хотел спросить')
    ]),
    (8, None, [
        "'What exactly do you want to find out?' The translation for exactly translates to ",
        ('nastya', 'именно'),
        ' pointing at the very thing. The phrase for to find out is ',
        ('nastya', 'узнать?')
    ]),
    (9, None, [
        "'How much whiskey exactly do I need to pour into the glasses?' The translation for how much is ",
        ('kostya', 'Сколько'),
        ' which also covers how many. Into the glasses translates to ',
        ('kostya', 'в стаканы?')
    ]),
    (10, None, [
        "'Two times a hundred grams, as usual!' The phrase for two times translates to ",
        ('nastya', 'Два раза'),
        ' built from the Russian term for time, ',
        ('nastya', 'раз.'),
        ' The phrase for as usual is ',
        ('nastya', 'как обычно!')
    ]),
    (11, None, [
        "'Got it, now I will prepare everything in the best way.' Literally in the best form translates to ",
        ('kostya', 'в лучшем виде.'),
        " a fixed phrase for doing a thing properly. The Russian term for I'll prepare is ",
        ('kostya', 'приготовлю')
    ]),
]
