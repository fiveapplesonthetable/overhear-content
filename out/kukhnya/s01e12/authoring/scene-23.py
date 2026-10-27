"""Scene 23 — Changes for the Better (s01e12, 00:22:27–00:23:00)."""

ID = "kukhnya-s01e12-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 23
TITLE = "Перемены к лучшему  (Changes for the Better)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"

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
    "At the busy bar counter of Claude Monet, Max and Kostya observe the buzzing restaurant full of happy guests. "
    "Reflecting on life's unexpected twists, Max concludes that whatever surprises change brings, every turn ultimately leads to something better."
)

STORY = [
    ("kostya", "Макс, зал ресторана снова полон людей.",
     "Max, the dining hall is full of people again.",
     [], "Kostya wipes bar counter"),

    ("anya", "Да, наш вечер закончился очень удачно.",
     "Yes, our evening ended very successfully.",
     [], "Max watches dining room"),

    ("anya", "И всё-таки перемены всегда неожиданно происходят.",
     "Still, changes always happen unexpectedly.",
     [(286, "И все-таки, как бы мы ни относились к переменам, они происходят.")], "Max begins reflection"),

    ("kostya", "Ты прав, жизнь постоянно меняется вокруг нас.",
     "You are right, life constantly changes around us.",
     [], "Kostya nods in agreement"),

    ("anya", "Иногда мы получаем совсем не то.",
     "Sometimes we get something completely different.",
     [(287, "Иногда мы получаем совсем не то, что хотели.")], "Max ponders surprises"),

    ("anya", "Мы получаем не то, что хотели раньше.",
     "We get not what we wanted before.",
     [(287, "что хотели.")], "Max smiles thoughtfully"),

    ("kostya", "Но часто всё складывается даже лучше.",
     "But often everything turns out even better.",
     [], "Kostya serves a drink"),

    ("anya", "Порой мы убеждаемся, что были правы.",
     "Sometimes we realize that we were right.",
     [(288, "Порой убеждаемся в том, что были правы.")], "Max reflects on conviction"),

    ("kostya", "И наши старые друзья остаются рядом.",
     "And our old friends remain by our side.",
     [], "Kostya smiles at friendship"),

    ("anya", "А бывает, мы приходим в исходную точку.",
     "And sometimes we arrive back at the starting point.",
     [(289, "мы приходим в исходную точку.")], "Max gestures around kitchen"),

    ("kostya", "Главное — не терять веру и надежду.",
     "The main thing is not to lose faith and hope.",
     [], "Kostya looks ahead"),

    ("anya", "Главное — верить во все перемены.",
     "The main thing is to believe in all changes.",
     [(290, "Главное верить")], "Max shares life philosophy"),

    ("anya", "Все перемены в жизни ведут к лучшему!",
     "All changes in life lead to the better!",
     [(290, "все перемены в жизни к лучшему.")], "Max concludes episode"),
]

OPENER = "Let's join Max and Kostya at the bar counter as Max shares his closing reflections on life and change."

WALK = [
    (0, None,
     "'Max, the dining hall is full of people again.' Kostya looks out at the packed tables cheerfully."),
    (1, None,
     "'Yes, our evening ended very successfully.' Max takes in the vibrant atmosphere with relief."),
    (2, None,
     "'Still, changes always happen unexpectedly.' He begins his philosophical reflection on life."),
    (3, None,
     "'You are right, life constantly changes around us.' Kostya prepares glasses with a relaxed grin."),
    (4, None,
     "'Sometimes we get something completely different.' Max recalls how their plans took unexpected turns."),
    (5, None,
     "'We get not what we wanted before.' He considers how destiny rearranges our desires."),
    (6, None,
     "'But often everything turns out even better.' Kostya finds a silver lining in every surprise."),
    (7, None,
     "'Sometimes we realize that we were right.' Max affirms the quiet instincts that guide us."),
    (8, None,
     "'And our old friends remain by our side.' Kostya celebrates the bonds that endure through chaos."),
    (9, None,
     "'And sometimes we arrive back at the starting point.' Max marvels at how life comes full circle."),
    (10, None,
     "'The main thing is not to lose faith and hope.' Kostya looks forward to tomorrow with steady confidence."),
    (11, None,
     "'The main thing is to believe in all changes.' Max summarizes the wisdom of embracing the unknown."),
    (12, None,
     "'All changes in life lead to the better!' He closes the night with bright and unwavering optimism."),
]

TRANSITION = "Now let's listen to Max's thoughtful closing reflections on change once again."

OUTRO = "With the restaurant buzzing and hearts restored, Max concludes that every unforeseen change in life ultimately works for the best."

CLOSING = ("anya", "Все перемены в жизни ведут к лучшему!")
