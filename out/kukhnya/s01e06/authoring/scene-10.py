# Authoring module for kukhnya-s01e06-scene-10.
ID = 'kukhnya-s01e06-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = 'Срочная уборка  (An Urgent Cleanup)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet the news has just arrived: the sanitary inspector is in the building. Barinov, the head chef, and his sous-chef Lyova have minutes to hide everything. It's in Russian first, and it's fast."
OPENER = "Let's replay it slowly. Nearly every line is an order, so listen for the commands."
TRANSITION = 'Now the panic at full speed.'
OUTRO = 'You\'ve just met a handful of kitchen orders: "nesi", carry, "brosay", throw, "vytrite", wipe. They all work in your own kitchen too. See you next time.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Не спим, Лёва, у нас проверка!', 'Wake up, Lyova, we have an inspection!', [(156, 'Не спим, Лёва, у нас проверка')], ''),
    ('lyova', 'Шеф, инспектор уже заходит в зал!', 'Chef, the inspector is already entering the hall!', [], ''),
    ('barinov', 'Быстро убирайте всё лишнее со столов.', 'Quickly clear everything extra off the tables.', [], ''),
    ('lyova', 'Куда спрятать эти старые продукты?', 'Where to hide these old products?', [], ''),
    ('barinov', 'Неси всё это прямо в холодильник.', 'Carry all this straight into the refrigerator.', [(153, 'порозилку')], ''),
    ('lyova', 'А что делать с грязными фартуками?', 'And what to do with dirty aprons?', [], ''),
    ('barinov', 'Лёва, немедленно бросай их в стирку!', 'Lyova, immediately throw them into the wash!', [(155, 'Лёва, стирку')], ''),
    ('lyova', 'Я уже отправил Сеню за тряпками.', 'I already sent Senya for cloths.', [], ''),
    ('barinov', 'Вытрите пол, он слишком скользкий!', 'Wipe the floor, it is too slippery!', [], ''),
    ('lyova', 'Повара уже моют свои рабочие места.', 'The cooks are already washing their workstations.', [], ''),
    ('barinov', 'Кухня должна быть идеально чистой!', 'The kitchen must be ideally clean!', [], ''),
    ('lyova', 'Мы успеем всё сделать вовремя, шеф!', 'We will manage to do everything in time, chef!', [], ''),
    ('barinov', 'По местам, инспектор уже здесь!', 'To your stations, the inspector is already here!', [], ''),
]
WALK = [
    (0, None, ["'Wake up, Lyova, we have an inspection!' Notice how he mentions the word ", ('barinov', 'проверка'), ', which means an inspection.']),
    (1, None, ["'Chef, the inspector is already entering the hall!' You can clearly hear Lyova say ", ('lyova', 'заходит'), ' to describe someone walking in right now.']),
    (2, None, ["'Quickly clear everything extra off the tables.' The busy chef shouts his command ", ('barinov', 'убирайте'), ' to tell multiple people to clear things away.']),
    (3, None, ["'Where to hide these old products?' In this tense moment of panic, ", ('lyova', 'спрятать'), ' is used for asking where to conceal things.']),
    (4, None, ["'Carry all this straight into the refrigerator.' Barinov gives clear directions by using ", ('barinov', 'прямо'), ' to mean taking it straight there.']),
    (5, None, ["'And what to do with dirty aprons?' Listen carefully to how he uses ", ('lyova', 'грязными'), ' to talk about the soiled aprons.']),
    (6, None, ["'Lyova, immediately throw them into the wash!' Here the head chef loudly demands ", ('barinov', 'бросай'), ', telling him to just toss them.']),
    (7, None, ["'I already sent Senya for cloths.' Lyova explains his quick action with ", ('lyova', 'отправил'), ', showing he has already dispatched someone.']),
    (8, None, ["'Wipe the floor, it is too slippery!' To describe the dangerous wet floor, ", ('barinov', 'скользкий'), ' is the word chosen here.']),
    (9, None, ["'The cooks are already washing their workstations.' Pay attention to the action word ", ('lyova', 'моют'), ', which indicates that the team is cleaning up.']),
    (10, None, ["'The kitchen must be ideally clean!' For emphasizing the required spotless state, ", ('barinov', 'идеально'), ' expresses that it must be perfect.']),
    (11, None, ["'We will manage to do everything in time, chef!' Trying to reassure his demanding boss, he uses ", ('lyova', 'вовремя'), ' to promise it will happen on time.']),
    (12, None, ["'To your stations, the inspector is already here!' As the final urgent warning comes, ", ('barinov', 'здесь'), ' simply points out that the guest has arrived.']),
]
