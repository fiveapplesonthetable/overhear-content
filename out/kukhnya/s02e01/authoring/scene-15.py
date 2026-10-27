# Authoring module for kukhnya s02e01 scene 15 (cues 195-215).
# Build: python3 tools/compose.py out/kukhnya/s02e01/authoring/scene-15.py --out out/kukhnya/s02e01/scene-15.json

ID = "kukhnya-s02e01-scene-15"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 1
SCENE = 15
TITLE = "Безумный план  (A Crazy Plan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S2.01"
SOURCE_FILE = "sources/kukhnya/s02/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 195-215. Inspired by Kostya's story about his dog Ralph, Max stages a fake stunt in the storage room "
    "and explains to a startled Kostya how the dramatic trick will make Vika forgive him."
)

INTRO = (
    "In the restaurant storage room, Max rigs up a dramatic stunt using a hidden harness to scare Vika into forgiving him. "
    "After nearly giving Kostya a heart attack, Max explains how his theatrical plan will work. "
    "Let's listen to their conversation in Russian first."
)

OPENER = "Now let's examine this conversation line by line."

STORY = [
    ("kostya", "Макс, что ты тут сейчас делаешь?",
     "Max, what are you doing here right now?",
     [(195, "Макс")], "adapted"),
    ("kostya", "Я ведь реально очень сильно испугался!",
     "After all, I really got very scared!",
     [(198, "Я реально подумал")], "adapted"),
    ("anya", "Ну, именно на это был расчёт.",
     "Well, that was the exact calculation.",
     [(199, "на это был расчет")], "adapted"),
    ("anya", "Костя, дай мне эти ящики, пожалуйста.",
     "Kostya, give me these boxes, please.",
     [(200, "Давай ящики")], "adapted"),
    ("kostya", "Слушай, а как ты это сделал?",
     "Listen, how did you do that?",
     [(202, "А как ты это сделал")], "adapted"),
    ("anya", "Смотри внимательно, я сейчас тебе покажу.",
     "Watch closely, I will show you right now.",
     [(203, "Сейчас покажу")], "adapted"),
    ("kostya", "Да, это выглядит просто очень круто.",
     "Yes, that looks simply very cool.",
     [(204, "это круто")], "adapted"),
    ("anya", "Помнишь, ты рассказывал мне про собаку?",
     "Do you remember telling me about the dog?",
     [(205, "про Ральфа рассказывал")], "adapted"),
    ("anya", "Вот поэтому у меня готов план.",
     "That is why I have a plan ready.",
     [(206, "план следующий")], "adapted"),
    ("anya", "Я спрошу Вику: ты простишь меня?",
     "I will ask Vika: will you forgive me?",
     [(207, "Ты простишь меня")], "adapted"),
    ("vika", "Нет, я тебя никогда не прощу!",
     "No, I will never forgive you!",
     [(208, "Тогда прощай")], "adapted"),
    ("vika", "Боже мой, помогите ему кто-нибудь скорее!",
     "Oh my God, somebody help him quickly!",
     [(209, "помогите")], "adapted"),
    ("kostya", "Это всё из-за вас, Виктория Сергеевна!",
     "This is all because of you, Victoria Sergeyevna!",
     [(211, "это все из-за вас")], "adapted"),
    ("anya", "И тогда она сразу меня простит!",
     "And then she will forgive me right away!",
     [(215, "жили они долго и счастливо")], "adapted"),
]

WALK = [
    (0, None,
     "'Max, what are you doing here right now?' -- Kostya walks into the storage room and panics."),
    (1, None,
     "'After all, I really got very scared!' -- The bartender catches his breath after the shock."),
    (2, None,
     "'Well, that was the exact calculation.' -- Max grins, pleased that his illusion looks convincing."),
    (3, None,
     "'Kostya, give me these boxes, please.' -- He asks his friend to help him climb down."),
    (4, None,
     "'Listen, how did you do that?' -- Kostya inspects the hidden rope harness in amazement."),
    (5, None,
     "'Watch closely, I will show you right now.' -- Max demonstrates the secret strap under his jacket."),
    (6, None,
     "'Yes, that looks simply very cool.' -- Kostya admits the stunt is cleverly rigged."),
    (7, None,
     "'Do you remember telling me about the dog?' -- Max reminds him of the story about Ralph."),
    (8, None,
     "'That is why I have a plan ready.' -- He explains that the story inspired his grand scheme."),
    (9, None,
     "'I will ask Vika: will you forgive me?' -- Max imagines how he will confront Vika."),
    (10, None,
     "'No, I will never forgive you!' -- In his daydream, Vika coldly rejects his apology."),
    (11, None,
     "'Oh my God, somebody help him quickly!' -- Then she panics when she sees him in danger."),
    (12, None,
     "'This is all because of you, Victoria Sergeyevna!' -- Kostya plays the part of the accusing friend in the fantasy."),
    (13, None,
     "'And then she will forgive me right away!' -- Max is convinced the theatrical scare will end with a happy reunion."),
]

TRANSITION = "Now let's listen to the whole storage room scene again without interruption."
OUTRO = (
    "Confident that his staged accident will melt Vika's heart just like Kostya's story about his dog, "
    "Max prepares to put his reckless plan into action."
)
CLOSING = ("anya", "И тогда она сразу меня простит!")
