# Authoring module for kukhnya-s01e16-scene-04.
ID = 'kukhnya-s01e16-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 4
TITLE = 'Любопытный Макс  (Curious Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Meanwhile in the kitchen, Max has five spare minutes and an idea. Chef Barinov is cooking something special, and Max wants to know what it is and maybe learn from him. Listen to how short the chef's answers get."
OPENER = "Now Max's questions, one by one."
TRANSITION = 'And the whole exchange once more, start to finish.'
OUTRO = "Max walks away with nothing, but his curiosity has only just started. Try to catch the Russian for 'not allowed' on your next listen, since the chef drops it like a door closing. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Шеф.', 'Chef.', [(33, 'Шеф.')], ''),
    ('barinov', 'Что тебе надо?', 'What do you need?', [], ''),
    ('max', 'А что вы готовите?', 'And what are you preparing?', [(34, 'А что вы готовите?')], ''),
    ('barinov', 'А тебе какое дело?', 'And what is it to you?', [(34, 'Тебе какое дело?')], ''),
    ('barinov', 'Тебе нечем заняться?', 'Do you have nothing to do?', [(35, 'Тебе что, заняться нечем?')], ''),
    ('max', 'У меня есть пять минут.', 'I have five minutes.', [(35, 'Ну, у меня пять минут есть,')], ''),
    ('max', 'Я хотел поучиться у вас.', 'I wanted to learn from you.', [(35, 'я хотел поучиться у вас.')], ''),
    ('barinov', 'Иди работай.', 'Go work.', [], ''),
    ('max', 'А можно попробовать?', 'And can I try it?', [(36, 'А можно попробовать?')], ''),
    ('barinov', 'Нет, нельзя.', 'No, you cannot.', [], ''),
    ('max', 'Почему?', 'Why?', [], ''),
    ('barinov', 'Потому что я так сказал.', 'Because I said so.', [], ''),
    ('max', 'Ладно, я понял.', 'Alright, I understand.', [], ''),
    ('barinov', 'Тогда иди отсюда.', 'Then go from here.', [], ''),
]
WALK = [
    (0, None, "'Chef.' 'Shef' is the French 'chef' in Russian letters. In this kitchen it is how the cooks address Barinov instead of using his name."),
    (1, None, "'What do you need?' 'Nado' means 'needed', so 'tebe nado' is literally 'to you is needed'. Barinov says 'ty' to Max, the way a boss talks to a junior cook."),
    (2, None, "'And what are you cooking?' 'Gotovite' is the 'vy' form of 'gotovit', which covers both 'to cook' and 'to prepare'. Max says 'vy' because Barinov is his boss."),
    (3, None, "'And what is it to you?' 'Kakoe delo', 'what business', makes this a blunt brush-off: 'tebe kakoe delo?' is 'what business is it of yours?'"),
    (4, None, "'Do you have nothing to do?' 'Nechem', 'with nothing', is a single word. The whole line is literally 'to you there is nothing to occupy yourself with'."),
    (5, None, "'I have five minutes.' 'U menya est' is 'I have', literally 'at me there is'. After 'pyat', 'five', 'minuta' shortens to 'minut'."),
    (6, None, "'I wanted to learn from you.' You learn 'at' someone in Russian: 'pouchitsya u vas'. 'Khotel', 'wanted', ends in '-l' because Max is a man; a woman would say 'khotela'."),
    (7, None, "'Go work.' 'Idi rabotay' sets two commands side by side with no 'and'. Russians do this all the time: 'idi spi', 'go and sleep'."),
    (8, None, "'And can I try it?' 'Mozhno' plus an action asks permission. 'Poprobovat' means both 'to try' and 'to taste', so with food it asks for a taste."),
    (9, None, "'No, you cannot.' 'Nelzya', 'not allowed', is the opposite of 'mozhno'. It is the word on signs, as in 'kurit nelzya', 'no smoking'."),
    (10, None, "'Why?' 'Pochemu' asks for a reason. Its answer word is built from the same pieces, as the next line shows."),
    (11, None, "'Because I said so.' 'Potomu chto', 'because', mirrors 'pochemu', 'why'. 'Ya tak skazal' is word for word 'I so said'."),
    (12, None, "'Alright, I understand.' 'Ladno' is a reluctant 'okay'. 'Ya ponyal', 'I got it', is in the past in Russian, since the understanding has already happened."),
    (13, None, "'Then get out of here.' 'Otsyuda', 'from here', turns 'idi', 'go', into 'get out'. Its partner is 'syuda', 'to here': 'idi syuda' means 'come here'."),
]
