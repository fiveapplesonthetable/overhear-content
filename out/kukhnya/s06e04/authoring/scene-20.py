# Authoring module for kukhnya-s06e04-scene-20.
ID = 'kukhnya-s06e04-scene-20'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 20
TITLE = 'Гуля — моя девушка!  (Gulya Is My Girlfriend!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'katya': 'Катя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'In the final scene, Lyova explains that he took the five thousand rubles himself earlier that day and tells his stunned mother that Gulya is his girlfriend, not a maid—while Katya introduces Olivier as her boyfriend.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "After taking pepper spray to the eyes playing a Michelin inspector, Olivier can only hope that playing Katya's boyfriend will be less painful. See you next time!"
CLOSING = ('lyova', 'До завтра!')
STORY = [
    ('lyova', 'Так, это что такое происходит?', 'Alright, what is going on here?', [(313, 'Так это что такое?')], 'adapted'),
    ('guest', 'Лёва, из нашей коробки исчезли пять тысяч!', 'Lyova, five thousand disappeared from our box!', [(314, 'Лёва'), (315, 'исчезли пять тысяч')], 'adapted'),
    ('lyova', 'Так это я их взял днем!', 'Why, I was the one who took them this afternoon!', [(316, 'Так это я их взял днем')], 'exact'),
    ('guest', 'Ну видишь, все сразу разъяснилось.', 'Well you see, everything cleared up right away.', [(317, 'Ну, видишь, ну все разъяснилось')], 'adapted'),
    ('katya', 'Я же говорила, прекрасный человек, великолепная домработница!', 'I told you, a wonderful person, a magnificent housekeeper!', [(318, 'прекрасный человек, великолепная домработница')], 'adapted'),
    ('lyova', 'Мама, Гуля — моя девушка!', 'Mom, Gulya is my girlfriend!', [(320, 'Мама, Гуля моя девушка')], 'exact'),
    ('guest', 'Какая красивая пара, она мне с самого начала понравилась.', 'What a lovely couple, I liked her right from the start.', [(321, 'Красивая пара'), (322, 'Она мне с самого начала понравилась')], 'adapted'),
    ('katya', 'До свидания всем.', 'Goodbye, everyone.', [(323, 'До свидания')], 'adapted'),
    ('katya', 'Ребята, забыла вас познакомить, это мой парень Оливье.', 'Guys, I forgot to introduce you, this is my boyfriend Olivier.', [(324, 'Ребята, забыла вас познакомить. Это мой парень')], 'adapted'),
    ('guest', 'Почему они на меня так посмотрели?', 'Why did they look at me like that?', [(325, 'Почему они на меня так посмотрели?')], 'exact'),
    ('guest', 'Что ты им сейчас сказала?', 'What did you just say to them?', [(326, 'Что ты им сказала?')], 'adapted'),
    ('katya', 'Я сказала им, что ты мой парень.', 'I told them that you are my boyfriend.', [(326, 'Я сказала им, что ты мой парень')], 'exact'),
]
WALK = [
    (0, None, '\'Alright, what is going on here?\' Asking whether Alright what is going on here puts the guest right on the defensive. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (1, None, "'Lyova, five thousand disappeared from our box!' Around the situation and truth, the guest makes his point loud and clear. Russian puts the key word right up front so his emotion lands on the first beat."),
    (2, None, "'Why, I was the one who took them this afternoon!' Saying that why he was the one who took them this afternoon is how Lyova takes charge of the moment."),
    (3, None, "'Well you see, everything cleared up right away.' Around the moment and situation, the guest sets a calm, everyday tone with Katya."),
    (4, None, "'I told you, a wonderful person, a magnificent housekeeper!' Because she told the guest a wonderful person a magnificent housekeeper, Katya does not bother softening the blow for the guest. Russian puts the key word right up front so her emotion lands on the first beat."),
    (5, None, "'Mom, Gulya is my girlfriend!' Insisting that Mom Gulya is his girlfriend shows Lyova is not backing down."),
    (6, None, "'What a lovely couple, I liked her right from the start.' The guest mentions that what a lovely couple he liked her right from the start so Katya sees what is at stake."),
    (7, None, "'Goodbye, everyone.' With the moment and plan in play, Katya keeps this short reply brisk and direct."),
    (8, None, "'Guys, I forgot to introduce you, this is my boyfriend Olivier.' Pointing out that she forgot to introduce the guest this is her boyfriend Olivier gives the guest a sobering reality check."),
    (9, None, '\'Why did they look at me like that?\' Here wondering why they look at him like shows the guest looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, '\'What did you just say to them?\' By wondering what Katya just say to them, the guest presses Katya for a straight answer. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, "'I told them that you are my boyfriend.' Noting that she told them that the guest is her boyfriend keeps Katya's side of the story simple and clear."),
]
