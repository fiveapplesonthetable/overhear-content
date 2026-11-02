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
OUTRO = 'A tiny goose, a big banquet, and a chef who needs a plan. If you remember anything, take the phrase for "because of".'
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
    (0, None, [
        "'Lyova, show me this goose.' In Russian, ",
        ('barinov', 'покажи'),
        " is the word for the informal instruction to 'show'. ",
        ('barinov', 'этого гуся.'),
        " translates to 'this goose', and takes the object shape."
    ]),
    (1, None, [
        "'Here it is, chef, I already finished.' For this line, ",
        ('lyova', 'Вот он,'),
        " literally translates to 'here he is', because the word for goose is a 'he' word. ",
        ('lyova', 'закончил.'),
        " means 'finished', and ends with an 'L' sound for a man."
    ]),
    (2, None, [
        "'Why is it so strangely small?' Notice that ",
        ('barinov', 'Чего'),
        " translates to 'why' in spoken language. ",
        ('barinov', 'странно'),
        " is the word for 'strangely', coming from 'strange', and ",
        ('barinov', 'маленький?'),
        " is 'small'."
    ]),
    (3, None, [
        "'It turned out like that because of feathers.' As you hear, ",
        ('lyova', 'из-за'),
        " translates to 'because of', often used for problems. ",
        ('lyova', 'перьев'),
        " is the 'of' shape for feathers, and ",
        ('lyova', 'так получилось.'),
        " is literally 'so it turned out'."
    ]),
    (4, None, [
        "'It turned out that it has very thick feathers.' Another detail, ",
        ('lyova', 'Оказалось,'),
        " meaning 'it turned out', is a great way to share news. ",
        ('lyova', 'у него'),
        " literally translates to 'at him' to show possession, and ",
        ('lyova', 'густые'),
        " is the word for 'thick'."
    ]),
    (5, None, [
        "'We bought a huge bird after all!' Another detail, ",
        ('barinov', 'же'),
        " gives the 'after all' feeling. ",
        ('barinov', 'купили'),
        " is the word for 'we bought', and ",
        ('barinov', 'огромную птицу!'),
        " meaning 'a huge bird', changes its ending because it is the thing being bought."
    ]),
    (6, None, [
        "'I was surprised myself when I was plucking it.' Let us review ",
        ('lyova', 'сам удивился,'),
        " literally translates to 'myself was surprised', with a self-reflective ending on the action word. ",
        ('lyova', 'ощипывал'),
        " meaning 'was plucking', is built from the action to pinch."
    ]),
    (7, None, [
        "'There is very little meat here for the guests.' What happens here, ",
        ('barinov', 'мало'),
        " the word for 'little', is followed by ",
        ('barinov', 'мяса'),
        " the 'of' shape of meat. ",
        ('barinov', 'для гостей.'),
        " translates to 'for the guests'."
    ]),
    (8, None, [
        "'What should we do with it now?' Observe how ",
        ('lyova', 'Что же нам'),
        ' mixed with ',
        ('lyova', 'делать?'),
        " literally translates to 'what to us to do?'. ",
        ('lyova', 'с ним'),
        " meaning 'with him', gets an added 'n' sound after the word for 'with'."
    ]),
    (9, None, [
        "'Prepare a special sauce and a beautiful side dish.' As you hear, ",
        ('barinov', 'Приготовь'),
        " is the word for the instruction to 'prepare'. Both ",
        ('barinov', 'соус'),
        ' and ',
        ('barinov', 'гарнир.'),
        " meaning 'side dish', are built from French words."
    ]),
    (10, None, [
        "'Alright, chef, I will do everything quickly.' Focusing here, ",
        ('lyova', 'сделаю.'),
        " translates to 'I will do', and is the finished version of the action, meaning 'I will get it done'. ",
        ('lyova', 'быстро'),
        " is the word for 'quickly'."
    ]),
    (11, None, [
        "'The guests must be pleased with our banquet!' Check out how ",
        ('barinov', 'должны быть'),
        " translates to 'must be'. ",
        ('barinov', 'довольны'),
        " is the word for 'pleased', and what you are pleased with takes a special shape: ",
        ('barinov', 'нашим банкетом!')
    ]),
]
