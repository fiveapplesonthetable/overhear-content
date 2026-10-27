ID = "kukhnya-s01e17-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 2
TITLE = "Возвращение на кухню  (Return to the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "shef": "anja"}
LABELS = {"anya": "Макс", "shef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 33-34. Walking back to Claude Monet after shopping, Max and Viktor discuss their culinary standards "
    "and the reputation of the neighboring Italian restaurant Arcobaleno."
)

INTRO = (
    "Carrying their market purchases through the street, Viktor and Max head back toward Claude Monet. "
    "Max brings up rumors about their competitors, prompting Viktor to vigorously defend the honor of his kitchen. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("shef", "Витя, держи рыбу крепче!",
     "Vitya, hold the fish tighter!",
     [(33, "Вить!"), (34, "Сынче,")], "adapted"),
    ("anya", "Шеф, я держу всё очень крепко.",
     "Chef, I am holding everything very tightly.",
     [], "new"),
    ("shef", "Мы уже почти пришли в ресторан.",
     "We have already almost arrived at the restaurant.",
     [], "new"),
    ("anya", "Вы действительно пойдёте в соседний ресторан?",
     "Will you really go to the neighboring restaurant?",
     [(20, "Вы же к нам собираетесь с ответным визитом"), (26, "Ты что, был в Варкабалена?")], "adapted"),
    ("shef", "Мне делать больше нечего, Макс.",
     "I have nothing better to do, Max.",
     [(23, "Вот чёрт, делать мне больше нечего.")], "adapted"),
    ("anya", "Говорят, там готовят неплохие блюда.",
     "They say they cook pretty good dishes there.",
     [(24, "там очень даже ничего.")], "adapted"),
    ("shef", "Кто тебе сказал такую глупость?",
     "Who told you such foolishness?",
     [(25, "Да ты-то откуда знаешь?")], "adapted"),
    ("anya", "Один мой хороший друг рассказывал.",
     "A good friend of mine told me.",
     [(29, "Просто мне друг рассказывал")], "adapted"),
    ("shef", "Твой друг ничего не понимает в еде.",
     "Your friend understands nothing about food.",
     [(31, "И человек он был, честно говоря, так себе.")], "adapted"),
    ("anya", "Наверное, вы правы, шеф.",
     "Probably you are right, chef.",
     [(32, "Да ладно, я так просто спросил.")], "adapted"),
    ("shef", "Наш ресторан — самый лучший в городе.",
     "Our restaurant is the best in the city.",
     [], "new"),
    ("anya", "Я согласен с вами на сто процентов.",
     "I agree with you one hundred percent.",
     [], "new"),
    ("shef", "Тогда быстро иди работать на кухню.",
     "Then quickly go work in the kitchen.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Vitya, hold the fish tighter!' -- Viktor warns his cook not to drop the food."),
    (1, None,
     "'Chef, I am holding everything very tightly.' -- Max reassures his boss that the bag is safe."),
    (2, None,
     "'We have already almost arrived at the restaurant.' -- The chef notes they are close to the door."),
    (3, None,
     "'Will you really go to the neighboring restaurant?' -- Max asks about the planned visit to Arcobaleno."),
    (4, None,
     "'I have nothing better to do, Max.' -- Viktor sarcastically dismisses the idea of visiting his rivals."),
    (5, None,
     "'They say they cook pretty good dishes there.' -- The young cook repeats local rumors."),
    (6, None,
     "'Who told you such foolishness?' -- Viktor demands to know where he heard that nonsense."),
    (7, None,
     "'A good friend of mine told me.' -- Max explains his source of information."),
    (8, None,
     "'Your friend understands nothing about food.' -- The chef scoffs at the friend's culinary taste."),
    (9, None,
     "'Probably you are right, chef.' -- Max quickly concedes to avoid angering the chef."),
    (10, None,
     "'Our restaurant is the best in the city.' -- Viktor proudly asserts the superiority of Claude Monet."),
    (11, None,
     "'I agree with you one hundred percent.' -- Max expresses complete support for his mentor."),
    (12, None,
     "'Then quickly go work in the kitchen.' -- Viktor orders him to get ready for the shift."),
]

TRANSITION = "Now let's listen to the walk back to the restaurant once again."

OUTRO = (
    "Arriving at the back entrance of Claude Monet, Viktor and Max step inside, "
    "ready to face another demanding day in the restaurant kitchen."
)

CLOSING = ("shef", "Тогда быстро иди работать на кухню.")
