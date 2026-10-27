ID = "kukhnya-s01e11-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 17
TITLE = "Назойливый клиент  (The Pushy Customer)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guest": "anja"}
LABELS = {"anya": "Настя", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 192-201. Waitress Nastya takes an order from a rude customer suspected of being a secret critic, "
    "firmly rejecting his pushy attempts to flirt during work."
)

INTRO = (
    "At an intimate dining table, waitress Nastya attends to a demanding male customer whom "
    "management suspects of being an undercover restaurant critic. When the diner crosses the line "
    "and pressures her to sit and flirt with him, Nastya defends her professional boundaries. "
    "Let us listen to their awkward exchange in Russian first."
)

STORY = [
    ("anya", "Что вы хотите заказать сегодня у нас?",
     "What do you want to order with us today?",
     [(192, "вы что-нибудь покушаете у нас?")], "adapted"),
    ("guest", "Принеси мне любое блюдо на твой вкус.",
     "Bring me any dish to your taste.",
     [(193, "на твое усмотрение")], "adapted"),
    ("anya", "Хорошо, я выберу для вас лучшее.",
     "Good, I will choose the best for you.",
     [(195, "Хорошо")], "adapted"),
    ("guest", "А почему бы тебе не присесть рядом?",
     "Why do you not take a seat nearby?",
     [(196, "Может, ты присядешь?")], "adapted"),
    ("anya", "Извините, но я сейчас на работе.",
     "Excuse me, but I am at work right now.",
     [(197, "Я вообще-то на работе")], "adapted"),
    ("guest", "Я твой клиент и плачу за всё.",
     "I am your customer and I pay for everything.",
     [(198, "Я твой клиент")], "adapted"),
    ("anya", "Я обязана только приносить ваши блюда.",
     "I am obliged only to bring your dishes.",
     [], "new"),
    ("guest", "Ты первая строила мне красивые глазки.",
     "You were the first to make pretty eyes at me.",
     [(199, "ты же первая начала мне строить глазки")], "adapted"),
    ("anya", "Я просто вежливо улыбалась вам, гость.",
     "I was simply smiling politely at you, guest.",
     [(200, "Я ничего не начинала")], "adapted"),
    ("guest", "Не уходи, посиди со мной немного.",
     "Do not leave, sit with me a little.",
     [(199, "Ну, не ломайся")], "adapted"),
    ("anya", "Я не имею права сидеть здесь.",
     "I do not have the right to sit here.",
     [], "new"),
    ("guest", "Ты должна выполнять любые мои просьбы.",
     "You must fulfill any requests of mine.",
     [(198, "ты должна выполнять все мои желания")], "adapted"),
    ("anya", "Извините, я сейчас пойду на кухню.",
     "Excuse me, I am going to the kitchen right now.",
     [(201, "Извините")], "adapted"),
]

OPENER = "Now let us examine Nastya's tense interaction with the customer line by line."

WALK = [
    (0, None,
     "'What do you want to order with us today?' -- The waitress politely asks for the patron's dinner choices."),
    (1, None,
     "'Bring me any dish to your taste.' -- The guest invites her to choose any menu item."),
    (2, None,
     "'Good, I will choose the best for you.' -- Nastya obliges pleasantly with the culinary request."),
    (3, None,
     "'Why do you not take a seat nearby?' -- The customer inappropriately invites the waitress to sit down."),
    (4, None,
     "'Excuse me, but I am at work right now.' -- Nastya reminds him of her professional duties."),
    (5, None,
     "'I am your customer and I pay for everything.' -- The pushy man asserts entitlement through paying money."),
    (6, None,
     "'I am obliged only to bring your dishes.' -- She sets clear boundaries regarding waitressing duties."),
    (7, None,
     "'You were the first to make pretty eyes at me.' -- The customer falsely claims that she was flirting."),
    (8, None,
     "'I was simply smiling politely at you, guest.' -- Nastya clarifies that her smile was purely customer service."),
    (9, None,
     "'Do not leave, sit with me a little.' -- The customer continues to cajole and pressure her."),
    (10, None,
     "'I do not have the right to sit here.' -- The waitress points out workplace conduct rules."),
    (11, None,
     "'You must fulfill any requests of mine.' -- The man arrogantly demands total obedience from the staff."),
    (12, None,
     "'Excuse me, I am going to the kitchen right now.' -- Nastya makes an orderly retreat to escape the harassment."),
]

TRANSITION = "Now let us listen to the tense confrontation at the table again."
OUTRO = (
    "Firmly refusing to compromise her self-respect, Nastya walks away from the arrogant diner "
    "and heads toward the kitchen to report the intolerable behavior to management."
)
CLOSING = ("anya", "Извините, я сейчас пойду на кухню.")
