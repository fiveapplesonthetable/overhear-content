# Authoring module for kukhnya-s01e05-scene-18.
ID = 'kukhnya-s01e05-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 18
TITLE = 'Рыбный экзамен  (The Fish Exam)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Back in the Claude Monet kitchen, Chef Barinov puts Max to a real test: tonight Max runs the fish station on his own. What Max doesn't know is that the chef plans to keep the orders coming. Listen in Russian first, and let a few words go by."
OPENER = "Let's walk through it. Barinov fires off orders, and Max says yes to every one."
TRANSITION = 'Now try it at service speed.'
OUTRO = 'Kitchen Russian is short and fast: "est", "shef" for \'yes, chef\', "ya spravlyus" for \'I\'ll cope\', and "dokazhi" for \'prove it\'.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Все заказы по рыбе выполняешь ты!', 'You are handling all the fish orders!', [(243, 'все заказы по рыбе')], ''),
    ('max', 'Есть, шеф, я готов к работе!', 'Yes, Chef, I am ready to work!', [(244, 'Есть, шеф')], ''),
    ('barinov', 'Посмотрим, какой из тебя рыбный мастер.', 'Let us see what kind of fish master you are.', [], ''),
    ('max', 'Я приготовлю все блюда очень быстро.', 'I will prepare all dishes very quickly.', [], ''),
    ('barinov', 'Максим, прими заказ: две трески по-флорентийски!', 'Maxim, take the order: two cod Florentines!', [(256, 'две трески')], ''),
    ('max', 'Да, шеф, уже начинаю готовить.', 'Yes, Chef, I am already starting to cook.', [(257, 'Да, шеф')], ''),
    ('barinov', 'И ещё две порции трески с миндалём!', 'And two more portions of cod with almonds!', [], ''),
    ('max', 'Я же уже взял два блюда!', 'But I already took two dishes!', [(260, 'Я же уже взял два блюда')], ''),
    ('barinov', 'Не спорь, Федя как-то справлялся!', 'Do not argue, Fedya managed somehow!', [(261, 'Федя как-то справлялся')], ''),
    ('max', 'Мне не хватает свежей рыбы здесь.', 'I do not have enough fresh fish here.', [], ''),
    ('barinov', 'Ищи на складе и быстрее крутись!', 'Search in the storage and hustle faster!', [], ''),
    ('max', 'Я справлюсь со всеми заказами сам.', 'I will handle all orders myself.', [], ''),
    ('barinov', 'Вот и докажи это делом, огузок!', 'Prove it with action then, rump!', [], ''),
]
WALK = [
    (0, None, '\'You are handling all the fish orders!\' "Ty" comes at the very end, which puts the weight on it: you and nobody else. "Zakazy po rybe" is literally \'orders on fish\'.'),
    (1, None, '\'Yes, Chef, I am ready to work!\' "Est" is the soldier\'s reply to an order, close to \'aye, sir\'. "Gotov k rabote", \'ready for work\', has "k", \'towards\', and -e on the end of "rabota".'),
    (2, None, '\'Let us see what kind of fish master you are.\' "Kakoy iz tebya master" is literally \'what master out of you\', a set way to doubt someone\'s skill. "Rybnyy" comes from "ryba", \'fish\', and works like \'fish\' in \'fish dish\'.'),
    (3, None, '\'I will prepare all dishes very quickly.\' "Prigotovlyu", \'I\'ll prepare\', promises the job will be done and finished. "Vse blyuda" is plural, and "vse" matches it.'),
    (4, None, '\'Maxim, take the order: two cod Florentines!\' "Treska", \'cod\', is a feminine noun, so \'two\' is "dve", and after it comes the genitive singular, "treski". "Po-florentiyski" means \'Florentine style\'.'),
    (5, None, '\'Yes, Chef, I am already starting to cook.\' "Uzhe" means \'already\'. "Nachinayu", \'I\'m starting\', is followed straight away by "gotovit", \'to cook\'.'),
    (6, None, '\'And two more portions of cod with almonds!\' "Eshchyo dve" is \'two more\'. After "s", \'with\', almonds get the ending -yom: "s mindalyom".'),
    (7, None, '\'But I already took two dishes!\' "Zhe" adds \'after all\', a note of protest. After "dva", \'two\', the noun goes into the genitive singular, so "blyudo" becomes "dva blyuda".'),
    (8, None, '\'Do not argue, Fedya managed somehow!\' "Ne spor" is a negative command, \'don\'t argue\'. "Spravlyalsya", \'was coping\', describes how Fedya used to get through it, shift after shift.'),
    (9, None, '\'I do not have enough fresh fish here.\' "Mne ne khvataet" is literally \'to me it\'s not enough\'. What\'s missing goes into the genitive: "svezhey ryby".'),
    (10, None, '\'Search in the storage and hustle faster!\' "Na sklade", \'in the storeroom\', has -e for \'where\'. "Krutis", \'hustle\', is literally \'spin yourself round\'.'),
    (11, None, '\'I will handle all orders myself.\' "Spravlyus" is \'I\'ll cope\', a one-time promise set against Fedya\'s "spravlyalsya". After "so", \'with\', the plural takes -ami: "so vsemi zakazami".'),
    (12, None, '\'Prove it with action then, rump!\' "Dokazhi" is the command \'prove\'. "Delom", \'with a deed\', is a case form of "delo", and Oguzok, \'rump\', is the chef\'s nickname for Max.'),
]
