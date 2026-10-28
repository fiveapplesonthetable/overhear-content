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
    (0, None, '\'Wait, did he pay the money after all?\' Pointing to the money beside Mikhail, Barinov puts the question word "chto" right at the start so Mikhail hears the focus immediately.'),
    (1, None, '\'Yes, he paid, of course.\' Mikhail briskly sends this confirmation without hesitation using "konechno" ("of course") — spoken with a soft "shn" sound in everyday Moscow Russian to mean "of course, certainly".'),
    (2, None, '\'After all, this guest of ours is a foreigner.\' Bringing up a foreigner before Barinov, Mikhail brings in "inostranets" ("foreigner") to make the meaning unmistakable.'),
    (3, None, "'He passed this along to you.' Mikhail follows up promptly during the talk, testing Barinov's reaction in the middle of the exchange."),
    (4, None, "'This is a Michelin inspector from Paris!' Mikhail continues right away on the spot, bringing things back to earth after the buildup."),
    (5, None, '\'He is their very chief inspector.\' Discussing the inspector in the exchange, Barinov reaches for the Russian word "inspektor" ("inspector") right at the heart of the line.'),
    (6, None, '\'He has already ruined many chefs.\' Bringing up the cooks around Mikhail, Barinov puts the weight on "povarov" ("cooks", from "povar") as the exchange unfolds.'),
    (7, None, "'Why is this happening to me?' Barinov asks sharply if there is more going on behind the scenes."),
    (8, None, '\'Just do not get nervous right now.\' Mikhail counters decisively before Barinov and brings in "nervnichayte" ("to be nervous", from "nervnichat") as the key Russian word here.'),
    (9, None, '\'Good afternoon, who is the chef here?\' The inspector calmly gives this daytime greeting at the start of the beat using "dobryy den" ("good afternoon") — literally "good day", the standard Russian greeting from late morning through afternoon.'),
    (10, None, "'Here he is sitting before you.' Mikhail continues briskly on the spot, making his position completely clear."),
    (11, None, '\'Thank you for your answer.\' The inspector simply drops this word of thanks in the exchange using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
]
