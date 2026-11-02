# Authoring module for kukhnya-s01e06-scene-02.
ID = 'kukhnya-s01e06-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 2
TITLE = 'Финальный штрих  (The Final Touch)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Chef Barinov is at the pass, the shelf where finished plates wait for the waiters. He is checking one dish, and he wants Max, his trainee, to see the last step. It's in Russian first, so don't worry about catching every word."
OPENER = "Let's go through the plate. Barinov inspects it, and Max asks careful questions."
TRANSITION = 'And now the whole exchange in one piece.'
OUTRO = 'Barinov\'s last step is herbs, and yours is to keep a few kitchen words: "tarelka", plate, "blyudo", dish, "zelen", herbs. They\'ll come back. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Огузок, посмотри на эту тарелку.', 'Oguzok, look at this plate.', [], ''),
    ('max', 'Шеф, это блюдо уже готово?', 'Chef, is this dish already ready?', [], ''),
    ('barinov', 'Осталось главное: украсить его зеленью.', 'The main thing remains: to garnish it with herbs.', [(4, 'Его украшают')], ''),
    ('max', 'Каждая деталь имеет важное значение.', 'Every detail has important meaning.', [], ''),
    ('barinov', 'Еда обязана выглядеть красиво и аппетитно.', 'Food is obliged to look beautiful and appetizing.', [(4, 'украшают')], ''),
    ('max', 'Положим сюда свежую зелень?', 'Shall we put fresh herbs here?', [], ''),
    ('barinov', 'Аккуратно! Не испорти дорогую подачу.', 'Carefully! Do not ruin the expensive presentation.', [], ''),
    ('max', 'Я делаю всё очень аккуратно, шеф.', 'I do everything very carefully, chef.', [], ''),
    ('barinov', 'Красивая подача очень важна для гостей.', 'Beautiful presentation is very important for guests.', [], ''),
    ('max', 'Официанты уже ждут на кухне.', 'The waiters are already waiting in the kitchen.', [], ''),
    ('barinov', 'Зови официанта, пусть несут заказ.', 'Call the waiter, let them carry the order.', [], ''),
    ('max', 'Саша, забери готовое горячее блюдо!', 'Sasha, take the ready hot dish!', [], ''),
    ('barinov', 'Отлично, продолжаем работать дальше.', 'Great, we continue working further.', [], ''),
]
WALK = [
    (0, None, ["'Oguzok, look at this plate.' When the chef tells him to look at this, ", ('barinov', 'тарелку'), ' refers directly to the plate itself.']),
    (1, None, ["'Chef, is this dish already ready?' Asking if the meal is prepared, he uses ", ('max', 'готово'), ' to express that it is completely finished.']),
    (2, None, ["'The main thing remains: to garnish it with herbs.' The head cook points out that adding ", ('barinov', 'зеленью'), ' brings fresh greens to the meal.']),
    (3, None, ["'Every detail has important meaning.' Highlighting that every little thing matters, ", ('max', 'деталь'), ' sounds very much like the English equivalent.']),
    (4, None, ["'Food is obliged to look beautiful and appetizing.' Stating that food must look good, he uses ", ('barinov', 'аппетитно'), ' to describe something that makes you want to eat it.']),
    (5, None, ["'Shall we put fresh herbs here?' Checking if they should add something, he asks about using ", ('max', 'свежую'), ' greens that were just picked.']),
    (6, None, ["'Carefully! Do not ruin the expensive presentation.' Giving a strong warning not to ruin things, the word ", ('barinov', 'дорогую'), ' emphasizes how valuable the dish is.']),
    (7, None, ["'I do everything very carefully, chef.' Reassuring the boss about his careful work, he says ", ('max', 'аккуратно'), ' to show his delicate handling.']),
    (8, None, ["'Beautiful presentation is very important for guests.' Explaining why presentation matters so much, the people eating are called ", ('barinov', 'гостей'), ' in this restaurant setting.']),
    (9, None, ["'The waiters are already waiting in the kitchen.' Mentioning that the servers are waiting, the people who will take the food are called ", ('max', 'Официанты'), ' here.']),
    (10, None, ["'Call the waiter, let them carry the order.' Telling them to carry the food away, the meal requested by the customer is the ", ('barinov', 'заказ'), ' they are finishing.']),
    (11, None, ["'Sasha, take the ready hot dish!' Shouting for someone to take the meal, he highlights that it is a ", ('max', 'горячее'), ' dish, meaning it was just cooked.']),
    (12, None, ["'Great, we continue working further.' Expressing approval before moving on, the chef states ", ('barinov', 'Отлично'), ' to show he is pleased with the result.']),
]
