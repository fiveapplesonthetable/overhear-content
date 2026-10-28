# Authoring module for kukhnya-s05e12-scene-01.
ID = 'kukhnya-s05e12-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 1
TITLE = 'Ночной звонок и тушёнка  (A Late-Night Call and Stewed Meat)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'
INTRO = 'Max reflects on the belief that thoughts are material: if you think about something constantly, it is bound to come true. In the middle of the night, his phone rings and pregnant Vika asks him to bring her canned stewed meat.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes our opening scene. Listen for the philosophical opening about thoughts becoming reality and Vika's unexpected midnight craving for canned stewed meat. Until next time!"
CLOSING = ('vika', 'До встречи!')
STORY = [
    ('max', 'Говорят, что мысли материальны.', 'They say that thoughts are material.', [(1, 'Говорят, что мысли')], 'adapted'),
    ('max', 'Если о чём-то постоянно думать, это обязательно произойдёт.', 'If you think about something constantly, it will definitely happen.', [(2, 'Если о чем-то постоянно думать, это обязательно произойдет')], 'adapted'),
    ('max', 'Алло, Вика?', 'Hello, Vika?', [(3, 'Алло'), (4, 'Вика, алло')], 'adapted'),
    ('vika', 'Алло, Макс.', 'Hello, Max.', [(4, 'алло. Макс')], 'adapted'),
    ('max', 'Да, что-то случилось?', 'Yes, did something happen?', [(5, 'Да что-то случилось')], 'adapted'),
    ('max', 'Ну, не молчи.', 'Well, do not stay silent.', [(6, 'Ну, не молчи')], 'adapted'),
    ('vika', 'Можешь мне кое-что привезти?', 'Can you bring me something?', [(6, 'Можешь мне кое-что привезти')], 'adapted'),
    ('max', 'Да, конечно!', 'Yes, of course!', [(7, 'Да, да, конечно')], 'adapted'),
    ('max', 'Что, лекарства?', 'What is it, medicine?', [(7, 'Что, лекарства')], 'adapted'),
    ('vika', 'Тушёнку.', 'Canned stewed meat.', [(8, 'Тушонку')], 'adapted'),
    ('max', 'Что?', 'What?', [(9, 'Что')], 'adapted'),
    ('vika', 'Привези мне тушёнку, пожалуйста.', 'Bring me canned stewed meat, please.', [(6, 'привезти'), (8, 'Тушонку')], 'adapted'),
]
WALK = [
    (0, None, '\'They say that thoughts are material.\' Max frames one memorable element right here: "materialny" means "material, tangible" (from "materialnyy"), giving the line its exact edge.'),
    (1, None, "'If you think about something constantly, it will definitely happen.' Max reacts openly hearing Vika, before Vika can change the subject."),
    (2, None, "'Hello, Vika?' Max questions openly before Vika can change the subject."),
    (3, None, "'Hello, Max.' Vika brings the reply for Max: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (4, None, '\'Yes, did something happen?\' Max offers that remark beside Vika: the "-sya" ending on "sluchilos" ("happened") turns the action inward or makes it happen between people naturally.'),
    (5, None, "'Well, do not stay silent.' Max chimes in honestly beside Vika, keeping the focus on what actually matters here."),
    (6, None, '\'Can you bring me something?\' Vika uses one colorful choice in reply: "privezti" means "to bring", and it carries the main weight of what Vika is saying.'),
    (7, None, "'Yes, of course!' Max hands over the comment before Vika: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (8, None, "'What is it, medicine?' Max inquires calmly about what Vika just brought up."),
    (9, None, '\'Canned stewed meat.\' Vika colors one concrete touch in reply: "tushyonku" means "canned stewed meat" (from "tushyonka"), giving the line its exact edge.'),
    (10, None, '\'What?\' Max directs the comment with warmth: putting the question word "chto" right at the front of the line lets Vika hear the point of the question on the very first beat.'),
    (11, None, "'Bring me canned stewed meat, please.' Vika fires back calmly during the talk, bringing things back to earth after the buildup."),
]
