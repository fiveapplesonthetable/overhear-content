"""s01e12 scene 27: Министр рыбного хозяйства (Minister of Fisheries)."""

ID = "domashniy-arest-s01e12-scene-27"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 27
TITLE = "Министр рыбного хозяйства  (Minister of Fisheries)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "stepan": "anja",
}
LABELS = {
    "anya": "Губернатор",
    "stepan": "Степаныч",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = "Cues 686-704. Governor Viktor Stepanovich shares the thrilling news with his aide Stepanych and heads out to collect the cash."

INTRO = (
    "Ecstatic after his phone call from Moscow, Governor Viktor Stepanovich hurries to share the grand "
    "news with his loyal aide Stepanych. Visions of wealth and influence fill his mind as he prepares "
    "to collect the funds. Let's listen in Russian first."
)

STORY = [
    ("anya", "Степаныч, я скоро стану федеральным министром!",
     "Stepanych, I will soon become a federal minister!",
     [(686, "Я буду министром.")], ""),

    ("stepan", "Какое именно министерство ты возглавишь?",
     "What ministry specifically will you head?",
     [(687, "Каким?")], ""),

    ("anya", "Министерство рыбного хозяйства всей страны!",
     "The ministry of fisheries of the whole country!",
     [(688, "Рыбного хозяйства.")], ""),

    ("stepan", "Вот это да, настоящая удача!",
     "Well look at that, real good luck!",
     [(691, "Вот это да.")], ""),

    ("stepan", "Такого подарка даже я не ожидал.",
     "Even I did not expect such a gift.",
     [(692, "Такого даже я не ожидал.")], ""),

    ("stepan", "Я от всей души поздравляю тебя.",
     "I congratulate you from all my heart.",
     [(693, "я поздравляю")], ""),

    ("stepan", "Это же настоящее золотое дно!",
     "This is a real gold mine after all!",
     [(693, "это же золотое дно.")], ""),

    ("anya", "Да, это открывает огромные возможности.",
     "Yes, this opens huge opportunities.",
     [(694, "Да.")], ""),

    ("stepan", "Теперь мы решим абсолютно все проблемы.",
     "Now we will solve absolutely all problems.",
     [], ""),

    ("anya", "Сначала надо закончить важное дело.",
     "First one must finish an important matter.",
     [(701, "Сначала надо дела доделать, потом.")], ""),

    ("stepan", "Мы едем прямо сейчас?",
     "Are we going right now?",
     [(702, "Все, поехали.")], ""),

    ("anya", "Да, поехали немедленно в резиденцию.",
     "Yes, let's go to the residence immediately.",
     [(702, "Все, поехали.")], ""),

    ("stepan", "Куда именно мы сейчас направляемся?",
     "Where exactly are we heading right now?",
     [(703, "Куда?")], ""),

    ("anya", "Пора обозначиться перед влиятельными людьми.",
     "It is time to make our move before influential people.",
     [(704, "Обозначаться.")], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the expressions used to celebrate major "
    "promotions and discuss lucrative official positions."
)

WALK = [
    (0, None,
     "'Stepanych, I will soon become a federal minister!' Joyful declaration with temporal adverb, future copular verb, and instrumental title."),
    (1, None,
     "'What ministry specifically will you head?' Interrogative pronoun phrase with second person future transitive verb."),
    (2, None,
     "'The ministry of fisheries of the whole country!' Exclamatory noun phrase governing two successive genitive specifications."),
    (3, None,
     "'Well look at that, real good luck!' Expressive conversational idiom of admiration followed by descriptive nominative noun phrase."),
    (4, None,
     "'Even I did not expect such a gift.' Emphatic particle with negative past transitive verb governing descriptive genitive object."),
    (5, None,
     "'I congratulate you from all my heart.' Idiomatic prepositional expression of sincerity with transitive verb and accusative pronoun."),
    (6, None,
     "'This is a real gold mine after all!' Emphatic particle with descriptive metaphorical predicate noun phrase."),
    (7, None,
     "'Yes, this opens huge opportunities.' Affirmative particle with third person singular present transitive verb and accusative object."),
    (8, None,
     "'Now we will solve absolutely all problems.' Temporal adverb with first person plural future verb and intensified direct object."),
    (9, None,
     "'First one must finish an important matter.' Temporal adverb with modal predicative and perfective infinitive governing accusative."),
    (10, None,
     "'Are we going right now?' Present tense verb of motion with temporal adverbial phrase."),
    (11, None,
     "'Yes, let's go to the residence immediately.' Imperative of motion with manner adverb and prepositional destination."),
    (12, None,
     "'Where exactly are we heading right now?' Interrogative directional phrase with present reflexive verb of motion."),
    (13, None,
     "'It is time to make our move before influential people.' Predicative word with reflexive infinitive and prepositional instrumental phrase."),
]

TRANSITION = "Now let's listen to the governor's excited conversation with Stepanych once again."

OUTRO = (
    "Filled with boundless ambition, Viktor Stepanovich rushes off to collect the cash that will "
    "seal his political future. See you next time!"
)

CLOSING = ("anya", "Степаныч, я скоро стану федеральным министром!")
