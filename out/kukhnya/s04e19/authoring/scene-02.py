# Authoring module for kukhnya-s04e19-scene-02.
ID = 'kukhnya-s04e19-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 19
SCENE = 2
TITLE = 'Правила конкурса  (Contest Rules)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'nagiyev': 'Нагиев', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.19'
SOURCE_FILE = 'sources/kukhnya/s04/e19.ru.srt'
INTRO = "Intrigued by the million-ruble prize and the chance to become head chef, Senya raises his hand with a question. Nagiyev welcomes all the kitchen cooks to participate—except for Viktor Petrovich—and explains the blind-tasting rules. Let's listen to their exchange in Russian."
OPENER = "Now let's examine how Nagiyev explains the contest rules to the cooks line by line."
TRANSITION = "Let's hear the conversation about the contest rules again from start to finish."
OUTRO = 'Nagiyev plans to sit in a spinning red armchair with his back to the cooks, judging dishes purely by taste. Listen for the verb meaning to participate and the nouns meaning armchair and dish. See you next time!'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('senya', 'Дмитрий Владимирович, а можно один вопрос?', 'Dmitry Vladimirovich, may I ask one question?', [(18, 'Владимирович, а можно вопрос')], 'adapted'),
    ('senya', 'А нам тоже участвовать можно?', 'Are we allowed to participate too?', [(19, 'Участвовать можно')], 'adapted'),
    ('nagiyev', 'Можно всем, кроме нашего Вити.', 'Everyone is allowed, except our Vitya.', [(20, 'Можно')], 'adapted'),
    ('nagiyev', 'Конечно, можно, дорогие друзья мои.', 'Of course you can, my dear friends.', [(22, 'Можно, конечно, можно, друзья мои')], 'adapted'),
    ('senya', 'Спасибо тебе большое, Дима.', 'Thank you very much, Dima.', [(23, 'Спасибо, Дим')], 'adapted'),
    ('senya', 'Вдруг я выиграю и шефом стану.', 'What if I win and become the head chef.', [(25, 'выиграю, шефом стану')], 'adapted'),
    ('senya', 'Я просто заранее с тобой репетирую.', 'I am just rehearsing with you in advance.', [(26, 'Просто репетирую')], 'adapted'),
    ('nagiyev', 'Я сижу в красном кресле.', 'I sit in a red armchair.', [(30, 'Я сижу'), (30, 'в кресле, в красном')], 'adapted'),
    ('nagiyev', 'Сижу спиной ко всем участникам.', 'I sit with my back to all the contestants.', [(30, 'спиной к участникам')], 'adapted'),
    ('nagiyev', 'И только по вкусу выбираю.', 'And I choose only by taste.', [(31, 'И только по вкусу')], 'adapted'),
    ('nagiyev', 'Мы определяем самое лучшее блюдо.', 'We determine the very best dish.', [(32, 'Мы определяем лучшее блюдо')], 'adapted'),
    ('fedya', 'Класс, это вообще очень оригинально!', 'Awesome, that is really original!', [(34, 'Класс. Вообще оригинально')], 'adapted'),
]
WALK = [
    (0, None, '\'Dmitry Vladimirovich, may I ask one question?\' Mentioning the question to Nagiyev, Senya leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (1, None, "'Are we allowed to participate too?' Senya asks evenly how Nagiyev expects that to work in practice."),
    (2, None, '\'Everyone is allowed, except our Vitya.\' Nagiyev counters warmly during the talk and leans on "mozhno" ("may, can") to give the whole sentence its punch.'),
    (3, None, '\'Of course you can, my dear friends.\' Nagiyev evenly offers this confirmation in front of Senya using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (4, None, '\'Thank you very much, Dima.\' Senya directly shares this word of thanks as they meet using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (5, None, '\'What if I win and become the head chef.\' Senya pushes back evenly with Nagiyev and uses "vyigrayu" ("will win", from "vyigrat") to make the point stick.'),
    (6, None, '\'I am just rehearsing with you in advance.\' Pointing out how advance he is during the talk, Senya uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (7, None, "'I sit in a red armchair.' Nagiyev speaks candidly on the spot, grounding the moment in plain reality."),
    (8, None, '\'I sit with my back to all the contestants.\' Bringing up the participants around Senya, Nagiyev chooses "uchastnikam" ("participants", from the root "uchastnik") so Senya hears the exact meaning.'),
    (9, None, '\'And I choose only by taste.\' Focusing on the taste with Fedya, Nagiyev lands on "vkusu" ("taste, style", built on "vkus") to keep the statement grounded.'),
    (10, None, "'We determine the very best dish.' Nagiyev reacts promptly with Fedya, leaving no doubt about where he stands."),
    (11, None, '\'Awesome, that is really original!\' Touching on the cool in this beat, Fedya reaches for the Russian word "originalno" ("original") right at the heart of the line.'),
]
