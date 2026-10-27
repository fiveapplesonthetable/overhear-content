"""Authoring module for Kukhnya s01e13 scene 15."""
from pathlib import Path

ID = "kukhnya-s01e13-scene-15"
TITLE = "Разговор на складе  (Talk in the Stockroom)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 15

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "max": "anja",
}

LABELS = {
    "narrator": "Narrator",
    "anya": "Вика",
    "max": "Макс",
}

SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = Path("sources/kukhnya/s01/e13.ru.dual.srt")
SOURCE_NOTE = "Cues 200-206 in the restaurant storeroom."

INTRO = (
    "Victoria enters the restaurant storeroom only to find Max sitting comfortably among the crates instead of working. "
    "As Victoria tries to lecture him about maturity and the impropriety of their workplace relationship, Max counters her worries with charming romance. "
    "Let's listen to their flirtatious conversation in Russian."
)

OPENER = (
    "Now let's examine how Victoria and Max balance professional duty and personal feelings line by line."
)

STORY = [
    ("anya", "Макс, почему ты снова прячешься здесь?",
     "Max, why are you hiding here again?",
     [(200, "Виктория Сергеевна не видала?")], "Vika catches Max"),

    ("max", "Я просто ждал тебя здесь.",
     "I was simply waiting for you here.",
     [], "Max smiles"),

    ("anya", "Какой же ты всё-таки несерьёзный ребёнок!",
     "What an unserious child you are!",
     [(201, "Какой же ты все-таки ребенок.")], "Vika scolds him"),

    ("max", "Тогда строго накажи меня за это!",
     "Then punish me strictly for that!",
     [(202, "Тогда накажи меня.")], "Max teases"),

    ("anya", "Макс, перестань шутить, я говорю серьёзно.",
     "Max, stop joking, I am serious.",
     [(203, "я не шучу.")], "Vika tries to be firm"),

    ("anya", "Ты молодой, тебе хочется веселья.",
     "You are young, you want fun.",
     [(204, "Я понимаю, что ты молодой, а тебе хочется веселиться.")], "Vika notes age gap"),

    ("anya", "На работе надо быть взрослым человеком.",
     "At work one must be an adult.",
     [(205, "Но иногда надо быть серьезней.")], "Vika urges maturity"),

    ("max", "Вика, почему ты так переживаешь?",
     "Vika, why are you so worried?",
     [(205, "что ты переживаешь")], "Max questions her fear"),

    ("max", "Разница в возрасте совсем не важна.",
     "The age difference is not important.",
     [], "Max dismisses concerns"),

    ("anya", "Мне кажется, мы совершаем ошибку.",
     "It seems we are making a mistake.",
     [], "Vika expresses hesitation"),

    ("max", "Рядом со мной ты забудешь тревоги.",
     "Beside me you will forget all worries.",
     [], "Max comforts her"),

    ("anya", "Макс, ты просто неисправимый романтик.",
     "Max, you are an incorrigible romantic.",
     [(220, "Макс,")], "Vika smiles"),

    ("max", "Потому что я очень люблю тебя, Вика.",
     "Because I love you very much, Vika.",
     [], "Max confesses love"),
]

WALK = [
    (0, None,
     "'Max, why are you hiding here again?' Victoria discovers him lounging in the stockroom."),
    (1, None,
     "'I was simply waiting for you here.' Max responds with a disarming smile."),
    (2, None,
     "'What an unserious child you are!' Victoria sighs at his playful attitude."),
    (3, None,
     "'Then punish me strictly for that!' Max turns her reprimand into a flirtatious dare."),
    (4, None,
     "'Max, stop joking, I am serious.' Victoria attempts to maintain professionalism."),
    (5, None,
     "'You are young, you want fun.' She reminds him of their generational divide."),
    (6, None,
     "'At work one must be an adult.' Victoria insists on responsible workplace conduct."),
    (7, None,
     "'Vika, why are you so worried?' Max asks why she lets small worries trouble her."),
    (8, None,
     "'The age difference is not important.' He dismisses her concerns about age barriers."),
    (9, None,
     "'It seems we are making a mistake.' Victoria voices her lingering doubts to him."),
    (10, None,
     "'Beside me you will forget all worries.' Max reassures her with tender affection."),
    (11, None,
     "'Max, you are an incorrigible romantic.' Victoria melts with a smile despite her hesitation."),
    (12, None,
     "'Because I love you very much, Vika.' Max expresses his sincere feelings directly."),
]

TRANSITION = (
    "Now let's listen to the flirtatious dialogue between Victoria and Max once more."
)

OUTRO = (
    "Unable to resist Max's charm, Victoria lets her professional guard down in the quiet storeroom."
)

CLOSING = ("max", "Потому что я очень люблю тебя, Вика.")
