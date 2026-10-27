ID = "domashniy-arest-s01e11-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 1
TITLE = "Предложение в кафе  (Proposal in the Cafe)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja"}
LABELS = {"anya": "Нина", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-49. In a 1990s flashback, young Ivan Samsonov takes Nina to a popular local pastry shop. "
    "He hides an engagement ring in an eclair and clumsily proposes, but Nina turns him down."
)

INTRO = (
    "In this flashback to the nineteen-nineties, young Ivan Samsonov takes Nina to a crowded local cafe. "
    "He reveals that couples often propose here because the civil registry office is right next door. "
    "Ivan unexpectedly hides an engagement ring inside Nina's pastry and asks her to marry him, but Nina rejects his rushed proposal. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Здесь всегда стоит такая большая очередь.",
     "There is always such a big line here.",
     [(1, "Все время очередник здесь")], ""),
    ("samson", "Здесь готовят самые вкусные пирожные в городе!",
     "They make the most delicious pastries in town here!",
     [(2, "самый вкусный бомбир в городе")], ""),
    ("samson", "Ты знаешь, что здесь часто делают предложение?",
     "Do you know that people often propose here?",
     [(5, "А ты в курсе, что здесь люди друг другу предложения делают")], ""),
    ("anya", "Я первый раз слышу об этом.",
     "This is the first time I hear about this.",
     [(6, "Не знаю, первый раз слышу")], ""),
    ("samson", "Тут же рядом находится городской ЗАГС.",
     "The town registry office is right nearby.",
     [(7, "тут же ЗАГС рядом")], ""),
    ("anya", "И что ты этим хочешь сказать?",
     "And what do you want to say by that?",
     [(8, "Ну и что")], ""),
    ("anya", "Самсон, что это лежит в моём пирожном?",
     "Samson, what is this lying in my pastry?",
     [(18, "Ну, это что, Самсон")], ""),
    ("samson", "Это красивое золотое кольцо для тебя!",
     "This is a beautiful gold ring for you!",
     [(19, "Что? Кольцо")], ""),
    ("anya", "Самсон, ты что, совсем сошёл с ума?",
     "Samson, have you completely lost your mind?",
     [(21, "Ты что, дурак, что ли")], ""),
    ("samson", "Мы с тобой уже целый месяц вместе.",
     "You and I have been together a whole month.",
     [(28, "Мы друг друга с тобой месяц знаем")], ""),
    ("samson", "У меня есть отдельная комната в коммуналке.",
     "I have a separate room in a communal flat.",
     [(38, "комната в коммуналке есть")], ""),
    ("samson", "Выходи за меня замуж прямо сейчас!",
     "Marry me right now!",
     [(40, "Давай, ладно, соглашайся")], ""),
    ("anya", "Нет, Самсон, я не согласна.",
     "No, Samson, I do not agree.",
     [(42, "Нет"), (44, "в смысле нет")], ""),
    ("anya", "Забери это кольцо обратно себе.",
     "Take this ring back for yourself.",
     [(45, "ты кольцо, конечно, забери")], ""),
]

OPENER = "Now let's examine Ivan and Nina's cafe conversation line by line."

WALK = [
    (0, None,
     "'There is always such a big line here.' Nina remarks on the crowded cafe with an adverb of frequency."),
    (1, None,
     "'They make the most delicious pastries in town here!' Samson boasts using a superlative adjective construction."),
    (2, None,
     "'Do you know that people often propose here?' Samson drops a hint using an impersonal third-person plural clause."),
    (3, None,
     "'This is the first time I hear about this.' Nina replies with a fixed conversational idiom of surprise."),
    (4, None,
     "'The town registry office is right nearby.' Samson points out the romantic convenience with a reflexive verb."),
    (5, None,
     "'And what do you want to say by that?' Nina asks suspiciously using the instrumental demonstrative pronoun."),
    (6, None,
     "'Samson, what is this lying in my pastry?' Nina discovers the hidden object with a prepositional singular noun."),
    (7, None,
     "'This is a beautiful gold ring for you!' Samson reveals the engagement ring with qualitative adjectives."),
    (8, None,
     "'Samson, have you completely lost your mind?' Nina reacts in disbelief using a popular idiomatic phrase."),
    (9, None,
     "'You and I have been together a whole month.' Samson argues his case with a duration accusative phrase."),
    (10, None,
     "'I have a separate room in a communal flat.' Samson presents his humble assets using a genitive possession clause."),
    (11, None,
     "'Marry me right now!' Samson proposes bluntly with the classic Russian marriage idiom."),
    (12, None,
     "'No, Samson, I do not agree.' Nina turns down the proposal using a short predicate adjective."),
    (13, None,
     "'Take this ring back for yourself.' Nina returns the ring with an imperative perfective verb."),
]

TRANSITION = "Now let's listen to Samson's clumsy proposal again without interruption."
OUTRO = (
    "Nina refuses Ivan's hasty proposal, leaving him sitting in shock. "
    "In the next scene, Ivan refuses to leave and waits outside for her."
)
CLOSING = ("anya", "Нет, Самсон, я не согласна.")
