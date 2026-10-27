# -*- coding: utf-8 -*-
"""Scene 28 of domashniy-arest s01e08: Medical Diagnosis."""

ID = "domashniy-arest-s01e08-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 28
TITLE = "Диагноз доктора  (Medical Diagnosis)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "doctor": "anja",
    "lyosha": "angelina",
}

LABELS = {
    "anya": "Аркадий",
    "doctor": "Доктор Тенинбаум",
    "lyosha": "Лёша",
}

INTRO = (
    "After Samsonov's friends refused to back him at the debates, we return to the communal "
    "flat. In Arkady's room, young Lyosha sits by the laptop while a foreign specialist, "
    "Dr. Tenenbaum, examines the boy over a video call. Listen to the Russian conversation "
    "first, and do not worry about catching every word."
)

OPENER = "Let's follow the online medical consultation line by line."

STORY = [
    ("doctor", "Доктор Тенинбаум слушает. Что случилось?",
     "Doctor Tenenbaum is listening. What happened?",
     [(531, "Доктор"), (539, "Что случилось")], ""),
    ("anya", "Яков Григорьевич, у меня срочный вопрос к вам.",
     "Yakov Grigoryevich, I have an urgent question for you.",
     [(538, "Яков Григорьевич, у меня срочный вопрос к вам")], ""),
    ("anya", "Здесь мальчик, Лёха. Поговорите с ним.",
     "There is a boy here, Lyokha. Speak with him.",
     [(544, "здесь пацан есть, Леха"), (545, "иди сюда")], ""),
    ("lyosha", "Здравствуйте, доктор. У меня остеохондропатия.",
     "Hello, doctor. I have osteochondropathy.",
     [(549, "У меня")], "ASR 'осё хондропатия' restored to 'остеохондропатия'"),
    ("doctor", "Ну и как тебя лечат?",
     "So how are they treating you?",
     [(551, "Ну и как тебя лечат")], ""),
    ("lyosha", "Мне назначили операцию.",
     "They scheduled surgery for me.",
     [(552, "назначило мне операцию")], ""),
    ("doctor", "Скажи мне, мальчик. Тебя когда-нибудь клещ кусал?",
     "Tell me, boy. Did a tick ever bite you?",
     [(563, "Скажи-ка мне, мальчик, тебя когда-нибудь клещ кусал")], ""),
    ("lyosha", "Да, год назад. Потом всё прошло.",
     "Yes, a year ago. Then everything went away.",
     [(564, "Год назад"), (568, "Потом прошло")], ""),
    ("doctor", "Ну что ж, беги, мальчик! Аркаша, слушай меня.",
     "Well then, run along, boy! Arkasha, listen to me.",
     [(570, "Ну что ж, беги, мальчик, беги"), (573, "Аркаша, слушай меня")], ""),
    ("doctor", "У этого мальчика нет никакой остеохондропатии.",
     "This boy has no osteochondropathy at all.",
     [(575, "У этого мальчика нет никакой остеохондропатии")], ""),
    ("doctor", "У него боррелиоз от укуса клеща!",
     "He has Lyme disease from a tick bite!",
     [(576, "у него боррелиоз"), (577, "Боррелиоз от укуса клеща")], ""),
    ("doctor", "И операция ему не нужна.",
     "And he does not need surgery.",
     [(579, "И операция ему не нужна")], ""),
    ("doctor", "Это заболевание лечится медикаментозно.",
     "This condition is treated with medication.",
     [(580, "Это заболевание лечится медикаментозно")], ""),
    ("anya", "Спасибо, доктор! Я всё понял.",
     "Thank you, doctor! I understood everything.",
     [], "new closing A1 line"),
]

WALK = [
    (0, "Доктор Тенинбаум слушает.",
     "'Doctor Tenenbaum is listening.' The doctor answers the call from his foreign clinic."),
    (0, "Что случилось?",
     "'What happened?' The past tense neuter question is the standard phrase for 'what's wrong?'."),
    (1, "Яков Григорьевич, у меня срочный вопрос к вам.",
     "'Yakov Grigoryevich, I have an urgent question for you.' Arkady addresses his old physician respectfully."),
    (2, "Здесь мальчик, Лёха.",
     "'There is a boy here, Lyokha.' Lyokha is the informal nickname for Lyosha."),
    (2, "Поговорите с ним.",
     "'Speak with him.' The preposition takes the instrumental pronoun."),
    (3, "Здравствуйте, доктор.",
     "'Hello, doctor.' Lyosha introduces himself politely."),
    (3, "У меня остеохондропатия.",
     "'I have osteochondropathy.' He recites the scary diagnosis from the local hospital."),
    (4, None,
     "'So how are they treating you?' The doctor asks about his current therapy."),
    (5, None,
     "'They scheduled surgery for me.' The third-person neuter verb refers to the state health board."),
    (6, "Скажи мне, мальчик.",
     "'Tell me, boy.' The doctor focuses on specific symptoms."),
    (6, "Тебя когда-нибудь клещ кусал?",
     "'Did a tick ever bite you?' The indefinite adverb means 'ever'."),
    (7, "Да, год назад.",
     "'Yes, a year ago.' The phrase indicates a point in the past."),
    (7, "Потом всё прошло.",
     "'Then everything went away.' The symptoms disappeared temporarily."),
    (8, "Ну что ж, беги, мальчик!",
     "'Well then, run along, boy!' The doctor sends Lyosha out of the room so he can speak privately with Arkady."),
    (8, "Аркаша, слушай меня.",
     "'Arkasha, listen to me.' He addresses Arkady by his familiar diminutive."),
    (9, None,
     "'This boy has no osteochondropathy at all.' The negative construction takes the genitive case."),
    (10, None,
     "'He has Lyme disease from a tick bite!' The doctor identifies the real cause of the boy's joint problems."),
    (11, None,
     "'And he does not need surgery.' The short adjective expresses that surgery is unnecessary."),
    (12, None,
     "'This condition is treated with medication.' A simple course of antibiotics is all Lyosha needs."),
    (13, "Спасибо, доктор!",
     "'Thank you, doctor!' Arkady breathes a huge sigh of relief."),
    (13, "Я всё понял.",
     "'I understood everything.' Now he must stop Marina before the hospital operates."),
]

TRANSITION = "Let's listen to the doctor's diagnosis once again."

OUTRO = (
    "Armed with the revelation that Lyosha only needs antibiotics, Arkady rushes to find "
    "Marina. But at the municipal hospital, Marina is already signing the surgeon's papers."
)

CLOSING = ("anya", "Спасибо, доктор! Я всё понял.")
