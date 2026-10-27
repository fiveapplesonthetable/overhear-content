"""Scene 24 — A Chance to Stay (s01e04, 00:23:26–00:23:45)."""

ID = "kukhnya-s01e04-scene-24"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 24
TITLE = "Шанс остаться  (A Chance to Stay)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vika": "anja",
}

LABELS = {
    "anya": "Макс",
    "vika": "Вика",
}

INTRO = (
    "Outside Claude Monet, Vika catches up with Max as he prepares to leave the restaurant for good. "
    "To his immense relief, Vika reveals that she intervened with Chef Barinov and secured him a second chance."
)

STORY = [
    ("vika", "Макс, подожди минуту!",
     "Max, wait a minute!",
     [(331, "Макс!")], "Vika calls"),

    ("anya", "Вика? Что случилось?",
     "Vika? What happened?",
     [], "Max stops"),

    ("vika", "Ты никуда не уходишь.",
     "You are not leaving anywhere.",
     [(316, "что он не уволен?")], "Vika informs"),

    ("anya", "Но шеф только что меня уволил.",
     "But the chef just fired me.",
     [], "Max is confused"),

    ("vika", "Я поговорила с шефом.",
     "I spoke with the chef.",
     [], "Vika explains"),

    ("anya", "И что он тебе сказал?",
     "And what did he tell you?",
     [], "Max asks"),

    ("vika", "Он разрешил тебе остаться на кухне.",
     "He allowed you to stay in the kitchen.",
     [], "Vika delivers news"),

    ("anya", "Правда? Ты меня спасла!",
     "Really? You saved me!",
     [], "Max is overjoyed"),

    ("vika", "Только больше не совершай глупых ошибок.",
     "Just do not make stupid mistakes anymore.",
     [], "Vika warns"),

    ("anya", "Обещаю, я буду работать очень старательно.",
     "I promise, I will work very diligently.",
     [], "Max promises"),

    ("vika", "Возвращайся на свое рабочее место.",
     "Return to your work station.",
     [], "Vika directs"),

    ("anya", "Спасибо огромное за твою помощь, Вика!",
     "Thank you very much for your help, Vika!",
     [], "Max thanks"),

    ("vika", "Иди, пока шеф не передумал.",
     "Go, before the chef changes his mind.",
     [], "Vika urges"),

    ("anya", "У меня появился второй шанс!",
     "I got a second chance!",
     [], "Max celebrates"),
]

OPENER = "Let's explore Vika delivering the great news of a second chance to Max."

WALK = [
    (0, None,
     "'Max, wait a minute!' Vika rushes out to stop Max before he leaves."),
    (1, None,
     "'Vika? What happened?' Max turns around in surprise with his packed bag."),
    (2, None,
     "'You are not leaving anywhere.' The dining room director delivers the surprising news."),
    (3, None,
     "'But the chef just fired me.' Max reminds her of Barinov's angry decision."),
    (4, None,
     "'I spoke with the chef.' Vika reveals that she intervened on his behalf."),
    (5, None,
     "'And what did he tell you?' Max asks eagerly with a glimmer of hope."),
    (6, None,
     "'He allowed you to stay in the kitchen.' Vika confirms that he has his job back."),
    (7, None,
     "'Really? You saved me!' Max is overjoyed and deeply grateful to her."),
    (8, None,
     "'Just do not make stupid mistakes anymore.' Vika gives him a strict warning."),
    (9, None,
     "'I promise, I will work very diligently.' Max pledges to prove his worth on the line."),
    (10, None,
     "'Return to your work station.' Vika instructs him to get back to the kitchen."),
    (11, None,
     "'Thank you very much for your help, Vika!' Max thanks her warmly from the heart."),
    (12, None,
     "'Go, before the chef changes his mind.' Vika urges him to hurry inside."),
    (13, None,
     "'I got a second chance!' Max celebrates his narrow escape from being fired."),
]

TRANSITION = "Now let's listen to the full conversation outside the restaurant once more."

OUTRO = "With a second chance in hand, Max returns to the kitchen ready to prove himself."

CLOSING = ("anya", "У меня появился второй шанс!")
