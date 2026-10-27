ID = "kukhnya-s01e08-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 3
TITLE = "Мужская профессия  (A Man's Profession)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Елена", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 29-31. During the TV broadcast, Chef Barinov insists he would never hire a woman in his kitchen, "
    "claiming female cooks talk too much and lack discipline."
)

INTRO = (
    "Continuing his provocative commentary on the morning cooking broadcast, Chef Viktor Barinov declares "
    "that he would never allow a female chef to work in the Claude Monet kitchen. He argues that women "
    "talk too much and cannot withstand the grueling pressure of haute cuisine, but Elena Sokolova fiercely "
    "defends the competence and discipline of her staff. Let's listen to their argument in Russian first."
)

STORY = [
    ("chef", "Я никогда не возьму женщину на кухню.",
     "I will never take a woman into the kitchen.",
     [(29, "Я бы себе на кухню поварику бы не взял")], "adapted"),
    ("anya", "Что за глупые мысли, Виктор?",
     "What foolish thoughts, Viktor?",
     [(31, "Что вы говорите")], "adapted"),
    ("chef", "Женщины слишком много говорят на работе.",
     "Women talk too much at work.",
     [(30, "Они слишком много болтают")], "adapted"),
    ("anya", "На моей кухне всегда идеальный порядок.",
     "In my kitchen there is always perfect order.",
     [], "new"),
    ("chef", "На кухне ресторана нужен строгий контроль.",
     "In a restaurant kitchen strict control is needed.",
     [], "new"),
    ("anya", "Мои повара работают спокойно и аккуратно.",
     "My cooks work calmly and neatly.",
     [], "new"),
    ("chef", "Вы не справитесь с нашей тяжёлой работой.",
     "You will not cope with our hard work.",
     [], "new"),
    ("anya", "Я справляюсь с любой трудной задачей.",
     "I cope with any difficult task.",
     [], "new"),
    ("chef", "В ресторане Клод Моне очень тяжело.",
     "At Claude Monet restaurant it is very hard.",
     [], "new"),
    ("anya", "Я не боюсь тяжёлой работы, шеф!",
     "I am not afraid of hard work, chef!",
     [], "new"),
    ("chef", "Вы не понимаете наших мужских правил.",
     "You do not understand our male rules.",
     [], "new"),
    ("anya", "Правила на кухне одинаковы для всех.",
     "The rules in the kitchen are the same for everyone.",
     [], "new"),
    ("chef", "Тогда докажите это на деле, Елена!",
     "Then prove it in deed, Elena!",
     [], "new"),
]

OPENER = "Now let's examine Barinov and Elena's debate on kitchen discipline line by line."

WALK = [
    (0, None,
     "'I will never take a woman into the kitchen.' Barinov expresses his dogmatic hiring rule with a negated future verb."),
    (1, None,
     "'What foolish thoughts, Viktor?' Elena dismisses his sexist ideas using an exclamatory phrase."),
    (2, None,
     "'Women talk too much at work.' Barinov justifies his bias by claiming excessive chatter among female cooks."),
    (3, None,
     "'In my kitchen there is always perfect order.' Elena points out the impeccable cleanliness and discipline at Arcobaleno."),
    (4, None,
     "'In a restaurant kitchen strict control is needed.' Barinov stresses the demand for absolute authority."),
    (5, None,
     "'My cooks work calmly and neatly.' Elena highlights professional composure over chaotic yelling."),
    (6, None,
     "'You will not cope with our hard work.' Barinov predicts failure using a future perfective verb."),
    (7, None,
     "'I cope with any difficult task.' Elena reaffirms her daily competence with an imperfective verb and instrumental object."),
    (8, None,
     "'At Claude Monet restaurant it is very hard.' Barinov describes the brutal physical demands of his kitchen."),
    (9, None,
     "'I am not afraid of hard work, chef!' Elena declares her fearlessness in the face of long shifts."),
    (10, None,
     "'You do not understand our male rules.' Barinov leans into kitchen machismo with a plural genitive phrase."),
    (11, None,
     "'The rules in the kitchen are the same for everyone.' Elena upholds universal culinary standards."),
    (12, None,
     "'Then prove it in deed, Elena!' Barinov throws down the gauntlet with an imperative challenge."),
]

TRANSITION = "Now let's listen to the debate on kitchen discipline again without interruption."
OUTRO = (
    "With neither chef backing down from their entrenched positions, Elena prepares to challenge Barinov "
    "to put his pride on the line before the entire television audience."
)
CLOSING = ("chef", "Тогда докажите это на деле, Елена!")
