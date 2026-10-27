"""s01e04 scene 19: Обед для персонала (Staff Lunch)."""

ID = "kukhnya-s01e04-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 19
TITLE = "Обед для персонала  (Staff Lunch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "senya": "anja",
}
LABELS = {
    "anya": "Макс",
    "senya": "Сеня",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "In the Claude Monet kitchen, the staff are hungry and waiting for their staff lunch. "
    "Max has been assigned to prepare the meal, and line cook Senya asks impatiently when it will be ready. "
    "Max proudly promises a gourmet purée soup far superior to the plain slop they usually eat. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("senya", "Макс, мы сегодня обедать будем?",
     "Max, are we going to have lunch today?",
     [(264, "Мы сегодня есть")], "impatient question"),
    ("anya", "Конечно, всё уже почти готово!",
     "Of course, everything is already almost ready!",
     [(265, "Все готово")], "reassuring crew"),
    ("senya", "Мы все очень хотим есть.",
     "We all really want to eat.",
     [(264, "Вообще будем")], "stating hunger"),
    ("anya", "Подождите ещё пару минут.",
     "Wait a couple more minutes.",
     [(265, "Будете, будете")], "asking patience"),
    ("senya", "Что ты нам приготовил сегодня?",
     "What did you prepare for us today?",
     [], "curious inquiry"),
    ("anya", "Я сварил особенный суп-пюре.",
     "I cooked a special purée soup.",
     [(267, "Суппюре")], "announcing dish"),
    ("senya", "Обычный суп был бы лучше.",
     "A regular soup would be better.",
     [], "skeptical reaction"),
    ("anya", "Вы все пальчики оближете!",
     "You will all lick your fingers!",
     [(266, "пальчики оближите")], "confident boast"),
    ("senya", "Надеюсь, это можно есть.",
     "I hope this is edible.",
     [], "playful doubt"),
    ("anya", "Вы такого никогда не пробовали.",
     "You have never tasted such a thing.",
     [(267, "никогда не пробовали")], "promising novelty"),
    ("senya", "Главное, чтобы было вкусно.",
     "The main thing is that it is tasty.",
     [], "practical requirement"),
    ("anya", "Это не то обычное месиво.",
     "This is not that usual slop.",
     [(268, "Не то месиво")], "mocking standard food"),
    ("senya", "Ладно, неси скорее на стол!",
     "Alright, bring it quickly to the table!",
     [], "urging delivery"),
    ("anya", "Сейчас я вас всех удивлю!",
     "Now I will surprise you all!",
     [], "eager finale"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Макс, мы сегодня обедать будем?",
     "'Max, are we going to have lunch today?' The line cook impatiently asks when food will be served."),
    (1, "Конечно, всё уже почти готово!",
     "'Of course, everything is already almost ready!' Max reassures the hungry crew in the kitchen."),
    (2, "Мы все очень хотим есть.",
     "'We all really want to eat.' The kitchen staff are exhausted and waiting for lunch."),
    (3, "Подождите ещё пару минут.",
     "'Wait a couple more minutes.' A polite request to give the cook just a moment."),
    (4, "Что ты нам приготовил сегодня?",
     "'What did you prepare for us today?' A curious question about the daily staff meal menu."),
    (5, "Я сварил особенный суп-пюре.",
     "'I cooked a special purée soup.' Max proudly announces his upscale culinary experiment."),
    (6, "Обычный суп был бы лучше.",
     "'A regular soup would be better.' The veteran cook expresses doubt about fancy experiments."),
    (7, "Вы все пальчики оближете!",
     "'You will all lick your fingers!' A classic Russian idiom meaning the food is extremely tasty."),
    (8, "Надеюсь, это можно есть.",
     "'I hope this is edible.' A teasing remark about the rookie cook's culinary skills."),
    (9, "Вы такого никогда не пробовали.",
     "'You have never tasted such a thing.' Max promises a unique and memorable flavor experience."),
    (10, "Главное, чтобы было вкусно.",
     "'The main thing is that it is tasty.' A practical reminder that taste matters more than presentation."),
    (11, "Это не то обычное месиво.",
     "'This is not that usual slop.' Max contrasts his refined creation with everyday cafeteria food."),
    (12, "Ладно, неси скорее на стол!",
     "'Alright, bring it quickly to the table!' An invitation to finally serve the cooked meal."),
    (13, "Сейчас я вас всех удивлю!",
     "'Now I will surprise you all!' An eager promise to impress the entire restaurant team."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Max promises an unforgettable culinary experience for the restaurant staff lunch. "
    "Next time, we will see how the team reacts when the colorful dish arrives at the table. Until then!"
)

CLOSING = ("anya", "Мы все хотим вкусно пообедать.")
