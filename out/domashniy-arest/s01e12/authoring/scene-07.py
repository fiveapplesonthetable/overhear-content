ID = "domashniy-arest-s01e12-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 7
TITLE = "Машина Фронтера  (The Frontera Car)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "officer": "anja"}
LABELS = {"anya": "Самсон", "officer": "Таможенник"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 128-133. Samson stops at a checkpoint with his imported Opel Frontera. "
    "The customs officer inspects the car and papers, approving the reliable vehicle, "
    "while Samson politely asks to pass quickly because he is in a hurry."
)

INTRO = (
    "In this scene, Samson arrives at a highway checkpoint driving an imported foreign SUV. "
    "The customs officer asks about the vehicle's model year and admires its build quality. "
    "Explaining that he is pressed for time, Samson asks to be let through promptly. "
    "Let's listen to their brief exchange in Russian first."
)

STORY = [
    ("officer", "Здравствуйте, покажите ваши документы на машину.",
     "Hello, show your documents for the car.",
     [], ""),
    ("anya", "Пожалуйста, вот все нужные бумаги.",
     "Please, here are all the necessary papers.",
     [], ""),
    ("officer", "Скажите, какого года эта Фронтера?",
     "Tell me, what year is this Frontera?",
     [(128, "Какого года Фронтера")], ""),
    ("anya", "Эта машина две тысячи восьмого года.",
     "This car is from the year 2008.",
     [(129, "Восьмого")], ""),
    ("officer", "Да, это действительно очень хорошая машина.",
     "Yes, this is truly a very good car.",
     [(130, "Хорошая машина")], ""),
    ("anya", "Мы пригоняем только самые надёжные автомобили.",
     "We bring in only the most reliable cars.",
     [], ""),
    ("officer", "Куда вы сейчас направляетесь на ней?",
     "Where are you heading in it now?",
     [], ""),
    ("anya", "Мы сейчас спешим в город Синеозёрск.",
     "We are hurrying to the town of Sineozersk now.",
     [], ""),
    ("anya", "Слышишь, братан, пропусти нас скорее вперёд.",
     "Listen, bro, let us through forward quickly.",
     [(131, "Слышь, братан")], ""),
    ("anya", "Мы очень сильно торопимся по делам.",
     "We are in a very big hurry on business.",
     [(131, "торопимся")], ""),
    ("officer", "Хорошо, с документами всё в порядке.",
     "Alright, everything is in order with the documents.",
     [], ""),
    ("anya", "Большое спасибо за вашу быструю помощь!",
     "Thank you very much for your quick help!",
     [(132, "Спасибо")], ""),
    ("officer", "Давай, счастливого пути и хорошей дороги!",
     "Go ahead, safe travels and have a good road!",
     [(133, "Давай")], ""),
    ("anya", "Спасибо, друг, мы поехали дальше!",
     "Thanks, friend, we drove on further!",
     [], ""),
]

OPENER = (
    "Now let's examine Samson's border check line by line. "
    "Notice the conversational car vocabulary and polite road etiquette."
)

WALK = [
    (0, None,
     "'Hello, show your documents for the car.' The imperative verb governs an accusative prepositional phrase."),
    (1, None,
     "'Please, here are all the necessary papers.' The particle introduces a nominative noun phrase with a qualifying adjective."),
    (2, None,
     "'Tell me, what year is this Frontera?' The interrogative genitive phrase inquires about the manufacture date."),
    (3, None,
     "'This car is from the year 2008.' The ordinal numeral is declined in the genitive case after 'goda'."),
    (4, None,
     "'Yes, this is truly a very good car.' The adverb of manner emphasizes the positive evaluation."),
    (5, None,
     "'We bring in only the most reliable cars.' The superlative adjective phrase describes the imported vehicles."),
    (6, None,
     "'Where are you heading in it now?' The interrogative adverb introduces a reflexive motion verb."),
    (7, None,
     "'We are hurrying to the town of Sineozersk now.' The present tense verb of motion takes a prepositional accusative destination."),
    (8, None,
     "'Listen, bro, let us through forward quickly.' Samson uses a familiar colloquial address with an imperative verb."),
    (9, None,
     "'We are in a very big hurry on business.' The adverbial phrase explains the urgent need for fast passage."),
    (10, None,
     "'Alright, everything is in order with the documents.' The prepositional idiom confirms valid official paperwork."),
    (11, None,
     "'Thank you very much for your quick help!' The courtesy formula governs an accusative prepositional phrase."),
    (12, None,
     "'Go ahead, safe travels and have a good road!' The officer uses a traditional Russian travel blessing in the genitive."),
    (13, None,
     "'Thanks, friend, we drove on further!' Samson announces departure using a past tense verb of setting off."),
]

TRANSITION = "Now let's listen to Samson and the customs officer's conversation once more without pauses."
OUTRO = (
    "Clearing the checkpoint without delay, Samson continues his journey toward the transit airfield. "
    "In the next scene, an unexpected reunion awaits him in the terminal."
)
CLOSING = ("officer", "Давай, счастливого пути и хорошей дороги!")
