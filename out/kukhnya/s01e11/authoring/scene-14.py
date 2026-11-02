# Authoring module for kukhnya-s01e11-scene-14.
ID = 'kukhnya-s01e11-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 14
TITLE = 'Подача для критика  (Serving the Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "The remade salad is ready, and Max carries it out to the lady at table seven. Vika meets him halfway with bad news: she is no longer sure the lady is the critic. We'll hear it through once before I say a word about it."
OPENER = "I'll take you through it now."
TRANSITION = 'Everything again, from the beginning.'
OUTRO = "Max turns round with the plate, and Vika hurries him along. A critic can't be kept waiting, even a possible one. Until then."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Вика, не паникуй, я уже несу горячее блюдо.', 'Vika, do not panic, I am already carrying the hot dish.', [(166, 'Все, все, не паникуй, я уже отдаю блюдо')], ''),
    ('vika', 'Ты уверен, что несёшь его правильному гостю?', 'Are you sure you are carrying it to the right guest?', [(166, 'твоему критику')], ''),
    ('max', 'Я отдаю этот шедевр твоему главному критику.', 'I am delivering this masterpiece to your chief critic.', [(166, 'я уже отдаю блюдо твоему критику')], ''),
    ('vika', 'Молодец, только я уже не уверена в ней.', 'Well done, only I am no longer sure about her.', [(167, 'Молодец. Только я уже не уверена, что это она')], ''),
    ('max', 'Что изменилось за эти пять коротких минут?', 'What changed during these five short minutes?', [(167, 'что это она')], ''),
    ('vika', 'Кажется, настоящий критик сидит у другого окна.', 'It seems the real critic is sitting by the other window.', [(167, 'я уже не уверена')], ''),
    ('max', 'А вот это уже твои личные проблемы!', 'And that is already your personal problem!', [(168, 'А это уже твои проблемы')], ''),
    ('vika', 'Подожди секунду, верни дорогую тарелку назад.', 'Wait a second, bring the expensive plate back.', [(168, 'твои проблемы')], ''),
    ('max', 'Гостья уже ждёт и смотрит прямо сюда.', 'The guest is already waiting and looking right here.', [(170, 'Девушка, можно вас?')], ''),
    ('vika', 'Скажи ей, что это особый подарок шефа.', 'Tell her that this is a special gift from the Chef.', [(171, 'Сейчас к вам подойдет')], ''),
    ('max', 'Я улыбнусь и скажу самые вежливые слова.', 'I will smile and say the most polite words.', [(171, 'подойдет ваш официант')], ''),
    ('vika', 'Иди скорее, не заставляй важного человека ждать.', 'Go quickly, do not make an important person wait.', [(171, 'Сейчас к вам подойдет')], ''),
]
WALK = [
    (0, None, ["'Vika, do not panic, I am already carrying the hot dish.' The phrase ", ('max', 'не'), ('max', 'паникуй'), ' turns panic into a verb. ', ('max', 'несу'), ' means I am carrying, and ', ('max', 'горячее'), ('max', 'блюдо'), ' is a hot dish.']),
    (1, None, ["'Are you sure you are carrying it to the right guest?' The term ", ('vika', 'уверен'), ' ends bare because Max is a man, and a woman would add an ending. ', ('vika', 'правильному'), ('vika', 'гостю'), ' means to the right guest.']),
    (2, None, ["'I am delivering this masterpiece to your chief critic.' Now we can consider the phrase: ", ('max', 'шедевр'), ' is borrowed from French, the word Max used before about artists signing their work. ', ('max', 'твоему'), ('max', 'главному'), ('max', 'критику'), ' changes the ending on every word to point to the critic.']),
    (3, None, ["'Well done, only I am no longer sure about her.' We can break down the words: ", ('vika', 'Молодец'), ' is praise for anyone, men or women. ', ('vika', 'уверена'), ('vika', 'в'), ('vika', 'ней'), ' means sure in her.']),
    (4, None, ["'What changed during these five short minutes?' The term ", ('max', 'изменилось'), ' for changed takes a neutral ending because it follows the question word what. The expression includes ', ('max', 'пять'), ' for five.']),
    (5, None, ["'It seems the real critic is sitting by the other window.' We will inspect the dialogue: ", ('vika', 'Кажется'), ' means it seems. ', ('vika', 'у'), ('vika', 'другого'), ('vika', 'окна'), ' means by the other window. Vika has a new theory.']),
    (6, None, ["'And that is already your personal problem!' We will focus on the phrase: ", ('max', 'личные'), ' means personal, from the family of personally that the chef used earlier. ', ('max', 'твои'), ('max', 'личные'), ('max', 'проблемы'), ' means your personal problems.']),
    (7, None, ["'Wait a second, bring the expensive plate back.' The command ", ('vika', 'верни'), ' means give back. ', ('vika', 'дорогую'), ' means both dear and expensive. ', ('vika', 'Подожди'), ' is the command to wait.']),
    (8, None, ["'The guest is already waiting and looking right here.' Let's break down this line: ", ('max', 'сюда'), ' means to here, the same word Kostya used earlier. ', ('max', 'Гостья'), ' is the woman guest again.']),
    (9, None, ["'Tell her that this is a special gift from the Chef.' The phrase ", ('vika', 'подарок'), ('vika', 'шефа'), ' means gift of the chef, with the ending doing the work of of. ', ('vika', 'особый'), ' means special.']),
    (10, None, ["'I will smile and say the most polite words.' The verb ", ('max', 'улыбнусь'), ' is a single smile, unlike the continuous habit used earlier. ', ('max', 'самые'), ('max', 'вежливые'), ('max', 'слова'), ' means the most polite words.']),
    (11, None, ["'Go quickly, do not make an important person wait.' The command ", ('vika', 'не'), ('vika', 'заставляй'), ' means do not make or force. ', ('vika', 'важного'), ('vika', 'человека'), ' means an important person, changing the endings as the target of the action.']),
]
