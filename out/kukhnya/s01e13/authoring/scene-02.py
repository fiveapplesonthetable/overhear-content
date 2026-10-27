"""s01e13 scene 02: Чужая машина (Someone Else's Car)."""

ID = "kukhnya-s01e13-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 2
TITLE = "Чужая машина  (Someone Else's Car)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "elena": "anja",
}
LABELS = {
    "anya": "Шеф",
    "elena": "Елена",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

INTRO = (
    "In the parking courtyard behind Claude Monet, Chef Viktor arrives to find an unfamiliar car parked in his favorite spot. "
    "When he confronts the driver, she turns out to be Elena, the formidable chef of a rival restaurant, who refuses to budge. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Кто поставил сюда эту старую машину?",
     "Who parked this old car here?",
     [(26, "Какой кретин поставил сюда машину?")], "complaining about spot"),
    ("elena", "Здравствуйте. Я поставила свою машину.",
     "Hello. I parked my car.",
     [], "greeting coolly"),
    ("anya", "Женщина, уберите автомобиль с моего места.",
     "Woman, move the automobile from my spot.",
     [(30, "Я говорю, машину с моего места уберите.")], "demanding removal"),
    ("elena", "Где написано, что это ваше место?",
     "Where does it say this is your spot?",
     [(32, "Где это написано, что это место ваше?")], "challenging ownership"),
    ("anya", "Здесь висит знак с предупреждением.",
     "A warning sign is hanging here.",
     [(33, "Ну вот же, огромными буквами написано.")], "pointing at sign"),
    ("elena", "Там написано только про сосульки.",
     "It only says about icicles there.",
     [(34, "Сосульки, машины не ставить.")], "mocking interpretation"),
    ("anya", "Я шеф-повар этого известного ресторана.",
     "I am the head chef of this famous restaurant.",
     [], "asserting status"),
    ("elena", "А я шеф-повар соседнего ресторана.",
     "And I am the head chef of the neighboring restaurant.",
     [], "matching rank"),
    ("anya", "Тогда вы должны понимать правила.",
     "Then you must understand the rules.",
     [], "demanding compliance"),
    ("elena", "Я не буду переставлять свою машину.",
     "I will not move my car.",
     [(36, "В общем, я свою машину переставлять никуда не буду.")], "refusing to move"),
    ("elena", "Вон там есть другое свободное место.",
     "Over there is another open spot.",
     [(37, "Вон вам свободное место.")], "redirecting parking"),
    ("anya", "Какая упрямая и вредная женщина!",
     "What a stubborn and obnoxious woman!",
     [(40, "Обиженная женщина способна на любые поступки")], "grumbling in annoyance"),
    ("elena", "Приятного рабочего дня, господин шеф!",
     "Have a nice working day, Mr. Chef!",
     [], "parting sarcastically"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Кто поставил сюда эту старую машину?",
     "'Who parked this old car here?' — interrogative pronoun subject with past perfective motion verb."),
    (2, "Женщина, уберите автомобиль с моего места.",
     "'Woman, move the automobile from my spot.' — formal plural imperative followed by a prepositional phrase."),
    (3, "Где написано, что это ваше место?",
     "'Where does it say this is your spot?' — impersonal passive participle introducing a content clause."),
    (5, "Там написано только про сосульки.",
     "'It only says about icicles there.' — prepositional construction with restrictive particle."),
    (6, "Я шеф-повар этого известного ресторана.",
     "'I am the head chef of this famous restaurant.' — compound occupational noun with a genitive modifier."),
    (7, "А я шеф-повар соседнего ресторана.",
     "'And I am the head chef of the neighboring restaurant.' — contrasting coordinate clause asserting equal status."),
    (8, "Тогда вы должны понимать правила.",
     "'Then you must understand the rules.' — modal short adjective governing an imperfective infinitive."),
    (9, "Я не буду переставлять свою машину.",
     "'I will not move my car.' — compound negative future verb governing a reflexive possessive noun."),
    (10, "Вон там есть другое свободное место.",
     "'Over there is another open spot.' — existential sentence with a pointing particle and adjective."),
    (12, "Приятного рабочего дня, господин шеф!",
     "'Have a nice working day, Mr. Chef!' — polite farewell wish in the genitive case with formal title."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("elena", "Приятного рабочего дня, господин шеф!")
