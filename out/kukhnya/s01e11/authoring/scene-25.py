"""Scene 25 — The Critic's Review (s01e11, 00:21:37–00:23:33)."""

ID = "kukhnya-s01e11-scene-25"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 25
TITLE = "Отзыв критика  (The Critic's Review)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nagiev": "anja",
    "mother": "angelina",
}

LABELS = {
    "anya": "Шеф",
    "nagiev": "Нагиев",
    "mother": "Мама",
}

INTRO = (
    "After enduring a stern lecture from his mother in the restaurant kitchen, Chef Barinov is interrupted by a frantic Nagiyev. "
    "To everyone's disbelief, the televised food review awards Claude Monet nine out of ten, heaping special praise upon Kostya's professional integrity."
)

STORY = [
    ("mother", "Витя, я выражаю тебе своё крайнее возмущение!",
     "Vitya, I express to you my extreme outrage!",
     [(324, "Чтобы выразить тебе свое крайнее возмущение.")], "Mother scolds"),

    ("mother", "Я глубоко разочарована плохим сервисом в ресторане.",
     "I am deeply disappointed by the bad service in the restaurant.",
     [(326, "И глубоко разочарована.")], "Mother complains"),

    ("anya", "Мама, не кричи здесь, мы заняты работой.",
     "Mom, do not shout here, we are busy with work.",
     [], "Barinov pleads"),

    ("mother", "Чтобы в двенадцать часов ровно был дома!",
     "Be home at twelve o'clock sharp!",
     [(334, "В 12 часов, чтобы был дома.")], "Mother orders strictly"),

    ("nagiev", "Шеф, скорее включай телевизор, там кулинарный критик!",
     "Chef, turn on the TV quickly, the food critic is on!",
     [], "Nagiyev runs in"),

    ("anya", "Неужели критик уже выпустил свой разгромный отзыв?",
     "Has the critic already released his devastating review?",
     [], "Barinov panics"),

    ("nagiev", "Он говорит, что наше главное достоинство — принципиальность.",
     "He says that our main virtue is integrity.",
     [(340, "Главным достоинством ресторана является особая принципиальность всего коллектива.")], "Nagiyev listens closely"),

    ("anya", "Правда? А что он сказал про кухню?",
     "Really? And what did he say about the kitchen?",
     [], "Barinov asks eagerly"),

    ("nagiev", "Он назвал всю нашу еду просто восхитительной!",
     "He called all our food simply delicious!",
     [(346, "Она здесь просто восхитительна")], "Nagiyev beams"),

    ("nagiev", "А бармена Костю он назвал настоящим профессионалом.",
     "And he called bartender Kostya a real professional.",
     [(347, "Отдельно я бы отметил бармена Константина."),
      (348, "Это не просто профессионал своего дела, но еще и очень хороший человек.")], "Nagiyev quotes critic"),

    ("nagiev", "Критик поставил ресторану девять баллов из десяти!",
     "The critic gave the restaurant nine points out of ten!",
     [(349, "В целом я бы поставил этому ресторану 9 баллов из 10.")], "Nagiyev announces score"),

    ("anya", "Девять из десяти? Это же невероятный успех!",
     "Nine out of ten? That is an incredible success!",
     [(350, "9 из 10.")], "Barinov rejoices"),

    ("nagiev", "Витя, срочно верни Костю обратно на работу!",
     "Vitya, urgently bring Kostya back to work!",
     [(351, "Бармена надо вернуть.")], "Nagiyev commands"),
]

OPENER = "Let's watch Barinov's mother lecture her grown son before Nagiyev bursts in with the astonishing television review."

WALK = [
    (0, None,
     "'Vitya, I express to you my extreme outrage!' Barinov's formidable mother scolds him in the kitchen."),
    (1, None,
     "'I am deeply disappointed by the bad service in the restaurant.' She lists her severe grievances."),
    (2, None,
     "'Mom, do not shout here, we are busy with work.' The embarrassed head chef whispers pleadingly."),
    (3, None,
     "'Be home at twelve o'clock sharp!' She lays down an uncompromising curfew before departing."),
    (4, None,
     "'Chef, turn on the TV quickly, the food critic is on!' Nagiyev rushes in waving his hands."),
    (5, None,
     "'Has the critic already released his devastating review?' Barinov braces for public disaster."),
    (6, None,
     "'He says that our main virtue is integrity.' Nagiyev quotes the critic's surprisingly glowing words."),
    (7, None,
     "'Really? And what did he say about the kitchen?' Barinov listens with breathless curiosity."),
    (8, None,
     "'He called all our food simply delicious!' The restaurant owner beams with pure delight."),
    (9, None,
     "'And he called bartender Kostya a real professional.' The critic praises the brave bartender."),
    (10, None,
     "'The critic gave the restaurant nine points out of ten!' Nagiyev announces the spectacular score."),
    (11, None,
     "'Nine out of ten? That is an incredible success!' Barinov celebrates the miraculous outcome."),
    (12, None,
     "'Vitya, urgently bring Kostya back to work!' Nagiyev orders an instant reversal of the dismissal."),
]

TRANSITION = "Now let's listen to the comical maternal scolding and the triumphant broadcast review once more."

OUTRO = "Saved by Kostya's unwavering honesty, Claude Monet triumphs as Nagiyev insists on the bartender's immediate return."

CLOSING = ("nagiev", "Витя, срочно верни Костю обратно на работу!")
