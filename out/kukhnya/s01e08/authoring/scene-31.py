"""Scene 31 — The Beginning of Love (s01e08, 00:21:27–00:21:35)."""

ID = "kukhnya-s01e08-scene-31"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 31
TITLE = "Начало отношений  (The Beginning of Love)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 359-361. Talking warmly at the bar after the shift, Nastya and Kostya claim "
    "they are only close friends, completely unaware that romantic feelings have already begun."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}

LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
}

INTRO = (
    "As the hectic shift at Claude Monet winds down, waitress Nastya joins bartender Kostya at the counter. "
    "While they assure each other that their connection is strictly platonic friendship, "
    "their warm glances reveal that a genuine romance has already quietly sparked between them. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Костя, этот сумасшедший рабочий день наконец закончился.",
     "Kostya, this crazy workday has finally ended.",
     [], "Nastya sighs at bar"),

    ("kostya", "Да, Настя, на кухне творилось настоящее безумие.",
     "Yes, Nastya, real madness was happening in the kitchen.",
     [], "Kostya agrees"),

    ("anya", "Зато мы отлично поддерживали друг друга сегодня.",
     "On the other hand, we supported each other great today.",
     [], "Nastya praises mutual support"),

    ("kostya", "С тобой всегда легко и очень приятно работать.",
     "With you it is always easy and very pleasant to work.",
     [], "Kostya compliments Nastya"),

    ("anya", "Мы с тобой просто замечательные верные друзья.",
     "You and I are simply wonderful loyal friends.",
     [], "Nastya frames as friendship"),

    ("kostya", "Конечно, между нами только крепкая искренняя дружба.",
     "Of course, between us there is only strong sincere friendship.",
     [], "Kostya agrees on friendship"),

    ("anya", "Некоторые уверены, что ничего не может быть.",
     "Some are sure that nothing can happen.",
     [(359, "Другие..."), (360, "в их отношениях никогда и ничего не может быть")], "Quoting voiceover"),

    ("anya", "Они не понимают, что всё уже началось.",
     "They do not understand that everything has already begun.",
     [(361, "даже не понимая, что все уже началось.")], "Romantic realization"),

    ("kostya", "Ты говоришь про нас или про шефа?",
     "Are you talking about us or about the chef?",
     [], "Kostya wonders"),

    ("anya", "Я просто размышляю о жизни и чувствах.",
     "I am simply reflecting on life and feelings.",
     [], "Nastya reflects"),

    ("kostya", "Тогда давай вместе выпьем вкусного чаю.",
     "Then let us drink some delicious tea together.",
     [], "Kostya offers tea"),

    ("anya", "С большим удовольствием посижу здесь с тобой.",
     "With great pleasure I will sit here with you.",
     [], "Nastya accepts"),

    ("kostya", "Я безумно рад нашей неожиданной тёплой встрече!",
     "I am insanely glad for our unexpected warm meeting!",
     [], "Kostya smiles warmly"),
]

OPENER = "Now let's examine Nastya and Kostya's tender conversation line by line."

WALK = [
    (0, None,
     "'Kostya, this crazy workday has finally ended.' Nastya leans against the bar counter with a sigh of relief."),
    (1, None,
     "'Yes, Nastya, real madness was happening in the kitchen.' The bartender agrees after surviving the evening chaos."),
    (2, None,
     "'On the other hand, we supported each other great today.' She appreciates their teamwork amid the stress."),
    (3, None,
     "'With you it is always easy and very pleasant to work.' Kostya expresses his genuine appreciation for her presence."),
    (4, None,
     "'You and I are simply wonderful loyal friends.' Nastya firmly establishes their relationship as strictly platonic."),
    (5, None,
     "'Of course, between us there is only strong sincere friendship.' Kostya nods in agreement, concealing his deeper feelings."),
    (6, None,
     "'Some are sure that nothing can happen.' Nastya echoes Max's voiceover about denial in romance."),
    (7, None,
     "'They do not understand that everything has already begun.' She smiles softly, hinting at an unspoken romantic spark."),
    (8, None,
     "'Are you talking about us or about the chef?' Kostya feels a sudden rush of hope and curiosity."),
    (9, None,
     "'I am simply reflecting on life and feelings.' The waitress plays coy with an enigmatic smile."),
    (10, None,
     "'Then let us drink some delicious tea together.' Kostya hospitably offers to pour her a hot beverage."),
    (11, None,
     "'With great pleasure I will sit here with you.' Nastya gladly accepts the invitation to stay by his side."),
    (12, None,
     "'I am insanely glad for our unexpected warm meeting!' Kostya smiles warmly as they share a private moment."),
]

TRANSITION = "Now let's listen to Nastya and Kostya once more without interruption."

OUTRO = (
    "Believing they are merely close friends, Nastya and Kostya fail to see that love is already blossoming."
)

CLOSING = ("kostya", "Я безумно рад нашей неожиданной тёплой встрече!")
