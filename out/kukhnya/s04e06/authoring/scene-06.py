# Authoring module for kukhnya-s04e06-scene-06.
ID = 'kukhnya-s04e06-scene-06'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 6
SCENE = 6
TITLE = 'Перенос встречи  (Rescheduling the Visit)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.06'
SOURCE_FILE = 'sources/kukhnya/s04/e06.ru.srt'
INTRO = "Seconds after Elena Pavlovna walks out the door for her afternoon spa appointment, Viktor Barinov's phone rings. It is his friend Volodya calling to say that he cannot make it for lunch after all and will come to Arcobaleno for dinner instead—right when Elena will be back!"
OPENER = "Let's break down Volodya's phone call to Barinov line by line."
TRANSITION = "Now let's listen to the phone call about rescheduling the visit again."
OUTRO = 'With Volodya now coming at dinnertime instead of lunch, Barinov has to figure out how to keep Elena away from Arcobaleno in the evening too. See you next time!'
CLOSING = ('barinov', 'Увидимся!')
STORY = [
    ('barinov', 'Да, Володя, привет, я тебя уже жду!', 'Yes, Volodya, hi, I am already waiting for you!', [(71, 'Да, Володь. Вить, привет.')], 'adapted'),
    ('guest', 'Витя, у нас не получится зайти на обед.', 'Vitya, we will not be able to drop by for lunch.', [(72, 'не получится у нас к тебе зайти на обед.')], 'adapted'),
    ('guest', 'У нас самолёт вечером, а дел ещё много.', 'Our plane is in the evening, and there is still much to do.', [(73, 'самолет вечером, а еще столько дел сделать надо.')], 'adapted'),
    ('barinov', 'Как же вы так меня подводите, друзья?', 'How can you let me down like that, folks?', [(75, 'Что же вы так?')], 'adapted'),
    ('barinov', 'Вы меня сейчас просто очень сильно расстроили.', 'You have just upset me very much right now.', [(76, 'Вы меня очень расстроили.')], 'adapted'),
    ('guest', 'Прости меня, пожалуйста, мой старый друг.', 'Please forgive me, my old pal.', [(77, 'Прости, дружище.')], 'adapted'),
    ('barinov', 'Я так старался вас сегодня вкусно удивить.', 'I tried so hard to surprise you deliciously today.', [(77, 'Я старался вас как-то удивить')], 'adapted'),
    ('guest', 'Хорошо, тогда мы заедем к тебе на ужин!', 'All right, then we will stop by your place for dinner!', [(78, 'тогда мы заедем к тебе прямо перед рейсом на ужин')], 'adapted'),
    ('guest', 'Заедем прямо перед нашим вечерним рейсом.', 'We will drop in right before our evening flight.', [(78, 'прямо перед рейсом')], 'adapted'),
    ('barinov', 'Подожди, вы хотите приехать вечером на ужин?', 'Wait, you want to come in the evening for dinner?', [], 'new'),
    ('guest', 'Да, вечером мы точно будем у тебя!', 'Yes, in the evening we will definitely be at your place!', [], 'new'),
    ('barinov', 'Нет проблем, Володя, буду вас ждать вечером.', 'No problem, Volodya, I will wait for you in the evening.', [(79, 'Нет проблем, жду.')], 'adapted'),
]
WALK = [
    (0, None, "'Yes, Volodya, hi, I am already waiting for you!' Barinov follows up lightly with a nod, keeping the focus on what actually matters here."),
    (1, None, '\'Vitya, we will not be able to drop by for lunch.\' The guest centers one classic expression at once: "poluchitsya" means "will come out", and it carries the main weight of what the guest is saying.'),
    (2, None, '\'Our plane is in the evening, and there is still much to do.\' The guest phrases the reaction plainly here: the phrase "u nas" literally means "by us" or "at our place", the standard Russian way to talk about what a group or couple shares.'),
    (3, None, "'How can you let me down like that, folks?' Barinov challenges frankly as the guest tries to explain the situation."),
    (4, None, '\'You have just upset me very much right now.\' Barinov points to this sharp expression in earnest: "rasstroili" means "to upset, distress" (from "rasstroit"), giving the line its exact edge.'),
    (5, None, '\'Please forgive me, my old pal.\' The guest delivers this statement around Barinov: dropping in "pozhaluysta" ("please") keeps the request polite on the surface even in a brisk exchange.'),
    (6, None, "'I tried so hard to surprise you deliciously today.' Barinov counters lightly across the room, making his position completely clear."),
    (7, None, '\'All right, then we will stop by your place for dinner!\' The guest chooses one memorable element with Barinov: "khorosho" means "good, fine", and it carries the main weight of what the guest is saying.'),
    (8, None, "'We will drop in right before our evening flight.' The guest counters bluntly on the spot, leaving no doubt about where he stands."),
    (9, None, "'Wait, you want to come in the evening for dinner?' Barinov tests skeptically about what the guest just brought up."),
    (10, None, '\'Yes, in the evening we will definitely be at your place!\' The guest anchors one colorful word toward Barinov: "vecherom" means "in the evening", and it carries the main weight of what the guest is saying.'),
    (11, None, '\'No problem, Volodya, I will wait for you in the evening.\' Barinov spotlights one loaded expression at once: "problem" means "problems" (from "problema"), giving the line its exact edge.'),
]
