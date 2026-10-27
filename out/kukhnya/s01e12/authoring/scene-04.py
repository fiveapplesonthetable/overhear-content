"""Authoring module for Kukhnya s01e12 scene 04."""
from pathlib import Path

ID = "kukhnya-s01e12-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 4
TITLE = "Приступ аппендицита  (An Appendicitis Attack)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Саша", "max": "Макс"}
SOURCE_NAME = "Кухня (The Kitchen) S1.12"
SOURCE_FILE = Path("sources/kukhnya/s01/e12.ru.dual.srt")

INTRO = (
    "In the dining room near the waiter station, Max stages an elaborate medical emergency to get waitress Sasha's attention. "
    "Pretending to suffer from acute appendicitis, he draws her close before surprising her with cinema tickets. "
    "Let's listen to their playful encounter in Russian."
)

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the symptoms of distress, medical emergency phrasing, and casual conversational invitations."
)

STORY = [
    ("max", "Саша, привет! Как дела?", "Sasha, hi! How are things?", [(27, "Саш, привет.")], "greeting sasha"),
    ("anya", "Привет, поварёнок! Всё нормально.", "Hi, little cook! Everything is normal.", [(27, "О, привет, Ваваренок.")], "greeting back"),
    ("max", "Ой, ай! Как больно!", "Oh, ow! How painful!", [(28, "Ай!")], "faking pain"),
    ("anya", "Что с тобой случилось?", "What happened to you?", [(29, "Чего такое?")], "asking in concern"),
    ("max", "У меня сильно колет в боку.", "I have a sharp pain in my side.", [(30, "Чего-то букует.")], "describing pain"),
    ("anya", "С какой именно стороны?", "On which side exactly?", [(31, "С какой стороны?")], "checking side"),
    ("max", "Вот здесь, с правой стороны.", "Right here, on the right side.", [(31, "Да с правой.")], "pointing to right"),
    ("anya", "С правой? Это может быть аппендицит!", "On the right? That could be appendicitis!", [(32, "Слушай, с правой это аппендицит.")], "identifying appendicitis"),
    ("anya", "Давай я срочно вызову скорую?", "Shall I urgently call an ambulance?", [(33, "А давай скорую вызову?")], "offering ambulance"),
    ("max", "Нет, не надо никакой скорой!", "No, no need for any ambulance!", [(33, "Да не надо.")], "stopping her"),
    ("max", "Смотри, у меня два билета!", "Look, I have two tickets!", [(34, "О, билетики.")], "revealing tickets"),
    ("anya", "Что? Ты просто придурок, Макс!", "What? You are just a jerk, Max!", [(36, "Ну ты придурок.")], "scolding him"),
    ("max", "Пойдёшь со мной вечером в кино?", "Will you go to the movies with me tonight?", [(35, "Пойдешь")], "asking out"),
    ("anya", "Ладно, пойдём! До вечера, артист.", "All right, let's go! See you tonight, actor.", [(38, "Ладно, пойдем. Тогда до вечера.")], "accepting date"),
]

WALK = [
    (0, "Саша, привет! Как дела?",
     "'Sasha, hi! How are things?' Max greets Sasha with a friendly and casual tone."),
    (1, "Привет, поварёнок! Всё нормально.",
     "'Hi, little cook! Everything is normal.' Sasha replies with a cheerful and affectionate nickname."),
    (2, "Ой, ай! Как больно!",
     "'Oh, ow! How painful!' Max suddenly winces and clutches his abdomen in dramatic distress."),
    (3, "Что с тобой случилось?",
     "'What happened to you?' Sasha asks with immediate concern after seeing him doubled over."),
    (4, "У меня сильно колет в боку.",
     "'I have a sharp pain in my side.' Max claims to feel an agonizing stitch in his torso."),
    (5, "С какой именно стороны?",
     "'On which side exactly?' Sasha investigates the precise location of his reported discomfort."),
    (6, "Вот здесь, с правой стороны.",
     "'Right here, on the right side.' Max points directly to his lower right abdominal quadrant."),
    (7, "С правой? Это может быть аппендицит!",
     "'On the right? That could be appendicitis!' Sasha gasps with alarming medical suspicion."),
    (8, "Давай я срочно вызову скорую?",
     "'Shall I urgently call an ambulance?' Sasha reaches for her phone to summon emergency assistance."),
    (9, "Нет, не надо никакой скорой!",
     "'No, no need for any ambulance!' Max panics slightly as he stops her from dialing."),
    (10, "Смотри, у меня два билета!",
     "'Look, I have two tickets!' Max pulls the movie tickets from his pocket with a grin."),
    (11, "Что? Ты просто придурок, Макс!",
     "'What? You are just a jerk, Max!' Sasha realizes he staged the whole medical emergency."),
    (12, "Пойдёшь со мной вечером в кино?",
     "'Will you go to the movies with me tonight?' Max playfully extends the evening invitation."),
    (13, "Ладно, пойдём! До вечера, артист.",
     "'All right, let's go! See you tonight, actor.' Sasha smiles, agrees to the date, and heads back to work."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Sasha heads off to her tables with a laugh while Max celebrates the success of his clever theatrical ploy. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("max", "Мой хитрый план сработал идеально!")
