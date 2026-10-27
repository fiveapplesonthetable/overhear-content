"""s01e06 scene 07: Шутки на кухне (Jokes in the Kitchen)."""

ID = "kukhnya-s01e06-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = "Шутки на кухне  (Jokes in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "luis": "anja"}
LABELS = {"anya": "Макс", "luis": "Луи"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"

INTRO = (
    "In the kitchen of Claude Monet, the staff must clean every corner ahead of a surprise health inspection. "
    "Pastry chef Louis playfully pretends to duel Max with a giant stick of sausage before they start wiping down the dusty storage shelves. "
    "Let's listen to their playful exchange in Russian first."
)

STORY = [
    ("luis", "Осторожно, ты пронзил меня своей колбасой!",
     "Careful, you impaled me with your sausage!",
     [(75, "Ты пронзил меня своей колбасой")], "dramatizing a fake duel"),
    ("anya", "Луи, перестань так громко кричать.",
     "Louis, stop screaming so loudly.",
     [], "trying to calm him down"),
    ("luis", "Скажи Марии, что я любил её!",
     "Tell Maria that I loved her!",
     [(76, "Скажи Марию, что я любил ее друг")], "feigning a tragic death"),
    ("anya", "Хватит умирать, нам нужно убирать кухню.",
     "Stop dying, we need to clean the kitchen.",
     [], "urging him to get to work"),
    ("luis", "Шеф заставляет нас мыть эти полки?",
     "Does Chef force us to wash these shelves?",
     [], "asking with mild reluctance"),
    ("anya", "Да, шеф требует идеальной чистоты везде.",
     "Yes, Chef demands perfect cleanliness everywhere.",
     [], "explaining the strict orders"),
    ("luis", "Тут пыль лежит уже целый год!",
     "Dust has been lying here for a whole year!",
     [], "commenting on the dirty shelves"),
    ("anya", "С открытия ресторана здесь никто не убирался.",
     "Since the restaurant opened nobody cleaned here.",
     [(77, "Тут, наверное, с открытия никто не убирался")], "confirming the neglect"),
    ("luis", "Тогда бери скорее тряпку и воду.",
     "Then take a rag and water quickly.",
     [], "handing over cleaning supplies"),
    ("anya", "Я готов, давай закончим эту работу.",
     "I am ready, let's finish this work.",
     [], "stepping up to the task"),
    ("luis", "Главное, чтобы шеф был очень доволен.",
     "The main thing is that Chef is very pleased.",
     [], "hoping to avoid trouble"),
    ("anya", "Точно, иначе нам сильно достанется!",
     "Exactly, otherwise we will really get it!",
     [], "agreeing with caution"),
]

OPENER = "Let's review this humorous kitchen exchange line by line."

WALK = [
    (0, None,
     "'Careful, you impaled me with your sausage!' Louis dramatically pretends to be mortally wounded in a playful duel."),
    (1, None,
     "'Louis, stop screaming so loudly.' Max tries to quiet the flamboyant French pastry chef."),
    (2, None,
     "'Tell Maria that I loved her!' Louis delivers an over-the-top final request as if taking his dying breath."),
    (3, None,
     "'Stop dying, we need to clean the kitchen.' Max brings him back to reality before the inspection begins."),
    (4, None,
     "'Does Chef force us to wash these shelves?' Louis sighs at the unglamorous cleaning assignment."),
    (5, None,
     "'Yes, Chef demands perfect cleanliness everywhere.' Max reminds him of Viktor Barinov's fierce standards."),
    (6, None,
     "'Dust has been lying here for a whole year!' Louis points out how thick the grime on the shelves really is."),
    (7, None,
     "'Since the restaurant opened nobody cleaned here.' Max guesses that these storage spaces have never been touched."),
    (8, None,
     "'Then take a rag and water quickly.' Louis gestures toward the bucket to get the chore started."),
    (9, None,
     "'I am ready, let's finish this work.' Max sets to work with practical determination."),
    (10, None,
     "'The main thing is that Chef is very pleased.' Louis hopes their hard work satisfies the temperamental head chef."),
    (11, None,
     "'Exactly, otherwise we will really get it!' Max agrees that displeasing Barinov carries severe consequences."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "After their playful banter, Max and Louis roll up their sleeves and tackle the dusty kitchen shelves. "
    "See you next time!"
)

CLOSING = ("anya", "Точно, иначе нам сильно достанется!")
