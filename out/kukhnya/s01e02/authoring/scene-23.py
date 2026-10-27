"""Scene 23 — Hide the Knife (s01e02, 00:18:25–00:18:36)."""

ID = "kukhnya-s01e02-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 23
TITLE = "Спрячь нож  (Hide the Knife)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 245-248. Near the dishwashing area, Ainura frantically warns kitchen worker Jindi "
    "to hide the chef's knife before Barinov sees it and loses his temper."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "jindi": "anja",
}

LABELS = {
    "anya": "Айнура",
    "jindi": "Джинди",
}

INTRO = (
    "In the dishwashing corner of the kitchen, cleaner Ainura catches Jindi holding Chef Barinov's missing knife. "
    "Terrified of the chef's explosive anger, she urgently orders him to conceal the blade before anyone notices. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ой, Джинди, скорее спрячь этот нож!",
     "Oh, Jindi, hide this knife quickly!",
     [(245, "Джинди, спрячь нож")], "Ainura panics"),

    ("jindi", "Зачем мне прятать этот нож?",
     "Why should I hide this knife?",
     [], "Jindi is puzzled"),

    ("anya", "Это любимый нож нашего шефа!",
     "This is our chef's favorite knife!",
     [], "Ainura explains significance"),

    ("anya", "Шеф ищет его уже всё утро.",
     "The chef has been looking for it all morning.",
     [], "Search status"),

    ("jindi", "Я просто хотел помыть посуду.",
     "I simply wanted to wash dishes.",
     [], "Jindi's innocent intent"),

    ("anya", "Если шеф увидит нож, будет скандал!",
     "If the chef sees the knife, there will be a scandal!",
     [(246, "Если шеф увидит")], "Warning of explosion"),

    ("anya", "Он будет очень сильно кричать на нас.",
     "He will yell at us very loudly.",
     [], "Fear of chef's wrath"),

    ("jindi", "Что же мне теперь делать?",
     "What should I do now?",
     [], "Jindi asks for advice"),

    ("anya", "Положи нож обратно на стол.",
     "Put the knife back onto the table.",
     [], "Specific instruction"),

    ("anya", "Пусть шеф сам найдёт свой нож.",
     "Let the chef find his knife himself.",
     [(247, "Пусть он уже сам найдет.")], "Leave it to chef"),

    ("anya", "Спрячь его подальше отсюда, быстрее!",
     "Hide it further away from here, quickly!",
     [(247, "Спрячь, спрячь.")], "Urgent repetition"),

    ("jindi", "Хорошо, я сейчас всё уберу.",
     "Alright, I will put everything away now.",
     [(248, "Ну")], "Jindi complies"),

    ("anya", "Только никому ничего не говори!",
     "Just do not say anything to anyone!",
     [], "Ainura demands secrecy"),
]

OPENER = "Now let's examine Ainura and Jindi's tense kitchen exchange line by line."

WALK = [
    (0, None,
     "'Oh, Jindi, hide this knife quickly!' Ainura urgently warns Jindi about the dangerous object in his hands."),
    (1, None,
     "'Why should I hide this knife?' Jindi does not yet grasp why the blade causes such panic."),
    (2, None,
     "'This is our chef's favorite knife!' Ainura explains that Barinov has a special attachment to the tool."),
    (3, None,
     "'The chef has been looking for it all morning.' Ainura emphasizes how long the kitchen has been in turmoil."),
    (4, None,
     "'I simply wanted to wash dishes.' Jindi defends his innocent intentions at the washing station."),
    (5, None,
     "'If the chef sees the knife, there will be a scandal!' Ainura paints a terrifying picture of the chef's temper."),
    (6, None,
     "'He will yell at us very loudly.' Ainura warns of the intense shouting match that would follow."),
    (7, None,
     "'What should I do now?' Jindi asks for practical guidance to avoid trouble."),
    (8, None,
     "'Put the knife back onto the table.' Ainura advises him to return the blade to an open work surface."),
    (9, None,
     "'Let the chef find his knife himself.' Ainura prefers that Barinov stumble upon it naturally."),
    (10, None,
     "'Hide it further away from here, quickly!' Ainura reiterates her frantic demand to remove suspicion."),
    (11, None,
     "'Alright, I will put everything away now.' Jindi agrees to stash the knife out of sight."),
    (12, None,
     "'Just do not say anything to anyone!' Ainura swears Jindi to absolute secrecy."),
]

TRANSITION = "Now let's listen to Ainura and Jindi's conversation once more without interruption."

OUTRO = (
    "Ainura makes sure the knife is hidden from immediate sight, "
    "while Barinov continues hunting across the entire restaurant."
)

CLOSING = ("anya", "Только никому ничего не говори!")
