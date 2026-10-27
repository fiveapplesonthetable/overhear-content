"""s01e04 scene 08: Ингредиенты для супа (Ingredients for Soup)."""

ID = "kukhnya-s01e04-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = "Ингредиенты для супа  (Ingredients for Soup)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Макс", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "In the busy kitchen of Claude Monet, cook Senya hands Max the fresh ingredients for a cream soup. "
    "Senya gives practical advice on prepping the vegetables, while Max promises to make the dish unforgettable. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("senya", "Вот твои сухарики, сливки и морковка.",
     "Here are your croutons, cream, and carrot.",
     [(96, "Вот твои хлебочки, сливки и морковка")], "handing over ingredients"),
    ("anya", "Отлично, а где свежий лук?",
     "Great, and where is the fresh onion?",
     [], "asking for more produce"),
    ("senya", "Вот и лук, начинай варить суп.",
     "Here is the onion, start boiling the soup.",
     [(97, "вот и лук варим")], "passing the onion"),
    ("anya", "Я сделаю самый вкусный крем-суп.",
     "I will make the most delicious cream soup.",
     [], "expressing culinary ambition"),
    ("senya", "Главное, не пересоли бульон на плите.",
     "The main thing is do not oversalt the broth on the stove.",
     [], "warning against mistakes"),
    ("anya", "Не волнуйся, я знаю точный рецепт.",
     "Do not worry, I know the exact recipe.",
     [], "reassuring his mentor"),
    ("senya", "Сначала мелко нарежь лук и морковь.",
     "First chop the onion and carrot finely.",
     [], "explaining technique"),
    ("anya", "Я нарежу овощи ровными кусочками.",
     "I will cut the vegetables into even pieces.",
     [], "promising neat preparation"),
    ("senya", "Затем добавь масло и тёплые сливки.",
     "Then add butter and warm cream.",
     [], "giving the next step"),
    ("anya", "Всё будет готово вовремя, Сеня.",
     "Everything will be ready on time, Senya.",
     [], "promising punctual delivery"),
    ("senya", "Я приду и проверю твоё блюдо.",
     "I will come and check your dish.",
     [], "setting up inspection"),
    ("anya", "Ты будешь приятно удивлён этим супом!",
     "You will be pleasantly surprised by this soup!",
     [], "showing confidence"),
]

OPENER = "Let's review this kitchen prep session step by step."

WALK = [
    (0, None,
     "'Here are your croutons, cream, and carrot.' Senya gathers the necessary supplies at the prep station."),
    (1, None,
     "'Great, and where is the fresh onion?' Max checks his ingredient inventory before beginning."),
    (2, None,
     "'Here is the onion, start boiling the soup.' Senya passes the last vegetable and urges him to start."),
    (3, None,
     "'I will make the most delicious cream soup.' Max sets an ambitious culinary standard for his work."),
    (4, None,
     "'The main thing is do not oversalt the broth on the stove.' Senya offers crucial culinary advice."),
    (5, None,
     "'Do not worry, I know the exact recipe.' Max shows full confidence in his cooking abilities."),
    (6, None,
     "'First chop the onion and carrot finely.' Senya outlines the proper knife technique for the mirepoix."),
    (7, None,
     "'I will cut the vegetables into even pieces.' Max demonstrates his commitment to clean prep work."),
    (8, None,
     "'Then add butter and warm cream.' Senya explains how to incorporate the dairy elements."),
    (9, None,
     "'Everything will be ready on time, Senya.' Max promises reliable timing during dinner service."),
    (10, None,
     "'I will come and check your dish.' Senya ensures strict quality control on the hot line."),
    (11, None,
     "'You will be pleasantly surprised by this soup!' Max concludes with enthusiastic optimism."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "With the ingredients assembled and prep instructions in mind, Max begins cooking with energy. "
    "See you next time!"
)

CLOSING = ("anya", "Ты будешь приятно удивлён этим супом!")
