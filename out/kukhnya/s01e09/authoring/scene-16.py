"""s01e09 scene 16: Торт для банкета (The Banquet Cake)."""

ID = "kukhnya-s01e09-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 16
TITLE = "Торт для банкета  (The Banquet Cake)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "louis": "anja",
}
LABELS = {
    "anya": "Шеф",
    "louis": "Луи",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"

INTRO = (
    "In the pastry kitchen of Claude Monet, pastry chef Louis is finishing an elaborate banquet cake. "
    "Chef Barinov arrives to inspect the preparation, but they discover a small tool stuck in the cream. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("louis", "Шеф, я почти закончил этот торт.",
     "Chef, I have almost finished this cake.",
     [], "announcing cake"),
    ("anya", "Покажи мне его, Луи.",
     "Show it to me, Louis.",
     [], "asking to see"),
    ("louis", "Я думаю, торт скоро можно подавать.",
     "I think the cake can be served soon.",
     [(309, "Я думаю, торт через пять минут уже можно подавать.")], "estimating readiness"),
    ("anya", "Подожди, это ещё что такое?",
     "Wait, what on earth is this?",
     [(310, "Это еще что такое?")], "noticing foreign object"),
    ("louis", "Ой, это же железная струбцина!",
     "Oh, this is an iron clamp!",
     [(311, "Это струб.")], "shocked discovery"),
    ("anya", "Откуда она взялась в креме?",
     "Where did it come from in the cream?",
     [], "asking about cream"),
    ("anya", "Это же праздничный торт для гостей!",
     "This is a celebration cake for the guests!",
     [], "stressing importance"),
    ("louis", "Наверное, маленькая девочка играла здесь.",
     "Probably the little girl was playing here.",
     [], "explaining cause"),
    ("anya", "Алиса трогала твой торт?",
     "Did Alisa touch your cake?",
     [], "realizing daughter touched it"),
    ("louis", "Шеф, спокойно, не нужно кричать.",
     "Chef, calm down, no need to shout.",
     [(312, "Спокойно.")], "pleading calm"),
    ("louis", "Я сейчас быстро всё исправлю.",
     "I will quickly fix everything right now.",
     [(313, "Я все исправлю.")], "promising quick fix"),
    ("anya", "Сделай красиво, чтобы гости ничего не заметили.",
     "Make it pretty so the guests notice nothing.",
     [], "demanding perfection"),
    ("louis", "Обещаю, торт будет идеальным.",
     "I promise, the cake will be perfect.",
     [], "reassuring chef"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Шеф, я почти закончил этот торт.",
     "'Chef, I have almost finished this cake.' — past tense verb with an adverb of degree."),
    (1, "Покажи мне его, Луи.",
     "'Show it to me, Louis.' — imperative verb followed by dative and accusative pronouns."),
    (2, "Я думаю, торт скоро можно подавать.",
     "'I think the cake can be served soon.' — modal construction using an adverb of possibility."),
    (3, "Подожди, это ещё что такое?",
     "'Wait, what on earth is this?' — an imperative verb paired with an emphatic interrogative phrase."),
    (4, "Ой, это же железная струбцина!",
     "'Oh, this is an iron clamp!' — an exclamation expressing surprise at finding a metal tool."),
    (6, "Это же праздничный торт для гостей!",
     "'This is a celebration cake for the guests!' — pointing particle with a prepositional phrase."),
    (7, "Наверное, маленькая девочка играла здесь.",
     "'Probably the little girl was playing here.' — modal word expressing probability in the past."),
    (9, "Шеф, спокойно, не нужно кричать.",
     "'Chef, calm down, no need to shout.' — an adverb of reassurance with a negative modal phrase."),
    (10, "Я сейчас быстро всё исправлю.",
     "'I will quickly fix everything right now.' — future perfective verb promising immediate correction."),
    (11, "Сделай красиво, чтобы гости ничего не заметили.",
     "'Make it pretty so the guests notice nothing.' — purpose clause introduced by the conjunction."),
    (12, "Обещаю, торт будет идеальным.",
     "'I promise, the cake will be perfect.' — 1st person present verb followed by an instrumental predicate."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("louis", "Обещаю, торт будет идеальным.")
