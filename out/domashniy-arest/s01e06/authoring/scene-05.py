"""
Scene 05 authoring module — Домашний арест S01E06.

Девочка-сирота (An Orphan Girl)
Cues 138–186 (00:09:30,220 – 00:11:35,350).
"""

ID = "domashniy-arest-s01e06-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = "Девочка-сирота  (An Orphan Girl)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"

SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
CUE_RANGE = (138, 186)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",      # Юля
    "ignatyev": "anja",   # Вениамин Игоревич Игнатьев
    "vasya": "angelina",  # Вася
}

LABELS = {
    "anya": "Юля",
    "ignatyev": "Игнатьев",
    "vasya": "Вася",
}

INTRO = (
    "After leaving the restaurant where Pasha yelled at her over his cappuccino, "
    "teenage Yulya hurries to her second job serving coffee in the office of Veniamin Igorevich Ignatyev, "
    "the wealthy owner of the town's meatpacking plant. "
    "Ignatyev is bargaining with a wholesale sausage buyer named Vasya when Yulya brings their coffee, "
    "revealing the tragic sob story she invented to win the old boss's sympathy. "
    "Listen to the Russian dialogue first; don't worry about catching every word."
)

STORY = [
    ("vasya",
     "Сколько сможешь мне давать? Скидку сделаешь?",
     "How much can you supply me? Will you give me a discount?",
     [(143, "Сколько сможешь мне"), (145, "сделаешь")],
     "simplified 'отгружать' -> 'давать', 'скидочку' -> 'скидку'"),
    ("ignatyev",
     "Две тонны в месяц. Десять процентов.",
     "Two tonnes a month. Ten percent.",
     [(144, "Две"), (144, "в месяц"), (149, "Десять процентов")],
     "fixed ASR 'Две стенок' -> 'Две тонны'"),
    ("anya",
     "Спасибо. Ваш кофе, пожалуйста.",
     "Thank you. Your coffee, please.",
     [(151, "Спасибо. Ваш кофе, пожалуйста")],
     ""),
    ("ignatyev",
     "Спасибо, солнышко. Иди, Юля, работай.",
     "Thank you, sweetheart. Go on, Yulya, work.",
     [(152, "Спасибо, солнышко"), (155, "Иди, Юля")],
     "simplified 'шевели' -> 'работай'"),
    ("vasya",
     "Слушай, откуда ты красавиц таких берёшь?",
     "Listen, where do you get such beauties from?",
     [(153, "Слушай"), (154, "откуда ты"), (154, "таких")],
     "fixed ASR 'красавицы таких набираешь' -> 'красавиц таких берёшь'"),
    ("ignatyev",
     "По объявлению. Девочка — сирота, у неё трагедия.",
     "Through an ad. The girl is an orphan, she has a tragedy.",
     [(155, "По объявлению"), (159, "Девочка-сирота, у нее трагедия")],
     ""),
    ("ignatyev",
     "Мать под поезд попала. А отец с двадцатого этажа прыгнул.",
     "Her mother was hit by a train. And her father jumped from the twentieth floor.",
     [(160, "Мать под"), (160, "попала"), (161, "Отец"), (161, "с двадцатого этажа")],
     "simplified 'электричку' -> 'поезд' and fixed ASR 'Горя ... осеганул' -> 'прыгнул'; omitted 'в лепёшку'"),
    ("ignatyev",
     "Она с бабушкой живёт. Бабушка болеет всё время.",
     "She lives with her grandmother. Her grandmother is sick all the time.",
     [(163, "живет"), (163, "все время")],
     "simplified 'С бабкой' -> 'Она с бабушкой' and fixed ASR 'оболеет' -> 'болеет'"),
    ("vasya",
     "Ну, так даже лучше! С сиротой вообще никаких проблем.",
     "Well, that's even better! With an orphan there are no problems at all.",
     [(165, "Ну, так даже лучше"), (166, "вообще никаких проблем")],
     "restored 'С' before 'сиротой'"),
    ("ignatyev",
     "Вася, ты дурак? Встал и вышел отсюда!",
     "Vasya, are you an idiot? Stand up and get out of here!",
     [(167, "Вася, ты дурак"), (168, "Встал"), (168, "вышел отсюда")],
     ""),
    ("vasya",
     "Ну всё, понял. Значит, по пятнадцать рублей, да?",
     "Alright, I got it. So, fifteen roubles each, right?",
     [(169, "все, ну, понял"), (174, "значит, пятнадцать, да")],
     ""),
    ("ignatyev",
     "Иди, пятнадцать.",
     "Go on, fifteen.",
     [(175, "Иди, пятнадцать")],
     ""),
    ("ignatyev",
     "Ну как, Юля, не обижают тебя здесь?",
     "Well, how is it, Yulya, is nobody bothering you here?",
     [(177, "не обижают тебя здесь")],
     "simplified 'Юляш' -> 'Юля'"),
    ("anya",
     "Да нет. Спасибо, Вениамин Игоревич.",
     "No, not at all. Thank you, Veniamin Igorevich.",
     [(178, "Да нет"), (179, "Спасибо, Вениамин Игоревич")],
     ""),
    ("ignatyev",
     "Подожди. Купи себе платье или бабушке что-нибудь.",
     "Wait. Buy yourself a dress or something for your grandmother.",
     [(180, "подожди"), (181, "Купи себе платье"), (183, "или бабушке что-нибудь")],
     ""),
    ("anya",
     "Спасибо, вы меня балуете!",
     "Thank you, you're spoiling me!",
     [(184, "Спасибо, вы меня"), (184, "балуете")],
     ""),
]

