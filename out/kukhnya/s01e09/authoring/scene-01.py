ID = "kukhnya-s01e09-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 1
TITLE = "Заказ на банкет  (The Banquet Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Луи", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-17. In the kitchen, pastry chef Louis panics over a massive banquet order. "
    "Chef Barinov assigns Max to be his helper."
)

INTRO = (
    "In the bustling kitchen of Claude Monet, French pastry chef Louis is overwhelmed by an enormous banquet order. "
    "Desperate for assistance, he appeals to Chef Viktor Barinov, who decides that novice cook Max will be his "
    "helper for the day. Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Шеф, у меня большие проблемы.",
     "Chef, I have big problems.",
     [(1, "У меня проблемы.")], "adapted"),
    ("chef", "Что опять случилось на кухне?",
     "What happened in the kitchen again?",
     [], "new"),
    ("anya", "Мне срочно нужен хороший помощник.",
     "I urgently need a good assistant.",
     [(1, "Мне очень срочно нужен"), (7, "тебе нужен помощник.")], "adapted"),
    ("chef", "Почему ты не работаешь один?",
     "Why are you not working alone?",
     [], "new"),
    ("anya", "Я один сегодня не справлюсь.",
     "I alone will not manage today.",
     [(4, "Я один не справлюсь.")], "adapted"),
    ("chef", "У тебя слишком много работы?",
     "Do you have too much work?",
     [], "new"),
    ("anya", "Пришёл очень большой заказ на банкет.",
     "A very big banquet order arrived.",
     [(5, "Очень большой заказ на банкет.")], "adapted"),
    ("chef", "Что именно нужно приготовить?",
     "What exactly needs to be prepared?",
     [], "new"),
    ("anya", "Свежие круассаны и большой торт.",
     "Fresh croissants and a big cake.",
     [(6, "Круассаны")], "adapted"),
    ("chef", "Макс будет работать с тобой.",
     "Max will work with you.",
     [(16, "Макс сегодня твой")], "adapted"),
    ("anya", "Но он ничего не умеет.",
     "But he does not know how to do anything.",
     [], "new"),
    ("chef", "Он будет чистить и резать.",
     "He will peel and cut.",
     [], "new"),
    ("anya", "Ладно, пусть моет посуду.",
     "Fine, let him wash the dishes.",
     [], "new"),
]

OPENER = "Now let's examine Louis and Chef Barinov's kitchen exchange line by line."

WALK = [
    (0, None,
     "'Chef, I have big problems.' -- Louis calls out to Chef Barinov, stating that he faces severe trouble in the pastry kitchen."),
    (1, None,
     "'What happened in the kitchen again?' -- Barinov asks gruffly, wanting to know what new crisis has occurred."),
    (2, None,
     "'I urgently need a good assistant.' -- Louis explains that he requires a capable helper right away."),
    (3, None,
     "'Why are you not working alone?' -- Barinov questions why the French pastry chef cannot manage by himself."),
    (4, None,
     "'I alone will not manage today.' -- Louis admits that handling the workload alone is completely impossible."),
    (5, None,
     "'Do you have too much work?' -- The chef inquires whether the volume of preparation is truly excessive."),
    (6, None,
     "'A very big banquet order arrived.' -- Louis reveals that a massive banquet booking has been received."),
    (7, None,
     "'What exactly needs to be prepared?' -- Barinov asks for specific details about the required menu items."),
    (8, None,
     "'Fresh croissants and a big cake.' -- Louis lists the pastries, including fresh croissants and a large cake."),
    (9, None,
     "'Max will work with you.' -- The chef decides to send junior cook Max to assist him for the shift."),
    (10, None,
     "'But he does not know how to do anything.' -- Louis complains that the novice cook lacks proper culinary skill."),
    (11, None,
     "'He will peel and cut.' -- Barinov points out that basic tasks like peeling and chopping will save time."),
    (12, None,
     "'Fine, let him wash the dishes.' -- Louis reluctantly agrees, deciding the newcomer can at least handle washing up."),
]

TRANSITION = "Now let's listen to the kitchen conversation again without interruption."
OUTRO = (
    "With a skeptical Louis reluctantly accepting Max's assistance, the kitchen prepares to tackle "
    "the demanding banquet pastry order under Chef Barinov's watchful eye."
)
CLOSING = ("anya", "Ладно, пусть моет посуду.")
