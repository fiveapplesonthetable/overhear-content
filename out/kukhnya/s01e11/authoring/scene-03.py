ID = "kukhnya-s01e11-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 3
TITLE = "Свидание на митинге  (A Date at the Rally)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Настя", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 41-50. At the bar, Kostya asks Nastya out for a weekend date, only to discover "
    "she wants to attend an environmental protest."
)

INTRO = (
    "Standing behind the bar at Claude Monet, Kostya notices waitress Nastya looking upset about cut flowers "
    "in the dining room. Hoping to cheer her up and ask her out on a romantic weekend date, he is caught "
    "completely off guard when she eagerly invites him to a forest protest rally. Let's listen to their conversation in Russian first."
)

STORY = [
    ("kostya", "Привет, Настя, почему ты без настроения?",
     "Hi, Nastya, why are you in a bad mood?",
     [(41, "Привет."), (43, "без настроения?")], "adapted"),
    ("anya", "Люди сорвали живые цветы ради удовольствия.",
     "People tore live flowers for pleasure.",
     [(44, "выбьют живые цветы?")], "adapted"),
    ("kostya", "Не грусти, Настя, всё будет хорошо.",
     "Do not be sad, Nastya, everything will be fine.",
     [], "new"),
    ("anya", "Это ужасно, так поступают злые люди.",
     "This is terrible, wicked people act like that.",
     [(45, "Это же ужасно. Изверги.")], "adapted"),
    ("kostya", "Давай сходим куда-нибудь на этих выходных.",
     "Let us go somewhere this weekend.",
     [(46, "сходим куда-нибудь?")], "adapted"),
    ("anya", "Я тоже хотела предложить тебе встречу.",
     "I also wanted to suggest a meeting to you.",
     [(47, "Я тебе тоже хотела предложить.")], "adapted"),
    ("kostya", "Отлично! В какое красивое место пойдём?",
     "Great! What beautiful place shall we go to?",
     [(48, "Класс. Куда?")], "adapted"),
    ("anya", "Мы поедем вместе в Химкинский лес.",
     "We will go together to the Khimki forest.",
     [(48, "В Химкинский лес.")], "adapted"),
    ("kostya", "А зачем нам ехать в лес?",
     "And why do we need to go to the forest?",
     [(49, "А зачем?")], "adapted"),
    ("anya", "Там будет большой митинг в защиту леса.",
     "There will be a big rally in defense of the forest.",
     [(50, "На митинг против вырубки.")], "adapted"),
    ("kostya", "Я думал, мы пойдём в кино.",
     "I thought we would go to the cinema.",
     [], "new"),
    ("anya", "Спасать живую природу гораздо важнее кино!",
     "Saving living nature is much more important than cinema!",
     [], "new"),
    ("kostya", "Хорошо, Настя, я с удовольствием поеду.",
     "Alright, Nastya, I will gladly go.",
     [], "new"),
]

OPENER = "Now let's examine this conversation at the bar line by line."

WALK = [
    (0, None,
     "'Hi, Nastya, why are you in a bad mood?' -- Kostya notices her unhappy expression at the bar."),
    (1, None,
     "'People tore live flowers for pleasure.' -- Nastya laments the cruel treatment of plants."),
    (2, None,
     "'Do not be sad, Nastya, everything will be fine.' -- The bartender tries to comfort her."),
    (3, None,
     "'This is terrible, wicked people act like that.' -- The activist condemns human cruelty."),
    (4, None,
     "'Let us go somewhere this weekend.' -- Kostya suggests a romantic weekend outing."),
    (5, None,
     "'I also wanted to suggest a meeting to you.' -- She welcomes the idea with enthusiasm."),
    (6, None,
     "'Great! What beautiful place shall we go to?' -- The excited bartender asks for her choice."),
    (7, None,
     "'We will go together to the Khimki forest.' -- Nastya names their outdoor destination."),
    (8, None,
     "'And why do we need to go to the forest?' -- Kostya is surprised by the unusual venue."),
    (9, None,
     "'There will be a big rally in defense of the forest.' -- She reveals the ecological protest."),
    (10, None,
     "'I thought we would go to the cinema.' -- The young man recalls his original plan."),
    (11, None,
     "'Saving living nature is much more important than cinema!' -- Nastya passionately defends the trees."),
    (12, None,
     "'Alright, Nastya, I will gladly go.' -- In love, Kostya agrees to accompany her."),
]

TRANSITION = "Now let's listen to the bar conversation again without interruption."
OUTRO = (
    "Swapping movie popcorn for protest banners out of affection for Nastya, Kostya accepts "
    "her unconventional date proposal with bemused devotion."
)
CLOSING = ("kostya", "Хорошо, Настя, я с удовольствием поеду.")
