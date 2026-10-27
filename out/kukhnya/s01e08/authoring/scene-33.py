"""Scene 33 — The Right to Make Mistakes (s01e08, 00:22:01–00:22:20)."""

ID = "kukhnya-s01e08-scene-33"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 33
TITLE = "Право на ошибку  (The Right to Make Mistakes)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Макс",
    "kostya": "Костя",
}

INTRO = (
    "After an exhausting dinner service filled with kitchen blunders and shouting, Kostya confides his worries to Max. "
    "Max reflects on how mistakes are an unavoidable part of human life that ultimately help us find the right path."
)

STORY = [
    ("kostya", "Макс, я сегодня натворил глупых глупостей.",
     "Max, I did stupid things today.",
     [], "Kostya regrets"),

    ("anya", "Не переживай, все повара делают ошибки.",
     "Do not worry, all cooks make mistakes.",
     [], "Max comforts"),

    ("kostya", "Но шеф так громко на меня кричал!",
     "But the chef shouted so loudly at me!",
     [], "Kostya laments"),

    ("anya", "Мы не можем не совершать разные ошибки.",
     "We cannot help making various mistakes.",
     [(363, "Мы не можем не совершать ошибки.")], "Max begins reflection"),

    ("kostya", "Ты правда думаешь, что это нормально?",
     "Do you really think that this is normal?",
     [], "Kostya asks"),

    ("anya", "Ошибки — это важная часть нашей жизни.",
     "Mistakes are an important part of our life.",
     [(364, "Они часть нашей жизни.")], "Max explains role of errors"),

    ("kostya", "И чему же они могут нас научить?",
     "And what can they teach us?",
     [], "Kostya wonders"),

    ("anya", "Они помогают найти нам правильный путь.",
     "They help us find the right path.",
     [(365, "А самое главное, они помогают найти нам правильный путь.")], "Max reveals lesson"),

    ("kostya", "Значит, каждый промах делает нас сильнее?",
     "So every blunder makes us stronger?",
     [], "Kostya grasps idea"),

    ("anya", "Именно так мы становимся настоящими мастерами.",
     "That is precisely how we become true masters.",
     [], "Max confirms"),

    ("kostya", "Тогда я больше не буду сильно расстраиваться.",
     "Then I will not be so upset anymore.",
     [], "Kostya feels better"),

    ("anya", "Главное — помнить свои уроки и двигаться вперёд.",
     "The main thing is to remember your lessons and move forward.",
     [], "Max advises"),

    ("kostya", "Спасибо за поддержку, ты отличный друг.",
     "Thank you for the support, you are a great friend.",
     [], "Kostya thanks"),

    ("anya", "Завтра мы покажем на кухне высший класс!",
     "Tomorrow we will show top class in the kitchen!",
     [], "Max ends with optimism"),
]

OPENER = "Let's explore Max and Kostya's uplifting conversation about learning from life's mistakes."

WALK = [
    (0, None,
     "'Max, I did stupid things today.' Kostya regrets his blunders behind the bar."),
    (1, None,
     "'Do not worry, all cooks make mistakes.' Max offers comfort to his distressed roommate."),
    (2, None,
     "'But the chef shouted so loudly at me!' The young bartender winces recalling the chef's wrath."),
    (3, None,
     "'We cannot help making various mistakes.' Max begins his philosophical reflection on human nature."),
    (4, None,
     "'Do you really think that this is normal?' Kostya seeks validation from his thoughtful friend."),
    (5, None,
     "'Mistakes are an important part of our life.' Max explains that errors are completely inevitable in life."),
    (6, None,
     "'And what can they teach us?' Kostya questions the deeper meaning behind failure."),
    (7, None,
     "'They help us find the right path.' Max reveals that blunders guide people toward wisdom."),
    (8, None,
     "'So every blunder makes us stronger?' Kostya grasps the encouraging lesson with a smile."),
    (9, None,
     "'That is precisely how we become true masters.' Max confirms the path of growth in the craft."),
    (10, None,
     "'Then I will not be so upset anymore.' Kostya regains his confidence after the heartfelt conversation."),
    (11, None,
     "'The main thing is to remember your lessons and move forward.' Max emphasizes resilience and purpose."),
    (12, None,
     "'Thank you for the support, you are a great friend.' Kostya appreciates the uplifting encouragement."),
    (13, None,
     "'Tomorrow we will show top class in the kitchen!' Max finishes his reflection with bright optimism."),
]

TRANSITION = "Now let's listen to the reassuring conversation between the two friends once more."

OUTRO = "With renewed confidence and mutual support, Max and Kostya prepare to conquer tomorrow's shift."

CLOSING = ("anya", "Завтра мы покажем на кухне высший класс!")
