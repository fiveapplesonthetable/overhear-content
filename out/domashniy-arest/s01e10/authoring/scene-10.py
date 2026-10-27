ID = "domashniy-arest-s01e10-scene-10"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 10
TITLE = "Один-один  (One-One)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 268-284. Samsonov suggests skipping the televised family performance, but Nina insists they keep their agreement. "
    "In frustration over her accusations, Samsonov absurdly tells Nina to cheat on him so their score is one-one."
)

INTRO = (
    "In this scene, Samsonov gets cold feet about the upcoming televised family performance and suggests canceling it entirely. "
    "Frustrated by Nina's lingering distrust, Samsonov absurdly offers that she cheat on him too, so they can be even at one-one. "
    "Nina sarcastically names local candidates before telling him to pull himself together. "
    "Let's listen to their argument in Russian first."
)

STORY = [
    ("anya", "Может, вообще не будем выступать?",
     "Maybe we will not perform at all?",
     [(269, "Может, вообще выступать не будем")], ""),
    ("nina", "Самсон, мы же обо всём договорились!",
     "Samson, we agreed on everything!",
     [(271, "Мы же договорились")], ""),
    ("anya", "Я ведь тоже живой человек.",
     "I am a living person too, after all.",
     [(272, "я тоже живой человек")], ""),
    ("nina", "Тогда постарайся ради наших детей.",
     "Then try for the sake of our children.",
     [(273, "Постарайся")], ""),
    ("anya", "Знаешь что? Измени мне тоже!",
     "You know what? Cheat on me too!",
     [(275, "Ну, хочешь, измени меня")], ""),
    ("nina", "Чего? Что ты такое говоришь?",
     "What? What are you saying?",
     [(276, "Чего")], ""),
    ("anya", "Чтобы у нас счёт был один-один!",
     "So that our score is one-one!",
     [(277, "чтобы у нас один-один был")], ""),
    ("nina", "Тогда это никогда не закончится.",
     "Then this will never end.",
     [(279, "Тогда это вечно будет продолжаться")], ""),
    ("anya", "Иди, я тебе серьёзно говорю.",
     "Go, I am telling you seriously.",
     [(280, "Я тебе серьезно говорю")], ""),
    ("nina", "И с кем мне изменить?",
     "And with whom should I cheat?",
     [(281, "С кем")], ""),
    ("anya", "С продавцом из продуктового магазина!",
     "With the clerk from the grocery store!",
     [(282, "с продуктового")], ""),
    ("nina", "Ты совсем с ума сошёл, Самсон?",
     "Have you completely lost your mind, Samson?",
     [], "Nina questions Samsonov's sanity"),
    ("nina", "Прекрати глупости и просто соберись!",
     "Stop the foolishness and just pull yourself together!",
     [(284, "Ну, тогда соберись")], ""),
    ("anya", "Ладно, я готов к выступлению.",
     "Alright, I am ready for the performance.",
     [], "Samsonov concedes"),
]

OPENER = (
    "Now let's examine Samsonov and Nina's argument line by line. "
    "Samsonov makes a bizarre proposal to resolve their marital distrust."
)

WALK = [
    (0, None,
     "'Maybe we will not perform at all?' Samsonov suggests canceling the television performance."),
    (1, None,
     "'Samson, we agreed on everything!' Nina reminds him of their mutual agreement."),
    (2, None,
     "'I am a living person too, after all.' Samsonov appeals to his emotional vulnerability."),
    (3, None,
     "'Then try for the sake of our children.' Nina urges him to act responsibly for the family."),
    (4, None,
     "'You know what? Cheat on me too!' Samsonov makes an absurd retaliatory offer."),
    (5, None,
     "'What? What are you saying?' Nina expresses astonishment at his bizarre suggestion."),
    (6, None,
     "'So that our score is one-one!' Samsonov uses sports scoring terminology to achieve parity."),
    (7, None,
     "'Then this will never end.' Nina points out the flaw in his cyclical logic."),
    (8, None,
     "'Go, I am telling you seriously.' Samsonov insists on his ridiculous proposal."),
    (9, None,
     "'And with whom should I cheat?' Nina asks sarcastically using the instrumental case."),
    (10, None,
     "'With the clerk from the grocery store!' Samsonov names a local neighborhood candidate."),
    (11, None,
     "'Have you completely lost your mind, Samson?' Nina questions his sanity with a common idiom."),
    (12, None,
     "'Stop the foolishness and just pull yourself together!' Nina orders him to focus on the performance."),
    (13, None,
     "'Alright, I am ready for the performance.' Samsonov relents and confirms his readiness."),
]

TRANSITION = "Now let's listen to Samsonov and Nina's argument once more without interruption."
OUTRO = (
    "Nina successfully deflects Samsonov's absurdity and refocuses him on the performance. "
    "In the next scene, the media circus begins."
)
CLOSING = ("nina", "Прекрати глупости и просто соберись!")
