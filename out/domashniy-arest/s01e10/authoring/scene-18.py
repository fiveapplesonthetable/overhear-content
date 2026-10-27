# Scene 18: Свадьба по скайпу (Wedding on Skype)
# Cues 552-564: Slavik recommends a romantic comedy and shares communal apartment gossip.

ID = "domashniy-arest-s01e10-scene-18"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 18

TITLE = "Свадьба по скайпу  (Wedding on Skype)"
LEVEL = "A1"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "slavik": "anja",
    "nina": "angelina",
}

LABELS = {
    "anya": "Самсон",
    "slavik": "Славик",
    "nina": "Нина",
}

INTRO = "In the communal flat, Slavik recommends a funny movie for Samsonov's date while Nina questions where he learned the gossip."

STORY = [
    ("slavik", "Папа, сходи лучше на другой фильм.",
     "Dad, better go to another movie.",
     [(552, "Сходи лучше на")], "adapted cue 552"),

    ("slavik", "Посмотри фильм Свадьба по скайпу.",
     "Watch the movie Wedding on Skype.",
     [(552, "свадьбу по скайпу.")], "adapted cue 552"),

    ("anya", "А про что этот фильм?",
     "And what is this movie about?",
     [], "new line"),

    ("slavik", "Это весёлая комедия про любовь.",
     "It is a cheerful comedy about love.",
     [(553, "Веселая, при любовь.")], "adapted cue 553"),

    ("slavik", "И Таньке фильм очень понравится.",
     "And Tanya will like the movie very much.",
     [(554, "И Таньке понравится.")], ""),

    ("nina", "А ты откуда про Таньку знаешь?",
     "And how do you know about Tanya?",
     [(555, "А ты откуда про Таньку знаешь?")], ""),

    ("slavik", "Мне тётя Клавдия всё рассказала.",
     "Aunt Klavdia told me everything.",
     [(556, "Так мне Клавдия рассказала.")], "adapted cue 556"),

    ("nina", "А тётя Клавдия откуда знает?",
     "And how does Aunt Klavdia know?",
     [(557, "А она откуда знает?")], "adapted cue 557"),

    ("slavik", "Танька ей сама всё сказала.",
     "Tanya told her everything herself.",
     [(558, "Так ей Танька сама и сказала.")], "adapted cue 558"),

    ("anya", "Ты точно уверен в этом?",
     "Are you definitely sure about this?",
     [(561, "Точно?")], "adapted cue 561"),

    ("slavik", "Да, век воли не видать!",
     "Yes, swear on my freedom!",
     [(562, "Век воли не видать.")], ""),

    ("slavik", "Честное слово, зуб даю!",
     "Honest word, swear on my tooth!",
     [(564, "Зуб даю.")], "adapted cue 564"),

    ("nina", "Славик, где ты нахватался таких слов?",
     "Slavik, where did you pick up such words?",
     [], "new reaction"),

    ("slavik", "Во дворе все пацаны так говорят.",
     "In the yard all the boys talk like that.",
     [], "new line"),

    ("anya", "Хорошо, пойдём на эту комедию.",
     "Alright, we will go to this comedy.",
     [], "new line"),
]

OPENER = "Now let's see how Slavik advises his father on choosing a romantic comedy."

WALK = [
    (1, None,
     "'Watch the movie Wedding on Skype.' Slavik suggests a contemporary comedy about modern romance."),
    (4, None,
     "'And Tanya will like the movie very much.' The verb takes the dative case of the person experiencing the liking."),
    (5, None,
     "'And how do you know about Tanya?' Nina is suspicious of how the child learned adult apartment gossip."),
    (8, None,
     "'Tanya told her everything herself.' The intensive pronoun emphasizes that the information came directly from her."),
    (10, None,
     "'Yes, swear on my freedom!' The phrase is traditional Russian slang used to pledge absolute truthfulness."),
]

TRANSITION = "Let's listen to the amusing apartment gossip once again from the beginning."

OUTRO = "Nina is shocked by Slavik's street slang while Samsonov accepts the movie recommendation."

CLOSING = ("nina", "Смотри, чтобы вы не опоздали!")
