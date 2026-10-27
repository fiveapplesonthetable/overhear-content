ID = "kukhnya-s01e04-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = "Собеседование у конкурентов  (An Interview with the Competitor)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "elena": "anja"}
LABELS = {"anya": "Макс", "elena": "Елена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-5. Frustrated by only peeling vegetables and unloading boxes at Claude Monet, "
    "Max secretly attends a job interview with Elena Sokolova, head chef of rival restaurant Arcobaleno."
)

INTRO = (
    "Feeling unappreciated at Claude Monet, Max secretly visits the rival restaurant Arcobaleno across the street. "
    "Head chef Elena Sokolova reviews his résumé and expresses keen interest in taking him onto her kitchen staff. "
    "Encouraged by her praise, Max eagerly awaits her follow-up call. "
    "Let's listen to their interview in Russian first."
)

STORY = [
    ("elena", "Максим, я внимательно прочла ваше резюме.",
     "Maksim, I carefully read your résumé.",
     [(1, "Я прочла резюме")], "adapted"),
    ("anya", "Надеюсь, вам понравился мой опыт.",
     "I hope you liked my experience.",
     [], "new"),
    ("elena", "Вы очень способный и перспективный повар.",
     "You are a very capable and promising cook.",
     [(2, "такого перспективного работника")], "adapted"),
    ("anya", "Спасибо, я действительно хочу многому научиться.",
     "Thank you, I truly want to learn a lot.",
     [], "new"),
    ("elena", "Я с радостью возьму вас на кухню.",
     "I will gladly take you into the kitchen.",
     [(2, "могу взять к себе на кухню")], "adapted"),
    ("anya", "В ресторане Клод Моне меня не ценят.",
     "At the Claude Monet restaurant they do not appreciate me.",
     [(3, "почему в Мане они ценят такие кадры")], "adapted"),
    ("elena", "Я не понимаю, почему они так поступают.",
     "I do not understand why they act like that.",
     [(3, "вообще не понимаю")], "adapted"),
    ("anya", "Там мне дают только чистить овощи.",
     "There they only give me vegetables to peel.",
     [], "new"),
    ("elena", "У нас вы будете готовить сложные блюда.",
     "With us you will cook complex dishes.",
     [], "new"),
    ("anya", "Это именно то, о чём я мечтал!",
     "This is exactly what I dreamed about!",
     [], "new"),
    ("elena", "Вот мои контакты на всякий случай.",
     "Here are my contacts just in case.",
     [(4, "Это мои контакты на всякий случай")], "adapted"),
    ("anya", "Когда мне ожидать вашего звонка?",
     "When should I expect your call?",
     [], "new"),
    ("elena", "Я позвоню вам через пару дней.",
     "I will call you in a couple of days.",
     [(5, "я позвоню вам через пару дней")], "adapted"),
]

OPENER = "Now let's examine Elena Sokolova and Max's interview line by line."

WALK = [
    (0, None,
     "'Maksim, I carefully read your résumé.' Elena opens the interview with a past perfective verb and adverb."),
    (1, None,
     "'I hope you liked my experience.' Max expresses politeness using a past reflexive verb."),
    (2, None,
     "'You are a very capable and promising cook.' The rival chef compliments him with descriptive predicate adjectives."),
    (3, None,
     "'Thank you, I truly want to learn a lot.' Max displays enthusiasm using paired verbs of desire and study."),
    (4, None,
     "'I will gladly take you into the kitchen.' Elena offers employment using a future perfective verb with a prepositional phrase."),
    (5, None,
     "'At the Claude Monet restaurant they do not appreciate me.' Max vents his frustration using a negative present verb."),
    (6, None,
     "'I do not understand why they act like that.' Elena sympathizes with him using an imperfective verb of manner."),
    (7, None,
     "'There they only give me vegetables to peel.' Max complains about mundane tasks using an infinitive."),
    (8, None,
     "'With us you will cook complex dishes.' Elena promises creative culinary freedom using a compound future verb."),
    (9, None,
     "'This is exactly what I dreamed about!' Max reacts joyfully with a relative pronoun clause in the past tense."),
    (10, None,
     "'Here are my contacts just in case.' Elena gives him her business card with an idiomatic prepositional phrase."),
    (11, None,
     "'When should I expect your call?' Max asks about next steps using an infinitive of expectation."),
    (12, None,
     "'I will call you in a couple of days.' Elena concludes the meeting with a future time expression."),
]

TRANSITION = "Now let's listen to the interview between Elena and Max again without interruption."
OUTRO = (
    "Max leaves Arcobaleno in high spirits, hopeful for a fresh start as a genuine chef. "
    "In the next scene, Chef Viktor Barinov crosses paths with Elena outside on the street."
)
CLOSING = ("elena", "Я позвоню вам через пару дней.")
