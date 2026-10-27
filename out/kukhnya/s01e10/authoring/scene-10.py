"""Authoring module for Kukhnya s01e10 scene 10."""
from pathlib import Path

ID = "kukhnya-s01e10-scene-10"
TITLE = "Срочный заём  (An Urgent Loan)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 10

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

SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")
SOURCE_NOTE = "Cues 77-86 at the kitchen food pass."

INTRO = (
    "In this scene at the restaurant pass, Chef Viktor Barinov hands over a dish for table five. "
    "Desperate to find money for his football bet before the match starts, Viktor tries to borrow tip money from Kostya. "
    "Listen to their hurried exchange in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this urgent kitchen interaction."
)

STORY = [
    ("kostya", "Шеф, давай уже быстрее заказ!", "Chef, hurry up the order already!", [(77, "давай уже быстрее.")], "adapted: added noun"),
    ("kostya", "Гость за пятым столиком ждёт.", "The guest at table five is waiting.", [(78, "за пятым столиком")], "adapted: simplified register"),
    ("anya", "Всё готово, можешь забирать блюдо.", "Everything is ready, you can take the dish.", [(79, "Все, можешь забирать.")], "adapted: added noun"),
    ("kostya", "Отлично, несу в зал.", "Great, taking it to the dining room.", [(80, "Отлично.")], "adapted: added action"),
    ("anya", "Стой, секунду, подожди меня здесь!", "Wait, one second, wait for me here!", [(80, "Стой, стой, стой, секунду. Подожди.")], "adapted: shortened"),
    ("kostya", "Шеф, мне надо сейчас работать.", "Chef, I need to work right now.", [(81, "Сейчас надо поделать.")], "adapted: standard verb"),
    ("anya", "Костя, скажи, как твои дела?", "Kostya, tell me, how are your affairs?", [(82, "Как дела?")], "adapted: polite greeting"),
    ("kostya", "Нормально, чаевые сегодня хорошие.", "Fine, tips are good today.", [(83, "Нормально.")], "adapted: added context"),
    ("anya", "Точно хорошие? Ты богатый человек!", "Really good? You are a wealthy man!", [(83, "Точно?")], "adapted: added flattery"),
    ("anya", "Мне просто занять немного нужно.", "I just need to borrow a little.", [(84, "Мне просто занять немного.")], "adapted: added verb"),
    ("kostya", "Шеф, вы хотите мои чаевые?", "Chef, you want my tips?", [], "new"),
    ("anya", "Всего пару тысяч до утра!", "Only a couple of thousand until morning!", [], "new"),
    ("kostya", "Шеф, давай попозже поговорим!", "Chef, let us talk later!", [(85, "Давай попозже поговорим.")], "adapted: added address"),
    ("anya", "Ладно, иди, но я вернусь!", "All right, go, but I will return!", [(86, "Ладно.")], "adapted: added promise"),
]

WALK = [
    (0, None, "'Chef, hurry up the order already!' Kostya rushes the kitchen line during service."),
    (1, None, "'The guest at table five is waiting.' Kostya highlights the demanding customer."),
    (2, None, "'Everything is ready, you can take the dish.' Viktor hands over the freshly prepared meal."),
    (3, None, "'Great, taking it to the dining room.' Kostya prepares to deliver the hot plate."),
    (4, None, "'Wait, one second, wait for me here!' Viktor halts the waiter before he can leave."),
    (5, None, "'Chef, I need to work right now.' Kostya points to his busy dining room duties."),
    (6, None, "'Kostya, tell me, how are your affairs?' Viktor tries small talk to break the ice."),
    (7, None, "'Fine, tips are good today.' Kostya mentions his successful shift at the tables."),
    (8, None, "'Really good? You are a wealthy man!' Viktor flatters him with exaggerated compliments."),
    (9, None, "'I just need to borrow a little.' Viktor makes his direct financial request."),
    (10, None, "'Chef, you want my tips?' Kostya reacts with protective disbelief."),
    (11, None, "'Only a couple of thousand until morning!' Viktor begs for a temporary emergency loan."),
    (12, None, "'Chef, let us talk later!' Kostya makes a swift excuse and hurries away."),
    (13, None, "'All right, go, but I will return!' Viktor calls after him with stubborn persistence."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A comical encounter showing Viktor Barinov's shameless willingness to borrow tip money from his staff."
)

CLOSING = ("anya", "Никто на кухне не ценит футбол.")
