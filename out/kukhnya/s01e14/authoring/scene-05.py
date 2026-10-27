ID = "kukhnya-s01e14-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 5
TITLE = "Пьяный шеф  (The Drunk Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 48-64. Victoria intercepts a heavily intoxicated Chef Barinov in the corridor. "
    "Disgusted by his state, she forbids him from entering the dining room, but he stubbornly "
    "insists on inspecting the bar."
)

INTRO = (
    "In the corridor of Claude Monet, Victoria intercepts a heavily intoxicated Chef Barinov. "
    "Furious at his unprofessional state, she explicitly forbids him from entering the dining room, "
    "but the drunk chef stubbornly insists on conducting an inspection of the bar. "
    "Let us listen to their argument in Russian first."
)

STORY = [
    ("anya", "Шеф, зачем ты так сильно напился?",
     "Chef, why did you get so drunk?",
     [(50, "Ты зачем так нажирался?")], "adapted"),
    ("chef", "Я не напился, а выпил немного аперитива.",
     "I am not drunk, but drank a little aperitif.",
     [(51, "Не нажался,"), (52, "а употребил некоторое количество дежестива в качестве аперитива.")], "adapted"),
    ("anya", "Ты еле стоишь на своих ногах.",
     "You can barely stand on your feet.",
     [], "new"),
    ("chef", "Лицо ресторана прибыло, я готов встречать гостей!",
     "The face of the restaurant arrived, I am ready to welcome guests!",
     [(53, "Короче говоря, лицо ресторана доставлено, я готов вам торговать.")], "adapted"),
    ("anya", "В таком состоянии ты к гостям не выйдешь!",
     "In this state you will not go out to the guests!",
     [(54, "Нет, в таком состоянии ты к гостям не выйдешь.")], "adapted"),
    ("chef", "А ты замуж никогда не выйдешь.",
     "And you will never get married.",
     [(55, "А ты замуж не выйдешь,")], "adapted"),
    ("anya", "Хватит за меня так грубо хвататься.",
     "Stop grabbing me so roughly.",
     [(55, "если будешь так хвататься.")], "adapted"),
    ("chef", "Я должен лично проверить наш ресторан.",
     "I must personally check our restaurant.",
     [], "new"),
    ("anya", "Сделайте что-нибудь с этим пьяным чудовищем!",
     "Do something with this drunken monster!",
     [(59, "Пожалуйста, сделай что-нибудь с этим пьяным чудовищем,")], "adapted"),
    ("chef", "У меня появилась очень хорошая идея.",
     "I had a very good idea.",
     [(60, "Шеф, ну, а у меня идея."), (62, "У меня лучшая идея.")], "adapted"),
    ("anya", "Какая ещё может быть идея сейчас?",
     "What other idea can there be now?",
     [], "new"),
    ("chef", "А пойдёмте все вместе проинспектируем бар!",
     "Let us all together inspect the bar!",
     [(61, "Пойдемте проинспектируем бар."), (63, "А пойдем-ка проинспектируем бар.")], "adapted"),
]

OPENER = "Now let us examine Victoria and the chef's argument line by line."

WALK = [
    (0, None,
     "'Chef, why did you get so drunk?' -- Victoria is appalled by Barinov's intoxicated condition."),
    (1, None,
     "'I am not drunk, but drank a little aperitif.' -- The chef tries to downplay his heavy drinking."),
    (2, None,
     "'You can barely stand on your feet.' -- The manager points out his obvious lack of balance."),
    (3, None,
     "'The face of the restaurant arrived, I am ready to welcome guests!' -- Barinov proudly declares his readiness to work."),
    (4, None,
     "'In this state you will not go out to the guests!' -- Victoria strictly forbids him from entering the dining hall."),
    (5, None,
     "'And you will never get married.' -- The drunken chef throws a personal insult at her."),
    (6, None,
     "'Stop grabbing me so roughly.' -- Victoria pushes him away in disgust."),
    (7, None,
     "'I must personally check our restaurant.' -- Barinov insists on performing his managerial duties."),
    (8, None,
     "'Do something with this drunken monster!' -- Victoria begs the staff for help with him."),
    (9, None,
     "'I had a very good idea.' -- The chef suddenly announces a new plan."),
    (10, None,
     "'What other idea can there be now?' -- Victoria asks with deep exhaustion and dread."),
    (11, None,
     "'Let us all together inspect the bar!' -- Barinov decides to visit the bar for more alcohol."),
]

TRANSITION = "Now let us listen to their messy confrontation once again."
OUTRO = (
    "Despite Victoria's desperate attempts to hide the drunken chef from the VIP guests, "
    "Barinov stumbles off toward the bar, determined to cause more chaos."
)
CLOSING = ("chef", "А пойдёмте все вместе проинспектируем бар!")
