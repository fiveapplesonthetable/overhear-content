ID = "domashniy-arest-s01e12-scene-18"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 18
TITLE = "Спецоперация на складе  (Special Operation at the Warehouse)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "viktor": "anja"}
LABELS = {"anya": "Лавров", "viktor": "Виктор Степанович"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"

INTRO = (
    "At an abandoned warehouse outside Sineozersk, FSB Major Lavrov and his tactical team launch a surprise raid. "
    "However, local police under Viktor Stepanovich also arrive on the scene, creating a tense standoff between agencies. "
    "Let's listen to how the two commanders negotiate in Russian."
)

STORY = [
    ("anya", "Внимание, всем оставаться на своих местах!",
     "Attention, everyone remain in your places!",
     [(403, "На полу работает СОБАР"), (408, "Внимание")], "tactical order"),
    ("anya", "Работает специальная группа ФСБ, бросайте оружие!",
     "The FSB special group is operating, drop weapons!",
     [(404, "Работает ФСБ не стреляй"), (405, "оружие на землю")], "warning"),
    ("viktor", "Спокойно, майор, здесь работает областная полиция.",
     "Calmly, major, regional police are operating here.",
     [(413, "в моей области"), (415, "Виктор Степанович")], "intervening"),
    ("anya", "Кто у вас здесь главный командир?",
     "Who is your chief commander here?",
     [(410, "Кто у вас там старше")], "demanding identity"),
    ("viktor", "Говорит генерал-майор полиции Виктор Степанович.",
     "Major General of Police Viktor Stepanovich is speaking.",
     [(402, "товарищ генерал-майор"), (415, "Виктор Степанович")], "identifying himself"),
    ("anya", "Мы проводим здесь секретную операцию.",
     "We are conducting a secret operation here.",
     [(406, "Это операция ФСБ")], "justifying raid"),
    ("viktor", "Вы не должны действовать без моего ведома.",
     "You must not act without my knowledge.",
     [(413, "без моего ведома")], "asserting jurisdiction"),
    ("anya", "Мы ловим опасных коррупционеров уже полгода.",
     "We have been catching dangerous corrupt officials for six months.",
     [(471, "мы полгода всем этим занимались")], "explaining mission"),
    ("viktor", "Давайте спокойно решим эту сложную проблему.",
     "Let us calmly resolve this complex problem.",
     [(460, "давайте решать как быть"), (461, "Ситуация сложная")], "de-escalating"),
    ("anya", "У вас есть конкретные предложения?",
     "Do you have specific proposals?",
     [(462, "давайте так")], "asking plan"),
    ("viktor", "Это будет наша общая совместная операция.",
     "This will be our shared joint operation.",
     [(463, "Это была ваша совместная операция")], "proposing solution"),
    ("anya", "Хорошо, оформляем задержание вместе.",
     "Good, we are documenting the arrest together.",
     [(464, "под четким контролем")], "agreeing"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the formal vocabulary used in official negotiations."
)

WALK = [
    (0, "Внимание, всем оставаться на своих местах!",
     "'Attention, everyone remain in your places!' Interjection demanding attention with an infinitive expressing an imperative command."),
    (1, "Работает специальная группа ФСБ, бросайте оружие!",
     "'The FSB special group is operating, drop weapons!' Present tense verb governing a feminine subject followed by an imperative verb."),
    (2, "Спокойно, майор, здесь работает областная полиция.",
     "'Calmly, major, regional police are operating here.' Adverb of manner with vocative address and a feminine noun phrase."),
    (3, "Кто у вас здесь главный командир?",
     "'Who is your chief commander here?' Interrogative pronoun subject with a prepositional pronoun and masculine nominal predicate."),
    (4, "Говорит генерал-майор полиции Виктор Степанович.",
     "'Major General of Police Viktor Stepanovich is speaking.' Third-person present verb with official rank and patronymic."),
    (5, "Мы проводим здесь секретную операцию.",
     "'We are conducting a secret operation here.' First-person plural verb governing an accusative feminine noun phrase."),
    (6, "Вы не должны действовать без моего ведома.",
     "'You must not act without my knowledge.' Plural modal adjective governing an imperfective infinitive and genitive prepositional phrase."),
    (7, "Мы ловим опасных коррупционеров уже полгода.",
     "'We have been catching dangerous corrupt officials for six months.' Present imperfective verb governing an animate accusative noun phrase."),
    (8, "Давайте спокойно решим эту сложную проблему.",
     "'Let us calmly resolve this complex problem.' Hortative particle governing a perfective future verb and accusative noun phrase."),
    (9, "У вас есть конкретные предложения?",
     "'Do you have specific proposals?' Possessive construction governing plural nominative subject."),
    (10, "Это будет наша общая совместная операция.",
     "'This will be our shared joint operation.' Demonstrative subject with future copula governing a feminine predicate nominative."),
    (11, "Хорошо, оформляем задержание вместе.",
     "'Good, we are documenting the arrest together.' Affirmative adverb with a first-person plural verb and neuter direct object."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at natural speed."

OUTRO = (
    "Major Lavrov and Viktor Stepanovich reach an understanding to conduct a joint operation. "
    "Great work practicing official conversational Russian!"
)

CLOSING = ("anya", "Хорошо, оформляем задержание вместе.")
