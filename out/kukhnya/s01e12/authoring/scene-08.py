"""s01e12 scene 08: Открытая кухня (The Open Kitchen)."""

ID = "kukhnya-s01e12-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 8
TITLE = "Открытая кухня  (The Open Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = "Cues 73-75. Chef Barinov discovers a newly installed glass wall turning his kitchen into a show kitchen, furiously protesting to Max."

INTRO = (
    "Entering the kitchen, Chef Viktor Barinov stops dead in his tracks upon discovering a massive new glass wall overlooking the dining room. "
    "When Max explains that Victoria installed the show kitchen window to attract customers, Barinov explodes with anger over being put on display like a circus act. "
    "Let's listen to their argument in Russian."
)

STORY = [
    ("anya", "Шеф, всё в полном порядке?", "Chef, is everything in complete order?",
     [(73, "все в порядке?")], "adapted"),
    ("chef", "Это что ещё за стеклянный аквариум?", "What kind of glass aquarium is this?",
     [(74, "Это что за аквариум?")], "adapted"),
    ("anya", "Это распоряжение Виктории Сергеевны, шеф.", "This is Victoria Sergeyevna's order, chef.",
     [(74, "это Виктория Сергеевна сказала")], "adapted"),
    ("chef", "Зачем нам эта прозрачная стена?", "Why do we need this transparent wall?",
     [], "new"),
    ("anya", "Она нужна для привлечения новых гостей.", "It is needed to attract new guests.",
     [(75, "для привлечения клиентов")], "adapted"),
    ("anya", "Это модный формат открытой кухни.", "This is a trendy open kitchen format.",
     [(75, "Называется «шоу-китчен»")], "adapted"),
    ("chef", "Повара не должны быть на арене!", "Cooks should not be in an arena!",
     [], "new"),
    ("anya", "Гости любят смотреть на процесс готовки.", "Guests love watching the cooking process.",
     [], "new"),
    ("chef", "Они будут видеть каждый наш шаг.", "They will see our every step.",
     [], "new"),
    ("anya", "Зато в ресторане станет больше посетителей.", "On the other hand, there will be more patrons in the restaurant.",
     [], "new"),
    ("chef", "Я не клоун в цирке, Макс.", "I am not a clown in a circus, Max.",
     [], "new"),
    ("anya", "Виктория Сергеевна всё уже решила сама.", "Victoria Sergeyevna has already decided everything herself.",
     [], "new"),
    ("chef", "Я сейчас же пойду поговорить с ней.", "I will go talk to her right now.",
     [], "new"),
]

OPENER = "Let's explore how Chef Barinov reacts to the controversial new show kitchen glass window."

WALK = [
    (1, None,
     "'What kind of glass aquarium is this?' A scornful exclamatory question mocking the newly installed transparent partition in the restaurant."),
    (4, None,
     "'It is needed to attract new guests.' An impersonal purpose construction explaining the marketing strategy behind the dining renovation."),
    (6, None,
     "'Cooks should not be in an arena!' An emphatic negative modal statement rejecting public display during culinary preparation."),
    (10, None,
     "'I am not a clown in a circus, Max.' A colorful metaphor asserting personal pride and refusing theatrical entertainment for patrons."),
]

TRANSITION = "Now, let's hear Chef Barinov express his outrage over the open kitchen once more."

OUTRO = (
    "Now you know how to react to unexpected changes, discuss restaurant renovations, and express professional pride in Russian. "
    "Listen for these vivid expressions in the following scene."
)

CLOSING = ("chef", "Кухня должна оставаться священным местом.")
