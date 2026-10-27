# -*- coding: utf-8 -*-
"""Scene 27 of domashniy-arest s01e09: Ambush at the Kindergarten."""

ID = "domashniy-arest-s01e09-scene-27"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 27
TITLE = "Засада в детском саду  (Ambush at the Kindergarten)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "lavrov": "anja",
    "sokolov": "angelina",
}

LABELS = {
    "anya": "Осипенко",
    "lavrov": "Лавров",
    "sokolov": "Соколов",
}

INTRO = (
    "Osipenko and Lavrov lay out their trap at the kindergarten. While they calculate how to "
    "gain Anikeyev's trust, special forces officers pack into a cramped assault vehicle. "
    "Young officer Sokolov finds the bumpy ride a bit too overwhelming. Listen to their "
    "Russian conversation first, and do not worry about catching every single word."
)

OPENER = "Let's examine how the raid is planned and deployed line by line."

STORY = [
    ("lavrov", "Я не понял, в чём смысл?",
     "I did not understand, what is the point?",
     [(727, "в чем смысл")], ""),
    ("anya", "Она сейчас поедет в детский сад.",
     "She will go to the kindergarten now.",
     [(728, "Она сейчас поедет в детский сад")], ""),
    ("anya", "Там всё тихо. Значит, Марина чистая.",
     "Everything is quiet there. That means Marina is clean.",
     [(729, "Там все тихо"), (729, "Значит, Марина чистая")], ""),
    ("anya", "После этого Аникеев ей будет полностью доверять.",
     "After that, Anikeyev will trust her completely.",
     [(730, "ей будет полностью доверять")], ""),
    ("anya", "И тогда мы узнаем всё, что нужно.",
     "And then we will find out everything necessary.",
     [(731, "И тогда мы узнаем все")], ""),
    ("lavrov", "Хитро придумано, шеф!",
     "Cleverly thought out, boss!",
     [(732, "Хитро")], ""),
    ("anya", "Учись, Соколов! Соколов!",
     "Learn from this, Sokolov! Sokolov!",
     [(733, "Учись, Соколов! Соколов!")], ""),
    ("lavrov", "А где Соколов? Ты что, обиделся?",
     "And where is Sokolov? What, did you get offended?",
     [(734, "Ты что, обиделся"), (735, "А где Соколов?")], ""),
    ("sokolov", "Пошли, ребята, пошли на штурм!",
     "Let's go, guys, let's go on the raid!",
     [(737, "Пошли, ребята, пошли!")], ""),
    ("sokolov", "Так, первый пошёл, второй, третий!",
     "Right, first one in, second, third!",
     [(738, "первый пошел, второй")], ""),
    ("sokolov", "Простите, можно я выйду?",
     "Excuse me, may I get out?",
     [(746, "Простите, можно я выйду?")], ""),
    ("anya", "Нельзя! Сидеть на месте!",
     "You cannot! Sit in your place!",
     [(747, "Нельзя")], ""),
    ("sokolov", "Меня сейчас тошнит.",
     "I feel nauseous right now.",
     [(748, "Меня сейчас тошнит")], ""),
    ("anya", "Терпеть! Операция началась!",
     "Endure it! The operation has begun!",
     [(749, "Терпеть!")], ""),
]

WALK = [
    (0, None,
     "'I did not understand, what is the point?' The prepositional phrase asks for meaning."),
    (1, None,
     "'She will go to the kindergarten now.' The motion verb in future tense indicates departure."),
    (2, "Там всё тихо.",
     "'Everything is quiet there.' A short descriptive statement using the neuter adjective."),
    (2, "Значит, Марина чистая.",
     "'That means Marina is clean.' The conversational conjunction introduces a logical conclusion."),
    (3, None,
     "'After that, Anikeyev will trust her completely.' The compound future combines auxiliary and infinitive."),
    (4, None,
     "'And then we will find out everything necessary.' The perfective verb marks achieving knowledge."),
    (5, None,
     "'Cleverly thought out, boss!' A short passive participle used predicatively in praise."),
    (6, None,
     "'Learn from this, Sokolov! Sokolov!' The reflexive imperative commands someone to learn."),
    (7, "А где Соколов?",
     "'And where is Sokolov?' Lavrov looks around looking for their absent colleague."),
    (7, "Ты что, обиделся?",
     "'What, did you get offended?' The past tense masculine reflexive verb describes hurt feelings."),
    (8, None,
     "'Let's go, guys, let's go on the raid!' A classic rallying cry before moving into action."),
    (9, None,
     "'Right, first one in, second, third!' Counting off troops loading sequentially into position."),
    (10, None,
     "'Excuse me, may I get out?' The modal predicative asks for polite permission to leave."),
    (11, "Нельзя!",
     "'You cannot!' A strict categorical negative command expressing total prohibition."),
    (11, "Сидеть на месте!",
     "'Sit in your place!' An infinitive used as a firm military-style order."),
    (12, None,
     "'I feel nauseous right now.' An impersonal construction using accusative pronoun with verb."),
    (13, "Терпеть!",
     "'Endure it!' An infinitive used forcefully to order someone to hold on."),
    (13, "Операция началась!",
     "'The operation has begun!' The reflexive past feminine verb indicates the start."),
]

TRANSITION = "Now listen to the kindergarten assault coordination one more time."

OUTRO = (
    "With the assault underway, the stage is set for a chaotic showdown at the daycare. "
    "In the following scenes, both sides converge on the Golden Key."
)

CLOSING = ("anya", "Операция началась!")
