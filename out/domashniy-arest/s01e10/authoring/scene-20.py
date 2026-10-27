# Scene 20: Фильм о монастыре (Film About the Monastery)
# Cues 586-612: Marina pitches a documentary project about the monastery to Eduard.

ID = "domashniy-arest-s01e10-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 20

TITLE = "Фильм о монастыре  (Film About the Monastery)"
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

INTRO = "In Eduard's office, Marina pitches an ambitious documentary project about the monastery while Eduard makes cautious promises."

STORY = [
    ("anya", "Вы же знаете, что я историк.",
     "You know that I am a historian.",
     [(586, "Вы же знаете, я историк.")], "adapted cue 586"),

    ("anya", "Я исследовала историю нашего города.",
     "I researched the history of our town.",
     [(587, "Я занималась исследованием наших мест.")], "adapted cue 587"),

    ("anya", "Моя диссертация — о монастыре.",
     "My dissertation is about the monastery.",
     [(588, "диссертация о Синей Озерском монастыре.")], "adapted cue 588"),

    ("anya", "У меня есть много редких материалов.",
     "I have many rare materials.",
     [(589, "У меня есть целый ворох архивных материалов")], "adapted cue 589"),

    ("anya", "Здесь был утрачен древний оригинал летописи.",
     "Here the ancient original of the chronicle was lost.",
     [(592, "был утрачен оригинал повести временных лет?")], "adapted cue 592"),

    ("anya", "Мы могли бы сделать фильм расследования.",
     "We could make an investigative film.",
     [(595, "мы могли бы сделать фильм расследования.")], ""),

    ("eduard", "Это просто прекрасная идея!",
     "This is simply a wonderful idea!",
     [(599, "Прекрасная идея. Просто замечательная.")], "adapted cue 599"),

    ("eduard", "Но сейчас мы очень ограничены в средствах.",
     "But right now we are very limited in funds.",
     [(602, "мы очень ограничены в средствах.")], "adapted cue 602"),

    ("eduard", "Как только деньги появятся, мы запустим программу.",
     "As soon as the money appears, we will launch the program.",
     [(604, "как только эти средства появятся"), (606, "и мы тут же запустим эту программу.")], "combined cues 604 and 606"),

    ("anya", "Хорошо. А что у вас с лицом?",
     "Alright. And what happened to your face?",
     [(607, "Хорошо. Что у вас с лицом?")], ""),

    ("eduard", "Это просто аллергия на орехи.",
     "It is just an allergy to nuts.",
     [(608, "Аллергия. Фундук.")], "adapted cue 608"),

    ("anya", "Будьте аккуратнее со своим здоровьем.",
     "Be more careful with your health.",
     [(609, "Аккуратнее.")], "adapted cue 609"),

    ("anya", "Хорошего вам дня, Эдуард Валентинович.",
     "Have a good day, Eduard Valentinovich.",
     [(610, "Хорошего дня.")], "adapted cue 610"),

    ("eduard", "Спасибо вам большое, Марина.",
     "Thank you very much, Marina.",
     [(611, "Спасибо вам большое.")], "adapted cue 611"),

    ("eduard", "Обязательно забегайте ко мне снова.",
     "Be sure to drop by my office again.",
     [(612, "Забегайте.")], "adapted cue 612"),
]

OPENER = "Now let's see how Marina pitches her historical documentary to Eduard."

WALK = [
    (0, None,
     "'You know that I am a historian.' Marina establishes her academic credentials as the basis for the project."),
    (5, None,
     "'We could make an investigative film.' The conditional construction proposes a documentary film format."),
    (7, None,
     "'But right now we are very limited in funds.' Eduard relies on budgetary constraints to delay immediate commitments."),
    (9, "А что у вас с лицом?",
     "'And what happened to your face?' Marina notices red marks and swelling on his face."),
    (11, None,
     "'Be more careful with your health.' The imperative adjective urges him to exercise caution with food allergens."),
]

TRANSITION = "Let's listen to Marina's documentary pitch once again from the beginning."

OUTRO = "Eduard praises Marina's initiative and promises to consider the documentary later."

CLOSING = ("anya", "Я подготовлю подробный план фильма.")
