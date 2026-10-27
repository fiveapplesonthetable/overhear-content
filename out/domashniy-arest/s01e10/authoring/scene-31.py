"""s01e10 scene 31: Первое место для барашка (craft contest)."""

ID = "domashniy-arest-s01e10-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 31
TITLE = "Первое место для барашка  (First Place for the Lamb)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "teacher": "angelina", "lyosha": "anja"}
LABELS = {"anya": "Марина", "teacher": "Учительница", "lyosha": "Лёша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 960-998 (00:53:20-00:54:57). At the children's clay craft contest, the teacher awards first place "
    "to young Lyosha for his upside-down lamb. Marina proudly congratulates her son and thanks the teacher, "
    "then calls Arkady inviting him home early for a celebration dinner."
)

INTRO = (
    "At the local community center, parents gather to hear the results of the children's annual clay modeling competition. "
    "To Marina's immense delight, young Lyosha takes first prize with his imaginative animal sculpture. "
    "Ecstatic over her son's triumph, Marina decides to prepare a special celebratory dinner at the apartment. "
    "Let's listen to the award ceremony in Russian first; don't worry about catching every word."
)

STORY = [
    ("teacher", "Итак, у нас конкурс детских поделок.",
     "And so, we have a children's craft contest.",
     [(960, "Итак")], "expanded cue 960"),
    ("teacher", "На третьем месте Света Копылова.",
     "In third place is Sveta Kopylova.",
     [(961, "на третьем месте"), (962, "Света Копылова")], "combined cues 961-962"),
    ("teacher", "На втором месте Вова Петухов.",
     "In second place is Vova Petukhov.",
     [(964, "На втором месте"), (965, "Вова Петухов")], "combined cues 964-965"),
    ("teacher", "А первое место у Алексея Былинкина!",
     "And first place goes to Alexei Bylinkin!",
     [(967, "А на первом месте"), (969, "у Алексея Былинкина")], "combined cues 967 and 969"),
    ("teacher", "Лёша, напомни нам, что это?",
     "Lyosha, remind us, what is this?",
     [(971, "Напомни, что это")], "adapted cue 971 with yo"),
    ("lyosha", "Это барашек. Надо перевернуть работу.",
     "This is a lamb. You have to flip the work.",
     [(972, "Барашек"), (973, "Просто перевернуть надо")], "combined cues 972-973"),
    ("teacher", "Прекрасно! Аплодисменты нашему победителю!",
     "Wonderful! Applause for our winner!",
     [(974, "Аплодисменты")], "expanded cue 974"),
    ("teacher", "Возьмите свои работы и подарите родителям.",
     "Take your works and give them to parents.",
     [(976, "возьмите свои работы"), (977, "и подарите родителям")], "combined cues 976-977"),
    ("lyosha", "Мама, смотри! Я занял первое место!",
     "Mama, look! I took first place!",
     [(982, "Мама")], "expanded cue 982"),
    ("anya", "Лёшка, милый, я тебя поздравляю!",
     "Lyoshka, sweetie, I congratulate you!",
     [(985, "Лешка, я тебя поздравляю")], "verbatim cue 985 with yo"),
    ("anya", "Спасибо вам за честное судейство.",
     "Thank you for the fair judging.",
     [(988, "Спасибо вам"), (989, "за объективное судейство")], "simplified cue 989"),
    ("teacher", "Поздравляю. До свидания вам.",
     "Congratulations. Goodbye to you.",
     [(984, "До свидания")], "expanded cue 984"),
    ("anya", "Она очень странно на нас посмотрела.",
     "She looked at us very strangely.",
     [(991, "Странная такая")], "expanded cue 991"),
    ("anya", "Приходи сегодня домой пораньше, Аркадий.",
     "Come home early today, Arkady.",
     [(996, "приходи сегодня домой пораньше")], "adapted cue 996"),
    ("anya", "Тебя ждёт очень вкусный ужин.",
     "A very tasty dinner is waiting for you.",
     [(997, "тебя ждет вкусный ужин")], "verbatim cue 997 with yo"),
]

OPENER = "Let us walk through this joyful school award ceremony step by step to explore each phrase."

WALK = [
    (0, None,
     "'And so, we have a children's craft contest.' The introductory particle introduces the official results."),
    (1, None,
     "'In third place is Sveta Kopylova.' The preposition with the prepositional case indicates rank or placement."),
    (2, None,
     "'In second place is Vova Petukhov.' Ordinal numerals decline like regular qualitative adjectives in Russian."),
    (3, None,
     "'And first place goes to Alexei Bylinkin!' The preposition with the genitive indicates possession of the title."),
    (4, None,
     "'Lyosha, remind us, what is this?' The imperative verb takes the dative pronoun for the recipient."),
    (5, None,
     "'This is a lamb. You have to flip the work.' The predicative word expresses necessity with an infinitive."),
    (6, None,
     "'Wonderful! Applause for our winner!' The dative case indicates the recipient of the audience applause."),
    (7, None,
     "'Take your works and give them to parents.' Plural imperative forms direct all the participating children."),
    (8, None,
     "'Mama, look! I took first place!' The past tense masculine verb describes achieving a winning rank."),
    (9, None,
     "'Lyoshka, sweetie, I congratulate you!' The verb of congratulation governs the accusative case of the person."),
    (10, None,
     "'Thank you for the fair judging.' The preposition meaning 'for' governs the accusative neuter noun phrase."),
    (11, None,
     "'Congratulations. Goodbye to you.' Polite standard formulas conclude the school event."),
    (12, None,
     "'She looked at us very strangely.' The adverbial manner modifier describes the teacher's odd glance."),
    (13, None,
     "'Come home early today, Arkady.' The comparative adverb denotes an earlier time than usual."),
    (14, None,
     "'A very tasty dinner is waiting for you.' The transitive verb governs the accusative pronoun form."),
]

TRANSITION = "Now let us listen to the complete ceremony once more, from the award announcements to the warm phone call."
OUTRO = ("Young Lyosha proudly holds his winning clay lamb as Marina plans a wonderful evening at home. "
         "Excellent work mastering these school contest and family phrases in Russian.")
CLOSING = ("lyosha", "Мама, смотри!")
