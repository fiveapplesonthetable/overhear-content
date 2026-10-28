ID = "kukhnya-s01e20-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 3
TITLE = "Скрытый смысл  (Hidden Meaning)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 3"

INTRO = "Kostya tells Max about Nastya's weird staircase metaphor. Max explains the true meaning of her words and then receives a surprising message from Vika."

STORY = [
    ("kostya", "Настя сказала, что мы идём по лестнице.",
     "Nastya said that we are walking on a staircase.",
     [(79, 'поднимаемся по какой-то лестнице')], "adapted"),
    ("kostya", "И если мы остановимся, то разобьёмся.",
     "And if we stop, then we will break.",
     [(79, 'можем разбиться')], "adapted"),
    ("kostya", "Я ничего не понял.",
     "I did not understand anything.",
     [(81, 'ничего не понял')], "adapted"),
    ("anya", "А чё ты не понял?",
     "And what did you not understand?",
     [(82, 'чё ты не понял')], "adapted"),
    ("anya", "Она тебе на свадьбу намекает.",
     "She is hinting at a wedding to you.",
     [(82, 'на свадьбу намекает')], "adapted"),
    ("kostya", "Да ладно, ты серьёзно?",
     "Come on, are you serious?",
     [(83, 'Да ладно')], "adapted"),
    ("anya", "Сделай вид, что ты ничего не понял.",
     "Pretend that you did not understand anything.",
     [(85, 'Сделай вид, что ты ничего не понял')], "adapted"),
    ("kostya", "Так я и так ничего не понял.",
     "But I already did not understand anything.",
     [(87, 'Так я и так ничего не понял')], "adapted"),
    ("anya", "Ну вот, тебе даже врать не придётся.",
     "Well there, you will not even have to lie.",
     [(88, 'даже врать не придётся')], "adapted"),
    ("kostya", "Чего там? Что она прислала?",
     "What is there? What did she send?",
     [(93, 'Чего там')], "adapted"),
    ("anya", "Она прислала мне фото красивого кольца.",
     "She sent me a photo of a beautiful ring.",
     [(96, 'Красивое кольцо')], "adapted"),
    ("anya", "Она мне на дорогой подарок намекает.",
     "She is hinting at an expensive gift to me.",
     [(95, 'на подарок намекает')], "adapted"),
    ("anya", "Мне на него год работать надо.",
     "I need to work a year for it.",
     [(97, 'Мне на него год работать надо')], "adapted"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Nastya said that we are walking on a staircase.' In Russian, 'Nastya' leads into 'stairs' in a very natural everyday phrasing."),
    (1, None,
     "'And if we stop, then we will break.' Here 'we' sets up the idea, while 'to crash' comes at the end for emphasis."),
    (2, None,
     "'I did not understand anything.' You'll hear 'I' all the time in the show, here connected with 'understood?'."),
    (3, None,
     "'And what did you not understand?' Max puts 'what' up front so the listener immediately catches the tone, followed by 'you'."),
    (4, None,
     "'She is hinting at a wedding to you.' The key word here means 'it', which Max combines with 'for you'."),
    (5, None,
     "'Come on, are you serious?' The first content word means 'you', and 'seriously' rounds out the thought."),
    (6, None,
     "'Pretend that you did not understand anything.' Max starts with 'make' and pairs it with 'appearance' to make the point clear. Then Kostya replies."),
    (7, None,
     "'But I already did not understand anything.' Kostya puts 'I' up front so the listener immediately catches the tone, followed by 'nothing'."),
    (8, None,
     "'Well there, you will not even have to lie.' Max puts 'for you' up front so the listener immediately catches the tone, followed by 'to lie'."),
    (9, None,
     "'What is there? What did she send?' Here 'what?' sets up the idea, while 'to send' comes at the end for emphasis. And Max jumps in."),
    (10, None,
     "'She sent me a photo of a beautiful ring.' The key word here means 'it', which Max combines with 'to send'."),
    (11, None,
     "'She is hinting at an expensive gift to me.' The first content word means 'it', and 'to hint' rounds out the thought."),
    (12, None,
     "'I need to work a year for it.' Notice the word order: 'to me' comes first, and 'it is necessary' finishes the sentence."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max realizes Vika expects an extremely expensive gift, leaving him stressed about his financial situation."
CLOSING = ("anya", "Мне на него год работать надо.")
