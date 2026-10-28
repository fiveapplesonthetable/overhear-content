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
    (1, None, '\'I thought it was just a cash register.\' The "-l" on the end of "dumal" tells you Max is a man. And "prosto", "just", is a word that keeps cropping up.'),
    (2, None, '\'Make two espressos, please.\' The command is friendly, and "espresso" doesn\'t change after "two" because it\'s a borrowed word. "Pozhaluysta" does the work of "please".'),
    (3, None, '\'What are you doing here?\' Nastya says "tut", the casual "here", which is shorter than "zdes\'". She\'s using the friendly "you" with Max.'),
    (4, None, '\'And I am now the new bartender.\' A cheeky "and I" begins it, as though Max had been waiting to say so. "Now" and "new" are the next two words, and they look nothing alike.'),
    (5, None, '\'Oh, stop making things up.\' "Da ladno" is literally "yes, fine", but it means "come on!". The word for "make up" has "dumat\'", to think, inside it: you think something out.'),
    (6, None, '\'I saw you in the kitchen.\' The -a on "videla" shows Nastya is a woman. And Russian says "on the kitchen", not "in", for a restaurant kitchen.'),
    (7, None, '\'You are a cook after all.\' Russian skips "are", so this is just "you cook". The tiny word "zhe" in the middle brings in "after all".'),
    (8, None, '\'I have very many talents.\' "At me" is how Russian says "I have". After "many", the word for talent takes a plural ending.'),
    (9, None, '\'And at heart I am a bartender.\' Literally "in the soul". Russians use it like English "deep down".'),
    (10, None, '\'Did Kostya already fix the machine?\' The word for "fixed" ends in -l for a man. "Apparat" is "machine", borrowed from German.'),
    (11, None, '\'Of course, everything works wonderfully.\' It\'s spelled with a "ch" but said "koneshno". And "vsyo" means "everything".'),
    (12, None, '\'Then make coffee faster.\' Russians "cook" coffee, so the command here comes from the verb for boiling or cooking. "Faster" is the one with the "-eye" ending.'),
    (13, None, '\'Right away. Everything will be ready.\' "This second" is a fixed phrase meaning "right away". The word for "ready" ends in -o to agree with "everything".'),
]
