"""Authoring module for Kukhnya s01e10 scene 08."""
from pathlib import Path

ID = "kukhnya-s01e10-scene-08"
TITLE = "Звонок Нагиеву  (Phone Call to Nagiyev)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 8

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nagiev": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Шеф",
    "nagiev": "Нагиев",
}

SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")
SOURCE_NOTE = "Cues 67-71 over the phone in the chef's office."

INTRO = (
    "In this scene in the restaurant office, Chef Viktor Barinov urgently needs money to place a guaranteed bet on a football derby. "
    "He calls restaurant owner Dmitry Nagiyev, hoping to secure an advance, but Dmitry sees right through him. "
    "Listen to their phone conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this sharp phone exchange."
)

STORY = [
    ("anya", "Дмитрий Владимирович, доброе вам утро!", "Dmitry Vladimirovich, good morning to you!", [(67, "Дмитрий Владимирович, доброе вам утро.")], "verbatim"),
    ("nagiev", "Здорово, Виктор, денег не дам!", "Hey, Viktor, I am not giving you money!", [(68, "Здорово, денег не дам,")], "adapted: added name"),
    ("nagiev", "Я тебе две зарплаты уже выдал.", "I already paid you two paychecks.", [(68, "я тебе две зарплаты уже вперед выдал.")], "adapted: shortened"),
    ("nagiev", "Чего ты хотел?", "What did you want?", [(69, "Чего хотел?")], "adapted: added pronoun"),
    ("anya", "Да я не за деньгами звоню!", "Why, I am not calling for money!", [(70, "Да я не зачем звоню.")], "adapted: clarified target"),
    ("nagiev", "Да? А зачем тогда звонишь?", "Really? Then why are you calling?", [(71, "Да зачем?")], "adapted: expanded question"),
    ("anya", "Сегодня вечером важный футбольный матч.", "Tonight is an important football match.", [], "new"),
    ("nagiev", "Опять твой любимый Спартак играет?", "Is your beloved Spartak playing again?", [], "new"),
    ("anya", "Да, и у меня есть верная информация!", "Yes, and I have reliable insider info!", [], "new"),
    ("nagiev", "Виктор, ставки на спорт опасны.", "Viktor, sports betting is dangerous.", [], "new"),
    ("anya", "Мне нужен небольшой аванс до завтра.", "I need a small advance until tomorrow.", [], "new"),
    ("nagiev", "Я знаю твои авансы, Виктор.", "I know your advances, Viktor.", [], "new"),
    ("nagiev", "Ни копейки ты не получишь!", "You will not get a single kopeck!", [], "new"),
    ("anya", "Дмитрий, ты пожалеешь об этом!", "Dmitry, you will regret this!", [], "new"),
]

WALK = [
    (0, None, "'Dmitry Vladimirovich, good morning to you!' Viktor greets his boss on the phone with polite cheerfulness."),
    (1, None, "'Hey, Viktor, I am not giving you money!' Dmitry immediately shuts down any financial requests."),
    (2, None, "'I already paid you two paychecks.' Dmitry reminds the chef of his previous advance payments."),
    (3, None, "'What did you want?' Dmitry demands to know the real reason behind the phone call."),
    (4, None, "'Why, I am not calling for money!' Viktor pretends that his intention is purely social."),
    (5, None, "'Really? Then why are you calling?' Dmitry questions him with deep skepticism."),
    (6, None, "'Tonight is an important football match.' Viktor tries to steer the topic toward sports."),
    (7, None, "'Is your beloved Spartak playing again?' Dmitry brings up the chef's well-known obsession."),
    (8, None, "'Yes, and I have reliable insider info!' Viktor hints at his guaranteed secret source."),
    (9, None, "'Viktor, sports betting is dangerous.' Dmitry warns his impulsive head chef against gambling."),
    (10, None, "'I need a small advance until tomorrow.' Viktor finally confesses his urgent monetary need."),
    (11, None, "'I know your advances, Viktor.' Dmitry remains completely unmoved by the plea."),
    (12, None, "'You will not get a single kopeck!' Dmitry firmly refuses to finance the gamble."),
    (13, None, "'Dmitry, you will regret this!' Viktor shouts frustratedly before hanging up."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A comedic interaction highlighting Dmitry Nagiyev's stubborn refusal to fund Barinov's gambling habits."
)

CLOSING = ("anya", "Придется искать деньги в другом месте.")
