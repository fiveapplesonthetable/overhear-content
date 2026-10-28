ID = 'kukhnya-s05e09-scene-01'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 9
SCENE = 1
TITLE = 'Перелом ребра  (A Rib Fracture)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'chef': 'anja', 'elena': 'angelina'}
LABELS = {'anya': 'Врач', 'chef': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = "Кухня (Kukhnya) S5.09"
SOURCE_FILE = 'sources/kukhnya/s05/e09.ru.srt'

INTRO = 'After a heavy wardrobe crashes down on Viktor Barinov, a doctor examines his ribs while Elena listens in. The physician confirms a hairline crack without bone displacement and asks how the injury happened.'

STORY = [
    ('elena', 'Доброе утро.', 'Good morning.', [(1, 'Доброе утро')], 'adapted'),
    ('elena', 'Иди потом позавтракай.', 'Go have breakfast later.', [(2, 'Иди потом позавтракай')], 'adapted'),
    ('anya', 'У вас неполный перелом ребра.', 'You have an incomplete rib fracture.', [(4, 'вас неполный перелом ребра')], 'adapted'),
    ('anya', 'Как я и предполагал.', 'Just as I assumed.', [(4, 'как я и предполагал')], 'adapted'),
    ('chef', 'Вы же сказали, трещина.', 'You said it was a crack.', [(5, 'сказали трещина')], 'adapted'),
    ('anya', 'Ну, это она и есть.', 'Well, that is what it is.', [(5, 'Ну, это она и есть')], 'adapted'),
    ('anya', 'Радуйтесь. Как была получена травма?', 'Be glad. How was the injury sustained?', [(6, 'Радуйтесь'), (6, 'была получена травма')], 'adapted'),
    ('chef', 'Только шкаф упал.', 'Only a wardrobe fell.', [(7, 'Только шкаф'), (8, 'Упал')], 'adapted'),
    ('anya', 'Большой?', 'A big one?', [(8, 'Большой')], 'adapted'),
    ('chef', 'Килограммов сто.', 'About a hundred kilograms.', [(9, 'Килограммов сто')], 'adapted'),
    ('elena', 'Даже побольше будет.', 'It is even heavier than that.', [(9, 'побольше будет')], 'adapted'),
    ('chef', 'Сто двадцать.', 'One hundred and twenty.', [(11, 'Сто двадцать')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Good morning.' Elena anchors the line on 'good', while 'morning' completes the thought."),
    (1, None, "'Go have breakfast later.' The grammar packs 'go' and 'have breakfast' into a tight, idiomatic kitchen exchange."),
    (2, None, "'You have an incomplete rib fracture.' Spoken Russian keeps this brisk, leaning on 'at' and finishing on 'rib'."),
    (3, None, "'Just as I assumed.' the doctor brings out the contrast between 'how' and 'I' in a few short words."),
    (4, None, "'You said it was a crack.' Spoken Russian keeps this brisk, leaning on 'you' and finishing on 'crack'."),
    (5, None, "'Well, that is what it is.' Notice how Russian expresses 'come on' and 'there is' with crisp inflection rather than helper words."),
    (6, None, "'Be glad. How was the injury sustained?' In Russian, the idea of 'rejoice' flows naturally into 'injury' without extra filler words."),
    (7, None, "'Only a wardrobe fell.' The grammar packs 'only' and 'fell' into a tight, idiomatic kitchen exchange."),
    (8, None, "'A big one?' Notice how Russian expresses 'big' and 'big' with crisp inflection rather than helper words. Chef Barinov answers right away."),
    (9, None, "'About a hundred kilograms.' The grammar packs 'kilograms' and 'hundred' into a tight, idiomatic kitchen exchange."),
    (10, None, "'It is even heavier than that.' The meaning hinges on 'even' working together with 'will be' in spoken Russian."),
    (11, None, "'One hundred and twenty.' In Russian, the idea of 'hundred' flows naturally into 'twenty' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes our opening scene at the clinic. Listen for the medical terms for a rib fracture and a crack, and how Viktor and Elena estimate the weight of the fallen wardrobe. See you in the next scene.'
CLOSING = ('chef', 'Это просто трещина!')
