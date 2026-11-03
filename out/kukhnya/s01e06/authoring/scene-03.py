# Authoring module for kukhnya-s01e06-scene-03.
ID = 'kukhnya-s01e06-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = 'Секрет лучших продуктов  (The Secret of the Best Products)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "It's prep time in the kitchen at Claude Monet, with knives going on every board. Barinov walks past, inspects the chopping, and then tells Max where good cooking really starts: at the market. It's in Russian first, and you can let the odd word go."
OPENER = 'Slowly now. Barinov is giving orders, which means plenty of useful commands.'
TRANSITION = 'Back to the scene as it happened.'
OUTRO = 'Chopping fast without mistakes is hard enough for a trainee, and Barinov reminds Max that great cooking begins long before the knives come out, right at the market. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Так, повара, нарежьте все овощи.', 'So, cooks, chop all the vegetables.', [(5, 'Режут')], ''),
    ('max', 'Шеф, мы уже режем лук.', 'Chef, we are already chopping onions.', [(5, 'Режут')], ''),
    ('barinov', 'Режьте быстрее, гости скоро придут.', 'Chop faster, guests will come soon.', [], ''),
    ('max', 'А где мы возьмём свежее мясо?', 'And where will we get fresh meat?', [], ''),
    ('barinov', 'Сначала повар выбирает лучшие продукты.', 'First a cook selects the best products.', [(6, 'Но сначала для вашего блюда выбирают лучшие продукты')], ''),
    ('max', 'Мы покупаем мясо в магазине?', 'Do we buy meat in a shop?', [], ''),
    ('barinov', 'Нет, я сам выбираю всё на рынке.', 'No, I choose everything myself at the market.', [(6, 'выбирают лучшие продукты')], ''),
    ('max', 'Вы лично проверяете каждый кусок?', 'Do you personally inspect every piece?', [], ''),
    ('barinov', 'Настоящий шеф не доверяет чужим людям.', 'A real chef does not trust strangers.', [], ''),
    ('max', 'Можно мне поехать с вами?', 'May I go with you?', [], ''),
    ('barinov', 'Ты останешься на кухне чистить картошку.', 'You will stay in the kitchen peeling potatoes.', [], ''),
    ('max', 'Я мечтал выбирать лучшие продукты.', 'I dreamed of selecting the best products.', [], ''),
    ('barinov', 'Сначала научись резать без ошибок!', 'First learn to cut without mistakes!', [(5, 'Режут')], ''),
]
WALK = [
    (0, None, ["'So, cooks, chop all the vegetables.' To kick things off, you will hear the chef mention ", ('barinov', 'овощи'), ', which just means vegetables.']),
    (1, None, ["'Chef, we are already chopping onions.' Max quickly points out that they are ", ('max', 'уже'), ', already, chopping exactly what was asked.']),
    (2, None, ["'Chop faster, guests will come soon.' Notice how the head chef warns that ", ('barinov', 'скоро'), ', meaning soon, the hungry guests will arrive.']),
    (3, None, ["'And where will we get fresh meat?' It is very important to find completely ", ('max', 'свежее'), ', or fresh, meat for this busy restaurant.']),
    (4, None, ["'First a cook selects the best products.' The experienced master explains they always need ", ('barinov', 'лучшие'), ', meaning the absolute best, ingredients to cook with.']),
    (5, None, ["'Do we buy meat in a shop?' Our young cook naively wonders about the ", ('max', 'магазине'), ', which is a regular shop, rather than a market.']),
    (6, None, ["'No, I choose everything myself at the market.' Instead, the older man insists on the ", ('barinov', 'рынке'), ', the open market, for picking out the best items.']),
    (7, None, ["'Do you personally inspect every piece?' A good eager student asks if he ", ('max', 'лично'), ', personally, checks every piece of food they buy.']),
    (8, None, ["'A real chef does not trust strangers.' According to the professional in charge, a ", ('barinov', 'Настоящий'), ', or real, cook relies on nobody else.']),
    (9, None, ["'May I go with you?' Hoping to learn more, the helper asks to ", ('max', 'поехать'), ', which means to go along for the ride.']),
    (10, None, ["'You will stay in the kitchen peeling potatoes.' Unfortunately for him, he just has to ", ('barinov', 'чистить'), ', or peel, potatoes all day long.']),
    (11, None, ["'I dreamed of selecting the best products.' The trainee reveals that he has always ", ('max', 'мечтал'), ', dreamed, of doing the more exciting prep work.']),
    (12, None, ["'First learn to cut without mistakes!' The final piece of advice is about avoiding ", ('barinov', 'ошибок'), ', mistakes, while doing the basic chopping tasks.']),
]
