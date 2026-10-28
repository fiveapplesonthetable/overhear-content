# Authoring module for kukhnya-s06e12-scene-03.
ID = 'kukhnya-s06e12-scene-03'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 3
TITLE = 'Таинственный букмекер  (The Mysterious Bookmaker)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = 'In the dining hall, Barinov overhears a guest on the phone discussing fourteen-to-one odds on fixed Italian championship matches. Barinov tries to ply the bookmaker with free cognac for a betting tip, while Sveta tells her coworkers that Denis is the man of her dreams.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as Sveta finishes bragging about Denis, her trap goes into motion when the jewelry store calls Denis's phone. Until next time!"
CLOSING = ('guest', 'Благодарю вас и всего доброго!')
STORY = [
    ('barinov', 'Пожалуйста, ваш свежий салат уже полностью готов.', 'Here you go, your fresh salad is already completely ready.', [(36, 'Ваш салат готов')], 'adapted'),
    ('guest', 'Да, у меня есть пара игр чемпионата Италии.', 'Yes, I have a couple of Italian championship games.', [(39, 'Да, кое-что есть'), (40, 'Пару игр чемпионата Италии')], 'adapted'),
    ('guest', 'Отличный коэффициент, давай я тебе позже перезвоню.', 'Great odds, let me call you back later.', [(41, 'Коэффициент'), (43, 'перезвоню')], 'adapted'),
    ('barinov', 'Извините, я случайно услышал, вы настоящий букмекер?', 'Excuse me, I overheard by chance, are you a real bookmaker?', [(44, 'Вы букмекер'), (45, 'Я тут услышал')], 'adapted'),
    ('guest', 'Спасибо, салат очень вкусный, я знаю секреты.', 'Thank you, the salad is very tasty, I know secrets.', [(46, 'Спасибо'), (47, 'Очень вкусно. Я знаю кое-какие секреты')], 'adapted'),
    ('guest', 'Наверное, точно так же, как вы на кухне.', 'Probably just the same as you in your kitchen.', [(48, 'Наверное, как и вы на своей кухне')], 'adapted'),
    ('barinov', 'Может, подскажете строго между нами, на кого ставить?', 'Maybe you could give a hint strictly between us on whom to bet?', [(49, 'Может, подскажете, на кого ставить'), (50, 'Строго между нами')], 'adapted'),
    ('guest', 'Извините, но я не понимаю, о чём вы.', 'Excuse me, but I do not understand what you mean.', [(51, 'Я не понимаю')], 'adapted'),
    ('barinov', 'А может, французского коньяка за мой личный счёт?', 'How about some French cognac on my personal tab?', [(52, 'за мой счет')], 'adapted'),
    ('guest', 'Нет, я не пью, особенно с незнакомыми людьми.', 'No, I do not drink, especially with strangers.', [(53, 'Нет, я не пью'), (54, 'Особенно с незнакомыми людьми')], 'adapted'),
    ('sveta', 'Да, мы с Денисом неплохо звучим вместе.', 'Yes, Denis and I sound pretty good together.', [(56, 'Да, неплохо звучим вместе')], 'adapted'),
    ('sveta', 'Похоже, я наконец-то встретила своего любимого мужчину!', 'It seems I have finally met my beloved man!', [(58, 'Похоже, я встретила наконец-то своего мужчину')], 'adapted'),
]
WALK = [
    (0, None, '\'Here you go, your fresh salad is already completely ready.\' Mentioning that here the guest goes the guest\'s fresh salad is already completely ready moves the talk in a new direction. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (1, None, "'Yes, I have a couple of Italian championship games.' Even though he has a couple of Italian championship games, the guest keeps a steady face in front of Barinov."),
    (2, None, '\'Great odds, let me call you back later.\' Because great odds let him call Barinov back later, the guest treats the matter as settled. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
    (3, None, '\'Excuse me, I overheard by chance, are you a real bookmaker?\' Questioning whether he overheard by chance are the guest a real bookmaker is how Barinov tests the guest\'s story. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (4, None, "'Thank you, the salad is very tasty, I know secrets.' The guest mentions that the salad is very tasty he knows secrets so Barinov sees what is at stake."),
    (5, None, '\'Probably just the same as you in your kitchen.\' Around the moment and phone, the guest sets a calm, everyday tone with Barinov. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, '\'Maybe you could give a hint strictly between us on whom to bet?\' Asking whether maybe the guest could give a hint strictly between them on whom to bet puts the guest right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'Excuse me, but I do not understand what you mean.' The guest explains that he does not understand what Barinov means, keeping his voice calm and direct."),
    (8, None, '\'How about some French cognac on my personal tab?\' With the shift and phone hanging in the air, Barinov puts the guest on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (9, None, "'No, I do not drink, especially with strangers.' Noting that he does not drink especially with strangers keeps the guest's side of the story simple and clear."),
    (10, None, "'Yes, Denis and I sound pretty good together.' Even though Denis and she sounds pretty good together, Sveta keeps a steady face in front of Barinov."),
    (11, None, "'It seems I have finally met my beloved man!' Insisting that it seems she has finally met her beloved man shows Sveta is not backing down. Russian puts the key word right up front so her emotion lands on the first beat."),
]
