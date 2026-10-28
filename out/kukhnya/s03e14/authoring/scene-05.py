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
    (0, None, "'Oh, and here comes our hero.' The guest counters firmly to settle things, steering the talk right where he wants it."),
    (1, None, "'Will you sit down with us for the road?' The guest tests skeptically while looking straight at Max here."),
    (2, None, '\'We are not allowed to sit down in the dining room.\' Max stresses one concrete detail right here: "polozheno" means "allowed, supposed to" (from "polozhennyy"), giving the line its exact edge.'),
    (3, None, "'Well then let's step outside and you can lie down.' The guest speaks promptly in this moment, to clear the air between them once and for all."),
    (4, None, "'Let's go outside, we have something to discuss.' The guest steps in honestly with a smile, saying out loud what both of them already know."),
    (5, None, '\'Alright, only I have a dish in the kitchen.\' Max focuses on this vivid piece in reply: "khorosho" means "good, fine", and it carries the main weight of what Max is saying.'),
    (6, None, "'I will finish stuffing it right now and come right out.' Max proceeds sharply hearing Barinov, refusing to let the moment slip past."),
    (7, None, "'Go on then, we are waiting for you outside.' The guest opens up honestly as they talk, without trying to dress up how he really feels."),
    (8, None, '\'Hey, pops, why did you call?\' Max underscores one classic expression in earnest: "zdorovo" means "great, cool", and it carries the main weight of what Max is saying.'),
    (9, None, '\'Things turned out rather awkwardly between us yesterday.\' Max aims the reaction on cue: the phrase "u nas" literally means "by us" or "at our place", the standard Russian way to talk about what a group or couple shares.'),
    (10, None, "'You need money, and I need my daughter.' Barinov cuts in sharply during the talk, keeping the focus on what actually matters here."),
    (11, None, '\'Got it, and how much money is here?\' Max colors this telling term for the guest: "deneg" means "money" (from "dengi"), giving the line its exact edge.'),
    (12, None, '\'There is exactly one hundred thousand rubles here.\' Barinov directs that reply beside the guest: notice how Russian needs no word for "am", "is", or "are" in the present — placing the words side by side says it all.'),
    (13, None, "'Do you have any more daughters?' Max asks deadpan as the guest tries to explain the situation."),
]
