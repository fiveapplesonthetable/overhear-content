"""s01e16 scene 18: Метод дедукции (Method of Deduction)."""

ID = "kukhnya-s01e16-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 18
TITLE = "Метод дедукции  (Method of Deduction)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Луи", "kostya": "Инспектор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 260-269. The migration inspector approaches pastry chef Louis in the dining room and deduces from his habits that he works at the restaurant."

INTRO = (
    "Still searching the dining room for disguised employees, the migration inspector stops at the table of French pastry chef Louis. "
    "Like a seasoned detective, the inspector points out three telltale habits that prove Louis is actually a chef working at the restaurant rather than a guest. "
    "Let's listen to his clever deduction in Russian."
)

STORY = [
    ("kostya", "Можно посмотреть на ваши документы?", "May I look at your documents?",
     [(261, "ваши документы?")], "adapted"),
    ("anya", "Я просто обычный гость ресторана.", "I am just an ordinary guest of the restaurant.",
     [], "new"),
    ("kostya", "Нет, вы работаете здесь поваром.", "No, you work here as a chef.",
     [(261, "Вы же повар в этом ресторане")], "adapted"),
    ("anya", "Почему вы вдруг так решили?", "Why did you suddenly decide so?",
     [], "new"),
    ("kostya", "Вы очень внимательно смотрите на блюдо.", "You are looking at the dish very carefully.",
     [(262, "только повар может так придирчиво рассматривать")], "adapted"),
    ("kostya", "Вам эта еда совсем не нравится.", "You do not like this food at all.",
     [(263, "ему оно не понравится")], "adapted"),
    ("kostya", "Потому что готовил её другой повар.", "Because another chef cooked it.",
     [(264, "готовил-то его кто-то другой")], "adapted"),
    ("anya", "Я просто люблю хорошую кухню.", "I simply love good cuisine.",
     [], "new"),
    ("kostya", "Ещё вы постоянно трогаете свою голову.", "Also you are constantly touching your head.",
     [(265, "Вы все время трогаете голову")], "adapted"),
    ("kostya", "На работе вы всегда носите шапку.", "At work you always wear a cap.",
     [], "new"),
    ("kostya", "И вы совсем не пьёте вино.", "And you are not drinking the wine at all.",
     [(266, "Вы не прикоснулись вообще")], "adapted"),
    ("kostya", "Потому что на работе нельзя пить.", "Because at work one must not drink.",
     [(267, "потому что на работе пить")], "adapted"),
    ("anya", "Да, вы сказали чистую правду.", "Yes, you told the pure truth.",
     [], "new"),
]

OPENER = "Let's examine how the inspector uses observation to uncover Louis's true profession."

WALK = [
    (0, None,
     "'May I look at your documents?' A formal request used by an official during an inspection."),
    (2, None,
     "'No, you work here as a chef.' Russian uses the instrumental case for the profession after the verb to work."),
    (8, None,
     "'Also you are constantly touching your head.' A sharp observation pointing out a physical habit."),
    (11, None,
     "'Because at work one must not drink.' An explanation referencing workplace rules with an impersonal modal word."),
]

TRANSITION = "Now, let's listen to the inspector's deduction from start to finish."

OUTRO = (
    "Now you know how to ask for documents, describe someone's profession, and explain workplace rules in Russian. "
    "Listen to what happens next when the inspector escorts Louis away."
)

CLOSING = ("kostya", "Покажите мне ваш французский паспорт.")
