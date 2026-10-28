# Authoring module for kukhnya-s04e03-scene-02.
ID = 'kukhnya-s04e03-scene-02'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 3
SCENE = 2
TITLE = 'Мастер-класс на складе  (Master Class in the Storage Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'lyova': 'Лёва', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.03'
SOURCE_FILE = 'sources/kukhnya/s04/e03.ru.srt'
INTRO = "In the storage room of Claude Monet, Max shows Denis how to peel potatoes without giving away that he is not a trained cook, until sous-chef Lyova walks in. Let's hear the dialogue in Russian first."
OPENER = "Now let's walk through the Russian dialogue together."
TRANSITION = "Let's hear the entire conversation one more time from start to finish."
OUTRO = "That covers Max coaching Denis in the storage room before Nagiyev's staff meeting. See you next time!"
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('max', 'Кто так чистит, салага?', 'Who peels like that, rookie?', [(26, 'Кто так чистит, салага?')], ''),
    ('denis', 'Мне кажется, все уже догадались.', 'I think everyone has already guessed.', [(27, 'Мне кажется, все уже догадались')], ''),
    ('denis', 'Что я вообще совсем не повар.', 'That I am not a cook at all.', [(27, 'что я'), (27, 'не повар.')], 'adapted'),
    ('max', 'Да пока ты на складе, никто ничего не поймёт.', 'As long as you are in the storage room, nobody will figure anything out.', [(28, 'на складе никто ничего не поймет.')], ''),
    ('max', 'А заготовщиком можно и полгода пробыть.', 'And you can stay a prep cook for half a year.', [(29, 'А заготовщиком можно и полгода пробыть.')], ''),
    ('max', 'Поверь моему опыту.', 'Trust my experience.', [(30, 'моему опыту.')], ''),
    ('lyova', 'Ты и картошку за него чистить будешь, да?', 'Are you going to peel potatoes for him too, huh?', [(31, 'Ты и картошку за него'), (31, 'будешь, да?')], ''),
    ('lyova', 'Заканчивай мастер-класс.', 'Wrap up the master class.', [(32, 'Заканчивай мастер-класс.')], ''),
    ('lyova', 'Нагиев весь персонал собирает.', 'Nagiyev is gathering the entire staff.', [(33, 'Нагиев весь персонал собирает.')], ''),
    ('denis', 'Пойдём скорее.', "Let's go quickly.", [(33, 'собирает')], ''),
    ('max', 'Сейчас идём, Лёв.', 'We are coming right now, Lyova.', [(32, 'мастер-класс')], ''),
    ('lyova', 'Быстрее давайте.', 'Come on, hurry up.', [(31, 'будешь, да?')], ''),
]
WALK = [
    (0, None, '\'Who peels like that, rookie?\' Touching on the rookie right here, Max puts the question word "kto" right at the start so Denis hears the focus immediately.'),
    (1, None, "'I think everyone has already guessed.' Denis proceeds steadily around Max, steering the talk right where he wants it."),
    (2, None, '\'That I am not a cook at all.\' Bringing up a cook at once, Denis leans on "voobshche" ("at all") to give the whole sentence its punch.'),
    (3, None, '\'As long as you are in the storage room, nobody will figure anything out.\' Returning to the warehouse in the exchange, Max pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (4, None, "'And you can stay a prep cook for half a year.' Max speaks up frankly hearing Denis, letting the remark speak for itself."),
    (5, None, '\'Trust my experience.\' Mentioning his experience in this beat, Max brings in "opytu" ("experience", from "opyt") as the key Russian word here.'),
    (6, None, "'Are you going to peel potatoes for him too, huh?' Reacting warmly on the spot, Lyova keeps normal statement word order here, turning the line into a question for Max purely through rising pitch."),
    (7, None, "'Wrap up the master class.' Lyova speaks up evenly during the talk, grounding the moment in plain reality."),
    (8, None, '\'Nagiyev is gathering the entire staff.\' Discussing the entire staff to Denis, Lyova centers the remark on "personal" ("staff") without any extra fuss.'),
    (9, None, "'Let's go quickly.' Reacting earnestly to Lyova, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (10, None, "'We are coming right now, Lyova.' Max chimes in at once with a shrug, without trying to dress up how he really feels."),
    (11, None, '\'Come on, hurry up.\' Lyova pushes back briskly with Max and reaches for the Russian word "bystreye" ("faster", built from "bystro") right at the center of the line.'),
]
