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
    (0, None, '\'Wake up, Lyova, we have an inspection!\' "Ne spim", \'we\'re not sleeping\', is a Russian way of saying \'look alive\'. "U nas proverka", \'at us an inspection\', is how \'we have\' works.'),
    (1, None, '\'Chef, the inspector is already entering the hall!\' "Zakhodit", he\'s coming in, is the same word as "zakhodi", come in, just with the \'he\' ending. "V zal", into the hall, says where he\'s heading.'),
    (2, None, '\'Quickly clear everything extra off the tables.\' "Ubirayte", clear away, is said to the whole team, so it ends in -te. "Vsyo lishnee" is \'everything superfluous\', and so "stolov", off the tables, uses so, \'off\'.'),
    (3, None, '\'Where to hide these old products?\' Russian needs no \'should\': "kuda spryatat", \'where to hide\', is a plain dictionary form after the question word. "Kuda" asks \'where to\', for a destination.'),
    (4, None, '\'Carry all this straight into the refrigerator.\' "Nesi", carry, tells one person to "nesti", carry by hand. "Pryamo", straight, also means \'directly\' or \'right\'.'),
    (5, None, '\'And what to do with dirty aprons?\' "S gryaznymi fartukami", with dirty aprons, puts -ymi and -ami on the two words after s, \'with\'. "Chto delat", \'what to do\', is the classic Russian question.'),
    (6, None, '\'Lyova, immediately throw them into the wash!\' "Stirka" is washing clothes, from "stirat"; dishes and floors take "myt" instead. "Brosay", throw, is what you\'d say for tossing anything into a pile.'),
    (7, None, '\'I already sent Senya for cloths.\' "Za tryapkami" is \'for rags\', in the sense of \'to fetch rags\'. Senya becomes "Senyu" because he\'s the one sent.'),
    (8, None, '\'Wipe the floor, it is too slippery!\' "Vytrite", wipe, is said to everyone, so it has -te. "Slishkom", too, goes before any adjective, like "slishkom dorogo", too expensive.'),
    (9, None, '\'The cooks are already washing their workstations.\' "Moyut", they wash, is from "myt", the word for washing plates, hands and floors. "Svoi", their own, points back at the cooks.'),
    (10, None, '\'The kitchen must be ideally clean!\' "Dolzhna", must, ends in -a to match "kukhnya". After "byt", "chistaya", clean, turns into "chistoy".'),
    (11, None, '\'We will manage to do everything in time, chef!\' "Uspeem", we\'ll make it in time, has no neat English equivalent. "Vovremya", on time, is v plus "vremya", \'in time\', written as one word.'),
    (12, None, '\'To your stations, the inspector is already here!\' "Po mestam", \'to places\', is a call with no verb, like \'places, everyone\' in a theatre. "Zdes", here, is where you are right now.'),
]
