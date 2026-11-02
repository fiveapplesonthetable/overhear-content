# Authoring module for kukhnya-s01e15-scene-16.
ID = 'kukhnya-s01e15-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 16
TITLE = 'Больное сердце  (A Bad Heart)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Back in the kitchen, Fedya wants to know what Lyova has been playing at. Russian first."
OPENER = 'Again, slowly.'
TRANSITION = 'And the scene again, start to finish.'
OUTRO = 'Lyova realises that a made-up illness can still cause real stress. Can he calm down? Until next time.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('fedya', 'Лёва, ну что такое?', 'Lyova, well what is this?', [(330, 'Лёва, ну что такое, а?')], ''),
    ('lyova', 'Что ты хочешь сказать?', 'What do you want to say?', [], ''),
    ('fedya', 'Что за цирк ты устроил?', 'What kind of circus did you stage?', [], ''),
    ('lyova', 'Я ничего не устраивал.', 'I did not stage anything.', [], ''),
    ('fedya', 'Виктору Петровичу надо хорошо выспаться.', 'Viktor Petrovich needs to sleep well.', [], ''),
    ('lyova', 'Почему ему надо спать?', 'Why does he need to sleep?', [], ''),
    ('fedya', 'Ты же знаешь его ситуацию.', 'You know his situation.', [], ''),
    ('fedya', 'У него больное сердце.', 'He has a sick heart.', [], ''),
    ('lyova', 'У него больное сердце?', 'He has a sick heart?', [], ''),
    ('lyova', 'Это у меня больное сердце.', 'It is me who has a sick heart.', [], ''),
    ('fedya', 'Тебе надо успокоиться, Лёва.', 'You need to calm down, Lyova.', [], ''),
    ('lyova', 'Я не могу работать в таком стрессе.', 'I cannot work in such stress.', [], ''),
]
WALK = [
    (0, None, ["'Lyova, well what is this?' We can analyze the sentence: ", ('fedya', 'ну'), ('fedya', 'что'), ('fedya', 'такое'), " asks what's going on, while ", ('fedya', 'ну'), ' pushes for an answer.']),
    (1, None, ["'What do you want to say?' This means what are you getting at. The verb ", ('lyova', 'сказать'), ' stays in its basic form after ', ('lyova', 'хочешь'), '.']),
    (2, None, ["'What kind of circus did you stage?' The expression ", ('fedya', 'Что'), ('fedya', 'за'), ' asks what kind of. To say ', ('fedya', 'цирк'), ('fedya', 'ты'), ('fedya', 'устроил'), ' means to put on a show.']),
    (3, None, ["'I did not stage anything.' The expression ", ('lyova', 'ничего'), ('lyova', 'не'), ' is a double negative Russian insists on. Using ', ('lyova', 'устраивал'), ' is the way to deny doing it at all.']),
    (4, None, ["'Viktor Petrovich needs to sleep well.' The verb ", ('fedya', 'выспаться'), ' starts with out, meaning sleep your fill. Both names take a to ending, making them ', ('fedya', 'Виктору'), ('fedya', 'Петровичу'), '.']),
    (5, None, ["'Why does he need to sleep?' We can look at the words: ", ('lyova', 'ему'), ' is the to form of he. Here we have ', ('lyova', 'Почему'), ('lyova', 'ему'), ('lyova', 'надо'), ' asks why is it necessary for him.']),
    (6, None, ["'You know his situation.' We will break down the speech: ", ('fedya', 'его'), ' never changes, whatever it describes. The ', ('fedya', 'же'), ' after ', ('fedya', 'Ты'), ' adds after all, meaning you do know.']),
    (7, None, ["'He has a sick heart.' Russian says at him a sick heart where English says he has. The small word ", ('fedya', 'У'), ' does the work of has.']),
    (8, None, ["'He has a sick heart?' Lyova repeats ", ('lyova', 'У'), ('lyova', 'него'), ('lyova', 'больное'), ('lyova', 'сердце'), ' as a question. In Russian only the tone changes, with no extra words needed.']),
    (9, None, ["'It is me who has a sick heart.' Putting ", ('lyova', 'Это'), ' in front to make it ', ('lyova', 'Это'), ('lyova', 'у'), ('lyova', 'меня'), " stresses who, meaning it is me who. Lyova turns Fedya's line round on himself."]),
    (10, None, ["'You need to calm down, Lyova.' Russian says to you it is necessary, and the calming word ", ('fedya', 'успокоиться'), ' ends in self, which makes it calm yourself.']),
    (11, None, ["'I cannot work in such stress.' Let's break down the dialogue: ", ('lyova', 'в'), ('lyova', 'таком'), ('lyova', 'стрессе'), ' puts an ending on stress for in. The words ', ('lyova', 'не'), ('lyova', 'могу'), ' come before ', ('lyova', 'работать'), '.']),
]
