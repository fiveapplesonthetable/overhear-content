"""s01e03 scene 15: Живой гусь (The Live Goose)."""

ID = "kukhnya-s01e03-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 15
TITLE = "Живой гусь  (The Live Goose)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "sasha": "anja",
}
LABELS = {
    "anya": "Настя",
    "sasha": "Саша",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = (
    "In the restaurant back hallway, waitress Nastya has made a startling discovery inside a delivery box. "
    "Horrified that Chef Barinov plans to slaughter a live banquet goose, Nastya resolves to save the bird. "
    "Listen to her whispered conversation with Sasha in Russian first, and then we will examine every phrase."
)

STORY = [
    ("anya", "Саша, иди скорее сюда!",
     "Sasha, come here quickly!",
     [(265, "сюда и позвала")], "urgent call"),
    ("sasha", "Что случилось, Настя?",
     "What happened, Nastya?",
     [(261, "на минуточку")], "inquiring"),
    ("anya", "Посмотри, в коробке сидит живой гусь!",
     "Look, a live goose is sitting in the box!",
     [(264, "гусь")], "verbatim discovery"),
    ("sasha", "Откуда здесь взялся этот гусь?",
     "Where did this goose come from?",
     [(264, "гусь")], "shocked question"),
    ("anya", "Шеф хотел приготовить из него блюдо.",
     "The chef wanted to prepare a dish out of it.",
     [], "explaining plan"),
    ("sasha", "Ты решила спасти эту птицу?",
     "Did you decide to save this bird?",
     [], "asking motive"),
    ("anya", "Да, я не могу его бросить.",
     "Yes, I cannot abandon him.",
     [], "resolute stance"),
    ("sasha", "Шеф будет в ярости, если узнает!",
     "The chef will be furious if he finds out!",
     [], "warning of danger"),
    ("anya", "Я спрячу гуся в безопасное место.",
     "I will hide the goose in a safe place.",
     [(271, "перепрячу")], "protective plan"),
    ("sasha", "Только делай это очень осторожно.",
     "Just do it very carefully.",
     [], "advising caution"),
    ("anya", "Его чуть не нашли гости.",
     "The guests almost found him.",
     [(267, "в зал"), (270, "тебя здесь найдут")], "close call"),
    ("sasha", "Унеси его с кухни прямо сейчас!",
     "Carry him away from the kitchen right now!",
     [(265, "сюда и позвала")], "order to move"),
    ("anya", "Я найду для него тёплый угол.",
     "I will find a warm corner for him.",
     [(271, "перепрячу")], "safe refuge"),
    ("sasha", "И возвращайся скорее к работе!",
     "And return to work quickly!",
     [(266, "Спасибо большое")], "back to shifts"),
]

OPENER = "Now let us walk through each line together to understand every Russian word."

WALK = [
    (0, "Саша, иди скорее сюда!",
     "'Sasha, come here quickly!' An imperative urging a coworker to approach immediately."),
    (1, "Что случилось, Настя?",
     "'What happened, Nastya?' A direct question asking about the unexpected situation."),
    (2, "Посмотри, в коробке сидит живой гусь!",
     "'Look, a live goose is sitting in the box!' The imperative draws attention to the hidden bird."),
    (3, "Откуда здесь взялся этот гусь?",
     "'Where did this goose come from?' An interrogative phrase asking about the origin of the animal."),
    (4, "Шеф хотел приготовить из него блюдо.",
     "'The chef wanted to prepare a dish out of it.' The past-tense verb explains the culinary fate of the bird."),
    (5, "Ты решила спасти эту птицу?",
     "'Did you decide to save this bird?' The feminine past verb asks about her rescue intentions."),
    (6, "Да, я не могу его бросить.",
     "'Yes, I cannot abandon him.' The modal verb with negated infinitive expresses moral duty."),
    (7, "Шеф будет в ярости, если узнает!",
     "'The chef will be furious if he finds out!' A conditional warning describing Barinov's temper."),
    (8, "Я спрячу гуся в безопасное место.",
     "'I will hide the goose in a safe place.' The future verb states her plan to protect the animal."),
    (9, "Только делай это очень осторожно.",
     "'Just do it very carefully.' Adverbs of degree and manner urge extreme stealth."),
    (10, "Его чуть не нашли гости.",
     "'The guests almost found him.' The adverb meaning nearly explains the close call."),
    (11, "Унеси его с кухни прямо сейчас!",
     "'Carry him away from the kitchen right now!' A sharp imperative telling her to remove the bird."),
    (12, "Я найду для него тёплый угол.",
     "'I will find a warm corner for him.' The future verb promises a cozy hiding spot."),
    (13, "И возвращайся скорее к работе!",
     "'And return to work quickly!' A practical reminder to resume waitressing duties."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Nastya successfully hustles the live goose out of the prep area, determined to keep him safe until her shift ends. "
    "Meanwhile in the dining hall, Chef Barinov is about to present a special birthday dish. See you in the next scene!"
)

CLOSING = ("anya", "Я обязательно спасу этого гуся.")
