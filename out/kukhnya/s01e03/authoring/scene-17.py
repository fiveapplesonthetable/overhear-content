"""Scene 17 — A Dangerous Quarrel (s01e03, 00:19:44–00:20:40)."""

ID = "kukhnya-s01e03-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 17
TITLE = "Опасная ссора  (A Dangerous Quarrel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 298-318. Max attempts to apologize to Vika behind the restaurant, "
    "when her jealous ex Vadim bursts in and threatens them until Chef Barinov steps in."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vika": "anja",
    "vadim": "angelina",
}

LABELS = {
    "anya": "Макс",
    "vika": "Вика",
    "vadim": "Вадим",
}

INTRO = (
    "Behind the restaurant Claude Monet, Max catches Vika alone to apologize for his clumsy behavior. "
    "Their uneasy conversation is suddenly shattered when Vika's aggressive ex-lover Vadim arrives, "
    "demanding explanations and escalating the confrontation into real danger. "
    "Let's listen to their intense exchange in Russian first."
)

STORY = [
    ("anya", "Вика, пожалуйста, прости меня за всё.",
     "Vika, please forgive me for everything.",
     [(298, "ну прости меня")], "Max apologizes"),

    ("vika", "Почему я всегда верю не тем людям?",
     "Why do I always trust the wrong people?",
     [(301, "Ну почему меня тянет")], "Vika laments"),

    ("anya", "Каждый человек может совершить ошибку.",
     "Every person can make a mistake.",
     [(304, "все ошибаются")], "Max seeks forgiveness"),

    ("vika", "Я сама виновата в этой ситуации.",
     "I myself am to blame for this situation.",
     [(306, "это я виновата")], "Vika blames herself"),

    ("vadim", "Так значит, это правда, вы вместе?",
     "So that means it is true, you are together?",
     [(310, "Так значит, это правда")], "Vadim confronts them"),

    ("vika", "Вадим, что ты здесь делаешь?",
     "Vadim, what are you doing here?",
     [(309, "Вадик")], "Vika is shocked"),

    ("vadim", "Я пришёл поговорить с тобой прямо сейчас.",
     "I came to talk with you right now.",
     [], "Vadim's demand"),

    ("vadim", "А этот парень должен немедленно уйти!",
     "And this guy must leave immediately!",
     [], "Vadim dismisses Max"),

    ("anya", "Выбирай слова, когда говоришь с ней!",
     "Choose your words when talking with her!",
     [(312, "подбирай выражение")], "Max defends Vika"),

    ("anya", "Ты разговариваешь с красивой девушкой.",
     "You are talking to a beautiful girl.",
     [(313, "с девушкой разговариваешь")], "Max demands respect"),

    ("vadim", "Ты что мне сейчас сказал, щенок?",
     "What did you just say to me, pup?",
     [(314, "Ты что сказал")], "Vadim bristles"),

    ("anya", "Я сказал тебе: отойди от неё!",
     "I told you: step away from her!",
     [(315, "отстань от неё сказал")], "Max stands firm"),

    ("vika", "Макс, прекрати, у него есть пистолет!",
     "Max, stop, he has a gun!",
     [(318, "Прячь мушку")], "Vika panics"),
]

OPENER = "Now let's examine this high-stakes dramatic confrontation line by line."

WALK = [
    (0, None,
     "'Vika, please forgive me for everything.' Max attempts to make peace after their disastrous morning together."),
    (1, None,
     "'Why do I always trust the wrong people?' Vika expresses bitter frustration with her choices in men."),
    (2, None,
     "'Every person can make a mistake.' Max tries to reason with Vika using an impersonal philosophical truth."),
    (3, None,
     "'I myself am to blame for this situation.' Vika refuses easy comfort and shoulders the blame alone."),
    (4, None,
     "'So that means it is true, you are together?' Vadim steps out from the shadows consumed by furious jealousy."),
    (5, None,
     "'Vadim, what are you doing here?' Vika is startled and frightened by her aggressive former lover."),
    (6, None,
     "'I came to talk with you right now.' Vadim refuses to leave until he gets the answers he demands."),
    (7, None,
     "'And this guy must leave immediately!' The prosecutor aggressively orders the young cook out of the way."),
    (8, None,
     "'Choose your words when talking with her!' Max courageously steps forward to shield Vika from verbal abuse."),
    (9, None,
     "'You are talking to a beautiful girl.' Max insists that Vadim show basic decency and respect."),
    (10, None,
     "'What did you just say to me, pup?' Enraged that a lowly cook dares challenge him, Vadim turns aggressive."),
    (11, None,
     "'I told you: step away from her!' Max refuses to back down despite the growing physical threat."),
    (12, None,
     "'Max, stop, he has a gun!' Vika screams in horror as Vadim reaches into his jacket for a weapon."),
]

TRANSITION = "Now let's listen to this tense back-alley showdown once more without interruption."

OUTRO = (
    "Just as Vadim pulls out his weapon, Chef Barinov storms into the alley and brings the dangerous duel to an abrupt halt."
)

CLOSING = ("vika", "Макс, прекрати, у него есть пистолет!")