OPENER = (
    "Let's walk through the scene in the meatpacking plant office and see how Yulya's invented story works like a charm."
)

WALK = [
    (0, "Сколько сможешь мне давать?",
     "The wholesale buyer Vasya tastes the sausage and asks Ignatyev: how much can you supply me?"),
    (0, "Скидку сделаешь?",
     "And he bargains for a better price: will you give me a discount?"),
    (1, "Две тонны в месяц.",
     "Ignatyev names the volume: two tonnes per month."),
    (1, "Десять процентов.",
     "And he offers a ten percent discount."),
    (2, "Спасибо.",
     "Yulya steps up to the desk with a tray: thank you."),
    (2, "Ваш кофе, пожалуйста.",
     "She sets down the cups politely: your coffee, please."),
    (3, "Спасибо, солнышко.",
     "Ignatyev smiles warmly at her: thank you, little sun — an affectionate Russian term like 'sweetheart'."),
    (3, "Иди, Юля, работай.",
     "He sends her back to the kitchen: go on, Yulya, work."),
    (4, None,
     "As soon as the door closes behind her, Vasya leans in with a grin: listen, where do you get such beauties from?"),
    (5, "По объявлению.",
     "Through a job advertisement, Ignatyev answers seriously."),
    (5, "Девочка — сирота, у неё трагедия.",
     "He repeats the tale Yulya told him when she was hired: the girl is an orphan, she has a family tragedy."),
    (6, "Мать под поезд попала.",
     "According to Yulya's story, her mother was hit by a train."),
    (6, "А отец с двадцатого этажа прыгнул.",
     "And her father jumped from the twentieth floor out of grief."),
    (7, "Она с бабушкой живёт.",
     "Now she lives alone with her grandmother."),
    (7, "Бабушка болеет всё время.",
     "And the grandmother is sick all the time."),
    (8, "Ну, так даже лучше!",
     "Vasya chuckles cynically: well, that is even better!"),
    (8, "С сиротой вообще никаких проблем.",
     "With an orphan there are no problems at all — nobody to stand up for her."),
    (9, "Вася, ты дурак?",
     "Ignatyev's face darkens with anger: Vasya, are you a fool?"),
    (9, "Встал и вышел отсюда!",
     "Using past-tense verbs as a sharp command, he throws the buyer out: stand up and get out of here!"),
    (10, "Ну всё, понял.",
     "Vasya quickly backs down: alright, I understood."),
    (10, "Значит, по пятнадцать рублей, да?",
     "At the door, he realises Ignatyev has raised the price as punishment: so, fifteen roubles a unit now, right?"),
    (11, None,
     "Ignatyev waves him out the door: go on, fifteen."),
    (12, None,
     "When Yulya returns to clear the cups, Ignatyev asks gently: well, how is it, Yulya, is nobody bothering you here?"),
    (13, "Да нет.",
     "Yulya puts on her sweetest innocent voice: no, not at all."),
    (13, "Спасибо, Вениамин Игоревич.",
     "Thank you, Veniamin Igorevich."),
    (14, "Подожди.",
     "As she turns to leave, Ignatyev reaches into his wallet: wait."),
    (14, "Купи себе платье или бабушке что-нибудь.",
     "He hands her a generous tip: buy yourself a dress or something for your grandmother."),
    (15, None,
     "Beaming, Yulya pockets the cash: thank you, you are spoiling me!"),
]

TRANSITION = (
    "Now listen to the entire scene at the meatpacking plant once more from beginning to end."
)

OUTRO = (
    "While Yulya pockets Ignatyev's generous tip for her fictional sick grandmother, "
    "across town Major Lavrov connects by video link with General Kruglov in Moscow."
)

CLOSING = ("anya", "Спасибо, вы меня балуете!")
