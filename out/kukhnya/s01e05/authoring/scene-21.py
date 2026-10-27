"""Scene 21 — Rush in the Head (s01e05, 00:22:22–00:22:38)."""

ID = "kukhnya-s01e05-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 21
TITLE = "Запара в голове  (Rush in the Head)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 306-312. Seeing Max completely overwhelmed by the dinner rush, "
    "veteran cook Fedya steps in to teach him how to breathe and stay calm under pressure."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}

LABELS = {
    "anya": "Макс",
    "fedya": "Федя",
}

INTRO = (
    "During the overwhelming evening rush at Claude Monet, orders pile up endlessly "
    "and Max finds himself pushed to the absolute breaking point. "
    "Taking pity on the rookie, seasoned fish cook Fedya steps up to his station "
    "to teach him the ultimate golden rule of kitchen survival. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("fedya", "Ладно, новичок, отойди немного в сторону.",
     "Alright, newcomer, step aside a little.",
     [(306, "Ладно")], "Fedya steps in"),

    ("fedya", "Подвинься давай, я помогу тебе.",
     "Move over, come on, I will help you.",
     [(307, "Подвинься давай.")], "Fedya offers help"),

    ("anya", "Федя, спасибо, у меня ничего не получается!",
     "Fedya, thank you, nothing is working out for me!",
     [], "Max admits struggle"),

    ("fedya", "Сейчас главное — полностью успокоиться.",
     "Right now the main thing is to completely calm down.",
     [(308, "Нужно расслабиться.")], "Calm advice"),

    ("fedya", "Сделай глубокий вдох.",
     "Take a deep breath.",
     [(308, "Вдох.")], "Breathing instruction"),

    ("fedya", "А теперь медленный выдох.",
     "And now a slow exhale.",
     [(309, "Выдох.")], "Exhale instruction"),

    ("fedya", "И навсегда запомни главное правило.",
     "And forever remember the main rule.",
     [(310, "И запомнить.")], "Core rule announcement"),

    ("fedya", "Запара бывает не на кухне.",
     "The rush does not happen in the kitchen.",
     [(311, "на кухне.")], "Dispelling the myth"),

    ("fedya", "Настоящая запара всегда только в голове!",
     "The real rush is always only in your head!",
     [(312, "Запара в голове.")], "The golden rule"),

    ("anya", "Но заказы идут каждую минуту!",
     "But orders keep coming every minute!",
     [], "Max points to pressure"),

    ("fedya", "Делай каждое блюдо по очереди.",
     "Make each dish in turn.",
     [], "Methodical approach"),

    ("anya", "Хорошо, я понял твой совет.",
     "Alright, I understood your advice.",
     [], "Max takes advice"),

    ("fedya", "Тогда начинай готовить спокойно!",
     "Then begin to cook calmly!",
     [], "Fedya encourages Max"),
]

OPENER = "Now let's examine Fedya and Max's kitchen advice line by line."

WALK = [
    (0, None,
     "'Alright, newcomer, step aside a little.' Fedya takes charge of the crowded workspace with calm authority."),
    (1, None,
     "'Move over, come on, I will help you.' The experienced line cook generously offers practical assistance."),
    (2, None,
     "'Fedya, thank you, nothing is working out for me!' Max gratefully admits his helplessness amid the tickets."),
    (3, None,
     "'Right now the main thing is to completely calm down.' Fedya emphasizes emotional control over panic."),
    (4, None,
     "'Take a deep breath.' Fedya guides his young colleague through a simple centering exercise."),
    (5, None,
     "'And now a slow exhale.' The veteran chef ensures Max releases the mounting physical tension."),
    (6, None,
     "'And forever remember the main rule.' Fedya prepares to impart essential professional wisdom."),
    (7, None,
     "'The rush does not happen in the kitchen.' Fedya begins dismantling the illusion of external chaos."),
    (8, None,
     "'The real rush is always only in your head!' The seasoned cook reveals the psychological secret to handling pressure."),
    (9, None,
     "'But orders keep coming every minute!' Max vocalizes the anxiety caused by the relentless printer."),
    (10, None,
     "'Make each dish in turn.' Fedya reminds him that steady sequential focus conquers any pile of tickets."),
    (11, None,
     "'Alright, I understood your advice.' Max internalizes the lesson and regains his composure."),
    (12, None,
     "'Then begin to cook calmly!' Fedya gives the green light to restart work with confidence."),
]

TRANSITION = "Now let's listen to Fedya's wise coaching once more without interruption."

OUTRO = (
    "Equipped with Fedya's invaluable advice, Max steadies his hands and prepares to clear the rush."
)

CLOSING = ("fedya", "Тогда начинай готовить спокойно!")
