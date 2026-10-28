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
    (0, None, "'What is that noise early in the morning?' Waking up feeling terrible, the boss grumbles about the loud sounds disturbing his rest."),
    (1, None, "'Who is calling me so early in the morning?' Annoyed by the ringing phone, he questions who could possibly be bothering him at this hour."),
    (2, None, "'Hello, Viktor Petrovich, are you up already?' Lyuba checks in on her boss, making sure he is awake and getting ready for the day."),
    (3, None, "'Of course, I have been up for a long time.' Lying through his teeth, he pretends he has been active and alert for quite a while."),
    (4, None, "'You are lying to me, you are still sleeping!' Seeing right through his bluff, she calls him out on his obvious attempt to deceive her."),
    (5, None, "'I am cheerful and full of new strength.' Trying to sound energetic, he claims to be completely refreshed and ready to go."),
    (6, None, "'Viktor Petrovich, you will be late for work!' She issues a stern warning about the time, reminding him of his responsibilities."),
    (7, None, "'Lyuba, leave me alone, I know my business.' Brushing off her concerns, the chef insists he has everything completely under control."),
    (8, None, "'The restaurant is opening soon for guests.' Highlighting the urgency, the caller points out that service is about to begin."),
    (9, None, "'You are the one who will be late for the shift today!' Flipping the blame, he attempts to turn the accusation around on his employee."),
    (10, None, "'And when will you arrive at the kitchen yourself?' Refusing to back down, she directly asks for his actual estimated time of arrival."),
    (11, None, "'And I am the chef, I will be a little late!' Pulling rank, the boss excuses his own tardiness by relying on his authority."),
]
