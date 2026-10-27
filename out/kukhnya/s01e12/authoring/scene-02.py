ID = "kukhnya-s01e12-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 2
TITLE = "Фальшивая боль  (Fake Pain)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 2-15. Max pretends to have terrible stomach pain to gain Victoria's sympathy, "
    "only to surprise her with cinema tickets."
)

INTRO = (
    "In the restaurant corridor, Max suddenly grabs his right side and groans in pain. "
    "When a concerned Victoria rushes over to help him, he miraculously recovers and reveals his true intentions. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ай! Как мне больно в животе!",
     "Ouch! How it hurts me in the stomach!",
     [(8, "Блин, что это?"), (12, "Ой, что это?")], "adapted"),
    ("vika", "Макс, что такое? Тебе очень больно?",
     "Max, what is it? Does it hurt you a lot?",
     [(9, "Что такое? Больно так?")], "adapted"),
    ("anya", "Я не знаю, что это такое.",
     "I do not know what this is.",
     [(10, "Не знаю, что это.")], "adapted"),
    ("vika", "Ой, с правой стороны это очень плохо!",
     "Oh, on the right side this is very bad!",
     [(11, "Боже мой.")], "adapted"),
    ("anya", "Боже мой, как мне сейчас больно.",
     "My god, how much it hurts me now.",
     [], "new"),
    ("vika", "Давай я быстро вызову тебе врача.",
     "Let me quickly call a doctor for you.",
     [], "new"),
    ("anya", "Нет, серьёзно, не надо вызывать врачей.",
     "No, seriously, do not call doctors.",
     [(10, "Нет, всё нормально, всё нормально.")], "adapted"),
    ("vika", "Почему? Тебе же нужна срочная помощь.",
     "Why? You need urgent help after all.",
     [], "new"),
    ("anya", "Смотри, вот два билета в кино.",
     "Look, here are two tickets to the cinema.",
     [(13, "Билетики. Пойдем в кино, а?")], "adapted"),
    ("vika", "Ну ты и придурок, честное слово!",
     "Well you are a jerk, honestly!",
     [(14, "Дебил.")], "adapted"),
    ("anya", "Пойдём в кино сегодня вечером, а?",
     "Shall we go to the cinema tonight, eh?",
     [(13, "Пойдем в кино, а?")], "adapted"),
    ("vika", "Ты настоящий идиот, я никуда не пойду!",
     "You are a real idiot, I will not go anywhere!",
     [(14, "Дебил.")], "adapted"),
    ("anya", "Ладно, тогда я пойду в кино один.",
     "Alright, then I will go to the cinema alone.",
     [], "new"),
]

OPENER = "Now let's examine this tricky conversation in the corridor line by line."

WALK = [
    (0, None,
     "'Ouch! How it hurts me in the stomach!' -- Max suddenly doubles over in intense pain."),
    (1, None,
     "'Max, what is it? Does it hurt you a lot?' -- Victoria rushes to him with genuine concern."),
    (2, None,
     "'I do not know what this is.' -- He pretends to be confused by the sudden ailment."),
    (3, None,
     "'Oh, on the right side this is very bad!' -- The manager worries it might be appendicitis."),
    (4, None,
     "'My god, how much it hurts me now.' -- He continues to dramatically fake his suffering."),
    (5, None,
     "'Let me quickly call a doctor for you.' -- Victoria offers to summon medical assistance immediately."),
    (6, None,
     "'No, seriously, do not call doctors.' -- Max quickly stops her from calling an ambulance."),
    (7, None,
     "'Why? You need urgent help after all.' -- She insists that he needs professional care."),
    (8, None,
     "'Look, here are two tickets to the cinema.' -- Dropping the act, he presents his romantic surprise."),
    (9, None,
     "'Well you are a jerk, honestly!' -- Relieved but furious, Victoria insults his childish prank."),
    (10, None,
     "'Shall we go to the cinema tonight, eh?' -- He playfully asks her out on a date."),
    (11, None,
     "'You are a real idiot, I will not go anywhere!' -- Still angry about the trick, she flatly rejects him."),
    (12, None,
     "'Alright, then I will go to the cinema alone.' -- Max accepts his defeat with a sigh."),
]

TRANSITION = "Now let's listen to the corridor conversation again without interruption."
OUTRO = (
    "Furious at being tricked into worrying about his health, Victoria storms off, "
    "leaving Max standing alone with his cinema tickets."
)
CLOSING = ("anya", "Ладно, тогда я пойду в кино один.")
