# Authoring module for kukhnya-s05e03-scene-20.
ID = 'kukhnya-s05e03-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 20
TITLE = 'Спасение Дениса и новый Аркадий  (Saving Denis and the New Arkady)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = 'In the closing scene of Episode 3, Kostya and Nastya smuggle Denis out of room 205 on a laundry cart just before Eleonora opens the door, and Katya tells her father why Eleonora decided to keep him on. Listen to the finale.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Episode 3 to a close as Denis narrowly escapes Eleonora's trap, though his guilty secret still weighs on him. See you in Episode 4. See you next time!"
CLOSING = ('katya', 'Пока!')
STORY = [
    ('katya', 'Мама, пойдём скорее отсюда.', "Mom, let's get out of here quickly.", [(351, 'Мам, пойдем?')], 'adapted'),
    ('katya', 'Может быть, он сейчас в душе.', 'Maybe he is in the shower right now.', [(352, 'Может быть, он в душе')], 'verbatim'),
    ('denis', 'Отпусти его, они уже ушли!', 'Let him go, they have left already!', [(353, 'его, они ушли!')], 'adapted'),
    ('denis', 'Слабость может превратиться в большую тайну.', 'A weakness can turn into a big secret.', [(355, 'слабость'), (355, 'тайну')], 'adapted'),
    ('denis', 'Тайна может разрушить нам всю жизнь.', 'A secret can destroy our whole life.', [(356, 'разрушить нам жизнь')], 'adapted'),
    ('barinov', 'Поздравляю тебя с новосельем!', 'Congratulations on your housewarming!', [(357, 'С новосельем!')], 'adapted'),
    ('barinov', 'Они у меня долго не живут.', 'They do not live long with me.', [(359, 'Да, они у меня долго не живут')], 'verbatim'),
    ('denis', 'Кто-то хранит тайны ради своих близких.', 'Someone keeps secrets for the sake of loved ones.', [(360, 'Кто-то хранит тайны ради своих близких')], 'verbatim'),
    ('barinov', 'Твоя мама меня почему-то не увольняет.', 'For some reason your mom is not firing me.', [(361, 'меня не увольняет')], 'adapted'),
    ('barinov', 'Она обещала. Не знаешь почему?', 'She promised to. Do you know why?', [(362, 'Обещала. Не знаешь почему?')], 'verbatim'),
    ('katya', 'Да, папа, я это знаю.', 'Yes, Dad, I know why.', [(363, 'Знаю')], 'adapted'),
    ('katya', 'Потому что ты очень крутой шеф.', 'Because you are a really cool chef.', [(364, 'Ты крутой шеф')], 'adapted'),
    ('denis', 'Кто-то готов разлучить близких людей.', 'Someone is ready to separate close people.', [(366, 'Кто-то готов разлучить близких людей')], 'verbatim'),
    ('denis', 'А кто-то не может доверить тайну себе.', 'And someone cannot entrust a secret even to himself.', [(368, 'кто-то не может доверить тайну'), (368, 'себе')], 'adapted'),
]
WALK = [
    (0, None, '\'Mom, let\'s get out of here quickly.\' Katya takes a calm tone without hesitation, combining "mama" ("mum, mother") and "poydyom" ("let\'s go") so the key meaning lands right away.'),
    (1, None, '\'Maybe he is in the shower right now.\' Katya sustains a clear rhythm during the exchange, joining "mozhet" ("can") to "byt" ("be") so every word pulls its weight.'),
    (2, None, '\'Let him go, they have left already!\' Denis conveys a calm rhythm during the exchange, weaving "otpusti" ("let go, release") together with "uzhe" ("already, now") just the way native speakers do.'),
    (3, None, '\'A weakness can turn into a big secret.\' Denis sustains a natural tack during the exchange, leaning on "slabost" ("weakness") before closing the thought with "mozhet" ("can").'),
    (4, None, '\'A secret can destroy our whole life.\' Denis sustains a direct position in front of Barinov, joining "tayna" ("secrecy, privilege") to "mozhet" ("can") so every word pulls its weight.'),
    (5, None, '\'Congratulations on your housewarming!\' Barinov adopts a brisk posture as they talk, pairing "pozdravlyayu" ("congratulations") with "novoselyem" ("housewarming") to get the point across in plain spoken Russian.'),
    (6, None, '\'They do not live long with me.\' Barinov establishes a resolute position on the spot, anchoring the Russian line on "dolgo" ("for a long time") and "zhivut" ("live") without extra filler.'),
    (7, None, '\'Someone keeps secrets for the sake of loved ones.\' Denis adopts an earnest tack in the conversation, putting "khranit" ("keeps") alongside "tayny" ("secrets") in a tight, everyday turn of phrase.'),
    (8, None, '\'For some reason your mom is not firing me.\' Barinov displays a sharp bearing straight away, anchoring the Russian line on "mama" ("mum, mother") and "pochemu-to" ("for some reason") without extra filler.'),
    (9, None, '\'She promised to. Do you know why?\' Barinov checks boldly in this moment, combining "obeshchala" ("promised") and "znayesh" ("know") so the key meaning lands right away.'),
    (10, None, '\'Yes, Dad, I know why.\' Katya sustains a calm view across the room, anchoring the Russian line on "papa" ("Dad") and "znayu" ("know") without extra filler.'),
    (11, None, '\'Because you are a really cool chef.\' Katya brings a pointed angle toward Denis, placing "potomu" ("because") straight beside "ochen" ("very much") with no word for "to be" needed.'),
    (12, None, '\'Someone is ready to separate close people.\' Denis shows a wry manner for Barinov, weaving "gotov" ("ready") together with "razluchit" ("to separate") just the way native speakers do.'),
    (13, None, '\'And someone cannot entrust a secret even to himself.\' Denis adopts an emphatic posture at once, putting "mozhet" ("can") alongside "doverit" ("to entrust") in a tight, everyday turn of phrase.'),
]
