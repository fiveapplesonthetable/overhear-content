"""s01e02 scene 21: Опасная находка (A Dangerous Find)."""

ID = "kukhnya-s01e02-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 21
TITLE = "Опасная находка  (A Dangerous Find)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "senya": "anja",
}
LABELS = {
    "anya": "Макс",
    "senya": "Сеня",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = (
    "In the kitchen prep area, Senya discovers that Max is holding the Chef's missing fish knife. "
    "Terrified of Chef Barinov's legendary fury, Senya frantically comes up with an absurd hiding place. "
    "Listen to their frantic whispered conversation in Russian first, then we will break it down in English."
)

STORY = [
    ("senya", "Ты совсем с ума сошёл, парень?",
     "Have you gone completely out of your mind, buddy?",
     [(231, "Ты совсем")], "verbatim shock"),
    ("senya", "Зачем ты взял этот острый нож?",
     "Why did you take this sharp knife?",
     [(231, "ты его взял")], "verbatim question"),
    ("anya", "Шеф сам оставил его на столе.",
     "The chef left it on the table himself.",
     [(233, "Я не брал")], "defending oneself"),
    ("senya", "Он же тебя просто на куски порежет!",
     "After all, he will simply slice you into pieces!",
     [(232, "Он же тебя"), (233, "Прирежет")], "hyperbolic warning"),
    ("anya", "Я не хотел брать чужой нож.",
     "I did not want to take someone else's knife.",
     [(233, "Я не брал")], "verbatim excuse"),
    ("senya", "Слушай меня очень внимательно сейчас.",
     "Listen to me very carefully right now.",
     [(234, "Слушай")], "urgent command"),
    ("senya", "Нужно срочно спрятать его от шефа.",
     "We need to hide it from the chef urgently.",
     [(234, "спрятать его")], "urgent plan"),
    ("anya", "Куда мы можем спрятать этот нож?",
     "Where can we hide this knife?",
     [(234, "спрятать его")], "looking for spot"),
    ("senya", "Спрячь его в большую свежую рыбу!",
     "Hide it inside a big fresh fish!",
     [(241, "в рыбе")], "bizarre idea"),
    ("anya", "Ты серьёзно предлагаешь спрятать в рыбу?",
     "Are you seriously suggesting hiding it in a fish?",
     [(242, "В рыбе")], "incredulous reaction"),
    ("senya", "Там его точно никто не найдёт.",
     "Nobody will definitely find it there.",
     [(234, "пока шеф не видит")], "confident guarantee"),
    ("anya", "Хорошо, я быстро положу его туда.",
     "All right, I will put it in there quickly.",
     [(234, "спрятать его")], "compliance"),
    ("senya", "Только делай всё тихо и незаметно.",
     "Just do everything quietly and inconspicuously.",
     [(234, "пока шеф не видит")], "urging caution"),
    ("anya", "Никто на кухне ничего не заметил.",
     "Nobody in the kitchen noticed anything.",
     [(234, "пока шеф не видит")], "confirming success"),
]

OPENER = "Now let us walk through each phrase to understand every Russian word."

WALK = [
    (0, "Ты совсем с ума сошёл, парень?",
     "'Have you gone completely out of your mind, buddy?' A colloquial idiom expressing intense shock and alarm."),
    (1, "Зачем ты взял этот острый нож?",
     "'Why did you take this sharp knife?' Senya asks what possessed Max to touch the forbidden blade."),
    (2, "Шеф сам оставил его на столе.",
     "'The chef left it on the table himself.' Max defends himself by noting where the knife was lying."),
    (3, "Он же тебя просто на куски порежет!",
     "'After all, he will simply slice you into pieces!' A hyperbolic warning of Chef Barinov's legendary temper."),
    (4, "Я не хотел брать чужой нож.",
     "'I did not want to take someone else's knife.' Max explains his lack of bad intentions."),
    (5, "Слушай меня очень внимательно сейчас.",
     "'Listen to me very carefully right now.' An imperative demanding full focus for urgent instructions."),
    (6, "Нужно срочно спрятать его от шефа.",
     "'We need to hide it from the chef urgently.' Predicative phrasing indicating necessary immediate action."),
    (7, "Куда мы можем спрятать этот нож?",
     "'Where can we hide this knife?' The directional question looks for a secret spot in the kitchen."),
    (8, "Спрячь его в большую свежую рыбу!",
     "'Hide it inside a big fresh fish!' An ingenious but absurd hiding place suggested by Senya."),
    (9, "Ты серьёзно предлагаешь спрятать в рыбу?",
     "'Are you seriously suggesting hiding it in a fish?' Max questions whether the plan is completely crazy."),
    (10, "Там его точно никто не найдёт.",
     "'Nobody will definitely find it there.' The negative pronoun pairs with the negated verb."),
    (11, "Хорошо, я быстро положу его туда.",
     "'All right, I will put it in there quickly.' Max complies before the chef returns to the prep area."),
    (12, "Только делай всё тихо и незаметно.",
     "'Just do everything quietly and inconspicuously.' Paired adverbs instructing stealthy execution."),
    (13, "Никто на кухне ничего не заметил.",
     "'Nobody in the kitchen noticed anything.' A double negative confirming that the concealment succeeded."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "The missing knife is now buried deep inside a large salmon, setting the stage for one of the show's funniest disasters. "
    "Listen out for what happens when that very fish is carried out into the dining room! Until next time!"
)

CLOSING = ("anya", "Теперь нож спрятан надёжно.")
