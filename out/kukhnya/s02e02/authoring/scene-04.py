# Authoring module for kukhnya-s02e02-scene-04.
ID = 'kukhnya-s02e02-scene-04'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 4
TITLE = 'Всё в прошлом  (All in the Past)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "Focused on all in the past, Max runs into Sasha in the kitchen. Sasha asks if he is still upset about Vika leaving, but Max denies it. Let's listen closely to Max and Sasha's exchange in Russian first, and then walk through each line together."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max runs into Sasha in the kitchen. Sasha asks if he is still upset about Vika leaving, but Max denies it. Next time you watch the episode, listen for the Russian expressions for 'matter' and 'to happen' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Привет.', 'Hi.', [(80, 'Привет.')], ''),
    ('sasha', 'Привет, Макс.', 'Hi, Max.', [(80, 'Привет.')], ''),
    ('sasha', 'Как дела?', 'How are you?', [(81, 'Как дела?')], ''),
    ('max', 'Бывало и лучше.', "I've been better.", [(82, 'Да так бывало и лучше.')], ''),
    ('sasha', 'Всё ещё переживаешь?', 'Are you still worrying?', [(83, 'Все еще переживаешь из Вики, да?')], ''),
    ('max', 'Да нет.', 'Well, no.', [(84, 'Да нет.')], ''),
    ('max', 'С Викой всё в прошлом.', 'With Vika everything is in the past.', [(84, 'С Викой уже все в прошлом.')], ''),
    ('sasha', 'Ты уверен?', 'Are you sure?', [], ''),
    ('max', 'Конечно.', 'Of course.', [], ''),
    ('sasha', 'Ну ладно.', 'Well, okay.', [], ''),
    ('sasha', 'Мне пора работать.', "It's time for me to work.", [], ''),
    ('max', 'Увидимся.', 'See you.', [], ''),
]
WALK = [
    (0, None, "'Hi.' Max greets Sasha casually as they cross paths."),
    (1, None, "'Hi, Max.' Sasha smiles and says hello back to him."),
    (2, None, "'How are you?' She asks how things are going with him today."),
    (3, None, "'I' Max sighs and admits he has seen better days."),
    (4, None, "'Are you still worrying?' Guessing the reason, Sasha asks if he is still upset over Vika. Then Max responds."),
    (5, None, "'Well, no.' Max brushes the question off, pretending he is fine."),
    (6, None, "'With Vika everything is in the past.' Trying to sound convincing, he claims that everything with Vika is behind him now."),
    (7, None, "'Are you sure?' Sasha looks at him skeptically and asks if he is really sure. Then Max replies."),
    (8, None, "'Of course.' Max insists that of course he is over her."),
    (9, None, "'Well, okay.' Not pushing him further, Sasha accepts his answer."),
    (10, None, "'It's time for me to work.' She notes that it is time for her to get back to her tables."),
    (11, None, "'See you.' Max tells her he will see her around later."),
]
