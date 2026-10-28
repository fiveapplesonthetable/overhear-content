ID = "kukhnya-s01e16-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 4
TITLE = "Любопытный Макс  (Curious Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Макс', 'leva': 'Виктор'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the kitchen, Max is bored and looking for a distraction. He approaches Chef Victor and curiously asks about the special dish the chef is preparing, but Victor quickly shuts him down. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Шеф.",
     "Chef.",
     [(33, 'Шеф.')], "adapted"),
    ("leva", "Что тебе надо?",
     "What do you need?",
     [], "new"),
    ("anya", "А что вы готовите?",
     "And what are you preparing?",
     [(34, 'А что вы готовите?')], "adapted"),
    ("leva", "А тебе какое дело?",
     "And what is it to you?",
     [(34, 'Тебе какое дело?')], "adapted"),
    ("leva", "Тебе нечем заняться?",
     "Do you have nothing to do?",
     [(35, 'Тебе что, заняться нечем?')], "adapted"),
    ("anya", "У меня есть пять минут.",
     "I have five minutes.",
     [(35, 'Ну, у меня пять минут есть,')], "adapted"),
    ("anya", "Я хотел поучиться у вас.",
     "I wanted to learn from you.",
     [(35, 'я хотел поучиться у вас.')], "adapted"),
    ("leva", "Иди работай.",
     "Go work.",
     [], "new"),
    ("anya", "А можно попробовать?",
     "And can I try it?",
     [(36, 'А можно попробовать?')], "adapted"),
    ("leva", "Нет, нельзя.",
     "No, you cannot.",
     [], "new"),
    ("anya", "Почему?",
     "Why?",
     [], "new"),
    ("leva", "Потому что я так сказал.",
     "Because I said so.",
     [], "new"),
    ("anya", "Ладно, я понял.",
     "Alright, I understand.",
     [], "new"),
    ("leva", "Тогда иди отсюда.",
     "Then go from here.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Chef.' — Built around the key proper name meaning 'chef, boss'."),
    (1, None,
     "'What do you need?' — Notice the pronoun meaning 'what' paired with the pronoun for 'for you, to you'."),
    (2, None,
     "'And what are you preparing?' — Notice the pronoun meaning 'what' paired with the pronoun for 'you'."),
    (3, None,
     "'And what is it to you?' — Notice the pronoun meaning 'for you, to you' paired with the adjective for 'what a'."),
    (4, None,
     "'Do you have nothing to do?' — Notice the pronoun meaning 'for you, to you' paired with the noun for 'nothing (to do it with)'."),
    (5, None,
     "'I have five minutes.' — Notice the pronoun meaning 'me' paired with the verb for 'there is (   = I have)'."),
    (6, None,
     "'I wanted to learn from you.' — Notice the pronoun meaning 'I' paired with the verb for 'wanted'."),
    (7, None,
     "'Go work.' — Notice the verb meaning 'go' paired with the verb for 'work'."),
    (8, None,
     "'And can I try it?' — Notice the adverb meaning 'may, can' paired with the verb for 'to taste'."),
    (9, None,
     "'No, you cannot.' — Built around the key adverb meaning 'not allowed, can't'."),
    (10, None,
     "'Why?' — Built around the key adverb meaning 'why'."),
    (11, None,
     "'Because I said so.' — Notice the adverb meaning 'because (with )' paired with the pronoun for 'what'."),
    (12, None,
     "'Alright, I understand.' — Notice the pronoun meaning 'I' paired with the verb for 'understood? (got it?)'."),
    (13, None,
     "'Then go from here.' — Notice the adverb meaning 'back then' paired with the verb for 'go'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Тогда иди отсюда.")
