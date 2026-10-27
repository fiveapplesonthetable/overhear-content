"""Authoring module for Kukhnya s01e12 scene 05."""
from pathlib import Path

ID = "kukhnya-s01e12-scene-05"
TITLE = "Опасные конкуренты  (Dangerous Competitors)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 5

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Вика",
    "chef": "Шеф",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = Path("sources/kukhnya/s01/e12.ru.dual.srt")
SOURCE_NOTE = "Cues 38-58 in the restaurant hallway and kitchen."

INTRO = (
    "Victoria approaches Chef Barinov with a colorful advertising flyer for a new Italian restaurant, Arcobaleno, opening right next door. "
    "While Victoria urgently presses for fresh menu updates to meet the incoming competition, Barinov vehemently refuses any changes to his kitchen. "
    "Let's listen to their heated debate in Russian."
)

OPENER = (
    "Now let's examine how Victoria and Barinov clash over the new restaurant competition line by line."
)

STORY = [
    ("anya", "Витя, посмотри на этот рекламный буклет!",
     "Vitya, look at this advertising flyer!",
     [(41, "Полюбуйся.")], "Vika shows the flyer"),

    ("chef", "Что это за странное слово Аркобалено?",
     "What kind of strange word is Arcobaleno?",
     [(42, "ресторана Аркобалена.")], "Barinov sneers at the name"),

    ("chef", "Это вообще что, редкая болезнь почек?",
     "What is that anyway, a rare kidney disease?",
     [(45, "Это вообще что, болезнь почек?")], "Barinov mocks the name"),

    ("anya", "Аркобалено значит радуга по-итальянски, Витя.",
     "Arcobaleno means rainbow in Italian, Vitya.",
     [(46, "Аркабалена – это радуга по-итальянски.")], "Vika translates the name"),

    ("chef", "Я не пойду в их кафе!",
     "I will not go to their cafe!",
     [(43, "я к ним не приду.")], "Barinov rejects the venue"),

    ("anya", "Через неделю они открываются рядом с нами.",
     "In a week they are opening right next to us.",
     [(48, "У нас под боком через неделю открываются конкуренты.")], "Vika points out the threat"),

    ("chef", "Ой, боюсь, кафе Радуга нас разорит!",
     "Oh, I am scared, cafe Rainbow will bankrupt us!",
     [(49, "Боюсь, боюсь. Кафе «Радуга» разорит нас.")], "Barinov mocks the competition"),

    ("anya", "Витя, нам пора привлечь новых гостей.",
     "Vitya, it is time for us to attract new guests.",
     [(54, "Нам нужно привлечь людей чем-то новым.")], "Vika urges proactive steps"),

    ("anya", "Нам нужно срочно поменять наше меню.",
     "We need to urgently change our menu.",
     [(55, "Меню поменять.")], "Vika proposes menu change"),

    ("chef", "Мы лучшие, и нас любят за это!",
     "We are the best, and people love us for that!",
     [(55, "Мы такие, какие есть, и за это нас любят.")], "Barinov asserts quality"),

    ("anya", "Ресторану нужны свежие и смелые идеи.",
     "The restaurant needs fresh and bold ideas.",
     [], "Vika emphasizes modern approaches"),

    ("chef", "Меняй всё в зале, на своей территории!",
     "Change everything in the dining room, on your turf!",
     [(56, "меняй на своей территории, в зале.")], "Barinov defines boundaries"),

    ("chef", "А на кухню ко мне не лезь!",
     "And do not get into my kitchen!",
     [(57, "А ко мне на кухню не лезь.")], "Barinov bans interference"),
]

WALK = [
    (0, None,
     "'Vitya, look at this advertising flyer!' Victoria shows the promotional material to Barinov."),
    (1, None,
     "'What kind of strange word is Arcobaleno?' Barinov questions the foreign name with disgust."),
    (2, None,
     "'What is that anyway, a rare kidney disease?' He mocks the unusual restaurant name sarcastically."),
    (3, None,
     "'Arcobaleno means rainbow in Italian, Vitya.' Victoria explains the literal meaning patiently."),
    (4, None,
     "'I will not go to their cafe!' Barinov refuses to show any interest in their business."),
    (5, None,
     "'In a week they are opening right next to us.' Victoria warns him of the impending competition."),
    (6, None,
     "'Oh, I am scared, cafe Rainbow will bankrupt us!' Barinov ridicules the notion that they pose a threat."),
    (7, None,
     "'Vitya, it is time for us to attract new guests.' Victoria urges an urgent update to their approach."),
    (8, None,
     "'We need to urgently change our menu.' She suggests refreshing their culinary offerings."),
    (9, None,
     "'We are the best, and people love us for that!' Barinov proudly defends his classic recipes with passion."),
    (10, None,
     "'The restaurant needs fresh and bold ideas.' Victoria insists on modern marketing strategies."),
    (11, None,
     "'Change everything in the dining room, on your turf!' Barinov draws a clear line between front of house and kitchen."),
    (12, None,
     "'And do not get into my kitchen!' He strictly forbids any administrative interference in his domain."),
]

TRANSITION = (
    "Now let's listen to the debate over the rival restaurant and kitchen management once more."
)

OUTRO = (
    "Refusing to alter his culinary traditions, Barinov retreats to his kitchen while Victoria seeks other ways to compete."
)

CLOSING = ("chef", "А на кухню ко мне не лезь!")
