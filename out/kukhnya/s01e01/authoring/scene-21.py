"""s01e01 scene 21: Пари на кухне (A Bet in the Kitchen)."""

ID = "kukhnya-s01e01-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 21
TITLE = "Пари на кухне  (A Bet in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

INTRO = (
    "Max proudly presents his dessert for Eleonora Andreyevna, only to discover that she is a dog, "
    "and she completely refuses to eat sweet pastry! Indignant, Max challenges the Chef to a high-stakes bet. "
    "Listen to the dialogue in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Шеф, праздничный десерт уже готов!",
     "Chef, the festive dessert is already ready!",
     [(244, "Десерт"), (244, "готов")], "verbatim announcement"),
    ("chef", "Все внимание! Гостья пробует блюдо новичка.",
     "Attention everyone! The guest is tasting the newcomer's dish.",
     [(245, "Все внимание"), (246, "будет пробовать")], "verbatim announcement"),
    ("chef", "Иди сюда, милая собачка! Попробуй десерт.",
     "Come here, sweet little doggy! Taste the dessert.",
     [(251, "Ко мне"), (252, "Прошу")], "playful command"),
    ("chef", "Она даже не смотрит на тарелку.",
     "She doesn't even look at the plate.",
     [(253, "не жрет")], "cleaned of crude language for A1"),
    ("anya", "Шеф, это нечестно! Это же собака.",
     "Chef, that is unfair! After all, it is a dog.",
     [(255, "Шеф, ну так нечестно"), (255, "это же собака")], "verbatim protest"),
    ("chef", "Мир вообще не идеален, молодой человек.",
     "The world is not ideal at all, young man.",
     [(256, "мир не идеален")], "verbatim philosophical retort"),
    ("anya", "Давайте поспорим, шеф!",
     "Let's make a bet, chef!",
     [(259, "давайте поспорим")], "verbatim challenge"),
    ("chef", "О чём мы будем спорить?",
     "What will we bet about?",
     [(260, "Чего")], "expanded for A1"),
    ("anya", "Обычному человеку понравится моё горячее блюдо.",
     "An ordinary person will like my hot dish.",
     [(261, "простой нормальный человек"), (261, "понравится мое блюдо")], "verbatim thesis"),
    ("chef", "Хорошо! Ты приготовишь блюдо для меня.",
     "Good! You will cook a dish for me.",
     [(262, "Давай поспорим"), (263, "Ты приготовишь блюдо для меня")], "verbatim terms"),
    ("chef", "Если мне понравится, ты остаёшься здесь.",
     "If I like it, you stay here.",
     [(264, "Если мне понравится, ты"), (264, "остаешься")], "verbatim prize"),
    ("chef", "Если нет, ты уйдёшь отсюда навсегда.",
     "If not, you will leave here forever.",
     [(265, "Если выиграю я"), (265, "ты уйдешь отсюда")], "cleaned penalty for A1"),
    ("anya", "Я согласен на этот спор!",
     "I agree to this bet!",
     [(266, "Согласен")], "verbatim acceptance"),
    ("chef", "Посмотрим, какой из тебя повар!",
     "We will see what kind of cook you are!",
     [(274, "Папочка готовить будет")], "culinary challenge"),
]

OPENER = "Now let us go through the scene line by line to understand every expression."

WALK = [
    (0, "Шеф, праздничный десерт уже готов!",
     "'Chef, the festive dessert is already ready!' Max announces completion with the short adjective."),
    (1, "Все внимание!",
     "'Attention everyone!' The chef calls out to gather the kitchen staff."),
    (1, "Гостья пробует блюдо новичка.",
     "'The guest is tasting the newcomer's dish.' Genitive nouns indicate the taster and the creator."),
    (2, "Иди сюда, милая собачка!",
     "'Come here, sweet little doggy!' The chef reveals the guest is actually a dog."),
    (2, "Попробуй десерт.",
     "'Taste the dessert.' An imperative offering the plate to the pet."),
    (3, "Она даже не смотрит на тарелку.",
     "'She doesn't even look at the plate.' The verb takes the preposition for directing attention."),
    (4, "Шеф, это нечестно!",
     "'Chef, that is unfair!' An adverb expressing indignation at the unfair test."),
    (4, "Это же собака.",
     "'After all, it is a dog.' The emphatic particle stresses the absurdity of a pet judge."),
    (5, "Мир вообще не идеален, молодой человек.",
     "'The world is not ideal at all, young man.' A dry philosophical shrug from the chef."),
    (6, "Давайте поспорим, шеф!",
     "'Let's make a bet, chef!' The first-person plural imperative invites a wager."),
    (7, "О чём мы будем спорить?",
     "'What will we bet about?' The prepositional question form asks for the terms."),
    (8, "Обычному человеку понравится моё горячее блюдо.",
     "'An ordinary person will like my hot dish.' The dative construction indicates who will enjoy the food."),
    (9, "Хорошо!",
     "'Good!' The chef accepts the idea of a culinary challenge."),
    (9, "Ты приготовишь блюдо для меня.",
     "'You will cook a dish for me.' The perfective verb specifies a completed culinary task."),
    (10, "Если мне понравится, ты остаёшься здесь.",
     "'If I like it, you stay here.' The conditional clause sets the prize for victory."),
    (11, "Если нет, ты уйдёшь отсюда навсегда.",
     "'If not, you will leave here forever.' The future verb states the severe penalty for defeat."),
    (12, "Я согласен на этот спор!",
     "'I agree to this bet!' The masculine short adjective confirms acceptance of the challenge."),
    (13, "Посмотрим, какой из тебя повар!",
     "'We will see what kind of cook you are!' An idiomatic phrase expressing anticipation of the trial."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "The stakes could not be higher: Max must cook a dish that truly impresses Chef Viktor Barinov, "
    "or lose his place at Claude Monet for good. Next time, the culinary duel begins. See you then!"
)

CLOSING = ("anya", "Я обязательно выиграю этот спор.")
