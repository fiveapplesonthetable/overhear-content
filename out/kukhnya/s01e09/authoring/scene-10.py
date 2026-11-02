# Authoring module for kukhnya-s01e09-scene-10.
ID = 'kukhnya-s01e09-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 10
TITLE = "Папина дочка  (Daddy's Girl)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'alisa': 'Алиса', 'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = 'The banquet guests have arrived, and Alisa is on the dining room floor next to Vika. She has opinions about everyone, and then her father turns up. Listen to who says what.'
OPENER = "Let's take the lines one by one."
TRANSITION = "Let's play it through again."
OUTRO = "Barinov is back in his kitchen shouting, and Alisa is back in the dining room, watching. In this restaurant nothing stays quiet for long. That's it for this one."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Добрый день, добро пожаловать в ресторан!', 'Good afternoon, welcome to the restaurant!', [(224, 'Добрый день'), (226, 'Мы с моей помощницей рады видеть вас в нашем ресторане')], ''),
    ('alisa', 'Здравствуйте, а это ваша девушка?', 'Hello, is that your girlfriend?', [(227, 'Здравствуйте'), (229, 'А это твоя девушка?')], ''),
    ('vika', 'Алиса, веди себя прилично с гостями.', 'Alisa, behave decently with the guests.', [], ''),
    ('alisa', 'У меня был дедушка в Новороссийске.', 'I had a grandfather in Novorossiysk.', [(230, 'У меня тоже был дедушка в Новороссийске')], ''),
    ('alisa', 'Но он умер в прошлом году.', 'But he died last year.', [(231, 'Только он умер')], ''),
    ('vika', 'А вот наконец и твой папа!', 'And here at last is your dad!', [(233, 'вот и папа')], ''),
    ('alisa', 'Папа, пойдём скорее играть со мной!', 'Dad, let us go play with me quickly!', [(237, 'Пап, давай играть')], ''),
    ('barinov', 'Сначала я проверю работу наших поваров.', "First I will check our cooks' work.", [(238, 'Давай-ка я сначала посмотрю, как готовят эти инвалиды')], ''),
    ('barinov', 'Кладите меньше пармезана в это блюдо!', 'Put less Parmesan into this dish!', [(239, 'Меньше пармезана')], ''),
    ('barinov', 'Соус заказали целых полчаса назад.', 'The sauce was ordered a whole half-hour ago.', [(241, 'Соус полчаса назад заказали')], ''),
    ('barinov', 'Шевелитесь быстрее, гости долго ждут заказ.', 'Move faster, the guests have been waiting long for the order.', [(242, 'Шевелись')], ''),
    ('alisa', 'Папа всегда так громко командует.', 'Dad always commands so loudly.', [], ''),
    ('vika', 'Твой папа — настоящий хозяин кухни.', 'Your dad is the true master of the kitchen.', [(236, 'Папина дочка')], ''),
]
WALK = [
    (0, None, ["'Good afternoon, welcome to the restaurant!' The hostess welcomes the guests using ", ('vika', 'добро'), ', which means good or welcome here.']),
    (1, None, ["'Hello, is that your girlfriend?' A polite greeting is followed by ", ('alisa', 'девушка'), ', meaning young woman or girlfriend.']),
    (2, None, ["'Alisa, behave decently with the guests.' The stressed manager tries maintaining order, asking her to behave ", ('vika', 'прилично'), ', which means decently.']),
    (3, None, ["'I had a grandfather in Novorossiysk.' This little girl suddenly mentions her ", ('alisa', 'дедушка'), ', meaning grandfather, completely out of nowhere.']),
    (4, None, ["'But he died last year.' Our story takes a dark twist featuring ", ('alisa', 'умер'), ', which tells us someone died.']),
    (5, None, ["'And here at last is your dad!' Absolute relief washes over the hostess as she says ", ('vika', 'наконец'), ', meaning at last or finally.']),
    (6, None, ["'Dad, let us go play with me quickly!' His excited daughter wants him to move ", ('alisa', 'скорее'), ', which translates to quickly or faster.']),
    (7, None, ["'First I will check our cooks' work.' He always has to check the ", ('barinov', 'работу'), ', meaning work, before doing anything else.']),
    (8, None, ["'Put less Parmesan into this dish!' The head chef barks orders about putting ", ('barinov', 'меньше'), ', which means less, into the meal.']),
    (9, None, ["'The sauce was ordered a whole half-hour ago.' Time is moving too slowly for him, marked by ", ('barinov', 'назад'), ', meaning ago or back.']),
    (10, None, ["'Move faster, the guests have been waiting long for the order.' Patience is definitely not his strong suit, complaining they wait ", ('barinov', 'долго'), ', which translates to a long time.']),
    (11, None, ["'Dad always commands so loudly.' She is very used to him speaking ", ('alisa', 'громко'), ', meaning loudly, in the noisy kitchen.']),
    (12, None, ["'Your dad is the true master of the kitchen.' Everyone in the restaurant agrees he is the true ", ('vika', 'хозяин'), ', meaning master or boss around here.']),
]
