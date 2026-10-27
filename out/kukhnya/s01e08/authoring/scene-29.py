"""Scene 29 — Bet Between the Chefs (s01e08, 00:20:14–00:20:59)."""

ID = "kukhnya-s01e08-scene-29"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 29
TITLE = "Пари между шефами  (Bet Between the Chefs)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 343-356. After Elena's disastrous day managing the Claude Monet kitchen, "
    "Barinov celebrates winning their bet and passionately defends his flawed cooks."
)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}

LABELS = {
    "anya": "Елена",
    "chef": "Шеф",
}

INTRO = (
    "After rival chef Elena Sokolova spends a grueling day attempting to manage the Claude Monet kitchen, "
    "orders fall apart and dishes get sent back by disgruntled diners. "
    "Confronting Elena in his office, Chef Barinov triumphantly declares that he won their bet, "
    "delivering a passionate defense of his quirky kitchen crew. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("chef", "Что и требовалось доказать, Елена Павловна!",
     "That proves my point, Elena Pavlovna!",
     [(343, "Что и требовалось доказать.")], "Barinov declares victory"),

    ("chef", "Я снова оказался абсолютно прав сегодня.",
     "I turned out absolutely right again today.",
     [(344, "Я говорю, что я оказался прав.")], "Barinov insists he was right"),

    ("chef", "Впрочем, как и всегда, я выиграл пари!",
     "As always, I won the bet!",
     [(345, "Впрочем, как и всегда. Я выиграл парень.")], "Claiming the bet"),

    ("anya", "Виктор, прекратите говорить эту глупую ерунду.",
     "Viktor, stop talking this silly nonsense.",
     [(346, "Да не говорите ерунду.")], "Elena pushes back"),

    ("anya", "Я проработала на вашей кухне целый день.",
     "I worked in your kitchen the whole day.",
     [(347, "Я проработала у вас на кухне целый день")], "Elena recounts shift"),

    ("anya", "Сначала всё было совершенно спокойно и нормально.",
     "At first everything was completely calm and normal.",
     [(347, "и все было нормально.")], "Recalling smooth start"),

    ("anya", "А потом все повара словно заболели!",
     "And then all the cooks seemed to get sick!",
     [(348, "что-то случилось"), (349, "Все как будто заболели.")], "Describing sudden chaos"),

    ("anya", "У вас на кухне работают сплошные инвалиды!",
     "You have nothing but cripples working in your kitchen!",
     [(350, "У вас не повара, а инвалиды.")], "Venting frustration"),

    ("chef", "Правильно, но это мои родные люди!",
     "Right, but these are my own people!",
     [(351, "Правильно."), (352, "Но это мои инвалиды.")], "Defending crew"),

    ("chef", "И только я имею право их ругать.",
     "And only I have the right to scold them.",
     [(352, "И только я имею право их так называть.")], "Claiming exclusive right"),

    ("chef", "Работа шефа — сделать из них команду!",
     "The chef's job is to make a team out of them!",
     [(353, "И разве не в этом состоит работа шефа?"), (354, "высококлассную команду?")], "Articulating leadership"),

    ("anya", "Вы умеете красиво оправдать любой беспорядок.",
     "You know how to beautifully justify any mess.",
     [], "Elena shakes head"),

    ("chef", "Шеф, вы мне должны отличный ужин!",
     "Chef, you owe me a great dinner!",
     [(355, "А? Шеф?"), (356, "Вы мне ужин должны.")], "Demanding dinner wager"),
]

OPENER = "Now let's examine Viktor and Elena's wager post-mortem line by line."

WALK = [
    (0, None,
     "'That proves my point, Elena Pavlovna!' Viktor Barinov gloats about his victory with undisguised pleasure."),
    (1, None,
     "'I turned out absolutely right again today.' The head chef celebrates his superior kitchen strategy."),
    (2, None,
     "'As always, I won the bet!' Barinov reminds his culinary rival of their high-stakes wager."),
    (3, None,
     "'Viktor, stop talking this silly nonsense.' Elena dismisses his arrogance with sharp exasperation."),
    (4, None,
     "'I worked in your kitchen the whole day.' The guest chef recounts her exhausting shift on the line."),
    (5, None,
     "'At first everything was completely calm and normal.' She recalls the smooth operation of the kitchen early on."),
    (6, None,
     "'And then all the cooks seemed to get sick!' Elena describes the sudden wave of disastrous blunders."),
    (7, None,
     "'You have nothing but cripples working in your kitchen!' She vents her frustration at the crew's sudden incompetence."),
    (8, None,
     "'Right, but these are my own people!' As Barinov fiercely defends his cooks against outside criticism."),
    (9, None,
     "'And only I have the right to scold them.' The chef claims exclusive ownership of his kitchen family."),
    (10, None,
     "'The chef's job is to make a team out of them!' Barinov eloquently articulates the true essence of leadership."),
    (11, None,
     "'You know how to beautifully justify any mess.' Elena shakes her head at Viktor's brazen charm."),
    (12, None,
     "'Chef, you owe me a great dinner!' Barinov happily claims his wager prize with a triumphant grin."),
]

TRANSITION = "Now let's listen to Viktor and Elena discussing the bet once more without interruption."

OUTRO = (
    "Viktor Barinov defends his loyal cooks and secures a hard-earned dinner date from his rival."
)

CLOSING = ("chef", "Шеф, вы мне должны отличный ужин!")
