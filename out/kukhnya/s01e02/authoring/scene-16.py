# Authoring module for kukhnya-s01e02-scene-16.
ID = 'kukhnya-s01e02-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 16
TITLE = 'Пропавший коньяк  (The Missing Cognac)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'master': 'Мастер'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "Kostya has chased the fake repairman out into the street and caught up with him. The bottle of cognac is somewhere in the man's bag, and Kostya wants it back, but the man does not look frightened. Here is their face-off in Russian first."
OPENER = "Let's go through the standoff."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Kostya, who looks gentle, has a surprise for the thief. You\'ve heard a good threat: "otday", "give it back".'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Стой, парень! Куда ты несёшь дорогой коньяк?', 'Wait, guy! Where are you carrying the expensive cognac?', [(197, 'где коньяк')], ''),
    ('master', 'Какой коньяк? Я ничего не брал.', 'What cognac? I took nothing.', [(198, 'Какой коньяк')], ''),
    ('kostya', 'Бутылку из бара! Она стоит двадцать тысяч.', 'The bottle from the bar! It costs twenty thousand.', [(198, 'За 20 тысяч')], ''),
    ('master', 'Ого, двадцать тысяч рублей? Ничего себе цена!', 'Wow, twenty thousand rubles? What a price!', [(199, '20 тысяч')], ''),
    ('master', 'Ты серьёзно попал в беду, бармен.', 'You seriously got into trouble, bartender.', [(200, 'Ты реально попал')], ''),
    ('kostya', 'Нет, это ты попал в беду!', 'No, you are the one in trouble!', [(201, 'Это ты попал')], ''),
    ('kostya', 'Немедленно верни мне эту дорогую бутылку.', 'Return this expensive bottle to me immediately.', [], ''),
    ('master', 'Слушай сюда, парень, ты сейчас нарываешься.', 'Listen here, guy, you are asking for it now.', [], ''),
    ('master', 'Большой шкаф всегда очень громко падает.', 'A big wardrobe always falls very loudly.', [(203, 'Большой шкаф громко падает')], ''),
    ('master', 'Ты слышал такое умное народное правило?', 'Have you heard such a clever folk rule?', [(203, 'Слышал такое')], ''),
    ('kostya', 'Я много лет серьёзно занимался боксом.', 'I seriously practiced boxing for many years.', [(204, 'я боксом занимался')], ''),
    ('kostya', 'Отдай коньяк, иначе я ударю тебя!', 'Hand over the cognac, otherwise I will hit you!', [], ''),
    ('master', 'Ладно, ладно, не надо сразу драться!', 'Okay, okay, no need to fight right away!', [], ''),
]
WALK = [
    (0, None, '\'Wait, guy! Where are you carrying the expensive cognac?\' "Stoy" is literally "stand", so "stop!". The question word is "kuda", where to, because the bottle is moving.'),
    (1, None, '\'What cognac? I took nothing.\' "Ya nichego ne bral" is "I nothing not took", another double negative. "Bral" is the same plain "took" Nastya used to deny taking the knife.'),
    (2, None, '\'The bottle from the bar! It costs twenty thousand.\' "Stoit" means "costs" again. In "dvadtsat\' tysyach", twenty thousand, "tysyacha" shrinks to "tysyach" after the number.'),
    (3, None, '\'Wow, twenty thousand rubles? What a price!\' "Ogo" is "wow". "Nichego sebe", "nothing to oneself", means "well, I never!". "Tsena" is the price.'),
    (4, None, '\'You seriously got into trouble, bartender.\' "Popal v bedu" is "fell into trouble", like English "landed in". "Beda", trouble, becomes "bedu" after "v".'),
    (5, None, '\'No, you are the one in trouble!\' "Eto ty" is "it\'s you", which puts the stress on "you". Kostya turns the man\'s own sentence back on him.'),
    (6, None, '\'Return this expensive bottle to me immediately.\' "Verni", give back, is the friendly command, and "mne" is "to me". "Etu doroguyu butylku" all end in -u as the thing returned.'),
    (7, None, '\'Listen here, guy, you are asking for it now.\' "Slushay syuda" is literally "listen here". "Naryvayesh\'sya" means "you\'re asking for it", a threat.'),
    (8, None, '\'A big wardrobe always falls very loudly.\' "Bol\'shoy shkaf gromko padayet" is a real Russian saying, like "the bigger they are, the harder they fall". "Shkaf" is a wardrobe and "padayet" is "falls".'),
    (9, None, '\'Have you heard such a clever folk rule?\' "Umnyy", clever, comes from "um", mind. "Narodnyy", folk, comes from "narod", people, and "slyshal" is the past for a man.'),
    (10, None, '\'I seriously practiced boxing for many years.\' After "mnogo", "god", year, turns into "let", an odd form. "Zanimalsya boksom" is "busied myself with boxing", so the sport takes -om.'),
    (11, None, '\'Hand over the cognac, otherwise I will hit you!\' "Otday" is "give it over", and "inache" is "otherwise". "Udaryu", I\'ll hit, is one word.'),
    (12, None, '\'Okay, okay, no need to fight right away!\' "Ladno, ladno" is "OK, OK". "Ne nado" is "no need", and "drat\'sya", to fight, ends in "-sya".'),
]
