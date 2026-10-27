ID = "kukhnya-s01e02-scene-14"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 14
TITLE = "Пропажа коньяка  (The Missing Cognac)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (The Kitchen) S1.2"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = (
    "Bartender Kostya rushes over to the bar counter after being called by Vika, finding her thoroughly unimpressed. "
    "Demanding to know why an unsupervised stranger was left behind the bar, Vika notices an expensive bottle missing. "
    "Let's listen to their confrontation in Russian."
)

STORY = [
    ("kostya", "Да, Виктория Сергеевна, вы звали меня?",
     "Yes, Viktoria Sergeyevna, did you call me?",
     [(187, "Да Виктория Сергеевна")], "reporting to manager"),
    ("anya", "Костя, объясни, что за беспорядок в баре?",
     "Kostya, explain what this mess in the bar is?",
     [(187, "Костя это что нормально"), (188, "Почему у тебя бардак")], "demanding explanation"),
    ("kostya", "Здесь нет никакого страшного беспорядка.",
     "There is no terrible mess here.",
     [(187, "это что нормально")], "minimizing issue"),
    ("anya", "Почему чужой человек стоял за барной стойкой?",
     "Why was a strange man standing behind the bar counter?",
     [(188, "сторонние в баре")], "questioning stranger"),
    ("kostya", "Он специалист и чинил нашу электронную кассу.",
     "He is a specialist and was fixing our electronic register.",
     [(189, "он это Сикипер чинил")], "explaining technician"),
    ("anya", "Ты оставил незнакомца совсем одного без присмотра?",
     "You left a stranger completely alone without supervision?",
     [(188, "сторонние в баре")], "scolding negligence"),
    ("kostya", "Я отошёл на кухню буквально на минуту.",
     "I stepped away to the kitchen for literally a minute.",
     [(189, "чинил")], "justifying absence"),
    ("anya", "А теперь внимательно посмотри на эту полку.",
     "And now look carefully at this shelf.",
     [(191, "Где тогда коньяк")], "directing attention"),
    ("kostya", "Я не вижу здесь ничего необычного.",
     "I see nothing unusual here.",
     [(190, "Да")], "looking around"),
    ("anya", "Где тогда стоит наш дорогой коньяк?",
     "Where then is our expensive cognac standing?",
     [(191, "Где тогда коньяк")], "pointing out absence"),
    ("kostya", "Этот коньяк всегда стоял прямо здесь.",
     "This cognac always stood right here.",
     [(191, "Где тогда коньяк")], "noticing empty spot"),
    ("anya", "Бутылки больше нет на своём месте.",
     "The bottle is no longer in its place.",
     [(191, "Где тогда коньяк")], "confirming disappearance"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the past tense verbs of action and the negative constructions."
)

WALK = [
    (0, "Да, Виктория Сергеевна, вы звали меня?",
     "'Yes, Viktoria Sergeyevna, did you call me?' Affirmative particle with a polite vocative name and patronymic followed by a past question."),
    (1, "Костя, объясни, что за беспорядок в баре?",
     "'Kostya, explain what this mess in the bar is?' Vocative name with an imperative verb governing a colloquial interrogative phrase of surprise."),
    (2, "Здесь нет никакого страшного беспорядка.",
     "'There is no terrible mess here.' Locative adverb with a negative existential impersonal predicate governing genitive case."),
    (3, "Почему чужой человек стоял за барной стойкой?",
     "'Why was a strange man standing behind the bar counter?' Interrogative adverb of reason governing a past verb and instrumental prepositional phrase."),
    (4, "Он специалист и чинил нашу электронную кассу.",
     "'He is a specialist and was fixing our electronic register.' Nominal predicate coordinated with a past transitive verb governing an accusative object."),
    (5, "Ты оставил незнакомца совсем одного без присмотра?",
     "'You left a stranger completely alone without supervision?' Past perfective verb governing an animate accusative noun and genitive prepositional phrase."),
    (6, "Я отошёл на кухню буквально на минуту.",
     "'I stepped away to the kitchen for literally a minute.' Past verb of motion governing directional and temporal prepositional phrases."),
    (7, "А теперь внимательно посмотри на эту полку.",
     "'And now look carefully at this shelf.' Temporal adverb with manner adverb governing a directional imperative verb phrase."),
    (8, "Я не вижу здесь ничего необычного.",
     "'I see nothing unusual here.' Negated present transitive verb governing a negative pronoun and genitive adjective."),
    (9, "Где тогда стоит наш дорогой коньяк?",
     "'Where then is our expensive cognac standing?' Interrogative spatial question governing an intransitive present verb and subject phrase."),
    (10, "Этот коньяк всегда стоял прямо здесь.",
     "'This cognac always stood right here.' Demonstrative subject phrase with frequency adverb and past verb of location."),
    (11, "Бутылки больше нет на своём месте.",
     "'The bottle is no longer in its place.' Genitive subject of a negative existential sentence with a prepositional locative phrase."),
]

TRANSITION = "Now let's listen to the entire dialogue once more at normal speed."

OUTRO = (
    "Vika points out the empty shelf where the expensive cognac used to be, leaving Kostya in deep trouble. "
    "Wonderful work practicing situational Russian dialogue!"
)

CLOSING = ("anya", "Бутылки больше нет на своём месте.")
