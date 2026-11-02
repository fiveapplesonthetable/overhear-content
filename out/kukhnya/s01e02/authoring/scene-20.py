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
OUTRO = 'Lyova leaves the office with the weight of the whole crisis on his shoulders. Remember his final obedient response, the answer of someone who knows he\'d better obey.'
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
    (0, None, ['\'Lyova, come to my office!\' ', ('barinov', 'зайди'), ' is "drop in", built from a little word at the start for a quick stop. ', ('barinov', 'ко мне'), ' has an extra letter to make it easier to say.']),
    (1, None, ['\'Yes, chef, I am already here.\' ', ('lyova', 'я уже здесь.'), ' translates to "I already here", with no "am", since the language leaves it out.']),
    (2, None, ['\'Where is my favorite fish knife?\' ', ('barinov', 'рыбий нож?'), ' is a fish knife: the word for fish becomes the describing word ', ('barinov', 'рыбий'), '. The word for favorite, ', ('barinov', 'любимый'), ',', ' favourite, shares its root with the action word for love.']),
    (3, None, ['\'We are looking for it everywhere, chef.\' Why ', ('lyova', 'его,'), ' which also translates to "him"? Because the word for knife belongs to the "he" group, and you use the "him" word for those things. ', ('lyova', 'ищем'), ' already means "we look for", so the word for "we" is there for emphasis.']),
    (4, None, ['\'Are you a sous-chef or who?\' ', ('barinov', 'су-шеф'), ' is borrowed from French. ', ('barinov', 'или кто такой?'), ' literally translates to "or who such", a rude way to ask "who do you think you are?".']),
    (5, None, ['\'I maintain order in the kitchen.\' ', ('lyova', 'слежу за'), ' translates to "I keep an eye on", built from the word for a track. The word for order, ', ('lyova', 'порядком'), ' is the root of the word for mess.']),
    (6, None, ['\'You keep an eye on the kitchen very poorly!\' The chef throws back the same action word, now ', ('barinov', 'следишь'), ' "you keep an eye". The word for poorly, ', ('barinov', 'плохо'), ' is the opposite of good.']),
    (7, None, ['\'All the cooks are very busy with the search right now.\' ', ('lyova', 'заняты'), ' is the word for "busy" for several people. ', ('lyova', 'поисками.'), ' the search, refers to more than one thing, and the ending gives the meaning of with.']),
    (8, None, ['\'Without this knife, the restaurant does not function!\' The little word for without, ', ('barinov', 'Без'), ' changes the ending of the phrase for this knife. ', ('barinov', 'не работает!'), ' "doesn\'t work", does the job of "doesn\'t function".']),
    (9, None, ['\'We checked all tables and shelves.\' ', ('lyova', 'проверили'), ' checked, ends with the letters for "we". The word for tables and the word for shelves, ', ('lyova', 'столы и полки.'), ' both refer to more than one thing and take those specific endings.']),
    (10, None, ['\'If the knife is not found, I will fire everyone!\' ', ('barinov', 'найдётся,'), ' "is found", ends with letters as if the knife will find itself. ', ('barinov', 'всех уволю!'), ' literally translates to "all I\'ll fire".']),
    (11, None, ['\'Chef, we will certainly find what went missing.\' ', ('lyova', 'обязательно'), ' certainly, is built from the action word for oblige. ', ('lyova', 'пропажу.'), ' what went missing, comes from the action word for to vanish.']),
    (12, None, ['\'Go and find it right now!\' ', ('barinov', 'Иди и найди'), ' is two commands joined by the little word for and. ', ('barinov', 'прямо сейчас!'), ' literally translates to "straight now", meaning "right now".']),
    (13, None, ['\'Understood, chef! I will find the knife.\' ', ('lyova', 'Слушаюсь,'), ' is what a soldier says: "I\'m listening", meaning "yes, sir". ', ('lyova', 'найду'), ' translates to "I\'ll find".']),
]
