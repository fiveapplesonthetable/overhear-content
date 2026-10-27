"""Authoring module for Kukhnya s01e11 scene 04."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-04"
TITLE = "Возвращение на кухню  (Return to the Kitchen)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 4

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Макс",
    "chef": "Шеф",
}

SOURCE_NAME = "Кухня s01e11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 58-65 in the restaurant hallway."

INTRO = (
    "In this scene in the hallway, Chef Viktor Barinov spots Max sitting idle after Victoria suspended him. "
    "Furious that someone else is giving orders to his cooks, Viktor fiercely asserts his kitchen authority and sends Max back to work. "
    "Listen to their conversation in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine the vocabulary and phrasing of this energetic backstage encounter."
)

STORY = [
    ("chef", "Макс, ты что здесь прохлаждаешься?", "Max, why are you slacking off here?", [(58, "Ты что это здесь прохлаждаешься?")], "adapted: added name"),
    ("anya", "Что мне еще делать, шеф?", "What else am I to do, chef?", [(59, "Что мне еще делать, шеф?")], "verbatim"),
    ("anya", "Меня сегодня отстранили от работы.", "I was suspended from work today.", [(60, "Меня же сегодня отстранили от работы.")], "adapted: shortened"),
    ("chef", "Кто тебя отстранил? Я?", "Who suspended you? Me?", [(61, "Кто тебя отстранил? Я?")], "verbatim"),
    ("anya", "Виктория Сергеевна сказала сидеть здесь.", "Viktoria Sergeyevna told me to sit here.", [], "new"),
    ("chef", "С каких пор ты её слушаешь?", "Since when do you listen to her?", [(62, "С каких пор ты стал слушать")], "adapted: polite register"),
    ("chef", "На этой кухне главный только я!", "In this kitchen, only I am the boss!", [], "new"),
    ("anya", "Она обещала меня уволить, шеф.", "She promised to fire me, chef.", [], "new"),
    ("chef", "Увольнять поваров могу только я!", "Only I can fire cooks!", [], "new"),
    ("chef", "А ну марш на кухню!", "Now march to the kitchen!", [(63, "марш на кухне")], "adapted: imperative order"),
    ("chef", "Там тебя куча чеков дожидается.", "A pile of orders is waiting for you there.", [(63, "там тебе куча чеков дождается.")], "adapted: corrected grammar"),
    ("anya", "Спасибо, шеф, я бегу!", "Thank you, chef, I am running!", [(64, "Спасибо, шеф.")], "adapted: added action"),
    ("chef", "Стой, куда ты понес сковороду?", "Wait, where are you carrying that pan?", [(65, "Куда понес?")], "adapted: added noun"),
    ("anya", "На рабочее место, шеф!", "To the workstation, chef!", [], "new"),
]

WALK = [
    (0, None, "'Max, why are you slacking off here?' Viktor scolds his idle apprentice with sharp irritation."),
    (1, None, "'What else am I to do, chef?' Max defends his inactivity with a helpless gesture."),
    (2, None, "'I was suspended from work today.' Max explains the disciplinary action taken against him."),
    (3, None, "'Who suspended you? Me?' Viktor bristles at hearing about someone else giving orders."),
    (4, None, "'Viktoria Sergeyevna told me to sit here.' Max names the management authority responsible."),
    (5, None, "'Since when do you listen to her?' Viktor angrily rejects any of her administrative interference."),
    (6, None, "'In this kitchen, only I am the boss!' Viktor asserts his absolute control over the crew."),
    (7, None, "'She promised to fire me, chef.' Max recalls her strict warning about being fired."),
    (8, None, "'Only I can fire cooks!' Viktor insists on his exclusive right to dismiss staff."),
    (9, None, "'Now march to the kitchen!' Viktor barks a direct order to return to duty."),
    (10, None, "'A pile of orders is waiting for you there.' Viktor points out the growing queue of tickets."),
    (11, None, "'Thank you, chef, I am running!' Max expresses his relief at getting back to work."),
    (12, None, "'Wait, where are you carrying that pan?' Viktor stops him with a suspicious glare."),
    (13, None, "'To the workstation, chef!' Max replies eagerly as he hurries toward the stoves."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A lively scene demonstrating Chef Barinov's fiery defiance of restaurant management."
)

CLOSING = ("anya", "Шеф всегда защищает своих поваров!")
