# Authoring module for kukhnya-s03e04-scene-13.
ID = 'kukhnya-s03e04-scene-13'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 4
SCENE = 13
TITLE = 'До последнего гостя  (Until the Last Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.04'
SOURCE_FILE = 'sources/kukhnya/s03/e04.ru.srt'
INTRO = "Late in the evening, Kostya's mushrooms begin to kick in as Nagiyev refuses to go home, ordering Max and Katya to stay after closing and keep bringing him molecular treats."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes Scene Thirteen. Notice how Vika finally tries to open up to Max, only for Nagiyev to march him straight back into the kitchen. Until next time!'
CLOSING = ('nagiyev', 'До свидания!')
STORY = [
    ('max', 'Прошу вас, пожалуйста.', 'Here you are, please.', [(176, 'Прошу вас, пожалуйста')], ''),
    ('max', 'Что-то ещё хотите? Просто кухня закрывается.', "Do you want anything else? It's just that the kitchen is closing.", [(177, 'еще хотите? Просто кухня закрывается')], 'adapted'),
    ('nagiyev', 'Кухня закрывается, а вы с Катей остаётесь до последнего гостя.', 'The kitchen is closing, and you and Katya are staying until the last guest.', [(178, 'Кухня закрывается. А вы с Катей остаетесь')], 'adapted'),
    ('max', 'Как остаёмся? Уже все гости ушли.', 'What do you mean, staying? All the guests have already left.', [(179, 'Как остаемся? Уже все гости ушли')], ''),
    ('nagiyev', 'Я что, не гость? Поэтому иди на кухню.', 'What, am I not a guest? So go to the kitchen.', [(180, 'Я что, не гость'), (181, 'Поэтому иди на кухню')], 'adapted'),
    ('nagiyev', 'Принеси что-нибудь вкусненькое ещё.', 'Bring something else tasty.', [(182, 'Принеси что-нибудь вкусненькое еще')], ''),
    ('nagiyev', 'Шагом марш!', 'Quick march!', [(183, 'Шагом марш')], ''),
    ('vika', 'А насчёт нашего последнего разговора...', 'And regarding our last conversation...', [(184, 'насчет нашего последнего разговора')], ''),
    ('nagiyev', 'Я всё вижу! Я сказал, на кухню!', 'I see everything! I said, to the kitchen!', [(185, 'я все вижу'), (186, 'Я сказал на кухню')], 'adapted'),
    ('nagiyev', 'Быстро марш!', 'Quick, march!', [(187, 'марш')], 'adapted'),
    ('max', 'Вика, давай не сейчас, а?', "Vika, let's not do this right now, okay?", [(187, 'Вика, давай не сейчас, а')], ''),
    ('max', 'Ты же видишь?', "You see how it is, don't you?", [(188, 'Ты же видишь')], ''),
]
WALK = [
    (0, None, "'Here you are, please.' Mentioning that here Nagiyev is please moves the talk in a new direction."),
    (1, None, '\'Do you want anything else? It\'s just that the kitchen is closing.\' Checking whether Nagiyev wants anything else is how Max puts Nagiyev on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (2, None, '\'The kitchen is closing, and you and Katya are staying until the last guest.\' Because the kitchen is closing and Max and Katya are staying until the last guest, Nagiyev treats the matter as settled. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (3, None, "'What do you mean, staying? All the guests have already left.' By asking what Nagiyev means staying, Max presses Nagiyev for a straight answer."),
    (4, None, '\'What, am I not a guest? So go to the kitchen.\' With the point and guest hanging in the air, Nagiyev puts Max on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Bring something else tasty.' Nagiyev mentions that Max should bring something else tasty so Max sees what is at stake."),
    (6, None, "'Quick march!' With the point and conversation at stake, Nagiyev reacts without holding back."),
    (7, None, "'And regarding our last conversation...' Between the shift and the guest, Vika gives Max a quick, grounded response."),
    (8, None, "'I see everything! I said, to the kitchen!' Because he sees everything, Nagiyev does not bother softening the blow for Max. Russian puts the key word right up front so his emotion lands on the first beat."),
    (9, None, "'Quick, march!' With the truth and guest at stake, Nagiyev reacts without holding back."),
    (10, None, '\'Vika, let\'s not do this right now, okay?\' Max asks whether they should not do this right now okay, refusing to let the point slide. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (11, None, '\'You see how it is, don\'t you?\' Questioning whether how it is do not Nagiyev is how Max tests Nagiyev\'s story. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
]
