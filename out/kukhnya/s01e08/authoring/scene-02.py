ID = "kukhnya-s01e08-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 2
TITLE = "Спор в прямом эфире  (On-Air Debate)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Елена", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 20-28. On the live morning TV show, Chef Barinov prepares a lamb specialty "
    "and stirs controversy by declaring that women are unfit to be head chefs."
)

INTRO = (
    "Live on the morning culinary broadcast 'A Tasty Morning', Chef Viktor Barinov demonstrates preparing "
    "a delicate young lamb dish. As the cameras roll, Barinov provokes rival head chef Elena Sokolova "
    "by claiming that male chefs inherently prepare meat better and asserting that women lack the stamina "
    "for professional restaurant leadership. Let's listen to their heated television exchange in Russian first."
)

STORY = [
    ("chef", "Сегодня я приготовлю мясо молодого ягнёнка.",
     "Today I will prepare meat of a young lamb.",
     [(20, "Я приготовлю сегодня жигой гненка")], "adapted"),
    ("anya", "Какое интересное и сложное мясное блюдо!",
     "What an interesting and complex meat dish!",
     [(22, "Это блюдо")], "adapted"),
    ("chef", "Такое блюдо лучше всего готовят мужчины.",
     "Men prepare such a dish best of all.",
     [(22, "лучше всего удается поварам-мужчинам")], "adapted"),
    ("anya", "Почему вы говорите такие странные вещи?",
     "Why do you say such strange things?",
     [(28, "вы действительно считаете, что")], "adapted"),
    ("chef", "Женщины часто режут мясо совсем неправильно.",
     "Women often cut meat completely incorrectly.",
     [(25, "а женщинам что-то норовят поперек")], "adapted"),
    ("anya", "Вы просто не уважаете женский талант.",
     "You simply do not respect female talent.",
     [], "new"),
    ("chef", "Женщина не способна стать великим шефом.",
     "A woman is not capable of becoming a great chef.",
     [(26, "женщина априори не может быть хорошим поваром")], "adapted"),
    ("anya", "Я руковожу кухней известного ресторана Аркабалено!",
     "I run the kitchen of the famous Arcobaleno restaurant!",
     [], "new"),
    ("chef", "Настоящий шеф-повар требует сильной воли.",
     "A real head chef requires strong willpower.",
     [(27, "Женщина на кухне — это кухарка")], "adapted"),
    ("anya", "У меня есть опыт и сильная воля.",
     "I have experience and strong willpower.",
     [], "new"),
    ("chef", "Для вас кухня остаётся обычной работой.",
     "For you the kitchen remains an ordinary job.",
     [], "new"),
    ("anya", "Кухня — это вся моя жизнь, Виктор!",
     "The kitchen is my whole life, Viktor!",
     [], "new"),
    ("chef", "Мы скоро проверим ваши смелые слова.",
     "We will soon check your bold words.",
     [], "new"),
]

OPENER = "Now let's examine Barinov and Elena's on-air debate line by line."

WALK = [
    (0, None,
     "'Today I will prepare meat of a young lamb.' Barinov announces his signature recipe with a genitive noun phrase."),
    (1, None,
     "'What an interesting and complex meat dish!' Elena politely observes the culinary demonstration with exclamatory adjectives."),
    (2, None,
     "'Men prepare such a dish best of all.' Barinov injects a controversial gender generalization with a superlative adverb."),
    (3, None,
     "'Why do you say such strange things?' Elena challenges Barinov's bizarre professional commentary."),
    (4, None,
     "'Women often cut meat completely incorrectly.' Barinov criticizes female butchering techniques with a manner adverb."),
    (5, None,
     "'You simply do not respect female talent.' Elena defends women in culinary arts using a present imperfective verb."),
    (6, None,
     "'A woman is not capable of becoming a great chef.' Barinov doubles down on his provocative claim using a short adjective."),
    (7, None,
     "'I run the kitchen of the famous Arcobaleno restaurant!' Elena cites her successful leadership of a premier dining venue."),
    (8, None,
     "'A real head chef requires strong willpower.' Barinov argues for intense emotional toughness using a genitive object."),
    (9, None,
     "'I have experience and strong willpower.' Elena affirms her professional resilience with noun coordinates."),
    (10, None,
     "'For you the kitchen remains an ordinary job.' Barinov questions her genuine culinary dedication."),
    (11, None,
     "'The kitchen is my whole life, Viktor!' Elena passionately asserts her lifelong vocation."),
    (12, None,
     "'We will soon check your bold words.' Barinov issues a quiet challenge with a future verb and accusative noun phrase."),
]

TRANSITION = "Now let's listen to the on-air debate again without interruption."
OUTRO = (
    "Elena bristles at Barinov's arrogant chauvinism, setting the stage for an explosive confrontation "
    "as the live broadcast continues into the commercial break."
)
CLOSING = ("chef", "Мы скоро проверим ваши смелые слова.")
