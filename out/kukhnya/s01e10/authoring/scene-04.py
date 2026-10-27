ID = "kukhnya-s01e10-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 4
TITLE = "Низкий гонорар  (A Low Fee)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Девушка", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 7-20. A television producer offers Chef Barinov a regular hosting spot on a morning show, "
    "but Barinov rejects the offer due to the insultingly low pay."
)

INTRO = (
    "In the dining room of Claude Monet, a representative from a television studio meets with Chef Viktor Barinov. "
    "Impressed by his past guest appearance, producers want him to become the permanent host of a weekly morning "
    "cooking program, but their proposed fee leads to immediate outrage. Let's listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Здравствуйте, я вас внимательно слушаю.",
     "Hello, I am listening to you attentively.",
     [(7, "Я вас слушаю. Здравствуйте, Виктор")], "adapted"),
    ("anya", "Вы отлично выступали в нашем кулинарном шоу.",
     "You performed wonderfully on our culinary show.",
     [(8, "кулинарном шоу?")], "adapted"),
    ("chef", "И что решили ваши строгие продюсеры?",
     "And what did your strict producers decide?",
     [(9, "нашим продюсерам.")], "adapted"),
    ("anya", "Мы хотим предложить вам постоянную работу.",
     "We want to offer you a permanent job.",
     [(10, "хотят предложить вам")], "adapted"),
    ("chef", "Во сколько вы оценили мою работу?",
     "At how much did you value my work?",
     [(12, "во сколько ваши продюсеры оценили мою работу?")], "adapted"),
    ("anya", "Десять тысяч за каждую новую передачу.",
     "Ten thousand for each new broadcast.",
     [(14, "Десять, десять одна программа.")], "adapted"),
    ("chef", "Десять тысяч евро за один выпуск?",
     "Ten thousand euros for one episode?",
     [(15, "Евро?")], "adapted"),
    ("anya", "Нет, мы платим десять тысяч рублей.",
     "No, we pay ten thousand rubles.",
     [(15, "Рублей.")], "adapted"),
    ("chef", "Тогда до свидания, а лучше прощайте!",
     "Then goodbye, or rather farewell!",
     [(16, "До свидания. Нет, лучше прощайте.")], "adapted"),
    ("anya", "Подождите, Виктор, давайте спокойно всё обсудим.",
     "Wait, Viktor, let us calmly discuss everything.",
     [(17, "Подождите. Давайте мы с вами обсудим.")], "adapted"),
    ("chef", "Вы предлагаете работать в мой выходной день.",
     "You propose that I work on my day off.",
     [(18, "Вы мне предлагаете работать в мой выходной день")], "adapted"),
    ("anya", "Это сделает ваш ресторан очень известным.",
     "This will make your restaurant very famous.",
     [], "new"),
    ("chef", "Я не работаю за такие смешные копейки!",
     "I do not work for such ridiculous kopecks!",
     [(19, "да еще за копейки.")], "adapted"),
]

OPENER = "Now let's examine the television negotiation line by line."

WALK = [
    (0, None,
     "'Hello, I am listening to you attentively.' -- Barinov greets the visitor and invites her to speak."),
    (1, None,
     "'You performed wonderfully on our culinary show.' -- The producer compliments his earlier televised cooking performance."),
    (2, None,
     "'And what did your strict producers decide?' -- The chef inquires about the production team's decision."),
    (3, None,
     "'We want to offer you a permanent job.' -- She extends an offer for a regular television role."),
    (4, None,
     "'At how much did you value my work?' -- Barinov asks directly about the financial compensation."),
    (5, None,
     "'Ten thousand for each new broadcast.' -- The representative states the compensation per program."),
    (6, None,
     "'Ten thousand euros for one episode?' -- The chef presumes the figure is denominated in European currency."),
    (7, None,
     "'No, we pay ten thousand rubles.' -- She clarifies that the payment is in domestic rubles."),
    (8, None,
     "'Then goodbye, or rather farewell!' -- Insulted by the tiny sum, Barinov terminates the meeting abruptly."),
    (9, None,
     "'Wait, Viktor, let us calmly discuss everything.' -- The producer attempts to salvage the discussion."),
    (10, None,
     "'You propose that I work on my day off.' -- The chef points out that filming disrupts his personal Sunday rest."),
    (11, None,
     "'This is wonderful advertising for your restaurant.' -- She highlights the promotional value for Claude Monet."),
    (12, None,
     "'I do not work for such ridiculous kopecks!' -- Barinov firmly refuses to sacrifice his time for meager pay."),
]

TRANSITION = "Now let's listen to the heated negotiation again without interruption."
OUTRO = (
    "Furious at the insultingly modest payment offer, Chef Barinov turns his back on television stardom "
    "and returns to the comfort of his own high-end restaurant."
)
CLOSING = ("chef", "Я не работаю за такие смешные копейки!")
