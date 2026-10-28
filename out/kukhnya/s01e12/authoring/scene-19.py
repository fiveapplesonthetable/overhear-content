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
INTRO = 'In the kitchen back room of Claude Monet, cook Fedya returns from scouting out their new rival restaurant. Relieved to hear that the competitor is empty and quiet, Chef Viktor happily concludes that Claude Monet does not need any changes to stay on top. Listen to their conversation in Russian first, then we will break down each line in English.'
OPENER = "Now let's go back through the exchange around The Scout's Report line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In the back room, cook Fedya returns from scouting the rival restaurant and reports to Chef Viktor that the competitor is empty, confirming that Claude Monet needs no changes. Next time you watch the episode, listen for the Russian expressions for 'to tell' and 'for now' — you will catch every word right away. See you next time!"
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
    (0, None, "'Fedya, well, how are things at the competitors' Barinov eagerly asks Fedya for news about the rival restaurant."),
    (1, None, "'Chef, our scout has returned with a report.' Fedya jokingly calls himself a spy returning with news."),
    (2, None, "'Tell me faster. Did you go inside?' Barinov tells him to hurry up and asks if he went in."),
    (3, None, "'Yes, I looked at their new hall.' Fedya confirms he checked out the interior of the new place."),
    (4, None, "'To tell the truth, the interior is so-so.' Fedya admits that the new restaurant does not look very impressive inside."),
    (5, None, "'In the hall there is silence, plenty of empty seats.' Fedya reports that the place is quiet and completely empty."),
    (6, None, "'You see what I was talking about!' Barinov feels vindicated and says this proves he was right all along."),
    (7, None, "'We do not need to change anything yet.' Barinov decides they do not need to make any changes to their own restaurant."),
    (8, None, "'Go to the kitchen, you earned a hot lunch.' Barinov rewards Fedya with a hot meal for his spying work."),
    (9, None, "'Thank you, Chef, I am very hungry!' Fedya thanks him and says he is starving."),
]
