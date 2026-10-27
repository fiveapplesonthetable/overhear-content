ID = "kukhnya-s01e01-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 2
TITLE = "Коктейль в баре  (Cocktails at the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 22. Max and Vika sit together at the bar having drinks. "
    "Max shares his dream of becoming a top chef, and the chemistry between them grows stronger."
)

INTRO = (
    "Inside the lively bar, Max and Vika order drinks and sit close together. "
    "Vika chooses white wine while Max stays focused on tomorrow's interview, choosing only juice. "
    "Impressed by his passion and ambition to become an elite chef, Vika smiles warmly as the music plays. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Какой коктейль ты будешь пить, Вика?",
     "What cocktail will you drink, Vika?",
     [], "new"),
    ("vika", "Я люблю белое сухое вино.",
     "I like dry white wine.",
     [(4, "белого вина")], "adapted"),
    ("anya", "Бармен, принесите нам бокал белого вина!",
     "Bartender, bring us a glass of white wine!",
     [], "new"),
    ("vika", "А что ты сам будешь пить?",
     "And what will you drink yourself?",
     [], "new"),
    ("anya", "Я выпью немного хорошего сока.",
     "I will drink a little good juice.",
     [], "new"),
    ("vika", "Ты совсем не пьёшь крепкие напитки?",
     "Do you not drink strong drinks at all?",
     [], "new"),
    ("anya", "Завтра утром мне нужна свежая голова.",
     "Tomorrow morning I need a clear head.",
     [], "new"),
    ("vika", "Ты очень серьёзно относишься к работе.",
     "You take your work very seriously.",
     [], "new"),
    ("anya", "Я мечтаю стать самым лучшим шефом!",
     "I dream of becoming the very best chef!",
     [(9, "я тоже стану известным поваром")], "adapted"),
    ("vika", "Мне очень нравится твоя большая мечта.",
     "I like your big dream very much.",
     [], "new"),
    ("anya", "Ты сегодня выглядишь просто потрясающе.",
     "You look simply stunning tonight.",
     [], "new"),
    ("vika", "Спасибо, Макс, мне очень приятно.",
     "Thank you, Max, I am very pleased.",
     [], "new"),
    ("anya", "Пойдём танцевать под эту красивую музыку!",
     "Let's go dance to this beautiful music!",
     [], "new"),
]

OPENER = "Now let's examine Max and Vika's bar conversation line by line."

WALK = [
    (0, None,
     "'What cocktail will you drink, Vika?' Max asks her drink preference using an interrogative pronoun and future verb."),
    (1, None,
     "'I like dry white wine.' Vika specifies her taste with descriptive neuter adjectives and a noun."),
    (2, None,
     "'Bartender, bring us a glass of white wine!' Max places an order using a polite imperative verb."),
    (3, None,
     "'And what will you drink yourself?' Vika turns the question back with an emphatic reflexive pronoun."),
    (4, None,
     "'I will drink a little good juice.' Max chooses a non-alcoholic option using a partitive quantity phrase."),
    (5, None,
     "'Do you not drink strong drinks at all?' Vika questions his sobriety with an intensifying negative adverb."),
    (6, None,
     "'Tomorrow morning I need a clear head.' Max explains his discipline using a short predicate adjective."),
    (7, None,
     "'You take your work very seriously.' Vika admires his dedication with an adverb of manner and reflexive verb."),
    (8, None,
     "'I dream of becoming the very best chef!' Max declares his high ambition using an instrumental superlative phrase."),
    (9, None,
     "'I like your big dream very much.' Vika encourages him with an impersonal dative construction."),
    (10, None,
     "'You look simply stunning tonight.' Max pays her a heartfelt compliment with an evaluative adverb."),
    (11, None,
     "'Thank you, Max, I am very pleased.' Vika graciously accepts the praise with an impersonal predicative."),
    (12, None,
     "'Let's go dance to this beautiful music!' Max invites her to the dance floor with a prefixed imperative verb."),
]

TRANSITION = "Now let's listen to their bar dialogue again without interruption."
OUTRO = (
    "Max and Vika enjoy their drinks and head to the dance floor together. "
    "In the next scene, they talk intimately late into the night."
)
CLOSING = ("vika", "Мне очень нравится твоя большая мечта.")
