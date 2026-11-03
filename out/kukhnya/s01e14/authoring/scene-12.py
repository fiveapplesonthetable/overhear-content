# Authoring module for kukhnya-s01e14-scene-12.
ID = 'kukhnya-s01e14-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 12
TITLE = 'Слёзы на кухне  (Tears in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'In the kitchen, pastry chef Louis is sobbing again, and Barinov has no patience for it. Orders are waiting. Listen to it in Russian.'
OPENER = 'Once more, slowly.'
TRANSITION = 'Here is the kitchen scene again.'
OUTRO = "Louis gets back to work, and Barinov yells at the rest of the kitchen to do the same. Barking 'we work!' is the chef's way of saying 'get on with it'. Later."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Луи, почему ты опять горько плачешь?', 'Louis, why are you crying bitterly again?', [(175, 'Луи.')], ''),
    ('louis', 'Шеф, у меня случилась страшная драма.', 'Chef, a terrible drama happened to me.', [(176, 'свой плач')], ''),
    ('barinov', 'Прекрати этот глупый шум прямо сейчас!', 'Stop this foolish noise right now!', [(176, 'Прекрати, пожалуйста')], ''),
    ('louis', 'Моё нежное сердце разбито на куски.', 'My tender heart is broken into pieces.', [], ''),
    ('barinov', 'Быстро вытри слёзы и делай десерты.', 'Quickly wipe your tears and make desserts.', [(176, 'приступай, пожалуйста,'), (177, 'к десертам.')], ''),
    ('louis', 'Я не могу сейчас печь сладкие пирожные.', 'I cannot bake sweet cakes right now.', [], ''),
    ('barinov', 'Наши важные гости давно ждут десерты!', 'Our important guests have been waiting for desserts for a long time!', [], ''),
    ('louis', 'Хорошо, шеф, я начну готовить кремы.', 'All right, chef, I will start making creams.', [], ''),
    ('barinov', 'И прекрати свои постоянные пустые жалобы.', 'And stop your constant empty complaints.', [], ''),
    ('barinov', 'Эй, повара, почему вы все стоите?', 'Hey, cooks, why are you all standing around?', [(177, 'Что уставились')], ''),
    ('louis', 'Мы уже начинаем быстро делать заказы.', 'We are already starting to prepare orders quickly.', [], ''),
    ('barinov', 'Живее, лентяи, начинаем дружно работать!', 'Look lively, slackers, let us all start working!', [(178, 'Работаем!')], ''),
    ('barinov', 'Работаем быстро, гости ждут свои заказы!', 'Work quickly, guests are waiting for their orders!', [(178, 'Работаем!')], ''),
]
WALK = [
    (0, None, ["'Louis, why are you crying bitterly again?' To say bitterly, use ", ('barinov', 'горько'), '. And to say again, use ', ('barinov', 'опять'), '.']),
    (1, None, ["'Chef, a terrible drama happened to me.' To say happened, use ", ('louis', 'случилась'), ", which ends with an 'a' sound to match the feminine word drama. And 'to me' is ", ('louis', 'у'), ('louis', 'меня'), '.']),
    (2, None, ["'Stop this foolish noise right now!' To say stop, use ", ('barinov', 'Прекрати'), '. Noise is ', ('barinov', 'шум'), ', and this foolish noise is ', ('barinov', 'этот'), ('barinov', 'глупый'), ('barinov', 'шум'), '.']),
    (3, None, ["'My tender heart is broken into pieces.' To say 'is broken', use ", ('louis', 'разбито'), '. And into pieces is ', ('louis', 'на'), ('louis', 'куски'), '.']),
    (4, None, ["'Quickly wipe your tears and make desserts.' Tears are ", ('barinov', 'слёзы'), '. To say wipe, use ', ('barinov', 'вытри'), ', and to tell someone to make something, use ', ('barinov', 'делай'), '.']),
    (5, None, ["'I cannot bake sweet cakes right now.' To say to bake, use ", ('louis', 'печь'), '. A small cake or pastry is ', ('louis', 'пирожные'), '.']),
    (6, None, ["'Our important guests have been waiting for desserts for a long time!' To say 'have been waiting for a long time', use ", ('barinov', 'давно'), ('barinov', 'ждут'), '.']),
    (7, None, ["'All right, chef, I will start making creams.' To say 'I will start', use ", ('louis', 'начну'), '. And to say making or preparing, use ', ('louis', 'готовить'), '.']),
    (8, None, ["'And stop your constant empty complaints.' A complaint is ", ('barinov', 'жалобы'), ". To say 'your own', use ", ('barinov', 'свои'), ', referring back to the person being told off.']),
    (9, None, ["'Hey, cooks, why are you all standing around?' Cooks are ", ('barinov', 'повара'), ". And 'you all' is ", ('barinov', 'вы'), ('barinov', 'все'), '.']),
    (10, None, ["'We are already starting to prepare orders quickly.' To say 'we are starting', use ", ('louis', 'начинаем'), '. To make orders is ', ('louis', 'делать'), ('louis', 'заказы'), '.']),
    (11, None, ["'Look lively, slackers, let us all start working!' To say 'look lively', use ", ('barinov', 'Живее'), '. And all together or united is ', ('barinov', 'дружно'), '.']),
    (12, None, ["'Work quickly, guests are waiting for their orders!' To say 'we work' as a command, use ", ('barinov', 'Работаем'), '. To say their own orders, use ', ('barinov', 'свои'), ('barinov', 'заказы'), '.']),
]
