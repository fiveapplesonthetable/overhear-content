"""s01e01 scene 22: Визит конкурента (The Rival's Visit)."""

ID = "kukhnya-s01e01-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 22
TITLE = "Визит конкурента  (The Rival's Visit)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "dmitry": "anja",
    "mark": "angelina",
}
LABELS = {
    "anya": "Вика",
    "dmitry": "Нагиев",
    "mark": "Марк",
}
SOURCE_NAME = "Кухня, Сезон 1, Эпизод 1"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = "Cues 275-306. Dmitry Nagiyev hosts rival restaurateur Mark and chef Elena at Claude Monet."

INTRO = (
    "At the prestigious Claude Monet restaurant, charismatic celebrity owner Dmitry Nagiyev welcomes a rival restaurateur, Mark. "
    "The two exchange playful insults about their head chefs, before Dmitry orders dining room art director Vika to serve "
    "the main course with special dietary care."
)

STORY = [
    ("dmitry", "Рад приветствовать вас в лучшем ресторане!",
     "Delighted to welcome you to the finest restaurant!",
     [(280, "рад приветствовать вас в лучшем ресторане")], "adapted cue"),

    ("mark", "Мы открываем наш ресторан через две недели.",
     "We are opening our restaurant in two weeks.",
     [(282, "Мы открываемся через две недели")], "adapted cue"),

    ("mark", "Познакомься, это мой шеф-повар Елена.",
     "Meet her, this is my chef Elena.",
     [(283, "Вот познакомься"), (284, "Мой шеф-повар Елена")], "adapted cue"),

    ("mark", "Она работала в самом лучшем ресторане.",
     "She worked at the very best restaurant.",
     [(289, "Она работала в самом лучшем ресторане")], "adapted cue"),

    ("mark", "А твой шеф ещё не заболел?",
     "And has your chef not fallen sick yet?",
     [(294, "А у твоего шефа-алкоголика печень еще не отвалилась?")], "polite adaptation of cue"),

    ("dmitry", "Не волнуйся, мой шеф переживёт тебя.",
     "Do not worry, my chef will outlive you.",
     [(295, "Не волнуйся"), (296, "переживет")], "adapted cue"),

    ("dmitry", "Вика, скорее подавай гостям горячие блюда!",
     "Vika, serve the hot dishes to the guests quickly!",
     [(298, "Вика!"), (300, "Подавай-ка, Вика, горячая")], "adapted cue"),

    ("dmitry", "Наши гости очень сильно проголодались.",
     "Our guests have gotten very hungry.",
     [(301, "Гости наши проголодались")], "adapted cue"),

    ("anya", "Добрый день, сейчас всё принесут.",
     "Good day, they will bring everything right now.",
     [(276, "Добрый день"), (299, "Да, Дмитрий Владимирович")], "adapted cue"),

    ("mark", "Только проследите, чтобы совсем не было перца.",
     "Just make sure there is no pepper at all.",
     [(302, "Да, только проследите, пожалуйста, чтобы совсем не было перца")], "adapted cue"),

    ("anya", "Хорошо, я немедленно предупрежу шеф-повара.",
     "Very well, I will notify the head chef immediately.",
     [(303, "Хорошо, сейчас же предупрежу шеф-повара")], "adapted cue"),

    ("anya", "На кухне уже готовят этот заказ.",
     "In the kitchen they are already preparing this order.",
     [(304, "основное блюдо для гостей можно уже подавать")], "adapted cue"),

    ("dmitry", "У нас на кухне работают лучшие мастера.",
     "In our kitchen the best masters work.",
     [], "Nagiyev bragging"),

    ("anya", "Я лично прослежу за этим блюдом.",
     "I will personally oversee this dish.",
     [], "Vika's professional assurance"),
]

OPENER = "Let's see how Dmitry Nagiyev welcomes his rival in this lively scene."

WALK = [
    (0, None,
     "'Delighted to welcome you to the finest restaurant!' Dmitry grandly welcomes his guests into Claude Monet."),
    (1, None,
     "'We are opening our restaurant in two weeks.' Mark announces his imminent competition in Moscow."),
    (2, None,
     "'Meet her, this is my chef Elena.' Mark proudly introduces his elite culinary import."),
    (3, None,
     "'She worked at the very best restaurant.' Highlighting her international pedigree from prestigious venues."),
    (4, None,
     "'And has your chef not fallen sick yet?' Teasing Dmitry about Viktor Barinov's notorious drinking."),
    (5, None,
     "'Do not worry, my chef will outlive you.' Nagiyev fires back with confidence in his star cook."),
    (6, None,
     "'Vika, serve the hot dishes to the guests quickly!' Dmitry signals the floor manager to present food."),
    (7, None,
     "'Our guests have gotten very hungry.' A gracious host prioritizing the table's comfort."),
    (8, None,
     "'Good day, they will bring everything right now.' Vika responds with consummate professional charm."),
    (9, None,
     "'Just make sure there is no pepper at all.' Mark relays a critical dietary instruction."),
    (10, None,
     "'Very well, I will notify the head chef immediately.' Vika promises to deliver the strict constraint."),
    (11, None,
     "'In the kitchen they are already preparing this order.' Confirming active culinary preparation."),
    (12, None,
     "'In our kitchen the best masters work.' Dmitry proudly defends the quality of his staff."),
    (13, None,
     "'I will personally oversee this dish.' Vika takes personal responsibility for customer satisfaction."),
]

TRANSITION = "Now let's listen to the rival restaurateurs in the dining room once more."

OUTRO = "Dmitry exchanges smug smiles with Mark as Vika heads to the kitchen to deliver the ticket."

CLOSING = ("anya", "Я лично прослежу за этим блюдом.")
