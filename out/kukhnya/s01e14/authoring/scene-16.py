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
    (0, None, ["'Here everything is in French.' Let's inspect the sentence: ", ('elena', 'по'), '-', ('elena', 'французски'), ' has a common prefix and suffix used to describe languages.']),
    (1, None, ["'For our chef this is not a problem.' Let us examine the dialogue: ", ('elena', 'нашего'), ('elena', 'шефа'), ' changes its endings because of the word before it. ', ('elena', 'проблема'), " ends in an 'a', which affects the words around it."]),
    (2, None, ["'Right, Maximilian?' Now let's inspect the sentence: ", ('elena', 'Правда'), " means 'truth', and on the end of a question it works like 'isn't it?'. She puts him on the spot."]),
    (3, None, ["'Si.' Now let's consider the dialogue: ", ('max', 'Си'), " is an Italian 'yes', written in Russian letters. Max has chosen the wrong foreign language, which is the whole joke."]),
    (4, None, ["'Si? Idiot.' Louis echoes the term as a question, then the insult. ", ('louis', 'Идиот'), ' is the same word in Russian, but stressed on the end.']),
    (5, None, ["'Si is in Italian.' A dash stands in for 'is'. ", ('louis', 'по'), '-', ('louis', 'итальянски'), " follows the same pattern as 'in French' from the first line."]),
    (6, None, ["'In French it will be oui.' Russians use ", ('louis', 'будет'), " for how something is said in another language. You use this to ask 'how do you say it in English?'."]),
    (7, None, ["'Yes, of course, I know this.' We will inspect this line: ", ('max', 'конечно'), ' is one of the most common words in Russian. ', ('max', 'знаю'), " is 'I know'."]),
    (8, None, ["'Maximilian, do you understand the French language?' Elena uses the polite ", ('elena', 'вы'), ('elena', 'понимаете'), ' here. The full name of the language ends with ', ('elena', 'французский'), ('elena', 'язык'), ', but most people drop the second word, as Max does next.']),
    (9, None, ["'Of course, I understand French perfectly.' Here 'French' stands alone, ", ('max', 'французский'), ', describing the language.']),
    (10, None, ["'Well, what will you do now?' Let's examine the dialogue: ", ('louis', 'будешь'), ('louis', 'делать'), " is 'you will be doing'. That's the future of an action with no clear finish."]),
    (11, None, ["'I will read this recipe and prepare the dish.' Now we can consider the dialogue: ", ('max', 'прочитаю'), ' and ', ('max', 'приготовлю'), ' are single finished acts, so they are already future on their own. Compare what Louis said just before.']),
    (12, None, ["'This will be very funny.' Let us examine this part: ", ('louis', 'будет'), " is the one future form of 'be' Russian can't drop. ", ('louis', 'смешно'), " means 'funny'."]),
]
