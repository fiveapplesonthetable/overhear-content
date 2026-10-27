"""Scene 20 — A Place to Come Home To (s01e07, 00:23:45–00:24:05)."""

ID = "kukhnya-s01e07-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 20
TITLE = "Куда вернуться  (A Place to Come Home To)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Макс",
    "kostya": "Костя",
}

INTRO = (
    "Arriving at Kostya's apartment with his bags, Max finds a warm welcome and a place to stay. "
    "Surrounded by the comfort of friendship, Max reflects on the supreme importance of having a home to return to."
)

STORY = [
    ("kostya", "Заходи, Макс, чувствуй себя как дома.",
     "Come in, Max, make yourself at home.",
     [], "Kostya welcomes Max"),

    ("anya", "Спасибо, Костя, ты спас меня сегодня.",
     "Thank you, Kostya, you saved me today.",
     [], "Max is grateful"),

    ("kostya", "Мы друзья, а друзья всегда помогают друг другу.",
     "We are friends, and friends always help each other.",
     [], "Kostya reaffirms bond"),

    ("anya", "Я сегодня понял одну очень важную вещь.",
     "Today I realized one very important thing.",
     [(353, "Я понял одну важную вещь.")], "Max begins reflection"),

    ("kostya", "Какую вещь ты понял, философ?",
     "What thing did you realize, philosopher?",
     [], "Kostya asks smiling"),

    ("anya", "Что бы ни случилось с тобой днём...",
     "Whatever might happen to you during the day...",
     [(354, "Что бы с тобой не случилось днем,")], "Max reflects on day"),

    ("anya", "Главное — чтобы вечером было куда вернуться.",
     "The main thing is to have somewhere to return in the evening.",
     [(354, "главное, чтобы вечером было куда вернуться.")], "Max notes home"),

    ("anya", "Вернуться туда, где тебе искренне рады.",
     "Return to where you are sincerely welcomed.",
     [(355, "Вернуться туда, где тебе рады.")], "Max reflects on warmth"),

    ("kostya", "Это точно, в пустой квартире тоскливо.",
     "That is true, it is dreary in an empty apartment.",
     [], "Kostya agrees"),

    ("anya", "Ведь нет ничего хуже страшного одиночества.",
     "After all there is nothing worse than terrible loneliness.",
     [(356, "Потому что нет ничего хуже одиночества.")], "Max reflects on loneliness"),

    ("kostya", "Вдвоём нам точно будет веселее жить!",
     "Together we will definitely have more fun living!",
     [], "Kostya cheers up"),

    ("anya", "Теперь мы настоящие соседи и друзья.",
     "Now we are real roommates and friends.",
     [], "Max smiles"),

    ("kostya", "Давай пить чай и отдыхать.",
     "Let us drink tea and rest.",
     [], "Kostya offers tea"),

    ("anya", "Хорошо, когда есть настоящий дом!",
     "It is good when you have a real home!",
     [], "Max concludes happily"),
]

OPENER = "Let's explore Max's arrival at Kostya's apartment and his poignant reflections on home and friendship."

WALK = [
    (0, None,
     "'Come in, Max, make yourself at home.' Kostya warmly invites the stranded cook into his home."),
    (1, None,
     "'Thank you, Kostya, you saved me today.' Max is deeply grateful for the late-night shelter."),
    (2, None,
     "'We are friends, and friends always help each other.' The generous bartender smiles with kindness."),
    (3, None,
     "'Today I realized one very important thing.' Max shares his deep revelation about life and home."),
    (4, None,
     "'What thing did you realize, philosopher?' Kostya teases the thoughtful cook with a warm smile."),
    (5, None,
     "'Whatever might happen to you during the day...' Max begins his closing reflection on the day."),
    (6, None,
     "'The main thing is to have somewhere to return in the evening.' Max values having a safe haven."),
    (7, None,
     "'Return to where you are sincerely welcomed.' A true home is where loved ones greet you."),
    (8, None,
     "'That is true, it is dreary in an empty apartment.' Kostya understands the pain of living alone."),
    (9, None,
     "'After all there is nothing worse than terrible loneliness.' Max reflects on the ache of being solitary in the world."),
    (10, None,
     "'Together we will definitely have more fun living!' Kostya embraces having a lively roommate in the flat."),
    (11, None,
     "'Now we are real roommates and friends.' Max celebrates the unexpected bond that formed between them."),
    (12, None,
     "'Let us drink tea and rest.' Kostya invites Max to relax in the warm kitchen."),
    (13, None,
     "'It is good when you have a real home!' Max finishes his reflection feeling blessed and protected by friendship."),
]

TRANSITION = "Now let's listen to the heartwarming conversation between the new roommates once more."

OUTRO = "Safe from the cold street and surrounded by friendship, Max settles happily into his new home."

CLOSING = ("anya", "Хорошо, когда есть настоящий дом!")
