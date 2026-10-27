ID = "domashniy-arest-s01e09-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 3
TITLE = "Ты сам всё проиграл  (You Blew It All Yourself)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "viktor": "anja"}
LABELS = {"anya": "Паша", "viktor": "Виктор Степанович"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 22-53. Acting mayor Pasha Osipenko begs seasoned party official Viktor Stepanovich for help "
    "stopping Samsonov's surging campaign. The official demands three million rubles, which broke Pasha cannot afford. "
    "Crude obscenities in cues 22 ('просрал'), 23 ('Че'), 29 ('нафига'), and 47 ('хрена') are cleaned up for A1 retelling."
)

INTRO = (
    "In our last scene, the satirical opening theme song mocked the relentless greed and bribery of provincial politics. "
    "Now acting mayor Pasha Osipenko visits veteran party boss Viktor Stepanovich to plead for help against Ivan Samsonov, "
    "only to discover that political salvation carries a hefty price tag he can no longer afford. "
    "Let's listen to the scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("viktor", "Ты же сам всё проиграл!",
     "You lost everything yourself!",
     [(22, "Ты же сам все")], "crude просрал softened to проиграл"),
    ("viktor", "Что ты теперь от меня хочешь?",
     "What do you want from me now?",
     [(23, "теперь от меня-то хочешь")], ""),
    ("anya", "Виктор Степанович, помогите мне!",
     "Viktor Stepanovich, please help me!",
     [(24, "помогите")], "ASR garble Сарсифов restored"),
    ("viktor", "Как я могу тебе помочь?",
     "How can I help you?",
     [(25, "как я тебе помогу")], ""),
    ("viktor", "Твой Самсонов прёт как танк!",
     "Your Samsonov is charging ahead like a tank!",
     [(26, "Твой Самсонов прет как танк")], ""),
    ("anya", "Вы же опытный политик.",
     "You are an experienced politician, after all.",
     [(27, "но вы же опытный политик")], ""),
    ("anya", "Вы придумайте что-нибудь, пожалуйста.",
     "Think of something, please.",
     [(28, "Вы придумайте что-нибудь")], ""),
    ("viktor", "А зачем мне это надо, Паша?",
     "And why do I need this, Pasha?",
     [(29, "мне все это надо, Паша")], "crude нафига cleaned to зачем"),
    ("viktor", "В Москве считают, что Самсонов — хороший вариант.",
     "In Moscow they think Samsonov is a good option.",
     [(30, "В Москве"), (31, "хороший вариант")], ""),
    ("anya", "Нет, он ужасный вариант! Помогите!",
     "No, he is a terrible option! Help!",
     [(32, "Нет, не хороший вариант"), (33, "Ну пожалуйста")], ""),
    ("viktor", "Ладно. Три миллиона.",
     "Alright. Three million.",
     [(34, "Ну ладно"), (35, "Три")], "'миллиона' added for clarity"),
    ("anya", "У меня сейчас нет таких денег.",
     "I don't have that kind of money right now.",
     [(38, "У меня сейчас нету")], ""),
    ("viktor", "Паша, ты церковь или детский дом?",
     "Pasha, are you a church or an orphanage?",
     [(40, "Паша, ты церковь"), (42, "Ты детский дом")], ""),
    ("viktor", "Почему я должен помогать бесплатно?",
     "Why should I help you for free?",
     [(47, "я тебе должен помогать бесплатно")], "crude хрена omitted"),
]

OPENER = (
    "Now let's examine the tense negotiation between the two corrupt politicians line by line. "
    "Pasha leans forward anxiously over the senior official's mahogany desk."
)

WALK = [
    (0, None,
     "'You lost everything yourself!' The emphatic pronoun stresses personal responsibility for the election disaster."),
    (1, None,
     "'What do you want from me now?' Notice the genitive personal pronoun following the preposition for 'from'."),
    (2, None,
     "'Viktor Stepanovich, please help me!' Pasha pleads using the patronymic and polite imperative."),
    (3, None,
     "'How can I help you?' Viktor Stepanovich responds skeptically with the modal verb 'can'."),
    (4, None,
     "'Your Samsonov is charging ahead like a tank!' Colloquial verb describing relentless, stubborn momentum."),
    (5, None,
     "'You are an experienced politician, after all.' Pasha flatters the senior official with an appreciative adjective."),
    (6, None,
     "'Think of something, please.' The indefinite pronoun means 'something or other'."),
    (7, None,
     "'And why do I need this, Pasha?' The interrogative adverb asks about the purpose or personal benefit."),
    (8, None,
     "'In Moscow they think Samsonov is a good option.' The third-person plural verb indicates a general prevailing opinion."),
    (9, None,
     "'No, he is a terrible option! Help!' Pasha urgently rejects the idea that his rival could be accepted."),
    (10, None,
     "'Alright. Three million.' The senior official names his price with blunt brevity."),
    (11, None,
     "'I don't have that kind of money right now.' The negative genitive construction expresses complete lack of funds."),
    (12, None,
     "'Pasha, are you a church or an orphanage?' Viktor Stepanovich sarcastically asks if Pasha is a registered charity."),
    (13, None,
     "'Why should I help you for free?' The adverb means 'for free' or 'without payment'."),
]

TRANSITION = "Now let's listen to the political negotiation in the office again without interruption."
OUTRO = (
    "Refusing to help for free, Viktor Stepanovich leaves Pasha completely on his own. "
    "Next we'll join Samsonov as he seeks domestic advice from Arkady in the communal flat; see you there."
)
CLOSING = ("viktor", "Почему я должен помогать бесплатно?")
