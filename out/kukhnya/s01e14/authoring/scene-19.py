ID = "kukhnya-s01e14-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 19
TITLE = "План Макса  (Max's Plan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Илья', 'guest': 'Саша'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In a brief moment of chaos, Max realizes he needs to take control of a difficult situation. He tells his colleagues that they will figure it out and urges them to go. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ладно, мы разберёмся с этим.",
     "Alright, we will figure this out.",
     [(280, 'Ладно, разберёмся.')], "adapted"),
    ("anya", "Всё будет хорошо.",
     "Everything will be fine.",
     [], "exact"),
    ("leva", "Что нам делать сейчас?",
     "What should we do now?",
     [], "exact"),
    ("anya", "Поехали.",
     "Let's go.",
     [(281, 'Поехали.')], "adapted"),
    ("guest", "Куда мы едем?",
     "Where are we going?",
     [], "exact"),
    ("anya", "Мы никуда не едем.",
     "We are not going anywhere.",
     [], "exact"),
    ("anya", "Это значит, что мы начинаем.",
     "It means that we are starting.",
     [], "exact"),
    ("leva", "Теперь я всё понял.",
     "Now I understand everything.",
     [(282, 'Теперь')], "adapted"),
    ("guest", "Тогда давайте работать.",
     "Then let's work.",
     [], "exact"),
    ("anya", "Да, за работу.",
     "Yes, back to work.",
     [], "exact"),
    ("leva", "У нас мало времени.",
     "We have little time.",
     [], "new"),
    ("guest", "Мы должны успеть.",
     "We must be in time.",
     [], "new"),
    ("anya", "Конечно мы успеем.",
     "Of course we will be in time.",
     [], "new"),
    ("leva", "Тогда начинаем прямо сейчас.",
     "Then we start right now.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Alright, we will figure this out.' — Notice the pronoun meaning 'we' paired with the verb for 'will sort this out'."),
    (1, None,
     "'Everything will be fine.' — Notice the det meaning 'everything' paired with the verb for 'will be'."),
    (2, None,
     "'What should we do now?' — Notice the pronoun meaning 'what' paired with the pronoun for '(to) us'."),
    (3, None,
     "'Let's go.' — Built around the key verb meaning 'here we go, let's go'."),
    (4, None,
     "'Where are we going?' — Notice the adverb meaning 'where to' paired with the pronoun for 'we'."),
    (5, None,
     "'We are not going anywhere.' — Notice the pronoun meaning 'we' paired with the adverb for 'nowhere, anywhere (with motion)'."),
    (6, None,
     "'It means that we are starting.' — Notice the pronoun meaning 'this' paired with the adverb for 'then, so'."),
    (7, None,
     "'Now I understand everything.' — Notice the adverb meaning 'now' paired with the pronoun for 'I'."),
    (8, None,
     "'Then let's work.' — Notice the adverb meaning 'back then' paired with the verb for 'let's (do it)'."),
    (9, None,
     "'Yes, back to work.' — Built around the key noun meaning 'job'."),
    (10, None,
     "'We have little time.' — Notice the pronoun meaning 'us' paired with the adverb for 'little, not enough'."),
    (11, None,
     "'We must be in time.' — Notice the pronoun meaning 'we' paired with the adjective for 'must, should'."),
    (12, None,
     "'Of course we will be in time.' — Notice the adverb meaning 'of course' paired with the pronoun for 'we'."),
    (13, None,
     "'Then we start right now.' — Notice the adverb meaning 'back then' paired with the verb for 'are starting'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Тогда начинаем прямо сейчас.")
