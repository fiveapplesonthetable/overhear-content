# -*- coding: utf-8 -*-
"""Scene 30 of domashniy-arest s01e10: Craft Contest Announcement."""

ID = "domashniy-arest-s01e10-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 30
TITLE = "Конкурс поделок  (The Craft Contest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "teacher": "anja",
}

LABELS = {
    "anya": "Заведующая",
    "teacher": "Воспитательница",
}

INTRO = (
    "Parents and children assemble in the kindergarten hall for the climax of the crafts "
    "contest. The kindergarten director and the lead teacher take the stage to praise all the "
    "young participants before announcing who took the top prize. Listen to the Russian "
    "announcement first, and do not worry about catching every single word."
)

OPENER = "Let's examine how the kindergarten director builds suspense line by line."

STORY = [
    ("anya", "Дорогие родители и дети!",
     "Dear parents and children!",
     [], "the director welcomes the crowd"),
    ("teacher", "Наш конкурс поделок подошёл к концу.",
     "Our craft contest has come to an end.",
     [], "the teacher steps up"),
    ("anya", "Все наши юные творцы сделали замечательные поделки!",
     "All our young creators made wonderful crafts!",
     [(955, "Все наши юные творцы"), (956, "сделали замечательные поделки")], ""),
    ("teacher", "Каждая работа была очень интересной.",
     "Every work was very interesting.",
     [], "she points to the display tables"),
    ("anya", "Выбрать было очень сложно!",
     "It was very difficult to choose!",
     [(957, "Выбрать было очень сложно")], ""),
    ("teacher", "Все ребята очень старались.",
     "All the children tried very hard.",
     [], "the teacher nods affectionately"),
    ("anya", "Давайте поаплодируем всем нашим участникам!",
     "Let's give a round of applause to all our participants!",
     [(958, "Давайте поаплодируем всем")], ""),
    ("teacher", "Они заслужили самые громкие аплодисменты.",
     "They deserved the loudest applause.",
     [], "the room begins to clap"),
    ("anya", "А теперь наступил долгожданный момент.",
     "And now the long-awaited moment has arrived.",
     [], "she holds up the sealed envelope"),
    ("anya", "Перед тем, как я объявлю победителя, внимание!",
     "Before I announce the winner, your attention!",
     [(959, "перед тем, как я объявлю победителя")], ""),
    ("teacher", "Кто же занял первое место?",
     "Who took first place after all?",
     [], "the room falls silent in anticipation"),
    ("anya", "Давайте узнаем имя нашего главного победителя!",
     "Let's find out the name of our grand winner!",
     [], "the director opens the envelope"),
]

WALK = [
    (0, None,
     "'Dear parents and children!' A polite formal opening welcoming families in the hall."),
    (1, None,
     "'Our craft contest has come to an end.' The idiom means arrived at its conclusion."),
    (2, None,
     "'All our young creators made wonderful crafts!' Notice plural adjectives and nouns."),
    (3, None,
     "'Every work was very interesting.' The past tense feminine verb takes instrumental predicate."),
    (4, None,
     "'It was very difficult to choose!' An impersonal construction using infinitive and adverb."),
    (5, None,
     "'All the children tried very hard.' The reflexive past plural indicates diligent effort."),
    (6, None,
     "'Let's give a round of applause to all our participants!' The cohortative imperative takes dative."),
    (7, None,
     "'They deserved the loudest applause.' The compound superlative emphasizes the highest volume."),
    (8, None,
     "'And now the long-awaited moment has arrived.' The perfective verb marks a grand arrival."),
    (9, None,
     "'Before I announce the winner, your attention!' A temporal clause introduced by before."),
    (10, None,
     "'Who took first place after all?' The past tense perfective verb pairs with ordinal accusative."),
    (11, None,
     "'Let's find out the name of our grand winner!' The cohortative imperative urges discovering the name."),
]

TRANSITION = "Now listen to the kindergarten contest announcement once again."

OUTRO = (
    "Suspense peaks in the auditorium as the director prepares to reveal the top craft. In the "
    "next scene, young Lyosha discovers the unexpected fruits of Arkady's intervention."
)

CLOSING = ("anya", "Давайте узнаем имя нашего главного победителя!")
