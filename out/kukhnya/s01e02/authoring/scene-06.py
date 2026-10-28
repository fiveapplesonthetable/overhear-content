# Authoring module for kukhnya-s01e02-scene-06.
ID = 'kukhnya-s01e02-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'Новый бармен  (The New Bartender)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = 'Max has agreed to help out behind the bar, and he is quietly amazed by the cash register. Then Nastya comes in to order two espressos, and is very surprised to see a cook behind the counter. Here is their exchange in Russian first.'
OPENER = 'Now the exchange again, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max is a cook who says he\'s a bartender at heart, and nobody believes him. At least you\'ve learned "I thought" and "right away".'
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('max', 'Так вот как выглядит эта система.', 'So this is what this system looks like.', [], ''),
    ('max', 'Я думал, это просто касса.', 'I thought it was just a cash register.', [(100, 'Я думал, это касса')], ''),
    ('nastya', 'Сделай два эспрессо, пожалуйста.', 'Make two espressos, please.', [(101, 'два эспрессо сделай, пожалуйста')], ''),
    ('nastya', 'Что ты тут делаешь?', 'What are you doing here?', [(102, 'что ты тут делаешь')], ''),
    ('max', 'А я теперь новый бармен.', 'And I am now the new bartender.', [(102, 'А я новый бармен')], ''),
    ('nastya', 'Да ладно тебе выдумывать.', 'Oh, stop making things up.', [(104, 'Да ладно')], ''),
    ('nastya', 'Я тебя на кухне видела.', 'I saw you in the kitchen.', [(104, 'Я тебя на кухне видела')], ''),
    ('nastya', 'Ты же повар.', 'You are a cook after all.', [(105, 'Ты повар')], ''),
    ('max', 'У меня очень много талантов.', 'I have very many talents.', [(105, 'А у меня много талантов')], ''),
    ('max', 'А в душе я бармен.', 'And at heart I am a bartender.', [(105, 'в душе я бармен')], ''),
    ('nastya', 'Костя уже починил аппарат?', 'Did Kostya already fix the machine?', [], ''),
    ('max', 'Конечно, всё прекрасно работает.', 'Of course, everything works wonderfully.', [], ''),
    ('nastya', 'Тогда быстрее вари кофе.', 'Then make coffee faster.', [(107, 'сделай два эспрессо, пожалуйста')], ''),
    ('max', 'Сию секунду. Всё будет готово.', 'Right away. Everything will be ready.', [], ''),
]
WALK = [
    (0, None, '\'So this is what this system looks like.\' "Tak vot" is a pair of little words for "so here is". Inside "vyglyadit", "looks", you\'ll recognise "glyadet\'", to look.'),
    (1, None, '\'I thought it was just a cash register.\' "Ya dumal" is "I thought", and Russian leaves out "it was": "I thought, this just a till". "Kassa" is the cash register, and the till in any shop.'),
    (2, None, '\'Make two espressos, please.\' "Sdelay" is the friendly "make". "Espresso" doesn\'t change after "dva", two, because borrowed words ending in -o never change. "Pozhaluysta" does the work of "please".'),
    (3, None, '\'What are you doing here?\' Nastya says "tut", the casual "here", which is shorter than "zdes\'". She\'s using the friendly "you" with Max.'),
    (4, None, '\'And I am now the new bartender.\' A cheeky "a ya", "and I", begins it. "Teper\'" is "now", in the sense of "from now on", and "novyy" is "new".'),
    (5, None, '\'Oh, stop making things up.\' "Da ladno tebe" is "oh, come on", as Vika said to Max. "Vydumyvat\'", "to make up", has "dumat\'", to think, inside it: you think something out of nothing.'),
    (6, None, '\'I saw you in the kitchen.\' The -a on "videla" shows Nastya is a woman. And Russian always says "na kukhne", "on the kitchen", where English says "in".'),
    (7, None, '\'You are a cook after all.\' "Ty zhe povar" has no "are", just "you cook". The small word "zhe" brings in "after all".'),
    (8, None, '\'I have very many talents.\' "U menya", "at me", is the "I have" pattern. After "mnogo", many, "talant" takes "-ov": "mnogo talantov".'),
    (9, None, '\'And at heart I am a bartender.\' "V dushe" is "in the soul", from "dusha". Russians use it like English "deep down".'),
    (10, None, '\'Did Kostya already fix the machine?\' "Pochinil" is "fixed". "Apparat" is any machine or gadget, and here it means the coffee machine.'),
    (11, None, '\'Of course, everything works wonderfully.\' It\'s spelled with a "ch" but said "koneshno". And "vsyo" means "everything".'),
    (12, None, '\'Then make coffee faster.\' Russians boil coffee, so the command is "vari", boil, from the verb "varit\'". "Bystreye" is "faster".'),
    (13, None, '\'Right away. Everything will be ready.\' "Siyu sekundu" is an old-fashioned "this very second", what a waiter says. "Gotovo" ends in -o to agree with "vsyo", everything.'),
]
