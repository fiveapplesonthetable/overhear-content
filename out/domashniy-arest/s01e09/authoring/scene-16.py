# Scene 16: Блинчики (Pancakes)
# Cues 470-482: Ilona coaches Samsonov to pretend to flirt while Nina watches from outside.

ID = "domashniy-arest-s01e09-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 16

TITLE = "Блинчики  (Pancakes)"
LEVEL = "A1"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
}

LABELS = {
    "anya": "Илона",
    "samson": "Самсон",
}

INTRO = "Ilona and Samsonov sit together at a table in the cafe, pretending to be on a romantic date while Nina watches closely through the window."

STORY = [
    ("anya", "Не надо туда смотреть.",
     "Don't look over there.",
     [(470, "Не надо туда смотреть.")], ""),

    ("samson", "Нина стоит у окна.",
     "Nina is standing by the window.",
     [], "new setup line"),

    ("anya", "Смотри на меня и улыбайся.",
     "Look at me and smile.",
     [(471, "Смотри на меня и улыбайся.")], ""),

    ("samson", "Я пытаюсь улыбаться.",
     "I am trying to smile.",
     [], "new reaction"),

    ("anya", "Отмахнись от неё рукой.",
     "Wave her off with your hand.",
     [(473, "Отмахнись.")], "adapted cue 473"),

    ("samson", "Что ты говоришь?",
     "What are you saying?",
     [(474, "Что?")], "adapted cue 474"),

    ("anya", "Отмахнись, говорю тебе.",
     "Wave her off, I tell you.",
     [(475, "Отмахнись, говорю.")], "adapted cue 475"),

    ("samson", "Да ладно, неудобно как-то.",
     "Come on, it feels awkward somehow.",
     [(476, "Да ладно.")], "adapted cue 476"),

    ("anya", "Не пей, делай вид.",
     "Don't drink, just pretend.",
     [(477, "Не пей, делай вид.")], ""),

    ("anya", "А сейчас улыбнись мне.",
     "And now smile at me.",
     [(478, "А сейчас улыбнись мне.")], ""),

    ("samson", "Хорошо, я улыбаюсь.",
     "Alright, I am smiling.",
     [], "new line"),

    ("anya", "Скажи мне какое-нибудь слово.",
     "Say some word to me.",
     [(479, "Скажи мне какое-нибудь слово.")], ""),

    ("samson", "Какое слово сказать?",
     "What word should I say?",
     [(480, "Какое?")], "adapted cue 480"),

    ("anya", "Любое скажи.",
     "Say any word.",
     [(481, "Любое")], "adapted cue 481"),

    ("samson", "Блинчики?",
     "Pancakes?",
     [(482, "Блинчики?")], ""),
]

OPENER = "Now let's unpack how Ilona coaches Samsonov to make his wife jealous."

WALK = [
    (0, None,
     "'Don't look over there.' The negative expression tells someone not to look in that direction."),
    (2, None,
     "'Look at me and smile.' The imperative verb directs him to face her with a warm expression."),
    (8, None,
     "'Don't drink, just pretend.' The command instructs him to only simulate drinking wine."),
    (11, None,
     "'Say some word to me.' The indefinite pronoun asks for any random word to simulate dialogue."),
    (14, None,
     "'Pancakes?' Samsonov blurts out the first food item that pops into his head."),
]

TRANSITION = "Let's listen to the whole conversation once again from the beginning."

OUTRO = "Ilona is amused by Samsonov's awkward choice of words."

CLOSING = ("anya", "Почему именно блинчики?")
