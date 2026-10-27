"""s01e01 scene 20: Шанс для новичка (A Chance for the Newcomer)."""

ID = "kukhnya-s01e01-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 20
TITLE = "Шанс для новичка  (A Chance for the Newcomer)"
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
    "Max has been tasked with peeling stickers off crates of bananas, but he longs to show off his real skills. "
    "He pitches his signature chicken dish to the Chef, who mocks him but offers an unexpected test. "
    "Listen carefully to the Russian dialogue first, and then we will examine every sentence."
)

STORY = [
    ("anya", "Шеф, у меня есть отличная идея.",
     "Chef, I have an excellent idea.",
     [(218, "есть идея")], "expanded for A1"),
    ("anya", "Я могу приготовить своё фирменное блюдо.",
     "I can prepare my signature dish.",
     [(219, "Мое фирменное блюдо")], "verbatim"),
    ("anya", "Это нежная курица в сливочном соусе.",
     "It is tender chicken in cream sauce.",
     [(219, "Курица в сливочном соусе")], "adapted from subtitle"),
    ("chef", "Великолепная идея от неизвестного человека.",
     "A magnificent idea from an unknown person.",
     [(221, "Супер идея")], "sarcastic reaction"),
    ("chef", "Ты пришёл на мою кухню случайно.",
     "You came to my kitchen by accident.",
     [(222, "попавший случайно")], "adapted from line"),
    ("chef", "Лучше чисти бананы дальше!",
     "Better keep peeling bananas!",
     [(225, "Тащи еще пять ящиков бананов")], "contextual order"),
    ("anya", "Зачем вообще снимать эти наклейки?",
     "Why peel off these stickers at all?",
     [(228, "Нафига вообще отклеивать эти этикетки")], "cleaned of slang for A1"),
    ("chef", "Для идеального порядка во вселенной.",
     "For ideal order in the universe.",
     [(229, "Для баланса вселенной")], "adapted from dialogue"),
    ("anya", "Но я умею готовить прекрасные десерты.",
     "But I know how to prepare wonderful desserts.",
     [(232, "умеет офигенно готовить")], "cleaned for polite A1 learning"),
    ("chef", "Хорошо, я дам тебе один шанс.",
     "All right, I will give you one chance.",
     [(233, "Хорошо. Я дам тебе шанс")], "verbatim"),
    ("chef", "К нам пришёл наш постоянный гость.",
     "Our regular guest has arrived.",
     [(234, "У нас есть постоянный клиент")], "adapted for A1 vocabulary"),
    ("chef", "Ты приготовишь десерт для Элеоноры Андреевны.",
     "You will prepare dessert for Eleonora Andreyevna.",
     [(235, "Приготовишь для него десерт"), (237, "Элеонора Андреевна")], "verbatim task"),
    ("chef", "Если десерт понравится, ты останешься здесь.",
     "If the dessert is liked, you will stay here.",
     [(238, "Вот если ты сможешь угодить")], "conditional promise"),
    ("anya", "Договорились, шеф! Я сделаю лучший десерт.",
     "Agreed, chef! I will make the best dessert.",
     [(240, "Окей"), (241, "Ну, держитесь")], "eager acceptance"),
]

OPENER = "Now let us walk through each phrase to see how it works."

WALK = [
    (0, "Шеф, у меня есть отличная идея.",
     "'Chef, I have an excellent idea.' Max approaches his boss with standard possessive phrasing."),
    (1, "Я могу приготовить своё фирменное блюдо.",
     "'I can prepare my signature dish.' The reflexive possessive pronoun refers back to the subject."),
    (2, "Это нежная курица в сливочном соусе.",
     "'It is tender chicken in cream sauce.' Adjectives describe the texture and flavor of the proposed dish."),
    (3, "Великолепная идея от неизвестного человека.",
     "'A magnificent idea from an unknown person.' The chef uses heavy irony to dismiss the suggestion."),
    (4, "Ты пришёл на мою кухню случайно.",
     "'You came to my kitchen by accident.' The adverb underlines that Max has not earned any trust yet."),
    (5, "Лучше чисти бананы дальше!",
     "'Better keep peeling bananas!' An imperative telling the newcomer to return to his menial task."),
    (6, "Зачем вообще снимать эти наклейки?",
     "'Why peel off these stickers at all?' The question adverb challenges the purpose of the chore."),
    (7, "Для идеального порядка во вселенной.",
     "'For ideal order in the universe.' A grand philosophical excuse for giving meaningless busywork."),
    (8, "Но я умею готовить прекрасные десерты.",
     "'But I know how to prepare wonderful desserts.' Max asserts another branch of his culinary skills."),
    (9, "Хорошо, я дам тебе один шанс.",
     "'All right, I will give you one chance.' The future tense promises a single opportunity to impress."),
    (10, "К нам пришёл наш постоянный гость.",
     "'Our regular guest has arrived.' The noun phrase refers to a frequent restaurant customer."),
    (11, "Ты приготовишь десерт для Элеоноры Андреевны.",
     "'You will prepare dessert for Eleonora Andreyevna.' The genitive patronymic indicates polite respect."),
    (12, "Если десерт понравится, ты останешься здесь.",
     "'If the dessert is liked, you will stay here.' A conditional structure outlining the stakes."),
    (13, "Договорились, шеф!",
     "'Agreed, chef!' A short past-passive idiom confirming that a deal has been struck."),
    (13, "Я сделаю лучший десерт.",
     "'I will make the best dessert.' Max vows to produce his finest pastry."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Max has secured his chance to cook, confident that his dessert will win over Eleonora Andreyevna. "
    "Next time, we will see who this mysterious regular customer really is. See you soon!"
)

CLOSING = ("anya", "Мой десерт будет самым вкусным.")
