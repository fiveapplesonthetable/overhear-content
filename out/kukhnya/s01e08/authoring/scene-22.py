# Authoring module for kukhnya-s01e08-scene-22.
ID = 'kukhnya-s01e08-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 22
TITLE = 'В поисках руколы  (Searching for Arugula)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lyova': 'Лёва', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Lyova is down in the storeroom at Claude Monet, hunting for the arugula Elena sent him to fetch. He hates being used as a messenger. Nastya, a waitress, comes down to hurry him along. Here it is in Russian first."
OPENER = "Let's go through the search. Lyova grumbles, and Nastya keeps him moving."
TRANSITION = "Now the whole search in one take."
OUTRO = "\"Terpet ne mogu\", I can't stand it, is something you'll say about many things. And Nastya's answer, the main thing is that the guests get their food, is a good one to have ready. See you next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('lyova', 'Где же лежит эта чёртова рукола?', 'Where is this damn arugula lying?', [(259, 'Где это чертова рукола')], ''),
    ('nastya', 'Лёва, гости в зале ждут салат!', 'Lyova, guests in the dining room await salad!', [(262, 'Спасибо. Салат')], ''),
    ('lyova', 'Она нашла себе мальчика на побегушках!', 'She found herself an errand boy!', [(258, 'Тоже мне нашла мальчика на побегушках')], ''),
    ('nastya', 'Не переживай, шеф просто очень нервничает.', 'Do not worry, the chef is just very nervous.', [], ''),
    ('lyova', 'Сначала ищи зелень, потом мой посуду!', 'First look for greens, then wash dishes!', [(260, 'Сначала-то ищем руколу'), (261, 'Потом, может, еще посуду мне помыть')], ''),
    ('nastya', 'Ты опытный су-шеф, не обижайся так.', 'You are an experienced sous-chef, do not be so offended.', [], ''),
    ('lyova', 'Я уважаемый повар, а не грузчик!', 'I am a respected cook, not a loader!', [], ''),
    ('nastya', 'Помоги мне скорее найти эту коробку.', 'Help me find this box quickly.', [], ''),
    ('lyova', 'Вот она, спряталась за старыми ящиками.', 'Here it is, hidden behind old boxes.', [], ''),
    ('nastya', 'Отлично, бери её и бежим на кухню!', 'Great, take it and let us run to the kitchen!', [], ''),
    ('lyova', 'Терпеть не могу такие странные порядки.', 'I cannot stand such strange rules.', [], ''),
    ('nastya', 'Главное, чтобы гости получили свои блюда.', 'The main thing is that guests receive their dishes.', [], ''),
    ('lyova', 'Ладно, пойдём спасать наш любимый ресторан.', 'Alright, let us go save our beloved restaurant.', [], ''),
]
WALK = [
    (0, None, ["'Where is this damn arugula lying?' Notice how he says the arugula ", ('lyova', 'лежит'), ', which means lying down, as if the greens are resting on a surface.']),
    (1, None, ["'Lyova, guests in the dining room await salad!' The guests in the dining room ", ('nastya', 'ждут'), ', meaning they are actively waiting for their food.']),
    (2, None, ["'She found herself an errand boy!' Finding someone for a task uses ", ('lyova', 'нашла'), ', showing she picked him specifically for this errand.']),
    (3, None, ["'Do not worry, the chef is just very nervous.' When someone is feeling stressed, they ", ('nastya', 'нервничает'), ', showing that the chef is acting nervous right now.']),
    (4, None, ["'First look for greens, then wash dishes!' All the plates and pots are ", ('lyova', 'посуду'), ', a general word for kitchenware that needs washing.']),
    (5, None, ["'You are an experienced sous-chef, do not be so offended.' An experienced person is described as ", ('nastya', 'опытный'), ', showing they have spent time mastering their craft.']),
    (6, None, ["'I am a respected cook, not a loader!' A person who carries heavy boxes is a ", ('lyova', 'грузчик'), ', a job he clearly thinks is beneath his culinary skills.']),
    (7, None, ["'Help me find this box quickly.' Asking for help quickly is done using ", ('nastya', 'скорее'), ', giving a real sense of urgency to their search.']),
    (8, None, ["'Here it is, hidden behind old boxes.' Something that has hidden itself is ", ('lyova', 'спряталась'), ', as if the box played hide and seek.']),
    (9, None, ["'Great, take it and let us run to the kitchen!' The lively phrase for running is ", ('nastya', 'бежим'), ', making the action sound like a shared rush.']),
    (10, None, ["'I cannot stand such strange rules.' Things that are unusual or weird are ", ('lyova', 'странные'), ', which perfectly describes these new kitchen rules.']),
    (11, None, ["'The main thing is that guests receive their dishes.' The most important thing is simply ", ('nastya', 'Главное'), ', keeping their focus on serving the hungry guests.']),
    (12, None, ["'Alright, let us go save our beloved restaurant.' To talk about rescuing something, say ", ('lyova', 'спасать'), ', treating their cooking mission like saving the world.']),
]
