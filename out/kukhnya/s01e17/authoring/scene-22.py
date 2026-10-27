# Authoring module for kukhnya s01e17 scene 22 (cue 326).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-22.py --out out/kukhnya/s01e17/scene-22.json

ID = "kukhnya-s01e17-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 22
TITLE = "Бокал для шефа  (A Glass for the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "nastya": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 326. In the restaurant kitchen, Chef Viktor asks Nastya for a glass to toast with the team."
)

INTRO = (
    "Standing by the kitchen counter after the conflict is resolved, Chef Viktor decides "
    "it is time to properly celebrate with his staff. He asks Nastya to bring a clean glass "
    "so he can pour a celebratory drink and raise a toast with Max. Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this kitchen conversation line by line."

STORY = [
    ("chef", "Настя, принеси мне чистый бокал.", "Nastya, bring me a clean glass.",
     [(326, "принеси бокал.")], "adapted"),
    ("nastya", "Сейчас принесу, шеф.", "I will bring it right away, chef.",
     [], "new"),
    ("chef", "Мы должны выпить за праздник.", "We must drink to the holiday.",
     [], "new"),
    ("anya", "Шеф, это очень приятно.", "Chef, this is very pleasant.",
     [], "new"),
    ("chef", "Наливай всем хорошее вино.", "Pour good wine for everyone.",
     [], "new"),
    ("nastya", "Вот ваш бокал, шеф.", "Here is your glass, chef.",
     [], "new"),
    ("chef", "Спасибо, Настя, молодец.", "Thank you, Nastya, well done.",
     [], "new"),
    ("anya", "Какой красивый бокал!", "What a beautiful glass!",
     [], "new"),
    ("chef", "Для хорошего вина нужен красивый бокал.", "For good wine one needs a beautiful glass.",
     [], "new"),
    ("nastya", "Я принесла бокалы для всех.", "I brought glasses for everyone.",
     [], "new"),
    ("anya", "Теперь у всех есть бокалы.", "Now everyone has glasses.",
     [], "new"),
    ("chef", "Поднимите ваши бокалы.", "Raise your glasses.",
     [], "new"),
    ("chef", "Давайте выпьем за дружбу!", "Let us drink to friendship!",
     [], "new"),
]

WALK = [
    (0, None,
     "'Nastya, bring me a clean glass.' -- Chef Viktor calls for a glass to join the celebration."),
    (1, None,
     "'I will bring it right away, chef.' -- Nastya quickly responds to the order."),
    (2, None,
     "'We must drink to the holiday.' -- The chef insists on celebrating the occasion."),
    (3, None,
     "'Chef, this is very pleasant.' -- Max expresses his gratitude for the gesture."),
    (4, None,
     "'Pour good wine for everyone.' -- Viktor orders a generous pour for the staff."),
    (5, None,
     "'Here is your glass, chef.' -- Nastya hands him the clean glass."),
    (6, None,
     "'Thank you, Nastya, well done.' -- The chef praises her prompt assistance."),
    (7, None,
     "'What a beautiful glass!' -- Max admires the fine glassware on the counter."),
    (8, None,
     "'For good wine one needs a beautiful glass.' -- Viktor shares a rule of dining."),
    (9, None,
     "'I brought glasses for everyone.' -- Nastya makes sure that all cooks have one."),
    (10, None,
     "'Now everyone has glasses.' -- Max notes that the whole team is ready."),
    (11, None,
     "'Raise your glasses.' -- The chef rallies the room for a toast."),
    (12, None,
     "'Let us drink to friendship!' -- Viktor delivers a warm and unifying toast."),
]

TRANSITION = "Now let's listen to the kitchen scene again without interruption."
OUTRO = (
    "With glasses in hand, Chef Viktor and the kitchen crew prepare to drink together, "
    "enjoying a rare moment of camaraderie in Claude Monet."
)
CLOSING = ("chef", "Давайте выпьем за дружбу!")
