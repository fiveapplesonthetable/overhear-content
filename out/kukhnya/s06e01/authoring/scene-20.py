# Authoring module for kukhnya-s06e01-scene-20.
ID = 'kukhnya-s06e01-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 20
TITLE = "Мечта о звезде Мишлен и предложение олигарха  (The Michelin Star Dream and the Oligarch's Offer)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'In the final scene of the episode, Barinov explains that he cannot retire now that Restaurant Victor has entered the Michelin Guide, right before oligarch Alyokhin offers him a quiet position as his personal chef.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Torn between his doctor's warning, the oligarch's peaceful offer, and his lifelong dream of winning a Michelin star, Barinov faces his toughest choice yet. See you next time!"
CLOSING = ('guest', 'Всего доброго.')
STORY = [
    ('barinov', 'Мой ресторан в гид попал!', 'My restaurant made it into the guide!', [(349, 'Мой ресторан в Мишленовский гид попал')], 'adapted'),
    ('barinov', 'Нам могут звезду дать.', 'They might give us a star.', [(350, 'могут звезду дать')], 'adapted'),
    ('guest', 'Виктор Петрович, добрый вечер.', 'Viktor Petrovich, good evening.', [(352, 'Виктор Петрович, добрый вечер')], 'exact'),
    ('guest', 'Мы хотим поблагодарить вас за вчерашний ужин.', "We want to thank you for last night's dinner.", [(353, 'поблагодарить вас за вчерашний ужин')], 'adapted'),
    ('barinov', 'Не стоит, это моя работа.', 'Do not mention it, it is my job.', [(354, 'Не стоит. Это ж моя работа')], 'adapted'),
    ('guest', 'Кстати, по поводу работы.', 'By the way, regarding work.', [(355, 'Кстати, по поводу работы')], 'exact'),
    ('guest', 'Я хочу предложить вам стать моим личным поваром.', 'I want to offer you to become my personal chef.', [(356, 'Я хочу предложить вам стать моим личным поваром')], 'exact'),
    ('guest', 'Я понимаю, вы привыкли к другим масштабам.', 'I understand you are used to other scales.', [(357, 'Я понимаю, вы привыкли к другим масштабам')], 'exact'),
    ('guest', 'У вас будет достойная зарплата, оборудование, персонал.', 'You will have a worthy salary, equipment, and staff.', [(359, 'Достойная зарплата, какое угодно оборудование, персонал')], 'adapted'),
    ('guest', 'И у вас будет всего два постоянных гостя.', 'And you will have only two regular guests.', [(360, 'у вас будет всего два постоянных гостя')], 'adapted'),
    ('guest', 'Я и моя супруга.', 'Me and my wife.', [(361, 'Я и моя супруга')], 'exact'),
    ('barinov', 'Хорошо, я подумаю.', 'Alright, I will think about it.', [(362, 'Я подумаю. Хорошо')], 'adapted'),
]
WALK = [
    (0, None, '\'My restaurant made it into the guide!\' Underscoring his restaurant before the guest, Barinov reaches for the Russian word "restoran" ("restaurant") right at the heart of the line.'),
    (1, None, "'They might give us a star.' Barinov counters wryly in their talk, leaving no doubt about where he stands."),
    (2, None, '\'Viktor Petrovich, good evening.\' The guest casually directs this evening greeting without hesitation using "dobryy vecher" ("good evening") — the standard Russian evening hello, literally "good evening".'),
    (3, None, "'We want to thank you for last night's dinner.' The guest continues firmly beside Barinov, letting the remark speak for itself."),
    (4, None, "'Do not mention it, it is my job.' Barinov pushes back openly with the guest, watching the guest's face to see how the news lands."),
    (5, None, '\'By the way, regarding work.\' Highlighting the matter right here, the guest lands on "povodu" ("matter", built on "povod") to keep the statement grounded.'),
    (6, None, "'I want to offer you to become my personal chef.' The guest steps in openly in this moment, making his position completely clear."),
    (7, None, "'I understand you are used to other scales.' The guest speaks lightly across the room, making his position completely clear."),
    (8, None, '\'You will have a worthy salary, equipment, and staff.\' Touching on the equipment in the exchange, the guest brings in "oborudovaniye" ("equipment") to make the meaning unmistakable.'),
    (9, None, "'And you will have only two regular guests.' The guest fires back candidly without any doubt, leaving no doubt about where he stands."),
    (10, None, "'Me and my wife.' The guest chimes in warmly on the spot, shifting the mood of the conversation in a single beat."),
    (11, None, '\'Alright, I will think about it.\' Barinov speaks pointedly at once and reaches for the Russian word "khorosho" ("good, fine") right at the heart of the line.'),
]
