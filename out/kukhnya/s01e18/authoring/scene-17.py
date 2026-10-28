# Authoring module for kukhnya-s01e18-scene-17.
ID = 'kukhnya-s01e18-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 17
TITLE = 'Увольнения  (Firings)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Kristina's plans for the budget have landed on Nagiyev's desk, and he has decided to dismiss the highest-paid cooks. Barinov hears about it, and the two have a furious argument in the office. Listen for the moment Barinov plays his last card."
OPENER = 'Now the row, one blow at a time.'
TRANSITION = 'Now the whole row, as it happened.'
OUTRO = 'Barinov threatens to quit, and Nagiyev has to talk him round. Keep the pair: "uvolit", to fire, and "uvolitsya", to quit. See you next time!'
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Я должен уволить твоих поваров.', 'I must fire your cooks.', [(308, 'уволить')], ''),
    ('barinov', 'Ты совсем сошёл с ума?', 'Have you gone completely crazy?', [], ''),
    ('nagiyev', 'Они слишком дорого стоят.', 'They cost too much.', [], ''),
    ('nagiyev', 'Это почти полмиллиона каждый месяц.', 'This is almost half a million every month.', [(305, 'полмиллиона каждый месяц')], ''),
    ('barinov', 'Ты не можешь их увольнять.', 'You cannot fire them.', [(309, 'нельзя увольнять')], ''),
    ('barinov', 'Это лучшая команда в Москве.', 'This is the best team in Moscow.', [(312, 'лучшие в Москве')], ''),
    ('nagiyev', 'Дешевле найти новых людей.', 'It is cheaper to find new people.', [(314, 'Дешевле')], ''),
    ('nagiyev', 'Какая разница, кто режет морковь?', 'What difference does it make who cuts carrots?', [(313, 'какая разница, кто будет морковь')], ''),
    ('barinov', 'Это моя команда!', 'This is my team!', [(315, 'моя команда')], ''),
    ('barinov', 'Если ты их уволишь, ты потеряешь меня.', 'If you fire them, you will lose me.', [], ''),
    ('nagiyev', 'Витя, просто сядь и успокойся.', 'Vitya, just sit and calm down.', [(318, 'Витя, сядь')], ''),
    ('barinov', 'Хорошо, разбирайтесь сами.', 'Alright, sort it out yourselves.', [(320, 'Разбирайтесь')], ''),
    ('barinov', 'А я пока увольняюсь.', 'And I am quitting in the meantime.', [(320, 'А я пока увольняюсь')], ''),
    ('nagiyev', 'Подожди, мы всё решим.', 'Wait, we will solve everything.', [], ''),
]
WALK = [
    (0, None, '\'I have to fire your cooks.\' "Povar", cook, becomes "povarov": people on the receiving end of a plural action take that ending.'),
    (1, None, '\'Have you gone completely mad?\' "Soyti s uma" is \'to go off your mind\'.'),
    (2, None, '\'They cost too much.\' "Stoyat", cost, is stressed on the first syllable; with the stress at the end, "stoyat" means they stand.'),
    (3, None, '\'That\'s nearly half a million every month.\' "Pol-", half, is glued on: "polmilliona", like "polchasa", half an hour.'),
    (4, None, '\'You can\'t fire them.\' Barinov picks "uvolnyat", the ongoing partner of "uvolit": that\'s the usual choice when something is ruled out.'),
    (5, None, '\'It\'s the best team in Moscow.\' "Luchshaya", the best, agrees with feminine "komanda". After "v", "Moskva" becomes "Moskve".'),
    (6, None, '\'It\'s cheaper to find new people.\' "Deshevle", cheaper, from "deshevo", cheap. "Lyudi", people, becomes "lyudey".'),
    (7, None, '\'What difference does it make who chops carrots?\' "Kakaya raznitsa" is the everyday \'who cares\'. "Morkov" covers one carrot or a pile of them.'),
    (8, None, '\'It\'s my team!\' "Komanda" means a team, and also an order, a command.'),
    (9, None, '\'If you fire them, you\'ll lose me.\' Russian puts both halves in the future: \'if you will fire them\', "uvolish".'),
    (10, None, '\'Just sit down and calm down.\' "Syad", sit down!, and "uspokoysya", calm yourself, with "-sya" on the end.'),
    (11, None, '\'All right, sort it out yourselves.\' "Razbiraytes" speaks to more than one person. "Sami", yourselves.'),
    (12, None, '\'And meanwhile I\'m quitting.\' "Uvolnyayus" is \'I fire myself\'. "Poka", meanwhile, is the same word as the casual bye.'),
    (13, None, '\'Wait, we\'ll sort it all out.\' "Podozhdi", wait!, is friendly. "Reshim", we\'ll decide, promises a result.'),
]
