ID = "kukhnya-s01e03-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = "Живой гусь  (The Live Goose)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 46-60. Max arrives in the kitchen eager to cook after days of unloading boxes. "
    "However, Chef Viktor Barinov presents a live goose delivered for tonight's VIP banquet "
    "and insists every genuine chef must know how to butcher meat."
)

INTRO = (
    "Max arrives in the Claude Monet kitchen eager to start cooking after a full week of manual unloading. "
    "Instead of a saucepan, Chef Viktor Barinov hands him a live goose delivered for tonight's grand banquet. "
    "Barinov declares that every true cook must be able to slaughter and prepare their own meat. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("anya", "Доброе утро, шеф!",
     "Good morning, chef!",
     [(46, "Доброе утро, шеф")], ""),
    ("chef", "Здравствуй, огузок. Вот твоя работа.",
     "Hello, oguzok. Here is your work.",
     [(48, "Иди разгружай продукты")], "adapted"),
    ("anya", "Шеф, это живой гусь!",
     "Chef, this is a live goose!",
     [(36, "Это чего? Гусь"), (40, "живой гусь")], "adapted"),
    ("chef", "У нас сегодня очень важный банкет.",
     "We have a very important banquet today.",
     [(38, "у нас же сегодня банкет")], "adapted"),
    ("anya", "Зачем нам живой гусь на кухне?",
     "Why do we need a live goose in the kitchen?",
     [(40, "На хрена мне на кухне живой гусь")], "adapted"),
    ("chef", "Гостям нужен самый свежий продукт!",
     "The guests need the freshest product!",
     [(41, "вы просили самого свежего")], "adapted"),
    ("anya", "Но я повар, а не мясник.",
     "But I am a cook, not a butcher.",
     [(49, "ну я же не грузчик, я повар")], "adapted"),
    ("chef", "Каждый повар обязан уметь разделывать мясо.",
     "Every chef is obliged to know how to butcher meat.",
     [(59, "Каждый повар должен быть готов")], "adapted"),
    ("anya", "Что, мне нужно убить его?",
     "What, do I need to kill it?",
     [(56, "Что, прям насмерть")], "adapted"),
    ("chef", "А ты думал, мясо растёт на деревьях?",
     "Did you think meat grows on trees?",
     [(58, "ты думаешь, что мясо кусочком на деревьях растет")], "adapted"),
    ("anya", "Я никогда в жизни этого не делал.",
     "I have never done this in my life.",
     [], "new"),
    ("chef", "Убей гуся, или ты уволен!",
     "Kill the goose, or you are fired!",
     [(53, "Убей гуся"), (60, "Убей, гуся")], "adapted"),
    ("anya", "Хорошо, я попробую сделать это.",
     "Fine, I will try to do it.",
     [], "new"),
]

OPENER = "Now let's examine Chef Barinov and Max's tense dialogue line by line."

WALK = [
    (0, None,
     "'Good morning, chef!' Max greets the head chef warmly with an adjective and vocative noun."),
    (1, None,
     "'Hello, oguzok. Here is your work.' Barinov answers gruffly using his favorite derogatory nickname."),
    (2, None,
     "'Chef, this is a live goose!' Max reacts with shock using an adjective and nominative noun."),
    (3, None,
     "'We have a very important banquet today.' The head chef emphasizes the event with an adverb and adjective."),
    (4, None,
     "'Why do we need a live goose in the kitchen?' Max questions the situation with an interrogative adverb."),
    (5, None,
     "'The guests need the freshest product!' Barinov justifies the delivery using a dative noun and superlative adjective."),
    (6, None,
     "'But I am a cook, not a butcher.' Max defends his profession with contrasting predicate nouns."),
    (7, None,
     "'Every chef is obliged to know how to butcher meat.' The chef states kitchen standards with paired infinitives."),
    (8, None,
     "'What, do I need to kill it?' Max asks in disbelief using an impersonal modal construction."),
    (9, None,
     "'Did you think meat grows on trees?' Barinov uses a sarcastic rhetorical question in the past tense."),
    (10, None,
     "'I have never done this in my life.' Max confesses his complete lack of butchery experience."),
    (11, None,
     "'Kill the goose, or you are fired!' The chef issues a strict ultimatum with an imperative verb."),
    (12, None,
     "'Fine, I will try to do it.' Max reluctantly accepts the challenge using a future perfective verb."),
]

TRANSITION = "Now let's listen to Chef Barinov and Max's kitchen exchange again without interruption."
OUTRO = (
    "Faced with Barinov's ultimatum, Max takes the live bird to the back alley to figure out how to slaughter it. "
    "In the next scene, waitress Nastya and cleaner Ainura debate vegetarianism over staff lunch."
)
CLOSING = ("anya", "Хорошо, я попробую сделать это.")
