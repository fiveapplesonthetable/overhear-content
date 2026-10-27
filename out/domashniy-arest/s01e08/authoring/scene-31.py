# -*- coding: utf-8 -*-
"""Scene 31 of domashniy-arest s01e08: FSB Eavesdropping."""

ID = "domashniy-arest-s01e08-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 31
TITLE = "Прослушка в микроавтобусе  (Eavesdropping in the Van)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "zavarzin": "anja",
    "lyova": "angelina",
}

LABELS = {
    "anya": "Лавров",
    "zavarzin": "Заварзин",
    "lyova": "Лёва",
}

INTRO = (
    "While Samsonov walked home into the night, the surveillance team remained on duty. "
    "Inside their unmarked van across from the communal flat, Major Lavrov, Captain Zavarzin, "
    "and Lieutenant Lyova Sokolov monitor the wiretaps and discover startling news about "
    "Lyosha's surgery quota. Listen to the Russian conversation first, and do not worry "
    "about catching every word."
)

OPENER = "Let's listen in on the security agents inside their van line by line."

STORY = [
    ("zavarzin", "Товарищ майор, просыпайтесь! Тут важная новость.",
     "Comrade Major, wake up! There is important news here.",
     [(657, "Просыпайтесь")], "slang dialogue simplified to A1"),
    ("anya", "Что случилось? Говорите быстрее.",
     "What happened? Speak more quickly.",
     [(661, "Случилось что-то"), (663, "Я сейчас быстро")], ""),
    ("zavarzin", "Подождите, им дали квоту на операцию!",
     "Wait, they gave them a quota for surgery!",
     [(669, "Подождите, им дали квоту"), (671, "им квоту дали на операцию")], ""),
    ("anya", "Интересно совпало. Я не верю в такие совпадения.",
     "An interesting coincidence. I do not believe in such coincidences.",
     [(672, "совпало"), (673, "я мало верю в такие совпадения")], ""),
    ("zavarzin", "А не пожалел ли кто-то её пацана?",
     "What if someone took pity on her boy?",
     [(674, "А не пожалел ли кто-то ее пацана")], ""),
    ("lyova", "Товарищ майор, я тут что подумал!",
     "Comrade Major, look what I was thinking!",
     [(678, "товарищ майор, я тут что подумал")], ""),
    ("lyova", "А может быть, это он помог ей?",
     "What if it was he who helped her?",
     [(679, "А может быть, это он")], ""),
    ("lyova", "Он же заступался за неё!",
     "After all, he stood up for her!",
     [(680, "Он же заступался за нее")], ""),
    ("anya", "Лейтенант Соколов, вы каким местом думаете?",
     "Lieutenant Sokolov, what are you thinking with?",
     [(683, "Лейтенант Соколов, вы каким местом думаете")], ""),
    ("anya", "Капитан Заварзин зарекомендовал себя с лучшей стороны.",
     "Captain Zavarzin has proven himself in the best light.",
     [(684, "Капитан Заварзин"), (685, "зарекомендовал себя с самой лучшей стороны")], ""),
    ("anya", "Имеет безупречный послужной список. Стыдно!",
     "He has an impeccable service record. Shameful!",
     [(686, "Имеет безупречный послужной список"), (689, "Стыдно")], ""),
    ("lyova", "Да я просто выдвинул гипотезу.",
     "I was just putting forward a hypothesis.",
     [(690, "Да я просто выдвинул гипотезу")], ""),
    ("anya", "Ну вот задвиньте её обратно!",
     "Well, push it right back!",
     [(691, "Ну вот задвиньте ее обратно")], ""),
]

WALK = [
    (0, "Товарищ майор, просыпайтесь!",
     "'Comrade Major, wake up!' Zavarzin alerts Major Lavrov from the front seat."),
    (0, "Тут важная новость.",
     "'There is important news here.' The adjective agrees with the feminine noun."),
    (1, "Что случилось?",
     "'What happened?' Lavrov rubs his eyes."),
    (1, "Говорите быстрее.",
     "'Speak more quickly.' The comparative adverb demands brevity."),
    (2, None,
     "'Wait, they gave them a quota for surgery!' Zavarzin shares the wiretap intercept."),
    (3, "Интересно совпало.",
     "'An interesting coincidence.' Literally 'it coincided interestingly'."),
    (3, "Я не верю в такие совпадения.",
     "'I don't believe in such coincidences.' The preposition takes the accusative plural."),
    (4, None,
     "'What if someone took pity on her boy?' Zavarzin wonders if an officer intervened."),
    (5, None,
     "'Comrade Major, look what I was thinking!' Young Lyova pipes up from the back."),
    (6, None,
     "'What if it was he who helped her?' Lyova points his finger directly at Zavarzin."),
    (7, None,
     "'After all, he stood up for her!' Lyova remembers Zavarzin defending Marina from the debt collectors."),
    (8, None,
     "'Lieutenant Sokolov, what are you thinking with?' Major Lavrov scolds him for the absurd accusation."),
    (9, None,
     "'Captain Zavarzin has proven himself in the best light.' Lavrov defends his senior agent."),
    (10, "Имеет безупречный послужной список.",
     "'He has an impeccable service record.' The masculine accusative adjective describes the record."),
    (10, "Стыдно!",
     "'Shameful!' Lavrov is embarrassed by his nephew's clumsy detective work."),
    (11, None,
     "'I was just putting forward a hypothesis.' Lyova tries to defend his theory."),
    (12, None,
     "'Well, push it right back!' Lavrov puts an end to the ridiculous suspicion firmly."),
]

TRANSITION = "Let's listen to the FSB surveillance van conversation once again."

OUTRO = (
    "Dismissing Lyova's wild theory, Lavrov and Zavarzin return to monitoring the wiretaps. "
    "That concludes our five-scene block for Episode 8."
)

CLOSING = ("anya", "Ну вот задвиньте её обратно!")
