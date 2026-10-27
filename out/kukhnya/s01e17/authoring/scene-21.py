# Authoring module for kukhnya s01e17 scene 21 (cues 320-325).
# Build: python3 tools/compose.py out/kukhnya/s01e17/authoring/scene-21.py --out out/kukhnya/s01e17/scene-21.json

ID = "kukhnya-s01e17-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 17
SCENE = 21
TITLE = "Конец конфликта  (End of the Conflict)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja", "chef": "angelina"}
LABELS = {"anya": "Макс", "vika": "Вика", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.17"
SOURCE_FILE = "sources/kukhnya/s01/e17.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 320-325. Victoria and Chef Viktor apologize to Max for ruining his celebration, "
    "bringing peace to the restaurant."
)

INTRO = (
    "Gathered in the Claude Monet dining room, Victoria and the restaurant staff approach Max "
    "to apologize for ruining his birthday celebration. Chef Viktor steps in to ensure peace is restored, "
    "bringing the long day of intense conflicts to an end. Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this reconciliation line by line."

STORY = [
    ("vika", "Максим, прости нас, пожалуйста.", "Maxim, please forgive us.",
     [(321, "Максим, прости нас, пожалуйста, что испортили тебе праздник.")], "adapted"),
    ("vika", "Мы испортили тебе отличный праздник.", "We ruined a great holiday for you.",
     [(321, "что испортили тебе праздник")], "adapted"),
    ("anya", "Я не сержусь на вас.", "I am not angry at you.",
     [], "new"),
    ("vika", "Прости их, пожалуйста, от души.", "Please forgive them from the heart.",
     [(322, "Прости их, пожалуйста.")], "adapted"),
    ("chef", "Ну и меня тоже прости.", "Well and forgive me too.",
     [(323, "Ну и меня.")], "adapted"),
    ("chef", "Так, всё? Конфликт закончился?", "So, is that all? The conflict is over?",
     [(323, "Так все?"), (324, "Конфликт исчерпан?")], "adapted"),
    ("anya", "Да, шеф, конфликт закончился.", "Yes, chef, the conflict is over.",
     [(324, "Конфликт исчерпан")], "adapted"),
    ("chef", "Но только пока кто-то снова не ошибётся.", "But only until someone makes a mistake again.",
     [(324, "Временно, пока кто-нибудь снова не накосячит.")], "adapted"),
    ("vika", "Мы все хотим мира на кухне.", "We all want peace in the kitchen.",
     [], "new"),
    ("chef", "Мир на кухне — это главное.", "Peace in the kitchen is key.",
     [], "new"),
    ("anya", "Спасибо всем за добрые слова.", "Thank you all for the kind words.",
     [], "new"),
    ("vika", "Теперь мы можем спокойно работать.", "Now we can work calmly.",
     [], "new"),
    ("anya", "Я очень рад, что мы помирились.", "I am very glad that we reconciled.",
     [], "new"),
]

WALK = [
    (0, None,
     "'Maxim, please forgive us.' -- Victoria asks for forgiveness on behalf of the team."),
    (1, None,
     "'We ruined a great holiday for you.' -- She expresses regret for spoiling the special day."),
    (2, None,
     "'I am not angry at you.' -- Max shows that he holds no grudge against them."),
    (3, None,
     "'Please forgive them from the heart.' -- Victoria encourages him to let go of any pain."),
    (4, None,
     "'Well and forgive me too.' -- Chef Viktor joins the apology with a gruff smile."),
    (5, None,
     "'So, is that all? The conflict is over?' -- The chef wants to make sure that peace is restored."),
    (6, None,
     "'Yes, chef, the conflict is over.' -- Max confirms that there is no bad blood."),
    (7, None,
     "'But only until someone makes a mistake again.' -- The chef realistically predicts future trouble."),
    (8, None,
     "'We all want peace in the kitchen.' -- Victoria highlights the shared desire for harmony."),
    (9, None,
     "'Peace in the kitchen is key.' -- Viktor emphasizes the importance of a calm workspace."),
    (10, None,
     "'Thank you all for the kind words.' -- Max appreciates the sincere support from the team."),
    (11, None,
     "'Now we can work calmly.' -- Victoria looks forward to a productive shift."),
    (12, None,
     "'I am very glad that we reconciled.' -- Max celebrates the warm resolution of the fight."),
]

TRANSITION = "Now let's listen to the dining room conversation again without interruption."
OUTRO = (
    "Relieved that the tension has dissipated, Max accepts their apologies as Victoria "
    "and Chef Viktor return to their work in the restaurant."
)
CLOSING = ("anya", "Я очень рад, что мы помирились.")
