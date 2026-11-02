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
INTRO = 'The secret fricassee has reached a guest in the dining room, and now she is asking for the chef. Sasha, a waitress, brings the news to the kitchen, and the two cooks who made the dish, Senya and Fedya, start arguing about who should go and face Barinov. This is the conversation first.'
OPENER = 'Now the panic, one line at a time.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Neither of them wants to be the one who goes, and the clock is ticking. If you remember one thing, make it the local way to say "don\'t jinx it".'
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
    (0, None, [ '\'Guys, the guests in the dining hall want the chef!\' Sasha opens with ', ('sasha', 'Ребята,'), ', the word for any informal group. She says ', ('sasha', 'просят шефа!'), ' which translates to "ask for the chef".' ]),
    (1, None, [ '\'What? Has she already tasted our dish?\' ', ('senya', 'попробовала'), ' is the word for "tasted". The action word has a starting part making it a finished taste, and ends with a sound showing it is a woman.' ]),
    (2, None, [ '\'Yes, she ate almost all the fricassee.\' ', ('fedya', 'съела'), ' translates to "ate up", the finished partner of the action word to eat. ', ('fedya', 'почти всё'), ' is the phrase for "almost everything".' ]),
    (3, None, [ '\'Maybe she wants seconds?\' The phrase ', ('senya', 'Может быть,'), ' is "maybe". The word for seconds is literally "an addition", built from the action word to add.' ]),
    (4, None, [ '\'No, she is calling specifically for the head chef.\' ', ('fedya', 'именно'), ' translates to "precisely", a little word that points right at the one you mean. ', ('fedya', 'зовёт'), ' translates to "calls".' ]),
    (5, None, [ '\'I warned you! That was a bad idea!\' ', ('senya', 'предупреждал!'), ' translates to "I warned", and the action word for "was" gets a special ending because it describes the word for idea.' ]),
    (6, None, [ '\'Go to Chef\'s office yourself!\' ', ('fedya', 'Сам'), ', literally "yourself", throws the job back at the other cook. The phrase for "into the office" keeps the word for office unchanged because he would be going into it.' ]),
    (7, None, [ '\'Why me? You came up with all of this!\' ', ('senya', 'Почему я?'), ' translates to "why I?", with no change to the word for "I". ', ('senya', 'придумал!'), ', translating to "came up with", is built from the action word to think.' ]),
    (8, None, [ '\'You are his right-hand man in the kitchen.\' ', ('fedya', 'правая рука'), ', literally "right hand", is the same idiom as in English. The describing word for "right" has a cousin that means "correct".' ]),
    (9, None, [ '\'I am not going, he will kill me!\' ', ('senya', 'не пойду,'), ' translates to "I won\'t go". It looks like a present tense form, but the starting sound makes it a future action. ', ('senya', 'убьёт!'), ' translates to "will kill", and works the same way.' ]),
    (10, None, [ '\'Let us just send Chef a text message.\' ', ('fedya', 'Давайте просто напишем'), ' translates to "let\'s write". The word for a message is what you send to let someone know.' ]),
    (11, None, [ '\'And write our resignation letters right away?\' ', ('senya', 'заявление об увольнении?'), ' is literally "an application about dismissal", and the word for dismissal is built from the action word to fire. The little word for "about" adds an extra sound before a vowel.' ]),
    (12, None, [ '\'No need to jinx it ahead of time!\' The action word ', ('fedya', 'каркать'), ' means to caw like a crow, and locals use it for predicting doom out loud. The phrase for "ahead of time" is literally "earlier than time".' ]),
]