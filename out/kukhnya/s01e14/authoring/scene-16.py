# Authoring module for kukhnya-s01e14-scene-16.
ID = 'kukhnya-s01e14-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 16
TITLE = 'Идиот  (Idiot)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'louis': 'Луи', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "Elena has handed Max an old recipe, and it turns out to be written in French. Louis, the French pastry chef, is watching and can't believe it. Hear the scene in Russian first."
OPENER = 'Again, and watch Max dig himself deeper.'
TRANSITION = 'Here is the scene without interruptions.'
OUTRO = 'Max is stuck, with a French recipe he cannot read. Can you spot the moment he gives himself away? Speak soon.'
CLOSING = ('louis', 'Пока!')
STORY = [
    ('elena', 'Тут все по-французски.', 'Here everything is in French.', [(249, 'Макс')], ''),
    ('elena', 'Для нашего шефа это не проблема.', 'For our chef this is not a problem.', [(249, 'Макс')], ''),
    ('elena', 'Правда, Максимилиан?', 'Right, Maximilian?', [(249, 'Макс')], ''),
    ('max', 'Си.', 'Si.', [(249, 'Макс')], ''),
    ('louis', 'Си? Идиот.', 'Si? Idiot.', [(249, 'Макс')], ''),
    ('louis', 'Си — это по-итальянски.', 'Si is in Italian.', [(249, 'Макс')], ''),
    ('louis', 'По-французски будет уи.', 'In French it will be oui.', [(249, 'Макс')], ''),
    ('max', 'Да, конечно, я знаю это.', 'Yes, of course, I know this.', [(249, 'Макс')], ''),
    ('elena', 'Максимилиан, вы понимаете французский язык?', 'Maximilian, do you understand the French language?', [(249, 'Макс')], ''),
    ('max', 'Конечно, я прекрасно понимаю французский.', 'Of course, I understand French perfectly.', [(249, 'Макс')], ''),
    ('louis', 'Ну, что ты будешь делать теперь?', 'Well, what will you do now?', [(249, 'Макс')], ''),
    ('max', 'Я прочитаю этот рецепт и приготовлю блюдо.', 'I will read this recipe and prepare the dish.', [(249, 'Макс')], ''),
    ('louis', 'Это будет очень смешно.', 'This will be very funny.', [(249, 'Макс')], ''),
]
WALK = [
    (0, None, "'Here everything is in French.' 'Po-frantsuzski': 'po' in front, 'ski' at the end. The same pattern gives po-russki, in Russian."),
    (1, None, "'For our chef this is not a problem.' 'Dlya', for, takes the 'of' form, so nash shef becomes nashego shefa. 'Problema' ends in 'a', and that makes it a feminine word."),
    (2, None, "'Right, Maximilian?' 'Pravda' means 'truth', and on the end of a question it works like 'isn't it?'. She puts him on the spot."),
    (3, None, "'Si.' It's an Italian 'yes', written in Russian letters. Max has chosen the wrong foreign language, which is the whole joke."),
    (4, None, "'Si? Idiot.' Louis echoes the word as a question, then the insult. Idiot is the same word in Russian, but stressed on the end: idi-OT."),
    (5, None, "'Si is in Italian.' A dash stands in for 'is'. 'Po-italyanski' follows the po and ski pattern from the first line."),
    (6, None, "'In French it will be oui.' Russians use budet, 'will be', for how something is said in another language. 'Kak budet po-angliyski?' is the everyday 'how do you say it in English?'."),
    (7, None, "'Yes, of course, I know this.' 'Konechno', of course, is one of the most common words in Russian. 'Znayu' is 'I know', from znat, to know."),
    (8, None, "'Maximilian, do you understand the French language?' Elena says vy ponimaete, the polite 'you understand'. 'Frantsuzskiy yazyk' is the full name; most people drop yazyk, as Max does next."),
    (9, None, "'Of course, I understand French perfectly.' Here 'French' stands alone, frantsuzskiy, and it's an adjective that does duty as the name of the language."),
    (10, None, "'Well, what will you do now?' 'Budesh delat' is 'you will be doing': budesh, a form of 'be', plus delat. That's the future of an action with no clear finish."),
    (11, None, "'I will read this recipe and prepare the dish.' 'Prochitayu' and prigotovlyu are single finished acts, so they are already future on their own, no 'budu' needed. Compare Louis's budesh delat just before."),
    (12, None, "'This will be very funny.' 'Budet', 'will be', is the one future form of 'be' Russian can't drop. 'Smeshno' is 'funny' in the sense of 'it's funny'."),
]
