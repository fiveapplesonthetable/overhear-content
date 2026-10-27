ID = "kukhnya-s01e18-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 4
TITLE = "Дорогой коньяк  (Expensive Cognac)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Cues 129-132. Max shows Kostya the cognac trick."

INTRO = "At the bar counter, Max shows Kostya another way to make extra money by serving cognac. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Это ещё не всё, слушай дальше.",
     "That is not all yet, listen further.",
     [(129, "Еще не все. Слушай дальше.")], "adapted"),
    ("kostya", "Какой ещё секрет ты мне покажешь?",
     "What other secret will you show me?",
     [], "new"),
    ("anya", "Сейчас я покажу тебе новый фокус.",
     "Now I will show you a new trick.",
     [], "new"),
    ("anya", "Короче, сначала ты берёшь чистый стакан.",
     "In short, first you take a clean glass.",
     [(130, "берешь стакан")], "adapted"),
    ("kostya", "Хорошо, я взял большой красивый бокал.",
     "Alright, I took a large beautiful glass.",
     [], "new"),
    ("anya", "Теперь представь, что я богатый гость.",
     "Now imagine that I am a rich guest.",
     [], "new"),
    ("kostya", "Что вы желаете заказать сегодня вечером?",
     "What would you like to order tonight?",
     [], "new"),
    ("anya", "Налей мне пятьдесят грамм дорогого коньяка.",
     "Pour me fifty grams of expensive cognac.",
     [(131, "50 грамм")], "adapted"),
    ("kostya", "Отличный выбор, сейчас всё будет сделано.",
     "Great choice, everything will be done right now.",
     [(132, "Будет сделано.")], "adapted"),
    ("anya", "Но наливай не дорогой, а дешёвый коньяк!",
     "But pour cheap cognac, not the expensive one!",
     [], "new"),
    ("kostya", "Ты думаешь, гость совсем ничего не заметит?",
     "Do you think the guest will notice nothing at all?",
     [], "new"),
    ("anya", "Поверь мне, никто не почувствует разницу!",
     "Believe me, nobody will feel the difference!",
     [], "new"),
]

OPENER = "Let's break down this bar demonstration."

WALK = [
    (0, None,
     "'That is not all yet, listen further.' -- Max tells his friend that there are more tricks to learn."),
    (1, None,
     "'What other secret will you show me?' -- Kostya is curious about the next method."),
    (2, None,
     "'Now I will show you a new trick.' -- Max prepares to demonstrate another technique at the bar."),
    (3, None,
     "'In short, first you take a clean glass.' -- He instructs Kostya to pick up a vessel from the shelf."),
    (4, None,
     "'Alright, I took a large beautiful glass.' -- Kostya follows the instruction and holds it ready."),
    (5, None,
     "'Now imagine that I am a rich guest.' -- Max pretends to be a wealthy customer sitting at the counter."),
    (6, None,
     "'What would you like to order tonight?' -- Kostya plays along with a polite question."),
    (7, None,
     "'Pour me fifty grams of expensive cognac.' -- Max places an order for a luxury drink."),
    (8, None,
     "'Great choice, everything will be done right now.' -- Kostya replies like a professional bartender."),
    (9, None,
     "'But pour cheap cognac, not the expensive one!' -- Max reveals the secret swap to save money."),
    (10, None,
     "'Do you think the guest will notice nothing at all?' -- Kostya doubts that customers can be fooled so easily."),
    (11, None,
     "'Believe me, nobody will feel the difference!' -- Max assures him that patrons cannot tell the brands apart."),
]

TRANSITION = "Now let's listen to the scene again without interruption."
OUTRO = "Kostya pours the drink as Max finishes his lesson on bar economics."
CLOSING = ("anya", "Поверь мне, никто не почувствует разницу!")
