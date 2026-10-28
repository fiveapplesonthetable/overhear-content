ID = "kukhnya-s01e15-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 19
TITLE = "Омлет шефа  (The Chef's Omelet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Виктор', 'leva': 'Лёва', 'guest': 'Мама'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the morning, Chef Victor cooks breakfast for Leva and his mother. Leva wonders if this is Victor's way of apologizing for his earlier deception. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Доброе утро, виктор.",
     "Good morning, my friend.",
     [(366, 'Доброе утро. Доброе, доброе.')], "adapted"),
    ("guest", "Доброе утро.",
     "Good morning.",
     [(366, 'Доброе, доброе.')], "adapted"),
    ("guest", "Виктор приготовил такой омлет.",
     "Victor prepared such an omelet.",
     [(367, 'Виктор Петрович приготовил такой омлет.')], "adapted"),
    ("leva", "Это типа извинения?",
     "Is this a kind of apology?",
     [(368, 'Это типа извинения?')], "adapted"),
    ("anya", "Это типа омлет.",
     "This is a kind of omelet.",
     [(369, 'Это типа омлет.')], "adapted"),
    ("anya", "Ешь давай.",
     "Come on, eat.",
     [(370, 'Ешь давай, я на работу опоздаю.')], "adapted"),
    ("anya", "Я опоздаю на работу.",
     "I will be late for work.",
     [(370, 'я на работу опоздаю.')], "adapted"),
    ("guest", "Да, кушайте быстрее.",
     "Yes, eat faster.",
     [], "new"),
    ("leva", "Ладно, я съем это.",
     "Alright, I will eat this.",
     [], "new"),
    ("anya", "Это очень вкусно.",
     "This is very delicious.",
     [], "new"),
    ("guest", "Нам пора идти.",
     "It is time for us to go.",
     [], "new"),
    ("leva", "Спасибо за завтрак.",
     "Thank you for the breakfast.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Good morning, my friend.' — Notice the adjective meaning 'good' paired with the noun for 'morning'."),
    (1, None,
     "'Good morning.' — Notice the adjective meaning 'good' paired with the noun for 'morning'."),
    (2, None,
     "'Victor prepared such an omelet.' — Notice the proper name meaning 'Viktor' paired with the verb for 'cooked'."),
    (3, None,
     "'Is this a kind of apology?' — Notice the pronoun meaning 'this' paired with the noun for 'guy, fellow; type'."),
    (4, None,
     "'This is a kind of omelet.' — Notice the pronoun meaning 'this' paired with the noun for 'guy, fellow; type'."),
    (5, None,
     "'Come on, eat.' — Notice the verb meaning 'eat' paired with the verb for 'let's'."),
    (6, None,
     "'I will be late for work.' — Notice the pronoun meaning 'I' paired with the verb for 'to be late'."),
    (7, None,
     "'Yes, eat faster.' — Notice the verb meaning 'eat' paired with the adverb for 'faster'."),
    (8, None,
     "'Alright, I will eat this.' — Notice the pronoun meaning 'I' paired with the verb for 'to eat up'."),
    (9, None,
     "'This is very delicious.' — Notice the pronoun meaning 'this' paired with the adverb for 'very much'."),
    (10, None,
     "'It is time for us to go.' — Notice the pronoun meaning '(to) us' paired with the adverb for 'it's time'."),
    (11, None,
     "'Thank you for the breakfast.' — Notice the interjection meaning 'thank you' paired with the noun for 'breakfast'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Спасибо за завтрак.")
