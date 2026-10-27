"""s01e10 scene 18: Деньги на икру (Money for Caviar)."""

ID = "kukhnya-s01e10-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 18
TITLE = "Деньги на икру  (Money for Caviar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cue 152. Victoria hands Barinov cash designated for restaurant black caviar, which he secretly plans to use for his bet."

INTRO = (
    "Victoria briefly steps into Chef Barinov's office to hand over cash allocated for purchasing gourmet caviar for the restaurant. "
    "Seeing an unexpected pile of money right in front of him, Viktor instantly realizes he can fund his secret bet. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Виктор Петрович, я совсем забыла.", "Viktor Petrovich, I completely forgot.",
     [(152, "Забыла совсем")], ""),
    ("anya", "Вот наличные деньги на свежую икру.", "Here is the cash for fresh caviar.",
     [(152, "Вот деньги на икру")], ""),
    ("chef", "Огромное спасибо, моя дорогая Вика.", "Thank you very much, my dear Vika.",
     [], ""),
    ("chef", "Ты спасаешь наш вечерний банкет.", "You are saving our evening banquet.",
     [], ""),
    ("anya", "Поставщик привезёт банку через час.", "The supplier will bring the jar in an hour.",
     [], ""),
    ("chef", "Отлично, я сам встречу курьера.", "Excellent, I will meet the courier myself.",
     [], ""),
    ("anya", "Пожалуйста, отдайте ему деньги сразу.", "Please give him the money right away.",
     [], ""),
    ("chef", "Не переживай, всё под моим контролем.", "Do not worry, everything is under my control.",
     [], ""),
    ("anya", "И что там с нашей плитой?", "And what is going on with our stove?",
     [], ""),
    ("chef", "Мастера уже заканчивают сложный ремонт.", "The craftsmen are already finishing the complex repair.",
     [], ""),
    ("anya", "Надеюсь на вашу честность, шеф.", "I rely on your honesty, chef.",
     [], ""),
    ("chef", "Я всегда держу своё мужское слово.", "I always keep my manly word.",
     [], ""),
]

OPENER = "Let's explore how Victoria delivers the kitchen funds and how Barinov secures the cash for his own plans."

WALK = [
    (1, None,
     "'Here is the cash for fresh caviar.' The demonstrative particle introduces the cash payment needed for the kitchen."),
    (4, None,
     "'The supplier will bring the jar in an hour.' A future tense verb indicates a scheduled delivery time for the staff."),
    (7, None,
     "'Do not worry, everything is under my control.' A reassuring imperative followed by an assertive statement of confidence in the plan."),
    (11, None,
     "'I always keep my manly word.' A proud first person assertion used to build trust with a colleague."),
]

TRANSITION = "Now, let's hear Victoria deliver the restaurant funds once more."

OUTRO = (
    "Now you know how to talk about cash deliveries, give instructions about suppliers, and offer reassurances in Russian. "
    "Listen for these practical business expressions in the following scene."
)

CLOSING = ("chef", "Теперь у меня есть нужная сумма.")
