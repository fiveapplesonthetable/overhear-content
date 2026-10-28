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
    (0, None, '\'Guys, the guests in the dining hall want the chef!\' Sasha opens with "rebyata", the all-purpose word for an informal group. "Want the chef" is "ask the chef", and "chef" gains an -a as the thing they ask for.'),
    (1, None, '\'What? Has she already tasted our dish?\' The -la on "tasted" shows it\'s a woman, and the "po-" in front means "had a go".'),
    (2, None, '\'Yes, she ate almost all the fricassee.\' The "s-" on the front of "ate" makes it "ate it all up". And "almost everything" is two little words.'),
    (3, None, '\'Maybe she wants seconds?\' You know "mozhet byt\'" as "maybe". "Seconds" is literally "an addition", from the verb "to add".'),
    (4, None, '\'No, she is calling specifically for the head chef.\' "Imenno" means "precisely", a word that points right at the one you mean.'),
    (5, None, '\'I warned you! That was a bad idea!\' Senya is a man, so "warned" ends in -l. "Was" ends in -a, because "idea" is a feminine word.'),
    (6, None, '\'Go to Chef\'s office yourself!\' One word, "sam", means "yourself", and it throws the job back at the other cook. "Into the office" has no ending, since you\'re going into it.'),
    (7, None, '\'Why me? You came up with all of this!\' Russian keeps "I" after the question word, so it\'s literally "why I?". "Came up with" has "dumat\'", to think, inside.'),
    (8, None, '\'You are his right-hand man in the kitchen.\' Russian has the same idiom as English: "right hand". The word "right" also means "correct", so it\'s a happy double meaning.'),
    (9, None, '\'I am not going, he will kill me!\' "Poydu" is "I will go": "po-" turns the going into a future. Senya\'s fear is clear in the short sentences.'),
    (10, None, '\'Let us just send Chef a text message.\' "Let\'s write" is two short words, and "message" grows out of "report".'),
    (11, None, '\'And write our resignation letters right away?\' The phrase is "application about dismissal", and the "dismissal" is from "to fire", the one you heard in scene 8. The "o" becomes "ob" before a vowel.'),
    (12, None, '\'No need to jinx it ahead of time!\' The verb means to caw like a crow, and Russians use it for predicting doom out loud. "Ahead of time" is literally "earlier than time".'),
]
