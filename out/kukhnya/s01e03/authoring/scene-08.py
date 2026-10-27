"""s01e03 scene 08: Знакомься, это Макс (Meet Max)."""

ID = "kukhnya-s01e03-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = "Знакомься, это Макс  (Meet Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja", "vadim": "angelina"}
LABELS = {"anya": "Вика", "max": "Макс", "vadim": "Вадим"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = (
    "Outside the dining hall, Max attempts an awkward conversation with art director Victoria about keeping their private encounter secret. "
    "Irritated by his clumsy assumptions, Victoria uses him to ward off her persistent ex-husband Vadim by introducing Max as her new boyfriend. "
    "Listen to the dialogue in Russian first."
)

STORY = [
    ("max", "Вика, нам нужно спокойно поговорить.",
     "Vika, we need to talk calmly.",
     [], "approaching nervously"),
    ("anya", "Моя личная жизнь тебя не касается.",
     "My personal life is none of your business.",
     [(199, "Моя личная жизнь тебя не касается")], "setting boundaries"),
    ("max", "Давай не будем никому ничего рассказывать.",
     "Let us not tell anyone anything.",
     [(202, "не надо им об этом рассказывать")], "suggesting secrecy"),
    ("anya", "Ты боишься, что я расскажу коллегам?",
     "Are you afraid that I will tell colleagues?",
     [(204, "Ты боишься, что я расскажу")], "challenging him"),
    ("max", "Я? Нет, мне вообще всё равно.",
     "Me? No, I do not care at all.",
     [(205, "Я? Да прям")], "denying his concern"),
    ("max", "Между нами всё равно ничего серьёзного нет.",
     "There is nothing serious between us anyway.",
     [(207, "у нас"), (208, "а так")], "downplaying their connection"),
    ("anya", "Ах вот как ты заговорил!",
     "Oh, so that is how you speak now!",
     [], "taking offense"),
    ("vadim", "Вика, постой! Кто этот молодой человек?",
     "Vika, wait! Who is this young man?",
     [(210, "ты хотел знать")], "interjecting jealously"),
    ("anya", "Вадим, ты хотел знать правду?",
     "Vadim, did you want to know the truth?",
     [(210, "Вадим, ты хотел знать")], "seizing the opportunity"),
    ("vadim", "Да, я хочу знать всё.",
     "Yes, I want to know everything.",
     [], "demanding answers"),
    ("anya", "Вот, познакомься с моим парнем.",
     "Here, meet my boyfriend.",
     [(211, "Вот, познакомься")], "making a dramatic move"),
    ("anya", "Это мой Макс, мы теперь вместе!",
     "This is my Max, we are together now!",
     [(212, "Это мой Максик")], "announcing their relationship"),
    ("max", "Очень приятно познакомиться, уважаемый Вадим.",
     "Very nice to meet you, esteemed Vadim.",
     [], "playing along politely"),
]

OPENER = "Let's review this awkward hallway confrontation line by line."

WALK = [
    (0, None,
     "'Vika, we need to talk calmly.' Max pulls Victoria aside near the corridor."),
    (1, None,
     "'My personal life is none of your business.' Victoria establishes firm personal boundaries."),
    (2, None,
     "'Let us not tell anyone anything.' Max clumsily suggests keeping their past encounter completely secret."),
    (3, None,
     "'Are you afraid that I will tell colleagues?' Victoria questions his underlying anxiety with sharp skepticism."),
    (4, None,
     "'Me? No, I do not care at all.' Max defensively denies being nervous."),
    (5, None,
     "'There is nothing serious between us anyway.' Max makes the tactical mistake of trivializing their connection."),
    (6, None,
     "'Oh, so that is how you speak now!' Victoria takes immediate offense at his dismissive attitude."),
    (7, None,
     "'Vika, wait! Who is this young man?' Her ex-husband Vadim interrupts to demand an explanation."),
    (8, None,
     "'Vadim, did you want to know the truth?' Victoria seizes the moment to solve two problems at once."),
    (9, None,
     "'Yes, I want to know everything.' Vadim insists on clarity about her romantic status."),
    (10, None,
     "'Here, meet my boyfriend.' Victoria turns the tables dramatically."),
    (11, None,
     "'This is my Max, we are together now!' Victoria shocks both men with her sudden declaration."),
    (12, None,
     "'Very nice to meet you, esteemed Vadim.' Max awkwardly plays along with his unexpected new role."),
]

TRANSITION = "Now let's listen to the whole conversation again at full speed."

OUTRO = (
    "Trapped in a spontaneous romance of convenience, Max and Victoria must now play the part in front of Vadim. "
    "See you next time!"
)

CLOSING = ("anya", "Это мой Макс, мы теперь вместе!")
