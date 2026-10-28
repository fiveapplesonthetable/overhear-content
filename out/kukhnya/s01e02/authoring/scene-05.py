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
    (1, None, '\'You can\'t buy such a knife in a hurry.\' "Po-bystromu" is "in a quick way", from "bystro", quickly. Then "ne poluchitsya", "it won\'t work out", which Russians say whenever something can\'t be done.'),
    (2, None, '\'And how much does it cost?\' "Skol\'ko stoit" is the shop question, "how much costs". Nastya calls the knife "on", "he", because "nozh" is a masculine word.'),
    (3, None, '\'This is an expensive Japanese knife.\' "Dorogoy" does two jobs: it means "expensive" and also "dear", as in a dear friend. And there\'s no "is", just "eto", this, and the rest.'),
    (4, None, '\'The chef ordered it for a very long time.\' "Zakazyval", "ordered", comes from "zakaz", an order. "Yego", "it", is the same word as "him" and "his", and it never changes.'),
    (5, None, '\'And is it very sharp?\' "Ostryy" means "sharp" and also "spicy", so it\'s good for knives and for food. Context tells you which.'),
    (6, None, '\'The sharpest knife in the kitchen.\' Put "samyy" in front of a describing word and you get "the most": "samyy ostryy", "the most sharp". It works with any describing word.'),
    (7, None, '\'Where could it possibly be?\' "Mozhet byt\'" is "maybe", but here the two words keep their real meaning, "can be". "Zhe" after "gde" adds the "possibly".'),
    (8, None, '\'We already looked everywhere.\' "Uzhe", already, and "vezde", everywhere, are small words you\'ll use constantly. "Iskali", "looked for", is the past of "iskat\'", the same verb as the command "ishchi" below.'),
    (9, None, '\'Maybe someone took it home?\' "Mozhet" on its own can mean "maybe". "Kto-to" is "kto", who, plus "-to", which makes it "someone".'),
    (10, None, '\'Nobody would dare do that.\' "Nikto ne", "nobody not", is the double negative again. "Posmeyet", "will dare", grows from "smet\'", to dare.'),
    (11, None, '\'The chef will fire everyone immediately.\' "Srazu" is the everyday "immediately". "Vse", everyone, becomes "vsekh" because they\'re the ones being fired.'),
    (12, None, '\'Come on, look for the knife quickly.\' "Davay" is a friendly "come on". "Ishchi" is the command "look for", and "skoreye" is "quicker".'),
    (13, None, '\'All right. I will look here.\' The "po-" at the front of "I will look" gives it the sense of a quick look. "Here" is "zdes\'".'),
]
