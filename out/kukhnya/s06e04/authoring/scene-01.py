# Authoring module for kukhnya-s06e04-scene-01.
ID = 'kukhnya-s06e04-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 1
TITLE = 'Классическая музыка и новость об инспекторе  (Classical Music and News of the Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'Eleonora starts the morning by making the hotel staff listen to classical music to boost productivity, right before pastry chef Louis announces that a Michelin inspector is in Moscow!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the entire hotel on high alert for a secret Michelin inspector, every foreign guest immediately becomes a suspect. Until next time!'
CLOSING = ('louis', 'Хорошего дня!')
STORY = [
    ('eleonora', 'Всем спасибо, урок окончен.', 'Thank you everyone, the session is over.', [(1, 'Всем спасибо'), (1, 'окончен')], 'adapted'),
    ('barinov', 'А мы теперь это каждое утро будем переживать?', 'Are we going to go through this every morning now?', [(2, 'каждое утро будем переживать?')], 'adapted'),
    ('eleonora', 'Исследования показали, что день надо начинать с классической музыки.', 'Studies showed that the day should start with classical music.', [(3, 'Исследования показали'), (3, 'день начинать с классической музыки')], 'adapted'),
    ('eleonora', 'Тогда производительность труда увеличивается.', 'Then labor productivity increases.', [(4, 'производительность труда увеличивается')], 'adapted'),
    ('barinov', 'Я просто идею не сразу понял.', 'I simply did not understand the idea right away.', [(7, 'Я просто идею не сразу понял')], 'exact'),
    ('louis', 'А мне захотелось, чтобы меня мама обняла.', 'And it made me want my mom to hug me.', [(8, 'захотелось'), (8, 'чтобы меня мама обняла')], 'adapted'),
    ('eleonora', 'Всем спасибо, работаем.', "Thank you everyone, let's get to work.", [(9, 'Всем спасибо'), (10, 'Работаем')], 'adapted'),
    ('louis', 'Элеонора Андреевна, мне написал отец.', 'Eleonora Andreyevna, my father wrote to me.', [(11, 'Андреевна, мне написал отец')], 'adapted'),
    ('louis', 'У них в ресторане был инспектор.', 'There was an inspector at their restaurant.', [(12, 'У них в ресторане был инспектор')], 'exact'),
    ('louis', 'Если он в Москве, то он и к нам зайдет.', 'If he is in Moscow, then he will stop by our place too.', [(13, 'Если он в Москве, то он и к нам зайдет')], 'exact'),
    ('barinov', 'Это наш шанс получить звезду!', 'This is our chance to get a star!', [(12, 'инспектор')], 'adapted'),
    ('eleonora', 'Будьте готовы сегодня!', 'Be ready today!', [(10, 'Работаем')], 'adapted'),
]
WALK = [
    (0, None, "'Thank you everyone, the session is over.' Eleonora tells Barinov that everyone the session is without dressing it up."),
    (1, None, '\'Are we going to go through this every morning now?\' Checking whether they going to go through this every morning now is how Barinov puts Eleonora on the spot. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, '\'Studies showed that the day should start with classical music.\' Mentioning that studies showed that the day should start with classical music moves the talk in a new direction. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (3, None, "'Then labor productivity increases.' Over the kitchen and the hotel, Eleonora answers Barinov without a second thought."),
    (4, None, "'I simply did not understand the idea right away.' Because he simply did not understand the idea right away, Barinov treats the matter as settled."),
    (5, None, "'And it made me want my mom to hug me.' Explaining that it made him want his to hug him lays the cards on the table for Barinov."),
    (6, None, "'Thank you everyone, let's get to work.' Eleonora mentions that everyone let them get to work so Barinov sees what is at stake."),
    (7, None, "'Eleonora Andreyevna, my father wrote to me.' Claiming that his father wrote to him sounds confident, even if Barinov has doubts."),
    (8, None, "'There was an inspector at their restaurant.' Pointing out that there was an inspector at their restaurant gives Barinov a sobering reality check."),
    (9, None, "'If he is in Moscow, then he will stop by our place too.' Louis explains that if he is in Moscow then he will stop by their place, keeping his voice calm and direct."),
    (10, None, '\'This is our chance to get a star!\' Barinov insists that this is their chance to get a star, leaving Eleonora no room to argue. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (11, None, "'Be ready today!' Around the morning and shift, Eleonora makes her point loud and clear. Russian puts the key word right up front so her emotion lands on the first beat."),
]
