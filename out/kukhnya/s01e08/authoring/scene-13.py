# Authoring module for kukhnya-s01e08-scene-13.
ID = 'kukhnya-s01e08-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 13
TITLE = 'Тайник на складе  (Hiding Place in the Storeroom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "At Claude Monet, Max and Vika are trying to hide Nagiyev's dog, Tyson, in the vegetable storeroom, behind the potatoes. Lyova, the sous-chef, is about to walk in on them. It's in Russian first."
OPENER = 'Slowly now. Max and Vika speak in quick commands, and then Lyova walks in.'
TRANSITION = "Here's the hiding again, all in one go."
OUTRO = "Lyova's put-down, 'this is no motel for you', is a joke and a telling-off all at once, while Vika's 'let her lie for a while' tries to talk their way out of the mess. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Вот, положи её сюда.', 'Here, put her here.', [(139, 'сюда давай')], ''),
    ('vika', 'Пусть она полежит здесь до вечера.', 'Let her lie here until evening.', [(140, 'Пусть пока до вечера здесь полежит')], ''),
    ('max', 'Мы вынесем её ночью.', 'We will carry her out at night.', [(140, 'вынесем ее')], ''),
    ('vika', 'Возьми свежую кинзу.', 'Take the fresh cilantro.', [(141, 'Так, кинза')], ''),
    ('vika', 'Она легко перебьёт любой запах.', 'It will easily cover any odor.', [(142, 'Она так пахнет, если что, запах перебьет')], ''),
    ('max', 'Помоги мне поднять этот мешок.', 'Help me lift this sack.', [(148, 'Давай помогай')], ''),
    ('vika', 'Положи собаку глубже за картошку.', 'Put the dog deeper behind the potatoes.', [(152, 'Засовывай сюда'), (153, 'Глубже засовывай')], ''),
    ('lyova', 'А чем вы тут занимаетесь?', 'And what are you doing here?', [(154, 'А чем вы тут занимаетесь?')], ''),
    ('vika', 'Я просто ищу чистые скатерти.', 'I am just looking for clean tablecloths.', [(156, 'Я скатерти ищу')], ''),
    ('lyova', 'Скатерти на овощном складе?', 'Tablecloths in the vegetable storeroom?', [(157, 'скатерти на овощном складе')], ''),
    ('lyova', 'Макс, почему ты не на кухне?', "Max, why aren't you in the kitchen?", [(159, 'почему не на рабочем месте')], ''),
    ('max', 'У меня сегодня законный выходной.', 'I have a legitimate day off today.', [(160, 'А у меня выходной')], ''),
    ('lyova', 'Быстро уходите, это вам не мотель.', 'Leave quickly, this is no motel for you.', [(162, 'заканчивайте здесь фритюриться, это вам не мотель')], ''),
]
WALK = [
    (0, None, ["'Here, put her here.' To point out the exact spot, he uses ", ('max', 'сюда'), ', directing her to this specific place.']),
    (1, None, ["'Let her lie here until evening.' Waiting for the late time of day, she mentions ", ('vika', 'вечера'), ', hoping the dog stays hidden.']),
    (2, None, ["'We will carry her out at night.' When mentioning the dark time of the day, he says ", ('max', 'ночью'), ' to describe their planned escape.']),
    (3, None, ["'Take the fresh cilantro.' The specific fresh herb is called ", ('vika', 'кинзу'), ', chosen to hide the unexpected guest.']),
    (4, None, ["'It will easily cover any odor.' A strong scent or smell is the ", ('vika', 'запах'), ' they want to completely cover up.']),
    (5, None, ["'Help me lift this sack.' A large heavy bag is called a ", ('max', 'мешок'), ' and it needs to be moved out of the way.']),
    (6, None, ["'Put the dog deeper behind the potatoes.' Moving something further back requires pushing it ", ('vika', 'глубже'), ' into the storage area.']),
    (7, None, ["'And what are you doing here?' Asking about what people are busy doing, he uses ", ('lyova', 'занимаетесь'), ' to question their strange behavior.']),
    (8, None, ["'I am just looking for clean tablecloths.' The items used to cover tables are ", ('vika', 'скатерти'), ' and she pretends to need some clean ones.']),
    (9, None, ["'Tablecloths in the vegetable storeroom?' A room full of raw ingredients is the ", ('lyova', 'складе'), ', which is the wrong place for clean linens.']),
    (10, None, ["'Max, why aren't you in the kitchen?' The busy area for cooking food is the ", ('lyova', 'кухне'), ', where the chef expects his staff to be.']),
    (11, None, ["'I have a legitimate day off today.' Referring to the current day, he says ", ('max', 'сегодня'), ' to point out he is not supposed to be working.']),
    (12, None, ["'Leave quickly, this is no motel for you.' Comparing the space to a roadside accommodation, he mentions a ", ('lyova', 'мотель'), ' to insult their unusual activity.']),
]
