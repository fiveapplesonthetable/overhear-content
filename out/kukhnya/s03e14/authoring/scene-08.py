# Authoring module for kukhnya-s03e14-scene-08.
ID = 'kukhnya-s03e14-scene-08'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 14
SCENE = 8
TITLE = 'Свинина и разговор во дворе  (Pork and a Talk in the Courtyard)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.14'
SOURCE_FILE = 'sources/kukhnya/s03/e14.ru.srt'
INTRO = 'In the dining room, Max proudly announces that the dish is tender French pork, offending the Muslim guests even worse than before! Meanwhile, Chef Barinov meets Stas in the courtyard with Senya and Fedya hiding nearby. Listen first.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as Chef Barinov insists to Katya that he didn't want to hurt Stas, Senya and Fedya step out holding baseball bats! Let's hear the comedy in Scene Nine. See you next time!"
CLOSING = ('max', 'До завтра!')
STORY = [
    ('guest', 'Скажи, а что это за мясо?', 'Tell me, what kind of meat is this?', [(123, 'что это за мясо')], 'adapted'),
    ('max', 'Это нежнейшее мясо по старинному французскому рецепту, свинина!', 'This is the most tender meat from an old French recipe, pork!', [(124, 'это нежнейшее'), (124, 'по старинному французскому рецепту свинина')], 'adapted'),
    ('max', 'Ой, я перепутал, это блюдо не вам!', 'Oops, I mixed it up, this dish is not for you!', [(125, 'Перепутал. Это не вам')], 'adapted'),
    ('max', 'Сейчас я там дофарширую и сразу приду.', 'I will finish stuffing it in there right now and come right back.', [(126, 'Сейчас я там дофарширую и приду')], 'adapted'),
    ('guest', 'У тебя шесть секунд, мы возле машины.', 'You have six seconds, we are by the car.', [(127, 'У тебя шесть секунд, мы возле машины')], 'adapted'),
    ('barinov', 'Немедленно оставь мою дочь в покое!', 'Leave my daughter alone immediately!', [(131, 'Оставь мою дочь в покое')], 'adapted'),
    ('max', 'Ну что, батя, ты принёс деньги?', 'So, pops, did you bring the money?', [(130, 'принес'), (132, 'деньги')], 'adapted'),
    ('barinov', 'Вот тебе кулак, а не деньги!', 'Here is a fist for you, not money!', [(133, 'Вот тебе, а не деньги')], 'adapted'),
    ('barinov', 'Ещё раз увижу с Катей, ноги в рот запихаю!', 'If I see you with Katya again, I will shove your legs in your mouth!', [(134, 'увижу вместе с Катей, ноги в рот запихаю')], 'adapted'),
    ('max', 'Папа, пусти его, он просто поговорить приехал!', 'Dad, let him go, he just came to talk!', [(137, 'Папа, пусти его'), (138, 'поговорить приехал')], 'adapted'),
    ('barinov', 'Катя, не слушай его, он хотел получить деньги!', 'Katya, do not listen to him, he wanted to get money!', [(139, 'не слушай ты его'), (139, 'получить')], 'adapted'),
    ('barinov', 'Да я трогать его не хотел, он меня спровоцировал!', 'I did not want to touch him, he provoked me!', [(142, 'Да я трогать его не хотел, он меня спровоцировал')], 'adapted'),
]
WALK = [
    (0, None, '\'Tell me, what kind of meat is this?\' Dwelling on the meat beside Max, the guest puts the question word "chto" right at the start so Max hears the focus immediately.'),
    (1, None, "'This is the most tender meat from an old French recipe, pork!' Max continues honestly facing the guest, leaving no doubt about where he stands."),
    (2, None, '\'Oops, I mixed it up, this dish is not for you!\' Emphasizing the dish around the guest, Max centers the thought on "pereputal" ("mixed up, confused", from "pereputat") without wasting a word.'),
    (3, None, '\'I will finish stuffing it in there right now and come right back.\' Max weighs in decisively with the guest and leans on "dofarshiruyu" ("will finish stuffing", a form of "dofarshirovat") to give the remark its edge.'),
    (4, None, "'You have six seconds, we are by the car.' The guest fires back decisively with a nod, steering the talk right where he wants it."),
    (5, None, '\'Leave my daughter alone immediately!\' Addressing his daughter before the guest, Barinov uses "nemedlenno" ("immediately") to carry the main weight of the thought.'),
    (6, None, '\'So, pops, did you bring the money?\' Opening up frankly with Barinov, Max puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (7, None, "'Here is a fist for you, not money!' Barinov speaks earnestly across the room, so Max knows he is not just making small talk."),
    (8, None, '\'If I see you with Katya again, I will shove your legs in your mouth!\' Highlighting the legs during the talk, Barinov uses "zapikhayu" ("will shove", from "zapikhat") to make the point stick.'),
    (9, None, '\'Dad, let him go, he just came to talk!\' Bringing up the dad around Barinov, Max uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (10, None, "'Katya, do not listen to him, he wanted to get money!' Barinov answers calmly without any doubt, letting the remark speak for itself."),
    (11, None, '\'I did not want to touch him, he provoked me!\' Barinov weighs in candidly before Max and lands on "sprovotsiroval" ("provoked", built on "sprovotsirovat") to keep the statement grounded.'),
]
