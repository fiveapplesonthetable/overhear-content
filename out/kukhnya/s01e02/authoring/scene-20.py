# Authoring module for kukhnya-s01e02-scene-20.
ID = 'kukhnya-s01e02-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 20
TITLE = "Разговор в кабинете шефа  (Talk in the Chef's Office)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "The knife is still missing, and the chef summons his sous-chef, Lyova, to his private office. He wants to know why his kitchen is in chaos, and he leaves nobody in any doubt about what will happen if the knife isn't found. This is the Russian first."
OPENER = "Let's go through the interrogation."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Lyova leaves the office with the weight of the whole crisis on his shoulders. Remember "slushayus\'", the answer of someone who knows he\'d better obey.'
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Лёва, зайди ко мне в кабинет!', 'Lyova, come to my office!', [(230, 'Лева, зайди ко мне')], ''),
    ('lyova', 'Да, шеф, я уже здесь.', 'Yes, chef, I am already here.', [(230, 'Да, шеф')], ''),
    ('barinov', 'Где мой любимый рыбий нож?', 'Where is my favorite fish knife?', [], ''),
    ('lyova', 'Мы везде ищем его, шеф.', 'We are looking for it everywhere, chef.', [(230, 'шеф')], ''),
    ('barinov', 'Ты су-шеф или кто такой?', 'Are you a sous-chef or who?', [], ''),
    ('lyova', 'Я слежу за порядком на кухне.', 'I maintain order in the kitchen.', [], ''),
    ('barinov', 'Ты очень плохо следишь за кухней!', 'You keep an eye on the kitchen very poorly!', [], ''),
    ('lyova', 'Все повара сейчас очень заняты поисками.', 'All the cooks are very busy with the search right now.', [], ''),
    ('barinov', 'Без этого ножа ресторан не работает!', 'Without this knife, the restaurant does not function!', [], ''),
    ('lyova', 'Мы проверили все столы и полки.', 'We checked all tables and shelves.', [], ''),
    ('barinov', 'Если нож не найдётся, всех уволю!', 'If the knife is not found, I will fire everyone!', [], ''),
    ('lyova', 'Шеф, мы обязательно найдём пропажу.', 'Chef, we will certainly find what went missing.', [], ''),
    ('barinov', 'Иди и найди его прямо сейчас!', 'Go and find it right now!', [], ''),
    ('lyova', 'Слушаюсь, шеф! Я найду нож.', 'Understood, chef! I will find the knife.', [(230, 'Да, шеф')], ''),
]
WALK = [
    (0, None, '\'Lyova, come to my office!\' "Zaydi" is "drop in", with "za-" for a quick stop. "K mne" becomes "ko mne", with an extra "o" to make it easier to say.'),
    (1, None, '\'Yes, chef, I am already here.\' "Ya uzhe zdes\'" is "I already here", with no "am", since Russian leaves it out.'),
    (2, None, '\'Where is my favorite fish knife?\' "Rybiy nozh" is a fish knife: "ryba", fish, becomes the describing word "rybiy". "Lyubimyy", favourite, shares its root with "lyubit\'", love.'),
    (3, None, '\'We are looking for it everywhere, chef.\' "Vezde" is "everywhere". "Ishchem" is "we look for", and "yego", it, never changes.'),
    (4, None, '\'Are you a sous-chef or who?\' "Su-shef" is borrowed from French. "Ili kto takoy" is "or who such", a rude way to ask "who do you think you are?".'),
    (5, None, '\'I maintain order in the kitchen.\' "Slezhu za" is "I keep an eye on", from "sled", a track. "Poryadok", order, is the root of "besporyadok", mess.'),
    (6, None, '\'You keep an eye on the kitchen very poorly!\' The chef throws back the same verb, now "sledish\'", "you keep an eye". "Plokho", poorly, is the opposite of "khorosho".'),
    (7, None, '\'All the cooks are very busy with the search right now.\' "Zanyaty" is "busy" for several people. "Poiski", the search, is plural in Russian, and "-ami" gives the "with".'),
    (8, None, '\'Without this knife, the restaurant does not function!\' "Bez", without, makes "etot nozh" become "etogo nozha". "Ne rabotayet", "doesn\'t work", does the job of "doesn\'t function".'),
    (9, None, '\'We checked all tables and shelves.\' "Proverili", checked, ends in -li for "we". "Stoly i polki" are both plurals: "stol" takes -y and "polka" takes -i.'),
    (10, None, '\'If the knife is not found, I will fire everyone!\' "Naydyotsya", "is found", ends in "-sya", as if the knife will find itself. "Vsekh uvolyu" is "all I\'ll fire".'),
    (11, None, '\'Chef, we will certainly find what went missing.\' "Obyazatel\'no", certainly, is built on "obyazat\'", oblige. "Propazha", what went missing, comes from "propast\'", to vanish.'),
    (12, None, '\'Go and find it right now!\' "Idi i naydi" is two commands joined by "i", and. "Pryamo seychas" is "straight now", meaning "right now".'),
    (13, None, '\'Understood, chef! I will find the knife.\' "Slushayus\'" is what a soldier says: "I\'m listening", meaning "yes, sir". "Naydu" is "I\'ll find".'),
]
