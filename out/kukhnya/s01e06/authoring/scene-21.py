"""Scene 21 — Scandal in the Restaurant (s01e06, 00:19:32–00:21:43)."""

ID = "kukhnya-s01e06-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 21
TITLE = "Скандал в ресторане  (Scandal in the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 277-284. Following a drunken brawl in the dining room involving writer Viktor Pelevin, "
    "Vika confronts Chef Viktor Barinov, who cynically considers the fight fantastic publicity."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Вика",
    "chef": "Шеф",
}

INTRO = (
    "Chaos erupts in the dining room of Claude Monet when an unruly guest starts a drunken brawl "
    "and accidentally punches famous novelist Viktor Pelevin. "
    "Furious about the scandal, administrator Vika confronts Chef Barinov in his office, "
    "only to discover that he views the entire debacle as a marketing triumph. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Виктор, в зале случился ужасный скандал.",
     "Viktor, a terrible scandal happened in the dining room.",
     [], "Vika reports catastrophe"),

    ("chef", "Успокойся, Вика, мы покажем видео проверке.",
     "Calm down, Vika, we will show the video to the inspection.",
     [(277, "покажем ему завтра записи с камеры")], "Barinov points to camera footage"),

    ("chef", "Мы наверняка успешно пройдём проверку.",
     "We will surely successfully pass the inspection.",
     [(278, "пройдем проверку")], "Barinov predicts passing inspection"),

    ("anya", "Но этот бродяга устроил настоящий кошмар!",
     "But this vagrant caused a real nightmare!",
     [(257, "каких-то бродяг")], "Vika decries the mess"),

    ("anya", "Он кричал и распугал всех гостей!",
     "He shouted and scared off all the guests!",
     [(280, "распугал гостей")], "Describing guests' flight"),

    ("anya", "А потом он избил писателя Пелевина!",
     "And then he beat up the writer Pelevin!",
     [(280, "этот алкаш избил Пелевина")], "The celebrity assault"),

    ("anya", "Неужели для тебя это полная ерунда?",
     "Is this really complete nonsense to you?",
     [(280, "это ерунда")], "Challenging Viktor's calm"),

    ("chef", "Конечно, это совсем не ерунда.",
     "Of course, this is not nonsense at all.",
     [(281, "Конечно, это не ерунда.")], "Viktor agrees gravely"),

    ("chef", "Это очень большое важное событие!",
     "This is a very big important event!",
     [(282, "Это большое важное событие.")], "Reframing the brawl"),

    ("anya", "И какая в этом польза ресторану?",
     "And what benefit is there in this for the restaurant?",
     [], "Vika expresses skepticism"),

    ("chef", "Теперь мы не просто хороший ресторан.",
     "Now we are not just a good restaurant.",
     [(283, "Теперь мы не просто хороший ресторан")], "Building up status"),

    ("chef", "Здесь дали по морде известному человеку!",
     "Here they punched a famous person in the face!",
     [(284, "в котором дали по морде")], "Cynical publicity point"),

    ("anya", "Ты всегда найдёшь повод для радости!",
     "You will always find a reason for joy!",
     [], "Vika throws up her hands"),
]

OPENER = "Now let's examine Vika and Chef Barinov's conversation line by line."

WALK = [
    (0, None,
     "'Viktor, a terrible scandal happened in the dining room.' Vika rushes to the office in a state of distress."),
    (1, None,
     "'Calm down, Vika, we will show the video to the inspection.' Barinov points out the surveillance footage will prove their innocence."),
    (2, None,
     "'We will surely successfully pass the inspection.' The chef confidently reassures his administrator."),
    (3, None,
     "'But this vagrant caused a real nightmare!' Vika reminds him of the utter chaos in the dining area."),
    (4, None,
     "'He shouted and scared off all the guests!' She highlights the immediate damage to their business."),
    (5, None,
     "'And then he beat up the writer Pelevin!' Vika is horrified that a celebrity author was attacked."),
    (6, None,
     "'Is this really complete nonsense to you?' She questions Barinov's dismissive attitude toward the catastrophe."),
    (7, None,
     "'Of course, this is not nonsense at all.' Viktor Barinov reveals his surprising perspective on the brawl."),
    (8, None,
     "'This is a very big important event!' The head chef views the incident as extraordinary publicity."),
    (9, None,
     "'And what benefit is there in this for the restaurant?' Vika asks with obvious skepticism."),
    (10, None,
     "'Now we are not just a good restaurant.' Viktor prepares to deliver his cynical punchline."),
    (11, None,
     "'Here they punched a famous person in the face!' Barinov boasts about the unique notoriety of their establishment."),
    (12, None,
     "'You will always find a reason for joy!' Vika sighs at the chef's uncanny ability to spin any disaster."),
]

TRANSITION = "Now let's listen to Vika and the chef discussing the scandal once more without interruption."

OUTRO = (
    "Despite the wild brawl in the dining room, Barinov remains confident that any publicity is good publicity."
)

CLOSING = ("anya", "Ты всегда найдёшь повод для радости!")
