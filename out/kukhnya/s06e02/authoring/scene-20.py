ID = 'kukhnya-s06e02-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 20
TITLE = "Ультиматум Баринова  (Barinov's Ultimatum)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "chef": "anja", "eleonora": "angelina"}
LABELS = {"chef": "Шеф", "eleonora": "Элеонора"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = 'In the final scene, Eleonora tells Barinov he does not need to resign now that the prefect is gone, and Barinov gives her a firm ultimatum: either he stays with his Michelin-contender auteur menu, or he walks.'

STORY = [
    ('chef', 'Что случилось, у нас проблемы?', 'What happened, do we have problems?', [(343, 'Что случилось? У нас проблемы?')], 'exact'),
    ('eleonora', 'Витя, тебе вовсе не обязательно увольняться.', 'Vitya, you do not have to resign at all.', [(345, 'Витя, тебе вовсе не обязательно увольняться')], 'exact'),
    ('chef', 'Пожалела меня?', 'Did you feel sorry for me?', [(346, 'Пожалела?')], 'adapted'),
    ('eleonora', 'Пожалела себя, я тебя уволю, а у меня Катя весь мозг съест.', 'I felt sorry for myself, if I fire you Katya will nag me to death.', [(346, 'Себя'), (347, 'Я тебя уволю'), (348, 'У меня Катя весь мозг съест')], 'adapted'),
    ('eleonora', 'Оставайся в ресторане.', 'Stay at the restaurant.', [(350, 'Оставайся')], 'adapted'),
    ('chef', 'Остаться с моим меню?', 'Stay with my menu?', [(350, 'С моим меню?')], 'adapted'),
    ('eleonora', 'Только давай вот без условий, хорошо?', "Only let's do this without conditions, alright?", [(351, 'Только давай вот без условий, хорошо?')], 'exact'),
    ('chef', 'Эля, мне шестой десяток.', 'Elya, I am in my fifties.', [(352, 'Эля, мне шестой десяток')], 'exact'),
    ('chef', 'Это меню — последний шанс получить звезду.', 'This menu is my last chance to get a star.', [(353, 'Это меню последний шанс получить звезду')], 'exact'),
    ('chef', 'Или я остаюсь с моим меню, или мы уходим оба.', 'Either I stay with my menu, or both my menu and I leave.', [(354, 'или я остаюсь с моим меню, или мы уходим оба')], 'adapted'),
    ('eleonora', 'Хорошо, оставайся.', 'Alright, stay.', [(355, 'Оставайся')], 'adapted'),
    ('chef', 'В субботу идем знакомиться с моей мамой.', 'On Saturday we are going to meet my mom.', [(357, 'субботу идем знакомиться с моей мамой')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'What happened, do we have problems?' Here the Russian phrasing highlights 'what' before landing on 'problems'."),
    (1, None, "'Vitya, you do not have to resign at all.' Eleonora anchors the line on 'to you', while 'to resign' completes the thought. Chef Barinov answers right away."),
    (2, None, "'Did you feel sorry for me?' The '-a' ending on the past-tense verb for 'felt sorry for' marks a female speaker or subject."),
    (3, None, "'I felt sorry for myself, if I fire you Katya will nag me to death.' In Russian, the idea of 'felt sorry for' flows naturally into 'will eat up' without extra filler words."),
    (4, None, "'Stay at the restaurant.' Eleonora pairs 'stay' with 'restaurant' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (5, None, "'Stay with my menu?' The meaning hinges on 'to remain' working together with 'menu' in spoken Russian."),
    (6, None, "'Only let's do this without conditions, alright?' In Russian, the idea of 'only' flows naturally into 'well' without extra filler words."),
    (7, None, "'Elya, I am in my fifties.' Here the Russian phrasing highlights 'Elya' before landing on 'decade'."),
    (8, None, "'This menu is my last chance to get a star.' Chef Barinov brings out the contrast between 'this' and 'menu' in a few short words."),
    (9, None, "'Either I stay with my menu, or both my menu and I leave.' The grammar packs 'or' and 'both' into a tight, idiomatic kitchen exchange."),
    (10, None, "'Alright, stay.' Notice how Russian expresses 'well' and 'stay' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (11, None, "'On Saturday we are going to meet my mom.' Here the Russian phrasing highlights 'Saturday' before landing on 'Mum'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Barinov wins the right to keep his auteur menu and chase his Michelin star, while Elena surprises him at home with a warm dedication in her new cookbook. See you next time!'
CLOSING = ("eleonora", "До завтра!")
