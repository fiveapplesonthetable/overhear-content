# Authoring module for kukhnya-s06e04-scene-04.
ID = 'kukhnya-s06e04-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 4
TITLE = 'Паранойя родителей  (Parental Paranoia)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'While Lyova promises his mother a helper, Barinov and Eleonora summon Katya to the office and try to convince her that her prankster classmate Olivier is actually the Michelin inspector in disguise.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Eleonora offers Katya a bonus and a day off if she keeps Olivier company and reports back on his impressions. See you next time!'
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('barinov', 'Будет тебе помощница очень скоро.', 'You will have a female helper very soon.', [(53, 'Будет тебе помощница'), (54, 'Очень скоро')], 'adapted'),
    ('katya', 'Мама, ну это просто смешно.', 'Mom, well this is simply ridiculous.', [(55, 'ну это смешно')], 'adapted'),
    ('katya', 'Ну какой из Оливье инспектор?', 'How could Olivier possibly be an inspector?', [(56, 'Ну какой из Оливье инспектор?')], 'exact'),
    ('katya', 'Этот человек кидался яйцами на уроке.', 'That guy threw eggs in class.', [(56, 'Этот человек кидался яйцами')], 'adapted'),
    ('barinov', 'И что, я тоже занимался всякой ерундой.', 'So what, I also did all kinds of nonsense.', [(57, 'И что, я тоже'), (57, 'занимался всякой ерундой')], 'adapted'),
    ('eleonora', 'Да, и продолжаешь до сих пор.', 'Yes, and you still continue to this day.', [(58, 'Да, и продолжаешь до сих пор?')], 'adapted'),
    ('katya', 'Папа, я очень рада, что вы нашли то, что вас объединяет.', 'Dad, I am very glad that you two found something that unites you.', [(59, 'я очень рада, что вы нашли'), (59, 'что вас объединяет')], 'adapted'),
    ('barinov', 'Да ты пойми, что на кону звезда!', 'Understand that a star is at stake!', [(61, 'Да ты пойми, что на кону звезда')], 'exact'),
    ('barinov', 'Вдруг это он, просто будь начеку.', 'What if it is him, just be on guard.', [(62, 'вдруг это он. Просто будь начеку')], 'adapted'),
    ('eleonora', 'Или записи его увидишь в номере.', 'Or maybe you will see his notes in the room.', [(64, 'Или записи его увидишь')], 'adapted'),
    ('katya', 'Папа, может, мне еще его номер обыскать?', 'Dad, maybe I should search his room too?', [(66, 'номер?')], 'adapted'),
    ('barinov', 'Просто поговори с ним по-дружески.', 'Just talk with him in a friendly way.', [(62, 'Просто будь начеку')], 'adapted'),
]
WALK = [
    (0, None, '\'You will have a female helper very soon.\' Mentioning a female helper with Katya, Barinov centers the remark on "pomoshchnitsa" ("female helper") without any extra fuss.'),
    (1, None, '\'Mom, well this is simply ridiculous.\' Pointing to the mum at once, Katya uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (2, None, "'How could Olivier possibly be an inspector?' Turning to an inspector beside Barinov, Katya puts the real issue right on the table for Barinov."),
    (3, None, '\'That guy threw eggs in class.\' Bringing up the eggs beside Barinov, Katya reaches for the Russian word "yaytsami" ("with eggs", built from "yaytso") right at the center of the line.'),
    (4, None, '\'So what, I also did all kinds of nonsense.\' Discussing the nonsense during the talk, Barinov chooses "yerundoy" ("nonsense", from the root "yerunda") so Katya hears the exact meaning.'),
    (5, None, "'Yes, and you still continue to this day.' Eleonora responds promptly with a nod, keeping the focus on what actually matters here."),
    (6, None, '\'Dad, I am very glad that you two found something that unites you.\' Focusing on the dad in the exchange, Katya chooses "obyedinyayet" ("unites", from the root "obyedinyat") so Eleonora hears the exact meaning.'),
    (7, None, "'Understand that a star is at stake!' Bringing up a star toward Katya, Barinov brings the exchange with Katya back to practical reality."),
    (8, None, "'What if it is him, just be on guard.' Barinov jumps in firmly around Eleonora, so Eleonora knows he is not just making small talk."),
    (9, None, '\'Or maybe you will see his notes in the room.\' Focusing on the recordings with Barinov, Eleonora centers the thought on "zapisi" ("recordings", from "zapis") without wasting a word.'),
    (10, None, "'Dad, maybe I should search his room too?' Mentioning the number before Barinov, Katya keeps normal statement word order here, turning the line into a question for Barinov purely through rising pitch."),
    (11, None, "'Just talk with him in a friendly way.' Barinov responds lightly hearing Katya, leaving no doubt about where he stands."),
]
