ID = 'kukhnya-s03e01-scene-01'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 1
TITLE = "Новый официант  (The New Waiter)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "anja"}
LABELS = {"anya": "Макс", "guest": "Гость"}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'

INTRO = "Welcome to Season Three of Kukhnya. At the French restaurant Claude Monet in Moscow, Max Lavrov has traded his chef jacket for a waiter's vest, and he quickly discovers that serving demanding guests in the dining room is harder than it looks."

STORY = [
    ('anya', 'Я Макс Лавров.', 'I am Max Lavrov.', [(1, 'Я Макс Лавров')], ''),
    ('anya', 'Раньше работал поваром, теперь я официант.', 'I used to work as a cook, now I am a waiter.', [(1, 'Раньше работал поваром, теперь я официант')], ''),
    ('anya', 'Работать официантом совсем не легко.', 'Working as a waiter is not easy at all.', [(2, 'работать официантом легко')], 'adapted'),
    ('anya', 'Вы сильно заблуждаетесь.', 'You are gravely mistaken.', [(3, 'вы сильно заблуждаетесь')], ''),
    ('anya', 'Здравствуйте!', 'Hello!', [(6, 'Здравствуйте')], ''),
    ('guest', 'Вы записываете?', 'Are you writing this down?', [(7, 'Вы записываете')], ''),
    ('anya', 'Я запомню.', 'I will remember it.', [(8, 'Я запомню')], ''),
    ('guest', 'Гратен, пожалуйста. А мне кролика.', 'Gratin, please. And rabbit for me.', [(9, 'Гратен, пожалуйста. А мне кролика')], ''),
    ('guest', 'Салат и вода без газа.', 'A salad and still water.', [(9, 'Салат'), (10, 'И вода без газа')], 'adapted'),
    ('guest', 'И апельсиновый фреш.', 'And fresh orange juice.', [(11, 'И апельсиновый')], 'adapted'),
    ('anya', 'Что это?', 'What is this?', [(12, 'Что это')], ''),
    ('anya', 'Красота!', 'Beautiful!', [(15, 'Красота')], ''),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'I am Max Lavrov.' Max anchors the line on 'I', while 'Lavrov' completes the thought."),
    (1, None, "'I used to work as a cook, now I am a waiter.' The meaning hinges on 'earlier' working together with 'waiter' in spoken Russian."),
    (2, None, "'Working as a waiter is not easy at all.' The negative particle sits right before the verb meaning 'to work' to negate the statement."),
    (3, None, "'You are gravely mistaken.' Max pairs 'strongly' with 'are mistaken' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (4, None, "'Hello!' In Russian, the idea of 'hello' flows naturally into 'hello' without extra filler words."),
    (5, None, "'Are you writing this down?' In spoken Russian, the words stay in their normal statement order and the guest's rising voice at the end turns the line into a question."),
    (6, None, "'I will remember it.' Here the Russian phrasing highlights 'I' before landing on 'will remember'."),
    (7, None, "'Gratin, please. And rabbit for me.' the guest brings out the contrast between 'gratin' and 'please' in a few short words."),
    (8, None, "'A salad and still water.' the guest anchors the line on 'salad', while 'gas' completes the thought."),
    (9, None, "'And fresh orange juice.' Here the guest anchors the thought on 'orange' and finishes on 'fresh juice', keeping the spoken rhythm brisk and natural."),
    (10, None, "'What is this?' The meaning hinges on 'what' working together with 'this' in spoken Russian."),
    (11, None, "'Beautiful!' In Russian, the idea of 'beauty' flows naturally into 'beauty' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene in the dining room. Listen for Max introducing his new job as a waiter and promising to memorize the entire order without a notepad. Until next time!'
CLOSING = ("anya", "До завтра!")
