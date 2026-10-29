# Authoring module for kukhnya-s01e16-scene-13.
ID = 'kukhnya-s01e16-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 13
TITLE = 'В поисках ключа  (In Search of the Key)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'Major Lanovsky is heading for the kitchen, and the staff are on edge, because one of the cooks without papers, Fedya, is hiding in the walk-in fridge. Barinov and Senya whisper by the stove. Then the major asks for the fridge to be opened, very politely.'
OPENER = "Now the whispering, and the major's request, line by line."
TRANSITION = 'And the moment before the fridge opens, once more.'
OUTRO = "The fridge is about to be opened, and Barinov is nowhere near ready. Remember the major's 'bud'te lyubezny', literally 'be kind', which you can put in front of any polite request. See you next time!"
CLOSING = ('senya', 'Удачи, шеф!')
STORY = [
    ('barinov', 'Инспектор здесь.', 'The inspector is here.', [], ''),
    ('senya', 'Знаю, я его видел.', 'I know, I saw him.', [], ''),
    ('barinov', 'Он хочет проверить кухню.', 'He wants to check the kitchen.', [], ''),
    ('senya', 'Пусть проверяет.', 'Let him check.', [], ''),
    ('barinov', 'Он ищет нелегалов.', 'He is looking for illegals.', [], ''),
    ('senya', 'У нас их нет.', 'We do not have them.', [], ''),
    ('barinov', 'Где Федя?', 'Where is Fedya?', [], ''),
    ('senya', 'Он в холодильнике.', 'He is in the fridge.', [], ''),
    ('barinov', 'Только бы он там не замёрз.', "As long as he doesn't freeze in there.", [], ''),
    ('inspector', 'Виктор Петрович, будьте любезны.', 'Viktor Petrovich, would you be so kind.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Откройте, пожалуйста, холодильник.', 'Open the fridge, please.', [(168, 'Виктор Петрович, будьте любезны, откройте, пожалуйста, холодильник.')], ''),
    ('inspector', 'Я жду, Виктор Петрович.', "I'm waiting, Viktor Petrovich.", [], ''),
]
WALK = [
    (0, None, "'The inspector is here.' Russian needs no 'is': 'inspektor zdes' is literally 'inspector here'. 'Zdes' and 'tut' both mean 'here', and 'tut' is a little more casual."),
    (1, None, "'I know, I saw him.' 'Znayu', 'I know', needs no 'ya' because the '-yu' ending already says 'I'. 'Videl', 'saw', ends in '-l', the past for a man."),
    (2, None, "'He wants to check the kitchen.' 'Khotet', 'to want', is irregular: 'ya khochu', 'I want', but 'on khochet', 'he wants'. 'Kukhnya', 'kitchen', becomes 'kukhnyu' because it is what gets checked."),
    (3, None, "'Let him check.' 'Pust' means 'let', and it goes before the plain 'he checks', 'proveryaet'. It's the shrug of someone who has nothing to hide, or pretends not to."),
    (4, None, "'He is looking for illegals.' 'Nelegaly' is built from 'ne', 'not', and 'legal', the same word as in English. 'Ishchet', 'is looking for', changes it to 'nelegalov', for people looked for."),
    (5, None, "'We don't have them.' 'U nas ikh net' is literally 'at us them not'. 'Net' here means 'there isn't', and 'ikh', 'them', comes in front of it."),
    (6, None, "'Where is Fedya?' The name is the short, friendly form of 'Fyodor'. Russian needs no 'is' in a 'gde' question: 'gde Fedya?' is literally 'where Fedya?'"),
    (7, None, "'He is in the fridge.' After 'v', 'in', 'kholodilnik' becomes 'kholodilnike', the ending for where something is. Senya doesn't need to say more, because the fridge is the whole problem."),
    (8, None, "'As long as he doesn't freeze in there.' 'Tolko by' means 'if only' or 'as long as', for a worried wish. 'Zamyorz' comes from 'moroz', 'frost', so it is literally 'got frosted'."),
    (9, None, "'Viktor Petrovich, would you be so kind.' 'Bud'te lyubezny' is literally 'be kind', said before a polite request. It's what a very formal person says, or someone being formal on purpose."),
    (10, None, "'Open the fridge, please.' 'Otkroyte', 'open', ends in '-yte', the command ending for 'vy'. 'Pozhaluysta', 'please', also means 'you're welcome'."),
    (11, None, "'I'm waiting, Viktor Petrovich.' Short and cold: 'ya zhdu', I'm waiting, then the chef's first name and patronymic. That polite form of address makes the words sound like pressure."),
]
