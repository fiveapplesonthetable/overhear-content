ID = "kukhnya-s01e16-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 7
TITLE = "Первая проба  (The First Taste)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 52-57. In the kitchen, Max has Kostya taste the first experimental batch "
    "of his copycat pâté, receiving blunt feedback on its strange appearance and mediocre taste."
)

INTRO = (
    "In the kitchen of Claude Monet, Max finishes his first experimental batch of homemade pâté. "
    "He eagerly calls Kostya over to give an honest opinion. Kostya inspects the strange color "
    "with hesitation before taking a bite. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, быстро попробуй мой новый паштет.",
     "Kostya, quickly taste my new pâté.",
     [], "new"),
    ("kostya", "Слушай, это блюдо вообще можно есть?",
     "Listen, is this dish even edible now?",
     [(52, "Слушай, это съедобно вообще.")], "adapted"),
    ("anya", "Почему ты так подозрительно смотришь туда?",
     "Why are you looking in there so suspiciously?",
     [], "new"),
    ("kostya", "Цвет выглядит странно и совсем не аппетитно.",
     "The color looks strange and not appetizing at all.",
     [(53, "Потому что выглядит")], "adapted"),
    ("anya", "Главное в еде — это прекрасный вкус!",
     "The main thing in food is wonderful taste!",
     [], "new"),
    ("kostya", "Ну ладно, я сейчас попробую ложку.",
     "Well all right, I will try a spoon now.",
     [], "new"),
    ("anya", "И как тебе кажется этот рецепт?",
     "And how does this recipe seem to you?",
     [], "new"),
    ("kostya", "В принципе, вкус нормальный и не плохой.",
     "In principle, the taste is fine and not bad.",
     [(55, "Ну, ничего так.")], "adapted"),
    ("kostya", "Под холодное пиво такое блюдо пойдёт.",
     "With cold beer such a dish would do.",
     [(56, "Под пиво пойдет.")], "adapted"),
    ("anya", "А похоже на фирменный паштет шефа?",
     "And does it resemble the chef's signature pâté?",
     [], "new"),
    ("kostya", "Нет, у шефа блюдо намного лучше.",
     "No, the chef's dish is much better.",
     [(54, "У шефа даже на вид получше.")], "adapted"),
    ("kostya", "Ты положил туда слишком много соуса?",
     "Did you put too much sauce in there?",
     [(57, "А что, это кетчуп с мясом?")], "adapted"),
    ("kostya", "Да, продолжай стараться и готовить дальше!",
     "Yes, keep trying and cook further!",
     [], "new"),
]

OPENER = "Now let us examine Max and Kostya's tasting session line by line."

WALK = [
    (0, None,
     "'Kostya, quickly taste my new pâté.' -- Max eagerly invites the barman to test his first experimental batch."),
    (1, None,
     "'Listen, is this dish even edible now?' -- Kostya hesitates upon seeing the unappealing texture of the sample."),
    (2, None,
     "'Why are you looking in there so suspiciously?' -- The young cook wonders why his friend looks so reluctant."),
    (3, None,
     "'The color looks strange and not appetizing at all.' -- Kostya frankly critiques the murky appearance of the paste."),
    (4, None,
     "'The main thing in food is wonderful taste!' -- Max argues that culinary excellence lies in flavor rather than visuals."),
    (5, None,
     "'Well all right, I will try a spoon now.' -- Reluctantly agreeing to help, Kostya scoops up a small spoonful."),
    (6, None,
     "'And how does this recipe seem to you?' -- Max awaits his friend's verdict with tense anticipation."),
    (7, None,
     "'In principle, the taste is fine and not bad.' -- Kostya gives an unexpectedly tolerant review of the flavor."),
    (8, None,
     "'With cold beer such a dish would do.' -- The barman casually remarks that the salty snack pairs well with drinks."),
    (9, None,
     "'And does it resemble the chef's signature pâté?' -- Max cuts straight to the core of his competitive challenge."),
    (10, None,
     "'No, the chef's dish is much better.' -- Kostya shatters Max's illusions with an honest comparison."),
    (11, None,
     "'Did you put too much sauce in there?' -- Kostya offers constructive feedback on why the consistency is off."),
    (12, None,
     "'Yes, keep trying and cook further!' -- Kostya encourages the aspiring chef to refine his technique."),
]

TRANSITION = "Now let us listen to Max and Kostya once again."
OUTRO = (
    "Realizing that his first attempt falls short of Viktor's signature spread, "
    "Max heads back to the cutting board determined to crack the secret formula."
)
CLOSING = ("kostya", "Да, продолжай стараться и готовить дальше!")
