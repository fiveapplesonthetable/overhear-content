ID = "kukhnya-s01e05-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 2
TITLE = "Мечты о будущем  (Dreams of the Future)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja"}
LABELS = {"anya": "Настя", "sasha": "Саша"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 16-22. In the waitstaff locker room, waitress Nastya excitedly confides in Sasha "
    "about her kiss with Max, already imagining their romantic future and beautiful children."
)

INTRO = (
    "In the restaurant locker room, waitress Nastya glows with romantic excitement. "
    "She confides in fellow waitress Sasha about yesterday's unexpected kiss with Max. "
    "Sasha is stunned by how quickly Nastya has planned out their future together, including children and family life. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("sasha", "Настя, у вас с Максом всё серьёзно?",
     "Nastya, is everything serious between you and Max?",
     [(16, "у вас прям всё серьёзно")], "adapted"),
    ("anya", "Да, мы вчера даже поцеловались.",
     "Yes, yesterday we even kissed.",
     [(17, "Да"), (18, "Мы вчера даже поцеловались")], "adapted"),
    ("sasha", "Правда? И как это произошло?",
     "Really? And how did that happen?",
     [], "new"),
    ("anya", "Это было невероятно романтично!",
     "It was incredibly romantic!",
     [(19, "Это было так романтично")], "adapted"),
    ("sasha", "Неужели ты влюбилась в него?",
     "Did you really fall in love with him?",
     [], "new"),
    ("anya", "Он такой добрый и внимательный парень.",
     "He is such a kind and attentive guy.",
     [], "new"),
    ("sasha", "Вы ведь знакомы всего одну неделю.",
     "After all, you have only known each other one week.",
     [], "new"),
    ("anya", "Настоящая любовь не знает времени.",
     "True love knows no time.",
     [], "new"),
    ("anya", "Представляешь, какие у нас будут красивые дети!",
     "Imagine what beautiful children we will have!",
     [(22, "Представляешь, какие у нас дети красивые будут")], "adapted"),
    ("sasha", "Ты уже думаешь о детях?!",
     "Are you already thinking about children?!",
     [], "new"),
    ("anya", "Конечно, мы создадим прекрасную семью.",
     "Of course, we will create a wonderful family.",
     [], "new"),
    ("sasha", "А Макс знает о твоих планах?",
     "And does Max know about your plans?",
     [], "new"),
    ("anya", "Скоро мы обязательно всё обсудим.",
     "Soon we will definitely discuss everything.",
     [], "new"),
]

OPENER = "Now let's examine Nastya and Sasha's romantic conversation line by line."

WALK = [
    (0, None,
     "'Nastya, is everything serious between you and Max?' Sasha inquires about the relationship with an adjective."),
    (1, None,
     "'Yes, yesterday we even kissed.' Nastya confirms the spark using an emphatic particle and reflexive verb."),
    (2, None,
     "'Really? And how did that happen?' Sasha reacts with curiosity using a question word and past verb."),
    (3, None,
     "'It was incredibly romantic!' Nastya describes her feelings with an intensifier adverb."),
    (4, None,
     "'Did you really fall in love with him?' Sasha asks in surprise using a particle and past reflexive verb."),
    (5, None,
     "'He is such a kind and attentive guy.' Nastya praises Max with descriptive adjectives and a noun."),
    (6, None,
     "'After all, you have only known each other one week.' Sasha points out the brief timeline with short predicate adjectives."),
    (7, None,
     "'True love knows no time.' Nastya replies with a poetic statement about timeless affection."),
    (8, None,
     "'Imagine what beautiful children we will have!' Nastya projects ahead using a future verb and plural noun."),
    (9, None,
     "'Are you already thinking about children?!' Sasha is astonished by the speed of her friend's plans."),
    (10, None,
     "'Of course, we will create a wonderful family.' Nastya speaks with certainty using a future perfective verb."),
    (11, None,
     "'And does Max know about your plans?' Sasha asks whether the prospective groom has been consulted."),
    (12, None,
     "'Soon we will definitely discuss everything.' Nastya resolves the question with an adverb of certainty."),
]

TRANSITION = "Now let's listen to the waitresses' dialogue again without interruption."
OUTRO = (
    "Nastya heads off on her shift daydreaming about wedding bells, completely unaware of Max's panic. "
    "In the next scene, Chef Viktor Barinov rallies the kitchen staff to sell off thawed fish."
)
CLOSING = ("anya", "Скоро мы обязательно всё обсудим.")
