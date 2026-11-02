# Authoring module for kukhnya-s01e09-scene-03.
ID = 'kukhnya-s01e09-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 3
TITLE = 'Занят с дочерью  (Busy with His Daughter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "Barinov has shut himself in his office with Alisa, and he is playing with her. Lyova, his sous-chef, who tends to stutter when he's stressed, comes in with a problem from the dining room. Take it in once, and don't worry about the details."
OPENER = 'Now the same thing, but slowly.'
TRANSITION = 'Now put it all together.'
OUTRO = 'Lyova leaves with the door shut behind him and the kitchen on his shoulders. Barinov goes back to playing. Bye for now.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('lyova', 'Шеф, вам нужно срочно на кухню.', 'Chef, you need to go to the kitchen urgently.', [], ''),
    ('barinov', 'Лёва, не видишь, я занят?', "Lyova, don't you see I am busy?", [(85, 'не видишь, я занят.')], ''),
    ('lyova', 'Гости в зале ждут особые блюда.', 'Guests in the dining room are waiting for special dishes.', [(84, 'два блюда от шефа')], ''),
    ('barinov', 'Я сейчас играю с моей дочерью.', 'I am playing with my daughter right now.', [(86, 'Я с дочерью играю.')], ''),
    ('lyova', 'Но гости заказали блюда от шефа.', "But the guests ordered the chef's dishes.", [(84, 'блюда от шефа')], ''),
    ('barinov', 'Ты прекрасный повар и справишься сам.', 'You are a wonderful cook and will manage yourself.', [], ''),
    ('lyova', 'Они хотят именно ваше фирменное мясо.', 'They want specifically your signature meat.', [], ''),
    ('barinov', 'Приготовь наше обычное вкусное мясо сам.', 'Cook our usual tasty meat yourself.', [], ''),
    ('lyova', 'А если гостям не понравится вкус?', 'And what if the guests do not like the taste?', [], ''),
    ('barinov', 'Добавь немного соли и свежего перца.', 'Add a little salt and fresh pepper.', [], ''),
    ('lyova', 'Шеф, на кухне начинается настоящий хаос.', 'Chef, real chaos is starting in the kitchen.', [], ''),
    ('barinov', 'Закрой дверь и наведи там порядок.', 'Close the door and bring order there.', [], ''),
    ('lyova', 'Хорошо, шеф, я всё сделаю сам.', 'Alright, chef, I will do everything myself.', [], ''),
]
WALK = [
    (0, None, ["'Chef, you need to go to the kitchen urgently.' The sous chef tells the boss to come ", ('lyova', 'срочно'), ', meaning urgently, because there is an emergency.']),
    (1, None, ["'Lyova, don't you see I am busy?' Completely absorbed in playing, the chef says he is ", ('barinov', 'занят'), ', meaning busy.']),
    (2, None, ["'Guests in the dining room are waiting for special dishes.' Customers in the dining room are waiting for ", ('lyova', 'особые'), ' dishes right now, which are the specials.']),
    (3, None, ["'I am playing with my daughter right now.' It is obvious that the father wants to ", ('barinov', 'играю'), ' with his little girl, which means to play.']),
    (4, None, ["'But the guests ordered the chef's dishes.' People at the tables have indeed ", ('lyova', 'заказали'), ' food from the kitchen, meaning they ordered it.']),
    (5, None, ["'You are a wonderful cook and will manage yourself.' Trying to dismiss the worker, the boss calls him a ", ('barinov', 'прекрасный'), ' cook, meaning wonderful.']),
    (6, None, ["'They want specifically your signature meat.' Unfortunately, the clients specifically asked for his ", ('lyova', 'фирменное'), ' meat, meaning his signature dish.']),
    (7, None, ["'Cook our usual tasty meat yourself.' He tells his employee to just make their ", ('barinov', 'обычное'), ' meat instead, which means the usual one.']),
    (8, None, ["'And what if the guests do not like the taste?' Nervously, the young man wonders if the guests will dislike the ", ('lyova', 'вкус'), ' of the food, meaning the taste.']),
    (9, None, ["'Add a little salt and fresh pepper.' As a quick tip, the older man suggests adding some ", ('barinov', 'свежего'), ' pepper, meaning fresh.']),
    (10, None, ["'Chef, real chaos is starting in the kitchen.' Things are getting out of control with a ", ('lyova', 'настоящий'), ' mess in the back, which translates to real.']),
    (11, None, ["'Close the door and bring order there.' Closing the door is his solution to bring ", ('barinov', 'порядок'), ' back, meaning order.']),
    (12, None, ["'Alright, chef, I will do everything myself.' Giving up on getting help, the assistant promises he ", ('lyova', 'сделаю'), ' everything on his own, which means will do.']),
]
