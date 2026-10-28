ID = 'kukhnya-s06e12-scene-03'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 12
SCENE = 3
TITLE = 'Таинственный букмекер  (The Mysterious Bookmaker)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'gost': 'anja', 'sveta': 'angelina'}
LABELS = {'anya': 'Шеф', 'gost': 'Гость', 'sveta': 'Света'}
SOURCE_NAME = "Кухня (Kukhnya) S6.12"
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'

INTRO = 'In the dining hall, Barinov overhears a guest on the phone discussing fourteen-to-one odds on fixed Italian championship matches. Barinov tries to ply the bookmaker with free cognac for a betting tip, while Sveta tells her coworkers that Denis is the man of her dreams.'

STORY = [
    ('anya', 'Пожалуйста, ваш свежий салат уже полностью готов.', 'Here you go, your fresh salad is already completely ready.', [(36, 'Ваш салат готов')], 'adapted'),
    ('gost', 'Да, у меня есть пара игр чемпионата Италии.', 'Yes, I have a couple of Italian championship games.', [(39, 'Да, кое-что есть'), (40, 'Пару игр чемпионата Италии')], 'adapted'),
    ('gost', 'Отличный коэффициент, давай я тебе позже перезвоню.', 'Great odds, let me call you back later.', [(41, 'Коэффициент'), (43, 'перезвоню')], 'adapted'),
    ('anya', 'Извините, я случайно услышал, вы настоящий букмекер?', 'Excuse me, I overheard by chance, are you a real bookmaker?', [(44, 'Вы букмекер'), (45, 'Я тут услышал')], 'adapted'),
    ('gost', 'Спасибо, салат очень вкусный, я знаю секреты.', 'Thank you, the salad is very tasty, I know secrets.', [(46, 'Спасибо'), (47, 'Очень вкусно. Я знаю кое-какие секреты')], 'adapted'),
    ('gost', 'Наверное, точно так же, как вы на кухне.', 'Probably just the same as you in your kitchen.', [(48, 'Наверное, как и вы на своей кухне')], 'adapted'),
    ('anya', 'Может, подскажете строго между нами, на кого ставить?', 'Maybe you could give a hint strictly between us on whom to bet?', [(49, 'Может, подскажете, на кого ставить'), (50, 'Строго между нами')], 'adapted'),
    ('gost', 'Извините, но я не понимаю, о чём вы.', 'Excuse me, but I do not understand what you mean.', [(51, 'Я не понимаю')], 'adapted'),
    ('anya', 'А может, французского коньяка за мой личный счёт?', 'How about some French cognac on my personal tab?', [(52, 'за мой счет')], 'adapted'),
    ('gost', 'Нет, я не пью, особенно с незнакомыми людьми.', 'No, I do not drink, especially with strangers.', [(53, 'Нет, я не пью'), (54, 'Особенно с незнакомыми людьми')], 'adapted'),
    ('sveta', 'Да, мы с Денисом неплохо звучим вместе.', 'Yes, Denis and I sound pretty good together.', [(56, 'Да, неплохо звучим вместе')], 'adapted'),
    ('sveta', 'Похоже, я наконец-то встретила своего любимого мужчину!', 'It seems I have finally met my beloved man!', [(58, 'Похоже, я встретила наконец-то своего мужчину')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Here you go, your fresh salad is already completely ready.' Spoken Russian keeps this brisk, leaning on 'please' and finishing on 'ready'. the guest answers right away."),
    (1, None, "'Yes, I have a couple of Italian championship games.' the guest anchors the line on 'yes', while 'of Italy' completes the thought."),
    (2, None, "'Great odds, let me call you back later.' The grammar packs 'excellent' and 'will call back' into a tight, idiomatic kitchen exchange."),
    (3, None, "'Excuse me, I overheard by chance, are you a real bookmaker?' The '-l' ending on the verb meaning 'heard' places the action in the masculine past tense. the guest answers right away."),
    (4, None, "'Thank you, the salad is very tasty, I know secrets.' Here the Russian phrasing highlights 'thank you' before landing on 'secrets'."),
    (5, None, "'Probably just the same as you in your kitchen.' The meaning hinges on 'probably' working together with 'kitchen' in spoken Russian."),
    (6, None, "'Maybe you could give a hint strictly between us on whom to bet?' Chef Barinov raises the pitch on 'to put' to turn the phrase into a direct spoken question. the guest answers right away."),
    (7, None, "'Excuse me, but I do not understand what you mean.' the guest brings out the contrast between 'excuse me' and 'but' in a few short words."),
    (8, None, "'How about some French cognac on my personal tab?' In Russian, the idea of 'and' flows naturally into 'score' without extra filler words."),
    (9, None, "'No, I do not drink, especially with strangers.' Spoken Russian keeps this brisk, leaning on 'no' and finishing on 'people'. Sveta answers right away."),
    (10, None, "'Yes, Denis and I sound pretty good together.' Spoken Russian keeps this brisk, leaning on 'yes' and finishing on 'together'."),
    (11, None, "'It seems I have finally met my beloved man!' Sveta brings out the contrast between 'similar' and 'I' in a few short words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as Sveta finishes bragging about Denis, her trap goes into motion when the jewelry store calls Denis's phone. See you in the next scene."
CLOSING = ('gost', 'Благодарю вас и всего доброго!')
