# Authoring module for kukhnya-s05e09-scene-05.
ID = 'kukhnya-s05e09-scene-05'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 9
SCENE = 5
TITLE = 'Пропавшие трюфели  (The Missing Truffles)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lyova': 'Лёва', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.09'
SOURCE_FILE = 'sources/kukhnya/s05/e09.ru.srt'
INTRO = "Near the cold storage room, sous-chef Lyova notices that expensive truffles are missing and questions the cooks. Bound by his promise to tell only the truth, Max exposes Senya's hiding spot, forcing Senya to claim he was merely testing security."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that concludes the truffle inspection in the storage area. Listen for how Lyova asks who put the truffles there and how Senya talks his way out of trouble. Until next time!'
CLOSING = ('senya', 'Всего хорошего!')
STORY = [
    ('lyova', 'А трюфеля никто не брал?', 'Did nobody take the truffles?', [(59, 'А трюфеля никто не брал')], 'adapted'),
    ('lyova', 'Там не хватает.', 'Some are missing there.', [(59, 'Там не хватает')], 'adapted'),
    ('lyova', 'Луи, ты не видел?', 'Louis, did you not see them?', [(60, 'Луи, ты не видел')], 'adapted'),
    ('lyova', 'Лавров?', 'Lavrov?', [(62, 'Лавров')], 'adapted'),
    ('max', 'Видел.', 'I saw them.', [(63, 'Видел')], 'adapted'),
    ('lyova', 'Где они?', 'Where are they?', [(64, 'Где они')], 'adapted'),
    ('lyova', 'Кто их туда положил?', 'Who put them in there?', [(64, 'Кто'), (65, 'их туда положил')], 'adapted'),
    ('senya', 'Что такое, Лёв? Спокойно.', 'What is the matter, Lyova? Easy.', [(66, 'Что такое, Лёв? Спокойно')], 'adapted'),
    ('senya', 'Просто хотел проверить.', 'I just wanted to check.', [(67, 'Просто хотел проверить')], 'adapted'),
    ('senya', 'Смотрит кто-нибудь тут или нет.', 'Whether anyone watches things here or not.', [(67, 'смотрит кто-нибудь тут за этим или нет')], 'adapted'),
    ('senya', 'А то продукты пропадают.', 'Otherwise groceries keep disappearing.', [(68, 'продукты пропадают')], 'adapted'),
    ('lyova', 'Твои проверки?', 'Your inspections?', [(69, 'Твои проверки')], 'adapted'),
]
WALK = [
    (0, None, '\'Did nobody take the truffles?\' Checking on the truffle during the talk, Lyova pairs the negative word with "ne" ("not"), since Russian naturally doubles its negatives for emphasis.'),
    (1, None, "'Some are missing there.' Lyova weighs in quietly without holding back, testing Max's reaction in the middle of the exchange."),
    (2, None, '\'Louis, did you not see them?\' Lyova fires back pointedly beside Max and lands on "videl" ("saw, have seen", built on "videt") to keep the statement grounded.'),
    (3, None, "'Lavrov?' Following up promptly in front of Max, Lyova keeps normal statement word order here, turning the line into a question for Max purely through rising pitch."),
    (4, None, "'I saw them.' Max chimes in quietly with a shrug, so Lyova knows he is not just making small talk."),
    (5, None, '\'Where are they?\' Cutting in directly in front of Max, Lyova links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (6, None, '\'Who put them in there?\' Pressing on candidly in this beat, Lyova puts the question word "kto" right at the start so Senya hears the focus immediately.'),
    (7, None, "'What is the matter, Lyova? Easy.' Senya presses curiously whether Lyova really thought this through."),
    (8, None, '\'I just wanted to check.\' Senya cuts in promptly to Lyova and centers the remark on "proverit" ("to check, verify") without any extra fuss.'),
    (9, None, "'Whether anyone watches things here or not.' Senya speaks up boldly in this moment, keeping the focus on what actually matters here."),
    (10, None, "'Otherwise groceries keep disappearing.' Senya follows up wryly hearing Lyova, letting the remark speak for itself."),
    (11, None, '\'Your inspections?\' Focusing on the check right here, Lyova reaches for the Russian word "proverki" ("check, inspection", built from "proverka") right at the center of the line.'),
]
