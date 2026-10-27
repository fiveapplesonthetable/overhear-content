"""s01e06 scene 09: Волос в тарелке (A Hair on the Plate)."""

ID = "kukhnya-s01e06-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 9
TITLE = "Волос в тарелке  (A Hair on the Plate)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "gost": "anja"}
LABELS = {"anya": "Настя", "gost": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"

INTRO = (
    "In the elegant dining room of Claude Monet, an indignant diner summons waitress Nastya over to his table. "
    "He points out a long stray hair in his meal, sparking a hilariously deadpan exchange with the unflappable waitress. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("gost", "Девушка, подойдите немедленно к нашему столу!",
     "Miss, come over to our table immediately!",
     [(85, "Бевушка")], "calling the waitress angrily"),
    ("anya", "Добрый день, слушаю вас очень внимательно.",
     "Good day, I am listening to you very attentively.",
     [(86, "Слушаю вас")], "responding politely"),
    ("gost", "Посмотрите на это, что это такое?",
     "Look at this, what is that?",
     [(86, "Это что")], "pointing at his plate"),
    ("anya", "Я вижу, что это обычный волос.",
     "I see that this is an ordinary hair.",
     [(87, "Это волос")], "stating the obvious calmly"),
    ("gost", "Я тоже отлично вижу этот длинный волос!",
     "I also see this long hair perfectly well!",
     [(88, "Я вижу, что это волос")], "growing exasperated"),
    ("anya", "Тогда зачем вы об этом спрашиваете?",
     "Then why are you asking about it?",
     [(89, "А зачем тогда спрашиваете")], "replying with deadpan logic"),
    ("gost", "Как этот волос попал в тарелку?",
     "How did this hair get onto the plate?",
     [(90, "Я хочу понять, как этот волос попал ко мне в тарелку")], "demanding an explanation"),
    ("anya", "Вероятно, он просто выпал из вашей головы.",
     "Probably it simply fell out of your head.",
     [(91, "Вероятно, выпал из вашей головы")], "suggesting a logical source"),
    ("gost", "Такой длинный волос не может быть моим!",
     "Such a long hair cannot be mine!",
     [(92, "Такой длинный")], "protesting indignantly"),
    ("anya", "Тогда, наверное, он выпал из бороды.",
     "Then probably it fell out of a beard.",
     [(93, "Наверное, из вашей бороды")], "offering another guess"),
    ("gost", "У меня нет бороды, позовите шефа!",
     "I do not have a beard, call the chef!",
     [(94, "У меня нет бороды"), (95, "Позовите ко мне шеф-повара")], "losing his temper"),
    ("anya", "Хорошо, я сейчас позову шеф-повара.",
     "Fine, I will call the head chef right now.",
     [(96, "Зову")], "agreeing calmly"),
]

OPENER = "Let's review this hilarious confrontation in the dining room line by line."

WALK = [
    (0, None,
     "'Miss, come over to our table immediately!' The angry customer demands instant attention from the waitstaff."),
    (1, None,
     "'Good day, I am listening to you very attentively.' Nastya greets him with calm professional courtesy."),
    (2, None,
     "'Look at this, what is that?' The customer points aggressively down at his meal."),
    (3, None,
     "'I see that this is an ordinary hair.' Nastya offers a calm and literal observation of the offending item."),
    (4, None,
     "'I also see this long hair perfectly well!' The guest fumes at her obvious answer."),
    (5, None,
     "'Then why are you asking about it?' Nastya innocently questions why he posed a question he already knew the answer to."),
    (6, None,
     "'How did this hair get onto the plate?' The guest presses for an institutional explanation."),
    (7, None,
     "'Probably it simply fell out of your head.' Nastya neutrally suggests the customer might be the origin."),
    (8, None,
     "'Such a long hair cannot be mine!' The short-haired diner rejects the suggestion out of hand."),
    (9, None,
     "'Then probably it fell out of a beard.' Nastya helpfully suggests another facial source."),
    (10, None,
     "'I do not have a beard, call the chef!' The clean-shaven customer reaches his boiling point and demands management."),
    (11, None,
     "'Fine, I will call the head chef right now.' Nastya unhurriedly walks off toward the kitchen to fetch Barinov."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Leaving the infuriated guest waiting at his table, Nastya heads into the kitchen to alert Chef Barinov. "
    "See you next time!"
)

CLOSING = ("anya", "Хорошо, я сейчас позову шеф-повара.")
