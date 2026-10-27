# Scene 19: Вы брали взятки? (Did You Take Bribes?)
# Cues 587-606: Marina extracts a confession about bribery from Eduard during dinner.

ID = "domashniy-arest-s01e09-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 19

TITLE = "Вы брали взятки?  (Did You Take Bribes?)"
LEVEL = "A1"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "eduard": "anja",
}

LABELS = {
    "anya": "Марина",
    "eduard": "Эдуард",
}

INTRO = "Marina and Eduard share dinner at a stylish restaurant while Eduard opens up about his childhood and his controversial past as an official."

STORY = [
    ("eduard", "Мама меня бросила в детстве.",
     "Mother abandoned me in childhood.",
     [(587, "Мама меня бросила.")], "adapted cue 587"),

    ("eduard", "Я её совсем не помню.",
     "I do not remember her at all.",
     [(587, "Ее я не помню.")], "adapted cue 587"),

    ("eduard", "Своего отца я тоже не знаю.",
     "My father I do not know either.",
     [(589, "Так что отца своего я"), (590, "просто не знаю.")], "combined cues 589 and 590"),

    ("eduard", "Всё это очень грустно.",
     "All this is very sad.",
     [(591, "Все это грустно.")], ""),

    ("eduard", "Спросите что-нибудь другое.",
     "Ask something else.",
     [(591, "Спросите что-нибудь другое.")], ""),

    ("anya", "Хорошо, я спрошу.",
     "Alright, I will ask.",
     [(592, "Хорошо.")], "adapted cue 592"),

    ("anya", "Вы когда-нибудь брали взятки?",
     "Have you ever taken bribes?",
     [(593, "Вы брали взятки?")], "adapted cue 593"),

    ("eduard", "О, а вот это интересно!",
     "Oh, now that is interesting!",
     [(594, "О, а вот это интересно.")], ""),

    ("eduard", "Город — это сложная система.",
     "A city is a complex system.",
     [(595, "город это сложная")], "adapted cue 595"),

    ("eduard", "Им очень трудно управлять.",
     "It is very hard to manage it.",
     [(596, "Им нужно управлять")], "adapted cue 596"),

    ("anya", "Вы можете ответить на вопрос?",
     "Can you answer the question?",
     [(600, "Можете ответить на вопрос?")], ""),

    ("eduard", "Да, я брал взятки.",
     "Yes, I took bribes.",
     [(601, "Да, брал.")], "adapted cue 601"),

    ("anya", "Спасибо за честный ответ.",
     "Thank you for the honest answer.",
     [(603, "Спасибо.")], "adapted cue 603"),

    ("anya", "Вы ответили хорошо.",
     "You answered well.",
     [(604, "Вы на вопрос ответили хорошо")], "adapted cue 604"),

    ("anya", "Но брать взятки — очень плохо.",
     "But taking bribes is very bad.",
     [(604, "а то что брали плохо.")], "adapted cue 604"),
]

OPENER = "Now let's see how Marina extracts a confession about bribes from Eduard."

WALK = [
    (1, None,
     "'I do not remember her at all.' The negative expression intensifies the verb to mean not remembering a person at all."),
    (4, None,
     "'Ask something else.' The imperative verb takes the indefinite pronoun to mean any other topic."),
    (6, None,
     "'Have you ever taken bribes?' Marina bluntly asks the core incriminating question for the secret recording."),
    (10, None,
     "'Can you answer the question?' Marina cuts through his long explanation and demands a direct response."),
    (11, None,
     "'Yes, I took bribes.' Eduard openly admits his corrupt past on the restaurant microphone."),
]

TRANSITION = "Let's listen to the revealing dinner conversation once again from the beginning."

OUTRO = "Eduard has confessed to taking bribes without realizing he is being recorded."

CLOSING = ("eduard", "Что ещё вы хотите узнать?")
