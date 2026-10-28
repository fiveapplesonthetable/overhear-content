# Authoring module for kukhnya-s05e10-scene-14.
ID = 'kukhnya-s05e10-scene-14'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 14
TITLE = 'Плата за молчание и коктейль  (Hush Money and a Cocktail)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'mikhail': 'Михаил', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = 'After Senya hints that he must report the injury to the police unless he is paid for his silence, Mikhail promises to settle up with him. In the restaurant, a polite woman orders a Sex on the Beach cocktail from Nastya while Max frets over his mistake.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the bar scene to a close. Listen for the cocktail order that suddenly gives Max the clue he needed to solve the mystery. See you next time!'
CLOSING = ('max', 'До свидания!')
STORY = [
    ('max', 'Надо в полицию сообщать. Понял?', 'We have to report it to the police. Understood?', [(203, 'полицию сообщать'), (204, 'Понял')], 'adapted'),
    ('mikhail', 'Не понял. За молчание, да?', 'I did not understand. For silence, yes?', [(204, 'Не понял'), (206, 'там')], 'adapted'),
    ('mikhail', 'Ничего, вы не беспокойтесь. Мы решим это.', 'It is nothing, do not worry. We will solve this.', [(206, 'Ничего, вы не беспокойтесь'), (207, 'Мы решим это')], 'adapted'),
    ('nastya', 'Добрый день. Готовы делать заказ?', 'Good afternoon. Are you ready to place an order?', [(208, 'Добрый день'), (209, 'Готовы делать заказ')], 'adapted'),
    ('mikhail', 'Да, пожалуйста, коктейль.', 'Yes, please, a cocktail.', [(209, 'Да, пожалуйста, коктейли')], 'adapted'),
    ('mikhail', 'Коктейль на пляже.', 'A beach cocktail.', [(210, 'на пляже')], 'adapted'),
    ('max', 'Вика сильно расстроилась.', 'Vika got very upset.', [(211, 'Вика сильно расстроилась')], 'adapted'),
    ('max', 'Как думаешь, я проверку сорвал?', 'What do you think, did I ruin the inspection?', [(212, 'Как думаешь? Я, наверное, проверку сорвал')], 'adapted'),
    ('nastya', 'Конечно сорвал, Макс.', 'Of course you ruined it, Max.', [(212, 'проверку сорвал')], 'adapted'),
    ('nastya', 'Костя, сделай один коктейль на пляже!', 'Kostya, make one beach cocktail!', [(213, 'Костя, один'), (213, 'на пляже')], 'adapted'),
    ('max', 'Подожди, что она заказала?', 'Wait, what did she order?', [(209, 'заказ')], 'adapted'),
    ('nastya', 'Пожалуйста, ваш коктейль.', 'Here you go, your cocktail.', [(209, 'пожалуйста, коктейли')], 'adapted'),
]
WALK = [
    (0, None, '\'We have to report it to the police. Understood?\' Touching on the police before Mikhail, Max leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (1, None, "'I did not understand. For silence, yes?' Mikhail asks bluntly why things suddenly took this turn between them."),
    (2, None, '\'It is nothing, do not worry. We will solve this.\' Mikhail counters dryly in the exchange and lands on "bespokoytes" ("worry", built on "bespokoitsya") to keep the statement grounded.'),
    (3, None, '\'Good afternoon. Are you ready to place an order?\' Nastya directly sends this daytime greeting right on cue using "dobryy den" ("good afternoon") — literally "good day", the standard Russian greeting from late morning through afternoon.'),
    (4, None, '\'Yes, please, a cocktail.\' Mikhail plainly chooses this courtesy word with Nastya using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (5, None, '\'A beach cocktail.\' Talking about a beach cocktail on the spot, Mikhail uses "kokteyl" ("cocktail") to carry the main weight of the thought.'),
    (6, None, '\'Vika got very upset.\' Opening up dryly in front of Mikhail, the "-sya" ending on "rasstroilas" ("got upset") marks an action that unfolds mutually or turns back on the speaker.'),
    (7, None, "'What do you think, did I ruin the inspection?' Max prompts plainly about what Nastya just brought up."),
    (8, None, '\'Of course you ruined it, Max.\' Nastya politely gives this confirmation while facing Max using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (9, None, '\'Kostya, make one beach cocktail!\' Turning to the cocktail in this beat, Nastya centers the remark on "kokteyl" ("cocktail") without any extra fuss.'),
    (10, None, "'Wait, what did she order?' Max quizzes bluntly how Nastya expects that to work in practice."),
    (11, None, '\'Here you go, your cocktail.\' Nastya lightly chooses this courtesy word with Max using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
]
