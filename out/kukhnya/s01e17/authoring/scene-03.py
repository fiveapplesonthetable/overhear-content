ID = "kukhnya-s01e17-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 3
TITLE = "Долг и меню  (Debt and Menu)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja"}
LABELS = {"anya": "Вика", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 35-47. In the kitchen, Victoria reminds Viktor that he owes her money and demands either repayment "
    "or a brand-new seasonal dish for the restaurant's menu by tomorrow."
)

INTRO = (
    "In the quiet kitchen of Claude Monet, Viktor feeds his pet fish Arkady while enjoying a brief moment of peace. "
    "Victoria walks in to confront him about an unpaid loan, demanding that he either return her cash or create a new seasonal dish. "
    "Let's listen to their confrontation in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("shef", "Приятного аппетита, мой дорогой Аркадий.",
     "Enjoy your meal, my dear Arkady.",
     [(35, "приятного аппетита, Аркадий.")], "adapted"),
    ("anya", "Ты кормишь рыбу лучше наших гостей.",
     "You feed the fish better than our guests.",
     [(36, "ты для своей селедки готовишь с большим удовольствием")], "adapted"),
    ("shef", "Аркадий, молчи и не слушай её.",
     "Arkady, be quiet and do not listen to her.",
     [(37, "Аркадий, не отвечай.")], "adapted"),
    ("anya", "Ты помнишь, что завтра первое число?",
     "Do you remember that tomorrow is the first?",
     [(39, "Ты помнишь, что завтра первое число?")], "adapted"),
    ("shef", "Я верну тебе деньги через неделю.",
     "I will return your money in a week.",
     [(40, "отдам деньги через неделю.")], "adapted"),
    ("anya", "Ты обещал вернуть долг сегодня.",
     "You promised to return the debt today.",
     [], "new"),
    ("shef", "Твои деньги сейчас у футболиста Магиди.",
     "Your money is with the footballer Magidi right now.",
     [(42, "твои деньги у Магиди.")], "adapted"),
    ("anya", "Он не забил гол, при чём тут он?",
     "He missed the goal, what has he to do with it?",
     [(43, "он не забил с двух метров.")], "adapted"),
    ("shef", "Спроси свои деньги прямо с него.",
     "Ask for your money directly from him.",
     [(44, "Вот с него и спрашивай.")], "adapted"),
    ("anya", "Ты обещал новое сезонное блюдо, Виктор.",
     "You promised a new seasonal dish, Viktor.",
     [(45, "ты обещал новое сезонное блюдо от шефа.")], "adapted"),
    ("shef", "Когда нужны деньги, всегда много обещаешь.",
     "When money is needed, one always promises a lot.",
     [(46, "когда тебе нужны деньги, ты еще не то пообещаешь.")], "adapted"),
    ("anya", "Завтра я жду деньги или блюдо.",
     "Tomorrow I expect the money or the dish.",
     [(47, "завтра у меня должны быть либо мои деньги, либо сезонное блюдо.")], "adapted"),
    ("shef", "Хорошо, Вика, я что-нибудь придумаю.",
     "Fine, Vika, I will come up with something.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Enjoy your meal, my dear Arkady.' -- Viktor talks affectionately to his goldfish."),
    (1, None,
     "'You feed the fish better than our guests.' -- Victoria enters with a sarcastic remark."),
    (2, None,
     "'Arkady, be quiet and do not listen to her.' -- The chef playfully defends his pet from the criticism."),
    (3, None,
     "'Do you remember that tomorrow is the first?' -- The administrator reminds him of their financial deadline."),
    (4, None,
     "'I will return your money in a week.' -- Viktor tries to buy more time."),
    (5, None,
     "'You promised to return the debt today.' -- Victoria insists on their original agreement."),
    (6, None,
     "'Your money is with the footballer Magidi right now.' -- The chef blames his lost sports bets."),
    (7, None,
     "'He missed the goal, what has he to do with it?' -- Victoria refuses to accept sports gambling excuses."),
    (8, None,
     "'Ask for your money directly from him.' -- Viktor stubbornly shifts the blame to the athlete."),
    (9, None,
     "'You promised a new seasonal dish, Viktor.' -- Victoria pivots to his culinary obligations."),
    (10, None,
     "'When money is needed, one always promises a lot.' -- The chef shrugs off his past commitments."),
    (11, None,
     "'Tomorrow I expect the money or the dish.' -- Victoria lays down an uncompromising ultimatum."),
    (12, None,
     "'Fine, Vika, I will come up with something.' -- Viktor reluctantly agrees to find a solution."),
]

TRANSITION = "Now let's listen to the kitchen discussion once again."

OUTRO = (
    "Faced with Victoria's strict deadline, Viktor realizes he must quickly organize a competition "
    "among his cooks to invent the required seasonal special."
)

CLOSING = ("shef", "Хорошо, Вика, я что-нибудь придумаю.")
