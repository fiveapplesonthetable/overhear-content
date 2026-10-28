# Authoring module for kukhnya-s02e02-scene-01.
ID = 'kukhnya-s02e02-scene-01'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 2
SCENE = 1
TITLE = 'Новый грузчик  (The New Loader)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'suslan': 'Суслан', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.02'
SOURCE_FILE = 'sources/kukhnya/s02/e02.ru.dual.srt'
INTRO = "Focused on the new loader, Timur brings fish instead of what the Chef ordered. He also introduces his nephew Suslan, who is a law student. Let's listen closely to the staff and Chef Viktor's exchange in Russian first, and then walk through each line together."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Timur brings fish instead of what the Chef ordered. He also introduces his nephew Suslan, who is a law student. Next time you watch the episode, listen for the Russian expressions for 'matter' and 'well' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Дела хорошо пошли?', 'Business is going well?', [(1, 'дела хорошо пошли,')], ''),
    ('timur', 'Много работы.', 'A lot of work.', [(2, 'Много работы, много стресса.')], ''),
    ('timur', 'Я взял племянника.', 'I hired my nephew.', [(3, 'Вот решил племянника на работу взять.')], ''),
    ('timur', 'Его зовут Суслан.', 'His name is Suslan.', [(6, 'Суслан.')], ''),
    ('barinov', 'Что ты привёз?', 'What did you bring?', [(8, 'Что ты там привез?')], ''),
    ('timur', 'Суслан, разгружай.', 'Suslan, unload.', [(10, 'Иди давай разгружай.')], ''),
    ('suslan', 'Я нанимался водителем.', 'I was hired as a driver.', [(10, 'я к вам водителем нанимался,')], ''),
    ('suslan', 'А не грузчиком.', 'Not as a loader.', [(11, 'а не грузчиком.')], ''),
    ('timur', 'Вот скотина.', 'What a bastard.', [(12, 'Вот скотина, а.')], ''),
    ('timur', 'Вот ваша рыба, шеф.', 'Here is your fish, Chef.', [(13, 'Вот, шеф-брат, как просил рыбу?')], ''),
    ('barinov', 'Зачем мне рыба?', 'Why do I need fish?', [(15, 'На кой черт мне столько рыбы?')], ''),
    ('barinov', 'Увози обратно.', 'Take it back.', [(17, 'а это увози обратно.')], ''),
]
WALK = [
    (0, None, "'Business is going well?' Barinov greets his supplier Timur and asks if business is going well."),
    (1, None, "'A lot of work.' Timur replies that he has his hands full with work lately."),
    (2, None, "'I hired my nephew.' Because he is so busy, Timur explains that he hired his nephew to help."),
    (3, None, "'His name is Suslan.' He introduces the young man as Suslan."),
    (4, None, "'What did you bring?' Looking at the crates, Viktor asks what supplies Timur brought today."),
    (5, None, "'Suslan, unload.' Timur turns and orders his nephew to unload the van."),
    (6, None, "'I was hired as a driver.' Suslan protests that he took the job to be a driver."),
    (7, None, "'Not as a loader.' He insists he did not sign up to carry heavy boxes."),
    (8, None, "'What a bastard.' Annoyed by his nephew's attitude, Timur mutters an insult under his breath."),
    (9, None, "'Here is your fish, Chef.' Carrying the crate himself, Timur presents a batch of fish to the chef."),
    (10, None, "'Why do I need fish?' Barinov stares at the crate and asks why on earth he would need fish."),
    (11, None, "'Take it back.' Viktor did not order fish and tells Timur to haul it right back."),
]
