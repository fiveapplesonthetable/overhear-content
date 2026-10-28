ID = "kukhnya-s04e17-scene-06"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 17
SCENE = 6
TITLE = "Урок игры на рояле  (The Piano Lesson)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Денис", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S4.17"
SOURCE_FILE = "sources/kukhnya/s04/e17.ru.srt"
SOURCE_NOTE = "Restaurant owner Dmitry Nagiyev summons Denis to the grand piano and orders him to teach him a romantic piece by the day after tomorrow to impress a female pianist."

INTRO = "Restaurant owner Dmitry Nagiyev calls young cook and musician Denis over to the grand piano in the dining room. Nagiyev has a romantic date with a professional pianist in two days and demands that Denis teach him to play like a virtuoso immediately. Let's listen to Nagiyev's ultimatum in Russian."

STORY = [
    ("anya", "Дмитрий Владимирович, вы меня звали?", "Dmitry Vladimirovich, did you call for me?", [(69, 'Звали')], "adapted"),
    ("nagiyev", "Обожаю я всю эту музыку.", "I adore all this music.", [(69, 'Обожаю я вот это все'), (70, 'Обожаю')], "adapted"),
    ("nagiyev", "Только играть совсем не умею.", "Only I do not know how to play at all.", [(70, 'Не умею только')], "adapted"),
    ("nagiyev", "Раньше умел, но уже забыл.", "I used to know how, but I already forgot.", [(71, 'умел, забыл')], "adapted"),
    ("nagiyev", "Ты можешь меня быстро научить?", "Can you teach me quickly?", [(72, 'Можешь меня научить')], "adapted"),
    ("anya", "Ну, теоретически месяца за четыре.", "Well, theoretically in about four months.", [(74, 'Ну, теоретически, месяца за четыре')], "adapted"),
    ("nagiyev", "Мне нужно уже послезавтра вечером.", "I need it by the evening after tomorrow.", [(75, 'Да послезавтра')], "adapted"),
    ("nagiyev", "У меня свидание с одной пианисткой.", "I have a date with a certain pianist.", [(77, 'С одной пианисткой')], "adapted"),
    ("anya", "Может, вам лучше репетитора нанять?", "Maybe you should hire a tutor instead?", [(79, 'Может, вам репетитора нанять')], "adapted"),
    ("nagiyev", "А у тебя просто выбора нет.", "Well, you simply have no choice.", [(81, 'А у тебя выбора нет')], "adapted"),
    ("nagiyev", "Либо ты меня сейчас научишь.", "Either you will teach me right now.", [(82, 'Либо ты меня научишь')], "adapted"),
    ("anya", "Хорошо, гамму я уже уловил.", "All right, I already caught the scale.", [(84, 'Гамму уловил')], "adapted"),
]

OPENER = "Let's break down Nagiyev's piano request and Denis's response line by line."

WALK = [
    (0, None, "'Dmitry Vladimirovich, did you call for me?' Denis addresses the restaurant owner respectfully with a plural past-tense verb."),
    (1, None, "'I adore all this music.' Nagiyev gestures at the grand piano using an expressive first-person present verb meaning to adore."),
    (2, None, "'Only I do not know how to play at all.' In Russian, a dedicated modal verb expresses knowing how to perform a learned skill."),
    (3, None, "'I used to know how, but I already forgot.' He saves face by contrasting an imperfective past verb of ability with a perfective past verb of forgetting."),
    (4, None, "'Can you teach me quickly?' The perfective infinitive for teaching takes an accusative personal pronoun for the student."),
    (5, None, "'Well, theoretically in about four months.' Placing the noun for month before the preposition expresses an approximate four-month time period."),
    (6, None, "'I need it by the evening after tomorrow.' Nagiyev demands an impossible deadline using a single compound temporal adverb for the day after tomorrow."),
    (7, None, "'I have a date with a certain pianist.' The preposition for 'with' governs an instrumental feminine singular noun phrase."),
    (8, None, "'Maybe you should hire a tutor instead?' Denis suggests hiring a private teacher using an animate accusative noun and perfective infinitive."),
    (9, None, "'Well, you simply have no choice.' The negative existential predicate requires the genitive singular form of the noun for choice."),
    (10, None, "'Either you will teach me right now.' Nagiyev issues an ultimatum starting with a disjunctive conjunction meaning either."),
    (11, None, "'All right, I already caught the scale.' Denis surrenders immediately using a colloquial past verb meaning to grasp the tune."),
]

TRANSITION = "Let's hear their conversation by the piano again without interruption."
OUTRO = "Left with the choice of teaching Nagiyev the piano or sweeping the train station, Denis immediately sits down at the keys. Notice how Russian expresses 'either' with a disjunctive conjunction. See you in the next scene."
CLOSING = ("anya", "Гамму я уже уловил.")
CLOSING_TRANS = "I already caught the scale."
