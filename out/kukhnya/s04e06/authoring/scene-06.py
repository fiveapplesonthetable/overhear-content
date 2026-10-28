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
    (0, None, "'Yes, Volodya, hi, I am already waiting for you!' Barinov chimes in plainly toward the guest, watching the guest's face to see how the news lands."),
    (1, None, '\'Vitya, we will not be able to drop by for lunch.\' Highlighting the lunch beside Barinov, the guest centers the remark on "poluchitsya" ("will come out") without any extra fuss.'),
    (2, None, '\'Our plane is in the evening, and there is still much to do.\' Discussing his plane right here, the guest reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (3, None, "'How can you let me down like that, folks?' Barinov challenges frankly why things suddenly took this turn between them."),
    (4, None, '\'You have just upset me very much right now.\' Barinov responds briskly beside the guest and puts the weight on "rasstroili" ("to upset, distress", from "rasstroit") as the exchange unfolds.'),
    (5, None, '\'Please forgive me, my old pal.\' Pointing to the friend in this beat, the guest puts the emphasis on "staryy" ("old") in the middle of the talk.'),
    (6, None, "'I tried so hard to surprise you deliciously today.' Barinov weighs in lightly on the spot, testing the guest's reaction in the middle of the exchange."),
    (7, None, '\'All right, then we will stop by your place for dinner!\' Addressing the dinner to Barinov, the guest reaches for the Russian word "khorosho" ("good, fine") right at the heart of the line.'),
    (8, None, '\'We will drop in right before our evening flight.\' Pointing to the flight in the exchange, the guest lands on "vechernim" ("evening", built on "vecherniy") to keep the statement grounded.'),
    (9, None, "'Wait, you want to come in the evening for dinner?' Barinov tests skeptically before the guest can change the subject."),
    (10, None, '\'Yes, in the evening we will definitely be at your place!\' The guest pushes back frankly around Barinov and uses "vecherom" ("in the evening") to carry the main weight of the thought.'),
    (11, None, "'No problem, Volodya, I will wait for you in the evening.' Barinov continues dryly with a shrug, making his position completely clear."),
]
