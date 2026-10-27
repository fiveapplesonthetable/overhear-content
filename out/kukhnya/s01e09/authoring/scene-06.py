"""Authoring module for Kukhnya s01e09 scene 06."""
from pathlib import Path

ID = "kukhnya-s01e09-scene-06"
TITLE = "Уроки кондитера  (Pastry Chef Lessons)"
LEVEL = "A1"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 6

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "luis": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Макс",
    "luis": "Луи",
}

SOURCE_NAME = "Кухня s01e09"
SOURCE_FILE = Path("sources/kukhnya/s01/e09.ru.dual.srt")
SOURCE_NOTE = "Cues 160-179 in the restaurant kitchen."

INTRO = (
    "In this scene in the pastry section of Claude Monet, pastry chef Louis gives Max energetic instructions on "
    "preparing an anniversary cake for a bank. While explaining how to whip the cream and melt the white chocolate, "
    "Louis suddenly realizes his favorite knife is missing. Listen to the dialogue in Russian first, and then we will examine each sentence."
)

OPENER = (
    "Now, let us examine each step of this kitchen dialogue between Louis and Max."
)

STORY = [
    ("luis", "Макс, быстрее! Уже пора добавлять яйца.", "Max, faster! It is time to add the eggs.", [(160, "Быстрее. Уже пора добавлять яйца.")], "adapted: added name"),
    ("anya", "Луи, я делаю всё по рецепту.", "Louis, I am doing everything according to the recipe.", [], "new"),
    ("luis", "Обычно я делаю начинку сразу.", "Usually I make the filling right away.", [(161, "Обычно я делаю начинку сразу,")], "verbatim"),
    ("luis", "Мешай равномерно, чтобы без комочков.", "Stir evenly, so there are no lumps.", [(165, "Равномерно, чтобы без комочков.")], "adapted: added verb"),
    ("anya", "Сколько шоколада нужно разогреть?", "How much chocolate needs to be melted?", [(169, "Сколько чего?"), (168, "И разогреть шоколад.")], "adapted: combined"),
    ("luis", "И разогреть шоколад на водяной бане.", "And melt the chocolate in a water bath.", [(168, "И разогреть шоколад.")], "adapted: added detail"),
    ("anya", "Хорошо, белый или темный шоколад?", "All right, white or dark chocolate?", [], "new"),
    ("luis", "Только белый, для логотипа банка!", "Only white, for the bank logo!", [], "new"),
    ("luis", "О, телефон звонит, одну секунду.", "Oh, the phone is ringing, one second.", [(172, "Телефон.")], "adapted: extended"),
    ("luis", "Алло? Нет, сейчас я на кухне.", "Hello? No, right now I am in the kitchen.", [], "new"),
    ("anya", "Луи, я закончил взбивать крем.", "Louis, I finished whipping the cream.", [], "new"),
    ("luis", "О, спасибо, отличная работа!", "Oh, thank you, great job!", [(176, "О, спасибо.")], "adapted: added praise"),
    ("luis", "Постой, а где мой любимый нож?", "Wait, where is my favorite knife?", [(179, "мой нож?")], "adapted: extended question"),
    ("anya", "Я не трогал твой нож, Луи.", "I did not touch your knife, Louis.", [], "new"),
]

WALK = [
    (0, None, "'Max, faster! It is time to add the eggs.' Louis urges his kitchen assistant with impatient energy."),
    (1, None, "'Louis, I am doing everything according to the recipe.' Max defends his careful cooking pace."),
    (2, None, "'Usually I make the filling right away.' Louis describes his standard baking routine."),
    (3, None, "'Stir evenly, so there are no lumps.' Louis explains the proper stirring technique."),
    (4, None, "'How much chocolate needs to be melted?' Max asks for precise measurements."),
    (5, None, "'And melt the chocolate in a water bath.' Louis gives specific instructions on heating."),
    (6, None, "'All right, white or dark chocolate?' Max checks which variety to use for the dessert."),
    (7, None, "'Only white, for the bank logo!' Louis clarifies the required decoration."),
    (8, None, "'Oh, the phone is ringing, one second.' Louis steps away to answer an incoming call."),
    (9, None, "'Hello? No, right now I am in the kitchen.' Louis speaks quickly into his phone."),
    (10, None, "'Louis, I finished whipping the cream.' Max announces the completion of his task."),
    (11, None, "'Oh, thank you, great job!' Louis compliments his assistant with warm praise."),
    (12, None, "'Wait, where is my favorite knife?' Louis looks around in confusion for his tool."),
    (13, None, "'I did not touch your knife, Louis.' Max denies taking the missing kitchen knife."),
]

TRANSITION = (
    "Now, let us listen to the complete scene again to practice your comprehension."
)

OUTRO = (
    "A humorous culinary lesson that ends with a puzzling kitchen mystery."
)

CLOSING = ("luis", "Куда исчез мой нож?")
