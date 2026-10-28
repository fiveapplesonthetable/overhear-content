# Authoring module for kukhnya-s05e03-scene-01.
ID = 'kukhnya-s05e03-scene-01'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 1
TITLE = "Знакомство Дениса с мамой Кати  (Denis Meets Katya's Mother)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'eleonora': 'Элеонора', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = "Episode 3 picks up right in Eleonora Andreevna's office as Katya introduces her boyfriend Denis to her mother—and Denis realizes in shock that the stranger he slept with was Katya's mother. Listen to the tense meeting."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that captures Denis's mortifying realization in Eleonora's office. Until next time!"
CLOSING = ('denis', 'До встречи!')
STORY = [
    ('katya', 'Пожалуйста, ознакомьтесь.', 'Please get acquainted.', [(1, 'Ознакомьтесь')], 'verbatim'),
    ('katya', 'Денис, это моя мама.', 'Denis, this is my mom.', [(2, 'Денис, это моя мама')], 'verbatim'),
    ('katya', 'Мама, это мой парень Денис.', 'Mom, this is my boyfriend Denis.', [(3, 'Мама, это мой парень Денис')], 'verbatim'),
    ('eleonora', 'Мне очень приятно.', 'Very nice to meet you.', [(4, 'Очень приятно')], 'adapted'),
    ('katya', 'Не бойся, мама не кусается.', 'Do not be afraid, Mom does not bite.', [(5, 'Не бойся, мама не кусается')], 'verbatim'),
    ('denis', 'Да, я это уже знаю.', 'Yes, I already know that.', [(6, 'Я знаю')], 'adapted'),
    ('eleonora', 'Денис, а вы чем занимаетесь?', 'Denis, and what do you do for a living?', [(7, 'Денис, а вы чем занимаетесь?')], 'verbatim'),
    ('denis', 'Я здесь у вас работаю.', 'I work right here for you.', [(8, 'Работаю'), (9, 'У вас')], 'adapted'),
    ('denis', 'Я работаю поваром на кухне.', 'I work as a cook in the kitchen.', [(9, 'Поваром')], 'adapted'),
    ('eleonora', 'Очень хорошо, и к Кате поближе.', 'Very good, and closer to Katya.', [(10, 'Очень хорошо'), (10, 'поближе')], 'adapted'),
    ('eleonora', 'Вы теперь под моей крышей.', 'You are under my roof now.', [(11, 'И под моей крышей')], 'adapted'),
    ('eleonora', 'Значит, будете часто видеться.', 'So we will see each other often.', [(11, 'будете часто видеться')], 'adapted'),
    ('denis', 'Извините, мне нужно идти.', 'Excuse me, I need to go.', [(12, 'Извините, мне нужно идти')], 'verbatim'),
]
WALK = [
    (0, None, "'Please get acquainted.' Explaining that Denis should get acquainted lays the cards on the table for Denis."),
    (1, None, '\'Denis, this is my mom.\' With the plan and shock in play, Katya keeps this short reply brisk and direct. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (2, None, '\'Mom, this is my boyfriend Denis.\' Since Mom this is her boyfriend Denis, Katya does not waste words on excuses. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (3, None, "'Very nice to meet you.' With the office and shock in play, Eleonora keeps this short reply brisk and direct."),
    (4, None, "'Do not be afraid, Mom does not bite.' Explaining that do not be afraid Mom does not bite lays the cards on the table for Denis."),
    (5, None, '\'Yes, I already know that.\' Because he already knows, Denis treats the matter as settled. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, "'Denis, and what do you do for a living?' By wondering what Denis does for a living, Eleonora presses Denis for a straight answer."),
    (7, None, '\'I work right here for you.\' Since he works right here for Eleonora, Denis does not waste words on excuses. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (8, None, "'I work as a cook in the kitchen.' Saying that he works as a cook in the kitchen is how Denis sets the tone with Eleonora."),
    (9, None, "'Very good, and closer to Katya.' Over the office and the moment, Eleonora answers Denis without a second thought."),
    (10, None, '\'You are under my roof now.\' Eleonora explains that Denis is under her roof now, keeping her voice calm and direct. Notice how she sticks to the formal "you", keeping a professional line between them.'),
    (11, None, "'So we will see each other often.' Realizing that they will see each other often changes how Eleonora handles the situation."),
    (12, None, "'Excuse me, I need to go.' Explaining that he needs to go lays the cards on the table for Eleonora."),
]
