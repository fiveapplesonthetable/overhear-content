ID = "kukhnya-s01e11-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 2
TITLE = "Тайный критик  (The Secret Critic)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 24-40. Victoria enters the kitchen to announce that an anonymous international restaurant critic "
    "is visiting Claude Monet today."
)

INTRO = (
    "Restaurant administrator Victoria marches into the busy kitchen with urgent news from owner Dmitry Nagiev. "
    "An anonymous food critic writing for prestigious international guidebooks is dining at Claude Monet today, "
    "prompting Victoria to demand flawless discipline from the cooks. Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Внимание всем! У меня важная информация.",
     "Attention everyone! I have important information.",
     [(24, "Внимание! У меня важная информация.")], "adapted"),
    ("chef", "Вика, говори быстрее, у нас много заказов.",
     "Vika, speak faster, we have a lot of orders.",
     [(25, "У тебя минута")], "adapted"),
    ("anya", "Только что звонил сам Дмитрий Владимирович.",
     "Dmitry Vladimirovich himself just called.",
     [(26, "Звонил Дмитрий Владимирович.")], "adapted"),
    ("chef", "И что сказал наш уважаемый хозяин?",
     "And what did our respected owner say?",
     [(27, "Сообщил, что")], "adapted"),
    ("anya", "К нам сегодня приедет ресторанный критик.",
     "A restaurant critic will come to us today.",
     [(27, "к нам сегодня заедет."), (29, "Ресторанный критик.")], "adapted"),
    ("chef", "Мы накормим его вкусным горячим обедом.",
     "We will feed him a delicious hot lunch.",
     [(30, "в чем проблема?")], "adapted"),
    ("anya", "Никто не знает, как он выглядит.",
     "Nobody knows what he looks like.",
     [(32, "никто не знает, как он выглядит.")], "adapted"),
    ("chef", "Значит, готовим каждое блюдо идеально точно.",
     "That means we cook each dish with perfect precision.",
     [], "new"),
    ("anya", "И не пускай сегодня Макса на кухню.",
     "And do not let Max into the kitchen today.",
     [(36, "не допускай сегодня к работе")], "adapted"),
    ("chef", "А почему новый повар не должен работать?",
     "And why should the new cook not work?",
     [(36, "новенького."), (37, "Это еще почему?")], "adapted"),
    ("anya", "Потому что этот парень приносит сплошные проблемы.",
     "Because this guy brings constant problems.",
     [(38, "Потому что это и сплошная")], "adapted"),
    ("chef", "Хорошо, Макс будет мыть грязную посуду.",
     "Fine, Max will wash dirty dishes.",
     [], "new"),
    ("anya", "Сегодня на кухне нужен полный порядок.",
     "Today complete order is needed in the kitchen.",
     [(39, "А мне сегодня проблемы не нужны.")], "adapted"),
]

OPENER = "Now let's examine this kitchen announcement line by line."

WALK = [
    (0, None,
     "'Attention everyone! I have important information.' -- Victoria demands silence in the kitchen."),
    (1, None,
     "'Vika, speak faster, we have a lot of orders.' -- The chef urges her to hurry up."),
    (2, None,
     "'Dmitry Vladimirovich himself just called.' -- She announces a phone call from the owner."),
    (3, None,
     "'And what did our respected owner say?' -- Barinov asks for details about the phone call."),
    (4, None,
     "'A restaurant critic will come to us today.' -- Victoria drops the stressful announcement."),
    (5, None,
     "'We will feed him a delicious hot lunch.' -- The chef plans to win him over with food."),
    (6, None,
     "'Nobody knows what he looks like.' -- She warns that the reviewer remains anonymous."),
    (7, None,
     "'That means we cook each dish with perfect precision.' -- Barinov orders culinary excellence in the kitchen."),
    (8, None,
     "'And do not let Max into the kitchen today.' -- Victoria instructs him to sideline the novice."),
    (9, None,
     "'And why should the new cook not work?' -- The chef questions her harsh instruction."),
    (10, None,
     "'Because this guy brings constant problems.' -- She describes Max as a walking disaster."),
    (11, None,
     "'Fine, Max will wash dirty dishes.' -- Barinov assigns him to kitchen scullery duty."),
    (12, None,
     "'Today complete order is needed in the kitchen.' -- Victoria insists on total perfection."),
]

TRANSITION = "Now let's listen to the kitchen announcement again without interruption."
OUTRO = (
    "With strict instructions delivered and Max relegated to the dish pit, the kitchen brigade "
    "braces itself for the arrival of the mysterious culinary inspector."
)
CLOSING = ("anya", "Сегодня на кухне нужен полный порядок.")
