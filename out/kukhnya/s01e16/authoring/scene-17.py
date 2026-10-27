"""s01e16 scene 17: Яблочный штрудель (Apple Strudel)."""

ID = "kukhnya-s01e16-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 17
TITLE = "Яблочный штрудель  (Apple Strudel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Айнура", "kostya": "Инспектор"}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 222-259. The migration inspector sits with Aynura disguised as a guest; though he sees through the ruse, the delicious apple strudel convinces him to spare her."

INTRO = (
    "To hide cleaner Aynura from the migration inspection, the staff dress her up as a wealthy guest in the dining room. "
    "However, the sharp-eyed inspector sits right at her table, orders apple strudel, and reveals that he knows every trick restaurants use to hide workers. "
    "Let's listen to their tense conversation in Russian."
)

STORY = [
    ("kostya", "Добрый вечер, можно сесть за столик?", "Good evening, may I sit at the table?",
     [(224, "Добрый вечер")], "adapted"),
    ("anya", "Да, пожалуйста, садитесь сюда.", "Yes, please, sit down here.",
     [], "new"),
    ("kostya", "Вы уже готовы сделать заказ?", "Are you ready to place an order already?",
     [(225, "Готовы сделать заказ?")], "adapted"),
    ("anya", "Я хочу заказать этот дорогой коньяк.", "I want to order this expensive cognac.",
     [(229, "Этот коньяк очень дорогой")], "adapted"),
    ("kostya", "А я закажу вкусный яблочный штрудель.", "And I will order the delicious apple strudel.",
     [(234, "яблочный штрудель")], "adapted"),
    ("kostya", "Я всегда везде нахожу нелегальных работников.", "I always find illegal workers everywhere.",
     [(239, "я их всегда везде нахожу")], "adapted"),
    ("anya", "Вам очень нравится ваша работа?", "Do you like your job very much?",
     [], "new"),
    ("kostya", "Да, я занимаюсь этим пять лет.", "Yes, I have been doing this for five years.",
     [(248, "этим я уже занимаюсь пять лет")], "adapted"),
    ("kostya", "Обычно работников прячут на складе.", "Usually they hide workers in the storeroom.",
     [(250, "прячут их в туалете, на складе")], "adapted"),
    ("kostya", "А умные люди сажают их в зале.", "And smart people seat them in the dining room.",
     [(251, "А те, кто поумнее")], "adapted"),
    ("kostya", "Но этот яблочный штрудель просто прекрасный!", "But this apple strudel is simply wonderful!",
     [(255, "самый прекрасный яблочный штрудель")], "adapted"),
    ("kostya", "Сегодня вкусный десерт спас вас.", "Today the delicious dessert saved you.",
     [(257, "сегодня кое-кого спас")], "adapted"),
    ("anya", "Хорошо, спасибо вам большое!", "All right, thank you very much!",
     [(259, "Хорошо. Спасибо")], "adapted"),
]

OPENER = "Let's see how the migration inspector toys with Aynura before pardoning her over dessert."

WALK = [
    (2, None,
     "'Are you ready to place an order already?' A polite question commonly used at a restaurant table."),
    (4, None,
     "'And I will order the delicious apple strudel.' A statement of intent using the future tense to choose a dessert."),
    (7, None,
     "'Yes, I have been doing this for five years.' Russian uses the present tense to describe an action that started in the past and continues now."),
    (11, None,
     "'Today the delicious dessert saved you.' A playful admission that the high quality of the food earned her a pardon."),
]

TRANSITION = "Now, let's hear the dining room scene between the inspector and Aynura once more."

OUTRO = (
    "Now you know how to order food at a table, talk about years of work experience, and express gratitude in Russian. "
    "See who the inspector catches next in the following scene."
)

CLOSING = ("kostya", "Сделайте себе разрешение на работу.")
