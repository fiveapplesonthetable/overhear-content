# Authoring module for kukhnya-s06e01-scene-04.
ID = 'kukhnya-s06e01-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 4
TITLE = 'Брачный контракт и ревность  (The Prenup and Jealousy)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'mikhail': 'Михаил', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "At the bar counter, hotel manager Mikhail Dzhekovich and groom Dmitry Nagiyev marvel at the harsh ten-million-ruble infidelity clause in Eleonora's prenuptial contract, right before a maid asks Nagiyev for an autograph."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Eleonora's jealousy is on a hair trigger today, costing another employee her job before the ceremony even starts. See you next time!"
CLOSING = ('eleonora', 'До свидания!')
STORY = [
    ('mikhail', 'Боюсь, что у нас нет времени.', 'I am afraid that we have no time.', [(46, 'Боюсь, что у нас на это нет времени')], 'adapted'),
    ('eleonora', 'Свободного времени у тебя появится очень много.', 'You will suddenly have plenty of free time.', [(48, 'свободного времени у тебя появится очень много')], 'adapted'),
    ('nagiyev', 'Обалдеть, за измену десять миллионов.', 'Unbelievable, ten million for infidelity.', [(51, 'Обалдеть. За измену')], 'adapted'),
    ('mikhail', 'Я читал сам про это дело.', 'I read about this matter myself.', [(53, 'Я читал сам')], 'adapted'),
    ('mikhail', 'Извините, можно у вас автограф взять?', 'Excuse me, may I get your autograph?', [(55, 'можно у вас автограф взять')], 'adapted'),
    ('mikhail', 'Это для племянницы.', 'It is for my niece.', [(56, 'Для племянницы')], 'adapted'),
    ('nagiyev', 'Как зовут?', 'What is her name?', [(58, 'Как зовут?')], 'exact'),
    ('nagiyev', 'Я желаю тебе красивые волосы.', 'I wish you beautiful hair.', [(59, 'красивые')], 'adapted'),
    ('mikhail', 'Спасибо.', 'Thank you.', [(61, 'Спасибо')], 'exact'),
    ('nagiyev', 'Слушай, а у тебя есть парень?', 'Listen, do you have a boyfriend?', [(62, 'Слушай, а у тебя парень')], 'adapted'),
    ('eleonora', 'Ты уволена.', 'You are fired.', [(63, 'Ты уволена')], 'exact'),
    ('eleonora', 'Работать надо, а не моему мужу улыбаться.', 'You need to work, not smile at my husband.', [(64, 'работать надо')], 'adapted'),
]
WALK = [
    (0, None, '\'I am afraid that we have no time.\' Pointing to the time with Eleonora, Mikhail centers the thought on "vremeni" ("time", from "vremya") without wasting a word.'),
    (1, None, '\'You will suddenly have plenty of free time.\' Pointing to the time in front of Mikhail, Eleonora uses "u tebya" (literally "by you") where English says "you have" or "your".'),
    (2, None, "'Unbelievable, ten million for infidelity.' Nagiyev jumps in decisively hearing Eleonora, testing Eleonora's reaction in the middle of the exchange."),
    (3, None, '\'I read about this matter myself.\' Underscoring the matter in the exchange, Mikhail chooses "delo" ("matter") so Nagiyev gets the point right away.'),
    (4, None, '\'Excuse me, may I get your autograph?\' Opening up directly at once, Mikhail leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (5, None, "'It is for my niece.' Mikhail steps in dryly in this moment, shifting the mood of the conversation in a single beat."),
    (6, None, '\'What is her name?\' Nagiyev replies evenly before Mikhail and chooses "zovut" ("call", from the root "zvat") so Mikhail hears the exact meaning.'),
    (7, None, "'I wish you beautiful hair.' Nagiyev jumps in frankly on the spot, watching Mikhail's face to see how the news lands."),
    (8, None, '\'Thank you.\' Looking at Nagiyev casually as they meet, Mikhail says "spasibo" ("thank you"), the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (9, None, '\'Listen, do you have a boyfriend?\' Underscoring a boyfriend around Eleonora, Nagiyev chooses "paren" ("boyfriend") so Eleonora gets the point right away.'),
    (10, None, "'You are fired.' Jumping in openly to Nagiyev, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (11, None, "'You need to work, not smile at my husband.' Raising her husband with a smile, Eleonora makes it clear to Nagiyev that she means every word."),
]
