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
    (0, None, '\'Thank you everyone, the session is over.\' Eleonora emphasizes this clear term on cue: "spasibo" means "thank you", and it carries the main weight of what Eleonora is saying.'),
    (1, None, "'Are we going to go through this every morning now?' Barinov hands over this warning without pause: Russian keeps the exact word order of a normal statement here, turning it into a question for Louis purely through rising pitch at the end."),
    (2, None, "'Studies showed that the day should start with classical music.' Eleonora fires back bluntly without any doubt, grounding the moment in plain reality."),
    (3, None, '\'Then labor productivity increases.\' Eleonora centers this sharp piece right here: "proizvoditelnost" means "productivity", and it carries the main weight of what Eleonora is saying.'),
    (4, None, '\'I simply did not understand the idea right away.\' Barinov voices that remark beside Eleonora: the little word "prosto" ("simply, just") works like a shrug in the sentence, making a big claim sound effortless.'),
    (5, None, "'And it made me want my mom to hug me.' Louis answers at once beside Eleonora, leaving no doubt about where he stands."),
    (6, None, '\'Thank you everyone, let\'s get to work.\' Eleonora picks this sharp detail at once: "spasibo" means "thank you", and it carries the main weight of what Eleonora is saying.'),
    (7, None, "'Eleonora Andreyevna, my father wrote to me.' Louis continues openly around Eleonora, to clear the air between them once and for all."),
    (8, None, "'There was an inspector at their restaurant.' Louis holds firm promptly with a shrug, so Barinov knows he is not just making small talk."),
    (9, None, '\'If he is in Moscow, then he will stop by our place too.\' Louis focuses on one sharp touch on cue: "zaydet" means "will stop by" (from "zayti"), giving the line its exact edge.'),
    (10, None, "'This is our chance to get a star!' Barinov steps in firmly without holding back, to clear the air between them once and for all."),
    (11, None, "'Be ready today!' Eleonora responds decisively in their talk, refusing to let the moment slip past."),
]
