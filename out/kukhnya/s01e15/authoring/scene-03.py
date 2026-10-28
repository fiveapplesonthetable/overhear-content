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
INTRO = "Viktor Petrovich wakes up with a terrible headache as Lyuba calls to remind him about work. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around A Morning Call line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Viktor hangs up the phone, determined to get a few more minutes of rest. Next time you watch the episode, listen for the Russian expressions for 'morning' and 'a bit earlier' — you will catch every word right away. See you next time!"
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
    (0, None, "'What is that noise early in the morning?' Russian omits the present-tense verb 'to be' here, linking 'noise' directly with 'morning', followed by 'a bit earlier'."),
    (1, None, "'Who is calling me so early in the morning?' Chef Barinov chooses the action verb meaning 'is calling' for the ongoing action, followed by 'early' and 'this morning'."),
    (2, None, "'Hello, Viktor Petrovich, are you up already?' , combining 'hello?' with 'already' and 'stood still'."),
    (3, None, "'Of course, I have been up for a long time.' Russian omits the present-tense verb 'to be' here, linking 'of course' directly with 'for a long time', pairing it with 'already' and 'legs'."),
    (4, None, "'You are lying to me, you are still sleeping!' the speaker chooses the action verb meaning 'are deceiving' for the ongoing action, followed by 'more' and 'are sleeping'."),
    (5, None, "'I am cheerful and full of new strength.' Russian omits the present-tense verb 'to be' here, linking 'cheerful' directly with 'full', pairing it with 'new' and 'ofpower'."),
    (6, None, "'Viktor Petrovich, you will be late for work!' the speaker uses the action verb meaning 'will be late' to focus on the single completed result, pairing it with 'job'."),
    (7, None, "'Lyuba, leave me alone, I know my business.' Chef Barinov leads with the direct command form meaning 'leave alone', pairing it with 'know' and 'matter'."),
    (8, None, "'The restaurant is opening soon for guests.' the speaker puts the word for 'restaurant' together with 'soon' and 'is opening' in a crisp, natural spoken turn of phrase."),
    (9, None, "'You are the one who will be late for the shift today!' Chef Barinov uses the action verb meaning 'will be late' to focus on the single completed result, pairing it with 'today' and 'shift'."),
    (10, None, "'And when will you arrive at the kitchen yourself?' The phrasing opens with 'when' before bringing in 'will arrive' and 'kitchen' to make the point clear."),
    (11, None, "'And I am the chef, I will be a little late!' Chef Barinov expresses this naturally by combining the word for 'a bit' with 'will be delayed'."),
]
