ID = "kukhnya-s01e07-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 1
TITLE = "Жизнь в столице  (Life in the Capital)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-4. At Claude Monet early in the morning, Max tells Kostya about his first two weeks in Moscow "
    "and boasts about living in the city center for free."
)

INTRO = (
    "Two weeks after leaving Voronezh, Max arrives early at the Claude Monet restaurant. "
    "Chatting with bartender Kostya before the morning rush, Max reflects on working at Moscow's most prestigious "
    "culinary destination and boasts about living right in the city center without paying a penny. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Я живу в Москве уже две недели.",
     "I have been living in Moscow for two weeks already.",
     [(1, "Две недели, как я уехал из Воронежа")], "adapted"),
    ("kostya", "Ты уже привык к жизни в Москве?",
     "Have you already gotten used to life in Moscow?",
     [], "new"),
    ("anya", "Я приехал сюда из Воронежа за мечтой.",
     "I came here from Voronezh for a dream.",
     [(1, "я уехал из Воронежа")], "adapted"),
    ("kostya", "И теперь ты работаешь в лучшем ресторане.",
     "And now you work in the best restaurant.",
     [(2, "Я работаю в самом офигенном ресторане Москвы")], "adapted"),
    ("anya", "Ресторан Клод Моне — самый известный в городе.",
     "Claude Monet restaurant is the most famous in the city.",
     [(3, "Клод Мане")], "adapted"),
    ("kostya", "Здесь очень строгие правила и дорогое меню.",
     "Here there are very strict rules and an expensive menu.",
     [], "new"),
    ("anya", "Но для меня это прекрасный опыт.",
     "But for me this is wonderful experience.",
     [], "new"),
    ("kostya", "А где ты нашёл себе жильё?",
     "And where did you find yourself housing?",
     [], "new"),
    ("anya", "Я живу в самом центре города.",
     "I live right in the center of the city.",
     [(3, "я живу в самом центре Москвы")], "adapted"),
    ("kostya", "Квартиры в центре стоят огромных денег.",
     "Apartments in the center cost huge money.",
     [], "new"),
    ("anya", "А я не плачу ни одной копейки!",
     "And I do not pay a single kopeck!",
     [(3, "ни копейки за это не"), (4, "плачу")], "adapted"),
    ("kostya", "Это звучит очень странно и подозрительно.",
     "That sounds very strange and suspicious.",
     [], "new"),
    ("anya", "У меня есть один секретный план.",
     "I have one secret plan.",
     [], "new"),
]

OPENER = "Now let's examine Max and Kostya's morning chat line by line."

WALK = [
    (0, None,
     "'I have been living in Moscow for two weeks already.' Max opens the conversation with a temporal phrase."),
    (1, None,
     "'Have you already gotten used to life in Moscow?' Kostya asks about adapting to the big city using a dative construction."),
    (2, None,
     "'I came here from Voronezh for a dream.' Max recalls his journey using an instrumental purpose noun."),
    (3, None,
     "'And now you work in the best restaurant.' Kostya notes his friend's achievement with a superlative adjective."),
    (4, None,
     "'Claude Monet restaurant is the most famous in the city.' Max praises the establishment using a compound superlative."),
    (5, None,
     "'Here there are very strict rules and an expensive menu.' Kostya highlights the demanding kitchen atmosphere."),
    (6, None,
     "'But for me this is wonderful experience.' Max maintains enthusiasm using an evaluative adjective and masculine noun."),
    (7, None,
     "'And where did you find yourself housing?' Kostya inquires about living arrangements with a reflexive pronoun."),
    (8, None,
     "'I live right in the center of the city.' Max boasts about his prime location with a prepositional phrase."),
    (9, None,
     "'Apartments in the center cost huge money.' Kostya questions the affordability using a genitive of price."),
    (10, None,
     "'And I do not pay a single kopeck!' Max claims complete free rent using an emphatic negative particle."),
    (11, None,
     "'That sounds very strange and suspicious.' Kostya expresses doubt using paired adverbs of judgment."),
    (12, None,
     "'I have one secret plan.' Max finishes with a mysterious hint about his unconventional lodging."),
]

TRANSITION = "Now let's listen to the morning chat again without interruption."
OUTRO = (
    "Kostya is skeptical of Max's mysterious living arrangement, while Max heads into the kitchen with a confident grin. "
    "In the next scene, Kostya uncovers the bizarre truth about Max's free lodging."
)
CLOSING = ("anya", "У меня есть один секретный план.")
