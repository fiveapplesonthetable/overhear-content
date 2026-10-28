# Authoring module for kukhnya-s01e19-scene-20.
ID = 'kukhnya-s01e19-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 20
TITLE = 'Сомнения  (Doubts)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = 'Max and Vika are together at last, and Max is thinking about what that really means. Hear it in Russian before we unpack it; the ideas are big but the words are small.'
OPENER = 'Now their talk, one thought at a time.'
TRANSITION = "And here's the whole thought again, in Russian."
OUTRO = 'Max put a big idea into small words, and you followed it: to know what you have. See you next time!'
CLOSING = ('vika', 'Увидимся!')
STORY = [
    ('vika', 'О чём ты думаешь, Макс?', 'What are you thinking about, Max?', [], ''),
    ('max', 'О том, что у нас есть.', 'About what we have.', [], ''),
    ('vika', 'А что у нас есть?', 'And what do we have?', [], ''),
    ('max', 'Мы есть друг у друга.', 'We have each other.', [], ''),
    ('vika', 'Это правда.', "That's true.", [], ''),
    ('max', 'Многих часто терзают сомнения.', 'Many people are often troubled by doubts.', [(379, 'Многих часто терзают сомнения')], ''),
    ('vika', 'Какие сомнения?', 'What doubts?', [], ''),
    ('max', 'Насколько тебе дорого то, что ты имеешь.', 'About how much what you have means to you.', [(379, 'насколько тебе дорого то, что ты имеешь')], ''),
    ('vika', 'А тебе дорого то, что у тебя есть?', 'And does what you have mean a lot to you?', [], ''),
    ('max', 'Очень дорого.', 'A great deal.', [], ''),
    ('vika', 'И мне, Макс.', 'To me too, Max.', [], ''),
    ('max', 'Я не хочу это потерять.', "I don't want to lose it.", [], ''),
    ('vika', 'Ты не потеряешь.', "You won't lose it.", [], ''),
]
WALK = [
    (0, None, "'What are you thinking about, Max?' \"O chyom\", 'about what', is the question form; Kostya used it about Nastya's post. \"Dumaesh'\", 'you think', also covers 'you're thinking'."),
    (1, None, "'About what we have.' \"O tom, chto\", 'about that, which', stands in for 'about what'. \"U nas est'\" is 'we have'."),
    (2, None, "'And what do we have?' Vika just turns his words into a question. In Russian only the voice rising on \"chto\" makes it one."),
    (3, None, "'We have each other.' \"My est' drug u druga\" is literally 'we exist at each other'. It's the \"drug drugu\", 'each other', pair again, with \"u\" slotted in the middle."),
    (4, None, "'That's true.' \"Eto pravda\", 'this truth', needs no 'is'. \"Pravda\" is what Max asked, delighted, in the last scene."),
    (5, None, "'Many people are often troubled by doubts.' \"Terzayut\" means 'torment', a bookish word. \"Mnogikh\", 'many people', is the one being tormented, so it comes first."),
    (6, None, "'What doubts?' \"Kakie\", 'what kind of', ends in -ie because \"somneniya\" is plural. One doubt is \"somnenie\"."),
    (7, None, "'About how much what you have means to you.' \"Dorogo\" means both 'dear' and 'expensive'. Here it's 'dear': \"tebe dorogo\", 'it is dear to you'."),
    (8, None, "'And does what you have mean a lot to you?' Vika swaps Max's \"imeesh'\", 'you have', for the everyday \"u tebya est'\". \"Imet'\" is more formal."),
    (9, None, "'A great deal.' \"Ochen' dorogo\", 'very dear', is a full answer on its own. In a shop the same two words mean 'very expensive'."),
    (10, None, "'To me too, Max.' I \"mne\", 'and to me', is a short way of saying 'it's dear to me too'. Here i means 'also'."),
    (11, None, "'I don't want to lose it.' \"Poteryat'\", 'to lose', is the one-time version of \"teryat'\". \"Ne khochu\", 'I don't want', comes right before it."),
    (12, None, "'You won't lose it.' \"Poteryaesh'\", 'you'll lose', is already future, so no 'will' is needed. Vika makes it a promise."),
]
