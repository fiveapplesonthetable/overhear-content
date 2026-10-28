# Authoring module for kukhnya-s03e04-scene-11.
ID = 'kukhnya-s03e04-scene-11'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 4
SCENE = 11
TITLE = 'Нет чека — нет блюда  (No Receipt, No Dish)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.04'
SOURCE_FILE = 'sources/kukhnya/s03/e04.ru.srt'
INTRO = "At the clinic, Vika's doctor warns her that she shouldn't wait too many years to have a child, while back in the kitchen the cooks refuse to help Max make Nagiyev's off-menu aspic."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Eleven. Listen for how Fedya and Senya pay Max back for his earlier insults with the rule 'no receipt, no dish.'. Until next time!"
CLOSING = ('nagiyev', 'Всего хорошего!')
STORY = [
    ('max', 'Успокойся! Вон отсюда.', 'Calm down! Get out of here.', [(147, 'Успокойся'), (148, 'Вон отсюда')], 'adapted'),
    ('nagiyev', 'Результаты обследования показали, что уровень тоже низкий.', 'The examination results showed that the level is also low.', [(149, 'Результаты обследования показали, что'), (150, 'Уровень'), (150, 'тоже низкий')], 'adapted'),
    ('vika', 'То есть вы хотите сказать...', 'So you mean to say...', [(151, 'То есть вы хотите сказать')], ''),
    ('nagiyev', 'Родить вам надо в ближайшие два года, а иначе потом будет сложно.', 'You need to have a baby in the next two years, otherwise it will be difficult later.', [(152, 'Родить вам надо в ближайшие два года'), (153, 'А иначе потом будет сложно')], 'adapted'),
    ('max', 'Ребята, там Дмитрий Владимирович попросил холодец.', 'Guys, Dmitry Vladimirovich asked for aspic out there.', [(154, 'там Дмитрий Владимирович попросил холодец')], 'adapted'),
    ('max', 'Кто приготовит?', 'Who will prepare it?', [(155, 'Кто'), (155, 'приготовит')], 'adapted'),
    ('nagiyev', 'Как? Мы же криворукие! Мы же готовить не умеем.', "How? We are clumsy, after all! We don't know how to cook.", [(155, 'Как'), (156, 'Мы же криворукие'), (157, 'Мы же готовить не умеем')], 'adapted'),
    ('nagiyev', 'Тем более что не из меню.', 'Especially since it is not from the menu.', [(158, 'Тем более, что не из меню')], ''),
    ('max', 'Ребята, ну ладно, простите меня, я был не прав.', 'Guys, come on, forgive me, I was wrong.', [(159, 'Ребята, ну ладно, простите меня, я был не прав')], ''),
    ('nagiyev', 'Ну ладно, мы поможем.', 'All right, we will help.', [(160, 'Ну ладно'), (160, 'поможем')], 'adapted'),
    ('nagiyev', 'Чек давай. Что, нет чека?', 'Give me the receipt. What, no receipt?', [(161, 'Чек давай. Что, нету чека')], 'adapted'),
    ('nagiyev', 'Ну извини, нет чека — нет блюда.', 'Well sorry, no receipt, no dish.', [(162, 'Ну извини, нет чека, нет блюда')], ''),
]
WALK = [
    (0, None, '\'Calm down! Get out of here.\' Pressing on warmly in front of Nagiyev, the "-sya" ending on "uspokoysya" ("calm down") marks an action that unfolds mutually or turns back on the speaker.'),
    (1, None, "'The examination results showed that the level is also low.' Nagiyev jumps in candidly across the room, letting the remark speak for itself."),
    (2, None, "'So you mean to say...' Vika continues lightly with a sigh, letting the remark speak for itself."),
    (3, None, '\'You need to have a baby in the next two years, otherwise it will be difficult later.\' Reacting firmly during the talk, Nagiyev leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (4, None, "'Guys, Dmitry Vladimirovich asked for aspic out there.' Addressing the aspic without a pause, Max puts the real issue right on the table for Nagiyev."),
    (5, None, '\'Who will prepare it?\' Max speaks boldly in this beat and centers the remark on "prigotovit" ("makes, cooks") without any extra fuss.'),
    (6, None, '\'How? We are clumsy, after all! We don\'t know how to cook.\' Stressing how clumsy things are at once, Nagiyev puts the question word "kak" right at the start so Max hears the focus immediately.'),
    (7, None, "'Especially since it is not from the menu.' Nagiyev speaks sharply with a sigh, shifting the mood of the conversation in a single beat."),
    (8, None, '\'Guys, come on, forgive me, I was wrong.\' Highlighting the boys around Nagiyev, Max uses "rebyata" ("the boys, the lads") to carry the main weight of the thought.'),
    (9, None, '\'All right, we will help.\' Nagiyev lightly delivers this word of agreement in the exchange using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (10, None, "'Give me the receipt. What, no receipt?' Nagiyev challenges candidly before Max can change the subject."),
    (11, None, '\'Well sorry, no receipt, no dish.\' Pointing to the dish before Max, Nagiyev leans on "blyuda" ("of dish", a form of "blyudo") to give the remark its edge.'),
]
