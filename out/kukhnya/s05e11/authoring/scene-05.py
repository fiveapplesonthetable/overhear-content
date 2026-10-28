# Authoring module for kukhnya-s05e11-scene-05.
ID = 'kukhnya-s05e11-scene-05'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 11
SCENE = 5
TITLE = 'Заселение с комфортом  (Checking In with Comfort)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'max': 'Макс', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.11'
SOURCE_FILE = 'sources/kukhnya/s05/e11.ru.srt'
INTRO = "Max brings his grandparents into a plush room at Hotel Eleon. Worried about the cost, his grandmother offers to sleep on the floor at Max and Vika's apartment, so Max quickly insists they stay at the hotel in comfort and introduces them to Mikhail Dzhekovich."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes the hallway check-in scene. Listen for the verb meaning to spend the night and how Max persuades his grandmother to stay in comfort at the hotel. Until next time!'
CLOSING = ('max', 'Всего хорошего!')
STORY = [
    ('guest', 'Ух ты! Как в кино!', 'Wow! Just like in the movies!', [(75, 'Ух ты'), (76, 'Как в кино')], 'adapted'),
    ('guest', 'Максим, тут очень дорого, наверное.', 'Maxim, it is probably very expensive here.', [(77, 'Максим, тут очень дорого, наверное')], 'adapted'),
    ('guest', 'Давайте у вас переночуем.', 'Let us spend the night at your place.', [(78, 'Давайте у вас переночуем')], 'adapted'),
    ('max', 'Бабуль, перестань! Ну какой на полу?', 'Granny, stop it! What do you mean on the floor?', [(80, 'Бабуль, перестань. Ну, какой на полу')], 'adapted'),
    ('max', 'Переночуйте здесь с комфортом.', 'Spend the night here in comfort.', [(81, 'Переночуйте здесь с комфортом')], 'adapted'),
    ('max', 'Здравствуйте, Михаил Джекович.', 'Hello, Mikhail Dzhekovich.', [(83, 'Михаил Джекович')], 'adapted'),
    ('mikhail', 'Добрый день.', 'Good afternoon.', [(84, 'Добрый день')], 'adapted'),
    ('guest', 'Люба. Добрый день!', 'Lyuba. Good afternoon!', [(84, 'Люба'), (85, 'Добрый день')], 'adapted'),
    ('guest', 'А по-русски как хорошо разговаривает, да?', 'And how well he speaks Russian, right?', [(86, 'А по-русски-то как разговаривает, да')], 'adapted'),
    ('max', 'Пойдёмте в номер.', 'Let us go to the room.', [(87, 'Пойдемте, пойдемте')], 'adapted'),
    ('mikhail', 'Приятного отдыха!', 'Have a pleasant stay!', [(85, 'Добрый день')], 'adapted'),
    ('guest', 'Спасибо большое.', 'Thank you very much.', [], ''),
]
WALK = [
    (0, None, "'Wow! Just like in the movies!' The guest chimes in bluntly with a smile, making his position completely clear."),
    (1, None, "'Maxim, it is probably very expensive here.' The guest reacts right away watching Max, leaving no doubt about where he stands."),
    (2, None, '\'Let us spend the night at your place.\' The guest answers plainly in this beat and reaches for the Russian word "perenochuyem" ("will spend the night", built from "perenochevat") right at the center of the line.'),
    (3, None, '\'Granny, stop it! What do you mean on the floor?\' Turning to the granny beside the guest, Max puts the question word "kakoy" right at the start so the guest hears the focus immediately.'),
    (4, None, "'Spend the night here in comfort.' Max speaks earnestly with a sigh, refusing to let the moment slip past."),
    (5, None, '\'Hello, Mikhail Dzhekovich.\' Max plainly offers this formal greeting while facing Mikhail using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (6, None, '\'Good afternoon.\' Mikhail gently speaks this daytime greeting at the start of the beat using "dobryy den" ("good afternoon") — literally "good day", the standard Russian greeting from late morning through afternoon.'),
    (7, None, '\'Lyuba. Good afternoon!\' The guest firmly offers this daytime greeting as they meet using "dobryy den" ("good afternoon") — literally "good day", the standard Russian greeting from late morning through afternoon.'),
    (8, None, '\'And how well he speaks Russian, right?\' The guest cuts in plainly in front of Max and puts the weight on "razgovarivayet" ("to talk, to speak", from "razgovarivat") as the exchange unfolds.'),
    (9, None, "'Let us go to the room.' Returning to the number in front of the guest, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (10, None, "'Have a pleasant stay!' Mikhail speaks plainly with a shrug, without trying to dress up how he really feels."),
    (11, None, '\'Thank you very much.\' The guest firmly extends this word of thanks in the exchange using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
]
