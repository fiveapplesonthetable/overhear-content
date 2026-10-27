ID = "kukhnya-s02e02-scene-20"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 2
SCENE = 20
TITLE = "Вкусные роллы  (Delicious Rolls)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anja": "anja"}
LABELS = {"anya": "Шеф", "anja": "Кристина"}
SOURCE_NAME = "Кухня (Kukhnya) S2.02"
SOURCE_FILE = "sources/kukhnya/s02/e02.ru.dual.srt"
SOURCE_NOTE = "Scene 20"

INTRO = "The chef proudly presents his newly created sushi rolls to Kristina. He hopes his culinary skills will impress her and smooth over their previous conflicts."

STORY = [
    ("anya", "Кристина, ты знаешь одну вещь?",
     "Kristina, do you know one thing?",
     [(326, 'Кристина, ты знаешь')], "adapted"),
    ("anja", "Какую именно вещь?",
     "Which exact thing?",
     [], "new"),
    ("anya", "Я действительно неплохо готовлю.",
     "I truly cook not badly.",
     [(326, 'я действительно неплохо готовлю.')], "adapted"),
    ("anja", "Да, я это прекрасно знаю.",
     "Yes, I know that perfectly well.",
     [], "new"),
    ("anya", "Это очень вкусные роллы.",
     "These are very tasty rolls.",
     [(327, 'Очень вкусные роллы.')], "adapted"),
    ("anja", "Ты приготовил их сам?",
     "Did you prepare them yourself?",
     [], "new"),
    ("anya", "Да, специально для тебя.",
     "Yes, specially for you.",
     [], "new"),
    ("anja", "Они выглядят очень аппетитно.",
     "They look very appetizing.",
     [], "new"),
    ("anya", "Хочешь немного попробовать?",
     "Do you want to taste a little?",
     [(328, 'Хочешь?')], "adapted"),
    ("anja", "Да, с большим удовольствием.",
     "Yes, with great pleasure.",
     [], "new"),
    ("anya", "Я уверен, тебе очень понравится.",
     "I am sure you will like it very much.",
     [], "new"),
    ("anja", "Твоя еда всегда самая лучшая.",
     "Your food is always the best.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Kristina, do you know one thing?' -- ENG The chef approaches his demanding guest with a smile."),
    (1, None,
     "'Which exact thing?' -- ENG She looks up and waits for him to explain himself."),
    (2, None,
     "'I truly cook not badly.' -- ENG He modestly boasts about his legendary culinary talent."),
    (3, None,
     "'Yes, I know that perfectly well.' -- ENG She agrees that his food is completely unmatched."),
    (4, None,
     "'These are very tasty rolls.' -- ENG He presents a beautifully arranged plate of fresh sushi."),
    (5, None,
     "'Did you prepare them yourself?' -- ENG She is surprised that he made Japanese cuisine."),
    (6, None,
     "'Yes, specially for you.' -- ENG He admits that he cooked them to make her happy."),
    (7, None,
     "'They look very appetizing.' -- ENG She examines the artistic presentation of the meal."),
    (8, None,
     "'Do you want to taste a little?' -- ENG He invites her to try his latest creation."),
    (9, None,
     "'Yes, with great pleasure.' -- ENG She eagerly picks up her chopsticks to eat."),
    (10, None,
     "'I am sure you will like it very much.' -- ENG He watches her with absolute confidence in his recipe."),
    (11, None,
     "'Your food is always the best.' -- ENG She compliments him before even taking her first bite."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kristina is genuinely impressed by the delicious food, proving that the chef's talent can solve almost any problem."
CLOSING = ("anja", "Твоя еда всегда самая лучшая.")
