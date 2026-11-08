# Authoring module for dvorik-u-mosta-s01e04-scene-07.
ID = 'dvorik-u-mosta-s01e04-scene-07'
SHOW = 'dvorik-u-mosta'
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = 'Яркий свет на бирке  (Sunlight on the Tag)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kira': 'Кира', 'larisa': 'Лариса', 'matvey': 'Матвей'}
INTRO = 'At midday, Matvey opens the hallway closet to air it out after the storm and sets the unclaimed blue suitcase beside the front desk just as Larisa Borisovna walks in. Listen first.'
OPENER = "Let's walk through Larisa's midday realization line by line."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "Bright daylight on an old luggage tag just unlocked twenty-five years of history: two brothers on Lipovy Lane and their grandfather's wooden train. One scene left in Episode 4 — see you next time."
CLOSING = ('larisa', 'До скорого!')
STORY = [
    ('matvey', 'Поставлю этот синий чемодан здесь на пять минут, пока подмету кладовку.', 'I will set this blue suitcase here for five minutes while I sweep the closet.'),
    ('kira', 'Поаккуратнее с ним, Матвей. Пятница, полдень — это уже завтра!', 'Careful with it, Matvey. Friday at noon is tomorrow!'),
    ('larisa', 'Ой, это тот самый чемодан-близнец с утреннего поезда?', 'Oh, is that the very twin suitcase from the morning train?'),
    ('kira', 'Да, Лариса Борисовна, он всё ещё ждёт своего хозяина.', 'Yes, Larisa Borisovna, it is still waiting for its owner.'),
    ('larisa', 'Можно я ещё раз посмотрю на бумажную бирку при ярком дневном свете?', 'May I look at the paper tag once more in the bright daylight?'),
    ('matvey', 'Пожалуйста, смотрите. В понедельник днём в холле было темно.', 'Go right ahead and look. On Monday afternoon it was dark in the lobby.'),
    ('larisa', 'Подождите секунду... Садовая улица, дом двенадцать, и два детских инициала, написанных в уголке!', 'Wait a moment... Number twelve, Sadovaya Street, and two childhood initials written in the corner!'),
    ('kira', 'Лариса Борисовна, вы так удивились! Вы знаете дом двенадцать в Липовом переулке?', 'Larisa Borisovna, you look so amazed! Do you know house twelve on Lipovy Lane?'),
    ('larisa', 'Знаю ли я?! Шесть лет каждую пятницу я поднималась по той деревянной лестнице!', 'Do I know it?! For six years every Friday I climbed those wooden stairs!'),
    ('matvey', 'Двадцать пять лет назад? В этом самом доме?', 'Twenty-five years ago? In that very house?'),
    ('larisa', 'Там жил столяр и два его внука — старший играл на пианино, а младший любил поезда!', 'A cabinetmaker lived there with his two grandsons — the older played piano, while the younger loved trains!'),
    ('kira', 'Столяр... и маленький деревянный поезд внутри чемодана!', 'A cabinetmaker... and a little wooden train inside the suitcase!'),
]
WALK = [
    (0, None, ["'I will set this blue suitcase here for five minutes while I sweep the closet.' Cleaning a floor with a broom is ", (None, 'подмету'), " — 'I will sweep'."]),
    (1, None, ["'Careful with it, Matvey — tomorrow at noon is Friday already!' Softer and more specific than plain 'careful', ", (None, 'Поаккуратнее'), " means 'a bit more careful'."]),
    (2, None, ["'Oh, is that the very twin suitcase from the morning train?' Emphasizing 'that exact one' uses ", (None, 'тот самый'), " — 'the very same'."]),
    (3, None, ["'Yes, Larisa Borisovna, it is still waiting for its owner.' Combining ", (None, 'всё ещё ждёт'), " makes ongoing patience vivid: 'is still waiting'."]),
    (4, None, ["'May I look at the paper tag once more in the bright daylight?' Under sunlight or lamplight uses ", (None, 'при ярком дневном свете?'), " — 'in the presence of bright daylight'."]),
    (5, None, ["'Go right ahead and look. On Monday afternoon it was dark in the lobby.' Days of the week take 'into': ", (None, 'В понедельник'), " means 'on Monday'."]),
    (6, None, ["'Wait a second... Lipovy Lane, house twelve, and two childhood initials in the corner!' Russian street addresses name the street first, then ", (None, 'дом двенадцать,'), " — 'house twelve'."]),
    (7, None, ["'Larisa Borisovna, you look so amazed! Do you know house twelve on Lipovy Lane?' Reacting to someone's wide eyes uses ", (None, 'удивились!'), " — 'were astonished!'."]),
    (8, None, ["'Do I know it?! For six years every Friday I climbed those wooden stairs!' Repeating the action word with ", (None, 'Знаю ли я?!'), " echoes English 'do I know it?!', while ", (None, 'каждую пятницу'), ' marks every Friday.']),
    (9, None, "'Twenty-five years ago? In that very house?' Even sceptical Matvey stops sweeping as the neighbourhood puzzle clicks together."),
    (10, None, ["'A cabinetmaker lived there with his two grandsons — the older played piano, while the younger loved trains!' Notice how ", (None, 'столяр'), ' is built from the word for table — a fine furniture maker!']),
    (11, None, ["'A cabinetmaker... and a little wooden train inside the suitcase!' Look at how ", (None, 'внутри чемодана!'), " places the toy train right 'inside the suitcase'."]),
]
