"""s01e02 scene 20: Разговор в кабинете шефа (Talk in the Chef's Office)."""

ID = "kukhnya-s01e02-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 20
TITLE = "Разговор в кабинете шефа  (Talk in the Chef's Office)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Лёва",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = (
    "Furious about his missing fish knife, Chef Viktor Barinov calls his sous-chef Lyova into his private office. "
    "He demands an immediate explanation for the chaos in the kitchen and issues a dire threat to the whole team. "
    "Listen to their conversation in Russian first, and then we will examine every sentence in detail."
)

STORY = [
    ("chef", "Лёва, зайди ко мне в кабинет!",
     "Lyova, come to my office!",
     [(230, "Лева, зайди ко мне")], "verbatim summons"),
    ("anya", "Да, шеф, я уже здесь.",
     "Yes, chef, I am already here.",
     [(230, "Да, шеф")], "prompt reply"),
    ("chef", "Где мой любимый рыбий нож?",
     "Where is my favorite fish knife?",
     [(228, "Нож нашли")], "adapted inquiry"),
    ("anya", "Мы везде ищем его, шеф.",
     "We are looking for it everywhere, chef.",
     [(238, "Везде смотрели")], "verbatim context"),
    ("chef", "Ты су-шеф или кто такой?",
     "Are you a sous-chef or who?",
     [], "demanding authority"),
    ("anya", "Я слежу за порядком на кухне.",
     "I maintain order in the kitchen.",
     [], "stating responsibility"),
    ("chef", "Ты очень плохо следишь за кухней!",
     "You keep an eye on the kitchen very poorly!",
     [], "sharp rebuke"),
    ("anya", "Все повара сейчас очень заняты поисками.",
     "All the cooks are very busy with the search right now.",
     [], "explaining efforts"),
    ("chef", "Без этого ножа ресторан не работает!",
     "Without this knife, the restaurant does not function!",
     [], "importance of tool"),
    ("anya", "Мы проверили все столы и полки.",
     "We checked all tables and shelves.",
     [], "search details"),
    ("chef", "Если нож не найдётся, всех уволю!",
     "If the knife is not found, I will fire everyone!",
     [], "dire ultimatum"),
    ("anya", "Шеф, мы обязательно найдём пропажу.",
     "Chef, we will certainly find what went missing.",
     [], "reassuring promise"),
    ("chef", "Иди и найди его прямо сейчас!",
     "Go and find it right now!",
     [], "final order"),
    ("anya", "Слушаюсь, шеф! Я найду нож.",
     "Understood, chef! I will find the knife.",
     [(230, "Да, шеф")], "compliance"),
]

OPENER = "Now let us go through the dialogue line by line to understand every expression."

WALK = [
    (0, "Лёва, зайди ко мне в кабинет!",
     "'Lyova, come to my office!' The chef summons his sous-chef with a direct imperative command."),
    (1, "Да, шеф, я уже здесь.",
     "'Yes, chef, I am already here.' Lyova reports promptly to avoid aggravating his fiery boss."),
    (2, "Где мой любимый рыбий нож?",
     "'Where is my favorite fish knife?' The question uses descriptive adjectives for the missing utensil."),
    (3, "Мы везде ищем его, шеф.",
     "'We are looking for it everywhere, chef.' The adverb of place indicates a widespread search across the kitchen."),
    (4, "Ты су-шеф или кто такой?",
     "'Are you a sous-chef or who?' The chef angrily questions Lyova's competence and kitchen leadership."),
    (5, "Я слежу за порядком на кухне.",
     "'I maintain order in the kitchen.' The reflexive construction with instrumental denotes monitoring and control."),
    (6, "Ты очень плохо следишь за кухней!",
     "'You keep an eye on the kitchen very poorly!' The chef lashes out with a sharp evaluative adverb."),
    (7, "Все повара сейчас очень заняты поисками.",
     "'All the cooks are very busy with the search right now.' Short adjectives with instrumental nouns explain the activity."),
    (8, "Без этого ножа ресторан не работает!",
     "'Without this knife, the restaurant does not function!' The preposition governs the genitive singular."),
    (9, "Мы проверили все столы и полки.",
     "'We checked all tables and shelves.' The past perfective verb indicates completed inspections."),
    (10, "Если нож не найдётся, всех уволю!",
     "'If the knife is not found, I will fire everyone!' A harsh conditional ultimatum delivered in the future tense."),
    (11, "Шеф, мы обязательно найдём пропажу.",
     "'Chef, we will certainly find what went missing.' A reassuring promise with the perfective future."),
    (12, "Иди и найди его прямо сейчас!",
     "'Go and find it right now!' Two coordinated imperative verbs emphasizing urgent action."),
    (13, "Слушаюсь, шеф!",
     "'Understood, chef!' A military-style response commonly used in professional restaurant brigades."),
    (13, "Я найду нож.",
     "'I will find the knife.' Lyova affirms his determination to resolve the crisis."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Lyova leaves Chef Barinov's office feeling the full weight of the crisis on his shoulders. "
    "Meanwhile, out in the kitchen prep area, someone has made an unexpected discovery. See you next time!"
)

CLOSING = ("anya", "Мы найдём этот важный нож.")
