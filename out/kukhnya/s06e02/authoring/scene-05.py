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
    (0, None, "'I want to say something important.' Ainura delivers the thought to Lyova: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (1, None, "'Did you kiss her?' Ainura asks bluntly whether Senya really thought this through."),
    (2, None, '\'No, I have not kissed her yet.\' Lyova centers one direct piece at once: "tseloval" means "kissed" (from "tselovat"), giving the line its exact edge.'),
    (3, None, "'Do not worry, Lyova.' Ainura aims the reply before Senya: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (4, None, "'You took her to the movies five times and did not kiss her?' Ainura challenges quietly what Lyova is actually getting at here."),
    (5, None, '\'Did she come to Moscow to watch movies?\' Notice how Ainura reacts to Senya plainly here — the Russian word "priyekhala" ("came, arrived", built from "priyekhat") does the heavy lifting.'),
    (6, None, '\'I do not know how it is customary in your country to court girls.\' Lyova phrases that answer without fuss: using "u vas" (literally "by you") is how Russian politely asks or talks about what someone has on their side.'),
    (7, None, "'In your country you first have to ask the parents for permission.' Lyova holds firm right away without a pause, bringing things back to earth after the buildup."),
    (8, None, '\'But that is back home, and here is another country.\' Ainura points to one colorful choice on cue: "drugaya" means "different, other" (from "drugoy"), giving the line its exact edge.'),
    (9, None, '\'Here with you anything is allowed.\' Ainura shapes this statement to Senya: using "u vas" (literally "by you") is how Russian politely asks or talks about what someone has on their side.'),
    (10, None, "'So, yes, I heard everything.' Senya stands firm dryly with a smile, keeping the focus on what actually matters here."),
    (11, None, '\'Sorry, somehow I could not hold back.\' Senya colors one vivid detail right here: "uderzhatsya" means "to hold back", and it carries the main weight of what Senya is saying.'),
]
