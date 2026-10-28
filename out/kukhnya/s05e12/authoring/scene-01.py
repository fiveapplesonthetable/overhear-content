ID = 'kukhnya-s05e12-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 1
TITLE = "Ночной звонок и тушёнка  (A Late-Night Call and Stewed Meat)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'

INTRO = 'Max reflects on the belief that thoughts are material: if you think about something constantly, it is bound to come true. In the middle of the night, his phone rings and pregnant Vika asks him to bring her canned stewed meat.'

STORY = [
    ('anya', 'Говорят, что мысли материальны.', 'They say that thoughts are material.', [(1, 'Говорят, что мысли')], 'adapted'),
    ('anya', 'Если о чём-то постоянно думать, это обязательно произойдёт.', 'If you think about something constantly, it will definitely happen.', [(2, 'Если о чем-то постоянно думать, это обязательно произойдет')], 'adapted'),
    ('anya', 'Алло, Вика?', 'Hello, Vika?', [(3, 'Алло'), (4, 'Вика, алло')], 'adapted'),
    ('vika', 'Алло, Макс.', 'Hello, Max.', [(4, 'алло. Макс')], 'adapted'),
    ('anya', 'Да, что-то случилось?', 'Yes, did something happen?', [(5, 'Да что-то случилось')], 'adapted'),
    ('anya', 'Ну, не молчи.', 'Well, do not stay silent.', [(6, 'Ну, не молчи')], 'adapted'),
    ('vika', 'Можешь мне кое-что привезти?', 'Can you bring me something?', [(6, 'Можешь мне кое-что привезти')], 'adapted'),
    ('anya', 'Да, конечно!', 'Yes, of course!', [(7, 'Да, да, конечно')], 'adapted'),
    ('anya', 'Что, лекарства?', 'What is it, medicine?', [(7, 'Что, лекарства')], 'adapted'),
    ('vika', 'Тушёнку.', 'Canned stewed meat.', [(8, 'Тушонку')], 'adapted'),
    ('anya', 'Что?', 'What?', [(9, 'Что')], 'adapted'),
    ('vika', 'Привези мне тушёнку, пожалуйста.', 'Bring me canned stewed meat, please.', [(6, 'привезти'), (8, 'Тушонку')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'They say that thoughts are material.' Max anchors the line on 'say', while 'material' completes the thought."),
    (1, None, "'If you think about something constantly, it will definitely happen.' The grammar packs 'if' and 'to happen' into a tight, idiomatic kitchen exchange."),
    (2, None, "'Hello, Vika?' Max raises the pitch on 'Vika' to turn the phrase into a direct spoken question. Vika answers right away."),
    (3, None, "'Hello, Max.' In Russian, the idea of 'hello' flows naturally into 'Max' without extra filler words."),
    (4, None, "'Yes, did something happen?' Spoken Russian keeps this brisk, leaning on 'yes' and finishing on 'happened'."),
    (5, None, "'Well, do not stay silent.' Spoken Russian keeps this brisk, leaning on 'come on' and finishing on 'be silent'. Vika answers right away."),
    (6, None, "'Can you bring me something?' Vika anchors the line on 'can', while 'to bring' completes the thought."),
    (7, None, "'Yes, of course!' Max brings out the contrast between 'yes' and 'of course' in a few short words."),
    (8, None, "'What is it, medicine?' Notice how Russian expresses 'what' and 'medicines' with crisp inflection rather than helper words. Vika answers right away."),
    (9, None, "'Canned stewed meat.' The grammar packs 'canned stewed meat' and 'canned stewed meat' into a tight, idiomatic kitchen exchange."),
    (10, None, "'What?' The meaning hinges on 'what' working together with 'what' in spoken Russian."),
    (11, None, "'Bring me canned stewed meat, please.' In Russian, the idea of 'to bring' flows naturally into 'please' without extra filler words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for the philosophical opening about thoughts becoming reality and Vika's unexpected midnight craving for canned stewed meat. Until next time!"
CLOSING = ("vika", "До встречи!")
