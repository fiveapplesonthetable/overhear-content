"""s01e07 scene 10: Произведение искусства (A Work of Art)."""

ID = "kukhnya-s01e07-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 10
TITLE = "Произведение искусства  (A Work of Art)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiev": "anja"}
LABELS = {"anya": "Шеф", "nagiev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = "Cues 192-195. Chef Barinov proudly presents his signature sauce to restaurant owner Dmitry Nagiyev."

INTRO = (
    "Chef Viktor Barinov personally brings his latest culinary creation to the VIP table of restaurant owner Dmitry Nagiyev. "
    "Confident in his culinary genius, the chef boasts about the exquisite flavor while Dmitry prepares to judge the dish. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Дмитрий, сейчас ты попробуешь шедевр!", "Dmitry, right now you will taste a masterpiece!",
     [(192, "Сейчас попробуешь произведение искусства")], ""),
    ("nagiev", "Виктор, ты снова хвалишь себя?", "Viktor, are you praising yourself again?",
     [], ""),
    ("anya", "Это настоящее кулинарное произведение искусства!", "This is a real culinary work of art!",
     [(192, "произведение искусства")], ""),
    ("nagiev", "Мне не терпится отведать твоего соуса.", "I cannot wait to taste your sauce.",
     [(195, "не терпится отведать")], ""),
    ("anya", "Я готовил этот соус всё утро.", "I was preparing this sauce all morning.",
     [], ""),
    ("nagiev", "Надеюсь, ты положил правильные специи.", "I hope you put the right spices.",
     [], ""),
    ("anya", "Там только самые свежие ингредиенты.", "There are only the freshest ingredients there.",
     [], ""),
    ("nagiev", "Запах действительно очень приятный и тонкий.", "The aroma is indeed very pleasant and subtle.",
     [], ""),
    ("anya", "Один кусочек мяса изменит всё.", "One piece of meat will change everything.",
     [], ""),
    ("nagiev", "Не преувеличивай, дай мне вилку.", "Do not exaggerate, give me a fork.",
     [], ""),
    ("anya", "Сначала попробуй соус с хлебом.", "First try the sauce with bread.",
     [], ""),
    ("nagiev", "Хорошо, давай начнём эту дегустацию.", "Alright, let us begin this tasting.",
     [], ""),
    ("anya", "Приятного аппетита, дорогой хозяин!", "Bon appetit, my dear owner!",
     [], ""),
]

OPENER = "Let's explore how Chef Barinov presents his signature sauce to the restaurant owner."

WALK = [
    (0, None,
     "'Dmitry, right now you will taste a masterpiece!' The chef addresses the owner with a direct vocative name and an enthusiastic future tense verb."),
    (2, None,
     "'This is a real culinary work of art!' The expressive noun phrase uses demonstrative and descriptive adjectives with a genitive noun complement."),
    (3, None,
     "'I cannot wait to taste your sauce.' An impersonal construction with a reflexive verb in the dative expresses keen anticipation."),
    (10, None,
     "'First try the sauce with bread.' The chef gives guidance with an imperative verb and instrumental case showing accompaniment."),
]

TRANSITION = "Now, let's listen to Chef Barinov presenting the sauce to Dmitry once more."

OUTRO = (
    "Now you know how to talk about culinary creations and express high anticipation in Russian. "
    "Listen for these gourmet expressions in the next scene."
)

CLOSING = ("nagiev", "Посмотрим, стоит ли этот соус похвалы.")
