"""s01e13 scene 16: Утро после клуба (The Morning After the Club)."""

ID = "kukhnya-s01e13-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 16
TITLE = "Утро после клуба  (The Morning After the Club)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 221-239. Victoria wakes up in Max's bed horrified, but Max reminds her that she begged him to pick her up."

INTRO = (
    "Waking up disoriented in an unfamiliar bedroom, Victoria is horrified to discover that she has spent the night in Max's apartment. "
    "When she angrily accuses him of taking advantage of her, Max playfully reminds her of her desperate late-night phone call begging for a rescue. "
    "Let's listen to their morning argument in Russian."
)

STORY = [
    ("anya", "Где я нахожусь? Что это такое?", "Where am I? What is this?",
     [(221, "где я?")], "adapted"),
    ("anya", "Ты опять затащил меня в постель?", "Did you drag me into bed again?",
     [(222, "Ты что, меня опять в постель затащил?")], "adapted"),
    ("max", "Конечно, связал и принёс сюда сам.", "Of course, tied you up and brought you here myself.",
     [(223, "Насильно связал и затащил")], "adapted"),
    ("anya", "Не смейся надо мной, говори правду.", "Do not laugh at me, tell the truth.",
     [], "new"),
    ("max", "Ты сама позвонила мне ночью из клуба.", "You called me yourself at night from the club.",
     [(224, "Ты что, не помнишь, что мне сама позвонила?")], "adapted"),
    ("anya", "Я не могла сделать такую глупость.", "I could not do such a foolish thing.",
     [], "new"),
    ("max", "Ты плакала в трубку в три часа.", "You were crying into the phone at three o'clock.",
     [(226, "Как я могу спать 3 часа ночи?")], "adapted"),
    ("anya", "Что я тебе тогда говорила, Макс?", "What was I telling you then, Max?",
     [], "new"),
    ("max", "Ты очень просила забрать тебя домой.", "You were begging me to take you home.",
     [(234, "забери меня, пожалуйста")], "adapted"),
    ("anya", "Ты просто воспользовался моей минутной слабостью.", "You simply took advantage of my momentary weakness.",
     [(236, "Ты воспользовался тем, что я была пьяна")], "adapted"),
    ("max", "Я просто спас тебя от неприятностей.", "I simply saved you from trouble.",
     [], "new"),
    ("anya", "Мне нужно срочно уйти отсюда, Макс.", "I need to leave here urgently, Max.",
     [], "new"),
    ("max", "Твоя одежда лежит на том стуле.", "Your clothes are lying on that chair.",
     [], "new"),
]

OPENER = "Let's explore how Victoria reacts upon waking up in Max's apartment and how Max defends his actions."

WALK = [
    (1, None,
     "'Did you drag me into bed again?' A sharp accusatory question expressing indignation and shock upon waking up."),
    (4, None,
     "'You called me yourself at night from the club.' A defensive assertion clarifying who actually initiated the late-night contact."),
    (8, None,
     "'You were begging me to take you home.' An explanation revealing an earnest plea for rescue during the night."),
    (9, None,
     "'You simply took advantage of my momentary weakness.' A resentful claim deflecting personal responsibility for an embarrassing situation."),
]

TRANSITION = "Now, let's hear Victoria and Max confront each other once more."

OUTRO = (
    "Now you know how to talk about morning-after confusion, recall late-night phone calls, and express defensive reactions in Russian. "
    "Listen for these interpersonal phrases in the next scene."
)

CLOSING = ("anya", "Никто в ресторане не должен знать.")
