# Authoring module for kukhnya-s03e01-scene-01.
ID = 'kukhnya-s03e01-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 1
TITLE = 'Новый официант  (The New Waiter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = "Welcome to Season Three of Kukhnya. At the French restaurant Claude Monet in Moscow, Max Lavrov has traded his chef jacket for a waiter's vest, and he quickly discovers that serving demanding guests in the dining room is harder than it looks."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene in the dining room. Listen for Max introducing his new job as a waiter and promising to memorize the entire order without a notepad. Until next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('max', 'Я Макс Лавров.', 'I am Max Lavrov.', [(1, 'Я Макс Лавров')], ''),
    ('max', 'Раньше работал поваром, теперь я официант.', 'I used to work as a cook, now I am a waiter.', [(1, 'Раньше работал поваром, теперь я официант')], ''),
    ('max', 'Работать официантом совсем не легко.', 'Working as a waiter is not easy at all.', [(2, 'работать официантом легко')], 'adapted'),
    ('max', 'Вы сильно заблуждаетесь.', 'You are gravely mistaken.', [(3, 'вы сильно заблуждаетесь')], ''),
    ('max', 'Здравствуйте!', 'Hello!', [(6, 'Здравствуйте')], ''),
    ('guest', 'Вы записываете?', 'Are you writing this down?', [(7, 'Вы записываете')], ''),
    ('max', 'Я запомню.', 'I will remember it.', [(8, 'Я запомню')], ''),
    ('guest', 'Гратен, пожалуйста. А мне кролика.', 'Gratin, please. And rabbit for me.', [(9, 'Гратен, пожалуйста. А мне кролика')], ''),
    ('guest', 'Салат и вода без газа.', 'A salad and still water.', [(9, 'Салат'), (10, 'И вода без газа')], 'adapted'),
    ('guest', 'И апельсиновый фреш.', 'And fresh orange juice.', [(11, 'И апельсиновый')], 'adapted'),
    ('max', 'Что это?', 'What is this?', [(12, 'Что это')], ''),
    ('max', 'Красота!', 'Beautiful!', [(15, 'Красота')], ''),
]
WALK = [
    (0, None, "'I am Max Lavrov.' Being Max Lavrov is how Max lays out the situation for the guest."),
    (1, None, "'I used to work as a cook, now I am a waiter.' Once he used to work as a cook now he is a waiter, Max can finally tell the guest what he means."),
    (2, None, "'Working as a waiter is not easy at all.' Adding that working as a waiter is not easy at all fills in the missing piece for the guest."),
    (3, None, "'You are gravely mistaken.' Max tells the guest that the guest is gravely mistaken without dressing it up."),
    (4, None, "'Hello!' With the conversation and work at stake, Max reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (5, None, '\'Are you writing this down?\' Asking whether Max writing this down cuts straight through the tension between the guest and Max. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, "'I will remember it.' Max reminds the guest that he will remember it before the moment passes."),
    (7, None, "'Gratin, please. And rabbit for me.' Over the kitchen and the order, the guest answers Max without a second thought."),
    (8, None, "'A salad and still water.' Around the kitchen and shift, the guest sets a calm, everyday tone with Max."),
    (9, None, "'And fresh orange juice.' Around the kitchen and moment, the guest sets a calm, everyday tone with Max."),
    (10, None, '\'What is this?\' Asking what this is cuts straight through the tension between Max and the guest. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, "'Beautiful!' Over the room and the table, Max lets his real feelings show. Russian puts the key word right up front so his emotion lands on the first beat."),
]
