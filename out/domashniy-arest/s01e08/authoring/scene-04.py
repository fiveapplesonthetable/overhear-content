ID = "domashniy-arest-s01e08-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 4
TITLE = "Квоты на этот год закончились  (Quotas for This Year Are Gone)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "doctor": "anja", "lyosha": "angelina"}
LABELS = {"anya": "Марина", "doctor": "Доктор", "lyosha": "Лёша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 62-79. Marina and young Lyosha visit the orthopedic surgeon at the clinic. "
    "Garbled ASR in cues 69 ('общих' -> 'вообще') and 73 ('оплатную' -> 'платную') are restored to standard Russian. "
    "Abbreviation 'Минздрав' in cue 74 is replaced with 'Государство' to comply with the rule against abbreviations in spoken lines."
)

INTRO = (
    "In our last scene, Nina and Ilona searched the town for missing candidate Ivan Samsonov after the smear video aired. "
    "Meanwhile at the municipal pediatric clinic, Marina Sergeyevna meets with an orthopedic doctor about an urgent "
    "surgery quota for her son Lyosha, whose leg condition is rapidly getting worse. "
    "Let's hear the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("doctor", "Давайте я запишу вас на следующий год.",
     "Let me schedule you for next year.",
     [(62, "я вас запишу на"), (62, "следующего года")], ""),
    ("anya", "Как на следующий год? Почему?",
     "What do you mean, next year? Why?",
     [(63, "Как в следующем году")], "'Почему' added"),
    ("doctor", "В этом году все квоты выбрали.",
     "This year all the quotas have been used up.",
     [(64, "в этом году все квоты выбрали")], ""),
    ("doctor", "А в следующем году вы будете первой.",
     "And next year you will be first on the list.",
     [(66, "А в следующем году вы первая")], ""),
    ("anya", "Подождите! Но ему наступать стало больнее.",
     "Wait! But it has become more painful for him to step.",
     [(67, "Подождите. Но ему наступать стало больнее")], ""),
    ("anya", "Значит, болезнь прогрессирует!",
     "That means the disease is progressing!",
     [(68, "Значит, болезнь прогрессирует")], ""),
    ("anya", "А если он вообще ходить не сможет?",
     "And what if he can't walk at all?",
     [(69, "А если он"), (69, "ходить не сможет")], "cue 69 ASR 'общих' restored to 'вообще'"),
    ("doctor", "Я вас понимаю. Но я не распределяю квоты.",
     "I understand you. But I do not allocate the quotas.",
     [(70, "Вас понимаю"), (71, "не я эти квоты распределяю")], ""),
    ("doctor", "Пойдите в банк. Возьмите кредит на платную операцию.",
     "Go to a bank. Take out a loan for a paid surgery.",
     [(72, "пойдите в банк"), (73, "Возьмите кредит на"), (73, "операцию")], "cue 73 'оплатную' -> 'платную'"),
    ("doctor", "Государство вам потом вернёт деньги.",
     "The state will reimburse you the money later.",
     [(74, "вам потом вернет")], "abbreviation Минздрав replaced with 'Государство'"),
    ("anya", "Я безработная! Мне не одобрят никакой кредит.",
     "I am unemployed! They will not approve any loan for me.",
     [(75, "Я безработная. Мне не одобрят кредит")], ""),
    ("doctor", "Я вам искренне сочувствую, но мне пора работать.",
     "I sincerely feel for you, but it is time for me to work.",
     [(76, "Я вам, правда, искренне сочувствую"), (77, "мне работать надо")], ""),
    ("lyosha", "Мама, а операция будет очень дорогая?",
     "Mama, will the surgery be very expensive?",
     [], "added for child role presence"),
    ("anya", "Малыш, ты не переживай!",
     "Sweetie, don't worry!",
     [(78, "Малыш, ты не переживай")], ""),
    ("anya", "Государство обязательно увидит и назначит операцию.",
     "The state will surely see and will schedule the surgery.",
     [(79, "Государство обязательно увидит"), (79, "и назначит тебе операцию")], ""),
]

OPENER = (
    "Now let's examine the conversation in the doctor's office line by line. "
    "The orthopedic surgeon looks at Lyosha's medical file."
)

WALK = [
    (0, None,
     "'Let me schedule you for next year.' The doctor uses an imperative construction meaning 'let me write you down'."),
    (1, None,
     "'What do you mean, next year? Why?' Marina is stunned by the delay and asks for an explanation."),
    (2, None,
     "'This year all the quotas have been used up.' Notice the past plural verb meaning 'chose' or 'used up'."),
    (3, None,
     "'And next year you will be first on the list.' The ordinal numeral is in the feminine instrumental case."),
    (4, None,
     "'Wait! But it has become more painful for him to step.' The comparative adverb describes the worsening pain."),
    (5, None,
     "'That means the disease is progressing!' The feminine noun for 'disease' is the grammatical subject."),
    (6, None,
     "'And what if he can't walk at all?' The adverb means 'at all' or 'in general'."),
    (7, None,
     "'I understand you. But I do not allocate the quotas.' The doctor explains that administrative decisions are out of his hands."),
    (8, None,
     "'Go to a bank. Take out a loan for a paid surgery.' Both verbs are in the polite plural imperative form."),
    (9, None,
     "'The state will reimburse you the money later.' The perfective future verb means 'will return' or 'will reimburse'."),
    (10, None,
     "'I am unemployed! They will not approve any loan for me.' Marina reminds him that she was fired from the university."),
    (11, None,
     "'I sincerely feel for you, but it is time for me to work.' The adverb means 'sincerely' or 'from the heart'."),
    (12, None,
     "'Mama, will the surgery be very expensive?' Lyosha looks up anxiously from his crutches."),
    (13, None,
     "'Sweetie, don't worry!' Marina comforts her son with an affectionate diminutive address."),
    (14, None,
     "'The state will surely see and will schedule the surgery.' Marina tries to keep her son's spirits up despite the bureaucratic wall."),
]

TRANSITION = "Now let's listen to the scene in the clinic again without interruption."
OUTRO = (
    "Bureaucracy has left Lyosha without a quota, and Marina cannot afford a private clinic. "
    "Next we'll see Lyosha in the corridor asking about his broken toy tank; see you there."
)
CLOSING = ("anya", "Малыш, ты не переживай!")
