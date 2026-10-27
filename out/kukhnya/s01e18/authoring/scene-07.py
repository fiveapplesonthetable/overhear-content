ID = "kukhnya-s01e18-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 7
TITLE = "Жадный хозяин  (The Greedy Owner)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Шеф", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 140-167. Nagiyev enforces extreme austerity across Claude Monet, "
    "turning off lights and rejecting fresh ingredients, while Chef Viktor protests."
)

INTRO = (
    "In the dining room and kitchen of Claude Monet, owner Dmitry Nagiyev enforces extreme "
    "cost-cutting measures, turning off lights and rejecting fresh veal. Chef Viktor confronts "
    "him over the absurd penny-pinching. Let us listen to their heated exchange in Russian first."
)

STORY = [
    ("anya", "Дмитрий, почему здесь выключили яркий свет?",
     "Dmitry, why did they turn off the bright light here?",
     [(140, "Слушай, что так темно, а?")], "adapted"),
    ("nagiyev", "Мы не должны тратить деньги на свет.",
     "We must not spend money on electricity.",
     [(141, "Экономия.")], "adapted"),
    ("anya", "Но поварам трудно готовить в тёмном зале!",
     "However, it is hard for cooks to prepare food in a dark hall!",
     [], "new"),
    ("nagiyev", "Зато наш ресторан сохранит много полезных рублей.",
     "On the other hand, our restaurant will save many useful rubles.",
     [], "new"),
    ("anya", "Тимур только что привёз нам свежее мясо.",
     "Timur has just brought us fresh meat.",
     [(153, "У Тимура всегда самый лучший продукт.")], "adapted"),
    ("nagiyev", "Это мясо стоит слишком много дорогих денег!",
     "This meat costs far too much expensive money!",
     [(146, "Чего так дорого, а? Как дорого?")], "adapted"),
    ("anya", "Но у него всегда самые лучшие продукты.",
     "However, he always provides the very best products.",
     [(153, "У Тимура всегда самый лучший продукт.")], "adapted"),
    ("nagiyev", "Покупай только дешёвое мясо за мои деньги.",
     "Buy only cheap meat using my money.",
     [(155, "А на мои покупай просто. Хорошие.")], "adapted"),
    ("anya", "Наши гости заметят плохое качество этих блюд.",
     "Our guests will notice the poor quality of these dishes.",
     [], "new"),
    ("nagiyev", "Пусть официанты зажгут красивые свечи на столах.",
     "Let the waiters light beautiful candles on the tables.",
     [(165, "Свечи зажгите.")], "adapted"),
    ("anya", "Свечи не помогут спасти плохой ужин.",
     "Candles will not help save a bad dinner.",
     [], "new"),
    ("nagiyev", "Это прекрасный и дешёвый романтический ход!",
     "This is a wonderful and cheap romantic move!",
     [(167, "Экономия. Маркетинговый ход.")], "adapted"),
    ("anya", "Вы становитесь слишком жадным хозяином, Дмитрий!",
     "You are becoming too greedy an owner, Dmitry!",
     [], "new"),
]

OPENER = "Now let us examine Viktor and Dmitry's argument line by line."

WALK = [
    (0, None,
     "'Dmitry, why did they turn off the bright light here?' -- Viktor questions the sudden darkness in the restaurant."),
    (1, None,
     "'We must not spend money on electricity.' -- Nagiyev defends his extreme cost-cutting approach."),
    (2, None,
     "'However, it is hard for cooks to prepare food in a dark hall!' -- The chef protests the difficult working conditions."),
    (3, None,
     "'On the other hand, our restaurant will save many useful rubles.' -- The owner focuses strictly on saving cash."),
    (4, None,
     "'Timur has just brought us fresh meat.' -- Viktor announces the arrival of high-quality ingredients."),
    (5, None,
     "'This meat costs far too much expensive money!' -- Nagiyev refuses to approve top-grade purchases."),
    (6, None,
     "'However, he always provides the very best products.' -- Viktor defends their supplier's exceptional standards."),
    (7, None,
     "'Buy only cheap meat using my money.' -- Nagiyev orders the kitchen to downgrade quality."),
    (8, None,
     "'Our guests will notice the poor quality of these dishes.' -- Viktor warns of customer dissatisfaction."),
    (9, None,
     "'Let the waiters light beautiful candles on the tables.' -- The owner suggests an atmospheric cover-up."),
    (10, None,
     "'Candles will not help save a bad dinner.' -- Viktor points out the flaw in the marketing gimmick."),
    (11, None,
     "'This is a wonderful and cheap romantic move!' -- Nagiyev insists his scheme is brilliant."),
    (12, None,
     "'You are becoming too greedy an owner, Dmitry!' -- Viktor directly confronts the owner over his absurd frugality."),
]

TRANSITION = "Now let us listen to the complete confrontation once again."
OUTRO = (
    "Faced with Dmitry Nagiyev's extreme austerity and penny-pinching, Chef Viktor warns that "
    "sacrificing ingredient quality and dining atmosphere will drive customers away."
)
CLOSING = ("anya", "Вы становитесь слишком жадным хозяином, Дмитрий!")
