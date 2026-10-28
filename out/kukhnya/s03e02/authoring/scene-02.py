# Authoring module for kukhnya-s03e02-scene-02.
ID = 'kukhnya-s03e02-scene-02'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 2
SCENE = 2
TITLE = 'Спор на чаевые  (A Bet on the Tips)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.02'
SOURCE_FILE = 'sources/kukhnya/s03/e02.ru.srt'
INTRO = "At the bar, the waiters divide up the evening's shared tip pool, and arrogant waiter Ilya complains that Max is getting an equal share after putting in less money."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That brings the bar scene to a close. Watch how quickly Ilya's two-person challenge turns into a bet involving the entire waitstaff. See you next time!"
CLOSING = ('max', 'Увидимся!')
STORY = [
    ('ilya', 'Чаевые разбираем?', 'Are we dividing up the tips?', [(16, 'Чаевые разбираем')], ''),
    ('vika', 'Сегодня по семь тысяч. Не густо.', 'Seven thousand each today. Not much.', [(17, 'Не густо')], 'adapted'),
    ('ilya', 'Мне дали пятнашку, а я должен забрать семь?', 'They gave me fifteen, and I have to take seven?', [(18, 'мне на чай дали пятнашку, а я должен забрать семь')], 'adapted'),
    ('ilya', 'Почему я должен работать на ушастых?', 'Why do I have to work for big-eared rookies?', [(19, 'почему я должен работать на всяких ушастых')], 'adapted'),
    ('max', 'Чего? Я не работаю?', 'What? Do I not work?', [(20, 'Чего? Я не работаю')], ''),
    ('max', 'Я тоже в общую кассу положил.', 'I also put money into the common pool.', [(21, 'Я тоже в общую кассу')], 'adapted'),
    ('ilya', 'Нормально устроился?', "You have arranged things nicely for yourself, haven't you?", [(24, 'Нормально устроился')], ''),
    ('vika', 'Все работают, не ты один.', 'Everyone works, not just you alone.', [(25, 'Все работают, не ты один')], ''),
    ('vika', 'Всё. До свидания.', 'That is all. Goodbye.', [(26, 'Все'), (27, 'До свидания')], 'adapted'),
    ('ilya', 'Рыжий, погоди.', 'Redhead, wait.', [(28, 'Рыжий, погоди')], ''),
    ('ilya', 'Спорим на все чаевые за смену?', 'Shall we bet all the tips for the shift?', [(29, 'Спорим на все чаевые'), (29, 'за смену')], 'adapted'),
    ('max', 'Легко! Победитель потом заберёт всю сумму.', 'Easy! The winner will take the whole sum afterward.', [(30, 'Легко'), (30, 'победитель потом заберет всю сумму')], 'adapted'),
]
WALK = [
    (0, None, "'Are we dividing up the tips?' Ilya phrases the comment in earnest: Russian keeps the exact word order of a normal statement here, turning it into a question for Max purely through rising pitch at the end."),
    (1, None, "'Seven thousand each today. Not much.' Vika reacts warmly with a shrug, letting the remark speak for itself."),
    (2, None, '\'They gave me fifteen, and I have to take seven?\' Ilya centers one telling element on cue: "pyatnashku" means "fifteen thousand" (from "pyatnashka"), giving the line its exact edge.'),
    (3, None, '\'Why do I have to work for big-eared rookies?\' Ilya gives this line right away: putting the question word "pochemu" right at the front of the line lets Vika hear the point of the question on the very first beat.'),
    (4, None, "'What? Do I not work?' Max prompts openly if there is more going on behind the scenes."),
    (5, None, '\'I also put money into the common pool.\' Max stresses one direct element on cue: "obshchuyu" means "common, shared" (from "obshchiy"), giving the line its exact edge.'),
    (6, None, '\'You have arranged things nicely for yourself, haven\'t you?\' Ilya shares this statement in earnest: the "-sya" ending on "ustroilsya" ("to settle, to get a job") turns the action inward or makes it happen between people naturally.'),
    (7, None, "'Everyone works, not just you alone.' Vika responds bluntly with a smile, keeping the focus on what actually matters here."),
    (8, None, '\'That is all. Goodbye.\' Vika favors one concrete choice toward Ilya: "svidaniya" means "meeting" (from "svidaniye"), giving the line its exact edge.'),
    (9, None, "'Redhead, wait.' Ilya drops the reply frankly here: spoken Russian trims this down to just 2 words, dropping the extra helper words that English has to spell out."),
    (10, None, "'Shall we bet all the tips for the shift?' Ilya asks earnestly how Max expects that to work in practice."),
    (11, None, '\'Easy! The winner will take the whole sum afterward.\' Max favors one sharp piece in earnest: "pobeditel" means "winner", and it carries the main weight of what Max is saying.'),
]
