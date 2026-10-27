ID = "kukhnya-s01e12-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 16
TITLE = "Ресторан напротив  (The Restaurant Across the Street)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 213-233. Chef Viktor and Victoria discover flyers for rival luxury restaurant Arcobalena "
    "opening across the street, sparking Barinov's furious culinary pride."
)

INTRO = (
    "Outside Claude Monet, Chef Viktor is outraged to discover a promoter handing out flyers "
    "for a new rival restaurant, Arcobalena, opening right across the street. The competitor "
    "boldly boasts of superior cuisine and luxury service, pushing Viktor into a passionate defense "
    "of his kitchen. Let us listen to their dialogue in Russian first."
)

STORY = [
    ("chef", "Посмотри, что раздают прямо у нашей двери!",
     "Look at what they hand out right at our door!",
     [(221, "что я нашел под дверью ресторана")], "adapted"),
    ("anya", "Что это за странная яркая бумага?",
     "What is this strange bright paper?",
     [], "new"),
    ("chef", "Рядом новый ресторан открывается уже сегодня.",
     "Nearby a new restaurant is opening today.",
     [(213, "новый ресторан «Аркабалена»")], "adapted"),
    ("anya", "Они называют себя лучшим рестораном города.",
     "They call themselves the best restaurant in town.",
     [(214, "Современный ресторан класса «Люкс»")], "adapted"),
    ("chef", "Они нагло раздают рекламу нашим гостям!",
     "They brazenly hand out advertisements to our guests!",
     [(216, "там бы раздал")], "adapted"),
    ("anya", "Неужели они обещают более вкусную еду?",
     "Could they really be promising tastier food?",
     [(215, "будет намного вкуснее")], "adapted"),
    ("chef", "Они пишут, что у них намного лучше.",
     "They write that with them it is much better.",
     [(215, "и уютнее, чем тут")], "adapted"),
    ("anya", "Шеф, не надо так сильно нервничать.",
     "Chef, you should not be so nervous.",
     [(226, "Надо же, как вы нервничаете")], "adapted"),
    ("chef", "Я пойду и прогоню этого наглого парня.",
     "I will go and chase away this insolent fellow.",
     [(224, "Еще одного клоуна найду")], "adapted"),
    ("anya", "Мы просто должны показать высший класс.",
     "We simply must show top quality.",
     [], "new"),
    ("chef", "Наш ресторан лучший во всей Москве!",
     "Our restaurant is the best in all Moscow!",
     [], "new"),
    ("anya", "Ни один наш постоянный гость не уйдёт.",
     "Not a single regular guest of ours will leave.",
     [(227, "Боитесь, что к вам сегодня никто не придет?")], "adapted"),
    ("chef", "Пусть сначала попробуют нормально открыться!",
     "Let them try opening properly first!",
     [(229, "Да вы откройтесь для начала")], "adapted"),
]

OPENER = "Now let us examine Viktor and Victoria's heated reaction line by line."

WALK = [
    (0, None,
     "'Look at what they hand out right at our door!' -- Viktor shows Victoria the aggressive marketing flyer."),
    (1, None,
     "'What is this strange bright paper?' -- Victoria asks about the promotional material."),
    (2, None,
     "'Nearby a new restaurant is opening today.' -- The chef explains that competitor Arcobalena is opening."),
    (3, None,
     "'They call themselves the best restaurant in town.' -- The manager reads the pompous marketing slogan."),
    (4, None,
     "'They brazenly hand out advertisements to our guests!' -- Viktor vents his anger at promotional poachers."),
    (5, None,
     "'Could they really be promising tastier food?' -- Victoria questions the bold claims of the competitor."),
    (6, None,
     "'They write that with them it is much better.' -- The chef quotes their boastful promise of superiority."),
    (7, None,
     "'Chef, you should not be so nervous.' -- The manager urges Viktor to remain calm and collected."),
    (8, None,
     "'I will go and chase away this insolent fellow.' -- Viktor vows to drive the flyer promoter away."),
    (9, None,
     "'We simply must show top quality.' -- Victoria advises proving their superiority through excellent dining."),
    (10, None,
     "'Our restaurant is the best in all Moscow!' -- The proud chef proclaims Claude Monet supreme status."),
    (11, None,
     "'Not a single regular guest of ours will leave.' -- Victoria reassures him of their patrons loyal devotion."),
    (12, None,
     "'Let them try opening properly first!' -- Viktor dismisses the fledgling rival with fierce skepticism."),
]

TRANSITION = "Now let us listen to the spirited exchange between Viktor and Victoria again."
OUTRO = (
    "Faced with brazen competition from Arcobalena across the street, Viktor and Victoria "
    "unite to defend Claude Monet's honor, determined to outperform their new rival."
)
CLOSING = ("chef", "Пусть сначала попробуют нормально открыться!")
