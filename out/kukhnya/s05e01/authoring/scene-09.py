# Authoring module for kukhnya-s05e01-scene-09.
ID = 'kukhnya-s05e01-scene-09'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 9
TITLE = "Просьба Вики и заказ фламбе  (Vika's Request and the Flambé Order)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'In the dining room, Nastya shares a funny story from her own pregnancy before Vika asks her to keep the secret, and then Chef Barinov heads up to a guest room with a chicken breast flambé. Listen to the scene.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up Vika's conversation with Nastya and Barinov's trip upstairs. Notice the double negation in 'do not tell anyone about this'. Until next time!"
CLOSING = ('vika', 'До завтра!')
STORY = [
    ('nastya', 'Это совершенно нормально.', 'That is completely normal.', [(133, 'Это нормально')], 'adapted'),
    ('nastya', 'Я была беременна и всё забывала.', 'I was pregnant and kept forgetting everything.', [(134, 'Я когда была беременна, я все время что-нибудь забывала')], 'adapted'),
    ('nastya', 'Однажды я пришла в зоопарк.', 'One day I ended up at the zoo.', [(135, 'пришла в зоопарк')], 'adapted'),
    ('vika', 'Настя, у меня есть просьба.', 'Nastya, I have a favor to ask.', [(136, 'Настя, у меня просьба')], 'adapted'),
    ('vika', 'Не говори об этом никому, ладно?', 'Do not tell anyone about this, okay?', [(137, 'Не говори об этом никому, ладно?')], 'verbatim'),
    ('vika', 'Я пока не хочу афишировать.', 'I do not want to publicize it yet.', [(138, 'Я пока не хочу афишировать')], 'verbatim'),
    ('vika', 'Виктор Петрович, тут новый заказ.', 'Victor Petrovich, there is a new order here.', [(140, 'Петрович, тут заказ')], 'adapted'),
    ('vika', 'Гость заказал услугу в номер.', 'A guest ordered the room service.', [(140, 'шеф-номер')], 'adapted'),
    ('barinov', 'Ладно, сейчас я сам пойду.', 'Fine, I will go up myself right now.', [(141, 'Ладно')], 'adapted'),
    ('barinov', 'Вы вызывали шефа в номер?', 'Did you call the chef to the room?', [(142, 'в номер')], 'adapted'),
    ('barinov', 'Куриную грудку вы заказывали?', 'Did you order the chicken breast?', [(143, 'Куриную грудку'), (143, 'заказывали?')], 'adapted'),
    ('vika', 'Что вы сейчас там делаете?', 'What are you doing in there right now?', [(144, 'Что вы делаете?')], 'adapted'),
]
WALK = [
    (0, None, "'That is completely normal.' Nastya pushes back dryly with a nod, leaving no doubt about where she stands."),
    (1, None, '\'I was pregnant and kept forgetting everything.\' Nastya follows up frankly beside Vika and leans on "beremenna" ("pregnant", a form of "beremennyy") to give the remark its edge.'),
    (2, None, '\'One day I ended up at the zoo.\' Pointing to the zoo before Vika, Nastya lands on "zoopark" ("zoo") as the key everyday word here.'),
    (3, None, "'Nastya, I have a favor to ask.' Vika reacts candidly with a sigh, leaving no doubt about where she stands."),
    (4, None, '\'Do not tell anyone about this, okay?\' Vika fires back naturally before Nastya and centers the thought on "govori" ("say, talk", from "govorit") without wasting a word.'),
    (5, None, '\'I do not want to publicize it yet.\' Vika proceeds firmly during the talk and leans on "afishirovat" ("to publicize") to give the whole sentence its punch.'),
    (6, None, "'Victor Petrovich, there is a new order here.' Vika follows up earnestly with a sigh, leaving no doubt about where she stands."),
    (7, None, '\'A guest ordered the room service.\' Highlighting the room service in front of Barinov, Vika centers the thought on "uslugu" ("service, favor", from "usluga") without wasting a word.'),
    (8, None, '\'Fine, I will go up myself right now.\' Barinov firmly shares this word of agreement without hesitation using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (9, None, "'Did you call the chef to the room?' Barinov presses eagerly how Vika expects that to work in practice."),
    (10, None, '\'Did you order the chicken breast?\' Talking about the chicken breast around Vika, Barinov lands on "kurinuyu" ("chicken", built on "kurinyy") to keep the statement grounded.'),
    (11, None, '\'What are you doing in there right now?\' Cutting in earnestly with Barinov, Vika puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
]
