# Authoring module for kukhnya-s01e03-scene-12.
ID = 'kukhnya-s01e03-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 12
TITLE = 'Маленький гусь  (The Little Goose)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "The roast goose is ready, and Chef Barinov comes to look at it. It's tiny, much smaller than he expected. The cooks have to decide what to do about it before the banquet. Here is the conversation in Russian first."
OPENER = "Now let's see how small the goose is."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'A tiny goose, a big banquet, and a chef who needs a plan. If you remember anything, take "iz-za", "because of".'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Лёва, покажи мне этого гуся.', 'Lyova, show me this goose.', [(255, 'он такой')], ''),
    ('lyova', 'Вот он, шеф, я уже закончил.', 'Here it is, chef, I already finished.', [(255, 'Чего он')], ''),
    ('barinov', 'Чего он такой странно маленький?', 'Why is it so strangely small?', [(255, 'Чего он такой маленький')], ''),
    ('lyova', 'Это из-за перьев так получилось.', 'It turned out like that because of feathers.', [(256, 'так это перья')], ''),
    ('lyova', 'Оказалось, что у него очень густые перья.', 'It turned out that it has very thick feathers.', [(256, 'перья оказались')], ''),
    ('barinov', 'Мы же купили огромную птицу!', 'We bought a huge bird after all!', [(255, 'маленький')], ''),
    ('lyova', 'Я сам удивился, когда ощипывал его.', 'I was surprised myself when I was plucking it.', [(257, 'когда')], ''),
    ('barinov', 'Тут совсем мало мяса для гостей.', 'There is very little meat here for the guests.', [(255, 'маленький')], ''),
    ('lyova', 'Что же нам теперь с ним делать?', 'What should we do with it now?', [(256, 'оказались')], ''),
    ('barinov', 'Приготовь специальный соус и красивый гарнир.', 'Prepare a special sauce and a beautiful side dish.', [(255, 'Чего он')], ''),
    ('lyova', 'Хорошо, шеф, я всё быстро сделаю.', 'Alright, chef, I will do everything quickly.', [(256, 'так это')], ''),
    ('barinov', 'Гости должны быть довольны нашим банкетом!', 'The guests must be pleased with our banquet!', [(255, 'такой')], ''),
]
WALK = [
    (0, None, '\'Lyova, show me this goose.\' "Pokazhi" is the "ty" command "show". "Etogo gusya", this goose, takes the creature\'s object endings, -ogo and -ya.'),
    (1, None, '\'Here it is, chef, I already finished.\' "Vot on" is "here he is", because "gus\'" is masculine. "Zakonchil", finished, ends in -l for a man.'),
    (2, None, '\'Why is it so strangely small?\' "Chego" is spoken Russian for "why". "Stranno", strangely, is the adverb of "strannyy", strange, and "malen\'kiy" is "small".'),
    (3, None, '\'It turned out like that because of feathers.\' "Iz-za" is "because of", usually for something bad. "Per\'ya", feathers, becomes "per\'yev" after it, and "tak poluchilos\'" is "so it turned out".'),
    (4, None, '\'It turned out that it has very thick feathers.\' "Okazalos\'", it turned out, is a handy way to open news. "U nego" is "at him", the goose\'s "have", and "gustyye" is "thick".'),
    (5, None, '\'We bought a huge bird after all!\' "Zhe" gives the "after all". "Kupili" is "we bought", and "ogromnuyu ptitsu", a huge bird, ends in -u as the thing bought.'),
    (6, None, '\'I was surprised myself when I was plucking it.\' "Sam udivilsya" is "myself was surprised", with -sya on the verb. "Oshchipyval", was plucking, comes from "shchipat\'", to pinch.'),
    (7, None, '\'There is very little meat here for the guests.\' "Malo", little, is followed by "myasa", the "of" form of "myaso". "Dlya gostey" is "for the guests".'),
    (8, None, '\'What should we do with it now?\' "Chto nam delat\'?" is "what to us to do?". "S nim", with him, gets the added "n" after "s".'),
    (9, None, '\'Prepare a special sauce and a beautiful side dish.\' "Prigotov\'" is the command "prepare". "Sous" and "garnir", side dish, both came from French.'),
    (10, None, '\'Alright, chef, I will do everything quickly.\' "Sdelayu", I\'ll do, is the finished partner of "delayu", so it means "I\'ll get it done". "Bystro" is "quickly".'),
    (11, None, '\'The guests must be pleased with our banquet!\' "Dolzhny byt\'" is "must be". "Dovol\'ny" means "pleased", and what you\'re pleased with takes -om: "nashim banketom".'),
]
