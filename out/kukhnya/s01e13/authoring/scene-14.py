"""Authoring module for Kukhnya s01e13 scene 14."""
from pathlib import Path

ID = "kukhnya-s01e13-scene-14"
TITLE = "Честный разговор  (An Honest Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 14

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Настя",
    "kostya": "Костя",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = Path("sources/kukhnya/s01/e13.ru.dual.srt")
SOURCE_NOTE = "Cues 207-219 in Nastya's apartment."

INTRO = (
    "Visiting Nastya at her apartment, Kostya expects a romantic evening together. "
    "However, Nastya candidly confesses that she feels uncomfortable acting out of obligation or gratitude rather than genuine love, leading to a tender and respectful agreement. "
    "Let's listen to their conversation in Russian."
)

OPENER = (
    "Now let's examine how Nastya and Kostya navigate their personal feelings and boundaries line by line."
)

STORY = [
    ("anya", "Костя, подожди секунду, не спеши.",
     "Kostya, wait a second, do not rush.",
     [(207, "Костя, подожди.")], "Nastya pauses Kostya"),

    ("kostya", "Настя, что случилось, почему ты грустная?",
     "Nastya, what happened, why are you sad?",
     [], "Kostya asks kindly"),

    ("anya", "Сегодня у нас ничего не получится.",
     "Nothing will work out between us today.",
     [(208, "Наверное, сегодня у нас с тобой ничего не получится.")], "Nastya hesitates"),

    ("kostya", "Давай выпьем ещё немного сока!",
     "Let us drink a little more juice!",
     [(209, "Ну, давай еще выпьем.")], "Kostya suggests drinking"),

    ("anya", "Нет, Костя, дело совсем не в этом.",
     "No, Kostya, that is not the point.",
     [(210, "Нет, дело не в этом.")], "Nastya clarifies"),

    ("anya", "Я не хочу поступать не по любви.",
     "I do not want to act without love.",
     [(211, "я все это делаю не по любви")], "Nastya states her values"),

    ("anya", "Я просто очень благодарна за твою помощь.",
     "I am simply very grateful for your help.",
     [(212, "из благодарности, что ли, за то, что ты за меня вступился.")], "Nastya explains gratitude"),

    ("kostya", "Ты думаешь, что ты обязана мне?",
     "Do you think that you owe me?",
     [], "Kostya questions obligation"),

    ("anya", "Да, я чувствую себя нечестным человеком.",
     "Yes, I feel like a dishonest person.",
     [(214, "Получается, я как будто продажная женщина.")], "Nastya shares her guilt"),

    ("anya", "Давай сегодня просто спокойно поспим.",
     "Let us just sleep quietly tonight.",
     [(216, "Давай с тобой сегодня просто поспим, ладно?")], "Nastya proposes sleeping"),

    ("kostya", "Хорошо, давай сегодня просто поспим.",
     "All right, let us just sleep tonight.",
     [(217, "Давай поспим.")], "Kostya agrees gently"),

    ("anya", "Костя, ты правда понимаешь мои чувства?",
     "Kostya, do you really understand my feelings?",
     [(218, "Ты меня понимаешь?")], "Nastya seeks reassurance"),

    ("kostya", "Да, Настя, всё совершенно нормально.",
     "Yes, Nastya, everything is completely fine.",
     [(219, "Все нормально.")], "Kostya reassures her"),
]

WALK = [
    (0, None,
     "'Kostya, wait a second, do not rush.' Nastya asks him to pause the moment."),
    (1, None,
     "'Nastya, what happened, why are you sad?' Kostya inquires with gentle concern."),
    (2, None,
     "'Nothing will work out between us today.' She admits her emotional hesitation."),
    (3, None,
     "'Let us drink a little more juice!' Kostya suggests a refreshing beverage to relax."),
    (4, None,
     "'No, Kostya, that is not the point.' She clarifies that drinks cannot solve her dilemma."),
    (5, None,
     "'I do not want to act without love.' Nastya insists on emotional authenticity."),
    (6, None,
     "'I am simply very grateful for your help.' She reflects on her feeling of indebtedness."),
    (7, None,
     "'Do you think that you owe me?' Kostya reassures her that he expects nothing in return."),
    (8, None,
     "'Yes, I feel like a dishonest person.' Nastya shares her inner moral conflict with him."),
    (9, None,
     "'Let us just sleep quietly tonight.' She proposes an innocent, respectful rest."),
    (10, None,
     "'All right, let us just sleep tonight.' Kostya kindly agrees to her boundary."),
    (11, None,
     "'Kostya, do you really understand my feelings?' She seeks reassurance about his empathy."),
    (12, None,
     "'Yes, Nastya, everything is completely fine.' Kostya comforts her with genuine warmth."),
]

TRANSITION = (
    "Now let's listen to the honest conversation between Kostya and Nastya once more."
)

OUTRO = (
    "Finding mutual respect and emotional clarity, Kostya and Nastya spend a quiet, peaceful night together."
)

CLOSING = ("kostya", "Да, Настя, всё совершенно нормально.")
