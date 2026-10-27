ID = "kukhnya-s01e09-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 2
TITLE = "Семейный выбор  (A Family Choice)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 38-82. In the dining room of Claude Monet, Victoria and Chef Barinov argue about "
    "babysitting Barinov's young daughter Alisa."
)

INTRO = (
    "In the dining room of Claude Monet, restaurant administrator Victoria agrees to watch her young niece Alisa "
    "during a busy shift. But when Chef Viktor Barinov spots his ex-wife and daughter, an emotional argument "
    "erupts over who should care for the girl. Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Виктор, у меня сегодня много работы.",
     "Viktor, I have a lot of work today.",
     [(38, "у меня еще сегодня банкет.")], "adapted"),
    ("chef", "В чём дело, дорогая Виктория?",
     "What is the matter, dear Victoria?",
     [(70, "в чем дело?")], "adapted"),
    ("anya", "Сестра попросила меня посидеть с Алисой.",
     "My sister asked me to babysit Alisa.",
     [(71, "Алиса побудет с тетей.")], "adapted"),
    ("chef", "А почему с тобой, а не со мной?",
     "And why with you and not with me?",
     [(72, "А почему с тетей, а не с папой?")], "adapted"),
    ("anya", "Потому что ты всегда занят на кухне.",
     "Because you are always busy in the kitchen.",
     [], "new"),
    ("chef", "Я хочу сам провести время с дочерью.",
     "I want to spend time with my daughter myself.",
     [], "new"),
    ("anya", "Алиса, с кем ты хочешь остаться?",
     "Alisa, who do you want to stay with?",
     [(75, "ты хочешь остаться с папой или с теткой")], "adapted"),
    ("chef", "Дочка хочет остаться со своим папой.",
     "My daughter wants to stay with her dad.",
     [(77, "Но останусь с папой.")], "adapted"),
    ("anya", "Ну вот, вы всё решили сами.",
     "Well, you decided everything yourselves.",
     [(78, "Ну вот и решили.")], "adapted"),
    ("chef", "Я куплю ей вкусный сладкий шоколад.",
     "I will buy her delicious sweet chocolate.",
     [(80, "Я тебе шоколадку дам.")], "adapted"),
    ("anya", "Помни, ей нельзя есть шоколад.",
     "Remember, she is not allowed to eat chocolate.",
     [(81, "Ей нельзя шоколадку.")], "adapted"),
    ("chef", "Не волнуйся, Вика, я всё знаю.",
     "Do not worry, Vika, I know everything.",
     [(81, "Я знаю.")], "adapted"),
    ("anya", "Смотри за ней внимательно до вечера.",
     "Watch her attentively until the evening.",
     [(82, "Вика, до вечера.")], "adapted"),
]

OPENER = "Now let's examine Victoria and Chef Barinov's conversation line by line."

WALK = [
    (0, None,
     "'Viktor, I have a lot of work today.' -- Victoria explains that she has a heavy workload during the shift."),
    (1, None,
     "'What is the matter, dear Victoria?' -- Chef Barinov asks politely what is happening."),
    (2, None,
     "'My sister asked me to babysit Alisa.' -- Victoria tells him she agreed to look after her young niece."),
    (3, None,
     "'And why with you and not with me?' -- Barinov questions why his own child should not stay with him."),
    (4, None,
     "'Because you are always busy in the kitchen.' -- Victoria reminds him of his demanding culinary duties."),
    (5, None,
     "'I want to spend time with my daughter myself.' -- The chef insists on spending personal time with his child."),
    (6, None,
     "'Alisa, who do you want to stay with?' -- Victoria asks the girl directly to make her choice."),
    (7, None,
     "'My daughter wants to stay with her dad.' -- Barinov proudly announces that Alisa chose her father."),
    (8, None,
     "'Well, you decided everything yourselves.' -- Victoria accepts the decision with resigned acceptance."),
    (9, None,
     "'I will buy her delicious sweet chocolate.' -- Barinov immediately promises a treat to his daughter."),
    (10, None,
     "'Remember, she is not allowed to eat chocolate.' -- Victoria warns him about the girl's strict dietary rules."),
    (11, None,
     "'Do not worry, Vika, I know everything.' -- The chef confidently brushes aside Victoria's concerns."),
    (12, None,
     "'Watch her attentively until the evening.' -- Victoria gives her final warning to look after Alisa carefully."),
]

TRANSITION = "Now let's listen to the dining room conversation again without interruption."
OUTRO = (
    "With Alisa eagerly choosing to stay with her father, Chef Barinov takes charge of his daughter for the day, "
    "promising to keep her entertained while Victoria returns to managing the dining room."
)
CLOSING = ("anya", "Смотри за ней внимательно до вечера.")
