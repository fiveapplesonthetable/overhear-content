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
    (0, None, '\'You will have a female helper very soon.\' Barinov stresses one familiar term with Eleonora: "pomoshchnitsa" means "female helper", and it carries the main weight of what Barinov is saying.'),
    (1, None, '\'Mom, well this is simply ridiculous.\' Katya drops the comeback on cue: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (2, None, "'How could Olivier possibly be an inspector?' Cutting in right here, Katya says plainly what is on her mind."),
    (3, None, '\'That guy threw eggs in class.\' Katya frames this telling element for Eleonora: "yaytsami" means "with eggs" (from "yaytso"), giving the line its exact edge.'),
    (4, None, '\'So what, I also did all kinds of nonsense.\' Barinov frames the thought without fuss: the "-sya" ending on "zanimalsya" ("practiced") turns the action inward or makes it happen between people naturally.'),
    (5, None, "'Yes, and you still continue to this day.' Eleonora chimes in promptly with a nod, before Katya can change the subject."),
    (6, None, '\'Dad, I am very glad that you two found something that unites you.\' Katya picks this sharp term in reply: "obyedinyayet" means "unites" (from "obyedinyat"), giving the line its exact edge.'),
    (7, None, '\'Understand that a star is at stake!\' Barinov leans on one clear choice toward Katya: "zvezda" means "a star", and it carries the main weight of what Barinov is saying.'),
    (8, None, "'What if it is him, just be on guard.' Barinov stands firm firmly without any doubt, to clear the air between them once and for all."),
    (9, None, '\'Or maybe you will see his notes in the room.\' Eleonora colors one direct detail in earnest: "zapisi" means "recordings" (from "zapis"), giving the line its exact edge.'),
    (10, None, "'Dad, maybe I should search his room too?' Katya offers this warning before Barinov: Russian keeps the exact word order of a normal statement here, turning it into a question for Barinov purely through rising pitch at the end."),
    (11, None, "'Just talk with him in a friendly way.' Barinov answers lightly to settle things, refusing to let the moment slip past."),
]
