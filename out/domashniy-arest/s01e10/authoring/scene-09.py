ID = "domashniy-arest-s01e10-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 9
TITLE = "Примерка костюма  (Fitting the Costume)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 258-267. Nina asks Samsonov to help thread the needle so she can adjust the kids' theatrical costume. "
    "As Samsonov inspects the costume, they exchange awkward domestic banter."
)

INTRO = (
    "In this scene, Samsonov and Nina are preparing the children's theatrical costumes in their communal apartment. "
    "Nina struggles to thread her needle and asks Samsonov for domestic assistance. "
    "As they inspect the oversized stage outfit, their conversation carries subtle layers of marital tension and humor. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("nina", "Кто мне вставит нитку в иголку?",
     "Who will thread the needle for me?",
     [(257, "кто мне вставит"), (258, "нитку в иголку")], ""),
    ("nina", "Вот папа нам сейчас и поможет.",
     "Dad will help us right now.",
     [(259, "А вот папа и вставит")], ""),
    ("anya", "Давай сюда, я быстро вставлю.",
     "Give it here, I will thread it quickly.",
     [(260, "Ну да")], ""),
    ("nina", "Сегодня как раз твоя очередь помогать.",
     "Today is precisely your turn to help.",
     [(261, "Сегодня же папина очередь")], ""),
    ("anya", "Ну вот, нитка уже на месте.",
     "Well, the thread is already in place.",
     [], "Samsonov threads the needle"),
    ("nina", "Спасибо. А как тебе костюм?",
     "Thanks. And how do you like the costume?",
     [(262, "Ну как тебе")], ""),
    ("anya", "Сверху костюм выглядит просто супер!",
     "On top the costume looks simply super!",
     [(263, "Сверху вообще супер")], ""),
    ("nina", "А снизу я бы немного изменила.",
     "And on the bottom I would change a bit.",
     [(264, "А снизу я бы, конечно, изменила")], ""),
    ("anya", "Зачем там что-то менять?",
     "Why change anything there?",
     [], "Samsonov asks why alter it"),
    ("nina", "Совсем чуть-чуть, самую малость.",
     "Just a tiny bit, the bare minimum.",
     [(265, "Но чуть-чуть"), (266, "Самой малость")], ""),
    ("anya", "Штаны слишком длинные для Славика?",
     "Are the pants too long for Slavik?",
     [], "checking fit"),
    ("nina", "Да, надо подогнуть разок-другой.",
     "Yes, need to hem it a time or two.",
     [(267, "Разок-другой")], ""),
    ("anya", "Главное, чтобы дети хорошо выступили.",
     "The main thing is that the children perform well.",
     [], "focus on performance"),
    ("nina", "Мы сделаем всё красиво, не волнуйся.",
     "We will make everything beautiful, don't worry.",
     [], "reassurance"),
]

OPENER = (
    "Now let's examine the domestic costume preparation line by line. "
    "Nina and Samsonov discuss the children's stage costumes."
)

WALK = [
    (0, None,
     "'Who will thread the needle for me?' Nina asks for practical domestic assistance."),
    (1, None,
     "'Dad will help us right now.' Nina delegates the small chore to Samsonov."),
    (2, None,
     "'Give it here, I will thread it quickly.' Samsonov takes the needle with an imperative particle."),
    (3, None,
     "'Today is precisely your turn to help.' Nina emphasizes domestic duty with the noun for turn."),
    (4, None,
     "'Well, the thread is already in place.' Samsonov reports success with a prepositional phrase."),
    (5, None,
     "'Thanks. And how do you like the costume?' Nina asks for his opinion on the theatrical outfit."),
    (6, None,
     "'On top the costume looks simply super!' Samsonov praises the upper half of the outfit."),
    (7, None,
     "'And on the bottom I would change a bit.' Nina uses the conditional mood to suggest adjustments."),
    (8, None,
     "'Why change anything there?' Samsonov questions the need for further alterations."),
    (9, None,
     "'Just a tiny bit, the bare minimum.' Nina minimizes the required tailoring effort."),
    (10, None,
     "'Are the pants too long for Slavik?' Samsonov asks about the fit of their son's trousers."),
    (11, None,
     "'Yes, need to hem it a time or two.' Nina describes hemming the fabric with an idiom."),
    (12, None,
     "'The main thing is that the children perform well.' Samsonov emphasizes the theatrical outcome."),
    (13, None,
     "'We will make everything beautiful, don't worry.' Nina reassures him with a negative imperative."),
]

TRANSITION = "Now let's listen to the costume preparation conversation once more without pauses."
OUTRO = (
    "Working together on the costumes brings temporary domestic cooperation between Samsonov and Nina. "
    "In the next scene, lingering suspicions of infidelity resurface."
)
CLOSING = ("nina", "Мы сделаем всё красиво, не волнуйся.")
