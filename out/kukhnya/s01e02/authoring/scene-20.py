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
    (0, None, '\'Lyova, come to my office!\' "Zaydi" is "drop by", with "za-" meaning "on the way". "To me" becomes "ko mne" with an extra "o" for easier saying.'),
    (1, None, '\'Yes, chef, I am already here.\' "Already here" is two short words. Lyova needs no "am", since Russian leaves it out.'),
    (2, None, '\'Where is my favorite fish knife?\' "Fish knife" is "fish\'s knife", with the fish word in an adjective form. "Favorite" comes from "to love".'),
    (3, None, '\'We are looking for it everywhere, chef.\' "Everywhere" is one word. "Looking for" is the family of "ishchi", and "it" is the word that never changes.'),
    (4, None, '\'Are you a sous-chef or who?\' "Sous" is borrowed from French, as in "sous-chef". The second half, "or who such", is a rude way to ask "who are you?".'),
    (5, None, '\'I maintain order in the kitchen.\' "Slezhu za" means "keep an eye on", close to "follow after". "Order" is the word from "disorder" earlier.'),
    (6, None, '\'You keep an eye on the kitchen very poorly!\' The same verb comes back, now "you keep an eye". "Poorly" is "plokho", the opposite of "khorosho".'),
    (7, None, '\'All the cooks are very busy with the search right now.\' "Busy" is a short word, and "searches" is plural, from "poisk". "With" is shown by the ending "-ami".'),
    (8, None, '\'Without this knife, the restaurant does not function!\' "Without" is "bez", and it makes the knife take an "of" ending. "Works" is the word for "functions".'),
    (9, None, '\'We checked all tables and shelves.\' "Checked" ends in "-li" for "we". "Tables" and "shelves" are both plural.'),
    (10, None, '\'If the knife is not found, I will fire everyone!\' "Is found" ends in "-sya", as if the knife finds itself. "Everyone" takes the object form.'),
    (11, None, '\'Chef, we will certainly find what went missing.\' "Certainly" is the word from "obligatory". "What went missing" is a single noun, from the verb "to vanish".'),
    (12, None, '\'Go and find it right now!\' "Go and find" is two commands joined by "and". "Right now" is "straight now".'),
    (13, None, '\'Understood, chef! I will find the knife.\' "Slushayus\'" is what a soldier says: "I\'m listening", meaning "yes, sir". "I will find" is one word.'),
]
