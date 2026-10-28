ID = 'kukhnya-s03e18-scene-15'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 18
SCENE = 15
TITLE = 'Оговорка по Фрейду и костёр  (A Freudian Slip and a Bonfire)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'vika': 'anja', 'chef': 'angelina'}
LABELS = {'anya': 'Макс', 'vika': 'Вика', 'chef': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S3.18"
SOURCE_FILE = 'sources/kukhnya/s03/e18.ru.srt'

INTRO = "Flush with relief after talking to Katya, Max asks Vika what she is doing after work—but accidentally calls her 'Katya'! Before he can recover, a tipsy Chef Barinov announces the public burning of the new menu."

STORY = [
    ('anya', 'Костя, в общем, с Катей я всё разрулил.', 'Kostya, anyway, I sorted everything out with Katya.', [(226, 'с Катей я всё разрулил')], 'adapted'),
    ('anya', 'Слушай, Катя, то есть Вика, извини меня!', 'Listen, Katya, I mean Vika, forgive me!', [(228, 'то есть, Вик, извини')], 'adapted'),
    ('anya', 'Скажи, что ты делаешь сегодня после работы?', 'Tell me, what are you doing today after work?', [(228, 'что ты делаешь сегодня'), (229, 'После работы')], 'adapted'),
    ('vika', 'Вика сегодня вечером после работы очень занята.', 'Vika is very busy tonight after work.', [(229, 'Вика сегодня занята')], 'adapted'),
    ('vika', 'А вот насчёт Кати я ничего не знаю.', 'As for Katya, however, I do not know anything.', [(230, 'А насчёт Кати не знаю')], 'adapted'),
    ('anya', 'Ну вот, опять я всё себе испортил!', 'Well great, I ruined everything for myself again!', [(231, 'Вообще')], 'adapted'),
    ('vika', 'Макс, как ты вообще всё это делаешь?', 'Max, how on earth do you do all this?', [(232, 'Как это ты делаешь')], 'adapted'),
    ('anya', 'Честное слово, я уже и сам в шоке.', 'Honestly, I am in shock myself already.', [(233, 'Сам в шоке')], 'adapted'),
    ('chef', 'Внимание всем поварам! Быстро слушайте меня!', 'Attention all chefs! Listen to me quickly!', [(234, 'Внимание всем')], 'adapted'),
    ('chef', 'Впервые на этой кухне мы сжигаем меню!', 'For the first time in this kitchen we are burning a menu!', [(235, 'Впервые на этой кухне будет')], 'adapted'),
    ('chef', 'Мы сейчас сжигаем листы этого нового меню.', 'We are burning the pages of this new menu right now.', [(236, 'Нового меню')], 'adapted'),
    ('chef', 'Меню обвиняется в измене французской кухне с чебуреками!', 'The menu is accused of betraying French cuisine with chebureki!', [(237, 'Меню обвиняется в измене французской кухни')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Kostya, anyway, I sorted everything out with Katya.' Notice how Russian expresses 'Kostya' and 'sorted out' with crisp inflection rather than helper words."),
    (1, None, "'Listen, Katya, I mean Vika, forgive me!' Here the Russian phrasing highlights 'listen' before landing on 'me'."),
    (2, None, "'Tell me, what are you doing today after work?' The meaning hinges on 'say' working together with 'job' in spoken Russian."),
    (3, None, "'Vika is very busy tonight after work.' The grammar packs 'Vika' and 'busy' into a tight, idiomatic kitchen exchange."),
    (4, None, "'As for Katya, however, I do not know anything.' Vika brings out the contrast between 'and' and 'here' in a few short words."),
    (5, None, "'Well great, I ruined everything for myself again!' The '-l' ending on the verb meaning 'ruined' places the action in the masculine past tense."),
    (6, None, "'Max, how on earth do you do all this?' The meaning hinges on 'Max' working together with 'are doing' in spoken Russian. Max answers right away."),
    (7, None, "'Honestly, I am in shock myself already.' Notice how Russian expresses 'honest' and 'in shock' with crisp inflection rather than helper words."),
    (8, None, "'Attention all chefs! Listen to me quickly!' The grammar packs 'attention' and 'me' into a tight, idiomatic kitchen exchange."),
    (9, None, "'For the first time in this kitchen we are burning a menu!' Notice how Russian expresses 'for the first time' and 'menu' with crisp inflection rather than helper words."),
    (10, None, "'We are burning the pages of this new menu right now.' Chef Barinov anchors the line on 'we', while 'menu' completes the thought."),
    (11, None, "'The menu is accused of betraying French cuisine with chebureki!' Notice the reflexive suffix on the verb meaning 'is accused', turning the action back on the subject."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung by Max's speech, Chef Barinov lights the corporate menu ablaze right in the middle of the kitchen."
CLOSING = ('chef', 'Мы сжигаем это новое меню!')
