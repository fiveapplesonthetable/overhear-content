# Authoring module for kukhnya-s01e14-scene-15.
ID = 'kukhnya-s01e14-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 15
TITLE = 'Знакомство с шефом  (Meeting the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'The VIP guests are waiting in the dining room, and Elena stands up to introduce a very special chef. The chef, of course, is Max, who has no idea what is coming. Listen to it in Russian first.'
OPENER = 'Back through the speech, slowly.'
TRANSITION = 'Now the speech in one piece.'
OUTRO = "Max is now the French expert, with a recipe in a language he cannot read. How long does he keep smiling? Find out in the next scene."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Дорогие друзья, минуточку внимания.', 'Dear friends, a moment of attention.', [(233, 'Макс')], ''),
    ('elena', 'Я хочу познакомить вас с лучшим шеф-поваром.', 'I want to introduce you to the best chef.', [(233, 'Макс')], ''),
    ('max', 'Добрый вечер, дорогие гости.', 'Good evening, dear guests.', [(233, 'Макс')], ''),
    ('elena', 'Это Максимилиан, специалист по французской кухне.', 'This is Maximilian, an expert in French cuisine.', [(233, 'Макс')], ''),
    ('max', 'Я очень рад быть здесь.', 'I am very glad to be here.', [(233, 'Макс')], ''),
    ('elena', 'Он любезно согласился приготовить старинное блюдо.', 'He kindly agreed to prepare an old dish.', [(233, 'Макс')], ''),
    ('elena', 'Мы взяли его из этой французской книги.', 'We took it from this French book.', [(233, 'Макс')], ''),
    ('elena', 'Я выбрала для нас вот это блюдо.', 'I chose this dish for us.', [(233, 'Макс')], ''),
    ('max', 'Это прекрасный выбор для сегодняшнего вечера.', 'This is an excellent choice for tonight.', [(233, 'Макс')], ''),
    ('elena', 'Максимилиан приготовит его для нас сегодня.', 'Maximilian will prepare it for us today.', [(233, 'Макс')], ''),
    ('max', 'Я сделаю все в лучшем виде.', 'I will do everything in the best way.', [(233, 'Макс')], ''),
    ('elena', 'Мы ждем ваш кулинарный шедевр.', 'We are waiting for your culinary masterpiece.', [(233, 'Макс')], ''),
]
WALK = [
    (0, None, ["'Dear friends, a moment of attention.' A tiny minute or moment is ", ('elena', 'минуточку'), '. Attention is ', ('elena', 'внимания'), '.']),
    (1, None, ["'I want to introduce you to the best chef.' To introduce someone is ", ('elena', 'познакомить'), '. With the best chef is ', ('elena', 'с'), ('elena', 'лучшим'), ('elena', 'шеф'), '-', ('elena', 'поваром'), '.']),
    (2, None, ["'Good evening, dear guests.' Dear is ", ('max', 'дорогие'), '.']),
    (3, None, ["'This is Maximilian, an expert in French cuisine.' An expert in is ", ('elena', 'специалист'), ('elena', 'по'), '. Cuisine is ', ('elena', 'кухне'), '.']),
    (4, None, ["'I am very glad to be here.' Glad is ", ('max', 'рад'), '.']),
    (5, None, ["'He kindly agreed to prepare an old dish.' Agreed is ", ('elena', 'согласился'), '. Old is ', ('elena', 'старинное'), '.']),
    (6, None, ["'We took it from this French book.' From or out of is ", ('elena', 'из'), '. This French book is ', ('elena', 'этой'), ('elena', 'французской'), ('elena', 'книги'), '.']),
    (7, None, ["'I chose this dish for us.' I chose is ", ('elena', 'выбрала'), '. This right here is ', ('elena', 'вот'), ('elena', 'это'), '.']),
    (8, None, ["'This is an excellent choice for tonight.' Choice is ", ('max', 'выбор'), '. For tonight is ', ('max', 'для'), ('max', 'сегодняшнего'), ('max', 'вечера'), '.']),
    (9, None, ["'Maximilian will prepare it for us today.' It or him is ", ('elena', 'его'), '.']),
    (10, None, ["'I will do everything in the best way.' In the best way or form is ", ('max', 'в'), ('max', 'лучшем'), ('max', 'виде'), '. Everything is ', ('max', 'все'), '.']),
    (11, None, ["'We are waiting for your culinary masterpiece.' We wait is ", ('elena', 'ждем'), '. Masterpiece is ', ('elena', 'шедевр'), '.']),
]
