ID = "kukhnya-s01e02-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = "Две стороны ресторана  (Two Sides of a Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-6. Before the start of the morning shift, Max and bartender Kostya discuss the stark contrast "
    "between how luxurious the restaurant appears to wealthy guests and the chaotic reality behind the scenes."
)

INTRO = (
    "Before Claude Monet opens for the day, newly hired cook Maksim Lavrov talks with his new friend, bartender Kostya. "
    "Max reflects on how elite dining looks glamorous from the dining room, but reveals stress and modest food behind the kitchen doors. "
    "Determined to prove himself, Max vows to show the head chef his true culinary skills. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "С одной стороны, я работаю в крутом ресторане.",
     "On the one hand, I work in a cool restaurant.",
     [(1, "С одной стороны, ты устроился в самый крутой")], "adapted"),
    ("kostya", "А с другой стороны, ты ешь обычные сосиски.",
     "And on the other hand, you eat ordinary sausages.",
     [(2, "не повлияло на качество твоего питания")], "adapted"),
    ("anya", "Наш шеф готовит самую вкусную еду.",
     "Our chef cooks the most delicious food.",
     [(1, "самый крутой и вкусный ресторан")], "adapted"),
    ("kostya", "Но на кухне всегда царит полный хаос.",
     "But total chaos always reigns in the kitchen.",
     [], "new"),
    ("anya", "Гости думают, что это самое спокойное место.",
     "Guests think this is the most peaceful place.",
     [(5, "в самом красивом и спокойном месте")], "adapted"),
    ("kostya", "Они никогда не узнают правду о нас.",
     "They will never know the truth about us.",
     [(4, "вы никогда не узнаете, как на самом деле")], "adapted"),
    ("anya", "Каждый клиент считает себя важным человеком.",
     "Every customer considers themselves an important person.",
     [(3, "вы уважаемые гости элитного ресторана")], "adapted"),
    ("kostya", "А мы просто наливаем им вино.",
     "And we simply pour them wine.",
     [], "new"),
    ("anya", "Работа на кухне очень трудная и нервная.",
     "Work in the kitchen is very hard and nerve-wracking.",
     [], "new"),
    ("kostya", "Зато здесь никогда не бывает скучно!",
     "On the other hand, it's never boring here!",
     [], "new"),
    ("anya", "Скоро начинается наша утренняя смена.",
     "Our morning shift is starting soon.",
     [], "new"),
    ("kostya", "Тогда готовься к новому рабочему дню!",
     "Then prepare for a new workday!",
     [], "new"),
    ("anya", "Я докажу шефу, что умею готовить.",
     "I will prove to the chef that I know how to cook.",
     [], "new"),
]

OPENER = "Now let's examine Max and Kostya's dialogue line by line."

WALK = [
    (0, None,
     "'On the one hand, I work in a cool restaurant.' Max introduces the first perspective with a prepositional idiom."),
    (1, None,
     "'And on the other hand, you eat ordinary sausages.' Kostya points out the ironic contrast with a descriptive plural noun."),
    (2, None,
     "'Our chef cooks the most delicious food.' Max praises the head chef using a superlative accusative adjective."),
    (3, None,
     "'But total chaos always reigns in the kitchen.' Kostya describes restaurant reality with a present tense verb."),
    (4, None,
     "'Guests think this is the most peaceful place.' Max contrasts customer impressions with a superlative phrase."),
    (5, None,
     "'They will never know the truth about us.' Kostya highlights backstage secrecy using a future verb and accusative noun."),
    (6, None,
     "'Every customer considers themselves an important person.' Max discusses patron attitudes with a reflexive pronoun."),
    (7, None,
     "'And we simply pour them wine.' Kostya summarizes their humble service role with an imperfective verb."),
    (8, None,
     "'Work in the kitchen is very hard and nerve-wracking.' Max characterizes culinary life with predicate adjectives."),
    (9, None,
     "'On the other hand, it's never boring here!' Kostya finds the silver lining using an impersonal negative construction."),
    (10, None,
     "'Our morning shift is starting soon.' Max notes the approaching hour with a reflexive present verb."),
    (11, None,
     "'Then prepare for a new workday!' Kostya gives encouraging advice with an imperative reflexive verb."),
    (12, None,
     "'I will prove to the chef that I know how to cook.' Max declares his ambitious goal with a future perfective verb."),
]

TRANSITION = "Now let's listen to Max and Kostya's conversation again without interruption."
OUTRO = (
    "Max and Kostya get ready for the shift as the restaurant opens. "
    "In the next scene, Max faces the wrath of the head chef after arriving late."
)
CLOSING = ("anya", "Я докажу шефу, что умею готовить.")
