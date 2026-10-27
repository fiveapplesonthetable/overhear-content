ID = "kukhnya-s02e01-scene-17"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 17
TITLE = "Секретный ингредиент  (The Secret Ingredient)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anja": "anja", "angelina": "angelina"}
LABELS = {"anya": "Шеф", "anja": "Лёва", "angelina": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = "Scene 17"

INTRO = "The chef tastes the spiked tea and immediately recognizes the hidden alcohol. He praises his sous-chef for the clever trick while Kostya delivers a note to Victoria."

STORY = [
    ("anya", "Отличный чай!",
     "Excellent tea!",
     [(233, 'Чай. Чай.')], "adapted"),
    ("anya", "А что это за чай-то?",
     "And what kind of tea is this?",
     [(234, 'А что за чай-то')], "adapted"),
    ("anja", "Это Сенча.",
     "This is Sencha.",
     [(235, 'Сенча')], "adapted"),
    ("anya", "Молодцы, действуем по нашему плану.",
     "Good job, we are acting according to our plan.",
     [(236, 'Молодцы. Действуем по плану.')], "adapted"),
    ("anja", "Давай, Костян, давай, давай!",
     "Come on, Kostyan, come on, come on!",
     [(237, 'Давай, Костян, давай, давай, давай.')], "adapted"),
    ("angelina", "Всё понятно.",
     "Everything is understood.",
     [(238, 'Понятно.')], "adapted"),
    ("anja", "Займись седьмым столиком, пожалуйста.",
     "Take care of the seventh table, please.",
     [(238, 'Займи седьмым столиком, пожалуйста.')], "adapted"),
    ("angelina", "Виктория Сергеевна, это записка вам.",
     "Victoria Sergeyevna, this is a note for you.",
     [(239, 'Виктория Сергеевна, записка вам.')], "adapted"),
    ("anya", "Этот чай очень хорошо успокаивает.",
     "This tea calms very well.",
     [], "new"),
    ("anja", "Я рад, что вам понравилось.",
     "I am glad that you liked it.",
     [], "new"),
    ("anya", "Заварите мне ещё одну чашку.",
     "Brew me one more cup.",
     [], "new"),
    ("anja", "Сейчас всё сделаем.",
     "We will do everything now.",
     [], "new"),
    ("angelina", "А от кого эта записка?",
     "And from whom is this note?",
     [], "new"),
    ("anja", "Просто передай её Виктории Сергеевне.",
     "Just pass it to Victoria Sergeyevna.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Excellent tea!' -- ENG The chef is pleasantly surprised by the delicious alcoholic taste."),
    (1, None,
     "'And what kind of tea is this?' -- ENG He playfully asks about the specific variety of the drink."),
    (2, None,
     "'This is Sencha.' -- ENG The sous-chef replies with the name of a Japanese green tea."),
    (3, None,
     "'Good job, we are acting according to our plan.' -- ENG The boss approves of their clever rule-breaking strategy."),
    (4, None,
     "'Come on, Kostyan, come on, come on!' -- ENG Lyova encourages the bartender to hurry up with his tasks."),
    (5, None,
     "'Everything is understood.' -- ENG Kostya confirms that he has heard the instructions clearly."),
    (6, None,
     "'Take care of the seventh table, please.' -- ENG The sous-chef directs the bartender to serve waiting customers."),
    (7, None,
     "'Victoria Sergeyevna, this is a note for you.' -- ENG Kostya hands a folded piece of paper to the manager."),
    (8, None,
     "'This tea calms very well.' -- ENG The chef notes the immediate relaxing effect of the alcohol."),
    (9, None,
     "'I am glad that you liked it.' -- ENG Lyova is relieved that his risky trick was successful."),
    (10, None,
     "'Brew me one more cup.' -- ENG The boss demands a refill of his favorite new beverage."),
    (11, None,
     "'We will do everything now.' -- ENG The loyal assistant rushes to prepare another spiked drink."),
    (12, None,
     "'And from whom is this note?' -- ENG The bartender asks a question about the mysterious message."),
    (13, None,
     "'Just pass it to Victoria Sergeyevna.' -- ENG He is told to simply deliver the paper without asking questions."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "The kitchen staff successfully manages the boss's temper, allowing the restaurant service to continue smoothly without any further screaming."
CLOSING = ("anja", "Просто передай её Виктории Сергеевне.")
