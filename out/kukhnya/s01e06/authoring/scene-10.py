"""s01e06 scene 10: Срочная уборка (An Urgent Cleanup)."""

ID = "kukhnya-s01e06-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = "Срочная уборка  (An Urgent Cleanup)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Лёва", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = "Cues 153-156. Chef Barinov and sous-chef Lyova rush to prepare the kitchen for a surprise inspection."

INTRO = (
    "Panic strikes Claude Monet as word spreads that a health inspector has just entered the restaurant. "
    "Chef Viktor Barinov and his faithful sous-chef Lyova scramble across the kitchen, shouting orders to hide violations before the doors open. "
    "Let's listen to their frantic exchange in Russian first."
)

STORY = [
    ("chef", "Не спим, Лёва, у нас проверка!", "Wake up, Lyova, we have an inspection!",
     [(156, "Не спим, Лёва, у нас проверка")], ""),
    ("anya", "Шеф, инспектор уже заходит в зал!", "Chef, the inspector is already entering the hall!",
     [], ""),
    ("chef", "Быстро убирайте всё лишнее со столов.", "Quickly clear everything extra off the tables.",
     [], ""),
    ("anya", "Куда спрятать эти старые продукты?", "Where to hide these old products?",
     [], ""),
    ("chef", "Неси всё это прямо в холодильник.", "Carry all this straight into the refrigerator.",
     [(153, "порозилку")], ""),
    ("anya", "А что делать с грязными фартуками?", "And what to do with dirty aprons?",
     [], ""),
    ("chef", "Лёва, немедленно бросай их в стирку!", "Lyova, immediately throw them into the wash!",
     [(155, "Лёва, стирку")], ""),
    ("anya", "Я уже отправил Сеню за тряпками.", "I already sent Senya for cloths.",
     [], ""),
    ("chef", "Вытрите пол, он слишком скользкий!", "Wipe the floor, it is too slippery!",
     [], ""),
    ("anya", "Повара уже моют свои рабочие места.", "The cooks are already washing their workstations.",
     [], ""),
    ("chef", "Кухня должна быть идеально чистой!", "The kitchen must be ideally clean!",
     [], ""),
    ("anya", "Мы успеем всё сделать вовремя, шеф!", "We will manage to do everything in time, chef!",
     [], ""),
    ("chef", "По местам, инспектор уже здесь!", "To your stations, the inspector is already here!",
     [], ""),
]

OPENER = "Let's examine how the kitchen staff organizes a rapid emergency cleanup."

WALK = [
    (0, None,
     "'Wake up, Lyova, we have an inspection!' The negative plural verb literally means 'we are not sleeping', a common colloquial way to order people to hurry up."),
    (2, None,
     "'Quickly clear everything extra off the tables.' The adverb leads the sentence, followed by an imperative verb governing the accusative noun phrase."),
    (6, None,
     "'Lyova, immediately throw them into the wash!' The urgent adverb modifies the imperative verb, with the destination expressed by a prepositional phrase."),
    (8, None,
     "'Wipe the floor, it is too slippery!' The imperative verb commands immediate cleaning, followed by a clause describing the dangerous condition."),
]

TRANSITION = "Okay, let's hear the whole kitchen rush once more."

OUTRO = (
    "Now you know how Russian restaurant staff urgently cleans up before a health check. "
    "Listen for these fast-paced commands next time you watch the episode."
)

CLOSING = ("anya", "Сегодня будет очень трудный день.")
