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
    (0, None, "'What did he say?' The first content word means 'what', and 'said' rounds out the thought."),
    (1, None, "'He told us to leave.' Notice the word order: 'he' comes first, and 'to leave' finishes the sentence. And Chef jumps in."),
    (2, None, "'I do not believe this.' Here 'I' sets up the idea, while 'this' comes at the end for emphasis."),
    (3, None, "'Is this the end?' You'll hear 'this' all the time in the show, here connected with 'end'."),
    (4, None, "'I do not know.' The key word here means 'I', which Chef combines with 'know'. Maks answers straight away."),
    (5, None, "'Chef, what to do?' Maks starts with 'chef' and pairs it with 'what' to make the point clear."),
    (6, None, "'We must leave.' In Russian, 'we' leads into 'to leave' in a very natural everyday phrasing."),
    (7, None, "'I am very sorry.' Anya starts with 'to me' and pairs it with 'very much' to make the point clear."),
    (8, None, "'Pack your things.' The first content word means 'to intend', and 'to intend' rounds out the thought."),
    (9, None, "'I am sorry.' The key word here means 'sorry', which Anya combines with 'sorry'."),
    (10, None, "'It is my duty.' Listen for the word meaning 'this' right alongside 'debt' in this line. And Chef jumps in."),
    (11, None, "'Good.' You'll hear 'good' all the time in the show, here connected with 'good'."),
]

TRANSITION = "Let's listen to the dialog one more time."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around my duty, and for the words meaning 'said' and 'to leave'. You'll catch them now. See you next time."
CLOSING = ("anya", "До свидания!")
