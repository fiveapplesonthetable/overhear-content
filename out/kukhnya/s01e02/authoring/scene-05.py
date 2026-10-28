# Authoring module for kukhnya-s01e02-scene-05.
ID = 'kukhnya-s01e02-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Японский нож  (The Japanese Knife)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "While everyone searches, Nastya asks Senya why the chef can't just buy another knife. Senya explains what makes this one so special. Here is their talk in Russian first."
OPENER = "Now let's see why this knife is special."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So it\'s a very sharp, very expensive Japanese knife, and the chef has every reason to panic. Listen for "ishchi", the command "look for it", because it comes back.'
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('nastya', 'Почему нельзя купить такой нож?', "Why can't we buy such a knife?", [], ''),
    ('senya', 'По-быстрому такой нож купить не получится.', "You can't buy such a knife in a hurry.", [(95, 'быстрому такой нож купить не получится')], ''),
    ('nastya', 'А сколько он стоит?', 'And how much does it cost?', [], ''),
    ('senya', 'Это дорогой японский нож.', 'This is an expensive Japanese knife.', [], ''),
    ('senya', 'Шеф заказывал его очень долго.', 'The chef ordered it for a very long time.', [], ''),
    ('nastya', 'И он очень острый?', 'And is it very sharp?', [], ''),
    ('senya', 'Самый острый нож на кухне.', 'The sharpest knife in the kitchen.', [], ''),
    ('nastya', 'Где же он может быть?', 'Where could it possibly be?', [], ''),
    ('senya', 'Мы уже везде искали.', 'We already looked everywhere.', [], ''),
    ('nastya', 'Может, кто-то взял его домой?', 'Maybe someone took it home?', [], ''),
    ('senya', 'Никто не посмеет это сделать.', 'Nobody would dare do that.', [], ''),
    ('senya', 'Шеф сразу всех уволит.', 'The chef will fire everyone immediately.', [], ''),
    ('senya', 'Давай нож ищи скорее.', 'Come on, look for the knife quickly.', [(97, 'Давай нож ищи')], ''),
    ('nastya', 'Хорошо. Я посмотрю здесь.', 'All right. I will look here.', [], ''),
]
WALK = [
    (0, None, '\'Why can\'t we buy such a knife?\' "Nel\'zya" is a very useful word meaning "it\'s not allowed" or "it\'s impossible". Put "pochemu" in front and you can ask why anything can\'t be done.'),
    (1, None, '\'You can\'t buy such a knife in a hurry.\' The first word is "in a quick way". Then "ne poluchitsya", literally "it won\'t work out", which Russians say whenever something can\'t be done.'),
    (2, None, '\'And how much does it cost?\' The shop question: "how much" and then "costs". Nastya says "he" for the knife, because "nozh" is a masculine word.'),
    (3, None, '\'This is an expensive Japanese knife.\' One word does two jobs: it means "expensive" and also "dear", as in a dear friend. And there\'s no "is" here, just "this" and the rest.'),
    (4, None, '\'The chef ordered it for a very long time.\' The word for "ordered" is close to the noun "zakaz", an order. "It" is the same word that means "him" or "his", and it never changes.'),
    (5, None, "'And is it very sharp?' The Russian word for sharp also means spicy, so it's good for knives and for food. Context tells you which."),
    (6, None, '\'The sharpest knife in the kitchen.\' Put "samyy" in front of a describing word and you get "the most": "the most sharp". It\'s easy to remember, and works with any word.'),
    (7, None, '\'Where could it possibly be?\' You may know "mozhet byt\'" as "maybe", but taken apart the two words mean "can be". A tiny "zhe" in the middle adds the "possibly".'),
    (8, None, '\'We already looked everywhere.\' "Everywhere" is a single word, "vezde", and "already" is the small word you\'ve heard before. "Looked for" is from the same family as the command "ishchi" below.'),
    (9, None, '\'Maybe someone took it home?\' Russian can say "maybe" with just the first of those two words. Add "-to" to "who" and you get "someone".'),
    (10, None, '\'Nobody would dare do that.\' "Will dare" is one word. Then "nobody" and "not" together, the double negative again, and "do this" at the end.'),
    (11, None, '\'The chef will fire everyone immediately.\' "Immediately" is one word, "srazu". "Will fire" is also one word, and "everyone" takes a new ending because it\'s the object.'),
    (12, None, '\'Come on, look for the knife quickly.\' The first word is a friendly "come on". "Ishchi" is the command "look for", and "skoreye" is "faster".'),
    (13, None, '\'All right. I will look here.\' The "po-" at the front of "I will look" gives it the sense of a quick look. "Here" is "zdes\'".'),
]
