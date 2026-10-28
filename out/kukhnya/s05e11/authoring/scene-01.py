# Authoring module for kukhnya-s05e11-scene-01.
ID = 'kukhnya-s05e11-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 1
TITLE = 'Шахматы в лобби и гости утром  (Chess in the Lobby and Morning Guests)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = "Max reflects on different ways to begin the morning: playing chess in the hotel lobby like Mikhail and Chef Barinov, or enjoying a quiet moment before a busy day. At Vika's apartment, the morning calm vanishes when Max's grandparents arrive at her door."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for the action phrases describing ways to start the day and the surprise arrival of Max's grandparents. Until next time!"
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('barinov', 'Есть много способов отлично начать день.', 'There are many ways to start the day great.', [(1, 'Есть много способов отлично начать день')], 'adapted'),
    ('barinov', 'Можно заняться спортом.', 'One can do sports.', [(2, 'Можно заняться спортом')], 'adapted'),
    ('barinov', 'Пойдём лучше в шахматы сыграем.', 'Let us go play a game of chess instead.', [(4, 'пойдем лучше в шахматы сыграем')], 'adapted'),
    ('mikhail', 'Только в лобби, мне надо гостей встретить.', 'Only in the lobby, I need to greet guests.', [(5, 'Только в лобби. Мне надо гости')], 'adapted'),
    ('barinov', 'Пойдём, унижу тебя публично.', 'Let us go, I will humiliate you in public.', [(6, 'Пойдем. Унижу тебя публично')], 'adapted'),
    ('mikhail', 'Белые начинают выигрывать!', 'White starts winning!', [(7, 'Белые начинают выигрывать')], 'adapted'),
    ('barinov', 'А можно просто насладиться минутой тишины.', 'Or one can simply enjoy a minute of silence.', [(10, 'А можно просто насладиться минутой'), (10, 'тишины')], 'adapted'),
    ('mikhail', 'Здравствуй, моя родная!', 'Hello, my dear!', [(12, 'Здравствуй, моя родная')], 'adapted'),
    ('vika', 'Здравствуйте!', 'Hello!', [(13, 'Здравствуйте')], 'adapted'),
    ('mikhail', 'Здравствуй, Викуля! А внучок где?', 'Hello, Vikulya! And where is our grandson?', [(13, 'Здравствуй, Викуля'), (14, 'внучок-то где')], 'adapted'),
    ('mikhail', 'Наверное, на работу уже ускакал?', 'He probably dashed off to work already?', [(15, 'наверное, на работу уже ускакал')], 'adapted'),
    ('vika', 'Проходите, пожалуйста.', 'Come in, please.', [(13, 'Здравствуйте')], 'adapted'),
]
WALK = [
    (0, None, '\'There are many ways to start the day great.\' Pointing to the ways in the exchange, Barinov brings in "sposobov" ("ways, methods", from "sposob") as the key Russian word here.'),
    (1, None, '\'One can do sports.\' Bringing up the sport in the exchange, Barinov leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (2, None, "'Let us go play a game of chess instead.' Barinov proceeds promptly around Mikhail, before Mikhail can change the subject."),
    (3, None, '\'Only in the lobby, I need to greet guests.\' Bringing up the guests right here, Mikhail puts the weight on "gostey" ("guests", from "gost") as the exchange unfolds.'),
    (4, None, "'Let us go, I will humiliate you in public.' Weighing in smoothly in this beat, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (5, None, "'White starts winning!' Mikhail follows up calmly around Barinov, testing Barinov's reaction in the middle of the exchange."),
    (6, None, '\'Or one can simply enjoy a minute of silence.\' Highlighting a minute to Mikhail, Barinov puts the emphasis on "nasladitsya" ("to enjoy, savor") in the middle of the talk.'),
    (7, None, '\'Hello, my dear!\' Mikhail readily speaks this familiar greeting beside Vika using "zdravstvuy" ("hello") — the singular form of the classic greeting that literally means "be healthy".'),
    (8, None, '\'Hello!\' Vika firmly uses this formal greeting to Mikhail using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (9, None, '\'Hello, Vikulya! And where is our grandson?\' Mikhail gently directs this familiar greeting beside Vika using "zdravstvuy" ("hello") — the singular form of the classic greeting that literally means "be healthy".'),
    (10, None, "'He probably dashed off to work already?' Mentioning the job right here, Mikhail keeps normal statement word order here, turning the line into a question for Vika purely through rising pitch."),
    (11, None, '\'Come in, please.\' Vika casually voices this courtesy word for Mikhail using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
]
