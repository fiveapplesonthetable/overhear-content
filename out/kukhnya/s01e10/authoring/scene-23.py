ID = "kukhnya-s01e10-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 23
TITLE = "Нет денег — нет икры  (No Cash, No Caviar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "timur": "anja"}
LABELS = {"anya": "Шеф", "timur": "Тимур"}
SOURCE_NAME = "Кухня (The Kitchen) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

INTRO = (
    "Having tasted the black caviar and praised its flavor, Chef Barinov is hit with a hefty price tag of two hundred thousand rubles. "
    "When Barinov admits he lost all his cash on a bad football bet, the supplier flatly refuses credit and demands payment for the sample. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Да, эта чёрная икра действительно очень вкусная.",
     "Yes, this black caviar is indeed very tasty.",
     [(172, "Да. Да. Вкусная")], "praising caviar quality"),
    ("timur", "Сколько денег ты приготовил за пять килограмм?",
     "How much money did you prepare for five kilograms?",
     [(173, "Сколько денег? Пять кило")], "inquiring about cash"),
    ("anya", "Назови точную цену за весь этот товар.",
     "Name the exact price for all these goods.",
     [(174, "Двести тысяч")], "asking final total"),
    ("timur", "С тебя ровно двести тысяч рублей прямо сейчас.",
     "That will be exactly two hundred thousand rubles right now.",
     [(174, "Двести тысяч")], "quoting price"),
    ("anya", "Тимур, оставь икру, а деньги отдам позже.",
     "Timur, leave the caviar, and I will pay later.",
     [(175, "оставляю икру, а деньги через неделю")], "asking for credit"),
    ("timur", "Нет денег — нет никакой вкусной икры.",
     "No money — no delicious caviar.",
     [(176, "нет налички, нет икры")], "refusing credit"),
    ("anya", "Я поставил все деньги по твоему совету!",
     "I bet all the money on your advice!",
     [(177, "все деньги поставил на кони по твоей наводке")], "blaming supplier tip"),
    ("timur", "Ты проиграл на своих любимых быстрых конях.",
     "You lost on your favorite fast horses.",
     [(178, "На коней?")], "mocking team loss"),
    ("anya", "Ты же сам клялся в их победе!",
     "You yourself swore by their victory!",
     [(177, "Тимур, я отдам")], "reminding of promise"),
    ("timur", "Пусть теперь твои кони приносят тебе икру.",
     "Let your horses bring caviar to you now.",
     [(179, "пусть твои кони тебе икру и мечут")], "dismissing complaint"),
    ("anya", "Зачем ты убираешь этот товар обратно?",
     "Why are you taking this merchandise back?",
     [(180, "триста рублей годи")], "watching him pack"),
    ("timur", "Кстати, верни триста рублей за эту ложку!",
     "By the way, return three hundred rubles for this spoon!",
     [(180, "триста рублей годи"), (182, "Ты целую ложку икры съел")], "demanding sample cost"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the monetary expressions, gambling references, and transactional disputes."
)

WALK = [
    (0, "Да, эта чёрная икра действительно очень вкусная.",
     "'Yes, this black caviar is indeed very tasty.' Affirmative particle with demonstrative feminine noun phrase, modal adverb, degree adverb, and predicate adjective."),
    (1, "Сколько денег ты приготовил за пять килограмм?",
     "'How much money did you prepare for five kilograms?' Quantitative interrogative with genitive noun, subject pronoun, past verb, and prepositional numeral phrase."),
    (2, "Назови точную цену за весь этот товар.",
     "'Name the exact price for all these goods.' Imperative verb with accusative adjective-noun phrase and prepositional accusative demonstrative phrase."),
    (3, "С тебя ровно двести тысяч рублей прямо сейчас.",
     "'That will be exactly two hundred thousand rubles right now.' Origin prepositional phrase with quantitative adverb, numeral phrase with genitive noun, and temporal phrase."),
    (4, "Тимур, оставь икру, а деньги отдам позже.",
     "'Timur, leave the caviar, and I will pay later.' Direct address with imperative verb, accusative noun, conjunction, accusative noun, future verb, and comparative adverb."),
    (5, "Нет денег — нет никакой вкусной икры.",
     "'No money — no delicious caviar.' Negative existential construction with genitive noun, dash, and reinforced negative existential phrase."),
    (6, "Я поставил все деньги по твоему совету!",
     "'I bet all the money on your advice!' Subject pronoun with past verb, accusative object noun phrase, and prepositional dative possessive phrase."),
    (7, "Ты проиграл на своих любимых быстрых конях.",
     "'You lost on your favorite fast horses.' Subject pronoun with past verb and prepositional locative plural adjective-noun phrase."),
    (8, "Ты же сам клялся в их победе!",
     "'You yourself swore by their victory!' Emphatic subject pronoun with intensive pronoun, past reflexive verb, and prepositional locative noun phrase."),
    (9, "Пусть теперь твои кони приносят тебе икру.",
     "'Let your horses bring caviar to you now.' Third-person imperative particle with temporal adverb, subject noun phrase, present verb, dative pronoun, and accusative noun."),
    (10, "Зачем ты убираешь этот товар обратно?",
     "'Why are you taking this merchandise back?' Interrogative purpose adverb with subject pronoun, present verb, accusative demonstrative noun phrase, and directional adverb."),
    (11, "Кстати, верни триста рублей за эту ложку!",
     "'By the way, return three hundred rubles for this spoon!' Parenthetical conversational adverb with imperative verb, compound numeral phrase, and causal prepositional phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Humiliated by his gambling losses, Chef Barinov is left empty-handed and petty-taxed by his unimpressed supplier. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("timur", "Кстати, верни триста рублей за эту ложку!")
