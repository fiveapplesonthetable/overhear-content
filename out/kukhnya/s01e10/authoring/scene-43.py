"""Scene 43 — Caviar and Football (s01e10, 00:22:03–00:22:29)."""

ID = "kukhnya-s01e10-scene-43"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 43
TITLE = "Икра и футбол  (Caviar and Football)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "guest": "anja",
}

LABELS = {
    "anya": "Шеф",
    "guest": "Гость",
}

INTRO = (
    "In the main restaurant room, a VIP guest lavishly praises the special caviar, believing Barinov's tale about private planes from Astrakhan. "
    "Meanwhile, Barinov anxiously tracks the football broadcast, his mood swinging wildly with every update from the pitch."
)

STORY = [
    ("guest", "Шеф, налейте мне ещё немного вина.",
     "Chef, pour me some more wine.",
     [(310, "Налей мне чего-нибудь.")], "Guest asks"),

    ("guest", "Какая невероятно вкусная у вас чёрная икра!",
     "What an incredibly delicious black caviar you have!",
     [(311, "Какая вкусная у вас игра.")], "Guest praises"),

    ("anya", "Конечно, это лучшая икра прямо из Астрахани.",
     "Of course, this is the best caviar straight from Astrakhan.",
     [(312, "Из Астрахани.")], "Chef boasts"),

    ("anya", "Мы возим её сюда специальными боингами.",
     "We fly it here on special Boeings.",
     [(313, "Возим. Боингами.")], "Chef fabricates story"),

    ("guest", "Ну что, по вкусу всё просто отлично!",
     "Well, in taste everything is simply excellent!",
     [(314, "Ну что? Мне бы все хорошо.")], "Guest smiles"),

    ("anya", "В нашем ресторане иначе и быть не может.",
     "In our restaurant it cannot be any other way.",
     [(315, "Ну и иначе быть не может.")], "Chef nods politely"),

    ("anya", "Официант, какой сейчас счёт в матче?",
     "Waiter, what is the score in the match now?",
     [], "Chef asks aside"),

    ("guest", "Там сейчас счёт три-три, наши отыгрались!",
     "The score there is three-three now, our guys tied it up!",
     [(316, "Что? Три-три."), (317, "Наши молодцы отыгрались.")], "Guest checks score"),

    ("guest", "Они двадцать лет подряд так не отыгрывались.",
     "They had not tied it up like that for twenty years in a row.",
     [(318, "20 лет не отыгрывались.")], "Guest adds"),

    ("guest", "А сегодня вдруг забили три быстрых гола!",
     "And today they suddenly scored three quick goals!",
     [(319, "А сегодня отыгрались.")], "Guest marvels"),

    ("anya", "Неужели Спартак опять упустил победу в конце?!",
     "Did Spartak really let victory slip away in the end again?!",
     [], "Chef fumes inside"),

    ("guest", "Футбол сегодня получился очень нервный и странный.",
     "Football today turned out very nervous and strange.",
     [], "Guest remarks"),

    ("anya", "Да уж, играют как настоящие бездельники!",
     "Indeed, they play like real slackers!",
     [(321, "Уроды.")], "Chef curses quietly"),
]

OPENER = "Let's listen to the VIP guest savoring the fraudulent caviar while Barinov agonizes over a live football match."

WALK = [
    (0, None,
     "'Chef, pour me some more wine.' The relaxed guest enjoys his lavish meal at the table."),
    (1, None,
     "'What an incredibly delicious black caviar you have!' The patron showers compliments on the dish."),
    (2, None,
     "'Of course, this is the best caviar straight from Astrakhan.' Barinov spins a bold yarn."),
    (3, None,
     "'We fly it here on special Boeings.' The chef adds ridiculous claims about luxury transport."),
    (4, None,
     "'Well, in taste everything is simply excellent!' The guest remains totally unaware of the deception."),
    (5, None,
     "'In our restaurant it cannot be any other way.' Barinov plays along smoothly."),
    (6, None,
     "'Waiter, what is the score in the match now?' The chef whispers urgently about the game."),
    (7, None,
     "'The score there is three-three now, our guys tied it up!' The patron shares the thrilling score."),
    (8, None,
     "'They had not tied it up like that for twenty years in a row.' The guest marvels at the comeback."),
    (9, None,
     "'And today they suddenly scored three quick goals!' The table buzzes with football excitement."),
    (10, None,
     "'Did Spartak really let victory slip away in the end again?!' Barinov burns with inward fury."),
    (11, None,
     "'Football today turned out very nervous and strange.' The guest notes the unpredictable game."),
    (12, None,
     "'Indeed, they play like real slackers!' Barinov vents his deep sports frustration under his breath."),
]

TRANSITION = "Now let's listen to the high-society dining banter and Barinov's football agony once more."

OUTRO = "Between fraudulent caviar compliments and a painful match result, Barinov barely keeps his anger under control."

CLOSING = ("anya", "Да уж, играют как настоящие бездельники!")
