# Authoring module for kukhnya-s01e05-scene-08.
ID = 'kukhnya-s01e05-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'Звонок от мамы  (Call from Mom)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "The cook-off is on in the Claude Monet kitchen, and Chef Barinov has decided Max needs help, but he can't be seen giving it. So he rings the kitchen phone and pretends to be Max's mother, with the recipe. Max catches on and plays along in front of the other cooks. Listen in Russian first."
OPENER = "Let's replay the phone call, from the moment Max hears who's on the line."
TRANSITION = 'Now the call in one go.'
OUTRO = 'That\'s a whole phone call in miniature: "allo" to pick up, "perezvonyu" to promise you\'ll call back, "tseluyu" and "poka" to hang up. Max now has the chef\'s recipe, and nobody knows it.'
CLOSING = ('max', 'До скорого!')
STORY = [
    ('max', 'Кто? Мама?', 'Who? Mom?', [(124, 'Кто? Мама?')], ''),
    ('max', 'А откуда она знает этот номер?', 'And how does she know this number?', [(125, 'А откуда она знает этот номер')], ''),
    ('max', 'Алло, мама?', 'Hello, Mom?', [(126, 'Алло, мама?')], ''),
    ('barinov', 'Да, мама я, твоя мама.', 'Yes, it is Mom, your mom.', [(126, 'Да, мама я, твоя мама')], ''),
    ('barinov', 'Будешь готовить форель с обычным жюльеном.', 'You will cook trout with classic julienne.', [(127, 'Будешь готовить форель с обычным')], ''),
    ('barinov', 'Для начала выпотроши свежую рыбу.', 'First, clean the fresh fish.', [(128, 'Для начала выпотроши рыбу')], ''),
    ('barinov', 'Потом аккуратно удали хребет.', 'Then carefully remove the backbone.', [(128, 'удали хребет')], ''),
    ('barinov', 'И положи филе в холодильник.', 'And put the fillet in the fridge.', [(128, 'и положи филе в холодильник')], ''),
    ('barinov', 'Ты всё понял, мамуля?', 'Did you understand everything, Mommy?', [(129, 'Понял, мамуля?')], ''),
    ('max', 'Да я тебе попозже перезвоню, некогда.', 'I will call you back later, I am busy.', [(130, 'Да я тебе попозже перезвоню'), (130, 'некогда')], ''),
    ('max', 'Целую тебя, пока.', 'Kisses to you, bye.', [(131, 'Целую тебя пока')], ''),
    ('max', 'Это звонила мама из Воронежа.', 'That was Mom calling from Voronezh.', [(132, 'Мама из Воронежа')], ''),
]
WALK = [
    (0, None, "'Who? Mom?' Two one-word questions. Mama is the word Russian children use, just like English 'mama'."),
    (1, None, '\'And how does she know this number?\' "Otkuda" is literally \'from where\', and Russians use it for \'how come\'. "Etot nomer" is \'this number\'.'),
    (2, None, '\'Hello, Mom?\' "Allo" is the hello you say when you pick up the phone. Face to face you\'d say "privet" or "zdravstvuyte".'),
    (3, None, '\'Yes, it is Mom, your mom.\' Barinov says "mama ya", \'mom I\', with no \'am\'. "Tvoya" is the feminine \'your\', to go with "mama".'),
    (4, None, '\'You will cook trout with classic julienne.\' "Budesh gotovit", \'you will cook\', is "budu", \'will\', in its \'you\' form plus a plain verb. After "s", \'with\', "zhyulen" becomes "zhyulenom".'),
    (5, None, '\'First, clean the fresh fish.\' "Dlya nachala" is \'for a start\'. "Vypotroshi" literally means \'gut it\', which is exactly how you clean a fish.'),
    (6, None, '\'Then carefully remove the backbone.\' "Potom" means \'then\', \'after that\'. "Akkuratno" looks like \'accurately\' but means \'carefully\' or \'neatly\'.'),
    (7, None, '\'And put the fillet in the fridge.\' "Kholodilnik", \'fridge\', grows out of "kholod", \'cold\'. "Polozhi" means \'put\', for laying something down.'),
    (8, None, '\'Did you understand everything, Mommy?\' "Mamulya" is an extra-tender \'mommy\'. Coming from the chef, it\'s pure comedy.'),
    (9, None, '\'I will call you back later, I am busy.\' "Perezvonyu" is "zvonit", \'to call\', with "pere-", \'again\'. "Nekogda" means \'there\'s no time\', and "popozzhe" is \'a bit later\'.'),
    (10, None, '\'Kisses to you, bye.\' "Tseluyu tebya", \'I kiss you\', is how Russians end calls with family. Then "poka", the casual \'bye\'.'),
    (11, None, '\'That was Mom calling from Voronezh.\' "Zvonila" ends in -la to agree with "mama". After "iz", \'from\', Voronezh, a city south of Moscow, becomes "Voronezha".'),
]
