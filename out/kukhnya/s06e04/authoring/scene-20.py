# Authoring module for kukhnya-s06e04-scene-20.
ID = 'kukhnya-s06e04-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 20
TITLE = 'Гуля — моя девушка!  (Gulya Is My Girlfriend!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'gulya': 'Гуля', 'katya': 'Катя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'In the final scene, Lyova explains that he took the five thousand rubles himself earlier that day and tells his stunned mother that Gulya is his girlfriend, not a maid—while Katya introduces Olivier as her boyfriend.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "After taking pepper spray to the eyes playing a Michelin inspector, Olivier can only hope that playing Katya's boyfriend will be less painful. See you next time!"
CLOSING = ('lyova', 'До завтра!')
STORY = [
    ('lyova', 'Так, это что такое происходит?', 'Alright, what is going on here?', [(313, 'Так это что такое?')], 'adapted'),
    ('gulya', 'Лёва, из нашей коробки исчезли пять тысяч!', 'Lyova, five thousand disappeared from our box!', [(314, 'Лёва'), (315, 'исчезли пять тысяч')], 'adapted'),
    ('lyova', 'Так это я их взял днем!', 'Why, I was the one who took them this afternoon!', [(316, 'Так это я их взял днем')], 'exact'),
    ('gulya', 'Ну видишь, все сразу разъяснилось.', 'Well you see, everything cleared up right away.', [(317, 'Ну, видишь, ну все разъяснилось')], 'adapted'),
    ('katya', 'Я же говорила, прекрасный человек, великолепная домработница!', 'I told you, a wonderful person, a magnificent housekeeper!', [(318, 'прекрасный человек, великолепная домработница')], 'adapted'),
    ('lyova', 'Мама, Гуля — моя девушка!', 'Mom, Gulya is my girlfriend!', [(320, 'Мама, Гуля моя девушка')], 'exact'),
    ('gulya', 'Какая красивая пара, она мне с самого начала понравилась.', 'What a lovely couple, I liked her right from the start.', [(321, 'Красивая пара'), (322, 'Она мне с самого начала понравилась')], 'adapted'),
    ('katya', 'До свидания всем.', 'Goodbye, everyone.', [(323, 'До свидания')], 'adapted'),
    ('katya', 'Ребята, забыла вас познакомить, это мой парень Оливье.', 'Guys, I forgot to introduce you, this is my boyfriend Olivier.', [(324, 'Ребята, забыла вас познакомить. Это мой парень')], 'adapted'),
    ('gulya', 'Почему они на меня так посмотрели?', 'Why did they look at me like that?', [(325, 'Почему они на меня так посмотрели?')], 'exact'),
    ('gulya', 'Что ты им сейчас сказала?', 'What did you just say to them?', [(326, 'Что ты им сказала?')], 'adapted'),
    ('katya', 'Я сказала им, что ты мой парень.', 'I told them that you are my boyfriend.', [(326, 'Я сказала им, что ты мой парень')], 'exact'),
]
WALK = [
    (0, None, '\'Alright, what is going on here?\' Looking over firmly to Gulya, Lyova puts the question word "chto" right at the start so Gulya hears the focus immediately.'),
    (1, None, "'Lyova, five thousand disappeared from our box!' Gulya jumps in warmly without a pause, grounding the moment in plain reality."),
    (2, None, "'Why, I was the one who took them this afternoon!' Lyova follows up firmly with a smile, to clear the air between them once and for all."),
    (3, None, '\'Well you see, everything cleared up right away.\' Speaking warmly at once, the "-sya" ending on "razyasnilos" ("cleared up") marks an action that unfolds mutually or turns back on the speaker.'),
    (4, None, "'I told you, a wonderful person, a magnificent housekeeper!' Katya pushes back decisively without a pause, without trying to dress up how she really feels."),
    (5, None, '\'Mom, Gulya is my girlfriend!\' Turning to his girlfriend beside Gulya, Lyova chooses "devushka" ("girlfriend") so Gulya gets the point right away.'),
    (6, None, '\'What a lovely couple, I liked her right from the start.\' Talking about the match in front of Lyova, Gulya uses "krasivaya" ("pretty, beautiful", from "krasivyy") to make the point stick.'),
    (7, None, '\'Goodbye, everyone.\' Katya gently delivers this polite farewell at this moment using "do svidaniya" ("goodbye") — literally "until the next meeting", the standard Russian farewell.'),
    (8, None, '\'Guys, I forgot to introduce you, this is my boyfriend Olivier.\' Talking about the boys during the talk, Katya chooses "rebyata" ("the boys, the lads") so Gulya gets the point right away.'),
    (9, None, '\'Why did they look at me like that?\' Turning directly right here, Gulya puts the question word "pochemu" right at the start so Katya hears the focus immediately.'),
    (10, None, "'What did you just say to them?' Gulya presses wryly about what Katya just brought up."),
    (11, None, '\'I told them that you are my boyfriend.\' Emphasizing her boyfriend before Gulya, Katya chooses "paren" ("boyfriend") so Gulya gets the point right away.'),
]
