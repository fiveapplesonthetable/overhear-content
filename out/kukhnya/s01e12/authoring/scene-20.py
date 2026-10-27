"""Scene 20 — Vika's Jealousy (s01e12)."""

ID = "kukhnya-s01e12-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 20
TITLE = "Ревность Вики  (Vika's Jealousy)"
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
    "anya": "Вика",
    "kostya": "Макс",
}

INTRO = (
    "In the restaurant corridor, Max tries to convince Victoria that Sasha is innocent, "
    "admitting he was just acting to make her jealous. Victoria angrily refuses to listen."
)

STORY = [
    ("anya", "Слушай сюда, я не собираюсь ничего выяснять.",
     "Listen here, I am not going to figure anything out.",
     [(271, "Слушай сюда, я не собираюсь с тобой ничего выяснять.")], "Vika stops Max angrily"),

    ("kostya", "Вика, Саша тут совершенно ни при чём.",
     "Vika, Sasha has absolutely nothing to do with this.",
     [(272, "Вик, Саша тут ни при чем")], "Max defends Sasha"),

    ("kostya", "Не надо её увольнять с этой работы.",
     "Do not fire her from this job.",
     [(272, "не надо ее увольнять.")], "Max pleads with Vika"),

    ("kostya", "Это я тебя специально доводил до гнева.",
     "I was intentionally driving you to anger.",
     [(273, "Это я, я тебя доводил")], "Max confesses his trick"),

    ("kostya", "Я изображал, будто мы с ней встречаемся.",
     "I pretended as if we were dating.",
     [(273, "изображал, как будто мы с ней встречаемся.")], "Max explains his fake romance"),

    ("anya", "Ну, у тебя это очень хорошо получилось.",
     "Well, you did a very good job with it.",
     [(274, "Ну, это у тебя хорошо получилось")], "Vika crosses her arms"),

    ("anya", "Особенно когда ты её за грудь хватал.",
     "Especially when you grabbed her by the chest.",
     [(274, "особенно сейчас, когда ты ее за грудь хватал.")], "Vika glares at Max"),

    ("kostya", "Поверь, это была просто глупая случайность!",
     "Believe me, it was just a stupid accident!",
     [(275, "Да это вообще случайность была.")], "Max tries to excuse himself"),

    ("anya", "А что ты за неё так заступаешься?",
     "And why are you sticking up for her so much?",
     [(275, "А что ты за нее заступаешься?")], "Vika raises her eyebrows skeptically"),

    ("kostya", "Я совершенно не заступаюсь за неё сейчас.",
     "I am not sticking up for her at all now.",
     [(276, "Я не заступаюсь")], "Max quickly denies it"),

    ("kostya", "Я просто не хочу, чтобы кто-то пострадал.",
     "I just do not want anyone to get hurt.",
     [(276, "просто не хочу, чтобы из твоей реальности пострадал тот и другой.")], "Max tries to be reasonable"),

    ("anya", "Из-за чего? Из-за того самого.",
     "Because of what? Because of that exact thing.",
     [(277, "Из-за чего? Из-за того.")], "Vika turns and walks away"),
]

OPENER = "Let's join Max and Vika in the hallway as they argue."

WALK = [
    (0, None,
     "'Listen here, I am not going to figure anything out.' Vika interrupts him sharply."),
    (1, None,
     "'Vika, Sasha has absolutely nothing to do with this.' Max steps in front of her to block her path."),
    (2, None,
     "'Do not fire her from this job.' He begs the manager to show some leniency."),
    (3, None,
     "'I was intentionally driving you to anger.' Max finally admits his childish manipulation."),
    (4, None,
     "'I pretended as if we were dating.' He reveals that the entire romance was a staged act."),
    (5, None,
     "'Well, you did a very good job with it.' Vika sarcastically commends his theatrical performance."),
    (6, None,
     "'Especially when you grabbed her by the chest.' She angrily recalls their inappropriate contact by the bar."),
    (7, None,
     "'Believe me, it was just a stupid accident!' Max frantically waves his hands in denial."),
    (8, None,
     "'And why are you sticking up for her so much?' Vika squints at him with deep suspicion."),
    (9, None,
     "'I am not sticking up for her at all now.' Max nervously backtracks his defense."),
    (10, None,
     "'I just do not want anyone to get hurt.' He tries to appeal to her sense of fairness."),
    (11, None,
     "'Because of what? Because of that exact thing.' Vika abruptly ends the conversation and storms off."),
]

TRANSITION = "Now let's listen to Max and Vika argue once again."

OUTRO = "Despite Max's confession, Vika remains furious and refuses to forgive his jealous games."

CLOSING = ("anya", "Из-за чего? Из-за того самого.")
