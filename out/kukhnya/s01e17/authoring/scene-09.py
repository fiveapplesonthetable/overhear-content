ID = "kukhnya-s01e17-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 9
TITLE = "Сезонное блюдо  (The Seasonal Dish)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "fedya": "angelina"}
LABELS = {"anya": "Сеня", "chef": "Шеф", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 121-133. Chef Barinov tastes the kitchen team's submissions for the new seasonal menu and selects "
    "Senya's veal rolls with ham, leaving Fedya frustrated that his dish was not even tasted."
)

INTRO = (
    "In the kitchen of Claude Monet, the cooks present their creations for the new seasonal menu to Chef Barinov. "
    "Senya steps forward first with his veal and ham dish, hoping to win the competition before anyone else gets a chance. "
    "Let's listen to the tasting in Russian first."
)

STORY = [
    ("anya", "Шеф, попробуйте новое блюдо.",
     "Chef, try the new dish.",
     [(121, "Попробуйте сезонное блюдо")], "adapted"),
    ("chef", "Что? Какое ещё блюдо?",
     "What? What dish?",
     [(122, "Что?")], "adapted"),
    ("anya", "Вы же вчера дали нам задание.",
     "Yesterday you gave us an assignment.",
     [(123, "вы же вчера дали задание")], "adapted"),
    ("chef", "Ладно, давай будем пробовать.",
     "All right, let us try it.",
     [(125, "пробовать")], "adapted"),
    ("chef", "А это что такое?",
     "And what is this?",
     [(126, "Это что?")], "adapted"),
    ("anya", "Это нежное мясо с тонкой ветчиной.",
     "This is tender meat with thin ham.",
     [(127, "с тонкими ломтиками ветчины")], "adapted"),
    ("chef", "Очень вкусно, мне нравится этот рецепт!",
     "Very tasty, I like this recipe!",
     [], "new"),
    ("chef", "Поздравляю, твоё блюдо теперь в меню.",
     "Congratulations, your dish is now on the menu.",
     [(128, "Поздравляю, инвалид, твое блюдо в меню")], "adapted"),
    ("fedya", "Шеф, подождите, это совсем нечестно!",
     "Chef, wait, this is completely unfair!",
     [(129, "Шеф, подождите, шеф, это не честно")], "adapted"),
    ("anya", "Спасибо большое, шеф, я очень рад!",
     "Thank you very much, Chef, I am very glad!",
     [], "new"),
    ("fedya", "Поздравляю тебя с победой, коллега.",
     "Congratulations on the victory, colleague.",
     [(131, "Да, поздравляю, коллега")], "adapted"),
    ("fedya", "Шеф, а как же наши блюда?",
     "Chef, what about our dishes?",
     [(133, "Как же мы?")], "adapted"),
    ("chef", "Мне больше ничего не нужно, я нашёл.",
     "I do not need anything else, I found it.",
     [(133, "я его нашёл")], "adapted"),
]

OPENER = "Now let's examine this conversation line by line."

WALK = [
    (0, None,
     "'Chef, try the new dish.' -- Senya eagerly invites the Chef to taste his creation."),
    (1, None,
     "'What? What dish?' -- Barinov has completely forgotten about the contest he announced."),
    (2, None,
     "'Yesterday you gave us an assignment.' -- Senya reminds him of the task from the day before."),
    (3, None,
     "'All right, let us try it.' -- The Chef reluctantly agrees to taste the food."),
    (4, None,
     "'And what is this?' -- He inspects the plate in front of him with curiosity."),
    (5, None,
     "'This is tender meat with thin ham.' -- Senya proudly describes the ingredients of his roll."),
    (6, None,
     "'Very tasty, I like this recipe!' -- Barinov is pleasantly surprised by the flavor."),
    (7, None,
     "'Congratulations, your dish is now on the menu.' -- He immediately declares Senya the winner."),
    (8, None,
     "'Chef, wait, this is completely unfair!' -- Fedya protests that the others had no turn."),
    (9, None,
     "'Thank you very much, Chef, I am very glad!' -- Senya celebrates his triumph in the kitchen."),
    (10, None,
     "'Congratulations on the victory, colleague.' -- Another cook offers polite congratulations."),
    (11, None,
     "'Chef, what about our dishes?' -- Fedya points to the plates the other cooks prepared."),
    (12, None,
     "'I do not need anything else, I found it.' -- Barinov dismisses the rest of the entries and walks away."),
]

TRANSITION = "Now let's listen to the kitchen conversation again without interruption."
OUTRO = (
    "Having found a seasonal special on the very first try, Chef Barinov calls off the rest of the tasting "
    "and leaves Senya basking in his victory."
)
CLOSING = ("anya", "Моё блюдо лучше всех!")
