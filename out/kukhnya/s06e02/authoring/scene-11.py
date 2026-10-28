# Authoring module for kukhnya-s06e02-scene-11.
ID = 'kukhnya-s06e02-scene-11'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 11
TITLE = 'Элеонора отменяет новое меню  (Eleonora Cancels the New Menu)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'eleonora': 'Элеонора', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "After Denis and Nikita misidentify each other's girlfriends across the room, Mikhail warns Barinov that insulting the prefect will backfire—just as Eleonora storms in and orders the old menu restored."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Crushed that Eleonora has outlawed his auteur menu after a single day, Barinov threatens to resign on the spot. Until next time!'
CLOSING = ('eleonora', 'До свидания!')
STORY = [
    ('mikhail', 'Вон она, вино наливает.', 'There she is, pouring wine.', [(176, 'Вон она. Вино наливает')], 'exact'),
    ('mikhail', 'А моя с Луи заигрывает.', 'And mine is flirting with Louis.', [(178, 'А моя вон'), (179, 'заигрывает')], 'adapted'),
    ('mikhail', 'Давай выпьем за наших девушек, они у нас самые лучшие.', "Let's drink to our girls, they are the very best.", [(181, 'давай выпьем за наших девушек'), (182, 'Они у нас самые лучшие')], 'adapted'),
    ('mikhail', 'Зря ведь ты префекту нахамил.', 'You should not have been rude to the prefect.', [(183, 'Зря ведь ты префекта нахамил')], 'adapted'),
    ('barinov', 'У нас демократия, один гражданин имеет право нахамить другому.', 'We have democracy, one citizen has the right to be rude to another.', [(185, 'У нас демократия. Один гражданин имеет право нахамить другому')], 'exact'),
    ('barinov', 'Хамить префекту нельзя?', 'Is it forbidden to be rude to a prefect?', [(187, 'Хамить префекту?')], 'adapted'),
    ('eleonora', 'А я не поняла, что за праздник?', 'I do not understand, what is this celebration?', [(190, 'А я не поняла'), (191, 'Что за праздник?')], 'adapted'),
    ('barinov', 'У нас новое меню, Элеонора Андреевна.', 'We have a new menu, Eleonora Andreyevna.', [(193, 'У нас новое меню')], 'adapted'),
    ('eleonora', 'А я в курсе.', 'I am aware of that.', [(194, 'А я в курсе')], 'exact'),
    ('eleonora', 'И про то, что ты префекта выгнал, я тоже в курсе.', 'And I am also aware that you kicked out the prefect.', [(194, 'И про то, что ты префекта выгнал, я тоже в курсе')], 'exact'),
    ('eleonora', 'Витя, это мой ресторан!', 'Vitya, this is my restaurant!', [(195, 'Витя, это мой ресторан')], 'exact'),
    ('eleonora', 'Чтобы завтра же вернул старое меню, понял?', 'Bring back the old menu tomorrow, understood?', [(196, 'Чтобы завтра же вернул старое меню'), (197, 'Понял?')], 'adapted'),
]
WALK = [
    (0, None, "'There she is, pouring wine.' Pointing to the wine on the spot, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (1, None, "'And mine is flirting with Louis.' Mikhail fires back right away across the room, testing Barinov's reaction in the middle of the exchange."),
    (2, None, '\'Let\'s drink to our girls, they are the very best.\' Emphasizing how best things are in front of Barinov, Mikhail puts the weight on "luchshiye" ("best", from "luchshiy") as the exchange unfolds.'),
    (3, None, "'You should not have been rude to the prefect.' Mikhail proceeds earnestly with a shrug, watching Barinov's face to see how the news lands."),
    (4, None, "'We have democracy, one citizen has the right to be rude to another.' Barinov pushes back sharply with Mikhail, bringing things back to earth after the buildup."),
    (5, None, '\'Is it forbidden to be rude to a prefect?\' Touching on a prefect in the exchange, Barinov reaches for the Russian word "prefektu" ("district prefect", built from "prefekt") right at the center of the line.'),
    (6, None, '\'I do not understand, what is this celebration?\' Turning to the holiday at once, Eleonora puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (7, None, "'We have a new menu, Eleonora Andreyevna.' Mentioning a new menu with Eleonora, Barinov cuts straight through the tension with Eleonora."),
    (8, None, '\'I am aware of that.\' Highlighting the course in the exchange, Eleonora lands on "kurse" ("course, regimen", built on "kurs") to keep the statement grounded.'),
    (9, None, "'And I am also aware that you kicked out the prefect.' Eleonora pushes back plainly with a smile, so Barinov knows she is not just making small talk."),
    (10, None, "'Vitya, this is my restaurant!' Eleonora cuts in bluntly during the talk, shifting the mood of the conversation in a single beat."),
    (11, None, '\'Bring back the old menu tomorrow, understood?\' Mentioning the old menu with Barinov, Eleonora leans on "staroye" ("old", a form of "staryy") to give the remark its edge.'),
]
