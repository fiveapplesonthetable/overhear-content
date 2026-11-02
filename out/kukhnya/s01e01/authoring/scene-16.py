# Authoring module for kukhnya-s01e01-scene-16.
ID = 'kukhnya-s01e01-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 16
TITLE = 'Новое меню  (The New Menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'sasha': 'Саша', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "In the corridor of Claude Monet, the art director, Vika, catches up with the waitress, Sasha. She wants to know if the chef has seen her request for a new menu, and what he said. Here's their talk in Russian first."
OPENER = "Let's go through it line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Vika decides to deal with the chef herself, which is typical of her. You\'ve heard Russian for "I\'ll go myself", and a handy way to say "be careful".'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Саша, ты передала шефу мою важную просьбу?', 'Sasha, did you pass my important request to the chef?', [(146, 'ты сказал у шефа')], ''),
    ('sasha', 'Да, Виктория Сергеевна, я всё ему сказала.', 'Yes, Viktoriya Sergeyevna, I told him everything.', [(147, 'Я сказала')], ''),
    ('vika', 'Ты сказала, что я просила новое меню?', 'Did you say that I asked for the new menu?', [(146, 'что я просила новое меню')], ''),
    ('sasha', 'Да, я лично напомнила шефу об этом.', 'Yes, I personally reminded the chef about this.', [(147, 'Я сказала')], ''),
    ('vika', 'И какой был его ответ на это?', 'And what was his answer to that?', [(147, 'Понятно')], ''),
    ('sasha', 'Он только громко закричал на всю кухню.', 'He only loudly shouted at the entire kitchen.', [(148, 'Но и')], ''),
    ('vika', 'Понятно, он опять совершенно не слушает меня.', 'I see, he again is completely not listening to me.', [(147, 'Понятно')], ''),
    ('sasha', 'Шеф сегодня с самого утра очень сердитый.', 'The chef has been very angry since this morning.', [(148, 'Но и')], ''),
    ('vika', 'Нам срочно нужно обновить список наших блюд.', 'We urgently need to update the list of our dishes.', [(146, 'новое меню')], ''),
    ('sasha', 'Гости в зале уже спрашивают новые десерты.', 'Guests in the dining room are already asking for new desserts.', [(146, 'новое меню')], ''),
    ('vika', 'Я сама сейчас пойду и поговорю с ним.', 'I will go myself right now and talk to him.', [(148, 'Но и')], ''),
    ('sasha', 'Будьте очень осторожны, шеф в плохом настроении.', 'Be very careful, the chef is in a bad mood.', [(148, 'Но и')], ''),
    ('vika', 'Ничего, порядок в ресторане важнее его капризов!', 'That is fine, order in the restaurant is more important than his whims!', [(148, 'Но и')], ''),
]
WALK = [
    (0, None, ['\'Sasha, did you pass my important request to the chef?\' ', ('vika', "Передала"), ' ends in "-la" because Sasha is a woman. ', ('vika', "просьбу"), ', a request, comes from ', ('vika', "просьбу"), ', to ask, so ', ('vika', "просьбу"), ' is "request" as the object.']),
    (1, None, ['\'Yes, Viktoriya Sergeyevna, I told him everything.\' Sasha uses Vika\'s full name and father\'s name, as Max did with Nagiyev. ', ('sasha', "Сказала"), ' is "said", and the -a marks a woman, and ', ('sasha', "ему"), ' is "to him".']),
    (2, None, ['\'Did you say that I asked for the new menu?\' ', ('vika', "Просила"), ' is "asked", also with -la for Vika. ', ('vika', "Новое меню"), ' is "new menu", and ', ('vika', "меню"), ' never changes.']),
    (3, None, ['\'Yes, I personally reminded the chef about this.\' ', ('sasha', "Напомнила"), ' has ', ('sasha', "напомнила"), ', to remember, inside it, so "reminded" is "made remember". ', ('sasha', "Об этом"), ' is "about this", and ', ('sasha', "о"), ' becomes ', ('sasha', "об"), ' before a vowel.']),
    (4, None, ['\'And what was his answer to that?\' ', ('vika', "Его ответ"), ' is "his answer", and ', ('vika', "его"), ' never changes, unlike ', ('vika', "его"), ' and ', ('vika', "его"), '. ', ('vika', "Был"), ' is masculine "was", because ', ('vika', "ответ"), ' is masculine.']),
    (5, None, ['\'He only loudly shouted at the entire kitchen.\' ', ('sasha', "Закричал"), ' is ', ('sasha', "закричал"), ', to shout, with "za-" for "burst into". ', ('sasha', "Громко"), ' is "loudly", and ', ('sasha', "на всю кухню"), ' is "across the whole kitchen".']),
    (6, None, ['\'I see, he again is completely not listening to me.\' ', ('vika', "Слушает"), ' takes ', ('vika', "меня"), ' directly, with no "to". ', ('vika', "Совершенно"), ' is "completely", and ', ('vika', "опять"), ' is "again".']),
    (7, None, ['\'The chef has been very angry since this morning.\' ', ('sasha', "С самого утра"), ' is "from the very morning". ', ('sasha', "Сердитый"), ', angry, comes from ', ('sasha', "сердитый"), ', the heart.']),
    (8, None, ['\'We urgently need to update the list of our dishes.\' Russian says "to us it\'s needed": ', ('vika', "Нам"), ', with ', ('vika', "Нам"), ' in the "to" form. ', ('vika', "Обновить"), ', to update, has ', ('vika', "нов"), ', new, in the middle, and in ', ('vika', "наших блюд"), ', of our dishes, ', ('vika', "блюд"), ' loses its last vowel.']),
    (9, None, ['\'Guests in the dining room are already asking for new desserts.\' ', ('sasha', "Спрашивают"), ' is "they ask", and here it\'s "ask for": Russian takes the desserts straight after the verb, with no "for". ', ('sasha', "В зале"), ' is "in the hall", the dining room.']),
    (10, None, ['\'I will go myself right now and talk to him.\' ', ('vika', "Сама"), ' is the feminine ', ('vika', "сам"), ', "myself" or "herself". ', ('vika', "Пойду"), ' and ', ('vika', "поговорю"), ' are two futures, one word each. ', ('vika', "С ним"), ' is "with him", and the "n" is added after ', ('vika', "с"), '.']),
    (11, None, ['\'Be very careful, the chef is in a bad mood.\' ', ('sasha', "Будьте"), ' is the formal command "be". ', ('sasha', "Осторожны"), ' ends in a plural "-y" because Sasha speaks to Vika as ', ('sasha', "Будьте"), '. ', ('sasha', "В плохом настроении"), ' is "in a bad mood".']),
    (12, None, ['\'That is fine, order in the restaurant is more important than his whims!\' ', ('vika', "Ничего"), ' is "never mind" here. ', ('vika', "Важнее"), ' is "more important", sharing the "-eye" of "faster". ', ('vika', "Каприз"), ' is borrowed from French.']),
]