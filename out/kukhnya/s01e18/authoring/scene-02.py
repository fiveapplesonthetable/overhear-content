ID = "kukhnya-s01e18-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 2
TITLE = "Низкая выручка  (Low Revenue)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "dmitry": "anja", "barinov": "angelina"}
LABELS = {"anya": "Вика", "dmitry": "Дмитрий", "barinov": "Баринов"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 18-37. Dmitry checks financial reports with Vika and Barinov."

INTRO = "Dmitry is shocked by the tiny revenue numbers in the financial report and confronts Vika and Viktor. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("dmitry", "Что это за маленькие цифры в отчёте?",
     "What are these small numbers in the report?",
     [(18, "а что это за такие")], "adapted"),
    ("dmitry", "Почему у нас так мало денег?",
     "Why do we have so little money?",
     [(21, "Почему так мало у нас")], "adapted"),
    ("anya", "Дмитрий Владимирович, сейчас у нас мало гостей.",
     "Dmitry Vladimirovich, we have few guests right now.",
     [(22, "Дмитрий Владимирович")], "adapted"),
    ("anya", "Рядом открылся новый итальянский ресторан.",
     "A new Italian restaurant opened nearby.",
     [], "new"),
    ("dmitry", "А мне что теперь делать?",
     "And what am I supposed to do now?",
     [(24, "А мне что делать")], "adapted"),
    ("dmitry", "Мне нужно кормить свою большую семью!",
     "I need to feed my big family!",
     [], "new"),
    ("barinov", "Дима, ну сейчас просто нет людей.",
     "Dima, well there are simply no people right now.",
     [(27, "ну нет людей")], "adapted"),
    ("barinov", "Мы не можем тащить их сюда силой.",
     "We cannot drag them in here by force.",
     [(27, "Не можем же мы их сюда")], "adapted"),
    ("dmitry", "У вас всегда одна и та же история!",
     "You always have the exact same story!",
     [(28, "история")], "adapted"),
    ("anya", "Мы обязательно придумаем хорошее решение.",
     "We will definitely come up with a good solution.",
     [], "new"),
    ("dmitry", "Вы видите, мы здесь серьёзно работаем.",
     "You see, we are working seriously here.",
     [(36, "ты видишь, мы здесь работаем")], "adapted"),
    ("dmitry", "Я остаюсь в ресторане со своими коллегами!",
     "I am staying at the restaurant with my colleagues!",
     [(37, "с коллегами")], "adapted"),
]

OPENER = "Let's break down this tense business meeting."

WALK = [
    (0, None,
     "'What are these small numbers in the report?' -- Dmitry stares at the financial sheet in disbelief."),
    (1, None,
     "'Why do we have so little money?' -- The owner demands an explanation for the drop in profit."),
    (2, None,
     "'Dmitry Vladimirovich, we have few guests right now.' -- Vika explains that attendance is very low this month."),
    (3, None,
     "'A new Italian restaurant opened nearby.' -- She points out that competitors are drawing customers away."),
    (4, None,
     "'And what am I supposed to do now?' -- Dmitry asks how he should handle these losses."),
    (5, None,
     "'I need to feed my big family!' -- He complains about his heavy personal expenses."),
    (6, None,
     "'Dima, well there are simply no people right now.' -- Viktor tries to calm his boss down with facts."),
    (7, None,
     "'We cannot drag them in here by force.' -- The chef notes that guests must choose to come on their own."),
    (8, None,
     "'You always have the exact same story!' -- Dmitry is tired of hearing excuses from his staff."),
    (9, None,
     "'We will definitely come up with a good solution.' -- Vika promises to find a way to attract diners."),
    (10, None,
     "'You see, we are working seriously here.' -- Dmitry tells his wife that he has urgent business at the office."),
    (11, None,
     "'I am staying at the restaurant with my colleagues!' -- He decides to cancel shopping and supervise the team."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Dmitry sends Kristina away so he can take personal control of the restaurant's finances."
CLOSING = ("dmitry", "Я остаюсь в ресторане со своими коллегами!")
