# Scene 16: Приглашение в кино (Invitation to the Movies)
# Cues 425-455: Samsonov brings flowers and invites Ilona to the cinema.

ID = "domashniy-arest-s01e10-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 16

TITLE = "Приглашение в кино  (Invitation to the Movies)"
LEVEL = "A1"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "ilona": "anja",
}

LABELS = {
    "anya": "Самсон",
    "ilona": "Илона",
}

INTRO = "Samsonov brings a large bouquet of fresh flowers to the campaign office and tries awkwardly to invite Ilona out on a real romantic date for the evening."

STORY = [
    ("anya", "Привет, Илона. Это тебе цветы.",
     "Hi, Ilona. These flowers are for you.",
     [(430, "Держи, от тебя.")], "adapted cue 430"),

    ("ilona", "Какие странные цветы!",
     "What strange flowers!",
     [(425, "Какие цветы?")], "adapted cue 425"),

    ("anya", "Хочешь, я куплю другие?",
     "If you want, I will buy others?",
     [(435, "хочешь, другие куплю.")], "adapted cue 435"),

    ("ilona", "Слушай, что тебе надо?",
     "Listen, what do you need?",
     [(436, "Слушай, что надо?")], ""),

    ("anya", "Я уже сказал тебе.",
     "I already told you.",
     [(437, "я тебе сказал уже, что.")], "adapted cue 437"),

    ("anya", "Давай я к тебе заскочу вечером.",
     "Let me drop by your place this evening.",
     [(438, "давай я к тебе вечером заскочу")], "adapted cue 438"),

    ("ilona", "Мужчины обычно ухаживают за женщинами.",
     "Men usually court women.",
     [(444, "мужики делают, когда за женщинами ухаживают")], "adapted cue 444"),

    ("anya", "Я тоже пытаюсь ухаживать.",
     "I am also trying to court.",
     [(445, "как я ухаживаю.")], "adapted cue 445"),

    ("ilona", "Тогда пригласи меня в кино.",
     "Then invite me to the movies.",
     [(446, "В кино пригласи.")], ""),

    ("anya", "Пойдём прямо сегодня вечером.",
     "Let's go right this evening.",
     [(447, "пошли в кино.")], "adapted cue 447"),

    ("ilona", "Сегодня я работаю. Завтра могу.",
     "Today I am working. Tomorrow I can.",
     [(448, "я на работе. Завтра могу.")], ""),

    ("anya", "Хорошо, пойдём завтра.",
     "Alright, let's go tomorrow.",
     [(449, "давай завтра.")], "adapted cue 449"),

    ("ilona", "Только не на боевик!",
     "Just not to an action movie!",
     [(454, "только не на мультике, не на боевике")], "adapted cue 454"),

    ("ilona", "Я люблю романтические фильмы.",
     "I love romantic movies.",
     [(455, "Романтическая.")], "adapted cue 455"),

    ("anya", "Договорились, я выберу фильм.",
     "Agreed, I will choose a movie.",
     [], "new line"),
]

OPENER = "Now let's see how Samsonov tries to invite Ilona on a movie date."

WALK = [
    (0, "Это тебе цветы.",
     "'These flowers are for you.' Samsonov presents the bouquet as an awkward opening gesture."),
    (2, None,
     "'If you want, I will buy others?' The conditional sentence uses the present tense verb to offer alternatives."),
    (6, None,
     "'Men usually court women.' The verb governs the preposition and instrumental case for the person being courted."),
    (8, None,
     "'Then invite me to the movies.' The imperative verb directs him to ask her out on a date."),
    (13, None,
     "'I love romantic movies.' The adjective is used in the accusative plural to describe her preferred genre."),
]

TRANSITION = "Let's listen to Samsonov's awkward invitation once again from the beginning."

OUTRO = "Ilona accepts the invitation on the condition that the movie is romantic."

CLOSING = ("ilona", "Посмотрим, что ты выберешь.")
