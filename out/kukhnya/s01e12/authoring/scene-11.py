ID = "kukhnya-s01e12-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 11
TITLE = "Запрет на отношения  (Ban on Relationships)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 89-100. Victoria catches Max in the dining room and addresses the waitstaff, "
    "imposing an immediate ban on romantic workplace relationships."
)

INTRO = (
    "In the dining room of Claude Monet, Victoria catches Max loitering near the bar "
    "and sends him back to work. She then gathers the waitstaff to make a serious announcement, "
    "imposing a strict ban on workplace romances to ensure total focus during difficult times. "
    "Let us listen to their dialogue in Russian first."
)

STORY = [
    ("anya", "Макс, что ты здесь делаешь?",
     "Max, what are you doing here?",
     [(89, "А ты что здесь делаешь?")], "adapted"),
    ("max", "Я принёс свежие апельсины к бару.",
     "I brought fresh oranges to the bar.",
     [(90, "Я апельсины к бару принес.")], "adapted"),
    ("anya", "Вот и занимайся своими апельсинами на кухне!",
     "Then attend to your oranges in the kitchen!",
     [(91, "Вот и занимайся апельсинами.")], "adapted"),
    ("max", "Хорошо, я уже ухожу обратно.",
     "All right, I am already leaving.",
     [], "new"),
    ("anya", "Так, все официанты собрались здесь?",
     "So, have all the waitstaff gathered here?",
     [(92, "Так, все тут? Да.")], "adapted"),
    ("max", "Да, все слушают тебя очень внимательно.",
     "Yes, everyone is listening to you very attentively.",
     [], "new"),
    ("anya", "С сегодняшнего дня у нас строгий запрет.",
     "Starting today we have a strict ban.",
     [(93, "С сегодняшнего дня у нас вводится запрет")], "adapted"),
    ("max", "Какой ещё запрет в нашем ресторане?",
     "What sort of ban in our restaurant?",
     [], "new"),
    ("anya", "Запрещены любые личные отношения на работе.",
     "Any personal relationships at work are forbidden.",
     [(93, "запрет на личные отношения на"), (94, "работе.")], "adapted"),
    ("max", "Но зачем нам такое новое правило?",
     "But why do we need such a new rule?",
     [], "new"),
    ("anya", "Сейчас у ресторана очень сложное время.",
     "Now the restaurant has very difficult times.",
     [(95, "У нас сложный период.")], "adapted"),
    ("anya", "Вы должны думать только о работе!",
     "You must think only about work!",
     [(96, "вы думали о работе, а не о посторонних вещах.")], "adapted"),
    ("max", "А что будет за нарушение правила?",
     "And what will happen for breaking the rule?",
     [(98, "За нарушение этого правила увольнение.")], "adapted"),
    ("anya", "За нарушение этого правила будет увольнение!",
     "For breaking this rule there will be dismissal!",
     [(98, "За нарушение этого правила увольнение.")], "adapted"),
]

OPENER = "Now let us examine the strict announcement line by line."

WALK = [
    (0, None,
     "'Max, what are you doing here?' -- Victoria questions Max about his presence in the dining room."),
    (1, None,
     "'I brought fresh oranges to the bar.' -- Max explains that he was delivering fruit for drinks."),
    (2, None,
     "'Then attend to your oranges in the kitchen!' -- The manager tells him to return to kitchen work."),
    (3, None,
     "'All right, I am already leaving.' -- The young cook agrees to head back to the kitchen."),
    (4, None,
     "'So, have all the waitstaff gathered here?' -- Victoria checks that the whole team is present."),
    (5, None,
     "'Yes, everyone is listening to you very attentively.' -- Max confirms that all the servers are ready."),
    (6, None,
     "'Starting today we have a strict ban.' -- Victoria announces a new company policy for everyone."),
    (7, None,
     "'What sort of ban in our restaurant?' -- Max asks about the unexpected workplace restriction."),
    (8, None,
     "'Any personal relationships at work are forbidden.' -- The manager declares romance strictly prohibited."),
    (9, None,
     "'But why do we need such a new rule?' -- The cook wonders about the motivation behind the restriction."),
    (10, None,
     "'Now the restaurant has very difficult times.' -- Victoria explains that the business faces hardships."),
    (11, None,
     "'You must think only about work!' -- She demands undivided attention and focus from the staff."),
    (12, None,
     "'And what will happen for breaking the rule?' -- Max inquires about the penalty for noncompliance."),
    (13, None,
     "'For breaking this rule there will be dismissal!' -- Victoria warns that violators will lose their jobs."),
]

TRANSITION = "Now let us listen to Victoria and Max once more."
OUTRO = (
    "Victoria establishes a strict ban on office romances at Claude Monet, "
    "setting the stage for tension and clandestine schemes among the staff."
)
CLOSING = ("anya", "За нарушение этого правила будет увольнение!")
