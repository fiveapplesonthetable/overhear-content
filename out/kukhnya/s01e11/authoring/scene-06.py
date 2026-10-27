"""Authoring module for Kukhnya s01e11 scene 06."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-06"
TITLE = "Отказ от салата  (The Rejected Salad)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 6

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Шеф",
    "kostya": "Костя",
}

SOURCE_NAME = "Кухня s01e11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 72-77 in the kitchen."

INTRO = (
    "In this scene in the kitchen, waiter Kostya rushes to Chef Viktor Barinov with terrifying news. "
    "A guest at table seven, suspected of being a secret food critic, has just sent back her salad, complaining about the sour dressing. "
    "Listen to their panicked conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this dramatic kitchen crisis."
)

STORY = [
    ("kostya", "Шеф, внимание! На кухне чрезвычайная ситуация.", "Chef, attention! An emergency situation in the kitchen.", [(72, "внимание")], "adapted: added warning"),
    ("anya", "Костя, что случилось в зале?", "Kostya, what happened in the dining room?", [], "new"),
    ("kostya", "Обнаружен предполагаемый ресторанный критик!", "A suspected restaurant critic has been spotted!", [(73, "Обнаружен предполагаемый критик.")], "adapted: added adjective"),
    ("kostya", "Она сидит за седьмым столиком.", "She is sitting at table seven.", [(74, "сидит за седьмым столиком.")], "adapted: feminine pronoun"),
    ("kostya", "И у меня отказ от салата!", "And I have a salad rejection!", [(75, "У меня отказ от салата.")], "adapted: added conjunction"),
    ("anya", "Как отказ? Мой идеальный салат?", "How, a rejection? My perfect salad?", [(76, "Как отказ?")], "adapted: added reaction"),
    ("kostya", "Она вернула тарелку назад, шеф.", "She sent the plate back, chef.", [], "new"),
    ("anya", "Какой столик? Точно седьмой?", "Which table? Definitely the seventh?", [(77, "Какой столик? Седьмой.")], "adapted: added question"),
    ("kostya", "Да, строгая дама в очках.", "Yes, a strict lady in glasses.", [], "new"),
    ("anya", "Что именно ей не понравилось?", "What exactly did she not like?", [], "new"),
    ("kostya", "Сказала, что соус слишком кислый.", "She said the sauce was too sour.", [], "new"),
    ("anya", "Это авторский рецепт высокой кухни!", "This is an author recipe of haute cuisine!", [], "new"),
    ("kostya", "Шеф, она уже открыла блокнот.", "Chef, she has already opened a notepad.", [], "new"),
    ("anya", "Я лично приготовлю ей десерт!", "I will personally prepare her a dessert!", [], "new"),
]

WALK = [
    (0, None, "'Chef, attention! An emergency situation in the kitchen.' Kostya bursts into the workspace with urgent news."),
    (1, None, "'Kostya, what happened in the dining room?' Viktor asks as he stops cooking."),
    (2, None, "'A suspected restaurant critic has been spotted!' Kostya delivers the alarming announcement."),
    (3, None, "'She is sitting at table seven.' Kostya identifies the exact location of the threat."),
    (4, None, "'And I have a salad rejection!' Kostya reports the disastrous development."),
    (5, None, "'How, a rejection? My perfect salad?' Viktor gasps in personal and professional shock."),
    (6, None, "'She sent the plate back, chef.' Kostya confirms that the dish was refused."),
    (7, None, "'Which table? Definitely the seventh?' Viktor demands precise confirmation of the customer."),
    (8, None, "'Yes, a strict lady in glasses.' Kostya describes the appearance of the difficult diner."),
    (9, None, "'What exactly did she not like?' Viktor asks for the culinary criticism."),
    (10, None, "'She said the sauce was too sour.' Kostya relays her sharp feedback."),
    (11, None, "'This is an author recipe of haute cuisine!' Viktor defends his refined flavor profile."),
    (12, None, "'Chef, she has already opened a notepad.' Kostya warns that a review is being written."),
    (13, None, "'I will personally prepare her a dessert!' Viktor vows to win over the critic with sweet culinary mastery."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A tense comedic moment as Chef Barinov prepares to defend his kitchen's reputation against a ruthless reviewer."
)

CLOSING = ("anya", "Мы спасем репутацию нашего ресторана!")
