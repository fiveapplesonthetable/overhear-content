# Authoring module for kukhnya-s01e02-scene-10.
ID = 'kukhnya-s01e02-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 10
TITLE = 'Гости просят шефа  (The Guests Want the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'sasha': 'Саша', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'The secret fricassee has reached a guest in the dining room, and now she is asking for the chef. Sasha, a waitress, brings the news to the kitchen, and the two cooks who made the dish, Senya and Fedya, start arguing about who should go and face Barinov. This is the Russian first.'
OPENER = 'Now the panic, one line at a time.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Neither of them wants to be the one who goes, and the clock is ticking. If you remember one thing, make it "ne nado karkat\'", the Russian way to say "don\'t jinx it".'
CLOSING = ('senya', 'Пока!')
STORY = [
    ('sasha', 'Ребята, гости в зале просят шефа!', 'Guys, the guests in the dining hall want the chef!', [(138, 'Гости просят шефа')], ''),
    ('senya', 'Что? Она уже попробовала наше блюдо?', 'What? Has she already tasted our dish?', [], ''),
    ('fedya', 'Да, она съела почти всё фрикасе.', 'Yes, she ate almost all the fricassee.', [], ''),
    ('senya', 'Может быть, она хочет добавки?', 'Maybe she wants seconds?', [(136, 'добавки попросить')], ''),
    ('fedya', 'Нет, она зовёт именно шеф-повара.', 'No, she is calling specifically for the head chef.', [(134, 'Позовите, пожалуйста, вашего шефа')], ''),
    ('senya', 'Я предупреждал! Это была плохая идея!', 'I warned you! That was a bad idea!', [(140, 'Предупреждал')], ''),
    ('fedya', 'Сам иди к шефу в кабинет!', "Go to Chef's office yourself!", [(140, 'Иди к шефу')], ''),
    ('senya', 'Почему я? Ты всё это придумал!', 'Why me? You came up with all of this!', [(141, 'Причем здесь я'), (142, 'Все придумал')], ''),
    ('fedya', 'Ты его правая рука на кухне.', 'You are his right-hand man in the kitchen.', [(143, 'ты его правая рука')], ''),
    ('senya', 'Я не пойду, он меня убьёт!', 'I am not going, he will kill me!', [(144, 'Я не пойду')], ''),
    ('fedya', 'Давайте просто напишем шефу сообщение.', 'Let us just send Chef a text message.', [(146, 'давайте напишем шефу')], ''),
    ('senya', 'И сразу напишем заявление об увольнении?', 'And write our resignation letters right away?', [(147, 'заявления по собственному напишем')], ''),
    ('fedya', 'Не надо каркать раньше времени!', 'No need to jinx it ahead of time!', [(148, 'Не надо каркать')], ''),
]
WALK = [
    (0, None, '\'Guys, the guests in the dining hall want the chef!\' Sasha opens with "rebyata", the word for any informal group. "Prosyat shefa" is "ask for the chef", and "shef" gains an -a as the one being asked for.'),
    (1, None, '\'What? Has she already tasted our dish?\' "Poprobovala" is "tasted": the "po-" makes it a finished taste, and the "-la" shows it\'s a woman.'),
    (2, None, '\'Yes, she ate almost all the fricassee.\' "S\'yela" is "ate up", the finished partner of "yest\'", to eat. "Pochti vsyo" is "almost everything".'),
    (3, None, '\'Maybe she wants seconds?\' "Mozhet byt\'" is "maybe". "Dobavka", seconds, is literally "an addition", like the verb "dobavit\'", add.'),
    (4, None, '\'No, she is calling specifically for the head chef.\' "Imenno" means "precisely", a word that points right at the one you mean. "Zovyot" is "calls".'),
    (5, None, '\'I warned you! That was a bad idea!\' "Preduprezhdal" is "I warned", and "byla", "was", ends in -a because "ideya" is a feminine word.'),
    (6, None, '\'Go to Chef\'s office yourself!\' "Sam", "yourself", throws the job back at the other cook. "V kabinet", "into the office", keeps "kabinet" unchanged because he\'d be going into it.'),
    (7, None, '\'Why me? You came up with all of this!\' "Pochemu ya" is "why I?", with no change to "ya". "Pridumal", "came up with", has "dumat\'", to think, inside it.'),
    (8, None, '\'You are his right-hand man in the kitchen.\' "Pravaya ruka", "right hand", is the same idiom as in English. "Pravyy" is "right", and its cousin "prav" means "correct".'),
    (9, None, '\'I am not going, he will kill me!\' "Ne poydu" looks like a present form, but the "po-" makes it a future: "I won\'t go". "Ub\'yot", "will kill", works the same way.'),
    (10, None, '\'Let us just send Chef a text message.\' "Davayte napishem" is "let\'s write". "Soobshcheniye", a message, is what you send to "soobshchit\'", let someone know.'),
    (11, None, '\'And write our resignation letters right away?\' "Zayavleniye ob uvol\'nenii" is "an application about dismissal", and "uvol\'neniye" comes from "uvolit\'", to fire. "O" becomes "ob" before a vowel.'),
    (12, None, '\'No need to jinx it ahead of time!\' The verb means to caw like a crow, and Russians use it for predicting doom out loud. "Ahead of time" is literally "earlier than time".'),
]
