# Authoring module for kukhnya-s01e15-scene-03.
ID = 'kukhnya-s01e15-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 3
TITLE = 'Утренний звонок  (A Morning Call)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyuba': 'Люба'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'Barinov is fast asleep with a hangover when his phone starts ringing. It is Lyuba, from the restaurant, reminding him about work. Here is the call in Russian first.'
OPENER = "Let's go through the call slowly, line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Barinov hangs up, and tries to get a few more minutes in bed. When you watch, notice how awake he pretends to be. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Что за шум с утра пораньше?', 'What is that noise early in the morning?', [], ''),
    ('barinov', 'Кто мне звонит так рано утром?', 'Who is calling me so early in the morning?', [], ''),
    ('lyuba', 'Алло, Виктор Петрович, вы уже встали?', 'Hello, Viktor Petrovich, are you up already?', [(16, 'Алло. Виктор Петрович, вы уже встали?')], ''),
    ('barinov', 'Конечно, я давно уже на ногах.', 'Of course, I have been up for a long time.', [], ''),
    ('lyuba', 'Вы меня обманываете, вы ещё спите!', 'You are lying to me, you are still sleeping!', [(17, 'Вы меня обманываете')], ''),
    ('barinov', 'Я бодрый и полон новых сил.', 'I am cheerful and full of new strength.', [], ''),
    ('lyuba', 'Виктор Петрович, вы опоздаете на работу!', 'Viktor Petrovich, you will be late for work!', [(18, 'Виктор Петрович, вы опоздаете на работу')], ''),
    ('barinov', 'Люба, отстань, я знаю своё дело.', 'Lyuba, leave me alone, I know my business.', [(19, 'Люба, отстань')], ''),
    ('lyuba', 'Ресторан скоро открывается для гостей.', 'The restaurant is opening soon for guests.', [], ''),
    ('barinov', 'Это ты опоздаешь сегодня на смену!', 'You are the one who will be late for the shift today!', [(19, 'Это ты опоздаешь')], ''),
    ('lyuba', 'А когда вы сами приедете на кухню?', 'And when will you arrive at the kitchen yourself?', [], ''),
    ('barinov', 'А я шеф, я немного задержусь!', 'And I am the chef, I will be a little late!', [(20, 'А я задержусь')], ''),
]
WALK = [
    (0, None, "'What is that noise early in the morning?' 'Chto za' asks 'what kind of'. 'S utra poranshe' is 'from morning, a bit early', and it's a common phrase for an unreasonably early hour."),
    (1, None, "'Who is calling me so early in the morning?' 'Mne zvonit' is 'to me phones', so the person phoned goes in the 'to me' form. 'Utrom' ends in 'om' to mean 'in the morning'."),
    (2, None, "'Hello, Viktor Petrovich, are you up already?' 'Vstali' is the plural past, 'have you got up'. Lyuba uses 'vy', the polite form, to her boss, and the plural ending shows it."),
    (3, None, "'Of course, I have been up for a long time.' 'Na nogakh' is 'on feet', which is the Russian way to say 'up and about'. 'Davno' means 'long ago'."),
    (4, None, "'You are lying to me, you are still sleeping!' 'Obmanyaete' is the polite 'you deceive'. 'Eshchyo' means 'still' here, and it's the same word as 'more' or 'yet'."),
    (5, None, "'I am cheerful and full of new strength.' 'Polon' is 'full' and the full thing follows it with 'of' in the ending, 'novykh sil'. 'Bodry' is 'brisk', as in 'bright-eyed'."),
    (6, None, "'Viktor Petrovich, you will be late for work!' The word for 'will be late' is in the future, with 'vy' as the polite 'you'. 'Na rabotu' is 'to work'."),
    (7, None, "'Lyuba, leave me alone, I know my business.' 'Otstan' is literally 'fall behind', and it's the rude way to say 'get off my back'. 'Svoyo delo' is 'my own business', the thing you're good at."),
    (8, None, "'The restaurant is opening soon for guests.' 'Otkryvaetsya' ends in 'sya', so the restaurant 'opens itself'. 'Skoro' is 'soon'."),
    (9, None, "'You are the one who will be late for the shift today!' 'Eto ty' is 'it's you who', a handy way to hit back. 'Na smenu' is 'for the shift'."),
    (10, None, "'And when will you arrive at the kitchen yourself?' 'Sami' means 'yourselves', and it's in the plural because Lyuba is polite. The little 'a' at the start is a stern 'and what about'."),
    (11, None, "'And I am the chef, I will be a little late!' 'Zaderzhus'' means 'I will be held up', as in 'I will hold myself up'. 'A ya shef' is just 'and I chef', which is all the reason he needs."),
]
