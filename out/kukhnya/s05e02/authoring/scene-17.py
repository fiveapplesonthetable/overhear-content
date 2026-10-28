# Authoring module for kukhnya-s05e02-scene-17.
ID = 'kukhnya-s05e02-scene-17'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 17
TITLE = 'Месть лжеревизору  (Payback for the Fake Inspector)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'Convinced that the guest in room 313 is just a freeloader who exploited them for two days, Chef Barinov and Mikhail barge into his suite to force-feed him coffee and steaks. Listen to the confrontation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that captures Barinov and Mikhail's disastrous revenge in room 313. Notice how Barinov calls the guest 'Khlestakov' and 'revizor' after Gogol's famous play 'The Government Inspector'. Until next time!"
CLOSING = ('guest', 'Увидимся!')
STORY = [
    ('barinov', 'А вот и наш дорогой гость.', 'And here is our dear guest.', [(211, 'мой гость')], 'adapted'),
    ('barinov', 'Мы вам горячий кофе принесли.', 'We brought you hot coffee.', [(212, 'Мы вам кофе принесли')], 'adapted'),
    ('mikhail', 'Пожалуйста, вот ваш лучший кофе.', 'Here you go, here is your finest coffee.', [(215, 'Пожалуйста, ваш кофе')], 'adapted'),
    ('guest', 'Я не понял, что здесь происходит?', 'I do not understand, what is going on here?', [(216, 'я не понял, что здесь происходит?')], 'verbatim'),
    ('guest', 'Вы что творите, вы чего?', 'What are you doing, what is with you?', [(217, 'Да! Вы чего?')], 'adapted'),
    ('guest', 'Вы что, совсем с ума сошли?', 'Have you completely lost your minds?', [(218, 'Вы что, с ума сошли?')], 'verbatim'),
    ('barinov', 'Пей давай свой вкусный кофе!', 'Drink up your delicious coffee!', [(218, 'Поешь')], 'adapted'),
    ('guest', 'Что вы себе здесь позволяете?', 'What are you allowing yourselves here?', [(219, 'Что себе')], 'adapted'),
    ('mikhail', 'Витя, дай ему немного дышать.', 'Vitya, let him breathe a little.', [(219, 'Дай ему дышать')], 'adapted'),
    ('mikhail', 'Подожди, дай ему спокойно дышать.', 'Wait, let him breathe calmly.', [(220, 'Дай ему дышать')], 'adapted'),
    ('barinov', 'А куда пропал весь кофе?', 'And where did all the coffee go?', [(221, 'А там все кофе, а?')], 'adapted'),
    ('barinov', 'Держи этого хитрого ревизора!', 'Hold that clever inspector!', [(222, 'Держи ревизора')], 'adapted'),
]
WALK = [
    (0, None, '\'And here is our dear guest.\' Barinov picks an earnest mood in the room, combining "dorogoy" ("dear") and "gost" ("guest") so the key meaning lands right away.'),
    (1, None, '\'We brought you hot coffee.\' Barinov shows a clear tack right away, pairing "goryachiy" ("hot") with "kofe" ("of coffee") to get the point across in plain spoken Russian.'),
    (2, None, '\'Here you go, here is your finest coffee.\' Mikhail adopts a warm direction toward Barinov, placing "luchshiy" ("best") straight beside "kofe" ("of coffee") with no word for "to be" needed.'),
    (3, None, '\'I do not understand, what is going on here?\' The guest challenges calmly without a pause, weaving "ponyal" ("understood") together with "zdes" ("here") just the way native speakers do.'),
    (4, None, '\'What are you doing, what is with you?\' The guest questions plainly without a pause, putting "tvorite" ("are doing, perpetrating") alongside "vy" ("you") in a tight, everyday turn of phrase.'),
    (5, None, '\'Have you completely lost your minds?\' The guest checks boldly in the scene, anchoring the Russian line on "sovsem" ("at all") and "uma" ("mind") without extra filler.'),
    (6, None, '\'Drink up your delicious coffee!\' Barinov shows an emphatic angle in front of the guest, anchoring the Russian line on "pey" ("drink") and "davay" ("let\'s") without extra filler.'),
    (7, None, '\'What are you allowing yourselves here?\' The guest wonders briskly across the room, anchoring the Russian line on "zdes" ("here") and "pozvolyayete" ("allow, permit") without extra filler.'),
    (8, None, '\'Vitya, let him breathe a little.\' Mikhail chooses a firm manner straight away, leaning on "day" ("give") before closing the thought with "nemnogo" ("a bit").'),
    (9, None, '\'Wait, let him breathe calmly.\' Mikhail takes an unhurried stance in the conversation, weaving "podozhdi" ("wait") together with "day" ("give") just the way native speakers do.'),
    (10, None, '\'And where did all the coffee go?\' Barinov probes calmly at this point, joining "kuda" ("where to") to "propal" ("is missing") so every word pulls its weight.'),
    (11, None, '\'Hold that clever inspector!\' Barinov adopts a steady note beside Mikhail, combining "derzhi" ("here you go") and "khitrogo" ("cunning, sly") so the key meaning lands right away.'),
]
