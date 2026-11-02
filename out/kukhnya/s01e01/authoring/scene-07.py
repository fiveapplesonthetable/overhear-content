# Authoring module for kukhnya-s01e01-scene-07.
ID = 'kukhnya-s01e01-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 7
TITLE = 'Никогда не используй коньяк  (Never Use That Cognac)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Max is at the sauce station when Chef Barinov spots what he has done to the sauce: he has added cheap cognac. The chef is furious, and Max has to fix it. First, in Russian.'
OPENER = "Back through the chef's orders."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Barinov's orders all use short, sharp command forms, and now you can spot them. Max starts the sauce again, and this time the cognac stays on the shelf."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Никогда не используй этот дешёвый коньяк!', 'Never use that cheap cognac!', [(64, 'Никогда не используй этот')], ''),
    ('max', 'Да, шеф, я всё понял!', 'Yes, Chef, I understood everything!', [(64, 'Да, шеф')], ''),
    ('barinov', 'Ты испортил этим соус для мяса.', 'You ruined the meat sauce with this.', [(64, 'Да, шеф')], ''),
    ('max', 'Я просто хотел добавить яркий аромат.', 'I simply wanted to add a vivid aroma.', [(64, 'Да, шеф')], ''),
    ('barinov', 'Настоящий повар чувствует каждый вкус блюда.', 'A real chef feels every taste of the dish.', [(64, 'Да, шеф')], ''),
    ('max', 'Простите меня, шеф, я больше не буду.', 'Forgive me, Chef, I will not do it anymore.', [(64, 'Да, шеф')], ''),
    ('barinov', 'Возьми хорошую бутылку на верхней полке.', 'Take a good bottle on the top shelf.', [(64, 'Да, шеф')], ''),
    ('max', 'Сейчас я быстро принесу нужное вино.', 'Now I will quickly bring the needed wine.', [(64, 'Да, шеф')], ''),
    ('barinov', 'И начни готовить этот соус заново!', 'And begin making this sauce anew!', [(64, 'Да, шеф')], ''),
    ('max', 'Я всё сделаю правильно прямо сейчас.', 'I will do everything correctly right now.', [(64, 'Да, шеф')], ''),
    ('barinov', 'Внимательно смотри за температурой на плите.', 'Watch carefully the temperature on the stove.', [(64, 'Да, шеф')], ''),
    ('max', 'Да, шеф, я помню ваши правила!', 'Yes, Chef, I remember your rules!', [(64, 'Да, шеф')], ''),
]
WALK = [
    (0, None, ['\'Never use that cheap cognac!\' ', ('barinov', 'Никогда не'), ' is "never not", a double negative, and Russian insists on it. ', ('barinov', 'используй'), ' is a short, sharp "use!", and ', ('barinov', 'коньяк!'), ' is just cognac.']),
    (1, None, ['\'Yes, Chef, I understood everything!\' ', ('max', 'понял!'), ', "understood", is the past tense, and Russians use it where English says "got it". ', ('max', 'всё'), ', "everything", is the same word as in "and that\'s all?".']),
    (2, None, ['\'You ruined the meat sauce with this.\' ', ('barinov', 'испортил'), ' is "you ruined". ', ('barinov', 'этим'), ', "with this", needs no separate word for "with": the ending does it. And the word for meat becomes ', ('barinov', 'мяса.'), ' after "for".']),
    (3, None, ['\'I simply wanted to add a vivid aroma.\' With no -a on the end, ', ('max', 'хотел'), ', wanted, tells you a man is speaking, and the verb after it, ', ('max', 'добавить'), ', to add, stays in its dictionary form. ', ('max', 'яркий'), ' is the word for a bright colour, borrowed here for a strong smell.']),
    (4, None, ['\'A real chef feels every taste of the dish.\' ', ('barinov', 'Настоящий'), ' is "real", the word from "true love" in the night scene. ', ('barinov', 'вкус блюда.'), ' is "the taste of the dish": the word for dish swaps its ending to mean "of the dish".']),
    (5, None, ['\'Forgive me, Chef, I will not do it anymore.\' Max uses the formal ', ('max', 'Простите'), ', "forgive", with his boss. ', ('max', 'я больше не буду.'), ' is "I won\'t be anymore", and Russians leave it at that: a bare "won\'t be" means "I won\'t do it again".']),
    (6, None, ['\'Take a good bottle on the top shelf.\' ', ('barinov', 'Возьми'), ' is "take", an irregular command people simply learn. ', ('barinov', 'верхней'), ' is "top", from the peak, and the shelf becomes ', ('barinov', 'полке.'), ' after "on".']),
    (7, None, ['\'Now I will quickly bring the needed wine.\' ', ('max', 'Сейчас'), ' means "right now", though it often means "in a moment". ', ('max', 'принесу'), ' is "I will bring", the command of the bar scene with a different ending.']),
    (8, None, ['\'And begin making this sauce anew!\' ', ('barinov', 'начни'), ' is the command "begin". ', ('barinov', 'заново!'), ' is "anew", and you can hear the word for new inside it.']),
    (9, None, ['\'I will do everything correctly right now.\' ', ('max', 'сделаю'), ' is "I\'ll do", the form for getting a job finished rather than just working at it. ', ('max', 'прямо сейчас.'), ' is "straight now", this very second.']),
    (10, None, ['\'Watch carefully the temperature on the stove.\' ', ('barinov', 'Внимательно'), ', "carefully", comes from attention. ', ('barinov', 'смотри за'), ' is "keep an eye on", and the stove becomes ', ('barinov', 'плите.'), ' after "on".']),
    (11, None, ['\'Yes, Chef, I remember your rules!\' Max says ', ('max', 'ваши'), ', the polite "your", because nobody says informal you to the chef. ', ('max', 'правила!'), ', rules, is family to correctly: doing it right means doing it by the rules.']),
]
