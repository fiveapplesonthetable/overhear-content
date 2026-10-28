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
    (0, None, '\'They say that thoughts are material.\' Stressing how material things are at once, Max puts the weight on "materialny" ("material, tangible", from "materialnyy") as the exchange unfolds.'),
    (1, None, '\'If you think about something constantly, it will definitely happen.\' Max answers firmly on the spot and chooses "obyazatelno" ("surely, without fail") so Vika gets the point right away.'),
    (2, None, "'Hello, Vika?' Max questions openly before Vika can change the subject."),
    (3, None, "'Hello, Max.' Replying calmly at once, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (4, None, '\'Yes, did something happen?\' Reacting calmly in this beat, the "-sya" ending on "sluchilos" ("happened") marks an action that unfolds mutually or turns back on the speaker.'),
    (5, None, "'Well, do not stay silent.' Max opens up honestly in this moment, refusing to let the moment slip past."),
    (6, None, '\'Can you bring me something?\' Vika jumps in firmly on the spot and chooses "privezti" ("to bring") so Max gets the point right away.'),
    (7, None, '\'Yes, of course!\' Max naturally chooses this confirmation right on cue using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (8, None, "'What is it, medicine?' Max inquires calmly where this conversation is heading next."),
    (9, None, '\'Canned stewed meat.\' Pointing to the meat during the talk, Vika leans on "tushyonku" ("canned stewed meat", a form of "tushyonka") to give the remark its edge.'),
    (10, None, '\'What?\' Turning plainly right here, Max puts the question word "chto" right at the start so Vika hears the focus immediately.'),
    (11, None, '\'Bring me canned stewed meat, please.\' Vika plainly sends this courtesy word right on cue using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
]
