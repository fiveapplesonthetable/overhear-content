# Authoring module for kukhnya-s01e05-scene-06.
ID = 'kukhnya-s01e05-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = 'Кулинарная битва  (A Culinary Battle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "In the Claude Monet kitchen, Max and Fedya have agreed to a cook-off, and everyone has heard. Senya, the meat cook and Fedya's partner in pranks, is taking the bets. The main ingredient will be cod, the fish someone thawed too early. Just enjoy the noise in Russian first."
OPENER = "Let's go back. Senya talks like a market trader, and Fedya like a boxer before a fight."
TRANSITION = 'Same lines, no pauses this time.'
OUTRO = 'Betting talk is simple in Russian: "stavki" for the bets, "stavit na" for \'bet on\', and "vremya poshlo" when it starts. The cod is on the board.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('senya', 'Итак, повара, делаем ставки и записываемся!', 'So, cooks, place bets and sign up!', [(85, 'Итак, ставим и записываемся')], ''),
    ('senya', 'Сейчас Федя и Макс приготовят по блюду.', 'Now Fedya and Max will prepare a dish each.', [(86, 'Сейчас Федя'), (86, 'будут готовить по одному блюду')], ''),
    ('senya', 'А шеф попробует и выберет победителя.', 'And the chef will taste and choose the winner.', [(87, 'А шеф попробует'), (87, 'кто из них победил')], ''),
    ('max', 'Какой главный продукт для нашего блюда?', 'What is the main ingredient for our dish?', [(88, 'Выбираем главный продукт для блюда')], ''),
    ('senya', 'Главный продукт сегодняшнего конкурса — треска!', "The main ingredient of today's contest is cod!", [(88, 'главный продукт')], ''),
    ('fedya', 'Тебе конец, огузок!', 'You are finished, runt!', [(89, 'И конец')], ''),
    ('fedya', 'Я готовил всю рыбу в океане!', 'I have cooked all the fish in the ocean!', [(89, 'Я готовил всю рыбу, которая плавает в океане')], ''),
    ('max', 'Рыбу я тоже умею готовить.', 'I also know how to cook fish.', [], ''),
    ('fedya', 'Посмотрим на твои жалкие умения.', 'We will see your pathetic skills.', [], ''),
    ('senya', 'Кто ставит пятьсот рублей на Федю?', 'Who bets five hundred rubles on Fedya?', [(95, 'пятьсот рублей'), (95, 'для ставки')], ''),
    ('fedya', 'Все повара на кухне ставят на меня.', 'All the cooks in the kitchen bet on me.', [(90, 'Спасибо')], ''),
    ('max', 'А я всё равно докажу свой талант!', 'And I will prove my talent anyway!', [], ''),
    ('senya', 'Время пошло, начинаем готовить прямо сейчас!', 'Time has started, begin cooking right now!', [], ''),
    ('max', 'Я сделаю самый лучший соус.', 'I will make the best sauce.', [], ''),
]
WALK = [
    (0, None, '\'So, cooks, place bets and sign up!\' "Delaem" and "zapisyvaemsya" are \'we\' forms, used here as \'let\'s\'. "Stavki" are the bets, and the -sya on "zapisyvaemsya" means they\'re signing themselves up.'),
    (1, None, '\'Now Fedya and Max will prepare a dish each.\' "Po" in front of "blyudu" means \'one each\'. "Prigotovyat" ends in -yat, the \'they will\' form.'),
    (2, None, '\'And the chef will taste and choose the winner.\' "Poprobuet" and "vyberet" are both future. "Pobeditel", \'winner\', comes from "pobeda", \'victory\', as in "Den Pobedy", Victory Day, on the ninth of May.'),
    (3, None, '\'What is the main ingredient for our dish?\' "Glavnyy", \'main\', grows from "glava", \'head\'. After "dlya", \'for\', the dish becomes "nashego blyuda".'),
    (4, None, '\'The main ingredient of today\'s contest is cod!\' The dash stands in for \'is\'. "Segodnyashnego konkursa" means \'of today\'s contest\', with "segodnya", \'today\', inside the adjective.'),
    (5, None, '\'You are finished, runt!\' Literally \'to you an end\'. "Tebe konets" is the stock Russian way to say \'you\'re done for\'.'),
    (6, None, '\'I have cooked all the fish in the ocean!\' Fedya is the fish cook, so the boast fits. "V okeane" takes -e because it\'s a place, and "rybu" takes -u as the thing cooked.'),
    (7, None, '\'I also know how to cook fish.\' "Umeyu" is \'I know how\', for a skill. Max puts "rybu" first, like saying \'fish, I can do too\'.'),
    (8, None, '\'We will see your pathetic skills.\' "Umeniya", \'skills\', comes from "umet", so Fedya throws Max\'s own "umeyu" back at him. "Posmotrim na" means \'we\'ll look at\'.'),
    (9, None, '\'Who bets five hundred rubles on Fedya?\' "Pyatsot", \'five hundred\', joins "pyat" and "sto". You bet "na" someone, and Fedya becomes "Fedyu" after it.'),
    (10, None, '\'All the cooks in the kitchen bet on me.\' The same "na", now with "na menya", \'on me\'. "Stavyat" is the \'they\' form of "stavit".'),
    (11, None, '\'And I will prove my talent anyway!\' "Vsyo ravno", \'all the same\', means \'anyway\'. "Svoy" is the \'my\' you use when the owner is the one doing the action.'),
    (12, None, '\'Time has started, begin cooking right now!\' "Vremya poshlo", literally \'time went\', is the call that starts the clock. "Pryamo seychas", \'right now\', is worth keeping.'),
    (13, None, '\'I will make the best sauce.\' "Samyy luchshiy" is \'the most best\', a doubled-up superlative that\'s normal in everyday Russian. "Sous" comes from French.'),
]
