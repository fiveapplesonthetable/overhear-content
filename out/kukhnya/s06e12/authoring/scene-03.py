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
    (0, None, "'Here you go, your fresh salad is already completely ready.' Barinov speaks up calmly in their talk, watching the guest's face to see how the news lands."),
    (1, None, '\'Yes, I have a couple of Italian championship games.\' The guest leans on one direct piece on cue: "chempionata" means "of the championship" (from "chempionat"), giving the line its exact edge.'),
    (2, None, '\'Great odds, let me call you back later.\' The guest makes the comeback beside Barinov: starting with "davay" is the classic everyday Russian way to say "come on, let\'s do this" between people on close terms.'),
    (3, None, "'Excuse me, I overheard by chance, are you a real bookmaker?' Barinov questions quietly in front of Sveta without any preamble."),
    (4, None, '\'Thank you, the salad is very tasty, I know secrets.\' The guest centers one classic term on cue: "spasibo" means "thank you", and it carries the main weight of what the guest is saying.'),
    (5, None, '\'Probably just the same as you in your kitchen.\' The guest uses one vivid piece with Sveta: "navernoye" means "probably", and it carries the main weight of what the guest is saying.'),
    (6, None, "'Maybe you could give a hint strictly between us on whom to bet?' Barinov wonders quietly as the guest tries to explain the situation."),
    (7, None, '\'Excuse me, but I do not understand what you mean.\' The guest picks one loaded detail on cue: "izvinite" means "sorry, excuse me" (from "izvinit"), giving the line its exact edge.'),
    (8, None, "'How about some French cognac on my personal tab?' Barinov shares the comeback facing the guest: Russian keeps the exact word order of a normal statement here, turning it into a question for the guest purely through rising pitch at the end."),
    (9, None, "'No, I do not drink, especially with strangers.' The guest weighs in decisively across the room, before Sveta can change the subject."),
    (10, None, '\'Yes, Denis and I sound pretty good together.\' Sveta highlights one concrete expression with Barinov: "neplokho" means "not bad", and it carries the main weight of what Sveta is saying.'),
    (11, None, "'It seems I have finally met my beloved man!' Sveta reacts frankly with the guest, refusing to let the moment slip past."),
]
