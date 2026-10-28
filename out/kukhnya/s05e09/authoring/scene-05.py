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
    (0, None, '\'Did nobody take the truffles?\' By checking whether nobody take the truffles, Lyova presses Max for a straight answer. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (1, None, "'Some are missing there.' Realizing that some are missing there changes how Lyova handles the situation."),
    (2, None, "'Louis, did you not see them?' Checking whether Max not see them is how Lyova puts Max on the spot."),
    (3, None, '\'Lavrov?\' Over the room and the promise, Lyova presses Max for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'I saw them.' Admitting that he saw them shows Max being honest for a change."),
    (5, None, "'Where are they?' Wondering where they are cuts straight through the tension between Lyova and Max."),
    (6, None, '\'Who put them in there?\' Wondering if who put them in there shows Lyova caught off guard. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, '\'What is the matter, Lyova? Easy.\' Here asking what the matter Lyova is shows Senya looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'I just wanted to check.' Adding that he just wanted to check fills in the missing piece for Lyova."),
    (9, None, "'Whether anyone watches things here or not.' Since whether anyone watches things here or not, Senya does not waste words on excuses."),
    (10, None, "'Otherwise groceries keep disappearing.' With the work and promise in play, Senya keeps this short reply brisk and direct."),
    (11, None, "'Your inspections?' Over the promise and the room, Lyova presses Max for a straight answer."),
]
