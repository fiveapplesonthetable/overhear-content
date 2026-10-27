from pathlib import Path

ID = "kukhnya-s01e10-scene-39"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 39
TITLE = "Поспешное решение  (A Hasty Decision)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")

INTRO = (
    "As Tanya enthusiastically suggests arranging a quick registry appointment and announcing the wedding to the whole dining room, "
    "both Max and Victoria instantly regret their impulsive game of chicken. Admitting they moved too fast, they hastily backtrack. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Мы подадим официальное заявление в загс?",
     "Will we submit an official application to the registry office?",
     [(276, "подадим заявление")], "asking about registration"),
    ("vika", "Таня, у тебя есть знакомые в загсе?",
     "Tanya, do you have acquaintances at the registry office?",
     [(277, "Тань, у тебя есть кто-нибудь")], "asking for connections"),
    ("anya", "Пожалуйста, помоги нам расписаться как можно быстрее.",
     "Please help us sign the register as fast as possible.",
     [(278, "побыстрее расписать")], "requesting urgent ceremony"),
    ("vika", "Давайте расскажем эту новость всем гостям ресторана!",
     "Let's tell this news to all the guests of the restaurant!",
     [(280, "давайте скажем всем"), (281, "Обрадуем")], "suggesting public announcement"),
    ("anya", "Подожди, кажется, я немножко поторопился сейчас.",
     "Wait, it seems I jumped the gun a little now.",
     [(281, "Подожди"), (283, "А я с предложением")], "realizing rush"),
    ("vika", "Честно говоря, я тоже слишком поторопилась с ответом.",
     "To be honest, I also rushed with the answer too much.",
     [(282, "немножко поторопилась с ответом")], "admitting rash answer"),
    ("anya", "Значит, нам обоим нужно хорошенько подумать.",
     "So, both of us need to think carefully.",
     [(283, "Мы немножко подумаем")], "suggesting deliberation"),
    ("vika", "Да, нам лучше немного подождать со свадьбой.",
     "Yes, it is better for us to wait a little with the wedding.",
     [(284, "Да, мы подумаем")], "agreeing to delay"),
    ("anya", "Шеф, вы поможете нам спокойно разобраться?",
     "Chef, will you help us sort this out calmly?",
     [(285, "разбирайтесь сами")], "asking Barinov for advice"),
    ("anya", "Шеф не хочет слушать наши семейные споры.",
     "The chef doesn't want to listen to our family arguments.",
     [(285, "разбирайтесь сами")], "acknowledging Barinov's disinterest"),
    ("vika", "У Виктора сейчас начинается важный футбольный матч.",
     "Viktor has an important football match starting now.",
     [(286, "футбол начинается")], "noting football distraction"),
    ("anya", "Тогда мы сами во всём разберёмся позже.",
     "Then we will sort everything out ourselves later.",
     [(287, "Идите, идите")], "agreeing to postpone"),
    ("vika", "Иди работай, свадьба пока точно подождёт!",
     "Go work, the wedding will definitely wait for now!",
     [(287, "Идите, идите")], "calling off wedding for now"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the panic of hasty commitments, expressions of regret, and comedic retreat from marriage."
)

WALK = [
    (0, "Мы подадим официальное заявление в загс?",
     "'Will we submit an official application to the registry office?' Subject pronoun with future verb, accusative adjective-noun phrase, and locative prepositional noun."),
    (1, "Таня, у тебя есть знакомые в загсе?",
     "'Tanya, do you have acquaintances at the registry office?' Vocative address with locative pronoun, present verb, nominative plural noun, and locative prepositional noun."),
    (2, "Пожалуйста, помоги нам расписаться как можно быстрее.",
     "'Please help us sign the register as fast as possible.' Polite formula with imperative verb, dative pronoun, reflexive infinitive, and comparative adverbial phrase."),
    (3, "Давайте расскажем эту новость всем гостям ресторана!",
     "'Let's tell this news to all the guests of the restaurant!' Hortative particle with future verb, demonstrative adjective-noun phrase, and dative plural adjective-noun phrase."),
    (4, "Подожди, кажется, я немножко поторопился сейчас.",
     "'Wait, it seems I jumped the gun a little now.' Imperative verb with parenthetical modal verb, subject pronoun, degree adverb, past verb, and temporal adverb."),
    (5, "Честно говоря, я тоже слишком поторопилась с ответом.",
     "'To be honest, I also rushed with the answer too much.' Parenthetical phrase with subject pronoun, focusing particle, degree adverb, past verb, and prepositional phrase."),
    (6, "Значит, нам обоим нужно хорошенько подумать.",
     "'So, both of us need to think carefully.' Logical connector with dative collective numeral, predicative word, degree adverb, and imperfective infinitive."),
    (7, "Да, нам лучше немного подождать со свадьбой.",
     "'Yes, it is better for us to wait a little with the wedding.' Affirmative particle with dative pronoun, comparative predicative, degree adverb, infinitive, and prepositional phrase."),
    (8, "Шеф, вы поможете нам спокойно разобраться?",
     "'Chef, will you help us sort this out calmly?' Direct address title with subject pronoun, future verb, dative pronoun, manner adverb, and reflexive infinitive."),
    (9, "Шеф не хочет слушать наши семейные споры.",
     "'The chef doesn't want to listen to our family arguments.' Subject noun with negated present modal verb, infinitive, and accusative possessive-adjective-noun phrase."),
    (10, "У Виктора сейчас начинается важный футбольный матч.",
     "'Viktor has an important football match starting now.' Locative possessive name phrase with temporal adverb, present reflexive verb, and nominative adjective-noun phrase."),
    (11, "Тогда мы сами во всём разберёмся позже.",
     "'Then we will sort everything out ourselves later.' Temporal connector with subject pronoun, emphatic pronoun, locative prepositional phrase, future reflexive verb, and time adverb."),
    (12, "Иди работай, свадьба пока точно подождёт!",
     "'Go work, the wedding will definitely wait for now!' Imperative motion and action verbs with nominative subject noun, temporal particle, modal adverb, and future verb."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Realizing that they both acted far too impulsively in the heat of the moment, Max and Victoria agree to postpone any wedding talk indefinitely. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("vika", "Иди работай, свадьба пока точно подождёт!")
