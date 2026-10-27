"""s01e11 scene 28: С кадрами нужно работать (Managing the Staff)."""

ID = "domashniy-arest-s01e11-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 28
TITLE = "С кадрами нужно работать  (Managing the Staff)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "lidia": "angelina",
}
LABELS = {
    "anya": "Аркадий",
    "lidia": "Лидия",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 735-745. Arkady retrieves his hidden cash bags with the help of secretary Lidia Alexeyevna, who gleefully exposes her grudge against Pasha."

INTRO = (
    "Arriving at the secret location where his bribe money was concealed, Arkady Borisovich is greeted "
    "by former secretary Lidia Alexeyevna. Delighted to spite her rude boss Pasha, Lidia proudly assists "
    "Arkady with the heavy bags. Let's listen in Russian first."
)

STORY = [
    ("anya", "Вот вы где, мои дорогие деньги!",
     "Here you are, my dear money!",
     [(735, "Вот вы, мои дорогие.")], ""),

    ("lidia", "Здравствуйте, дорогой Аркадий Борисович!",
     "Hello, dear Arkady Borisovich!",
     [(736, "Ну, здравствуйте.")], ""),

    ("anya", "Доставайте скорее все большие сумки.",
     "Take out all the large bags quickly.",
     [(737, "сумки достали.")], ""),

    ("anya", "Мы аккуратно грузим все деньги.",
     "We are carefully loading all the money.",
     [(738, "Грузим деньги.")], ""),

    ("lidia", "Павел никогда не ценил своих сотрудников.",
     "Pavel never valued his own employees.",
     [(740, "по-человечески к вам отнесся.")], ""),

    ("lidia", "Он всегда грубо разговаривал со мной.",
     "He always spoke rudely with me.",
     [], ""),

    ("lidia", "А я регулярно плевала ему в чай!",
     "And I regularly spat in his tea!",
     [(742, "А я вам еще и в чай плевала.")], ""),

    ("anya", "Спасибо большое за помощь, Лидия Алексеевна.",
     "Thank you very much for your help, Lidia Alexeyevna.",
     [(743, "Спасибо, Лидия Алексеевна.")], ""),

    ("lidia", "С кадрами нужно уметь правильно работать.",
     "One must know how to work with staff properly.",
     [(744, "С кадрами нужно уметь работать, Паша.")], ""),

    ("anya", "Вы проявили настоящую смелость и верность.",
     "You showed real courage and loyalty.",
     [], ""),

    ("lidia", "Я всегда уважала только вас, Аркадий.",
     "I always respected only you, Arkady.",
     [], ""),

    ("anya", "Теперь мы отвезём сумки в надёжное место.",
     "Now we will take the bags to a safe place.",
     [], ""),

    ("lidia", "Будьте очень осторожны с этими миллионами.",
     "Be very careful with these millions.",
     [], ""),

    ("anya", "Не беспокойтесь, теперь всё будет в порядке.",
     "Do not worry, now everything will be fine.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the conversational idioms expressing loyalty, "
    "workplace grievances, and relief."
)

WALK = [
    (0, None,
     "'Here you are, my dear money!' Emotional exclamatory address to the recovered cash using plural affectionate adjectives."),
    (1, None,
     "'Hello, dear Arkady Borisovich!' Formal respectful greeting combining the patronymic with an affectionate adjective."),
    (2, None,
     "'Take out all the large bags quickly.' Plural imperative verb with comparative adverb and accusative direct object phrase."),
    (3, None,
     "'We are carefully loading all the money.' First person plural present verb with manner adverb and direct object."),
    (4, None,
     "'Pavel never valued his own employees.' Past tense negative transitive verb with reflexive-possessive genitive object."),
    (5, None,
     "'He always spoke rudely with me.' Past imperfective verb with manner adverb and prepositional instrumental pronoun."),
    (6, None,
     "'And I regularly spat in his tea!' Conjunction followed by past feminine verb with dative pronoun and accusative destination."),
    (7, None,
     "'Thank you very much for your help, Lidia Alexeyevna.' Polite expression of gratitude followed by a prepositional phrase with patronymic."),
    (8, None,
     "'One must know how to work with staff properly.' Impersonal modal construction with infinitive governing instrumental noun."),
    (9, None,
     "'You showed real courage and loyalty.' Past perfective transitive verb governing coordinated feminine accusative nouns."),
    (10, None,
     "'I always respected only you, Arkady.' Past feminine transitive verb with restrictive particle and personal name."),
    (11, None,
     "'Now we will take the bags to a safe place.' Future perfective verb with accusative plural direct object and prepositional goal."),
    (12, None,
     "'Be very careful with these millions.' Plural imperative of the copula with short adjective and prepositional instrumental phrase."),
    (13, None,
     "'Do not worry, now everything will be fine.' Reflexive negative imperative followed by an idiomatic prepositional state expression."),
]

TRANSITION = "Now let's listen to Arkady and Lidia Alexeyevna's secret exchange once again."

OUTRO = (
    "With the heavy bags loaded, Arkady feels victorious, unaware of the trap awaiting him ahead. "
    "See you next time!"
)

CLOSING = ("lidia", "С кадрами нужно уметь правильно работать.")
