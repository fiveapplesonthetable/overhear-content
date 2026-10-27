"""s01e11 scene 33: Пьяный командир (Eduard looks for Marina)."""

ID = "domashniy-arest-s01e11-scene-33"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 33
TITLE = "Пьяный командир  (Eduard Looks for Marina)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "eduard": "anja",
    "marina": "angelina",
}
LABELS = {
    "anya": "Клавдия",
    "eduard": "Эдуард",
    "marina": "Марина",
}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 990-1000. Drunk and heartbroken, Eduard arrives at the apartment looking for Marina."

INTRO = (
    "Inebriated and distraught over his fractured operation, FSB officer Eduard Valentinovich stumbles "
    "into the communal apartment corridor in search of Marina. Neighbor Klavdiya spitefully informs "
    "him that Marina is occupied with Arkady, sparking an emotional outburst."
)

STORY = [
    ("eduard", "Мариночка, открой скорее дверь!",
     "Marinochka, open the door quickly!",
     [(990, "Мариночка.")], "adapted cue"),

    ("anya", "Она сейчас сидит в туалете.",
     "She is in the bathroom right now.",
     [(991, "Она в туалете.")], "exact cue"),

    ("anya", "Она сидит там с Аркашкой.",
     "She is sitting there with Arkashka.",
     [(992, "С Аркашкой.")], "adapted cue"),

    ("eduard", "Ой, как это трогательно!",
     "Oh, how touching that is!",
     [(993, "Ой, как трогательно.")], "adapted cue"),

    ("marina", "Эдик, ты опять пьяный пришёл?",
     "Edik, did you come drunk again?",
     [(996, "ты пьяный?")], "adapted cue"),

    ("marina", "Иди скорее к себе домой.",
     "Go to your home right away.",
     [(996, "Иди домой")], "adapted cue"),

    ("eduard", "Я же долго воспитывал тебя!",
     "I raised you for a long time!",
     [(997, "воспитывал ее.")], "adapted cue"),

    ("eduard", "Я обучал тебя буквально всему.",
     "I taught you literally everything.",
     [(998, "Обучал, так сказать, всему.")], "adapted cue"),

    ("marina", "Перестань кричать на весь коридор.",
     "Stop shouting across the whole hallway.",
     [], "Marina's rebuke"),

    ("eduard", "А ты оказалась неблагодарной женщиной!",
     "And you turned out to be an ungrateful woman!",
     [(999, "А она оказалась")], "polite adaptation of cue"),

    ("marina", "Я больше не буду работать на вас.",
     "I will not work for you anymore.",
     [], "Marina's declaration"),

    ("eduard", "Ты разбила моё верное сердце!",
     "You broke my faithful heart!",
     [], "Eduard's lament"),

    ("anya", "Хватит шуметь, иди проспись, командир.",
     "Enough making noise, go sleep it off, commander.",
     [], "Klavdiya's intervention"),

    ("eduard", "Я всё равно не забуду эту обиду.",
     "I will not forget this insult anyway.",
     [], "Eduard's parting grudge"),
]

OPENER = "Let's explore the pathetic scene as the drunken commander confronts Marina."

WALK = [
    (0, None,
     "'Marinochka, open the door quickly!' Eduard calls out affectionately using an intimate diminutive."),
    (1, None,
     "'She is in the bathroom right now.' Klavdiya curtly points out Marina's current location."),
    (2, None,
     "'She is sitting there with Arkashka.' Klavdiya adds a malicious detail about Arkady's presence."),
    (3, None,
     "'Oh, how touching that is!' Eduard's sarcastic exclamation barely masks his deep wounded jealousy."),
    (4, None,
     "'Edik, did you come drunk again?' Marina reproaches him for arriving in a state of drunkenness."),
    (5, None,
     "'Go to your home right away.' Marina tries to turn him away before a major scene develops."),
    (6, None,
     "'I raised you for a long time!' Eduard dramatically exaggerates his paternal role in her life."),
    (7, None,
     "'I taught you literally everything.' The officer claims credit for shaping her personality."),
    (8, None,
     "'Stop shouting across the whole hallway.' Marina urges him to lower his voice in the communal house."),
    (9, None,
     "'And you turned out to be an ungrateful woman!' Eduard accuses his former operative of betrayal."),
    (10, None,
     "'I will not work for you anymore.' Marina firmly severs all remaining ties with the security agency."),
    (11, None,
     "'You broke my faithful heart!' A melodramatic expression revealing his personal affection."),
    (12, None,
     "'Enough making noise, go sleep it off, commander.' Klavdiya bluntly advises him to sober up."),
    (13, None,
     "'I will not forget this insult anyway.' Eduard vows to hold on to his bitter resentment."),
]

TRANSITION = "Now let's listen to the drunken confrontation in the apartment corridor once more."

OUTRO = "Eduard staggers away humiliated, while Marina stands firm in her newfound independence."

CLOSING = ("eduard", "Я всё равно не забуду эту обиду.")
