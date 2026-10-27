"""Scene 21 — Fire Across the Street (s01e12)."""

ID = "kukhnya-s01e12-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 21
TITLE = "Пожар напротив  (Fire Across the Street)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Сеня",
    "kostya": "Федя",
}

INTRO = (
    "As the kitchen staff take a quick smoke break, they suddenly notice that the brand new "
    "competing restaurant across the street is engulfed in flames."
)

STORY = [
    ("anya", "Эта сигарета уже горчит на вкус.",
     "This cigarette already tastes bitter.",
     [(278, "Горчит уже.")], "Senya frowns at his cigarette"),

    ("anya", "Да выбрось её скорее в урну.",
     "Just throw it out quickly into the trash bin.",
     [(278, "Да выбрось ее.")], "Senya advises his friend"),

    ("kostya", "Ладно, я хочу пойти в туалет.",
     "All right, I want to go to the bathroom.",
     [(279, "Ладно, я в туалет хочу.")], "Fedya turns to walk inside"),

    ("kostya", "Подожди, там это огонь, друзья!",
     "Wait, it is on fire over there, friends!",
     [(280, "Там это огонь, друзья.")], "Fedya suddenly stops and points"),

    ("anya", "Соседний ресторан горит прямо сейчас!",
     "The neighboring restaurant is burning right now!",
     [], "Senya stares in shock"),

    ("kostya", "Ты уверен, что это настоящий пожар?",
     "Are you sure that this is a real fire?",
     [], "Fedya squints his eyes"),

    ("anya", "Конечно, посмотри на этот чёрный дым.",
     "Of course, look at this black smoke.",
     [], "Senya points at the sky"),

    ("kostya", "Люди выбегают из здания на улицу.",
     "People are running out of the building onto the street.",
     [], "Fedya watches the crowd"),

    ("anya", "Нам надо срочно сказать об этом шефу.",
     "We urgently need to tell the boss about this.",
     [], "Senya turns toward the kitchen"),

    ("kostya", "Да, он должен знать про этот огонь.",
     "Yes, he must know about this fire.",
     [], "Fedya agrees immediately"),

    ("anya", "Бросай сигарету и пошли быстрее внутрь.",
     "Drop the cigarette and let's go inside faster.",
     [], "Senya rushes him"),

    ("kostya", "Я бегу за тобой, открывай дверь.",
     "I am running after you, open the door.",
     [], "Fedya follows closely"),
]

OPENER = "Let's join Senya and Fedya outside as they notice something alarming."

WALK = [
    (0, None,
     "'This cigarette already tastes bitter.' Senya complains about his smoke break."),
    (1, None,
     "'Just throw it out quickly into the trash bin.' He tosses the finished stub away."),
    (2, None,
     "'All right, I want to go to the bathroom.' Fedya decides to head back indoors."),
    (3, None,
     "'Wait, it is on fire over there, friends!' Fedya suddenly spots huge flames across the street."),
    (4, None,
     "'The neighboring restaurant is burning right now!' Senya stares in absolute disbelief at the burning building."),
    (5, None,
     "'Are you sure that this is a real fire?' Fedya asks nervously while looking at the flames."),
    (6, None,
     "'Of course, look at this black smoke.' Senya gestures toward the dark clouds above the roof."),
    (7, None,
     "'People are running out of the building onto the street.' Fedya observes the panicked evacuation in front of them."),
    (8, None,
     "'We urgently need to tell the boss about this.' Senya realizes they cannot just stand there doing nothing."),
    (9, None,
     "'Yes, he must know about this fire.' Fedya nods, recognizing the severity of the chaotic situation."),
    (10, None,
     "'Drop the cigarette and let's go inside faster.' Senya hurries back toward their own safe kitchen doors."),
    (11, None,
     "'I am running after you, open the door.' Fedya follows right behind his frightened coworker."),
]

TRANSITION = "Now let's listen to the cooks discover the fire once again."

OUTRO = "Shocked by the sudden blaze, the staff realize that their new rival is literally going up in smoke."

CLOSING = ("kostya", "Я бегу за тобой, открывай дверь.")
