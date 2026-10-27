ID = "kukhnya-s01e06-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 1
TITLE = "Путь на тарелку  (The Journey to the Plate)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-3. At the Claude Monet bar, Max watches dinner guests and discusses with Kostya "
    "how diners never realize the immense journey a dish takes to reach their plate."
)

INTRO = (
    "In the elegant dining room of Claude Monet, guests gather for dinner and order their favorite dishes. "
    "Looking out from behind the bar, Max and Kostya reflect on how little diners know about the long path "
    "every meal takes before arriving on their plate. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Макс, посмотри на гостей в зале.",
     "Max, look at the guests in the dining room.",
     [], "new"),
    ("anya", "Они заказывают наши фирменные блюда.",
     "They are ordering our specialty dishes.",
     [(1, "заказываете любимое блюдо")], "adapted"),
    ("kostya", "Люди приходят сюда каждый вечер.",
     "People come here every evening.",
     [(1, "Когда вы приходите в ресторан")], "adapted"),
    ("anya", "Каждый выбирает своё любимое блюдо.",
     "Everyone chooses their favorite dish.",
     [(1, "любимое блюдо")], "adapted"),
    ("kostya", "Они не думают о пути еды.",
     "They do not think about the food's journey.",
     [(2, "вы наверняка не задумываетесь, какой путь")], "adapted"),
    ("anya", "Какое блюдо проходит длинный путь?",
     "Which dish travels a long way?",
     [(2, "путь оно проделывает")], "adapted"),
    ("kostya", "Каждое блюдо начинает путь на рынке.",
     "Every dish begins its journey at the market.",
     [(3, "чтобы оказаться у вас на тарелке")], "adapted"),
    ("anya", "Потом повара готовят заказ на кухне.",
     "Then the cooks prepare the order in the kitchen.",
     [], "new"),
    ("kostya", "Вся кухня работает ради одной тарелки.",
     "The whole kitchen works for one plate.",
     [], "new"),
    ("anya", "Повара очень спешат и нервничают.",
     "The cooks rush very much and get nervous.",
     [], "new"),
    ("kostya", "А гости видят только вкусный результат.",
     "And guests only see the delicious result.",
     [], "new"),
    ("anya", "Для них это настоящий праздник вкуса.",
     "For them this is a real celebration of taste.",
     [], "new"),
    ("kostya", "Скоро начнётся наш обычный рабочий вечер.",
     "Soon our usual working evening will begin.",
     [], "new"),
]

OPENER = "Now let's examine Max and Kostya's dialogue line by line."

WALK = [
    (0, None,
     "'Max, look at the guests in the dining room.' Kostya directs his friend's attention with an imperative verb."),
    (1, None,
     "'They are ordering our specialty dishes.' Max observes customer behavior using a present imperfective verb."),
    (2, None,
     "'People come here every evening.' Kostya notes the regular attendance using a plural noun and temporal adverb."),
    (3, None,
     "'Everyone chooses their favorite dish.' Max highlights individual tastes using a reflexive determiner."),
    (4, None,
     "'They do not think about the food's journey.' Kostya remarks on diner unawareness with a negated present verb."),
    (5, None,
     "'Which dish travels a long way?' Max asks an open question with a question determiner and adjective."),
    (6, None,
     "'Every dish begins its journey at the market.' Kostya traces the culinary origins with a locative prepositional phrase."),
    (7, None,
     "'Then the cooks prepare the order in the kitchen.' Max describes the kitchen phase using a temporal adverb and plural verb."),
    (8, None,
     "'The whole kitchen works for one plate.' Kostya emphasizes collective effort with a preposition of purpose."),
    (9, None,
     "'The cooks rush very much and get nervous.' Max portrays the kitchen pressure using paired present verbs."),
    (10, None,
     "'And guests only see the delicious result.' Kostya contrasts the back of house with the dining experience."),
    (11, None,
     "'For them this is a real celebration of taste.' Max concludes with an appreciative metaphor about gastronomy."),
    (12, None,
     "'Soon our usual working evening will begin.' Kostya wraps up the chat as service begins with a future verb."),
]

TRANSITION = "Now let's listen to the conversation at the bar again without interruption."
OUTRO = (
    "Max and Kostya get ready for the dinner rush as orders start flooding into the kitchen. "
    "Every plate represents a synchronized performance between cooks, waitstaff, and suppliers."
)
CLOSING = ("kostya", "Скоро начнётся наш обычный рабочий вечер.")

