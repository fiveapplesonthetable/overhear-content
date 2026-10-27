ID = "domashniy-arest-s01e11-scene-02"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 2
TITLE = "Самсон ждёт ответа  (Samson Waits for an Answer)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja"}
LABELS = {"anya": "Нина", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 50-53. After Nina rejects his hasty proposal, Samsonov refuses to give up. "
    "He skips his soccer match and insists on waiting outside until she changes her mind."
)

INTRO = (
    "In this continuation of the nineteen-nineties flashback, Nina walks out of the cafe, expecting Samsonov to leave for his soccer match. "
    "Instead, Ivan stubbornly declares that soccer can wait. He sits down outside and announces he will wait for her as long as it takes. "
    "Nina tries to persuade him to go home, but Ivan remains determined to win her over. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Самсон, ты же опаздываешь на футбол!",
     "Samson, you are late for football!",
     [(50, "футболом")], ""),
    ("samson", "Ничего страшного, обойдётся без футбола.",
     "Nothing terrible, it will do without football.",
     [(50, "Хрен с ним, с футболом")], "colloquial vulgarity softened to clean A1"),
    ("samson", "Я никуда отсюда не уйду.",
     "I will not leave here anywhere.",
     [(51, "Подожду")], ""),
    ("anya", "И сколько ты собираешься здесь сидеть?",
     "And how long do you plan to sit here?",
     [(52, "Подожди")], ""),
    ("samson", "Я буду ждать столько, сколько нужно.",
     "I will wait as long as is necessary.",
     [(53, "Подожду, подожду")], ""),
    ("anya", "На улице становится очень холодно.",
     "It is getting very cold outside.",
     [], "continuation of street dialogue"),
    ("samson", "Мне совершенно не холодно в куртке.",
     "I am not cold at all in my jacket.",
     [], "continuation of street dialogue"),
    ("anya", "Ты ведёшь себя как упрямый ребёнок!",
     "You are behaving like a stubborn child!",
     [], "continuation of street dialogue"),
    ("samson", "Я просто очень сильно люблю тебя.",
     "I simply love you very much.",
     [], "continuation of street dialogue"),
    ("anya", "Мы знакомы всего один месяц.",
     "We have known each other only one month.",
     [], "continuation of street dialogue"),
    ("samson", "Для настоящей любви этого вполне достаточно.",
     "For true love this is quite enough.",
     [], "continuation of street dialogue"),
    ("anya", "Пожалуйста, перестань стоять под окнами.",
     "Please stop standing under the windows.",
     [], "continuation of street dialogue"),
    ("samson", "Я всё равно дождусь твоего ответа!",
     "I will wait for your answer anyway!",
     [], "continuation of street dialogue"),
]

OPENER = "Now let's examine Ivan and Nina's conversation on the street line by line."

WALK = [
    (0, None,
     "'Samson, you are late for football!' Nina reminds Ivan of his favorite hobby using a present imperfective verb."),
    (1, None,
     "'Nothing terrible, it will do without football.' Samson dismisses the soccer game with a prepositional genitive phrase."),
    (2, None,
     "'I will not leave here anywhere.' The negative pronoun with a perfective future verb expresses stubborn refusal."),
    (3, None,
     "'And how long do you plan to sit here?' Nina asks about his persistence with an interrogative adverb of quantity."),
    (4, None,
     "'I will wait as long as is necessary.' The compound future verb with a correlative adverb affirms his patience."),
    (5, None,
     "'It is getting very cold outside.' The impersonal reflexive verb describes the deteriorating weather."),
    (6, None,
     "'I am not cold at all in my jacket.' Samson uses a dative experiencer construction with a qualifying adverb."),
    (7, None,
     "'You are behaving like a stubborn child!' Nina compares him to an unruly boy using the reflexive construction for conduct."),
    (8, None,
     "'I simply love you very much.' Samson responds with an earnest declaration of affection."),
    (9, None,
     "'We have known each other only one month.' Nina repeats her rational objection with an adverb of limitation."),
    (10, None,
     "'For true love this is quite enough.' The preposition governing genitive introduces a romantic justification."),
    (11, None,
     "'Please stop standing under the windows.' Nina urges him to leave with a polite negative imperative."),
    (12, None,
     "'I will wait for your answer anyway!' Samson vows persistence using the adverbial idiom of determination."),
]

TRANSITION = "Now let's listen to their street argument once more without pauses."
OUTRO = (
    "Samsonov's stubborn refusal to give up slowly chips away at Nina's skepticism. "
    "In the next scene, Nina finally relents and gives Ivan the answer he has been waiting for."
)
CLOSING = ("samson", "Я всё равно дождусь твоего ответа!")
