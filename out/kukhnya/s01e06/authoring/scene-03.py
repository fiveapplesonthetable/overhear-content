ID = "kukhnya-s01e06-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = "Секрет лучших продуктов  (The Secret of the Best Products)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 5-6. As the cooks chop vegetables for dinner service, Chef Viktor Barinov "
    "reminds Max that great cooking starts with hand-picking the finest ingredients at the market."
)

INTRO = (
    "In the prep area of Claude Monet, knives click against cutting boards as cooks chop vegetables for dinner service. "
    "Chef Viktor Barinov inspects their technique and reminds young Max that culinary greatness begins long before cooking, "
    "with selecting the finest raw products at the market. "
    "Let's listen to their exchange in Russian first."
)

STORY = [
    ("chef", "Так, повара, нарежьте все овощи.",
     "So, cooks, chop all the vegetables.",
     [(5, "Режут")], "adapted"),
    ("anya", "Шеф, мы уже режем лук.",
     "Chef, we are already chopping onions.",
     [(5, "Режут")], "adapted"),
    ("chef", "Режьте быстрее, гости скоро придут.",
     "Chop faster, guests will come soon.",
     [], "new"),
    ("anya", "А где мы возьмём свежее мясо?",
     "And where will we get fresh meat?",
     [], "new"),
    ("chef", "Сначала повар выбирает лучшие продукты.",
     "First a cook selects the best products.",
     [(6, "Но сначала для вашего блюда выбирают лучшие продукты")], "adapted"),
    ("anya", "Мы покупаем мясо в магазине?",
     "Do we buy meat in a shop?",
     [], "new"),
    ("chef", "Нет, я сам выбираю всё на рынке.",
     "No, I choose everything myself at the market.",
     [(6, "выбирают лучшие продукты")], "adapted"),
    ("anya", "Вы лично проверяете каждый кусок?",
     "Do you personally inspect every piece?",
     [], "new"),
    ("chef", "Настоящий шеф не доверяет чужим людям.",
     "A real chef does not trust strangers.",
     [], "new"),
    ("anya", "Можно мне поехать с вами?",
     "May I go with you?",
     [], "new"),
    ("chef", "Ты останешься на кухне чистить картошку.",
     "You will stay in the kitchen peeling potatoes.",
     [], "new"),
    ("anya", "Я мечтал выбирать лучшие продукты.",
     "I dreamed of selecting the best products.",
     [], "new"),
    ("chef", "Сначала научись резать без ошибок!",
     "First learn to cut without mistakes!",
     [(5, "Режут")], "adapted"),
]

OPENER = "Now let's examine Barinov and Max's prep discussion line by line."

WALK = [
    (0, None,
     "'So, cooks, chop all the vegetables.' Barinov commands the kitchen staff with an imperative verb."),
    (1, None,
     "'Chef, we are already chopping onions.' Max reports on their current progress with a present imperfective verb."),
    (2, None,
     "'Chop faster, guests will come soon.' Barinov urges greater speed with a comparative adverb and future verb."),
    (3, None,
     "'And where will we get fresh meat?' Max inquires about the main ingredient using a question adverb and future verb."),
    (4, None,
     "'First a cook selects the best products.' Barinov reveals a foundational culinary principle using a superlative adjective."),
    (5, None,
     "'Do we buy meat in a shop?' Max asks about standard commercial purchasing channels."),
    (6, None,
     "'No, I choose everything myself at the market.' Barinov rejects commercial shortcuts, highlighting his personal selection."),
    (7, None,
     "'Do you personally inspect every piece?' Max asks with curiosity about the chef's hands-on inspection."),
    (8, None,
     "'A real chef does not trust strangers.' Barinov explains his philosophy of kitchen control with a negated verb."),
    (9, None,
     "'May I go with you?' Max eagerly asks for permission to join the shopping trip with a modal predicate."),
    (10, None,
     "'You will stay in the kitchen peeling potatoes.' Barinov assigns lowly prep duties with a future verb and infinitive."),
    (11, None,
     "'I dreamed of selecting the best products.' Max shares his culinary ambitions with a past imperfective verb."),
    (12, None,
     "'First learn to cut without mistakes!' Barinov shuts down the request with an imperative verb and prepositional phrase."),
]

TRANSITION = "Now let's listen to the kitchen prep discussion again without interruption."
OUTRO = (
    "Leaving Max to master chopping onions and peeling potatoes, Chef Barinov sets off for the morning market "
    "to inspect Timur's meat and negotiate for fresh delicacies."
)
CLOSING = ("chef", "Сначала научись резать без ошибок!")
