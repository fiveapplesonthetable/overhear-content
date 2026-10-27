"""s01e04 scene 20: Синий супчик (The Blue Soup)."""

ID = "kukhnya-s01e04-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 20
TITLE = "Синий супчик  (The Blue Soup)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "senya": "anja",
    "louis": "angelina",
}
LABELS = {
    "anya": "Макс",
    "senya": "Сеня",
    "louis": "Луи",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "Max serves his special soup to the Claude Monet kitchen crew, but it turns out to be an alarming bright blue color. "
    "The cooks are skeptical, pastry chef Louis suddenly notices his missing food dye, but the bizarre soup turns out to be surprisingly delicious. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("senya", "Что это за странное блюдо?",
     "What kind of strange dish is this?",
     [(269, "Что за фигня")], "bewildered reaction"),
    ("anya", "Это мой новый вкусный суп!",
     "This is my new delicious soup!",
     [], "proud presentation"),
    ("senya", "Почему он такого синего цвета?",
     "Why is it such a blue color?",
     [], "questioning appearance"),
    ("anya", "Это оригинальный авторский рецепт.",
     "This is an original creator's recipe.",
     [], "creative justification"),
    ("senya", "Спасибо, я сегодня на диете.",
     "Thanks, I am on a diet today.",
     [(270, "Спасибо, я сегодня на диете")], "polite refusal"),
    ("anya", "Подожди, это действительно очень вкусно!",
     "Wait, this is really very delicious!",
     [(271, "Подожди, это вкусно")], "insisting on taste"),
    ("louis", "Пардон, это же мой краситель!",
     "Pardon, that is my food coloring!",
     [(275, "Пардон, это же мой краситель")], "sudden realization"),
    ("louis", "Я так долго его искал!",
     "I looked for it for so long!",
     [(276, "я искал, я потерял")], "explaining lost item"),
    ("anya", "Подождите, вы куда все уходите?",
     "Wait, where are you all going?",
     [(277, "Подождите, вы куда")], "protesting retreat"),
    ("senya", "Мы не хотим есть химию.",
     "We do not want to eat chemicals.",
     [], "distrust of dye"),
    ("anya", "Но это же реально вкусно!",
     "But this is actually delicious!",
     [(277, "Это же реально вкусно")], "pleading quality"),
    ("senya", "Какой интересный красивый супчик.",
     "What an interesting pretty little soup.",
     [(273, "Какой красивый супчик")], "tasting cautiously"),
    ("senya", "Как будто прямо море ешь.",
     "Like you are eating the sea directly.",
     [(278, "как будто море ешь")], "surprised comparison"),
    ("anya", "Я же говорил, что вкусно!",
     "I told you it was delicious!",
     [(278, "Правда, вкусно")], "triumphant validation"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Что это за странное блюдо?",
     "'What kind of strange dish is this?' The cook stares in disbelief at the oddly colored food."),
    (1, "Это мой новый вкусный суп!",
     "'This is my new delicious soup!' Max introduces his culinary invention with great pride."),
    (2, "Почему он такого синего цвета?",
     "'Why is it such a blue color?' An obvious question about the soup's unnatural bright hue."),
    (3, "Это оригинальный авторский рецепт.",
     "'This is an original chef recipe.' Max defends his unusual approach to cooking."),
    (4, "Спасибо, я сегодня на диете.",
     "'Thanks, I am on a diet today.' An excuse to politely decline trying the suspect blue meal."),
    (5, "Подожди, это действительно очень вкусно!",
     "'Wait, this is really very delicious!' Max pleads with everyone to look beyond the appearance."),
    (6, "Пардон, это же мой краситель!",
     "'Pardon, that is my food coloring!' The French pastry chef recognizes his missing ingredient."),
    (7, "Я так долго его искал!",
     "'I looked for it for so long!' Louis reveals that a bottle of blue dye had gone missing."),
    (8, "Подождите, вы куда все уходите?",
     "'Wait, where are you all going?' Max sees his audience backing away from the table."),
    (9, "Мы не хотим есть химию.",
     "'We do not want to eat chemicals.' The cooks refuse to ingest artificial baking dye."),
    (10, "Но это же реально вкусно!",
     "'But this is actually delicious!' Max insists that the dish tastes wonderful despite the color."),
    (11, "Какой интересный красивый супчик.",
     "'What an interesting pretty little soup.' A brave cook takes a spoonful and reconsiders."),
    (12, "Как будто прямо море ешь.",
     "'Like you are eating the sea directly.' The flavor surprisingly evokes an oceanic essence."),
    (13, "Я же говорил, что вкусно!",
     "'I told you it was delicious!' Max celebrates winning over the skeptical kitchen staff."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Despite the shock of Louis's blue food dye, the staff lunch turns out to be a surprising hit. "
    "Next time, we will see what Chef Barinov thinks of the crew's colorful blue tongues. Until then!"
)

CLOSING = ("anya", "Необычный суп оказался очень вкусным.")
