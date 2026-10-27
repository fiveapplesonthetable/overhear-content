ID = "kukhnya-s01e01-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = "Ночной разговор  (Night Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 23. Late at night, Max and Vika talk intimately before falling asleep. "
    "Max speaks of his love for cooking and his high hopes for tomorrow's job interview."
)

INTRO = (
    "Late in the quiet night, Max and Vika lie awake talking in the dim room. "
    "Vika asks Max if he truly loves cooking, and Max passionately describes food as genuine art and happiness. "
    "They exchange gentle jokes about fate and coincidences before finally wishing each other good night. "
    "Let's listen to their bedroom conversation in Russian first."
)

STORY = [
    ("vika", "Макс, ты уже почти засыпаешь?",
     "Max, are you almost falling asleep?",
     [], "new"),
    ("anya", "Нет, я просто любуюсь тобой.",
     "No, I am simply admiring you.",
     [], "new"),
    ("vika", "Ты правда так сильно любишь готовить?",
     "Do you really love cooking so much?",
     [], "new"),
    ("anya", "Еда — это настоящая любовь и страсть!",
     "Food is true love and passion!",
     [(5, "Еда – это страсть"), (6, "Еда – это любовь")], "adapted"),
    ("vika", "Ты говоришь о еде как поэт.",
     "You speak about food like a poet.",
     [], "new"),
    ("anya", "Хорошая еда дарит людям огромное счастье.",
     "Good food gives people immense happiness.",
     [(6, "Еда – это жизнь для каждого человека")], "adapted"),
    ("vika", "В каком ресторане у тебя собеседование?",
     "At which restaurant is your interview?",
     [(18, "поваром в ресторан")], "adapted"),
    ("anya", "В самом лучшем французском ресторане Москвы.",
     "In the very best French restaurant in Moscow.",
     [], "new"),
    ("vika", "Наш город полон удивительных совпадений.",
     "Our city is full of surprising coincidences.",
     [], "new"),
    ("anya", "Я рад, что встретил тебя сегодня.",
     "I am glad that I met you today.",
     [], "new"),
    ("vika", "Ложись спать, тебе надо хорошо отдохнуть.",
     "Go to sleep, you need to rest well.",
     [], "new"),
    ("anya", "Спокойной ночи, прекрасная Вика.",
     "Good night, beautiful Vika.",
     [], "new"),
    ("vika", "Спокойной ночи, мой храбрый повар.",
     "Good night, my brave cook.",
     [], "new"),
]

OPENER = "Now let's examine Max and Vika's quiet nighttime conversation line by line."

WALK = [
    (0, None,
     "'Max, are you almost falling asleep?' Vika whispers with an intensifying adverb and imperfective verb."),
    (1, None,
     "'No, I am simply admiring you.' Max responds tenderly using a reflexive verb with an instrumental pronoun."),
    (2, None,
     "'Do you really love cooking so much?' Vika asks about his passion with an infinitive verb."),
    (3, None,
     "'Food is true love and passion!' Max defines cooking with an emphatic demonstrative predicate."),
    (4, None,
     "'You speak about food like a poet.' Vika smiles at his lyricism with a comparative preposition."),
    (5, None,
     "'Good food gives people immense happiness.' Max shares his philosophy with a transitive verb and dative noun."),
    (6, None,
     "'At which restaurant is your interview?' Vika inquires about his appointment with a prepositional question."),
    (7, None,
     "'In the very best French restaurant in Moscow.' Max names his dream venue with superlative adjectives."),
    (8, None,
     "'Our city is full of surprising coincidences.' Vika reflects with a short predicate adjective and genitive plural."),
    (9, None,
     "'I am glad that I met you today.' Max expresses gratitude for their meeting with a past perfective verb."),
    (10, None,
     "'Go to sleep, you need to rest well.' Vika urges him to rest using an imperative verb and predicative phrase."),
    (11, None,
     "'Good night, beautiful Vika.' Max wishes her restful sleep with a standard Russian nighttime greeting."),
    (12, None,
     "'Good night, my brave cook.' Vika returns the greeting affectionately with a vocative noun phrase."),
]

TRANSITION = "Now let's listen to their bedtime conversation again without interruption."
OUTRO = (
    "Max and Vika drift off to sleep together, unaware of how their paths will cross again. "
    "In the next scene, morning arrives with a sudden and awkward goodbye."
)
CLOSING = ("anya", "Еда — это настоящая любовь и страсть!")
