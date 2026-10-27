"""Scene 39 — Lev Egorych (s01e11, 01:10:43–01:10:53)."""

ID = "domashniy-arest-s01e11-scene-39"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 39
TITLE = "Лев Егорыч  (Lev Egorych)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "lev": "anja",
}

LABELS = {
    "anya": "Вика",
    "lev": "Лев",
}

INTRO = (
    "In his private residence, Governor Lev Yegorych relaxes with young Vika, who playfully flatters "
    "him while he encourages her to drop formal titles and address him simply by his first name."
)

STORY = [
    ("anya", "Какие же у вас взрослые сыновья!",
     "What grown sons you have!",
     [(1152, "Какие же у вас сынки,")], "compliment on sons"),

    ("anya", "Они очень похожи на вас, Лев Егорыч.",
     "They look very much like you, Lev Egorych.",
     [(1152, "Лев Егорыч?")], "addressing formally"),

    ("lev", "Просто Лев, малышка, без отчества.",
     "Just Lev, sweetheart, without the patronymic.",
     [(1153, "Просто Лев, малышка.")], "dropping patronymic"),

    ("lev", "Зови меня просто: Лёва.",
     "Call me simply: Lyova.",
     [(1154, "Лёва.")], "asking for nickname"),

    ("anya", "Хорошо, Лёва, как скажешь.",
     "All right, Lyova, as you say.",
     [], "Vika agrees playfully"),

    ("anya", "Мне очень нравится твоё имя.",
     "I like your name very much.",
     [], "flattery"),

    ("lev", "Ты сегодня выглядишь просто прекрасно.",
     "You look simply wonderful today.",
     [], "Lev compliments her"),

    ("anya", "Спасибо большое за твою доброту.",
     "Thank you very much for your kindness.",
     [], "Vika thanks him"),

    ("lev", "Я люблю дарить тебе радость.",
     "I love giving you joy.",
     [], "Lev's affection"),

    ("anya", "Ты всегда делаешь мне подарки.",
     "You always give me gifts.",
     [], "gifts acknowledged"),

    ("lev", "Для тебя мне ничего не жалко.",
     "For you I spare nothing.",
     [], "generosity"),

    ("anya", "Тогда налей мне ещё бокал вина.",
     "Then pour me another glass of wine.",
     [], "asking for wine"),

    ("lev", "С большим удовольствием, дорогая моя!",
     "With great pleasure, my dear!",
     [], "pouring wine"),

    ("anya", "Давай выпьем за наше общее счастье!",
     "Let us drink to our mutual happiness!",
     [], "toast to happiness"),
]

OPENER = "Let's explore the relaxed and affectionate conversation between Lev Yegorych and Vika."

WALK = [
    (0, None,
     "'What grown sons you have!' Vika compliments the governor on his family."),
    (1, None,
     "'They look very much like you, Lev Egorych.' Vika addresses him formally by his patronymic."),
    (2, None,
     "'Just Lev, sweetheart, without the patronymic.' Lev asks her to drop formal etiquette in private."),
    (3, None,
     "'Call me simply: Lyova.' Lev introduces his affectionate diminutive name with a warm smile."),
    (4, None,
     "'All right, Lyova, as you say.' Vika agrees playfully to call him by his nickname."),
    (5, None,
     "'I like your name very much.' Vika flatters him with charming compliments."),
    (6, None,
     "'You look simply wonderful today.' Lev compliments her charming appearance."),
    (7, None,
     "'Thank you very much for your kindness.' Vika thanks him warmly for his hospitality."),
    (8, None,
     "'I love giving you joy.' Lev expresses his affection for his young companion."),
    (9, None,
     "'You always give me gifts.' Vika acknowledges his continuous generosity."),
    (10, None,
     "'For you I spare nothing.' Lev assures her that he is generous without limits."),
    (11, None,
     "'Then pour me another glass of wine.' Vika asks for another drink to celebrate."),
    (12, None,
     "'With great pleasure, my dear!' Lev pours more wine for his young companion."),
    (13, None,
     "'Let us drink to our mutual happiness!' Vika raises a toast to their relationship."),
]

TRANSITION = "Now let's listen to the quiet, intimate dialogue between Vika and Lev Yegorych once more."

OUTRO = "Comfortable in his lavish surroundings, Governor Lev Yegorych enjoys a tranquil evening away from politics."

CLOSING = ("lev", "Зови меня просто: Лёва.")
