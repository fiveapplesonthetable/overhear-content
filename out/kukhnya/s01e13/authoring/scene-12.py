ID = "kukhnya-s01e13-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 12
TITLE = "Признание  (The Confession)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "anja", "barinov": "angelina"}
LABELS = {"anya": "Костя", "nastya": "Настя", "barinov": "Виктор Петрович"}
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"
SOURCE_NOTE = "Cues 164-179. Kostya offers to take the blame for the broken mirror, but Nastya confesses."

INTRO = "Inside the kitchen, Nastya is very worried about breaking the Chef's car mirror earlier. Kostya wants their date to happen, so he offers a brave sacrifice. Let's hear them in Russian."

STORY = [
    ("nastya", "Шеф опять с ней ругается.", "The boss is arguing with her again.", [(164, "Шеф опять с ней рукается.")], "typo 'рукается' corrected"),
    ("anya", "Да ладно, Настя, всё образуется.", "Come on, Nastya, everything will work out.", [(165, "Да ладно, Нась, все образуется.")], "Нась -> Настя"),
    ("nastya", "Сегодня у нас тоже ничего не получится?", "Things won't work out for us today either?", [(166, "сегодня у нас тоже ничего не получится?")], ""),
    ("anya", "Нет, Настя, ну ты просто обещала.", "No, Nastya, you simply promised.", [(168, "Да нет, Нась, ну ты просто обещала.")], "Да нет -> Нет, Нась -> Настя"),
    ("anya", "Хочешь, я пойду к шефу?", "Do you want me to go to the boss?", [(169, "хочешь, я пойду к шефу")], ""),
    ("anya", "Я скажу, что это я сломал зеркало.", "I will say that I broke the mirror.", [(169, "и скажу, что это я сломал его зеркало?")], "его -> the"),
    ("nastya", "Не надо, он тебя уволит.", "Do not do it, he will fire you.", [(170, "Не надо, он тебя уволит.")], ""),
    ("anya", "Я сказал, значит, я пойду.", "I said it, which means I will go.", [(172, "Я сказал, значит, я пойду.")], ""),
    ("nastya", "Костик, подожди, не ходи.", "Kostik, wait, do not go.", [(173, "Костик, подожди, не ходи.")], "removed repeated Костик"),
    ("anya", "Шеф, это я сломал ваше зеркало.", "Boss, it was me who broke your mirror.", [(175, "Шеф, это я сломал ваше зеркало.")], ""),
    ("nastya", "Нет, не верьте ему.", "No, do not believe him.", [(176, "Нет, не верьте ему.")], ""),
    ("nastya", "Это я сломала ваше зеркало.", "I broke your mirror.", [(177, "Это я сломала ваше зеркало.")], ""),
    ("nastya", "Он просто хочет меня прикрыть.", "He just wants to cover for me.", [(178, "А он просто хочет меня прикрыть.")], "removed А")
]

OPENER = "Let's review Kostya's brave attempt."

WALK = [
    (0, None, "'The boss is arguing with her again.' -- Nastya looks out the window in absolute terror."),
    (1, None, "'Come on, Nastya, everything will work out.' -- The bartender tries to calm his panicked girlfriend."),
    (2, None, "'Things won't work out for us today either?' -- She assumes their romantic evening is totally ruined."),
    (3, None, "'No, Nastya, you simply promised.' -- Kostya refuses to accept another cancelled dinner date."),
    (4, None, "'Do you want me to go to the boss?' -- He suggests a very dangerous rescue plan."),
    (5, None, "'I will say that I broke the mirror.' -- He offers to take the terrible blame himself."),
    (6, None, "'Do not do it, he will fire you.' -- Nastya begs him to protect his own job."),
    (7, None, "'I said it, which means I will go.' -- The determined bartender ignores her desperate warnings."),
    (8, None, "'Kostik, wait, do not go.' -- She desperately tries to stop him from confessing."),
    (9, None, "'Boss, it was me who broke your mirror.' -- He boldly delivers the fake confession to Barinov."),
    (10, None, "'No, do not believe him.' -- Nastya suddenly runs up to interrupt his lie."),
    (11, None, "'I broke your mirror.' -- She finally admits her terrible accident to the Chef."),
    (12, None, "'He just wants to cover for me.' -- She explains why her boyfriend was lying previously.")
]

TRANSITION = "Now let's hear the romantic sacrifice again."
OUTRO = "Kostya was ready to lose his job to save Nastya, but she bravely confessed the truth. Let's see what happens next!"
CLOSING = ("anya", "Я сказал, значит, я пойду.")
