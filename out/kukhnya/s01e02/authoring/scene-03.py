ID = "kukhnya-s01e02-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = "Ошибка природы  (Freak of Nature)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Настя", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 23-26. Waitress Nastya rushes into the kitchen to ask Chef Viktor Barinov what a female head chef is called. "
    "Barinov chauvinistically dubs female chefs a 'freak of nature', only for Nastya to reveal that the head chef "
    "of their rival restaurant is currently sitting in their dining room."
)

INTRO = (
    "Waitress Nastya bursts unexpectedly into the kitchen, catching Chef Viktor Barinov completely off guard. "
    "She innocently asks how to refer to a female head chef, prompting Barinov to scoff that women in high culinary positions are an anomaly. "
    "Nastya then drops the punchline: that exact rival chef has just taken a seat in Claude Monet's dining room. "
    "Let's listen to their fast-paced exchange in Russian first."
)

STORY = [
    ("chef", "Настя, ты меня когда-нибудь доведёшь!",
     "Nastya, you will drive me crazy one of these days!",
     [(23, "Настя, я из тебя когда-нибудь инфаркт получил")], "adapted"),
    ("chef", "Нельзя так неожиданно вбегать на кухню.",
     "One must not run into the kitchen so unexpectedly.",
     [], "new"),
    ("anya", "Шеф, у меня очень срочный вопрос.",
     "Chef, I have a very urgent question.",
     [], "new"),
    ("anya", "Как правильно называется шеф-повар женщина?",
     "What is the correct term for a female chef?",
     [(24, "как правильно называется шеф-повар женщина")], ""),
    ("chef", "Женщина шеф-повар — это ошибка природы.",
     "A female head chef is a freak of nature.",
     [(25, "Ошибка природы")], "adapted"),
    ("anya", "Почему вы так несправедливо говорите?",
     "Why do you speak so unfairly?",
     [], "new"),
    ("chef", "Потому что настоящая кухня — мужское дело!",
     "Because a real kitchen is a man's business!",
     [], "new"),
    ("anya", "Тогда у нас сидит ошибка природы.",
     "Then a freak of nature is sitting in our hall.",
     [(26, "у нас в зале сидит ошибка природы")], "adapted"),
    ("chef", "Где именно сидит эта женщина?",
     "Where exactly is this woman sitting?",
     [], "new"),
    ("anya", "Она сидит в нашем главном зале.",
     "She is sitting in our main dining hall.",
     [(26, "у нас в зале")], "adapted"),
    ("chef", "Откуда пришла эта странная гостья?",
     "Where did this strange guest come from?",
     [], "new"),
    ("anya", "Это шеф-повар из соседнего ресторана!",
     "This is the head chef from the neighboring restaurant!",
     [(26, "из соседнего ресторана")], ""),
    ("chef", "Что конкуренты забыли в моём ресторане?",
     "What do the rivals want in my restaurant?",
     [(27, "Что она здесь вынюхивает")], "adapted"),
]

OPENER = "Now let's examine Chef Barinov and Nastya's kitchen exchange line by line."

WALK = [
    (0, None,
     "'Nastya, you will drive me crazy one of these days!' The startled chef vents with a future perfective verb."),
    (1, None,
     "'One must not run into the kitchen so unexpectedly.' Barinov sets boundaries with a negative modal adverb and infinitive."),
    (2, None,
     "'Chef, I have a very urgent question.' Nastya introduces her pressing query with a genitive possession clause."),
    (3, None,
     "'What is the correct term for a female chef?' The waitress asks about culinary vocabulary with a reflexive present verb."),
    (4, None,
     "'A female head chef is a freak of nature.' Barinov responds chauvinistically with an emphatic demonstrative predicate."),
    (5, None,
     "'Why do you speak so unfairly?' Nastya challenges his statement with an adverb of manner."),
    (6, None,
     "'Because a real kitchen is a man's business!' The chef justifies his prejudice with an explanatory conjunction."),
    (7, None,
     "'Then a freak of nature is sitting in our hall.' Nastya turns his exact words back on him with an introductory particle."),
    (8, None,
     "'Where exactly is this woman sitting?' Barinov demands location details with an interrogative particle phrase."),
    (9, None,
     "'She is sitting in our main dining hall.' Nastya specifies the location using prepositional singular nouns."),
    (10, None,
     "'Where did this strange guest come from?' The chef asks about her origin using a past tense verb of motion."),
    (11, None,
     "'This is the head chef from the neighboring restaurant!' Nastya reveals the visitor's identity with a genitive modifier."),
    (12, None,
     "'What do the rivals want in my restaurant?' The paranoid chef wonders about espionage using a rhetorical past question."),
]

TRANSITION = "Now let's listen to Chef Barinov and Nastya's kitchen conversation again without interruption."
OUTRO = (
    "Barinov scrambles to discover why the rival chef is spying on Claude Monet. "
    "In the next scene, the kitchen prepares a suspicious welcome for the unwanted guest."
)
CLOSING = ("chef", "Что конкуренты забыли в моём ресторане?")
