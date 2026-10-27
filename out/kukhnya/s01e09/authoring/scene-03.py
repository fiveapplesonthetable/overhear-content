ID = "kukhnya-s01e09-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 3
TITLE = "Занят с дочерью  (Busy with His Daughter)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Лёва", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 84-86. In the office, sous-chef Lyova urges Chef Barinov to prepare two urgent VIP dishes, "
    "but Barinov refuses because he is busy playing with his daughter."
)

INTRO = (
    "In his private office at Claude Monet, Chef Viktor Barinov is supposed to be managing the kitchen during a busy "
    "lunch service. When sous-chef Lyova rushes in with urgent orders from VIP guests, Barinov bluntly dismisses him, "
    "insisting that spending quality time with his visiting daughter comes before any restaurant dish. Let's listen "
    "to their conversation in Russian first."
)

STORY = [
    ("anya", "Шеф, вам нужно срочно на кухню.",
     "Chef, you need to go to the kitchen urgently.",
     [], "new"),
    ("chef", "Лёва, не видишь, я занят?",
     "Lyova, don't you see I am busy?",
     [(85, "не видишь, я занят.")], "adapted"),
    ("anya", "Гости в зале ждут особые блюда.",
     "Guests in the dining room are waiting for special dishes.",
     [(84, "два блюда от шефа")], "adapted"),
    ("chef", "Я сейчас играю с моей дочерью.",
     "I am playing with my daughter right now.",
     [(86, "Я с дочерью играю.")], "adapted"),
    ("anya", "Но это важный заказ от шефа.",
     "But this is an important order from the chef.",
     [(84, "блюда от шефа")], "adapted"),
    ("chef", "Ты прекрасный повар и справишься сам.",
     "You are a wonderful cook and will manage yourself.",
     [], "new"),
    ("anya", "Они хотят именно ваше фирменное мясо.",
     "They want specifically your signature meat.",
     [], "new"),
    ("chef", "Приготовь наше обычное вкусное мясо сам.",
     "Cook our usual tasty meat yourself.",
     [], "new"),
    ("anya", "А если гостям не понравится вкус?",
     "And what if the guests do not like the taste?",
     [], "new"),
    ("chef", "Добавь немного соли и свежего перца.",
     "Add a little salt and fresh pepper.",
     [], "new"),
    ("anya", "Шеф, на кухне начинается настоящий хаос.",
     "Chef, real chaos is starting in the kitchen.",
     [], "new"),
    ("chef", "Закрой дверь и наведите там порядок.",
     "Close the door and establish order there.",
     [], "new"),
    ("anya", "Хорошо, шеф, я всё сделаю сам.",
     "Alright, chef, I will do everything myself.",
     [], "new"),
]

OPENER = "Now let's examine Lyova and Chef Barinov's office exchange line by line."

WALK = [
    (0, None,
     "'Chef, you need to go to the kitchen urgently.' -- Sous-chef Lyova pleads with Barinov to return to the kitchen line."),
    (1, None,
     "'Lyova, don't you see I am busy?' -- The chef snaps back that he is preoccupied with important personal business."),
    (2, None,
     "'Guests in the dining room are waiting for special dishes.' -- Lyova reports that diners have placed special orders."),
    (3, None,
     "'I am playing with my daughter right now.' -- Barinov explains that playing games with young Alisa takes priority."),
    (4, None,
     "'But this is an important order from the chef.' -- The sous-chef emphasizes that guests specifically requested the head chef's personal cooking."),
    (5, None,
     "'You are a wonderful cook and will manage yourself.' -- Barinov compliments Lyova's skill to delegate the task entirely."),
    (6, None,
     "'They want specifically your signature meat.' -- Lyova insists that only the master chef's technique will satisfy the patrons."),
    (7, None,
     "'Cook our usual tasty meat yourself.' -- Barinov tells him to prepare the standard restaurant recipe without him."),
    (8, None,
     "'And what if the guests do not like the taste?' -- The anxious sous-chef worries about negative guest feedback."),
    (9, None,
     "'Add a little salt and fresh pepper.' -- Barinov offers minimal culinary advice to finish the seasoning."),
    (10, None,
     "'Chef, real chaos is starting in the kitchen.' -- Lyova warns that tickets are piling up and disorder is spreading."),
    (11, None,
     "'Close the door and establish order there.' -- The chef commands him to shut the office door and restore kitchen discipline."),
    (12, None,
     "'Alright, chef, I will do everything myself.' -- Resigned to the situation, Lyova accepts full responsibility for the shift."),
]

TRANSITION = "Now let's listen to the office conversation again without interruption."
OUTRO = (
    "Leaving Chef Barinov happily playing games with Alisa behind closed doors, a flustered Lyova returns to the line "
    "to manage the rush and prepare the specialty dishes on his own."
)
CLOSING = ("anya", "Хорошо, шеф, я всё сделаю сам.")
