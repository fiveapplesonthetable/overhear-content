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
    (0, None, "'But we are in the kitchen!' Barinov cuts in candidly in this moment, leaving no doubt about where he stands."),
    (1, None, '\'And in the room above the kitchen it smells the exact same way. Something is wrong with the ventilation.\' Underscoring the ventilation beside Barinov, Lyova lands on "ventilyatsiyey" ("ventilation", built on "ventilyatsiya") to keep the statement grounded.'),
    (2, None, '\'Bring the tools, I will see what can be done.\' Turning to the tools with Lyova, Barinov leans on "mozhno" ("it is possible, one may"), which carries the whole predicate in Russian without needing "it is".'),
    (3, None, '\'Excuse me, I will sort it out.\' Barinov gently voices this polite apology in front of Lyova using "izvinite" ("excuse me") — the respectful form of "excuse me" or "sorry" used when stepping in or apologizing.'),
    (4, None, '\'Elena, I congratulate you! With all my heart I wish you happiness.\' Turning to the soul at once, Lyova uses "pozdravlyayu" ("congratulations", from "pozdravlyat") to make the point stick.'),
    (5, None, "'You deserve this.' Opening up quietly in front of Elena, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (6, None, '\'Thank you. Can people congratulate me already?\' Elena openly uses this word of thanks right on cue using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (7, None, '\'It looks like we can! Then I congratulate you too.\' Lyova answers sharply at once and lands on "pozdravlyayu" ("congratulations", built on "pozdravlyat") to keep the statement grounded.'),
    (8, None, '\'I always believed that you and Viktor Petrovich would get married.\' Weighing in dryly in this beat, the "-sya" ending on "pozhenites" ("will get married") marks an action that unfolds mutually or turns back on the speaker.'),
    (9, None, "'And I am very glad that he dared to take this step!' Lyova proceeds steadily without any doubt, grounding the moment in plain reality."),
    (10, None, '\'Wait, Lyova.\' Elena steps in vividly with Lyova and leans on "podozhdite" ("wait", a form of "podozhdat") to give the remark its edge.'),
    (11, None, '\'What step?\' Checking on the step around Lyova, Elena puts the question word "kakoy" right at the start so Lyova hears the focus immediately.'),
]
