ID = "kukhnya-s01e16-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 5
TITLE = "Секретный паштет  (The Secret Pâté)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Шеф", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 37-50. Max tastes Chef Viktor's signature pâté and bets that he can "
    "recreate the secret recipe by tonight in exchange for days off."
)

INTRO = (
    "In the kitchen of Claude Monet, Max tastes a sample of Chef Viktor's homemade pâté. "
    "Blown away by the extraordinary taste, Max asks for the recipe, but Viktor refuses to share his secret. "
    "Ambitious and confident, Max proposes a bet. Let us listen to their conversation in Russian first."
)

STORY = [
    ("max", "Шеф, это просто потрясающий паштет!",
     "Chef, this is simply amazing pâté!",
     [(37, "Обалденный паштет, шеф.")], "adapted"),
    ("anya", "Конечно, это мой лучший фирменный рецепт.",
     "Of course, this is my best signature recipe.",
     [(39, "Это мой фирменный рецепт.")], "adapted"),
    ("max", "А какие продукты вы туда положили?",
     "And what products did you put in there?",
     [(40, "А что в него входит?")], "adapted"),
    ("anya", "Это мой самый большой личный секрет.",
     "This is my biggest personal secret.",
     [(41, "Это секрет")], "adapted"),
    ("max", "Скажите хотя бы один секретный ингредиент.",
     "Tell me at least one secret ingredient.",
     [(42, "ну скажите хотя бы, из чего он состоит?")], "adapted"),
    ("anya", "Ты никогда сам не догадаешься об этом.",
     "You will never guess this by yourself.",
     [(43, "тебе никогда не догадаться")], "adapted"),
    ("max", "Я смогу сам приготовить такой шедевр!",
     "I will be able to make such a masterpiece myself!",
     [(45, "Да я могу сам такой приготовить.")], "adapted"),
    ("anya", "Ты серьёзно хочешь спорить со мной?",
     "Do you seriously want to bet with me?",
     [(46, "Серьезно?")], "adapted"),
    ("max", "Да, сегодня вечером я повторю блюдо.",
     "Yes, tonight I will reproduce the dish.",
     [(47, "Вечером повторю ваш паштет.")], "adapted"),
    ("anya", "Возьми кусочек, чтобы сравнивать свой вкус.",
     "Take a piece so that you can compare your taste.",
     [(48, "чтобы ты мог сравнивать")], "adapted"),
    ("max", "Если я угадаю, вы дадите выходной?",
     "If I guess, will you give a day off?",
     [(49, "До вечера угадаешь, дам выходной.")], "adapted"),
    ("anya", "Хорошо, если повторишь, получишь два выходных.",
     "Fine, if you repeat it, you will get two days off.",
     [(50, "Два.")], "adapted"),
    ("max", "Договорились, вечером я принесу своё блюдо!",
     "It is a deal, tonight I will bring my dish!",
     [], "new"),
]

OPENER = "Now let us examine Viktor and Max's culinary wager line by line."

WALK = [
    (0, None,
     "'Chef, this is simply amazing pâté!' -- Max praises the exceptional homemade taste of Viktor's signature spread."),
    (1, None,
     "'Of course, this is my best signature recipe.' -- The head chef boasts proudly of his culinary accomplishment."),
    (2, None,
     "'And what products did you put in there?' -- The inquisitive junior cook tries to uncover the hidden ingredients."),
    (3, None,
     "'This is my biggest personal secret.' -- Viktor strictly refuses to disclose any details of how he made the dish."),
    (4, None,
     "'Tell me at least one secret ingredient.' -- Max persists and begs for just a small hint about the recipe."),
    (5, None,
     "'You will never guess this by yourself.' -- The boss taunts Max, claiming he lacks the palate to crack the mystery."),
    (6, None,
     "'I will be able to make such a masterpiece myself!' -- Confident in his abilities, Max issues a daring wager."),
    (7, None,
     "'Do you seriously want to bet with me?' -- The amused chef challenges the young cook to back up his arrogant words."),
    (8, None,
     "'Yes, tonight I will reproduce the dish.' -- Max firmly commits to matching the recipe before the evening ends."),
    (9, None,
     "'Take a piece so that you can compare your taste.' -- Viktor hands over a reference sample for the culinary duel."),
    (10, None,
     "'If I guess, will you give a day off?' -- Max raises the stakes and asks for a tangible reward for winning."),
    (11, None,
     "'Fine, if you repeat it, you will get two days off.' -- The confident chef doubles the prize if Max somehow wins."),
    (12, None,
     "'It is a deal, tonight I will bring my dish!' -- Max accepts the bet and prepares to start his experiments."),
]

TRANSITION = "Now let us listen to Viktor and Max once again."
OUTRO = (
    "With two whole days off hanging in the balance, Max pockets the sample of Viktor's pâté "
    "and heads off to start his kitchen experiments."
)
CLOSING = ("max", "Договорились, вечером я принесу своё блюдо!")
