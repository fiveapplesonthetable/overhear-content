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
    (0, None, "'Here you go, your fresh salad is already completely ready.' Barinov jumps in calmly watching the guest, watching the guest's face to see how the news lands."),
    (1, None, '\'Yes, I have a couple of Italian championship games.\' Addressing the championship with Barinov, the guest centers the thought on "chempionata" ("of the championship", from "chempionat") without wasting a word.'),
    (2, None, '\'Great odds, let me call you back later.\' Focusing on the coefficient around Barinov, the guest starts with "davay" ("come on, let\'s") to invite Barinov right into the action.'),
    (3, None, "'Excuse me, I overheard by chance, are you a real bookmaker?' Barinov questions quietly while looking straight at the guest here."),
    (4, None, '\'Thank you, the salad is very tasty, I know secrets.\' Underscoring the thank beside Barinov, the guest brings in "spasibo" ("thank you") to make the meaning unmistakable.'),
    (5, None, "'Probably just the same as you in your kitchen.' The guest weighs in evenly in this moment, without trying to dress up how he really feels."),
    (6, None, "'Maybe you could give a hint strictly between us on whom to bet?' Barinov wonders quietly why things suddenly took this turn between them."),
    (7, None, '\'Excuse me, but I do not understand what you mean.\' The guest responds frankly in front of Barinov and leans on "izvinite" ("sorry, excuse me", a form of "izvinit") to give the remark its edge.'),
    (8, None, "'How about some French cognac on my personal tab?' Addressing the cognac on the spot, Barinov keeps normal statement word order here, turning the line into a question for the guest purely through rising pitch."),
    (9, None, "'No, I do not drink, especially with strangers.' The guest speaks decisively watching Barinov, steering the talk right where he wants it."),
    (10, None, '\'Yes, Denis and I sound pretty good together.\' Sveta answers frankly right here and reaches for the Russian word "neplokho" ("not bad") right at the heart of the line.'),
    (11, None, '\'It seems I have finally met my beloved man!\' Addressing the man beside the guest, Sveta brings in "lyubimogo" ("beloved", from "lyubimyy") as the key Russian word here.'),
]
