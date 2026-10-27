ID = "kukhnya-s01e16-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 3
TITLE = "Ответный удар  (Strike Back)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Дмитрий', 'leva': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Realizing that the neighboring Italian restaurant, Arcobaleno, ordered the fake fire inspection, Dmitry decides to take revenge. He angrily calls the immigration service with a fake complaint against his rivals. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Вы хотите войну?",
     "Do you want a war?",
     [(27, 'Война и хотите, будет вам война.')], "adapted"),
    ("anya", "Будет вам война.",
     "There will be a war for you.",
     [(27, 'будет вам война.')], "adapted"),
    ("anya", "Алло, добрый день.",
     "Hello, good afternoon.",
     [(28, 'Алло, за что вам, интересно, деньги платят в вашем ФМСе?')], "adapted"),
    ("anya", "За что вам платят деньги?",
     "For what do they pay you money?",
     [(28, 'за что вам, интересно, деньги платят в вашем ФМСе?')], "adapted"),
    ("anya", "Вы куда смотрите?",
     "Where are you looking?",
     [(29, 'Вы куда смотрите?')], "adapted"),
    ("anya", "В моём дворе мигранты.",
     "There are migrants in my courtyard.",
     [(29, 'В моем дворе гастарбайтеры из ресторана')], "adapted"),
    ("anya", "Из ресторана Аркабалена.",
     "From the restaurant Arcobaleno.",
     [(30, 'Аркабалена')], "adapted"),
    ("anya", "Они режут живого барана.",
     "They are slaughtering a live ram.",
     [(30, 'барана режут живого.')], "adapted"),
    ("anya", "А вы там спите?",
     "And are you sleeping there?",
     [(31, 'А вы что, там спите?')], "adapted"),
    ("anya", "Приезжайте быстро.",
     "Come quickly.",
     [], "new"),
    ("anya", "Аркабалена.",
     "Arcobaleno.",
     [(32, 'Аркабалена.')], "adapted"),
    ("leva", "Что ты делаешь?",
     "What are you doing?",
     [], "new"),
    ("anya", "Я решаю наши проблемы.",
     "I am solving our problems.",
     [], "new"),
    ("leva", "Молодец, так держать.",
     "Well done, keep it up.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Do you want a war?' -- The speaker makes the statement."),
    (1, None,
     "'There will be a war for you.' -- The speaker makes the statement."),
    (2, None,
     "'Hello, good afternoon.' -- The speaker makes the statement."),
    (3, None,
     "'For what do they pay you money?' -- The speaker makes the statement."),
    (4, None,
     "'Where are you looking?' -- The speaker makes the statement."),
    (5, None,
     "'There are migrants in my courtyard.' -- The speaker makes the statement."),
    (6, None,
     "'From the restaurant Arcobaleno.' -- The speaker makes the statement."),
    (7, None,
     "'They are slaughtering a live ram.' -- The speaker makes the statement."),
    (8, None,
     "'And are you sleeping there?' -- The speaker makes the statement."),
    (9, None,
     "'Come quickly.' -- The speaker makes the statement."),
    (10, None,
     "'Arcobaleno.' -- The speaker makes the statement."),
    (11, None,
     "'What are you doing?' -- The speaker makes the statement."),
    (12, None,
     "'I am solving our problems.' -- The speaker makes the statement."),
    (13, None,
     "'Well done, keep it up.' -- The speaker makes the statement."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("leva", "Молодец, так держать.")
