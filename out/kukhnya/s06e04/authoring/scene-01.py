ID = 'kukhnya-s06e04-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 1
TITLE = "Классическая музыка и новость об инспекторе  (Classical Music and News of the Inspector)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "louis": "anja", "eleonora": "angelina"}
LABELS = {"louis": "Луи", "eleonora": "Элеонора"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'

INTRO = 'Eleonora starts the morning by making the hotel staff listen to classical music to boost productivity, right before pastry chef Louis announces that a Michelin inspector is in Moscow!'

STORY = [
    ('eleonora', 'Всем спасибо, урок окончен.', 'Thank you everyone, the session is over.', [(1, 'Всем спасибо'), (1, 'окончен')], 'adapted'),
    ('louis', 'А мы теперь это каждое утро будем переживать?', 'Are we going to go through this every morning now?', [(2, 'каждое утро будем переживать?')], 'adapted'),
    ('eleonora', 'Исследования показали, что день надо начинать с классической музыки.', 'Studies showed that the day should start with classical music.', [(3, 'Исследования показали'), (3, 'день начинать с классической музыки')], 'adapted'),
    ('eleonora', 'Тогда производительность труда увеличивается.', 'Then labor productivity increases.', [(4, 'производительность труда увеличивается')], 'adapted'),
    ('louis', 'Я просто идею не сразу понял.', 'I simply did not understand the idea right away.', [(7, 'Я просто идею не сразу понял')], 'exact'),
    ('louis', 'А мне захотелось, чтобы меня мама обняла.', 'And it made me want my mom to hug me.', [(8, 'захотелось'), (8, 'чтобы меня мама обняла')], 'adapted'),
    ('eleonora', 'Всем спасибо, работаем.', "Thank you everyone, let's get to work.", [(9, 'Всем спасибо'), (10, 'Работаем')], 'adapted'),
    ('louis', 'Элеонора Андреевна, мне написал отец.', 'Eleonora Andreyevna, my father wrote to me.', [(11, 'Андреевна, мне написал отец')], 'adapted'),
    ('louis', 'У них в ресторане был инспектор.', 'There was an inspector at their restaurant.', [(12, 'У них в ресторане был инспектор')], 'exact'),
    ('louis', 'Если он в Москве, то он и к нам зайдет.', 'If he is in Moscow, then he will stop by our place too.', [(13, 'Если он в Москве, то он и к нам зайдет')], 'exact'),
    ('louis', 'Это наш шанс получить звезду!', 'This is our chance to get a star!', [(12, 'инспектор')], 'adapted'),
    ('eleonora', 'Будьте готовы сегодня!', 'Be ready today!', [(10, 'Работаем')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Thank you everyone, the session is over.' Eleonora anchors the line on 'to everyone', while 'finished' completes the thought."),
    (1, None, "'Are we going to go through this every morning now?' The meaning hinges on 'and' working together with 'to experience' in spoken Russian."),
    (2, None, "'Studies showed that the day should start with classical music.' The plural past ending '-li' on the verb for 'showed' covers a group or the polite 'you'."),
    (3, None, "'Then labor productivity increases.' Eleonora brings out the contrast between 'then' and 'productivity' in a few short words."),
    (4, None, "'I simply did not understand the idea right away.' Spoken Russian keeps this brisk, leaning on 'I' and finishing on 'understood'."),
    (5, None, "'And it made me want my mom to hug me.' In Russian, the idea of 'and' flows naturally into 'hugged' without extra filler words. Eleonora answers right away."),
    (6, None, "'Thank you everyone, let's get to work.' Here the Russian phrasing highlights 'to everyone' before landing on 'let's work'."),
    (7, None, "'Eleonora Andreyevna, my father wrote to me.' The grammar packs 'Eleonora' and 'father' into a tight, idiomatic kitchen exchange."),
    (8, None, "'There was an inspector at their restaurant.' Spoken Russian keeps this brisk, leaning on 'at' and finishing on 'inspector'."),
    (9, None, "'If he is in Moscow, then he will stop by our place too.' The grammar packs 'if' and 'will stop by' into a tight, idiomatic kitchen exchange."),
    (10, None, "'This is our chance to get a star!' The meaning hinges on 'this' working together with 'star' in spoken Russian."),
    (11, None, "'Be ready today!' An emphatic spoken line centered on the verb meaning 'be'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'With the entire hotel on high alert for a secret Michelin inspector, every foreign guest immediately becomes a suspect. Until next time!'
CLOSING = ("louis", "Хорошего дня!")
