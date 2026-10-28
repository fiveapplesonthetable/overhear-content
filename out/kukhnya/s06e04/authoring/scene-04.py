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
    (0, None, "'You will have a female helper very soon.' Explaining that Eleonora will have a female helper very soon lays the cards on the table for Eleonora."),
    (1, None, '\'Mom, well this is simply ridiculous.\' Since Mom well this is simply ridiculous, Katya does not waste words on excuses. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, '\'How could Olivier possibly be an inspector?\' By asking how Olivier possibly be an inspector could, Katya presses Barinov for a straight answer. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'That guy threw eggs in class.' Katya reminds Barinov that that guy threw eggs in class before the moment passes."),
    (4, None, "'So what, I also did all kinds of nonsense.' Because what he also did all kinds of nonsense, Barinov treats the matter as settled."),
    (5, None, "'Yes, and you still continue to this day.' With the truth and inspector in play, Eleonora keeps this short reply brisk and direct."),
    (6, None, "'Dad, I am very glad that you two found something that unites you.' Katya mentions that dad she is very glad that Barinov two found something that unites Barinov so Barinov sees what is at stake."),
    (7, None, '\'Understand that a star is at stake!\' Telling Eleonora to understand that a star is at stake is Barinov\'s blunt reaction in front of Eleonora. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (8, None, '\'What if it is him, just be on guard.\' Pointing out that what if it is him just be on guard gives Eleonora a sobering reality check. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'Or maybe you will see his notes in the room.' Eleonora explains that maybe Barinov will see his notes in the room, keeping her voice calm and direct."),
    (10, None, '\'Dad, maybe I should search his room too?\' When Katya asks if dad maybe she should search his room, Barinov has to answer fast. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Just talk with him in a friendly way.' With the plan and inspector in play, Barinov keeps this short reply brisk and direct."),
]
