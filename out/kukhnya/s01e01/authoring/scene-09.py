# Authoring module for kukhnya-s01e01-scene-09.
ID = 'kukhnya-s01e01-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = 'Соли через семь минут  (Add Salt in Seven Minutes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'At the stove, the chef gives Max exact orders about timing: salt after exactly seven minutes, step back, don\'t overcook the fillet. Max answers every order with "yes, Chef". This is the Russian first.'
OPENER = 'Now the orders, one at a time.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Almost every line here was an order, and orders are the easiest part of Russian to pick up. You\'ve now heard "do this" and "don\'t do that" about a dozen ways.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Соли мясо ровно через семь минут.', 'Salt the meat exactly in seven minutes.', [(66, 'Соли через 7 минут')], ''),
    ('barinov', 'Тогда наше мясо будет намного нежнее.', 'Then our meat will be much more tender.', [(67, 'Мясо будет нежнее')], ''),
    ('max', 'Понял, шеф, я засекаю точное время.', 'Understood, Chef, I am clocking the exact time.', [(70, 'Да, шеф')], ''),
    ('barinov', 'Отойди немного в сторону, не мешай мне!', 'Step aside a little, do not disturb me!', [(68, 'Уйди вот')], ''),
    ('max', 'Извините, шеф, я просто внимательно смотрю.', 'Excuse me, Chef, I am simply watching carefully.', [(70, 'Да, шеф')], ''),
    ('barinov', 'Осталось ровно три минуты до готовности блюда.', 'Exactly three minutes remain until the dish is ready.', [(69, 'Три минуты до готовности')], ''),
    ('barinov', 'Внимательно проследи за огнём на сковороде.', 'Keep close watch on the fire on the skillet.', [(70, 'Проследи')], ''),
    ('max', 'Да, шеф, я не отхожу никуда!', 'Yes, Chef, I am not stepping away anywhere!', [(70, 'Да, шеф')], ''),
    ('barinov', 'Главное, не пережарь это нежное филе.', 'The main thing is do not overcook this tender fillet.', [(70, 'Проследи')], ''),
    ('max', 'Я сниму сковороду с горячей плиты вовремя.', 'I will remove the pan from the hot stove on time.', [(70, 'Да, шеф')], ''),
    ('barinov', 'Подавай мясо на горячей тарелке гостям.', 'Serve the meat to the guests on a hot plate.', [(70, 'Проследи')], ''),
    ('max', 'Будет исполнено в самом лучшем виде!', 'It will be executed in the very best form!', [(70, 'Да, шеф')], ''),
]
WALK = [
    (0, None, ['\'Salt the meat exactly in seven minutes.\' ', ('barinov', 'Соли'), ' is both "salt" the command and, nearly, the noun salt. ', ('barinov', 'через семь минут.'), ' is "in seven minutes", literally "through seven minutes", and the number comes first.']),
    (1, None, ['\'Then our meat will be much more tender.\' ', ('barinov', 'нежнее.'), ' is "more tender", and the ending is the same one as in "faster". ', ('barinov', 'намного'), ' is "by much", and goes right before the "more". Max used the word for "then" in "then I\'m off".']),
    (2, None, ['\'Understood, Chef, I am clocking the exact time.\' ', ('max', 'Понял,'), ' on its own means "got it", with no "I". ', ('max', 'засекаю точное время.'), ' is a cook\'s phrase for timing something with a stopwatch, and ', ('max', 'точное время.'), ' is "the exact time".']),
    (3, None, ['\'Step aside a little, do not disturb me!\' Barinov gives two blunt commands. ', ('barinov', 'Отойди'), ' starts with away, and ', ('barinov', 'не мешай мне!'), ' is literally "don\'t hinder to me": the verb to hinder takes ', ('barinov', 'мне!'), ', "to me", where English just says "me".']),
    (4, None, ['\'Excuse me, Chef, I am simply watching carefully.\' ', ('max', 'Извините,'), ' is the formal "excuse me", and ', ('max', 'смотрю.'), ' is "I look". Max says "I look" for "I\'m watching", with ', ('max', 'внимательно'), ', "carefully", in the middle.']),
    (5, None, ['\'Exactly three minutes remain until the dish is ready.\' ', ('barinov', 'Осталось'), ' is "remained": Russian says "there remained three minutes". After three, the word for minute becomes ', ('barinov', 'минуты'), ', while after seven it lost its ending completely.']),
    (6, None, ['\'Keep close watch on the fire on the skillet.\' ', ('barinov', 'Проследи за'), ', "keep watch on", uses the same word for "on" as at the cutting board. The word for fire is used, and ', ('barinov', 'на сковороде.'), ' is "on the pan".']),
    (7, None, ['\'Yes, Chef, I am not stepping away anywhere!\' ', ('max', 'не отхожу никуда!'), ' is a double negative: "not... nowhere". ', ('max', 'никуда!'), ' is built like never, and both begin with a double negative prefix.']),
    (8, None, ['\'The main thing is do not overcook this tender fillet.\' ', ('barinov', 'пережарь'), ' is over, plus to fry: over-fry. ', ('barinov', 'Главное,'), ' is "the main thing", made from main.']),
    (9, None, ['\'I will remove the pan from the hot stove on time.\' ', ('max', 'вовремя.'), ', "on time", is in, plus time, written as one word. ', ('max', 'с горячей плиты'), ' is "off the hot stove": after off, the stove becomes ', ('max', 'плиты'), '.']),
    (10, None, ['\'Serve the meat to the guests on a hot plate.\' ', ('barinov', 'Подавай'), ' is "serve", and inside it is to give. ', ('barinov', 'гостям.'), ' is "to the guests": the ending means "to" when it\'s a group.']),
    (11, None, ['\'It will be executed in the very best form!\' ', ('max', 'Будет исполнено'), ' is the sort of thing a soldier says: "it will be carried out". It doesn\'t even say "I". ', ('max', 'в самом лучшем виде!'), ' is "in the very best form".']),
]
