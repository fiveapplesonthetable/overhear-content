ID = "kukhnya-s01e11-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 16
TITLE = "Тревога в зале  (Alarm in the Dining Room)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 189-191. Victoria and Chef Viktor panic when a female diner runs to the restroom feeling nauseous, "
    "fearing an outbreak of food poisoning in the middle of a rumored critic visit."
)

INTRO = (
    "In the elegant dining room of Claude Monet, Victoria and Chef Viktor watch in shock "
    "as a young female diner suddenly rushes to the restroom. Terrified that their food has "
    "caused food poisoning right when a secret restaurant critic is expected, they scramble "
    "to assess the danger. Let us listen to their anxious exchange in Russian first."
)

STORY = [
    ("chef", "Куда так быстро убежала эта девушка?",
     "Where did this girl run so quickly?",
     [(189, "Где она?")], "adapted"),
    ("anya", "Она сейчас побежала прямо в туалет.",
     "She just ran straight to the restroom.",
     [(189, "Она в туалете")], "adapted"),
    ("chef", "Ей вдруг стало плохо в зале?",
     "Did she suddenly feel ill in the dining room?",
     [], "new"),
    ("anya", "Да, её только что сильно тошнило.",
     "Yes, she was just feeling very nauseous.",
     [(190, "Ее сейчас так вырвало")], "adapted"),
    ("chef", "Неужели она отравилась нашей едой?",
     "Could she really have gotten poisoned by our food?",
     [(191, "отравилась, наверное")], "adapted"),
    ("anya", "Мы пока не знаем точной причины.",
     "We do not know the exact reason yet.",
     [], "new"),
    ("chef", "На кухне все продукты всегда свежие.",
     "In the kitchen all products are always fresh.",
     [], "new"),
    ("anya", "Но гостье стало плохо после обеда.",
     "But the guest felt ill after lunch.",
     [], "new"),
    ("chef", "А вдруг это тайный критик ресторана?",
     "What if this is a secret restaurant critic?",
     [], "new"),
    ("anya", "Тогда у нашего ресторана большие проблемы.",
     "Then our restaurant has big problems.",
     [], "new"),
    ("chef", "Нужно срочно всё проверить на кухне.",
     "We must urgently check everything in the kitchen.",
     [], "new"),
    ("anya", "Я пойду и узнаю её состояние.",
     "I will go and find out her condition.",
     [], "new"),
    ("chef", "Надеюсь, всё закончится хорошо для нас.",
     "I hope everything ends well for us.",
     [], "new"),
]

OPENER = "Now let us examine Victoria and Viktor's tense discussion line by line."

WALK = [
    (0, None,
     "'Where did this girl run so quickly?' -- The chef asks about the customer who fled her table."),
    (1, None,
     "'She just ran straight to the restroom.' -- Victoria explains that the woman dashed to the bathroom."),
    (2, None,
     "'Did she suddenly feel ill in the dining room?' -- The head chef asks if she developed sudden symptoms."),
    (3, None,
     "'Yes, she was just feeling very nauseous.' -- The manager confirms that the guest was severely sick."),
    (4, None,
     "'Could she really have gotten poisoned by our food?' -- The chef expresses deep horror over potential food poisoning."),
    (5, None,
     "'We do not know the exact reason yet.' -- Victoria prudently advises against jumping to conclusions."),
    (6, None,
     "'In the kitchen all products are always fresh.' -- The chef defends the high quality of their ingredients."),
    (7, None,
     "'But the guest felt ill after lunch.' -- Victoria notes that the timing looks suspicious."),
    (8, None,
     "'What if this is a secret restaurant critic?' -- Viktor voices his biggest paranoid fear."),
    (9, None,
     "'Then our restaurant has big problems.' -- The art director acknowledges the catastrophic stakes."),
    (10, None,
     "'We must urgently check everything in the kitchen.' -- The chef resolves to inspect every station immediately."),
    (11, None,
     "'I will go and find out her condition.' -- Victoria volunteers to check on the sick woman."),
    (12, None,
     "'I hope everything ends well for us.' -- Viktor wishes for a favorable resolution to the crisis."),
]

TRANSITION = "Now let us listen to the anxious conversation again without pause."
OUTRO = (
    "With fears of a culinary disaster mounting, Victoria heads off to investigate while "
    "Chef Viktor rushes to verify the cleanliness and quality of the kitchen dishes."
)
CLOSING = ("chef", "Надеюсь, всё закончится хорошо для нас.")
