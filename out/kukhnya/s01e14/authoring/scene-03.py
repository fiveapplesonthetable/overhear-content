ID = "kukhnya-s01e14-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 3
TITLE = "Серьёзный парень  (A Serious Guy)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Элеонора", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues 7-14."

INTRO = "Vika's mother Eleonora visits the restaurant to criticize Vika's relationship with Max. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("vika", "Мам, зачем ты пришла сюда сегодня?",
     "Mom, why did you come here today?",
     [], "new"),
    ("anya", "Зачем тебе этот странный тинейджер?",
     "What do you want with that strange teenager?",
     [(7, 'Зачем тебе этот тинейджер?')], "adapted"),
    ("vika", "Макс серьёзный парень и хороший повар.",
     "Max is a serious guy and a good cook.",
     [(11, 'Макс серьёзный парень.')], "adapted"),
    ("anya", "Почему ты вечно впадаешь в крайности?",
     "Why do you always go to extremes?",
     [(9, 'Вика, ну почему ты вечно впадаешь в какие-то крайности?')], "adapted"),
    ("vika", "Это моя жизнь, и я сама решаю.",
     "This is my life, and I decide myself.",
     [], "new"),
    ("anya", "То женатики, то дети, сразу дети.",
     "First married men, then kids, kids right away.",
     [(10, 'То женатики, то дети. В общем, сразу дети.')], "adapted"),
    ("vika", "Хватит критиковать меня каждый день!",
     "Stop criticizing me every single day!",
     [], "new"),
    ("anya", "Скажи, а ты записала парня в школу?",
     "Tell me, did you enroll the guy in school?",
     [(13, 'Скажи, а ты успела записать серьёзного парня в школу?')], "adapted"),
    ("vika", "Я не хочу это обсуждать сейчас.",
     "I do not want to discuss this now.",
     [], "new"),
    ("anya", "А то я могла бы вам помочь.",
     "Otherwise I could have helped you.",
     [(14, 'А то я могу бы хлопотать.')], "adapted"),
    ("vika", "Мама, пожалуйста, просто уходи отсюда.",
     "Mom, please, just leave from here.",
     [], "new"),
    ("anya", "Ладно, я оставлю вас в покое пока.",
     "Alright, I will leave you in peace for now.",
     [], "new"),
]

OPENER = "Let's analyze this tense mother-daughter dialogue."

WALK = [
    (0, None,
     "'Mom, why did you come here today?' -- Vika questions her mother's sudden visit."),
    (1, None,
     "'What do you want with that strange teenager?' -- Eleonora asks her about her young boyfriend."),
    (2, None,
     "'Max is a serious guy and a good cook.' -- Vika defends his character to her."),
    (3, None,
     "'Why do you always go to extremes?' -- The mother complains about her daughter's choices."),
    (4, None,
     "'This is my life, and I decide myself.' -- The manager tells her to stop interfering."),
    (5, None,
     "'First married men, then kids, kids right away.' -- Eleonora lists her previous romantic mistakes."),
    (6, None,
     "'Stop criticizing me every single day!' -- Vika demands an end to her harsh judgment."),
    (7, None,
     "'Tell me, did you enroll the guy in school?' -- Her mother makes a sarcastic joke at him."),
    (8, None,
     "'I do not want to discuss this now.' -- Vika refuses to answer her mocking question."),
    (9, None,
     "'Otherwise I could have helped you.' -- Eleonora sarcastically offers her assistance to them."),
    (10, None,
     "'Mom, please, just leave from here.' -- She asks her mother to exit the restaurant."),
    (11, None,
     "'Alright, I will leave you in peace for now.' -- The mother agrees to back off from her."),
]

TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Eleonora leaves, but her words leave Vika feeling frustrated."
CLOSING = ("anya", "Ладно, я оставлю вас в покое пока.")
