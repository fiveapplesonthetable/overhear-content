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
INTRO = 'Barinov is fast asleep with a hangover when his phone starts ringing. It is Lyuba, from the restaurant, reminding him about work. The call comes first, in Russian.'
OPENER = 'The call, line by line.'
TRANSITION = 'Now the call again, from the first ring.'
OUTRO = "Barinov hangs up and tries to get a few more minutes in bed. He sounds a lot more awake on the phone than he is. See you next time."
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
    (0, None, "'What is that noise early in the morning?' 'Chto za' means 'what sort of', and it often sounds annoyed. 'S utra poranshe' is a set phrase for 'at the crack of dawn', usually said with a groan."),
    (1, None, "'Who is calling me so early in the morning?' 'Mne zvonit' is 'to me phones', so the person phoned goes in the 'to me' form. 'Utrom' ends in 'om' to mean 'in the morning'."),
    (2, None, "'Hello, Viktor Petrovich, are you up already?' Lyuba uses the polite 'vy', so the verb is 'vstali', with the plural 'li', even though she's talking to one man. That's how you address a boss."),
    (3, None, "'Of course, I have been up for a long time.' 'Na nogakh' is literally 'on feet', Russian for 'up and about'. 'Davno' covers the 'have been'."),
    (4, None, "'You are lying to me, you are still sleeping!' 'Obmanyvaete' is 'you deceive', with the polite 'ete' ending. 'Eshchyo' means 'still' here, and in other lines 'more' or 'yet'."),
    (5, None, "'I am cheerful and full of new strength.' After 'polon', full, the thing that fills goes into the 'of' form: 'sily' becomes 'sil', 'of strengths'. 'Bodryy' is brisk and wide awake."),
    (6, None, "'Viktor Petrovich, you will be late for work!' Lyuba stays polite and puts 'will be late' in the future. 'Na rabotu' needs a 'u' on 'rabota' to show the direction."),
    (7, None, "'Lyuba, leave me alone, I know my business.' 'Otstan'' is literally 'fall behind', and it's rude for 'get off my back'. 'Svoyo delo' is 'my own business', the thing he's good at."),
    (8, None, "'The restaurant is opening soon for guests.' The restaurant 'opens itself', so 'otkryvaetsya' ends in 'sya'. 'Skoro' is just 'soon'."),
    (9, None, "'You are the one who will be late for the shift today!' 'Eto ty' is 'it's you who', a handy way to hit back. 'Na smenu' is 'for the shift'."),
    (10, None, "'And when will you arrive at the kitchen yourself?' 'Sami', yourself, is in the plural form, to match the polite 'vy'. The little 'a' at the start means 'and what about'."),
    (11, None, "'And I am the chef, I will be a little late!' 'Zaderzhus'' means 'I will be held up', as in 'I will hold myself up'. 'A ya shef' is just 'and I chef', which is all the reason he needs."),
]
