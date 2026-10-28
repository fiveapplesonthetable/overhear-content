ID = 'kukhnya-s05e09-scene-05'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 9
SCENE = 5
TITLE = 'Пропавшие трюфели  (The Missing Truffles)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'lyova': 'anja', 'senya': 'angelina'}
LABELS = {'anya': 'Макс', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = "Кухня (Kukhnya) S5.09"
SOURCE_FILE = 'sources/kukhnya/s05/e09.ru.srt'

INTRO = "Near the cold storage room, sous-chef Lyova notices that expensive truffles are missing and questions the cooks. Bound by his promise to tell only the truth, Max exposes Senya's hiding spot, forcing Senya to claim he was merely testing security."

STORY = [
    ('lyova', 'А трюфеля никто не брал?', 'Did nobody take the truffles?', [(59, 'А трюфеля никто не брал')], 'adapted'),
    ('lyova', 'Там не хватает.', 'Some are missing there.', [(59, 'Там не хватает')], 'adapted'),
    ('lyova', 'Луи, ты не видел?', 'Louis, did you not see them?', [(60, 'Луи, ты не видел')], 'adapted'),
    ('lyova', 'Лавров?', 'Lavrov?', [(62, 'Лавров')], 'adapted'),
    ('anya', 'Видел.', 'I saw them.', [(63, 'Видел')], 'adapted'),
    ('lyova', 'Где они?', 'Where are they?', [(64, 'Где они')], 'adapted'),
    ('lyova', 'Кто их туда положил?', 'Who put them in there?', [(64, 'Кто'), (65, 'их туда положил')], 'adapted'),
    ('senya', 'Что такое, Лёв? Спокойно.', 'What is the matter, Lyova? Easy.', [(66, 'Что такое, Лёв? Спокойно')], 'adapted'),
    ('senya', 'Просто хотел проверить.', 'I just wanted to check.', [(67, 'Просто хотел проверить')], 'adapted'),
    ('senya', 'Смотрит кто-нибудь тут или нет.', 'Whether anyone watches things here or not.', [(67, 'смотрит кто-нибудь тут за этим или нет')], 'adapted'),
    ('senya', 'А то продукты пропадают.', 'Otherwise groceries keep disappearing.', [(68, 'продукты пропадают')], 'adapted'),
    ('lyova', 'Твои проверки?', 'Your inspections?', [(69, 'Твои проверки')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Did nobody take the truffles?' Spoken Russian keeps this brisk, leaning on 'and' and finishing on 'took'."),
    (1, None, "'Some are missing there.' The negative particle sits right before the verb meaning 'is enough' to negate the statement."),
    (2, None, "'Louis, did you not see them?' Here the Russian phrasing highlights 'Louis' before landing on 'saw'."),
    (3, None, "'Lavrov?' In Russian, the idea of 'proper name' flows naturally into 'proper name' without extra filler words."),
    (4, None, "'I saw them.' Spoken Russian keeps this brisk, leaning on 'saw' and finishing on 'saw'. Lyova answers right away."),
    (5, None, "'Where are they?' Lyova anchors the line on 'where', while 'they' completes the thought."),
    (6, None, "'Who put them in there?' The meaning hinges on 'who' working together with 'put' in spoken Russian."),
    (7, None, "'What is the matter, Lyova? Easy.' In Russian, the idea of 'what' flows naturally into 'calmly' without extra filler words."),
    (8, None, "'I just wanted to check.' Here the Russian phrasing highlights 'simply' before landing on 'to check'."),
    (9, None, "'Whether anyone watches things here or not.' Notice how Russian expresses 'looks' and 'no' with crisp inflection rather than helper words."),
    (10, None, "'Otherwise groceries keep disappearing.' Here the Russian phrasing highlights 'and' before landing on 'disappear'. Lyova answers right away."),
    (11, None, "'Your inspections?' Lyova addresses the listener with the informal singular 'you' alongside 'inspections'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that concludes the truffle inspection in the storage area. Listen for how Lyova asks who put the truffles there and how Senya talks his way out of trouble. See you in the next scene.'
CLOSING = ('senya', 'Просто хотел проверить!')
