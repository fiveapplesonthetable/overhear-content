# Authoring module for kukhnya-s01e12-scene-19.
ID = 'kukhnya-s01e12-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 19
TITLE = "Отчёт разведчика  (The Scout's Report)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Fedya has been sent next door to spy on the new Italian restaurant, and he is back in the kitchen with a report. Chef Barinov is very keen to hear it. Listen to the report in Russian first.'
OPENER = 'Back through the report, line by line.'
TRANSITION = 'The report again, all in one piece.'
OUTRO = "Barinov hears what he wanted to hear, and Fedya gets his lunch. Try the phrase for so-so next time someone asks how something was. Talk soon."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('barinov', 'Федя, ну что там у конкурентов?', "Fedya, well, how are things at the competitors'?", [(256, 'Ну что?')], ''),
    ('fedya', 'Шеф, наш разведчик вернулся с отчётом.', 'Chef, our scout has returned with a report.', [(255, 'Здрасте. Штирец.')], ''),
    ('barinov', 'Рассказывай быстрее. Ты заходил внутрь?', 'Tell me faster. Did you go inside?', [(260, 'Давай рожай быстрее.')], ''),
    ('fedya', 'Да, я посмотрел их новый зал.', 'Yes, I looked at their new hall.', [], ''),
    ('barinov', 'И как? Интерьер выглядит красиво?', 'And how is it? Does the interior look nice?', [], ''),
    ('fedya', 'Честно говоря, интерьер так себе.', 'To tell the truth, the interior is so-so.', [(261, 'Ну, интерьер так себе.')], ''),
    ('barinov', 'А что происходит с гостями?', 'And what is going on with the guests?', [(258, 'Я тебя про ресторан спрашиваю.')], ''),
    ('fedya', 'В зале тишина, свободных мест полно.', 'In the hall there is silence, plenty of empty seats.', [(262, 'В зале штиль. Свободных мест полно.')], ''),
    ('barinov', 'Ты видишь, о чём я говорил!', 'You see what I was talking about!', [(263, 'Ты о чём я говорил, а?')], ''),
    ('barinov', 'Нам пока ничего не нужно менять.', 'We do not need to change anything yet.', [(264, 'Рано нам меняться.'), (265, 'Ничего нам пока менять не надо.')], ''),
    ('fedya', 'Шеф, а можно мне поесть?', 'Chef, can I have something to eat?', [], ''),
    ('barinov', 'Иди на кухню, заслужил горячий обед.', 'Go to the kitchen, you earned a hot lunch.', [(267, 'Иди, Федь, на кухню. Подхарчи.')], ''),
    ('fedya', 'Спасибо, шеф, я очень голодный!', 'Thank you, Chef, I am very hungry!', [], ''),
]
WALK = [
    (0, None, ["'Fedya, well, how are things at the competitors?' Now we can focus on the words: ", ('barinov', 'у'), ('barinov', 'конкурентов'), " means 'at the competitors'."]),
    (1, None, ["'Chef, our scout has returned with a report.' Now we can consider the sentence: ", ('fedya', 'вернулся'), ' is returned.']),
    (2, None, ["'Tell me faster. Did you go inside?' We can consider the sentence: ", ('barinov', 'быстрее'), ' means faster.']),
    (3, None, ["'Yes, I looked at their new hall.' We will inspect the words: ", ('fedya', 'новый'), ' is new.']),
    (4, None, ["'And how is it? Does the interior look nice?' Let us examine the dialogue: ", ('barinov', 'И'), ('barinov', 'как'), " means 'and how'."]),
    (5, None, ["'To tell the truth, the interior is so-so.' Let's examine the sentence: ", ('fedya', 'так'), ('fedya', 'себе'), " means 'so-so'."]),
    (6, None, ["'And what is going on with the guests?' Let's consider the sentence: ", ('barinov', 'А'), ('barinov', 'что'), " means 'and what'."]),
    (7, None, ["'In the hall there is silence, plenty of empty seats.' We can consider the dialogue: ", ('fedya', 'полно'), ' means plenty.']),
    (8, None, ["'You see what I was talking about!' We will consider this part: ", ('barinov', 'Ты'), ('barinov', 'видишь'), " means 'you see'."]),
    (9, None, ["'We do not need to change anything yet.' We can break down this part: ", ('barinov', 'ничего'), ' means nothing.']),
    (10, None, ["'Chef, can I have something to eat?' Let's consider the dialogue: ", ('fedya', 'поесть'), ' means to eat.']),
    (11, None, ["'Go to the kitchen, you earned a hot lunch.' Now let's consider the sentence: ", ('barinov', 'Иди'), ' means go.']),
    (12, None, ["'Thank you, Chef, I am very hungry!' Now let's break down the phrase: ", ('fedya', 'очень'), ' means very.']),
]
