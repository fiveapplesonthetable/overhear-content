"""s01e07 scene 09: Дегустация соуса (Tasting the Sauce)."""

ID = "kukhnya-s01e07-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 7
SCENE = 9
TITLE = "Дегустация соуса  (Tasting the Sauce)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "lyova": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "lyova": "Лёва"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"
SOURCE_NOTE = "Cues 169-186. Chef Barinov gathers his cooks to taste his newly invented gourmet sauce."

INTRO = (
    "In the kitchen of Claude Monet, Chef Viktor Barinov puts the finishing touches on a brand new signature sauce. "
    "Calling his line cooks over to the stove, he demands their honest feedback and basks in their immediate admiration. "
    "Let's listen to their enthusiastic exchange in Russian first."
)

STORY = [
    ("chef", "Повара, быстро подойдите все сюда!", "Cooks, quickly come over here, everyone!",
     [(169, "подошли все сюда")], ""),
    ("anya", "Что вы приготовили, шеф?", "What did you cook, chef?",
     [], ""),
    ("chef", "Все пробуем новый соус. Быстро!", "Everyone taste the new sauce. Quickly!",
     [(172, "Все пробуем соус. Быстро")], ""),
    ("chef", "Лёва, ты пробуешь самым первым.", "Lyova, you taste very first.",
     [(173, "Лёва")], ""),
    ("lyova", "Шеф, это невероятно вкусно!", "Chef, this is incredibly delicious!",
     [(175, "Очень вкусно")], ""),
    ("chef", "А теперь твоя очередь, Огузок.", "And now it is your turn, Oguzok.",
     [(179, "Гузак")], ""),
    ("chef", "Ты такого в Воронеже не пробовал?", "You haven't tasted anything like this in Voronezh?",
     [(179, "ты такого даже не пробовал в своих воронежских столовках")], ""),
    ("anya", "Потрясающий соус, шеф, просто восторг!", "Amazing sauce, chef, pure delight!",
     [(181, "Потрясающий соус, шеф")], ""),
    ("anya", "Я никогда не пробовал ничего лучше.", "I have never tasted anything better.",
     [(182, "Я такого никогда не пробовал")], ""),
    ("chef", "Учись, пока я добрый сегодня!", "Learn while I am kind today!",
     [(184, "Учись")], ""),
    ("anya", "Я искренне завидую нашему гостю.", "I genuinely envy our guest.",
     [(183, "Я искренне завидую тому человеку")], ""),
    ("chef", "Хватит болтать, оформите красивую подачу.", "Stop chatting, prepare a beautiful plating.",
     [(186, "Пошел на оформление")], ""),
    ("lyova", "Всё сделаем идеально, шеф!", "We will make everything ideally, chef!",
     [], ""),
]

OPENER = "Let's examine how Chef Barinov invites his kitchen crew to taste his culinary masterpiece."

WALK = [
    (0, None,
     "'Cooks, quickly come over here, everyone!' The chef addresses his team with an imperative verb and urgent adverbs to command immediate attention."),
    (2, None,
     "'Everyone taste the new sauce. Quickly!' The inclusive present tense verb invites collective action, emphasized by an energetic adverb."),
    (7, None,
     "'Amazing sauce, chef, pure delight!' The enthusiastic compliment uses an expressive adjective and an emotional noun phrase."),
    (8, None,
     "'I have never tasted anything better.' The negative construction employs a double negative with a comparative adverb for superlative praise."),
]

TRANSITION = "Okay, let's hear the sauce tasting dialogue once more."

OUTRO = (
    "Now you understand how Russian chefs present new dishes to their brigade. "
    "Listen for these culinary compliments next time you watch the episode."
)

CLOSING = ("anya", "Этот вкус я запомню навсегда.")
