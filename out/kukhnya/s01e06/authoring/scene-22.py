"""Scene 22 — The Truffle Bill (s01e06, 00:21:53–00:23:14)."""

ID = "kukhnya-s01e06-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 22
TITLE = "Счёт за трюфели  (The Truffle Bill)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 298-303. Max confesses to throwing away expensive black truffles because in Voronezh "
    "he only knew truffles as chocolate candies. Chef Barinov forgives him but hands him the lavish dinner bill."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
}

INTRO = (
    "After Rodion Sergeyevich rescues the discarded black truffles from the trash, "
    "Chef Viktor Barinov confronts rookie cook Max about how such expensive ingredients ended up in the bin. "
    "Max sheepishly confesses his provincial culinary ignorance, prompting the head chef to deliver an unforgettable lesson. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Макс, почему редкие трюфели оказались на помойке?",
     "Max, why did rare truffles end up in the dumpster?",
     [], "Barinov demands answers"),

    ("anya", "Шеф, извините меня, пожалуйста!",
     "Chef, forgive me, please!",
     [(298, "Шеф, извините")], "Max pleads forgiveness"),

    ("anya", "Я раньше никогда не видел трюфелей.",
     "I have never seen truffles before.",
     [(298, "я никогда не видел трюфелей")], "Confessing ignorance"),

    ("chef", "Как ты мог выбросить такое сокровище?",
     "How could you throw away such a treasure?",
     [], "Barinov vents shock"),

    ("anya", "В Воронеже трюфели — это только конфеты!",
     "In Voronezh, truffles are only candies!",
     [(299, "В Воронеже трюфеля это только конфеты.")], "Provincial excuse"),

    ("chef", "Конфеты? Это самый дорогой гриб!",
     "Candies? This is the most expensive mushroom!",
     [(300, "Трюфели?")], "Culinary correction"),

    ("anya", "Я подумал, что они испортились.",
     "I thought that they had spoiled.",
     [], "Explaining motive"),

    ("chef", "Хорошо, что бездомный вернул их нам.",
     "Good thing the homeless man returned them to us.",
     [(293, "Кто-то выбросил дивные трюфели")], "Relieved discovery"),

    ("chef", "Ладно, я сегодня очень добрый.",
     "Alright, I am very kind today.",
     [(301, "Ладно, я сегодня добрый.")], "Barinov shows mercy"),

    ("chef", "Мы успешно прошли сложную проверку.",
     "We successfully passed the difficult inspection.",
     [(302, "Мы проверку прошли.")], "Celebrating success"),

    ("chef", "Но счёт за его ужин оплатишь ты.",
     "But you will pay the bill for his dinner.",
     [(302, "счет за ужин Родиона Сергеевича надо будет оплатить")], "The catch"),

    ("anya", "Двадцать две тысячи рублей?!",
     "Twenty-two thousand roubles?!",
     [(303, "Двадцать две тысячи?")], "Max gasps at total"),

    ("chef", "Вот так ты запомнишь этот урок!",
     "This is how you will remember this lesson!",
     [], "Barinov concludes lesson"),
]

OPENER = "Now let's examine Barinov and Max's truffle discussion line by line."

WALK = [
    (0, None,
     "'Max, why did rare truffles end up in the dumpster?' Barinov demands an explanation for the discarded delicacy."),
    (1, None,
     "'Chef, forgive me, please!' Max stammers an apology while realizing the gravity of his mistake."),
    (2, None,
     "'I have never seen truffles before.' The young rookie explains his complete unfamiliarity with gourmet fungi."),
    (3, None,
     "'How could you throw away such a treasure?' Viktor Barinov cannot fathom wasting such an expensive ingredient."),
    (4, None,
     "'In Voronezh, truffles are only candies!' Max reveals his provincial background and culinary innocence."),
    (5, None,
     "'Candies? This is the most expensive mushroom!' The head chef sets the record straight with exasperation."),
    (6, None,
     "'I thought that they had spoiled.' Max explains his misguided reasoning for tossing them into the bin."),
    (7, None,
     "'Good thing the homeless man returned them to us.' Barinov acknowledges the stroke of unexpected luck."),
    (8, None,
     "'Alright, I am very kind today.' The chef shows rare leniency toward the frightened newcomer."),
    (9, None,
     "'We successfully passed the difficult inspection.' Barinov celebrates dodging the health inspector's sanctions."),
    (10, None,
     "'But you will pay the bill for his dinner.' The chef delivers the financial catch with a sly grin."),
    (11, None,
     "'Twenty-two thousand roubles?!' Max gasps in horror at the price of the celebratory meal."),
    (12, None,
     "'This is how you will remember this lesson!' Barinov ensures the rookie will never forget what a truffle looks like."),
]

TRANSITION = "Now let's listen to the chef and Max once more without interruption."

OUTRO = (
    "Max learns a costly lesson about luxury mushrooms, leaving Claude Monet with a hefty dinner tab."
)

CLOSING = ("chef", "Вот так ты запомнишь этот урок!")
