"""s01e06 scene 12: Строгая проверка (A Strict Inspection)."""

ID = "kukhnya-s01e06-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = "Строгая проверка  (A Strict Inspection)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Инспектор", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = "Cues 160-166. The sanitary inspector questions Chef Barinov about kitchen hazards and open alcohol."

INTRO = (
    "Inside the bustling kitchen, the stern sanitary inspector meticulously scrutinizes every surface alongside a nervous Chef Barinov. "
    "Noticing wet tiles and an open bottle of alcohol sitting right beside the grill station, the inspector delivers a harsh reprimand. "
    "Let's listen to their tense exchange in Russian first."
)

STORY = [
    ("anya", "Скользкий пол — это источник опасности.", "A slippery floor is a source of danger.",
     [(160, "Скользкий пол — это источник опасности для сотрудников")], ""),
    ("chef", "Мы сейчас же вытрем эту воду.", "We will wipe up this water immediately.",
     [], ""),
    ("anya", "Почему у гриля открыта эта бутылка?", "Why is this bottle open by the grill?",
     [(161, "Почему у гриля открыта бутылка с алкоголем")], ""),
    ("chef", "Это вино нужно для мясного соуса.", "This wine is needed for meat sauce.",
     [], ""),
    ("anya", "Понятно, но это всё равно нарушение.", "Understood, but that is still a violation.",
     [(162, "Понятно")], ""),
    ("chef", "Я лично уберу бутылку в шкаф.", "I will personally put the bottle in the cupboard.",
     [], ""),
    ("anya", "Простым штрафом вы здесь не отделаетесь!", "You won't get off with a simple fine here!",
     [(163, "простым штрафом вы здесь не отделаетесь")], ""),
    ("chef", "Поверьте, у нас образцовый ресторан!", "Believe me, we have an exemplary restaurant!",
     [], ""),
    ("anya", "Пойдёмте дальше, я осмотрю склад.", "Let's move on, I will inspect the storage.",
     [(164, "Пойдемте дальше")], ""),
    ("chef", "Прошу вас, идите прямо за мной.", "Please, walk right behind me.",
     [], ""),
    ("anya", "А что находится за этой дверью?", "And what is located behind this door?",
     [(165, "А тут что")], ""),
    ("chef", "Там наш склад для закрытых бутылок.", "There is our storage for unopened bottles.",
     [(166, "Склад алкоголя")], ""),
    ("anya", "Откройте замок, я должен всё увидеть.", "Open the lock, I must see everything.",
     [], ""),
]

OPENER = "Let's observe how the inspector identifies infractions on the kitchen floor."

WALK = [
    (0, None,
     "'A slippery floor is a source of danger.' The demonstrative pronoun links the descriptive subject to the predicate noun phrase."),
    (2, None,
     "'Why is this bottle open by the grill?' The short passive participle agrees with the feminine noun, followed by a prepositional location phrase."),
    (6, None,
     "'You won't get off with a simple fine here!' The instrumental phrase indicates the penalty, used with a perfective reflexive verb."),
    (8, None,
     "'Let's move on, I will inspect the storage.' The inclusive imperative suggests forward movement, followed by a simple future verb."),
]

TRANSITION = "Okay, let's hear the inspection confrontation once more."

OUTRO = (
    "Now you understand how sanitary infractions are discovered and disputed in restaurants. "
    "Listen for these stern phrases next time you watch the episode."
)

CLOSING = ("chef", "Этот инспектор не пропустит ни одной ошибки.")
