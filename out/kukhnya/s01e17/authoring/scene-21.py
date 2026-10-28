# Authoring module for kukhnya-s01e17-scene-21.
ID = 'kukhnya-s01e17-scene-21'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 21
TITLE = 'Конец конфликта  (End of the Conflict)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'The big row is over. In the dining room, Vika and the staff apologise to Max for ruining what they thought was his birthday, and Barinov wants to be sure the matter is closed. Here are the apologies in Russian first.'
OPENER = "Let's take the apologies one at a time."
TRANSITION = 'Now the apologies again, without the pauses.'
OUTRO = 'Everyone has made up, at least until the next mistake. "Mir" is a good word to keep: it means both peace and the world. See you next time!'
CLOSING = ('vika', 'До завтра, Макс!')
STORY = [
    ('vika', 'Максим, прости нас, пожалуйста.', 'Maxim, please forgive us.', [(321, 'Максим, прости нас, пожалуйста, что испортили тебе праздник.')], ''),
    ('vika', 'Мы испортили тебе отличный праздник.', 'We ruined a great holiday for you.', [(321, 'что испортили тебе праздник')], ''),
    ('max', 'Я не сержусь на вас.', 'I am not angry at you.', [], ''),
    ('vika', 'Прости их, пожалуйста.', 'Please forgive them.', [(322, 'Прости их, пожалуйста.')], ''),
    ('barinov', 'Ну и меня тоже прости.', 'Well and forgive me too.', [(323, 'Ну и меня.')], ''),
    ('barinov', 'Так, всё? Конфликт закончился?', 'So, is that all? The conflict is over?', [(323, 'Так все?'), (324, 'Конфликт исчерпан?')], ''),
    ('max', 'Да, шеф, конфликт закончился.', 'Yes, chef, the conflict is over.', [(324, 'Конфликт исчерпан')], ''),
    ('barinov', 'Но только пока кто-то снова не ошибётся.', 'But only until someone makes a mistake again.', [(324, 'Временно, пока кто-нибудь снова не накосячит.')], ''),
    ('vika', 'Мы все хотим мира на кухне.', 'We all want peace in the kitchen.', [], ''),
    ('barinov', 'Мир на кухне — это главное.', 'Peace in the kitchen is key.', [], ''),
    ('max', 'Спасибо всем за добрые слова.', 'Thank you all for the kind words.', [], ''),
    ('vika', 'Теперь мы можем спокойно работать.', 'Now we can work calmly.', [], ''),
    ('max', 'Я очень рад, что мы помирились.', 'I am very glad that we reconciled.', [], ''),
]
WALK = [
    (0, None, '\'Maksim, please forgive us.\' "Prosti" is "forgive" said to one person. Vika uses his full name to sound serious.'),
    (1, None, '\'We ruined a great celebration for you.\' "Isportili" means "spoiled". "Tebe", for you, says whose celebration it was.'),
    (2, None, '\'I\'m not angry with you.\' "Serzhus na vas" is "I\'m angry at you", using "na", onto.'),
    (3, None, '\'Please forgive them.\' Now she asks on behalf of the staff: "ikh" means them.'),
    (4, None, '\'Well, and forgive me too.\' "Menya" means me. Barinov tacks himself on at the end.'),
    (5, None, '\'So, is that it? Is the conflict over?\' "Tak, vsyo?" is literally "so, all?", meaning "are we done?".'),
    (6, None, '\'Yes, chef, the conflict is over.\' "Zakonchilsya", ended, is related to "konets", end.'),
    (7, None, '\'But only until somebody makes a mistake again.\' "Poka" with "ne" means "until". "Oshibyotsya" is related to "oshibka", a mistake.'),
    (8, None, '\'We all want peace in the kitchen.\' "Mir" means both peace and world, and here it becomes "mira".'),
    (9, None, '\'Peace in the kitchen is the main thing.\' "Glavnoe", the main thing, is related to "glava", head.'),
    (10, None, '\'Thanks to everyone for the kind words.\' "Vsem" means "to everyone". "Za dobrye slova" is "for the kind words".'),
    (11, None, '\'Now we can work in peace.\' "Mozhem" is "we can", and "spokoyno" means without trouble.'),
    (12, None, '\'I\'m really glad we made up.\' "Pomirilis", made peace with each other, is built on "mir" too.'),
]
