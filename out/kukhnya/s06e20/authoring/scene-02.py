# Authoring module for kukhnya-s06e20-scene-02.
ID = 'kukhnya-s06e20-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 20
SCENE = 2
TITLE = 'Инспектор из Парижа  (The Inspector from Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'inspector': 'Инспектор', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.20'
SOURCE_FILE = 'sources/kukhnya/s06/e20.ru.srt'
INTRO = 'After forcing the guest to pay, Barinov and Mikhail Jekovich read his card: he is Patrick Malouda, the feared chief Michelin inspector from Paris! When Malouda enters the kitchen asking who the head chef is, Mikhail points to a man in a wheelchair.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Thinking fast, Mikhail Jekovich points to a wheelchair-bound man to shield Viktor Petrovich from Malouda's wrath. See you next time!"
CLOSING = ('mikhail', 'Всего хорошего!')
STORY = [
    ('barinov', 'Он что, всё-таки заплатил деньги?', 'Wait, did he pay the money after all?', [(14, 'Он что, заплатит')], 'adapted'),
    ('mikhail', 'Да, он заплатил, конечно.', 'Yes, he paid, of course.', [(15, 'он заплатит, конечно')], 'adapted'),
    ('mikhail', 'Ведь этот гость у нас иностранец.', 'After all, this guest of ours is a foreigner.', [(16, 'иностранец')], 'adapted'),
    ('mikhail', 'Он вам вот это передал.', 'He passed this along to you.', [(17, 'Он вам это вот передал')], 'adapted'),
    ('mikhail', 'Это инспектор Мишлен из Парижа!', 'This is a Michelin inspector from Paris!', [(20, 'Инспектор Мишлен из Парижа')], 'adapted'),
    ('barinov', 'Он их самый главный инспектор.', 'He is their very chief inspector.', [(22, 'главный инспектор')], 'adapted'),
    ('barinov', 'Он уже погубил много поваров.', 'He has already ruined many chefs.', [(24, 'Он погубил')], 'adapted'),
    ('barinov', 'Почему со мной это происходит?', 'Why is this happening to me?', [(25, 'со мной все это происходит')], 'adapted'),
    ('mikhail', 'Вы только сейчас не нервничайте.', 'Just do not get nervous right now.', [(26, 'Вы только не нервничайте')], 'adapted'),
    ('inspector', 'Добрый день, кто здесь повар?', 'Good afternoon, who is the chef here?', [(28, 'Добрый день'), (30, 'Кто')], 'adapted'),
    ('mikhail', 'Вот он сидит перед вами.', 'Here he is sitting before you.', [(31, 'Вот он')], 'adapted'),
    ('inspector', 'Спасибо вам за ваш ответ.', 'Thank you for your answer.', [(32, 'Спасибо')], 'adapted'),
]
WALK = [
    (0, None, '\'Wait, did he pay the money after all?\' By asking whether he pay the money after all, Barinov presses the inspector for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Yes, he paid, of course.' Explaining that he paid of course lays the cards on the table for Barinov."),
    (2, None, "'After all, this guest of ours is a foreigner.' Saying that after all this guest of their is a foreigner is how Mikhail sets the tone with Barinov."),
    (3, None, '\'He passed this along to you.\' With the inspector and guest in play, Mikhail keeps this short reply brisk and direct. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (4, None, '\'This is a Michelin inspector from Paris!\' Because this is a Michelin inspector from Paris, Mikhail does not bother softening the blow for Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, "'He is their very chief inspector.' Since he is their very chief inspector, Barinov does not waste words on excuses."),
    (6, None, "'He has already ruined many chefs.' Saying that he has already ruined many chefs is how Barinov sets the tone with the inspector."),
    (7, None, '\'Why is this happening to me?\' Here wondering why this happening to him is shows Barinov looking for the real truth. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (8, None, "'Just do not get nervous right now.' Even though just do not get nervous right now, Mikhail keeps a steady face in front of Barinov."),
    (9, None, '\'Good afternoon, who is the chef here?\' Wondering who the here is cuts straight through the tension between the inspector and Barinov. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, '\'Here he is sitting before you.\' Saying that here he is sitting before Barinov is how Mikhail sets the tone with Barinov. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (11, None, "'Thank you for your answer.' Around the guest and shift, the inspector sets a calm, everyday tone with Barinov."),
]
