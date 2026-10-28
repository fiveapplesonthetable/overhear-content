# Authoring module for kukhnya-s04e07-scene-18.
ID = 'kukhnya-s04e07-scene-18'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 7
SCENE = 18
TITLE = 'Звонок Михалкову  (The Call to Mikhalkov)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S4.07'
SOURCE_FILE = 'sources/kukhnya/s04/e07.ru.srt'
INTRO = "At the table in Claude Monet, Gavril Ilyich calls legendary director Nikita Mikhalkov on his mobile phone and hands it to an starstruck Dmitry Nagiyev. Afterward, worried by German's outburst, Gavril Ilyich wonders whether they should hold the banquet next door instead."
OPENER = "Let's break down the phone call with Nikita Mikhalkov line by line."
TRANSITION = "Now let's listen to the phone call scene in the dining room again."
OUTRO = "Gavril Ilyich is almost persuaded to keep the banquet at Claude Monet—until a waiter lifts the silver cover hiding Denis's live street pigeon. See you next time!"
CLOSING = ('nagiyev', 'До встречи!')
STORY = [
    ('guest', 'Алло, Никита Сергеевич, я сейчас в ресторане.', 'Hello, Nikita Sergeyevich, I am at the restaurant right now.', [(275, 'Алло, Никита Сергеевич, я сейчас в Клод Мане.')], 'adapted'),
    ('guest', 'Тут Дмитрий Нагиев хочет с вами пообщаться.', 'Here Dmitry Nagiyev wants to chat with you.', [(276, 'А тут Дима Нагиев хочет с вами пообщаться.')], 'adapted'),
    ('nagiyev', 'Никита Сергеевич, я всю жизнь мечтал позвонить!', 'Nikita Sergeyevich, I dreamed of calling you my whole life!', [(278, 'Никита Сергеевич, я всю жизнь хотел')], 'adapted'),
    ('nagiyev', 'Хотел сказать вам спасибо за ваше искусство!', 'I wanted to say thank you to you for your art!', [(279, 'вам сказать спасибо за то, сколько вы есть.')], 'adapted'),
    ('nagiyev', 'Просто спасибо за то, что вы есть!', 'Simply thank you for existing!', [(280, 'За то, что вы есть.')], 'adapted'),
    ('nagiyev', 'Да, конечно, передаю трубку обратно Гавриилу Ильичу.', 'Yes, of course, I am handing the phone back to Gavriil Ilyich.', [(282, 'Слушай, дай Гаврилу на пару слов.'), (283, 'Слушаюсь.')], 'adapted'),
    ('guest', 'Да, Никита Сергеевич, тут есть небольшие проблемы.', 'Yes, Nikita Sergeyevich, there are some small problems here.', [(285, 'Да есть проблемки.')], 'adapted'),
    ('guest', 'Не знаю, может, в соседнем ресторане организуем?', 'I do not know, maybe we should organize it at the neighboring restaurant?', [(286, 'Не знаю, может быть, в соседнем ресторане организуем.')], 'adapted'),
    ('nagiyev', 'Не надо в соседнем ресторане, я вас умоляю!', 'Not in the neighboring restaurant, I beg you!', [(287, 'Не надо в соседнем ресторане, я вас умоляю, пожалуйста.')], 'adapted'),
    ('guest', 'А если ваш странный повар снова выскочит?', 'And what if your strange cook jumps out again?', [(288, 'Ну, а если ваш подчиненный у нас на банкете выскочит?')], 'adapted'),
    ('nagiyev', 'Он больше не выскочит, мы его уволим!', 'He will not jump out anymore, we will fire him!', [(289, 'Не выскочит, что он?')], 'adapted'),
    ('nagiyev', 'Я вас умоляю, дайте нам один шанс!', 'I beg you, please give us one chance!', [(290, 'Я вас умоляю, дайте, пожалуйста, один шанс.')], 'adapted'),
]
WALK = [
    (0, None, "'Hello, Nikita Sergeyevich, I am at the restaurant right now.' The guest opens up calmly watching Nagiyev, letting the remark speak for itself."),
    (1, None, '\'Here Dmitry Nagiyev wants to chat with you.\' The guest responds openly in front of Nagiyev and centers the remark on "poobshchatsya" ("to chat") without any extra fuss.'),
    (2, None, '\'Nikita Sergeyevich, I dreamed of calling you my whole life!\' Addressing the life beside the guest, Nagiyev chooses "zhizn" ("life") so the guest gets the point right away.'),
    (3, None, "'I wanted to say thank you to you for your art!' Nagiyev fires back calmly beside the guest, so the guest knows he is not just making small talk."),
    (4, None, '\'Simply thank you for existing!\' Touching on the thank around the guest, Nagiyev reaches for the Russian word "spasibo" ("thank you") right at the heart of the line.'),
    (5, None, '\'Yes, of course, I am handing the phone back to Gavriil Ilyich.\' Highlighting the receiver right here, Nagiyev chooses "gavriilu" ("ilyich", from the root "gavriila") so the guest hears the exact meaning.'),
    (6, None, "'Yes, Nikita Sergeyevich, there are some small problems here.' The guest proceeds warmly on the spot, so Nagiyev knows he is not just making small talk."),
    (7, None, '\'I do not know, maybe we should organize it at the neighboring restaurant?\' Bringing up the neighboring restaurant in the exchange, the guest reaches for the Russian word "restorane" ("restaurant", built from "restoran") right at the center of the line.'),
    (8, None, '\'Not in the neighboring restaurant, I beg you!\' Dwelling on the neighboring restaurant in front of the guest, Nagiyev leans on "nado" ("it is necessary, one needs to"), which carries the whole predicate in Russian without needing "it is".'),
    (9, None, "'And what if your strange cook jumps out again?' The guest presses sharply whether Nagiyev really thought this through."),
    (10, None, '\'He will not jump out anymore, we will fire him!\' Nagiyev answers candidly with the guest and reaches for the Russian word "vyskochit" ("to again") right at the heart of the line.'),
    (11, None, "'I beg you, please give us one chance!' Nagiyev responds decisively with the guest, shifting the mood of the conversation in a single beat."),
]
