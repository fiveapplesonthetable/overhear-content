"""Scene 04 — Walking to Work (s01e13)."""

ID = "kukhnya-s01e13-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 4
TITLE = "Тайный роман  (A Secret Romance)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Вика",
    "kostya": "Макс",
}

INTRO = (
    "As they commute to the restaurant, Victoria suggests they shouldn't arrive together "
    "to avoid damaging her professional reputation, though Max mockingly agrees."
)

STORY = [
    ("anya", "Давай отсюда ты дойдёшь пешком.",
     "Let's have you walk from here.",
     [(41, "Давай отсюда ты дойдешь пешком.")], "Vika stops the car"),

    ("anya", "Нам не надо появляться на работе вместе.",
     "We do not need to appear at work together.",
     [(43, "будет не очень хорошо, если мы боимся на работе вместе.")], "Vika explains her reasoning"),

    ("kostya", "Ты совершенно права, Вика.",
     "You are absolutely right, Vika.",
     [(44, "Это значит, ты права.")], "Max nods with fake seriousness"),

    ("kostya", "Это может нанести урон моей репутации.",
     "It could cause damage to my reputation.",
     [(44, "Это может нанести серьезный урон моей репутации.")], "Max sighs dramatically"),

    ("anya", "Макс, ты уверен, что это правильно?",
     "Max, are you sure that this is right?",
     [(45, "Макс! Макс, ты уверен, что все это правильно?")], "Vika looks at him doubtfully"),

    ("kostya", "Посмотрим.",
     "We will see.",
     [(46, "Посмотрим.")], "Max smiles slightly"),

    ("anya", "Я не хочу лишних вопросов от шефа.",
     "I do not want extra questions from the boss.",
     [], "Vika sighs softly"),

    ("kostya", "Никто не узнает про наш тайный роман.",
     "No one will find out about our secret romance.",
     [], "Max reassures her"),

    ("anya", "В этом ресторане люди очень любят сплетни.",
     "In this restaurant people really love gossip.",
     [], "Vika warns him"),

    ("kostya", "Я буду молчать и просто готовить еду.",
     "I will keep quiet and just cook food.",
     [], "Max promises faithfully"),

    ("anya", "Тогда иди первым, а я пойду потом.",
     "Then you go first, and I will go later.",
     [], "Vika makes a plan"),

    ("kostya", "Хорошо, увидимся на кухне через десять минут.",
     "Good, see you in the kitchen in ten minutes.",
     [], "Max agrees and walks away"),
]

OPENER = "Let's join Max and Vika as they discuss their arrival at work."

WALK = [
    (0, None,
     "'Let's have you walk from here.' Vika suggests they separate before reaching the restaurant."),
    (1, None,
     "'We do not need to appear at work together.' She worries about workplace gossip."),
    (2, None,
     "'You are absolutely right, Vika.' Max pretends to agree completely with her concern."),
    (3, None,
     "'It could cause damage to my reputation.' He jokingly twists her words about professionalism."),
    (4, None,
     "'Max, are you sure that this is right?' Vika questions if hiding is the best choice."),
    (5, None,
     "'We will see.' Max shrugs calmly as he prepares to walk."),
    (6, None,
     "'I do not want extra questions from the boss.' Vika wants to avoid any unnecessary office drama."),
    (7, None,
     "'No one will find out about our secret romance.' Max promises to keep their special relationship hidden."),
    (8, None,
     "'In this restaurant people really love gossip.' Vika knows how quickly rumors spread among the staff."),
    (9, None,
     "'I will keep quiet and just cook food.' Max assures her he will focus entirely on his duties."),
    (10, None,
     "'Then you go first, and I will go later.' She decides they must enter the building at different times."),
    (11, None,
     "'Good, see you in the kitchen in ten minutes.' Max accepts the clever plan and begins his short walk."),
]

TRANSITION = "Now let's listen to Vika and Max talk about their arrival once again."

OUTRO = "Trying to keep their romance a secret, they agree to enter the restaurant separately."

CLOSING = ("kostya", "Хорошо, увидимся на кухне через десять минут.")
