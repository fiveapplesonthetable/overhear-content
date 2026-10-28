# Authoring module for kukhnya-s05e01-scene-11.
ID = 'kukhnya-s05e01-scene-11'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 11
TITLE = 'Пять килограммов с Мадагаскара  (Five Kilograms from Madagascar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня', 'timur': 'Тимур'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'At the loading dock, supplier Timur hands Senya a huge crate of five kilograms of Madagascar cockroaches instead of five individual bugs, and mentions spotting Eleonora Andreevna nearby. Listen to the conversation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that wraps up Timur's delivery at the back door. Notice the contrast between five kilograms and five individual pieces in Russian. Until next time!"
CLOSING = ('senya', 'Хорошего дня!')
STORY = [
    ('timur', 'Смотри, свежайший товар привёз.', 'Look, I brought the freshest goods.', [(171, 'Смотри, свежайший')], 'adapted'),
    ('timur', 'Они ещё с утра завтракали.', 'They were still having breakfast this morning.', [(172, 'С утра еще'), (172, 'завтракали')], 'adapted'),
    ('senya', 'Зачем ты так много привёз?', 'Why did you bring so much?', [(173, 'так много привез?')], 'adapted'),
    ('timur', 'Вы сами просили пять килограмм.', 'You yourselves asked for five kilograms.', [(173, 'Сами просили пять килограмм')], 'adapted'),
    ('senya', 'Мы просили только пять штук.', 'We asked for only five individual ones.', [(174, 'Мы просили пять штук')], 'adapted'),
    ('timur', 'Я по одному их не продаю.', 'I do not sell them one by one.', [(175, 'не продаю')], 'adapted'),
    ('timur', 'Не купишь ты — купят другие.', 'If you do not buy them, others will.', [(176, 'Не купишь ты, купят')], 'adapted'),
    ('timur', 'Их купят в китайском ресторане.', 'They will buy them at the Chinese restaurant.', [(176, 'купят в китайском ресторане')], 'verbatim'),
    ('senya', 'Ладно, давай их сюда.', 'Fine, hand them over here.', [(177, 'Ладно, давай, давай')], 'adapted'),
    ('barinov', 'Доброе утро, Тимур.', 'Good morning, Timur.', [(177, 'Доброе утро')], 'adapted'),
    ('timur', 'Я Элеонору Андреевну встретил на улице.', 'I met Eleonora Andreevna on the street.', [(178, 'Андреевну встретил на улице')], 'adapted'),
    ('timur', 'Она нашла нас на новом месте.', 'She found us at the new place.', [(179, 'Нашла нас на новом месте')], 'adapted'),
    ('timur', 'Ты меня всегда отлично кормил, шеф.', 'You always fed me great, Chef.', [(180, 'ты меня так кормил')], 'adapted'),
]
WALK = [
    (0, None, "'Look, I brought the freshest goods.' Mentioning the freshest goods to Senya, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (1, None, "'They were still having breakfast this morning.' Timur pushes back right away with a smile, so Senya knows he is not just making small talk."),
    (2, None, '\'Why did you bring so much?\' Senya counters pointedly with Timur and uses "privyoz" ("brought", from "privezti") to make the point stick.'),
    (3, None, "'You yourselves asked for five kilograms.' Timur pushes back earnestly in their talk, making his position completely clear."),
    (4, None, "'We asked for only five individual ones.' Senya jumps in briskly across the room, leaving no doubt about where he stands."),
    (5, None, '\'I do not sell them one by one.\' Timur responds evenly beside Senya and uses "prodayu" ("I sell", from "prodavat") to make the point stick.'),
    (6, None, "'If you do not buy them, others will.' Timur chimes in honestly with a smile, steering the talk right where he wants it."),
    (7, None, "'They will buy them at the Chinese restaurant.' Timur reacts bluntly hearing Senya, shifting the mood of the conversation in a single beat."),
    (8, None, '\'Fine, hand them over here.\' Senya casually gives this word of agreement without hesitation using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (9, None, '\'Good morning, Timur.\' Barinov quietly gives this morning greeting at this moment using "dobroye utro" ("good morning") — literally "kind morning", with the neuter ending matching "utro" ("morning").'),
    (10, None, "'I met Eleonora Andreevna on the street.' Timur continues evenly without holding back, shifting the mood of the conversation in a single beat."),
    (11, None, '\'She found us at the new place.\' Touching on the new place at once, Timur puts the weight on "novom" ("new", from "novyy") as the exchange unfolds.'),
    (12, None, '\'You always fed me great, Chef.\' Pushing back naturally at once, Timur leans on "otlichno" ("great, excellent"), which carries the whole predicate in Russian without needing "it is".'),
]
