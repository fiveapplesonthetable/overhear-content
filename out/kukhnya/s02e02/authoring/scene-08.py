# Authoring module for kukhnya-s02e02-scene-08.
ID = 'kukhnya-s02e02-scene-08'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 8
TITLE = 'Держи  (Here You Go)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "In the middle of the kitchen chaos, a very brief exchange happens between two people handing over an item. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around Here You Go line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "A very brief exchange happens between two people handing over an item. Next time you watch the episode, listen for the Russian expressions for 'thing' and 'to take' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Привет.', 'Hi.', [], ''),
    ('max', 'Привет, Вика.', 'Hi, Vika.', [], ''),
    ('max', 'Вот твоя вещь.', 'Here is your thing.', [], ''),
    ('max', 'Возьми это.', 'Take this.', [], ''),
    ('max', 'Держи.', 'Here you go.', [(157, 'Держи')], ''),
    ('vika', 'Спасибо.', 'Thanks.', [], ''),
    ('vika', 'Это мне?', 'Is this for me?', [], ''),
    ('max', 'Да, тебе.', 'Yes, for you.', [], ''),
    ('vika', 'Очень хорошо.', 'Very good.', [], ''),
    ('max', 'Я рад.', 'I am glad.', [], ''),
    ('max', 'Пожалуйста.', "You're welcome.", [], ''),
    ('max', 'Я пойду.', 'I will go.', [], ''),
    ('vika', 'Пока.', 'Bye.', [], ''),
]
WALK = [
    (0, None, "'Hi.' Max catches up with Vika and greets her."),
    (1, None, "'Hi, Vika.' The greeting is returned as they pause for a brief handoff."),
    (2, None, "'Here is your thing.' Max holds out an item she left behind."),
    (3, None, "'Take this.' He tells her to go ahead and take it."),
    (4, None, "'Here you go.' Handing it over, he uses the everyday Russian word for 'here you go'."),
    (5, None, "'Thanks.' Vika takes the item and thanks him."),
    (6, None, "'Is this for me?' Surprised, she double-checks whether it is really meant for her."),
    (7, None, "'Yes, for you.' Max confirms that yes, it is for her."),
    (8, None, "'Very good.' Vika nods that that is very good."),
    (9, None, "'I am glad.' She adds a quick word of appreciation."),
    (10, None, "'You're welcome.' Max replies with a polite 'you are welcome'."),
    (11, None, "'I will go.' Not wanting to linger awkwardly, Max says he will head off now."),
    (12, None, "'Bye.' Vika says a brief goodbye as they part ways."),
]
