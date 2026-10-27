ID = "kukhnya-s01e14-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 12
TITLE = "Слёзы на кухне  (Tears in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "louis": "anja"}
LABELS = {"anya": "Шеф", "louis": "Луи"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 175-178. Chef Viktor finds pastry chef Louis weeping in the kitchen. "
    "Viktor orders Louis to stop crying and finish the desserts, then yells at the crew to get to work."
)

INTRO = (
    "In the busy kitchen of Claude Monet, Chef Viktor notices pastry chef Louis weeping uncontrollably. "
    "Impatient with the emotional display and concerned about pending orders, Viktor orders Louis to get back to work. "
    "Let us listen to their sharp confrontation in Russian first."
)

STORY = [
    ("anya", "Луи, почему ты опять горько плачешь?",
     "Louis, why are you crying bitterly again?",
     [(175, "Луи.")], "adapted"),
    ("louis", "Шеф, у меня случилась страшная драма.",
     "Chef, a terrible drama happened to me.",
     [(176, "свой плач")], "adapted"),
    ("anya", "Прекрати этот глупый шум прямо сейчас!",
     "Stop this foolish noise right now!",
     [(176, "Прекрати, пожалуйста")], "adapted"),
    ("louis", "Моё нежное сердце разбито на куски.",
     "My tender heart is broken into pieces.",
     [], "new"),
    ("anya", "Быстро вытри слёзы и делай десерты.",
     "Quickly wipe your tears and make desserts.",
     [(176, "приступай, пожалуйста,"), (177, "к десертам.")], "adapted"),
    ("louis", "Я не могу сейчас печь сладкие пирожные.",
     "I cannot bake sweet cakes right now.",
     [], "new"),
    ("anya", "Наши важные гости давно ждут десерты!",
     "Our important guests have been waiting for desserts for a long time!",
     [], "new"),
    ("louis", "Хорошо, шеф, я начну готовить кремы.",
     "All right, chef, I will start making creams.",
     [], "new"),
    ("anya", "И прекрати свои постоянные пустые жалобы.",
     "And stop your constant empty complaints.",
     [], "new"),
    ("anya", "Эй, повара, почему вы все стоите?",
     "Hey, cooks, why are you all standing around?",
     [(177, "Что уставились")], "adapted"),
    ("louis", "Мы уже начинаем быстро делать заказы.",
     "We are already starting to prepare orders quickly.",
     [], "new"),
    ("anya", "Живее, лентяи, начинаем дружно работать!",
     "Move lively, sluggards, let us begin working together!",
     [(178, "Работаем!")], "adapted"),
    ("anya", "Работаем быстро, гости ждут свои заказы!",
     "Work quickly, guests are waiting for their orders!",
     [(178, "Работаем!")], "adapted"),
]

OPENER = "Now let us examine Viktor and Louis's kitchen dispute line by line."

WALK = [
    (0, None,
     "'Louis, why are you crying bitterly again?' -- Chef Viktor confronts his pastry cook over his excessive emotional tears."),
    (1, None,
     "'Chef, a terrible drama happened to me.' -- Louis laments his personal troubles while trying to work in the kitchen."),
    (2, None,
     "'Stop this foolish noise right now!' -- The head chef sternly demands quiet so that food preparation can resume."),
    (3, None,
     "'My tender heart is broken into pieces.' -- The distressed pastry chef dramatically describes his romantic sorrow."),
    (4, None,
     "'Quickly wipe your tears and make desserts.' -- Viktor firmly reminds Louis of his professional duty to bake sweets."),
    (5, None,
     "'I cannot bake sweet cakes right now.' -- Louis protests that his current mood prevents him from producing pastries."),
    (6, None,
     "'Our important guests have been waiting for desserts for a long time!' -- The boss emphasizes the urgent backlog of diner orders."),
    (7, None,
     "'All right, chef, I will start making creams.' -- Yielding to Viktor's strict authority, Louis agrees to begin work."),
    (8, None,
     "'And stop your constant empty complaints.' -- The chef insists on zero further whining during dinner service."),
    (9, None,
     "'Hey, cooks, why are you all standing around?' -- Viktor pivots to yell at the rest of the kitchen crew."),
    (10, None,
     "'We are already starting to prepare orders quickly.' -- The cooks scramble to resume cutting, chopping, and frying."),
    (11, None,
     "'Move lively, sluggards, let us begin working together!' -- Viktor rallies the entire kitchen into high gear."),
    (12, None,
     "'Work quickly, guests are waiting for their orders!' -- The fiery chef gives a final shout to motivate the team."),
]

TRANSITION = "Now let us listen to Viktor and Louis once again."
OUTRO = (
    "With Louis pressured back into pastry prep and the kitchen crew snapped to attention, "
    "the bustling restaurant kitchen resumes its normal chaotic rhythm."
)
CLOSING = ("anya", "Работаем быстро, гости ждут свои заказы!")
