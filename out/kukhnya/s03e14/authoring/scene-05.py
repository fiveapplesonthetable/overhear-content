# Authoring module for kukhnya-s03e14-scene-05.
ID = 'kukhnya-s03e14-scene-05'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 14
SCENE = 5
TITLE = 'Вызов на разговор и взятка  (Summoned for a Talk and a Bribe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.14'
SOURCE_FILE = 'sources/kukhnya/s03/e14.ru.srt'
INTRO = 'At Table Seven, the driver and his tough friends order Max to step outside with them, so Max stalls by claiming he has a dish to finish stuffing. Meanwhile, Chef Barinov offers Stas one hundred thousand rubles to leave Katya. Listen first.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Stas happily pockets the money—wait until Katya finds out what her father just did! Until next time!'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('guest', 'О, а вот и наш герой пришёл.', 'Oh, and here comes our hero.', [(65, 'О, а вот и наш герой')], 'adapted'),
    ('guest', 'Присядешь с нами на дорожку?', 'Will you sit down with us for the road?', [(66, 'Присядешь на дорожку')], 'adapted'),
    ('max', 'Нам в зале не положено садиться.', 'We are not allowed to sit down in the dining room.', [(66, 'Нам вообще не положено садиться')], 'adapted'),
    ('guest', 'Ну тогда пойдём выйдем, приляжешь.', "Well then let's step outside and you can lie down.", [(67, 'Ну тогда пойдем выйдем, приляжешь')], 'adapted'),
    ('guest', 'Пойдём на улицу, разговор есть.', "Let's go outside, we have something to discuss.", [(68, 'Пойдем, разговор есть')], 'adapted'),
    ('max', 'Хорошо, только у меня там блюдо на кухне.', 'Alright, only I have a dish in the kitchen.', [(69, 'Хорошо, только у меня там блюдо')], 'adapted'),
    ('max', 'Я его сейчас дофарширую и сразу выйду.', 'I will finish stuffing it right now and come right out.', [(69, 'я его сейчас дофарширую, выйду')], 'adapted'),
    ('guest', 'Иди давай, мы тебя ждём на улице.', 'Go on then, we are waiting for you outside.', [(71, 'Иди давай, мы тебя ждем уже')], 'adapted'),
    ('max', 'Здорово, батя, зачем ты звонил?', 'Hey, pops, why did you call?', [(73, 'Здорово, батя')], 'adapted'),
    ('max', 'Вчера как-то неудобно у нас получилось.', 'Things turned out rather awkwardly between us yesterday.', [(75, 'вчера как-то неудобно получилось')], 'adapted'),
    ('barinov', 'Тебе нужны деньги, а мне нужна дочь.', 'You need money, and I need my daughter.', [(77, 'Тебе ж нужны деньги, а мне нужна дочь')], 'adapted'),
    ('max', 'Понял, а сколько здесь денег?', 'Got it, and how much money is here?', [(78, 'А сколько здесь')], 'adapted'),
    ('barinov', 'Здесь ровно сто тысяч рублей.', 'There is exactly one hundred thousand rubles here.', [(79, 'Сто тысяч')], 'adapted'),
    ('max', 'А у тебя ещё дочки есть?', 'Do you have any more daughters?', [(81, 'А у тебя еще дочки есть')], 'adapted'),
]
WALK = [
    (0, None, '\'Oh, and here comes our hero.\' Underscoring his hero before Max, the guest brings in "geroy" ("hero") to make the meaning unmistakable.'),
    (1, None, "'Will you sit down with us for the road?' The guest tests skeptically if there is more going on behind the scenes."),
    (2, None, '\'We are not allowed to sit down in the dining room.\' Emphasizing how allowed things are before the guest, Max centers the thought on "polozheno" ("allowed, supposed to", from "polozhennyy") without wasting a word.'),
    (3, None, '\'Well then let\'s step outside and you can lie down.\' The guest pushes back sharply in the exchange and uses "prilyazhesh" ("will lie down", from "prilech") to make the point stick.'),
    (4, None, "'Let's go outside, we have something to discuss.' The guest counters honestly in this moment, refusing to let the moment slip past."),
    (5, None, '\'Alright, only I have a dish in the kitchen.\' Highlighting a dish during the talk, Max leans on "blyudo" ("dish") to give the whole sentence its punch.'),
    (6, None, '\'I will finish stuffing it right now and come right out.\' Max speaks vividly at once and centers the thought on "dofarshiruyu" ("will finish stuffing", from "dofarshirovat") without wasting a word.'),
    (7, None, "'Go on then, we are waiting for you outside.' The guest opens up honestly without any doubt, bringing things back to earth after the buildup."),
    (8, None, '\'Hey, pops, why did you call?\' Focusing on the dad in the exchange, Max brings in "batya" ("Dad, the old man") to make the meaning unmistakable.'),
    (9, None, '\'Things turned out rather awkwardly between us yesterday.\' Cutting in dryly on the spot, Max reaches for "u nas" ("by us, at our place") to talk about what they share.'),
    (10, None, "'You need money, and I need my daughter.' Barinov opens up sharply with a nod, leaving no doubt about where he stands."),
    (11, None, '\'Got it, and how much money is here?\' Focusing on the money in the exchange, Max uses "deneg" ("money", from "dengi") to make the point stick.'),
    (12, None, '\'There is exactly one hundred thousand rubles here.\' Turning to the thousand with Max, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (13, None, "'Do you have any more daughters?' Max asks deadpan where this conversation is heading next."),
]
