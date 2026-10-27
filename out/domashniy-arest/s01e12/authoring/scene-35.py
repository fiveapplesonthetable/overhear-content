"""Scene 35 — Pasha's Conscience (s01e12, 01:17:36–01:17:40)."""

ID = "domashniy-arest-s01e12-scene-35"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 35
TITLE = "Совесть Паши  (Pasha's Conscience)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
}

LABELS = {
    "anya": "Паша",
    "samson": "Самсон",
}

INTRO = (
    "Following the chaotic shootout, Ivan Samsonov confronts the cornered gunman Pasha, demanding "
    "to know why he resorted to cold-blooded violence and whether he has any conscience left."
)

STORY = [
    ("samson", "Брось своё оружие прямо сейчас!",
     "Drop your weapon right now!",
     [], "confronting gunman"),

    ("samson", "Паша, ты зачем всех убиваешь?",
     "Pasha, why are you killing everyone?",
     [(1029, "Паша, ты зачем всех убиваешь?")], "demanding explanation"),

    ("anya", "Они все хотели меня предать!",
     "They all wanted to betray me!",
     [], "Pasha's justification"),

    ("samson", "У тебя совесть есть вообще?",
     "Have you no conscience at all?",
     [(1030, "У тебя совесть есть вообще?")], "appealing to conscience"),

    ("anya", "В этом городе нет никакой совести.",
     "In this city there is no conscience.",
     [], "cynical response"),

    ("samson", "Ты сам выбрал этот страшный путь.",
     "You chose this terrible path yourself.",
     [], "holding accountable"),

    ("anya", "Мне просто нужны были эти деньги!",
     "I simply needed that money!",
     [], "greed admitted"),

    ("samson", "Деньги не стоят человеческой жизни.",
     "Money is not worth a human life.",
     [], "value of life"),

    ("anya", "Теперь для меня уже всё кончено.",
     "Now everything is already over for me.",
     [], "defeat realized"),

    ("samson", "Подними руки и сдайся властям.",
     "Raise your hands and surrender to the authorities.",
     [], "order to surrender"),

    ("anya", "Я не хочу идти в тюрьму.",
     "I do not want to go to prison.",
     [], "fear of prison"),

    ("samson", "Ты должен ответить за свои преступления.",
     "You must answer for your crimes.",
     [], "insisting on justice"),

    ("anya", "Ты победил, Самсонов, забирай пистолет.",
     "You won, Samsonov, take the pistol.",
     [], "surrendering weapon"),

    ("samson", "Справедливость всегда побеждает в конце.",
     "Justice always triumphs in the end.",
     [], "final moral affirmation"),
]

OPENER = "Let's explore the dramatic confrontation between Samsonov and Pasha."

WALK = [
    (0, None,
     "'Drop your weapon right now!' Samsonov confronts the cornered gunman with determination."),
    (1, None,
     "'Pasha, why are you killing everyone?' Samsonov demands an answer for the senseless violence."),
    (2, None,
     "'They all wanted to betray me!' Pasha desperately justifies his ruthless actions in fear."),
    (3, None,
     "'Have you no conscience at all?' Samsonov asks whether Pasha feels any human guilt."),
    (4, None,
     "'In this city there is no conscience.' Pasha cynically rejects any moral code in local politics."),
    (5, None,
     "'You chose this terrible path yourself.' Samsonov places full personal responsibility on Pasha."),
    (6, None,
     "'I simply needed that money!' Pasha admits his insatiable greed drove the whole scheme."),
    (7, None,
     "'Money is not worth a human life.' Samsonov reminds him of the sacred value of life."),
    (8, None,
     "'Now everything is already over for me.' Pasha realizes there is no escape from consequences."),
    (9, None,
     "'Raise your hands and surrender to the authorities.' Samsonov orders him to surrender peacefully."),
    (10, None,
     "'I do not want to go to prison.' Pasha expresses dread of long-term legal imprisonment."),
    (11, None,
     "'You must answer for your crimes.' Samsonov insists on full accountability before the law."),
    (12, None,
     "'You won, Samsonov, take the pistol.' Pasha hands over his weapon in complete defeat."),
    (13, None,
     "'Justice always triumphs in the end.' Samsonov concludes with a firm affirmation of justice."),
]

TRANSITION = "Now let's listen to the high-stakes confrontation between Samsonov and Pasha once more."

OUTRO = "Disarmed and defeated, Pasha faces the consequences of his actions as justice prevails."

CLOSING = ("samson", "Справедливость всегда побеждает в конце.")
