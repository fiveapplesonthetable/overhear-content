"""Authoring module for Kukhnya s01e12 scene 06."""
from pathlib import Path

ID = "kukhnya-s01e12-scene-06"
TITLE = "Визит к конкурентам  (A Visit to Competitors)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 6

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "elena": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Шеф",
    "elena": "Елена",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = Path("sources/kukhnya/s01/e12.ru.dual.srt")
SOURCE_NOTE = "Cues 59-63 outside the rival restaurant Arcobaleno."

INTRO = (
    "Curious about the new Italian competition opening across the street, Chef Viktor Barinov walks over to inspect Arcobaleno. "
    "There he encounters rival chef Elena supervising the delivery of large decorative palm trees, leading to a sharp verbal duel between the chefs. "
    "Let's listen to their humorous encounter in Russian."
)

OPENER = (
    "Now let's examine how Barinov and Elena trade witty barbs outside the rival restaurant line by line."
)

STORY = [
    ("elena", "Осторожно заносите эти пальмы в ресторан!",
     "Carefully bring these palms into the restaurant!",
     [(59, "И ты заноси.")], "Elena instructs movers"),

    ("elena", "Ой, Виктор Петрович, захотели вкусно поесть?",
     "Oh, Viktor Petrovich, did you want to eat well?",
     [(59, "Ой, Виктор Петрович, захотели вкусно поесть.")], "Elena teases Barinov"),

    ("elena", "Мы откроемся только через шесть дней!",
     "We open only in six days!",
     [(60, "Извините, откроемся только через шесть дней.")], "Elena states opening date"),

    ("anya", "Я просто гулял по этой улице.",
     "I was simply taking a walk along this street.",
     [], "Barinov feigns disinterest"),

    ("elena", "Решили лично проверить своих главных конкурентов?",
     "Decided to personally check your main competitors?",
     [], "Elena challenges him"),

    ("anya", "Я совсем не боюсь вашего ресторана.",
     "I am not at all afraid of your restaurant.",
     [], "Barinov denies fear"),

    ("elena", "Тогда почему вы смотрите на нас?",
     "Then why are you looking at us?",
     [], "Elena probes further"),

    ("anya", "Зачем вам в зале настоящие пальмы?",
     "Why do you need real palm trees in the dining room?",
     [(61, "Просто подумал, что если у вас пальмы")], "Barinov questions decor"),

    ("elena", "Это создаёт уютную итальянскую атмосферу.",
     "This creates a cozy Italian atmosphere.",
     [], "Elena explains concept"),

    ("anya", "Пальмы не помогут готовить вкусную еду!",
     "Palm trees will not help cook tasty food!",
     [], "Barinov criticizes decor"),

    ("elena", "У нас будет самая вкусная кухня!",
     "We will have the tastiest cuisine!",
     [], "Elena defends restaurant"),

    ("elena", "Пропустите рабочих, заносите деревья внутрь!",
     "Let the workers through, bring the trees inside!",
     [(62, "Заносим, заносим.")], "Elena urges workers"),

    ("anya", "Дослушивать надо людей, когда они говорят!",
     "One must listen to people when they speak!",
     [(63, "Дослушивать надо.")], "Barinov complains of being ignored"),
]

WALK = [
    (0, None,
     "'Carefully bring these palms into the restaurant!' Elena instructs the delivery movers."),
    (1, None,
     "'Oh, Viktor Petrovich, did you want to eat well?' Elena teases Barinov as he lingers outside."),
    (2, None,
     "'We open only in six days!' She reminds him that business has not begun yet."),
    (3, None,
     "'I was simply taking a walk along this street.' Barinov feigns casual disinterest to her."),
    (4, None,
     "'Decided to personally check your main competitors?' Elena easily sees through his excuse with a grin."),
    (5, None,
     "'I am not at all afraid of your restaurant.' Barinov stubbornly denies feeling threatened in any way."),
    (6, None,
     "'Then why are you looking at us?' She playfully challenges his lingering presence."),
    (7, None,
     "'Why do you need real palm trees in the dining room?' Barinov scoffs at the lavish interior decor."),
    (8, None,
     "'This creates a cozy Italian atmosphere.' Elena defends the design vision of her establishment."),
    (9, None,
     "'Palm trees will not help cook tasty food!' Barinov argues that true cooking requires culinary skill."),
    (10, None,
     "'We will have the tastiest cuisine!' Elena confidently counters his skepticism with pride."),
    (11, None,
     "'Let the workers through, bring the trees inside!' Elena directs the movers right past Barinov."),
    (12, None,
     "'One must listen to people when they speak!' Barinov grumbles as he is ignored."),
]

TRANSITION = (
    "Now let's listen to the amusing encounter between rival head chefs once more."
)

OUTRO = (
    "Dismissed by Elena and the busy movers, Barinov heads back across the street to protect his own kitchen."
)

CLOSING = ("anya", "Дослушивать надо людей, когда они говорят!")
