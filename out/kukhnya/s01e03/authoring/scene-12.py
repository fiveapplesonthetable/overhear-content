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
    ('barinov', 'Тут совсем мало мяса для гостей.', 'There is completely little meat here for the guests.', [(255, 'маленький')], ''),
    ('lyova', 'Что же нам теперь с ним делать?', 'What should we do with it now?', [(256, 'оказались')], ''),
    ('barinov', 'Приготовь специальный соус и красивый гарнир.', 'Prepare a special sauce and a beautiful side dish.', [(255, 'Чего он')], ''),
    ('lyova', 'Хорошо, шеф, я всё быстро сделаю.', 'Alright, chef, I will do everything quickly.', [(256, 'так это')], ''),
    ('barinov', 'Гости должны быть довольны нашим банкетом!', 'The guests must be pleased with our banquet!', [(255, 'такой')], ''),
]
WALK = [
    (0, None, '\'Lyova, show me this goose.\' The command for "show" is friendly. "This goose" has the animate ending, "-ya".'),
    (1, None, '\'Here it is, chef, I already finished.\' "Here it is" is "vot on", pointing at the bird. "Finished" is a man\'s past, with "-l".'),
    (2, None, '\'Why is it so strangely small?\' "Chego" is a casual "why", close to "what for". "Strangely" is "strange" with the how-word ending.'),
    (3, None, '\'It turned out like that because of feathers.\' "Iz-za" means "because of", usually for something bad. "Feathers" is a plural with "-yev" on the end.'),
    (4, None, '\'It turned out that it has very thick feathers.\' "Okazalos\'" is "it turned out", a very useful sentence opener. "At him" is "u nego", the "have" pattern.'),
    (5, None, '\'We bought a huge bird after all!\' "Zhe" gives the "after all". "Huge" is the same word as "ogromnoye" in "huge thanks".'),
    (6, None, '\'I was surprised myself when I was plucking it.\' "Surprised" ends in "-sya", a little "self", since you surprise yourself. "Plucking" is a word for taking off feathers.'),
    (7, None, '\'There is completely little meat here for the guests.\' "Little" is followed by "meat" in the "of" form, "myasa". "For the guests" has the "for" ending.'),
    (8, None, '\'What should we do with it now?\' "To us to do" is the pattern for "what should we do". "With it" adds an "n" to "it".'),
    (9, None, '\'Prepare a special sauce and a beautiful side dish.\' The chef gives a command with "prepare" at the start. "Side dish" is borrowed from French.'),
    (10, None, '\'Alright, chef, I will do everything quickly.\' The "s-" in front of "do" makes it "get it done". Lyova sounds eager.'),
    (11, None, '\'The guests must be pleased with our banquet!\' "Must be" is two short words. "Pleased with" takes the "with" ending, so "banquet" ends in "-om".'),
]
