"""Authoring module for Kukhnya s01e11 scene 08."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-08"
TITLE = "Потерянный телефон  (The Lost Phone)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 8

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "guest": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Костя",
    "guest": "Гость",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 100-111 at the bar counter."

INTRO = (
    "At the Claude Monet bar counter, an exhausted and hungover visitor approaches bartender Kostya. "
    "Relieved to recover the mobile phone he left behind the night before, he unburdens his romantic sorrows to the sympathetic bartender. "
    "Let's listen to their friendly bar exchange in Russian."
)

OPENER = (
    "Now let's examine how Kostya assists the forgetful guest at the bar line by line."
)

STORY = [
    ("guest", "Привет! Как твои дела, бармен?",
     "Hello! How are things, bartender?",
     [(100, "Здрасте.")], "Guest greets Kostya"),

    ("anya", "Здравствуйте! Как вы себя сегодня чувствуете?",
     "Hello! How are you feeling today?",
     [(101, "Как себя чувствуете?")], "Kostya asks politely"),

    ("guest", "Эх, сегодня мне хуже, чем вчера.",
     "Ugh, today I feel worse than yesterday.",
     [(101, "Эх, хуже, чем вчера.")], "Guest groans in hangover"),

    ("guest", "Ты случайно не находил мой телефон?",
     "Did you happen to find my phone?",
     [(102, "Ты мой телефон не находил?")], "Guest inquires about phone"),

    ("anya", "Да, я нашёл его возле стойки.",
     "Yes, I found it near the counter.",
     [(103, "Находил.")], "Kostya returns phone"),

    ("guest", "Огромное спасибо за помощь, друг!",
     "Huge thanks for the help, friend!",
     [(103, "О, спасибо.")], "Guest is grateful"),

    ("guest", "Скажи честно, моя девушка не звонила?",
     "Tell me honestly, did my girlfriend not call?",
     [(104, "Она не звонила?")], "Guest asks about girlfriend"),

    ("anya", "Нет, сюда пока никто не звонил.",
     "No, no one has called here yet.",
     [(104, "Нет.")], "Kostya answers truthfully"),

    ("guest", "Она ещё не вернулась из Саратова.",
     "She has not returned from Saratov yet.",
     [(105, "Наверное, еще не вернулась из Саратова.")], "Guest explains girlfriend's trip"),

    ("anya", "Вы вчера долго говорили про неё.",
     "Yesterday you spoke about her for a long time.",
     [(107, "Ну, вы же мне вчера рассказывали.")], "Kostya remembers the conversation"),

    ("guest", "Да, память медленно возвращается ко мне.",
     "Yes, my memory is slowly returning to me.",
     [(108, "Да.")], "Guest recalls the evening"),

    ("anya", "Вот вам напиток за счёт заведения.",
     "Here is a drink for you on the house.",
     [(110, "За счет заведения.")], "Kostya serves a drink"),

    ("guest", "Спасибо тебе за доброту, дружище!",
     "Thank you for your kindness, buddy!",
     [(111, "Спасибо тебе, дружище.")], "Guest thanks Kostya warmly"),
]

WALK = [
    (0, None,
     "'Hello! How are things, bartender?' The tired customer greets Kostya at the counter."),
    (1, None,
     "'Hello! How are you feeling today?' Kostya asks with friendly concern."),
    (2, None,
     "'Ugh, today I feel worse than yesterday.' The man admits his painful hangover."),
    (3, None,
     "'Did you happen to find my phone?' He asks hopefully about the lost device."),
    (4, None,
     "'Yes, I found it near the counter.' Kostya retrieves the forgotten telephone."),
    (5, None,
     "'Huge thanks for the help, friend!' The customer sighs in immense relief."),
    (6, None,
     "'Tell me honestly, did my girlfriend not call?' He wonders if his partner reached out."),
    (7, None,
     "'No, no one has called here yet.' Kostya delivers the disappointing news."),
    (8, None,
     "'She has not returned from Saratov yet.' The guest explains where she traveled."),
    (9, None,
     "'Yesterday you spoke about her for a long time.' Kostya recalls their conversation of the previous night."),
    (10, None,
     "'Yes, my memory is slowly returning to me.' The guest starts piecing the night together."),
    (11, None,
     "'Here is a drink for you on the house.' Kostya kindly pours a restorative beverage."),
    (12, None,
     "'Thank you for your kindness, buddy!' The guest expresses his heartfelt gratitude."),
]

TRANSITION = (
    "Now let's listen to the warm conversation between Kostya and the visitor once more."
)

OUTRO = (
    "Comforted by the bartender's hospitality, the customer rests at the bar before facing the rest of his day."
)

CLOSING = ("guest", "Спасибо тебе за доброту, дружище!")
