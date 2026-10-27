"""Authoring module for Kukhnya s01e13 scene 13."""
from pathlib import Path

ID = "kukhnya-s01e13-scene-13"
TITLE = "Признание перед шефом  (Confession Before the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 13

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
    "chef": "angelina",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Настя",
    "kostya": "Костя",
    "chef": "Шеф",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = Path("sources/kukhnya/s01/e13.ru.dual.srt")
SOURCE_NOTE = "Cues 175-196 in the restaurant kitchen and dining hall."

INTRO = (
    "Feeling guilty over Chef Barinov's damaged car mirror, Kostya tries to take the blame himself to protect Nastya. "
    "However, Nastya rushes forward to confess that she accidentally hit the mirror while riding her bicycle, leading to a surprisingly peaceful resolution. "
    "Let's listen to their confession in Russian."
)

OPENER = (
    "Now let's examine how Kostya and Nastya confess their accident to Barinov line by line."
)

STORY = [
    ("kostya", "Шеф, это я сломал зеркало машины.",
     "Chef, I broke your car mirror.",
     [(175, "Шеф, это я сломал ваше зеркало.")], "Kostya confesses"),

    ("anya", "Шеф, совсем не верьте ему!",
     "Chef, do not believe him at all!",
     [(176, "Нет, не верьте ему.")], "Nastya interrupts"),

    ("anya", "Это я сама сломала зеркало!",
     "I broke your side mirror myself!",
     [(177, "Это я сломала ваше зеркало.")], "Nastya claims responsibility"),

    ("chef", "Вы оба сломали моё зеркало?",
     "Did you both break my mirror together?",
     [], "Barinov questions them"),

    ("anya", "Я ехала на велосипеде и задела.",
     "I was riding a bicycle and grazed it.",
     [(181, "Я ехала на велосипеде, и случайно ваше зеркало сломала.")], "Nastya explains the accident"),

    ("kostya", "Я просто хотел защитить Настю, шеф.",
     "I was simply trying to protect Nastya, chef.",
     [(178, "А он просто хочет меня прикрыть.")], "Kostya explains his lie"),

    ("anya", "Шеф, простите нас обоих, пожалуйста!",
     "Chef, please forgive both of us!",
     [(182, "Шеф, простите меня, пожалуйста.")], "Nastya pleads for mercy"),

    ("chef", "Я два дня ругался с соседкой!",
     "I was fighting with the neighbor for two days!",
     [(184, "А я с ней уже дня два воины.")], "Barinov recalls his pointless argument"),

    ("chef", "Идите работать, вы оба настоящие инвалиды!",
     "Go back to work, you clumsy people!",
     [(183, "Вот вы инвалиды.")], "Barinov forgives them gruffly"),

    ("kostya", "Настя, спасибо, ты поступила очень смело.",
     "Nastya, thank you, you acted very bravely.",
     [(190, "Ты была так мила.")], "Kostya thanks Nastya"),

    ("anya", "И ты меня красиво защитил, Костя.",
     "And you protected me so nicely, Kostya.",
     [(191, "Спасибо.")], "Nastya thanks Kostya"),

    ("anya", "Может, ты сегодня придёшь в гости?",
     "Maybe you will come visit me tonight?",
     [(193, "Слушай, может, сегодня придешь ко мне?")], "Nastya invites Kostya"),

    ("kostya", "С огромным удовольствием приду к тебе!",
     "I will gladly come visit you tonight!",
     [(196, "Сегодня приду не просто так.")], "Kostya accepts"),
]

WALK = [
    (0, None,
     "'Chef, I broke your car mirror.' Kostya bravely confesses to the accident."),
    (1, None,
     "'Chef, do not believe him at all!' Nastya urgently interrupts to tell the truth."),
    (2, None,
     "'I broke your side mirror myself!' She admits her own mistake honestly."),
    (3, None,
     "'Did you both break my mirror together?' Barinov looks at them in disbelief."),
    (4, None,
     "'I was riding a bicycle and grazed it.' Nastya explains how the collision happened."),
    (5, None,
     "'I was simply trying to protect Nastya, chef.' Kostya admits his noble lie to Barinov."),
    (6, None,
     "'Chef, please forgive both of us!' Nastya pleads with genuine remorse."),
    (7, None,
     "'I was fighting with the neighbor for two days!' Barinov throws his hands up in frustration."),
    (8, None,
     "'Go back to work, you clumsy people!' He gruffly dismisses them without punishment."),
    (9, None,
     "'Nastya, thank you, you acted very bravely.' Kostya admires her honesty and courage."),
    (10, None,
     "'And you protected me so nicely, Kostya.' Nastya appreciates his chivalry with gratitude."),
    (11, None,
     "'Maybe you will come visit me tonight?' She shyly invites the bartender over."),
    (12, None,
     "'I will gladly come visit you tonight!' Kostya accepts the invitation with excitement."),
]

TRANSITION = (
    "Now let's listen to the confession before Barinov and the romantic invitation once more."
)

OUTRO = (
    "Relieved of their guilt, Kostya and Nastya arrange their first intimate evening together."
)

CLOSING = ("kostya", "С огромным удовольствием приду к тебе!")
