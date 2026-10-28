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
     "'Open up, we need to talk.' Russian expresses this impersonally, literally saying 'to me' or 'to you' with 'to talk'. And Viktor jumps in."),
    (1, None,
     "'Leva, what do you want?' — Notice the proper name meaning 'Lyova' paired with the pronoun for 'what'."),
    (2, None,
     "'I want to tell you one thing.' Here 'I' sets up the idea, while 'thing' comes at the end for emphasis."),
    (3, None,
     "'So that your foot is no longer in my house.' You'll hear 'legs' all the time in the show, here connected with 'house'."),
    (4, None,
     "'Today pack your things and leave.' The first content word means 'today', and 'go away' rounds out the thought."),
    (5, None,
     "'You no longer live with me and Mom.' Lyova puts 'more' up front so the listener immediately catches the tone, followed by 'you'."),
    (6, None,
     "'Is that clear to you?' Here 'for you' sets up the idea, while 'clear?' comes at the end for emphasis. Then Viktor replies."),
    (7, None,
     "'Yes, sure.' In Russian, 'yes' leads into 'please' in a very natural everyday phrasing."),
    (8, None,
     "'As if I need it.' Notice the word order: 'very much' comes first, and 'it is necessary' finishes the sentence."),
    (9, None,
     "'I am waiting until you leave.' A compact expression built around 'I' and 'you'll leave'. And Viktor jumps in."),
    (10, None,
     "'I am already leaving.' Here 'I' sets up the idea, while 'am leaving' comes at the end for emphasis."),
    (11, None,
     "'Leave the keys on the table.' You'll hear 'the keys' all the time in the show, here connected with 'table'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around evicting the chef, and for the words meaning 'to open' and 'to talk'. You'll catch them now. See you next time."
CLOSING = ("anya", "Ключи оставь на столе.")
