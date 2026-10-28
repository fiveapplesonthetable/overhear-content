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
    (0, None, "'They say that thoughts are material.' Claiming that they say that thoughts are material sounds confident, even if Vika has doubts."),
    (1, None, '\'If you think about something constantly, it will definitely happen.\' Once if Vika thinks about something constantly it will definitely happen, Max can finally tell Vika what he means. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, '\'Hello, Vika?\' Turning from the call to the conversation, Max asks Vika directly. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'Hello, Max.' Between the work and the meat, Vika gives Max a quick, grounded response."),
    (4, None, '\'Yes, did something happen?\' Asking whether something happen cuts straight through the tension between Max and Vika. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Well, do not stay silent.' Mentioning that do not stay silent moves the talk in a new direction."),
    (6, None, "'Can you bring me something?' Here checking whether Max brings her something shows Vika looking for the real truth."),
    (7, None, "'Yes, of course!' Around the meat and conversation, Max makes his point loud and clear. Russian puts the key word right up front so his emotion lands on the first beat."),
    (8, None, '\'What is it, medicine?\' Wondering what it medicine is cuts straight through the tension between Max and Vika. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'Canned stewed meat.' Around the point and meat, Vika sets a calm, everyday tone with Max."),
    (10, None, '\'What?\' With the phone and kitchen hanging in the air, Max puts Vika on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (11, None, "'Bring me canned stewed meat, please.' Bringing her canned stewed meat please moves the conversation forward without extra drama."),
]
