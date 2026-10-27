ID = "kukhnya-s02e01-scene-01"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = "Новый хозяин  (The New Owner)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "igor": "anja", "dima": "angelina"}
LABELS = {"anya": "Шеф", "igor": "Игорь", "dima": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-63. Dmitry Nagiyev announces he has sold Claude Monet to Igor Valentinovich, "
    "who immediately confronts Chef Viktor about his drinking problem and forbids alcohol at work."
)

INTRO = (
    "In the dining room of Claude Monet, Dmitry Nagiyev shocks the staff by announcing that he has "
    "sold the entire restaurant to a strict new owner, Igor Valentinovich. Igor immediately pulls "
    "Chef Viktor aside to establish harsh new rules. Let us listen to their conversation in Russian first."
)

STORY = [
    ("dima", "Друзья мои, я продал весь наш ресторан.",
     "My friends, I sold our entire restaurant.",
     [(34, "Ресторан я все тютю продал.")], "adapted"),
    ("anya", "Дмитрий, кому вы продали этот прекрасный ресторан?",
     "Dmitry, to whom did you sell this wonderful restaurant?",
     [(33, "В смысле? В прямом.")], "adapted"),
    ("dima", "Знакомьтесь, Игорь теперь ваш новый главный хозяин.",
     "Meet Igor, he is now your new main owner.",
     [(30, "Извини мне. Вон Игорь Валентинович.")], "adapted"),
    ("igor", "Добрый день, Виктор, давайте сразу серьёзно поговорим.",
     "Good afternoon, Viktor, let us talk seriously right away.",
     [(47, "Как раз об этом я с вами собирался серьезно поговорить.")], "adapted"),
    ("anya", "О чём вы хотите говорить со мной?",
     "What do you want to talk about with me?",
     [], "new"),
    ("igor", "Дмитрий сказал, что вы часто пьёте алкоголь.",
     "Dmitry said that you often drink alcohol.",
     [(48, "Дима рассказывал у вас проблемы с алкоголем.")], "adapted"),
    ("anya", "У меня совсем нет проблем с алкоголем.",
     "I have no problems with alcohol at all.",
     [(49, "Никаких проблем с алкоголем.")], "adapted"),
    ("igor", "Вы прекрасно понимаете, о чём я говорю.",
     "You understand very well what I am talking about.",
     [(51, "Вы прекрасно понимаете, о чем я говорю.")], "exact"),
    ("igor", "Сегодня я строго решил запретить пить здесь.",
     "Today I strictly decided to forbid drinking here.",
     [(52, "С сегодняшнего дня я запрещаю вам пить на работе.")], "adapted"),
    ("anya", "А если я выпью немного вечером дома?",
     "And what if I drink a little at home in the evening?",
     [(53, "До работы, кстати, тоже.")], "adapted"),
    ("igor", "До работы тоже нельзя пить никакой алкоголь.",
     "Before work you also cannot drink any alcohol.",
     [(53, "До работы, кстати, тоже.")], "adapted"),
    ("igor", "Иначе мы быстро расстанемся с вами навсегда.",
     "Otherwise we will quickly part ways with you forever.",
     [(54, "Или считайте, что мы не сработались и нам надо расстаться.")], "adapted"),
    ("anya", "Хорошо, хозяин, я понял ваши новые правила.",
     "Fine, boss, I understood your new rules.",
     [(56, "Хозяин барин, у вас все?")], "adapted"),
]

OPENER = "Now let us examine the arrival of the new owner line by line."

WALK = [
    (0, None,
     "'My friends, I sold our entire restaurant.' -- Nagiyev casually announces the sale of Claude Monet."),
    (1, None,
     "'Dmitry, to whom did you sell this wonderful restaurant?' -- Chef Viktor demands to know who bought the business."),
    (2, None,
     "'Meet Igor, he is now your new main owner.' -- Nagiyev introduces Igor Valentinovich as the new boss."),
    (3, None,
     "'Good afternoon, Viktor, let us talk seriously right away.' -- Igor immediately initiates a stern conversation with the chef."),
    (4, None,
     "'What do you want to talk about with me?' -- Viktor asks what topic the new owner wants to discuss."),
    (5, None,
     "'Dmitry said that you often drink alcohol.' -- Igor brings up Viktor's notorious habit in the kitchen."),
    (6, None,
     "'I have no problems with alcohol at all.' -- Viktor tries to brush off the accusation with confidence."),
    (7, None,
     "'You understand very well what I am talking about.' -- Igor refuses to accept any excuses or jokes."),
    (8, None,
     "'Today I strictly decided to forbid drinking here.' -- The new owner imposes a total ban on workplace drinking."),
    (9, None,
     "'And what if I drink a little at home in the evening?' -- Viktor looks for a loophole outside working hours."),
    (10, None,
     "'Before work you also cannot drink any alcohol.' -- Igor closes the loophole and demands complete sobriety."),
    (11, None,
     "'Otherwise we will quickly part ways with you forever.' -- Igor warns that breaking the rule means immediate dismissal."),
    (12, None,
     "'Fine, boss, I understood your new rules.' -- Viktor reluctantly accepts the new owner's strict ultimatum."),
]

TRANSITION = "Now let us listen to the full conversation once again."
OUTRO = (
    "With Igor Valentinovich taking over Claude Monet, Chef Viktor faces an unprecedented ban on alcohol "
    "and the threat of losing his kitchen if he disobeys."
)
CLOSING = ("anya", "Хорошо, хозяин, я понял ваши новые правила.")
