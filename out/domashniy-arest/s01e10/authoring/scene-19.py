# Scene 19: Дружный коллектив (A Friendly Team)
# Cues 569-585: Eduard Valentinovich welcomes Marina and invites her suggestions.

ID = "domashniy-arest-s01e10-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 19

TITLE = "Дружный коллектив  (A Friendly Team)"
LEVEL = "A1"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест S01E10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "eduard": "anja",
}

LABELS = {
    "anya": "Марина",
    "eduard": "Эдуард",
}

INTRO = "In the municipal culture department, Eduard Valentinovich welcomes Marina and invites her to share new professional ideas."

STORY = [
    ("eduard", "Наше знакомство началось как-то неправильно.",
     "Our acquaintance started somehow wrong.",
     [(569, "наше знакомство началось как-то неправильно.")], ""),

    ("eduard", "Тогда я был сильно на взводе.",
     "Back then I was terribly on edge.",
     [(570, "Я был на взводе.")], "adapted cue 570"),

    ("eduard", "У меня были семейные неприятности.",
     "I had family troubles.",
     [(571, "Семейные неприятности, знаете ли")], "adapted cue 571"),

    ("eduard", "Обычно я совсем не такой.",
     "Usually I am not like that at all.",
     [(572, "обычно я не такой.")], "adapted cue 572"),

    ("eduard", "Я хочу официально поздравить вас.",
     "I want to officially congratulate you.",
     [(573, "Поэтому я хочу вас официально поздравить")], "adapted cue 573"),

    ("eduard", "Вы прекрасно влились в наш коллектив.",
     "You fit into our team wonderfully.",
     [(574, "вы прекрасно влились"), (575, "в наш маленький, но дружный коллектив.")], "combined cues 574 and 575"),

    ("eduard", "Наш коллектив маленький, но очень дружный.",
     "Our collective is small, but very friendly.",
     [(575, "в наш маленький, но дружный коллектив.")], "adapted cue 575"),

    ("anya", "Спасибо вам большое, Эдуард Валентинович.",
     "Thank you very much, Eduard Valentinovich.",
     [(576, "Спасибо.")], "adapted cue 576"),

    ("eduard", "Так что работайте спокойно.",
     "So work quietly.",
     [(577, "Так что работайте.")], "adapted cue 577"),

    ("eduard", "Если будут вопросы — милости просим.",
     "If there are questions, you are welcome.",
     [(578, "если будут какие-то вопросы"), (580, "милости просим.")], "combined cues 578 and 580"),

    ("anya", "Спасибо. Всего вам доброго.",
     "Thank you. All the best to you.",
     [(581, "Спасибо. Всего доброго.")], ""),

    ("anya", "Скажите, а вы серьёзно о предложениях?",
     "Tell me, were you serious about suggestions?",
     [(582, "Скажите, а"), (583, "о предложениях вы это серьезно?")], "combined cues 582 and 583"),

    ("eduard", "Ну конечно, я совершенно серьёзно!",
     "Well of course, I am completely serious!",
     [(584, "Ну, конечно.")], "adapted cue 584"),

    ("eduard", "Мы всегда находимся в творческом поиске.",
     "We are always in a creative search.",
     [(585, "мы всегда в творческом поиске.")], "adapted cue 585"),

    ("eduard", "Я внимательно слушаю вас, Марина.",
     "I am listening to you attentively, Marina.",
     [(585, "Слушаю вас.")], "adapted cue 585"),
]

OPENER = "Now let's see how Eduard Valentinovich welcomes Marina to the department."

WALK = [
    (0, None,
     "'Our acquaintance started somehow wrong.' Eduard seeks to smooth over their awkward initial meeting."),
    (4, None,
     "'I want to officially congratulate you.' The construction takes the accusative pronoun for the person congratulated."),
    (6, None,
     "'Our collective is small, but very friendly.' The contrasting conjunction links the two descriptive adjectives."),
    (9, None,
     "'If there are questions, you are welcome.' The traditional Russian welcoming phrase invites her to approach him."),
    (13, None,
     "'We are always in a creative search.' The prepositional phrase describes an ongoing artistic endeavor."),
]

TRANSITION = "Let's listen to the courteous office conversation once again from the beginning."

OUTRO = "Marina takes advantage of the warm welcome to introduce her historical documentary project."

CLOSING = ("anya", "У меня есть отличная идея!")
