"""s01e06 scene 11: Визит инспектора (The Inspector's Visit)."""

ID = "kukhnya-s01e06-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 11
TITLE = "Визит инспектора  (The Inspector's Visit)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "inspector": "anja"}
LABELS = {"anya": "Вика", "inspector": "Инспектор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = "Cues 157-159. Victoria escorts the sanitary inspector from the dining hall into the kitchen."

INTRO = (
    "Having completed an inspection of the pristine dining area, Victoria leads the stern sanitary inspector toward the kitchen. "
    "While Victoria attempts to maintain an upbeat and confident tone, the inspector makes it clear that standards are uncompromising. "
    "Let's listen to their formal conversation in Russian first."
)

STORY = [
    ("anya", "Проходите, пожалуйста, вот и наша кухня.", "Come in, please, here is our kitchen.",
     [(157, "А вот и наша кухня"), (158, "Прошу вас")], ""),
    ("inspector", "По залу у меня претензий нет.", "Regarding the hall, I have no complaints.",
     [(158, "по залу у меня никаких претензий нет")], ""),
    ("anya", "Мы строго следим за чистотой везде.", "We strictly monitor cleanliness everywhere.",
     [], ""),
    ("inspector", "Теперь посмотрим на вашу кухню внимательно.", "Now let's look at your kitchen carefully.",
     [(159, "Посмотрим вашу кухню")], ""),
    ("anya", "У нас здесь работают лучшие повара.", "We have the best cooks working here.",
     [], ""),
    ("inspector", "Меня интересуют только санитарные правила.", "I am interested only in sanitary rules.",
     [], ""),
    ("anya", "Все сотрудники носят чистую форму.", "All employees wear a clean uniform.",
     [], ""),
    ("inspector", "Я сам проверю каждое рабочее место.", "I myself will check every workstation.",
     [], ""),
    ("anya", "Наш шеф-повар лично всё контролирует.", "Our head chef personally oversees everything.",
     [], ""),
    ("inspector", "На кухне нельзя нарушать правила.", "In the kitchen one must not violate rules.",
     [], ""),
    ("anya", "Вы можете увидеть всё сами.", "You can see everything yourself.",
     [], ""),
    ("inspector", "Тогда начинаем полную санитарную проверку.", "Then we begin a full sanitary inspection.",
     [], ""),
    ("anya", "Добро пожаловать на нашу кухню!", "Welcome to our kitchen!",
     [], ""),
]

OPENER = "Let's examine the polite yet tense exchange between Victoria and the inspector."

WALK = [
    (0, None,
     "'Come in, please, here is our kitchen.' The polite imperative verb welcomes the guest, followed by a demonstrative phrase introducing the location."),
    (1, None,
     "'Regarding the hall, I have no complaints.' The prepositional phrase sets the topic, followed by the negative particle governing the genitive case."),
    (3, None,
     "'Now let's look at your kitchen carefully.' The future inclusive form expresses shared action, with the adverb placed at the end for emphasis."),
    (7, None,
     "'I myself will check every workstation.' The emphatic pronoun underscores personal oversight, governing the accusative noun phrase."),
]

TRANSITION = "Okay, let's hear the formal dialogue once more."

OUTRO = (
    "Now you understand how formal inspections are conducted in upscale restaurants. "
    "Listen for these official phrases next time you watch the episode."
)

CLOSING = ("anya", "Надеюсь, проверка пройдёт без проблем.")
