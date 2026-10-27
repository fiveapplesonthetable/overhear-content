ID = "kukhnya-s01e16-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 22
TITLE = "Мой долг  (My duty)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "maks": "angelina"}
LABELS = {"anya": "Anya", "chef": "Chef", "maks": "Maks"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"

INTRO = ("The fire inspector makes a harsh decision. Let us see what happens next in this scene. Let's listen closely to their exchange in Russian first, and then walk through each line together.")

STORY = [
    ("chef", "Что он сказал?", "What did he say?", [], "new"),
    ("anya", "Он сказал нам уходить.", "He told us to leave.", [], "new"),
    ("chef", "Я не верю в это.", "I do not believe this.", [], "new"),
    ("anya", "Это конец?", "Is this the end?", [], "new"),
    ("chef", "Я не знаю.", "I do not know.", [], "new"),
    ("maks", "Шеф, что делать?", "Chef, what to do?", [], "new"),
    ("chef", "Мы должны уйти.", "We must leave.", [], "new"),
    ("anya", "Мне очень жаль.", "I am very sorry.", [], "new"),
    ("anya", "Собирайтесь.", "Pack your things.", [(285, "Собирайтесь.")], "adapted"),
    ("anya", "Извините.", "I am sorry.", [(286, "Извините,")], "adapted"),
    ("anya", "Это мой долг.", "It is my duty.", [(286, "это мой долг.")], "adapted"),
    ("chef", "Хорошо.", "Good.", [], "new"),
]

OPENER = "Let's review the scene line by line."

WALK = [
    (0, None, "'What did he say?' -- The speaker asks a question. ENG"),
    (1, None, "'He told us to leave.' -- The speaker states this. ENG"),
    (2, None, "'I do not believe this.' -- The speaker states this. ENG"),
    (3, None, "'Is this the end?' -- The speaker states this. ENG"),
    (4, None, "'I do not know.' -- The speaker states this. ENG"),
    (5, None, "'Chef, what to do?' -- The speaker states this. ENG"),
    (6, None, "'We must leave.' -- The speaker states this. ENG"),
    (7, None, "'I am very sorry.' -- The speaker states this. ENG"),
    (8, None, "'Pack your things.' -- The speaker states this. ENG"),
    (9, None, "'I am sorry.' -- The speaker states this. ENG"),
    (10, None, "'It is my duty.' -- The speaker states this. ENG"),
    (11, None, "'Good.' -- The speaker states this. ENG"),
]

TRANSITION = "Let's listen to the dialog one more time."
OUTRO = "Things are getting very interesting in the kitchen. See you next time."
CLOSING = ("anya", "До свидания!")
