"""Authoring module for Kukhnya s01e10 scene 09."""
from pathlib import Path

ID = "kukhnya-s01e10-scene-09"
TITLE = "Старый долг  (An Old Debt)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 9

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Шеф",
    "fedya": "Федя",
}

SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")
SOURCE_NOTE = "Cues 73-76 in the kitchen fish station."

INTRO = (
    "In this scene in the kitchen, Chef Viktor Barinov tries to borrow cash from his line cook Fedya. "
    "Desperate to bet on the Spartak derby, Viktor flatters his cook, only for Fedya to remind him of an outstanding debt. "
    "Listen to their conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this kitchen financial plea."
)

STORY = [
    ("anya", "Федя, дорогой мой друг!", "Fedya, my dear friend!", [(73, "ружище")], "adapted: polite vocative"),
    ("fedya", "Шеф, почему вы такой добрый?", "Chef, why are you so kind?", [], "new"),
    ("anya", "Мне срочно нужна твоя помощь.", "I urgently need your help.", [], "new"),
    ("fedya", "Не, шеф, я абсолютно пустой!", "No, chef, I am completely broke!", [(74, "Не, шеф, я пустой.")], "adapted: added emphasis"),
    ("anya", "Даже пары тысяч не найдется?", "Not even a couple of thousand can be found?", [], "new"),
    ("fedya", "Вы мне еще пять тысяч должны!", "You still owe me five thousand!", [(75, "Кроме того, вы мне еще пять тысяч должны.")], "adapted: shortened"),
    ("anya", "Я всё верну завтра утром!", "I will return everything tomorrow morning!", [], "new"),
    ("fedya", "Вы всегда так обещаете, шеф.", "You always promise that, chef.", [], "new"),
    ("anya", "Но сегодня Спартак точно победит!", "But today Spartak will definitely win!", [], "new"),
    ("fedya", "Спартак играет против сильного соперника.", "Spartak is playing against a strong opponent.", [], "new"),
    ("anya", "У них проблемы с составом!", "They have roster problems!", [], "new"),
    ("fedya", "Шеф, футбол это чистая лотерея.", "Chef, football is pure lottery.", [], "new"),
    ("anya", "Ты не веришь в наш футбол?", "Do you not believe in our football?", [], "new"),
    ("fedya", "Я верю только в наличные деньги!", "I believe only in cash money!", [], "new"),
]

WALK = [
    (0, None, "'Fedya, my dear friend!' Viktor approaches his fish chef with suspicious warmth."),
    (1, None, "'Chef, why are you so kind?' Fedya immediately suspects a hidden motive."),
    (2, None, "'I urgently need your help.' Viktor reveals that he has a special request."),
    (3, None, "'No, chef, I am completely broke!' Fedya guesses the request and denies having cash."),
    (4, None, "'Not even a couple of thousand can be found?' Viktor bargains for a smaller loan."),
    (5, None, "'You still owe me five thousand!' Fedya brings up an unpaid past loan."),
    (6, None, "'I will return everything tomorrow morning!' Viktor gives his customary optimistic pledge."),
    (7, None, "'You always promise that, chef.' Fedya remains skeptical after hearing this many times."),
    (8, None, "'But today Spartak will definitely win!' Viktor reveals his secret source of guaranteed wealth."),
    (9, None, "'Spartak is playing against a strong opponent.' Fedya reminds him of the difficult derby."),
    (10, None, "'They have roster problems!' Viktor shares his insider tactical gossip."),
    (11, None, "'Chef, football is pure lottery.' Fedya argues against risking wages on sporting events."),
    (12, None, "'Do you not believe in our football?' Viktor accuses him of lacking patriotic faith."),
    (13, None, "'I believe only in cash money!' Fedya concludes his refusal with practical humor."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A relatable humorous scene showing how difficult it is to collect past debts from an eccentric boss."
)

CLOSING = ("fedya", "Сначала верните старый долг, шеф!")
