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
     "'Kristina, do you know one thing?' Here 'Kristina' sets up the idea, while 'thing' comes at the end for emphasis."),
    (1, None,
     "'Which exact thing?' You'll hear 'thing' all the time in the show, here connected with 'thing'."),
    (2, None,
     "'I truly cook not badly.' In Russian, 'I' leads into 'prepare' in a very natural everyday phrasing. Kristina answers straight away."),
    (3, None,
     "'Yes, I know that perfectly well.' Kristina starts with 'I' and pairs it with 'this' to make the point clear."),
    (4, None,
     "'These are very tasty rolls.' The key word here means 'this', which Chef Viktor combines with 'very much'."),
    (5, None,
     "'Did you prepare them yourself?' The key word here means 'you', which Kristina combines with 'cooked'. Then Chef Viktor replies."),
    (6, None,
     "'Yes, specially for you.' Chef Viktor puts 'on purpose' up front so the listener immediately catches the tone, followed by 'you'."),
    (7, None,
     "'They look very appetizing.' You'll hear 'they' all the time in the show, here connected with 'appetizingly'."),
    (8, None,
     "'Do you want to taste a little?' The first content word means 'do you want', and 'to taste' rounds out the thought. And Kristina jumps in."),
    (9, None,
     "'Yes, with great pleasure.' A compact expression built around 'great' and 'pleasure'."),
    (10, None,
     "'I am sure you will like it very much.' The first content word means 'I', and 'will please' rounds out the thought."),
    (11, None,
     "'Your food is always the best.' A compact expression built around 'your' and 'best'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kristina is genuinely impressed by the delicious food, proving that the chef's talent can solve almost any problem."
CLOSING = ("anja", "Твоя еда всегда самая лучшая.")
