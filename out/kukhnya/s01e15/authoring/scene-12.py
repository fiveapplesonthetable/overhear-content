ID = "kukhnya-s01e15-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 12
TITLE = "Выселение шефа  (Evicting the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Лёва', 'leva': 'Виктор'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Still furious about the deception, Leva confronts Chef Victor through a closed door. He firmly demands that Victor pack his bags and move out of his and his mother's apartment immediately. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Открывай, нам надо поговорить.",
     "Open up, we need to talk.",
     [(288, 'Открывай, поговорить надо.')], "adapted"),
    ("leva", "Лёва, что ты хочешь?",
     "Leva, what do you want?",
     [(289, 'Лёва, что ты хочешь, Лёва?')], "adapted"),
    ("anya", "Я хочу сказать тебе одну вещь.",
     "I want to tell you one thing.",
     [(291, 'Я хочу сказать.')], "adapted"),
    ("anya", "Чтобы ноги твоей больше не было в моём доме.",
     "So that your foot is no longer in my house.",
     [(292, 'Чего? Чтобы ноги вашей больше в моем доме не было.')], "adapted"),
    ("anya", "Сегодня же собирай вещи и уезжай.",
     "Today pack your things and leave.",
     [(293, 'Сегодня же собираете вещи и уезжаете.')], "adapted"),
    ("anya", "Больше ты у нас с мамой не живёшь.",
     "You no longer live with me and Mom.",
     [(294, 'Больше вы у нас с мамой не живете.')], "adapted"),
    ("anya", "Тебе это ясно?",
     "Is that clear to you?",
     [(295, 'Ясно?')], "adapted"),
    ("leva", "Да пожалуйста.",
     "Yes, sure.",
     [(295, 'Да пожалуйста.')], "adapted"),
    ("leva", "Очень мне надо.",
     "As if I need it.",
     [(296, 'Больно надо.')], "adapted"),
    ("anya", "Я жду, пока ты уйдёшь.",
     "I am waiting until you leave.",
     [], "new"),
    ("leva", "Я уже ухожу.",
     "I am already leaving.",
     [], "new"),
    ("anya", "Ключи оставь на столе.",
     "Leave the keys on the table.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Open up, we need to talk.' — Notice the verb meaning 'to open' paired with the pronoun for '(to) us'."),
    (1, None,
     "'Leva, what do you want?' — Notice the proper name meaning 'Lyova' paired with the pronoun for 'what'."),
    (2, None,
     "'I want to tell you one thing.' — Notice the pronoun meaning 'I' paired with the verb for 'want'."),
    (3, None,
     "'So that your foot is no longer in my house.' — Notice the noun meaning 'legs' paired with the det for 'your'."),
    (4, None,
     "'Today pack your things and leave.' — Notice the adverb meaning 'today' paired with the verb for 'pack, gather'."),
    (5, None,
     "'You no longer live with me and Mom.' — Notice the adverb meaning 'more' paired with the pronoun for 'you'."),
    (6, None,
     "'Is that clear to you?' — Notice the pronoun meaning 'for you, to you' paired with the pronoun for 'this'."),
    (7, None,
     "'Yes, sure.' — Notice the particle meaning 'yes (  = really?)' paired with the particle for 'please'."),
    (8, None,
     "'As if I need it.' — Notice the adverb meaning 'very much' paired with the pronoun for 'to me (  = I have no time)'."),
    (9, None,
     "'I am waiting until you leave.' — Notice the pronoun meaning 'I' paired with the verb for 'I'm waiting'."),
    (10, None,
     "'I am already leaving.' — Notice the pronoun meaning 'I' paired with the adverb for 'already, now'."),
    (11, None,
     "'Leave the keys on the table.' — Notice the noun meaning 'the keys' paired with the verb for 'keep, leave'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Ключи оставь на столе.")
