# Authoring module for kukhnya-s01e19-scene-13.
ID = 'kukhnya-s01e19-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 13
TITLE = 'Инвалиды  (The Cripples)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Max and the other cooks are taking a quick break in the kitchen. They are just standing around chatting when Senya and Fedya walk in and mock them for being lazy. Let's listen."
OPENER = "Now let's go back through the exchange around The Cripples line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The kitchen is always a battlefield. Next time you watch the episode, listen for the Russian expressions for 'very' and 'to get tired' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Я очень устал сегодня.', 'I am very tired today.', [], ''),
    ('max', 'Мы много работали утром.', 'We worked a lot in the morning.', [], ''),
    ('max', 'Давайте немного отдохнем.', "Let's rest a bit.", [], ''),
    ('senya', 'Привет, повара!', 'Hello, cooks!', [], ''),
    ('fedya', 'Что встали, инвалиды?', 'What are you standing around for, cripples?', [(233, 'Что встали, инвалиды')], ''),
    ('fedya', 'Не видите?', "Can't you see?", [(234, 'Не видите')], ''),
    ('senya', 'Профессионалы пришли.', 'The pros are here.', [(235, 'Профессионалы пришли')], ''),
    ('max', 'Вы не профессионалы.', 'You are not professionals.', [], ''),
    ('max', 'Вы просто много говорите.', 'You just talk a lot.', [], ''),
    ('fedya', 'Мы говорим правду.', 'We are telling the truth.', [], ''),
    ('senya', 'Идите работать!', 'Go to work!', [], ''),
    ('max', 'Хорошо, мы идем.', 'Okay, we are going.', [], ''),
]
WALK = [
    (0, None, "'I am very tired today.' Max complains about feeling very tired today."),
    (1, None, "'We worked a lot in the morning.' Max mentions that they worked incredibly hard all morning."),
    (2, None, "'Let's rest a bit.' Max suggests taking a break. You can hear the word for 'a bit'."),
    (3, None, "'Hello, cooks!' Senya cheerfully greets the cooks in the kitchen."),
    (4, None, "'What are you standing around for, cripples?' Fedya uses a harsh word for people who are standing and doing nothing. Notice that 'are' is missing in Russian."),
    (5, None, "'Can' Fedya questions if they can see who just arrived."),
    (6, None, "'The pros are here.' Senya sarcastically announces the arrival of the kitchen professionals."),
    (7, None, "'You are not professionals.' Max retorts that they are not real professionals."),
    (8, None, "'You just talk a lot.' Max accuses the two of them of just talking a lot."),
    (9, None, "'We are telling the truth.' Fedya defends them. In Russian, it's just 'We speak truth'."),
    (10, None, "'Go to work!' Senya orders the cooks to get back to work immediately."),
    (11, None, "'Okay, we are going.' Max gives up and heads back to his station. The word 'are' is not translated."),
]
