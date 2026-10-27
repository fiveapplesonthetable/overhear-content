"""Authoring module for Kukhnya s01e09 scene 05."""
from pathlib import Path

ID = "kukhnya-s01e09-scene-05"
TITLE = "Прятки с дядей Лёвой  (Hide and Seek with Uncle Lyova)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 5

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "lyova": "angelina",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Алиса",
    "chef": "Шеф",
    "lyova": "Лёва",
}

SOURCE_NAME = "Кухня s01e09"
SOURCE_FILE = Path("sources/kukhnya/s01/e09.ru.dual.srt")
SOURCE_NOTE = "Cues 93-106 in the restaurant kitchen and backrooms."

INTRO = (
    "In this scene in the restaurant, Chef Viktor Barinov entrusts his lively daughter Alisa to sous-chef Lyova. "
    "Alisa quickly takes control of the situation and convinces Lyova to play hide-and-seek. "
    "Listen to their amusing dialogue in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this entertaining exchange sentence by sentence."
)

STORY = [
    ("chef", "Лёва, сиди здесь и смотри за Алисой.", "Lyova, sit here and watch over Alisa.", [(93, "Сиди здесь."), (94, "Смотри за Алисой.")], "adapted: combined with name"),
    ("chef", "Глаз с нее не спускай.", "Do not take your eyes off her.", [(95, "Глаз с нее не спускай.")], "verbatim"),
    ("chef", "И не давай шоколад, у нее аллергия.", "And do not give her chocolate, she has an allergy.", [(96, "И не давай шоколад. У нее аллергия.")], "adapted: comma splice"),
    ("anya", "Дядя Лёва, давай играть!", "Uncle Lyova, let us play!", [(97, "Давай играть.")], "adapted: added name"),
    ("lyova", "Может, лучше просто посидим?", "Maybe we could just sit here instead?", [(98, "Может, лучше просто посидим?")], "verbatim"),
    ("anya", "Я папе скажу, он тебя уволит!", "I will tell Dad, he will fire you!", [(99, "Я папе скажу. Он тебя уволит.")], "adapted: combined"),
    ("lyova", "Хорошо, во что будем играть?", "All right, what should we play?", [(101, "Во что будем играть?")], "adapted: added agreement"),
    ("anya", "Давай в прятки!", "Let us play hide and seek!", [], "new"),
    ("lyova", "А кто будет прятаться?", "And who will hide?", [(103, "А кто будет прятаться?")], "adapted: shortened"),
    ("anya", "Конечно, я буду прятаться!", "Of course, I will hide!", [(104, "Конечно, я.")], "adapted: completed"),
    ("anya", "Тебя такого длинного нигде не спрячешь.", "You are so tall, you cannot be hidden anywhere.", [(104, "Тебя такого длинного нигде не спрячешь.")], "verbatim"),
    ("anya", "Закрывай глаза, считай до ста.", "Close your eyes, count to a hundred.", [(105, "Закрывай глаза, считай до ста.")], "verbatim"),
    ("lyova", "Раз, два, три, четыре...", "One, two, three, four...", [(106, "Раз, два.")], "adapted: continued counting"),
    ("anya", "Считай медленно, я иду прятаться!", "Count slowly, I am going to hide!", [], "new"),
]

WALK = [
    (0, None, "'Lyova, sit here and watch over Alisa.' Viktor gives his sous-chef a direct command."),
    (1, None, "'Do not take your eyes off her.' Viktor reinforces his strict instruction with a firm tone."),
    (2, None, "'And do not give her chocolate, she has an allergy.' Viktor warns him about her dietary restriction."),
    (3, None, "'Uncle Lyova, let us play!' Alisa demands his attention with energetic excitement."),
    (4, None, "'Maybe we could just sit here instead?' Lyova suggests a quiet alternative with gentle hesitation."),
    (5, None, "'I will tell Dad, he will fire you!' Alisa issues a cheeky threat with complete confidence."),
    (6, None, "'All right, what should we play?' Lyova gives in to her demand with a nervous sigh."),
    (7, None, "'Let us play hide and seek!' Alisa proposes a classic game with eager delight."),
    (8, None, "'And who will hide?' Lyova asks for clarification about the rules of their game."),
    (9, None, "'Of course, I will hide!' Alisa announces her role with immediate enthusiasm."),
    (10, None, "'You are so tall, you cannot be hidden anywhere.' Alisa points out his imposing height with blunt honesty."),
    (11, None, "'Close your eyes, count to a hundred.' Alisa sets the countdown before running away."),
    (12, None, "'One, two, three, four...' Lyova begins counting out loud with an obedient voice."),
    (13, None, "'Count slowly, I am going to hide!' Alisa calls out her final rule as she slips away."),
]

TRANSITION = (
    "Now, let us listen to the complete scene once more to consolidate your comprehension."
)

OUTRO = (
    "A hilarious situation where little Alisa easily outsmarts the tall sous-chef."
)

CLOSING = ("lyova", "Я уже считаю до ста!")
