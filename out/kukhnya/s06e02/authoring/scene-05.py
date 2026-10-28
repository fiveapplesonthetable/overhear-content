# Authoring module for kukhnya-s06e02-scene-05.
ID = 'kukhnya-s06e02-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 5
TITLE = "Совет Айнуры про поцелуй  (Ainura's Advice About the Kiss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ainura': 'Айнура', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'In the storeroom, Ainura pulls sous-chef Lyova aside to ask how his romance with her niece Gulya is going, and scolds him for taking Gulya to the cinema five times without kissing her.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Embarrassed that Senya overheard his romantic dilemma, Lyova resolves to finally kiss Gulya on their next date. Until next time!'
CLOSING = ('senya', 'До встречи!')
STORY = [
    ('ainura', 'Важное сказать хочу.', 'I want to say something important.', [(64, 'Важное сказать хочу')], 'exact'),
    ('ainura', 'Ты целовал ее?', 'Did you kiss her?', [(68, 'Ты целовал ее?')], 'exact'),
    ('lyova', 'Нет, еще не целовал.', 'No, I have not kissed her yet.', [(68, 'Ты целовал ее?')], 'adapted'),
    ('ainura', 'Не переживай, Лёва.', 'Do not worry, Lyova.', [(69, 'Не переживай')], 'adapted'),
    ('ainura', 'Пять раз в кино водил и не целовал ее?', 'You took her to the movies five times and did not kiss her?', [(70, 'пять раз кино водил и не целовал ее?')], 'adapted'),
    ('ainura', 'Она приехала в Москву кино смотреть?', 'Did she come to Moscow to watch movies?', [(71, 'она приехала в Москву кино смотреть?')], 'adapted'),
    ('lyova', 'Я же не знаю, как у вас принято за девушками ухаживать.', 'I do not know how it is customary in your country to court girls.', [(72, 'принято за девушками ухаживать')], 'adapted'),
    ('lyova', 'У вас сначала у родителей разрешение просить надо.', 'In your country you first have to ask the parents for permission.', [(73, 'у родителей разрешение просить надо')], 'adapted'),
    ('ainura', 'Но это у нас, а тут другая страна.', 'But that is back home, and here is another country.', [(74, 'Но это у нас. А тут другая страна')], 'exact'),
    ('ainura', 'Тут у вас все можно.', 'Here with you anything is allowed.', [(76, 'Тут у вас все можно')], 'exact'),
    ('senya', 'Значит, да, я все слышал.', 'So, yes, I heard everything.', [(80, 'Значит, да, я все слышал')], 'exact'),
    ('senya', 'Прости, что-то я удержаться не смог.', 'Sorry, somehow I could not hold back.', [(85, 'прости, что-то я удержаться не смог')], 'adapted'),
]
WALK = [
    (0, None, "'I want to say something important.' Holding firm quietly in front of Lyova, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (1, None, "'Did you kiss her?' Ainura asks bluntly about what Lyova just brought up."),
    (2, None, '\'No, I have not kissed her yet.\' Lyova proceeds sharply around Ainura and reaches for the Russian word "tseloval" ("kissed", built from "tselovat") right at the center of the line.'),
    (3, None, "'Do not worry, Lyova.' Opening up calmly with Lyova, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (4, None, "'You took her to the movies five times and did not kiss her?' Ainura challenges quietly how Lyova expects that to work in practice."),
    (5, None, '\'Did she come to Moscow to watch movies?\' Discussing the cinema in front of Lyova, Ainura chooses "priyekhala" ("came, arrived", from the root "priyekhat") so Lyova hears the exact meaning.'),
    (6, None, "'I do not know how it is customary in your country to court girls.' Lyova continues warmly across the room, before Ainura can change the subject."),
    (7, None, "'In your country you first have to ask the parents for permission.' Lyova responds right away without holding back, before Ainura can change the subject."),
    (8, None, '\'But that is back home, and here is another country.\' Making clear how different things are with Lyova, Ainura uses "drugaya" ("different, other", from "drugoy") to make the point stick.'),
    (9, None, '\'Here with you anything is allowed.\' Turning candidly in front of Senya, Ainura leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (10, None, "'So, yes, I heard everything.' Senya proceeds dryly during the talk, steering the talk right where he wants it."),
    (11, None, '\'Sorry, somehow I could not hold back.\' Senya speaks up briskly around Ainura and chooses "uderzhatsya" ("to hold back") so Ainura gets the point right away.'),
]
