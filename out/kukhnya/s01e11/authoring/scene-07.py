"""Authoring module for Kukhnya s01e11 scene 07."""
from pathlib import Path

ID = "kukhnya-s01e11-scene-07"
TITLE = "Отказ от салата  (Salad Rejection)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 7

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "max": "angelina",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Вика",
    "chef": "Шеф",
    "max": "Макс",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")
SOURCE_NOTE = "Cues 78-87 in the kitchen and dining entrance."

INTRO = (
    "In the busy restaurant kitchen, Victoria rushes in to confront Chef Barinov after a guest rejects Max's salad. "
    "Fearing that the dissatisfied diner might be the undercover food critic, Barinov orders Max to redo the dish personally. "
    "Let's listen to their tense kitchen conversation in Russian."
)

OPENER = (
    "Now let's examine how Victoria and Chef Barinov handle the salad complaint line by line."
)

STORY = [
    ("anya", "Шеф, что гостья сказала про салат?",
     "Chef, what did the guest say about the salad?",
     [(78, "Что она тебе сказала?")], "Vika questions the chef"),

    ("chef", "Она сказала, что у салата странный вкус.",
     "She said the salad had a strange taste.",
     [(79, "Она сказала, что ей салат не понравился, что у него какой-то вкус странный.")], "Chef explains the complaint"),

    ("max", "Шеф, я делал всё строго по рецепту!",
     "Chef, I made everything strictly by the recipe!",
     [(80, "Я все делал по технологической карте.")], "Max defends his cooking"),

    ("anya", "Я предупреждала, что нельзя его допускать!",
     "I warned you that he must not be allowed!",
     [(81, "Я же тебе говорила, что не надо его допускать.")], "Vika blames Barinov"),

    ("anya", "Ты теперь сам во всём убедился?",
     "Are you convinced of everything yourself now?",
     [(82, "Ты убедился?")], "Vika challenges Barinov"),

    ("chef", "Вика, иди скажи, что мы всё исправим.",
     "Vika, go say that we will fix everything.",
     [(83, "Так, иди скажи, что мы сейчас все исправим.")], "Barinov instructs Victoria"),

    ("anya", "Надеюсь, эта гостья не напишет жалобу.",
     "I hope this guest will not write a complaint.",
     [], "Vika worries about a bad review"),

    ("chef", "Макс, срочно переделай это блюдо сам!",
     "Max, urgently remake this dish yourself!",
     [(85, "Пожалуйста, срочно все переделай.")], "Barinov orders Max"),

    ("max", "Шеф, я приготовлю самый свежий салат.",
     "Chef, I will prepare the freshest salad.",
     [], "Max promises perfection"),

    ("chef", "Ты понимаешь, что ситуация очень серьёзная?",
     "Do you understand that the situation is very serious?",
     [(86, "Ты же понимаешь, что это очень серьезно.")], "Barinov stresses the gravity"),

    ("max", "Я не подведу наш ресторан, шеф!",
     "I will not let our restaurant down, chef!",
     [], "Max reassures his boss"),

    ("chef", "Тогда работай быстрее и не болтай лишнего!",
     "Then work faster and do not talk too much!",
     [], "Barinov demands silence and speed"),

    ("anya", "А я встречу нового гостя в зале.",
     "And I will meet a new guest in the dining room.",
     [], "Vika returns to the front of house"),
]

WALK = [
    (0, None,
     "'Chef, what did the guest say about the salad?' Victoria asks with urgent concern."),
    (1, None,
     "'She said the salad had a strange taste.' Barinov relays the customer's exact words."),
    (2, None,
     "'Chef, I made everything strictly by the recipe!' Max defends his culinary precision with confidence."),
    (3, None,
     "'I warned you that he must not be allowed!' Victoria reminds the chef of her earlier caution."),
    (4, None,
     "'Are you convinced of everything yourself now?' She demands an honest admission from Barinov."),
    (5, None,
     "'Vika, go say that we will fix everything.' Barinov sends her back to calm the customer."),
    (6, None,
     "'I hope this guest will not write a complaint.' Victoria worries about a damaging review."),
    (7, None,
     "'Max, urgently remake this dish yourself!' Barinov gives a strict command to his junior cook."),
    (8, None,
     "'Chef, I will prepare the freshest salad.' Max promises to redeem himself quickly."),
    (9, None,
     "'Do you understand that the situation is very serious?' Barinov emphasizes the high stakes."),
    (10, None,
     "'I will not let our restaurant down, chef!' Max declares his loyalty to the kitchen."),
    (11, None,
     "'Then work faster and do not talk too much!' Barinov orders him to focus entirely on cooking."),
    (12, None,
     "'And I will meet a new guest in the dining room.' Victoria returns to the front of house."),
]

TRANSITION = (
    "Now let's listen to the kitchen discussion and the urgent cooking order once more."
)

OUTRO = (
    "With Victoria calming the guest and Max redoing the salad, the kitchen braces for the reviewer's verdict."
)

CLOSING = ("anya", "А я встречу нового гостя в зале.")
