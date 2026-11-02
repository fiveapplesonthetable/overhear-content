# Authoring module for kukhnya-s01e01-scene-20.
ID = 'kukhnya-s01e01-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 20
TITLE = 'Шанс для новичка  (A Chance for the Newcomer)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Max has been given a first job: peeling stickers off bananas. He tries to pitch his chicken in cream sauce to the chef, who laughs at him, and then, unexpectedly, gives him a test: a dessert for an important guest. Here it is in Russian first.'
OPENER = "Let's go back over the pitch."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So Max has his chance, and a dessert to make for Eleonora Andreyevna, who is a regular at the restaurant. You can now say "I can cook" and "I have an idea".'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Шеф, у меня есть отличная идея.', 'Chef, I have an excellent idea.', [(218, 'есть идея')], ''),
    ('max', 'Я могу приготовить своё фирменное блюдо.', 'I can prepare my signature dish.', [(219, 'Мое фирменное блюдо')], ''),
    ('max', 'Это нежная курица в сливочном соусе.', 'It is tender chicken in cream sauce.', [(219, 'Курица в сливочном соусе')], ''),
    ('barinov', 'Великолепная идея от неизвестного человека.', 'A magnificent idea from an unknown person.', [(221, 'Супер идея')], ''),
    ('barinov', 'Ты пришёл на мою кухню случайно.', 'You came to my kitchen by accident.', [(222, 'попавший случайно')], ''),
    ('barinov', 'Лучше чисти бананы дальше!', 'Better keep peeling bananas!', [(225, 'Тащи еще пять ящиков бананов')], ''),
    ('max', 'Зачем вообще снимать эти наклейки?', 'Why peel off these stickers at all?', [(228, 'Нафига вообще отклеивать эти этикетки')], ''),
    ('barinov', 'Для идеального порядка во вселенной.', 'For ideal order in the universe.', [(229, 'Для баланса вселенной')], ''),
    ('max', 'Но я умею готовить прекрасные десерты.', 'But I know how to prepare wonderful desserts.', [(232, 'умеет офигенно готовить')], ''),
    ('barinov', 'Хорошо, я дам тебе один шанс.', 'All right, I will give you one chance.', [(233, 'Хорошо. Я дам тебе шанс')], ''),
    ('barinov', 'К нам пришёл наш постоянный гость.', 'Our regular guest has arrived.', [(234, 'У нас есть постоянный клиент')], ''),
    ('barinov', 'Ты приготовишь десерт для Элеоноры Андреевны.', 'You will prepare dessert for Eleonora Andreyevna.', [(235, 'Приготовишь для него десерт'), (237, 'Элеонора Андреевна')], ''),
    ('barinov', 'Если десерт понравится, ты останешься здесь.', 'If the dessert is liked, you will stay here.', [(238, 'Вот если ты сможешь угодить')], ''),
    ('max', 'Договорились, шеф! Я сделаю лучший десерт.', 'Agreed, chef! I will make the best dessert.', [(240, 'Окей'), (241, 'Ну, держитесь')], ''),
]
WALK = [
    (0, None, ['\'Chef, I have an excellent idea.\' ', ('max', "У меня есть"), ' is "at me there is", the full form of "I have". Earlier it was without it, with ', ('max', "есть"), ' left out.']),
    (1, None, ['\'I can prepare my signature dish.\' ', ('max', "Могу"), ' is "I can". ', ('max', "Фирменное"), ' comes from the word for company, so a ', ('max', "фирменное блюдо"), ' is the house\'s own dish.']),
    (2, None, ['\'It is tender chicken in cream sauce.\' Because ', ('max', "курица"), ', chicken, is feminine, ', ('max', "нежная"), ', tender, ends in -aya. The word for creamy comes from the word for cream, and after ', ('max', "в"), ' the sauce becomes ', ('max', "соусе"), ', "in the sauce".']),
    (3, None, ['\'A magnificent idea from an unknown person.\' ', ('barinov', "Великолепная"), ' has the word for great inside it. ', ('barinov', "Неизвестного"), ' is formed with the negative prefix, so "unknown". Praise this big from Barinov is a joke at Max\'s expense.']),
    (4, None, ['\'You came to my kitchen by accident.\' ', ('barinov', "Случайно"), ' comes from ', ('barinov', "случай"), ', chance, which is also in the phrase for "what happened". ', ('barinov', "На мою кухню"), ' is "to my kitchen".']),
    (5, None, ['\'Better keep peeling bananas!\' ', ('barinov', "Лучше"), ' is "better", used as "you\'d better". ', ('barinov', "Чисти"), ' is the command "peel", from the word for clean. ', ('barinov', "Дальше"), ' is "further", meaning "keep going".']),
    (6, None, ['\'Why peel off these stickers at all?\' ', ('max', "Зачем"), ' asks "what for?", about purpose, where the other word for why asks about the cause. ', ('max', "Снимать"), ' is "to take off", the everyday partner of the verb from the stove, and ', ('max', "наклейки"), ', stickers, come from the verb to glue.']),
    (7, None, ['\'For ideal order in the universe.\' The word for order here is the same word from "keep order on your table". ', ('barinov', "Во вселенной"), ' is "in the universe": ', ('barinov', "в"), ' becomes ', ('barinov', "во"), ' before a heavy cluster like "vs", just to make it sayable.']),
    (8, None, ['\'But I know how to prepare wonderful desserts.\' ', ('max', "Но"), ' is the plain "but", different from ', ('max', "а"), '. ', ('max', "Прекрасные десерты"), ' is plural, so the describing word ends in "-ye".']),
    (9, None, ['\'All right, I will give you one chance.\' ', ('barinov', "Дам"), ' is "I will give", irregular and short. ', ('barinov', "Тебе"), ' is "to you", the friendly form.']),
    (10, None, ['\'Our regular guest has arrived.\' ', ('barinov', "Постоянный"), ' means "regular", and its partner means "constantly". ', ('barinov', "К нам пришёл"), ' is "has come to us".']),
    (11, None, ['\'You will prepare dessert for Eleonora Andreyevna.\' Names change after ', ('barinov', "для"), ', even the father\'s name: the first name becomes ', ('barinov', "Элеоноры"), ', and the second name becomes ', ('barinov', "Андреевны"), '.']),
    (12, None, ['\'If the dessert is liked, you will stay here.\' ', ('barinov', "Понравится"), ' is "will please", the future of the verb to please. ', ('barinov', "Останешься"), ' is "you will stay", the "self" ending included.']),
    (13, None, ['\'Agreed, chef! I will make the best dessert.\' ', ('max', "Договорились"), '! is the everyday "deal!", the finished partner of the verb from the morning after. ', ('max', "Лучший"), ' already means "best", with no need for "very".']),
]