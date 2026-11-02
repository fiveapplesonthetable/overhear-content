# Authoring module for kukhnya-s01e06-scene-20.
ID = 'kukhnya-s01e06-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 20
TITLE = 'До следующей Пасхи  (Until Next Easter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, the truffle salad for table seven is late, and Barinov has run out of patience. Max has no truffle and has to say something. It's in Russian first."
OPENER = 'Slowly now. The chef gets angrier with every line, and Max gets more inventive.'
TRANSITION = "Here's the standoff in one go."
OUTRO = 'Do "sleduyushchey Paskhi", until next Easter, is a good way to say something takes forever, and "vsyo pod kontrolem" is a good way to lie. Between them you\'ve got a fair picture of kitchen life. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, где мой свежий дорогой трюфель?', 'Rump, where is my fresh expensive truffle?', [(243, 'свои трюфель')], ''),
    ('barinov', 'Я буду ждать его до следующей Пасхи?', 'Am I going to wait for it until next Easter?', [(243, 'дышащей Пасхи буду ждать')], ''),
    ('max', 'Шеф, я уже несу, всё хорошо!', 'Chef, I am already bringing it, all is well!', [(244, 'Шеф'), (245, 'несу. Все хорошо')], ''),
    ('barinov', 'Ты слишком медленно работаешь на кухне!', 'You work too slowly in the kitchen!', [], ''),
    ('barinov', 'Важный гость ждёт свой заказ.', 'The important guest is waiting for his order.', [], ''),
    ('max', 'Я ищу самый лучший гриб.', 'I am looking for the best mushroom.', [], ''),
    ('barinov', 'У тебя есть ровно одна минута!', 'You have exactly one minute!', [], ''),
    ('barinov', 'Иначе я лично тебя уволю сегодня!', 'Otherwise I will personally fire you today!', [], ''),
    ('max', 'Не переживайте, шеф, заказ будет готов.', 'Do not worry, chef, the order will be ready.', [], ''),
    ('barinov', 'Я хочу видеть результат прямо сейчас.', 'I want to see the result right now.', [], ''),
    ('max', 'Мы выполнили все ваши сложные условия.', 'We fulfilled all your difficult conditions.', [(246, 'Мы выполнили твои условия')], ''),
    ('barinov', 'Что ты там бормочешь себе под нос?', 'What are you muttering under your breath there?', [], ''),
    ('max', 'Я говорю, что всё под контролем.', 'I am saying that everything is under control.', [], ''),
    ('barinov', 'Тогда неси трюфель на стол шефа!', 'Then bring the truffle to the chef table!', [], ''),
]
WALK = [
    (0, None, ["'Rump, where is my fresh expensive truffle?' The chef demands to see his ", ('barinov', 'свежий'), ' ingredient for the special dish.']),
    (1, None, ["'Am I going to wait for it until next Easter?' He wonders if the wait until ", ('barinov', 'Пасхи'), ' will ever come to an end.']),
    (2, None, ["'Chef, I am already bringing it, all is well!' Max tries to calm him down by saying he is ", ('max', 'несу'), ' the item right now.']),
    (3, None, ["'You work too slowly in the kitchen!' Barinov complains that the young cook is moving too ", ('barinov', 'медленно'), ' for a busy restaurant.']),
    (4, None, ["'The important guest is waiting for his order.' There is a very important dining ", ('barinov', 'гость'), ' waiting for the meal.']),
    (5, None, ["'I am looking for the best mushroom.' Finding the absolute most perfect and ", ('max', 'лучший'), ' ingredient takes some time.']),
    (6, None, ["'You have exactly one minute!' A strict time limit of one ", ('barinov', 'минута'), ' is given to finish the task.']),
    (7, None, ["'Otherwise I will personally fire you today!' The very real threat to personally ", ('barinov', 'уволю'), ' the worker hangs in the air.']),
    (8, None, ["'Do not worry, chef, the order will be ready.' Telling the boss not to nervously ", ('max', 'переживайте'), ' is a bold move.']),
    (9, None, ["'I want to see the result right now.' Demanding to see the final completed ", ('barinov', 'результат'), ' is typical for a head chef.']),
    (10, None, ["'We fulfilled all your difficult conditions.' Claiming they met all the difficult ", ('max', 'условия'), ' might just save him.']),
    (11, None, ["'What are you muttering under your breath there?' Asking why the boy quietly and unclearly ", ('barinov', 'бормочешь'), ' under his breath shows his annoyance.']),
    (12, None, ["'I am saying that everything is under control.' Promising that the whole situation is under ", ('max', 'контролем'), ' is a classic lie.']),
    (13, None, ["'Then bring the truffle to the chef table!' Giving a direct order to bring it to the ", ('barinov', 'стол'), ' ends the intense argument.']),
]
