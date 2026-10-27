# Authoring module for kukhnya s01e17 scene 24 (cues 332-336).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-24.py --out out/kukhnya/s01e17/scene-24.json

ID = "kukhnya-s01e17-scene-24"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 24
TITLE = "Чистый лист  (A Clean Slate)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 332-336. Max and Kostya talk in the kitchen at night about honesty and starting over with a clean slate."
)

INTRO = (
    "Cleaning up the kitchen late at night, Max talks with Kostya about the difficult consequences of deception. "
    "Reflecting on his mistakes, Max resolves to leave the lies behind and start fresh with a clean slate. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this reflective conversation line by line."

STORY = [
    ("anya", "Сложно исправлять ошибки обмана.", "It is hard to fix the mistakes of deceit.",
     [(332, "Но самое сложное – это исправлять последствия вранья.")], "adapted"),
    ("kostya", "Ложь всегда создаёт новую ложь.", "A lie always creates a new lie.",
     [(333, "Ложь порождает новую ложь")], "adapted"),
    ("anya", "И найти выход бывает невозможно.", "And finding an exit can be impossible.",
     [(333, "и выбраться из этого невозможно.")], "adapted"),
    ("kostya", "Главное — говорить правду.", "The main thing is to speak the truth.",
     [(331, "Правда")], "adapted"),
    ("anya", "Надо верить в свои силы.", "One must believe in one's strength.",
     [(334, "Остается только верить в свои силы")], "adapted"),
    ("kostya", "И верить в себя настоящего.", "And believe in your true self.",
     [(334, "в себя настоящего.")], "adapted"),
    ("anya", "Я хочу начать всё заново.", "I want to start everything over.",
     [(335, "начинаешь все с чистого листа")], "adapted"),
    ("kostya", "Ты можешь всё исправить, Макс.", "You can fix everything, Max.",
     [(332, "исправлять")], "adapted"),
    ("anya", "Я начинаю всё с чистого листа.", "I am starting everything with a clean slate.",
     [(335, "начинаешь все с чистого листа")], "adapted"),
    ("kostya", "У тебя впереди хорошее будущее.", "You have a good future ahead.",
     [(335, "у тебя впереди")], "adapted"),
    ("anya", "Твоя судьба зависит только от тебя.", "Your destiny depends only on you.",
     [(336, "что сделаешь ты сам.")], "adapted"),
    ("kostya", "Мы верим в тебя, друг.", "We believe in you, friend.",
     [(334, "верить")], "adapted"),
    ("anya", "Спасибо, Костя, за твою поддержку.", "Thank you, Kostya, for your support.",
     [], "new"),
]

WALK = [
    (0, None,
     "'It is hard to fix the mistakes of deceit.' -- Max reflects on the painful results of deceit."),
    (1, None,
     "'A lie always creates a new lie.' -- Kostya agrees that dishonesty compounds."),
    (2, None,
     "'And finding an exit can be impossible.' -- Max notes how traps are formed by lies."),
    (3, None,
     "'The main thing is to speak the truth.' -- Kostya emphasizes the power of honesty."),
    (4, None,
     "'One must believe in one's strength.' -- Max finds inner resolve to carry on."),
    (5, None,
     "'And believe in your true self.' -- Kostya encourages him to stay authentic with others."),
    (6, None,
     "'I want to start everything over.' -- Max expresses a desire for redemption."),
    (7, None,
     "'You can fix everything, Max.' -- His loyal friend offers reassurance to him."),
    (8, None,
     "'I am starting everything with a clean slate.' -- Max commits to a fresh beginning."),
    (9, None,
     "'You have a good future ahead.' -- Kostya points toward positive possibilities for him."),
    (10, None,
     "'Your destiny depends only on you.' -- Max takes full ownership of his path."),
    (11, None,
     "'We believe in you, friend.' -- Kostya confirms the strength of their bond."),
    (12, None,
     "'Thank you, Kostya, for your support.' -- Max expresses deep appreciation for his loyalty."),
]

TRANSITION = "Now let's listen to the final kitchen scene again without interruption."
OUTRO = (
    "With renewed determination to be honest with himself and his friends, Max closes up the kitchen, "
    "ready to begin the next chapter on a clean slate."
)
CLOSING = ("anya", "Я начинаю всё с чистого листа.")
