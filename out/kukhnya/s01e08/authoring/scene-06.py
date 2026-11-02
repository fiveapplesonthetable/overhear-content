# Authoring module for kukhnya-s01e08-scene-06.
ID = 'kukhnya-s01e08-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 6
TITLE = 'Новый шеф на кухне  (A New Chef in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena Sokolova, chef of the Italian restaurant Arcobaleno, has bet Barinov that she can last a shift in his kitchen. The next morning she turns up at Claude Monet, and Barinov presents her to his cooks. It's in Russian first."
OPENER = 'Slowly now. Barinov makes the introductions, and within a minute Elena is giving the orders.'
TRANSITION = 'Now the whole first service again, at normal speed.'
OUTRO = "Two of Elena's lines are worth keeping: vsem vsyo ponyatno?, 'is everything clear to everyone?', which works in any meeting, and sledit za kachestvom, 'to watch over quality', her motto for the whole shift. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Внимание всем, на кухне важный гость!', 'Attention everyone, in the kitchen is an important guest!', [(84, 'У кухни, внимание, это Елена Павловна')], ''),
    ('barinov', 'Это шеф Елена Павловна Соколова.', 'This is Chef Elena Pavlovna Sokolova.', [(84, 'это Елена Павловна')], ''),
    ('elena', 'Здравствуйте, дорогие повара ресторана.', 'Hello, dear chefs of the restaurant.', [], ''),
    ('barinov', 'Сегодня она работает вместе с нами.', 'Today she works together with us.', [(85, 'Она будет сегодня')], ''),
    ('elena', 'Надеюсь, вы умеете готовить вкусно и быстро.', 'I hope you know how to cook tasty and fast.', [(80, 'ты уже час готовишь')], ''),
    ('barinov', 'Мои ребята умеют абсолютно всё!', 'My guys know how to do absolutely everything!', [(82, 'а не работали')], ''),
    ('elena', 'Тогда почему Лёва варит суп уже час?', 'Then why has Lyova been cooking soup for an hour already?', [(80, 'ты уже час готовишь')], ''),
    ('barinov', 'Лёва, отвечай шефу быстро и чётко!', 'Lyova, answer the chef quickly and clearly!', [(81, 'Заснул, что ли')], ''),
    ('elena', 'Так, официант принёс первый большой заказ.', 'Right, the waiter brought the first big order.', [(87, 'Заказ')], ''),
    ('elena', 'Одна телятина, треска и свежий салат!', 'One veal, cod, and fresh salad!', [(89, 'Телятина по трюфельным соусам, одна треска')], ''),
    ('barinov', 'Всем всё понятно? Начинайте готовить!', 'Is everything clear to everyone? Start cooking!', [(91, 'Всем все понятно')], ''),
    ('elena', 'Я лично проверю каждое готовое блюдо.', 'I will personally check every finished dish.', [(92, 'Хорошо')], ''),
    ('barinov', 'Не командуйте слишком громко, Елена.', "Don't boss around too loudly, Elena.", [(85, 'ну вы все сами слышали')], ''),
    ('elena', 'Настоящий шеф всегда следит за качеством!', 'A true chef always watches over quality!', [(85, 'ну вы все сами слышали')], ''),
]
WALK = [
    (0, None, ["'Attention everyone, in the kitchen is an important guest!' To call for quiet, Barinov says ", ('barinov', 'Внимание'), ', meaning attention.']),
    (1, None, ["'This is Chef Elena Pavlovna Sokolova.' He introduces her title as ", ('barinov', 'шеф'), ', which means chef.']),
    (2, None, ["'Hello, dear chefs of the restaurant.' Greeting the staff, Elena uses ", ('elena', 'дорогие'), ', meaning dear.']),
    (3, None, ["'Today she works together with us.' The schedule for the day begins with ", ('barinov', 'Сегодня'), ', meaning today.']),
    (4, None, ["'I hope you know how to cook tasty and fast.' She sets her expectations with ", ('elena', 'вкусно'), ', meaning tasty.']),
    (5, None, ["'My guys know how to do absolutely everything!' Defending his team, the chef adds ", ('barinov', 'абсолютно'), ', which means absolutely.']),
    (6, None, ["'Then why has Lyova been cooking soup for an hour already?' The dish causing the delay is ", ('elena', 'суп'), ', meaning soup.']),
    (7, None, ["'Lyova, answer the chef quickly and clearly!' Demanding a prompt reply, he says ", ('barinov', 'быстро'), ', meaning quickly.']),
    (8, None, ["'Right, the waiter brought the first big order.' A significant request arrives, described as ", ('elena', 'большой'), ', meaning big.']),
    (9, None, ["'One veal, cod, and fresh salad!' The final item must be ", ('elena', 'свежий'), ', which means fresh.']),
    (10, None, ["'Is everything clear to everyone? Start cooking!' Checking if the instructions make sense, he asks if it is ", ('barinov', 'понятно'), ', meaning clear.']),
    (11, None, ["'I will personally check every finished dish.' Emphasizing her own involvement, she says ", ('elena', 'лично'), ', meaning personally.']),
    (12, None, ["'Don\'t boss around too loudly, Elena.' Complaining about the noise level, Barinov includes ", ('barinov', 'слишком'), ', meaning too much.']),
    (13, None, ["'A true chef always watches over quality!' Stating a universal rule, Elena uses ", ('elena', 'всегда'), ', meaning always.']),
]