# Authoring module for kukhnya-s05e12-scene-15.
ID = 'kukhnya-s05e12-scene-15'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 15
TITLE = 'Вентиляция и преждевременные поздравления  (The Ventilation and Premature Congratulations)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'
INTRO = 'In the kitchen, Mikhail complains to Chef Barinov that the room above the kitchen smells strongly of roast meat because of the ventilation shaft. Out in the corridor, the staff congratulate Elena on her upcoming wedding to Viktor—making Elena think Viktor is about to propose!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes the kitchen and corridor scene. Listen for Lyova's heartfelt congratulations that accidentally convince Elena that Viktor is about to ask for her hand. Until next time!"
CLOSING = ('lyova', 'До встречи!')
STORY = [
    ('barinov', 'Но мы же на кухне!', 'But we are in the kitchen!', [(240, 'Но мы же на кухне')], 'adapted'),
    ('lyova', 'А в номере над кухней пахнет точно так же. Что-то с вентиляцией.', 'And in the room above the kitchen it smells the exact same way. Something is wrong with the ventilation.', [(241, 'А в номере над кухней пахнет точно так же'), (242, 'с вентиляцией')], 'adapted'),
    ('barinov', 'Неси инструменты, я посмотрю, что можно сделать.', 'Bring the tools, I will see what can be done.', [(243, 'инструменты'), (244, 'Я посмотрю, что можно сделать')], 'adapted'),
    ('barinov', 'Извините, я разберусь.', 'Excuse me, I will sort it out.', [(245, 'Извините, я разберусь')], 'adapted'),
    ('lyova', 'Елена, я поздравляю! От всей души я желаю счастья.', 'Elena, I congratulate you! With all my heart I wish you happiness.', [(248, 'я поздравляю'), (249, 'От всей души я желаю счастья')], 'adapted'),
    ('lyova', 'Вы этого заслуживаете.', 'You deserve this.', [(250, 'Вы этого заслуживаете')], 'adapted'),
    ('elena', 'Спасибо. А можно поздравлять?', 'Thank you. Can people congratulate me already?', [(250, 'Спасибо'), (251, 'А можно поздравлять')], 'adapted'),
    ('lyova', 'Похоже, что можно! Тогда я тоже поздравляю.', 'It looks like we can! Then I congratulate you too.', [(252, 'Похоже, что можно'), (253, 'Тогда я тоже поздравляю')], 'adapted'),
    ('lyova', 'Я всегда верил, что вы с Виктором Петровичем поженитесь.', 'I always believed that you and Viktor Petrovich would get married.', [(254, 'Я всегда верил, что вы с Виктором Петровичем поженитесь')], 'adapted'),
    ('lyova', 'И очень рад, что он осмелился сделать этот шаг!', 'And I am very glad that he dared to take this step!', [(255, 'И очень рад, что он осмелился сделать этот шаг')], 'adapted'),
    ('elena', 'Подождите, Лёва.', 'Wait, Lyova.', [(256, 'Подождите, Лёва')], 'adapted'),
    ('elena', 'А какой шаг?', 'What step?', [(257, 'А какой шаг')], 'adapted'),
]
WALK = [
    (0, None, "'But we are in the kitchen!' Barinov pushes back candidly without a pause, watching Elena's face to see how the news lands."),
    (1, None, '\'And in the room above the kitchen it smells the exact same way. Something is wrong with the ventilation.\' Lyova emphasizes one pointed touch on cue: "ventilyatsiyey" means "ventilation" (from "ventilyatsiya"), giving the line its exact edge.'),
    (2, None, '\'Bring the tools, I will see what can be done.\' Barinov directs this answer calmly now: the single Russian word "mozhno" ("it is possible, one may") sets up the whole statement without needing a separate word for "it is".'),
    (3, None, "'Excuse me, I will sort it out.' Barinov fires back at once to be clear, leaving no doubt about where he stands."),
    (4, None, '\'Elena, I congratulate you! With all my heart I wish you happiness.\' Lyova emphasizes this clear term in reply: "pozdravlyayu" means "congratulations" (from "pozdravlyat"), giving the line its exact edge.'),
    (5, None, "'You deserve this.' Lyova lays out this line frankly here: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (6, None, "'Thank you. Can people congratulate me already?' Elena wonders deadpan how Barinov expects that to work in practice."),
    (7, None, '\'It looks like we can! Then I congratulate you too.\' Lyova leans on one sharp term on cue: "pozdravlyayu" means "congratulations" (from "pozdravlyat"), giving the line its exact edge.'),
    (8, None, '\'I always believed that you and Viktor Petrovich would get married.\' Lyova aims that thought with ease: the "-sya" ending on "pozhenites" ("will get married") turns the action inward or makes it happen between people naturally.'),
    (9, None, "'And I am very glad that he dared to take this step!' Lyova counters steadily facing Elena, keeping the focus on what actually matters here."),
    (10, None, '\'Wait, Lyova.\' Elena centers this key word in reply: "podozhdite" means "wait" (from "podozhdat"), giving the line its exact edge.'),
    (11, None, '\'What step?\' Elena puts that thought around Lyova: putting the question word "kakoy" right at the front of the line lets Lyova hear the point of the question on the very first beat.'),
]
