from pathlib import Path

ID = "kukhnya-s01e10-scene-36"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 36
TITLE = "Неожиданная новость  (Unexpected News)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Таня", "vika": "Вика"}
SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")

INTRO = (
    "Tanya arrives unexpectedly at Claude Monet and sits at a corner table to confront her sister Victoria. "
    "Believing a wild rumor spread by Chef Barinov that Vika is pregnant, Tanya demands to know why she was kept in the dark. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Здравствуй, Вика! Я села за угловой столик.",
     "Hello, Vika! I sat down at the corner table.",
     [(254, "Угловой столик")], "greeting sister"),
    ("vika", "Привет, Таня! Почему ты пришла так срочно?",
     "Hello, Tanya! Why did you come so urgently?",
     [(253, "проходите, пожалуйста")], "asking about arrival"),
    ("anya", "Почему ты мне совсем ничего не рассказала?",
     "Why didn't you tell me anything at all?",
     [(255, "почему ты мне не позвонил")], "expressing frustration"),
    ("vika", "Таня, я не понимаю твоих странных вопросов.",
     "Tanya, I don't understand your strange questions.",
     [(256, "Что случилось")], "expressing confusion"),
    ("anya", "Ты должна была сразу позвонить родной сестре!",
     "You should have immediately called your own sister!",
     [(255, "наконец-то")], "scolding sister"),
    ("vika", "Объясни мне спокойно, что вообще произошло?",
     "Explain to me calmly, what happened at all?",
     [(256, "Что случилось")], "demanding explanation"),
    ("anya", "Ты беременна, а я узнаю об этом последней!",
     "You are pregnant, and I find out about it last!",
     [(257, "Ты же беременна")], "revealing rumor"),
    ("vika", "С чего ты вообще взяла такую глупость?",
     "Where did you get such nonsense at all?",
     [(258, "С чего ты взяла")], "denying rumor"),
    ("anya", "Мне об этом лично сказал шеф Витя!",
     "Chef Vitya told me about this personally!",
     [(258, "Мне Витя сказал")], "naming the source"),
    ("vika", "Виктор опять придумал эту безумную историю!",
     "Viktor again made up this insane story!",
     [(258, "Витя сказал")], "accusing chef"),
    ("anya", "Значит, ты совсем не ждёшь ребёнка?",
     "So, you are not expecting a baby at all?",
     [(257, "беременна")], "seeking clarification"),
    ("vika", "Конечно нет, это просто наглая ложь!",
     "Of course not, this is simply an insolent lie!",
     [(258, "С чего ты взяла")], "firmly denying"),
    ("anya", "Тогда тебе нужно срочно поговорить с Виктором.",
     "Then you need to urgently speak with Viktor.",
     [(258, "Мне Витя сказал")], "advising confrontation"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the family dynamics, expressions of disbelief, and denial of false rumors."
)

WALK = [
    (0, "Здравствуй, Вика! Я села за угловой столик.",
     "'Hello, Vika! I sat down at the corner table.' Conversational greeting and vocative name with subject pronoun, past motion verb, and locative prepositional adjective-noun phrase."),
    (1, "Привет, Таня! Почему ты пришла так срочно?",
     "'Hello, Tanya! Why did you come so urgently?' Informal greeting and vocative name with interrogative adverb, subject pronoun, past verb, and manner adverb."),
    (2, "Почему ты мне совсем ничего не рассказала?",
     "'Why didn't you tell me anything at all?' Interrogative adverb with subject pronoun, dative pronoun, degree adverb, negative pronoun, negative particle, and past verb."),
    (3, "Таня, я не понимаю твоих странных вопросов.",
     "'Tanya, I don't understand your strange questions.' Vocative address with subject pronoun, negated present verb, and genitive plural demonstrative-adjective-noun object phrase."),
    (4, "Ты должна была сразу позвонить родной сестре!",
     "'You should have immediately called your own sister!' Subject pronoun with modal short adjective, past copula, time adverb, perfective infinitive, and dative adjective-noun phrase."),
    (5, "Объясни мне спокойно, что вообще произошло?",
     "'Explain to me calmly, what happened at all?' Imperative verb with dative pronoun, manner adverb, interrogative pronoun, modal adverb, and past neuter verb."),
    (6, "Ты беременна, а я узнаю об этом последней!",
     "'You are pregnant, and I find out about it last!' Subject pronoun with short adjective, coordinating conjunction, subject pronoun, present verb, prepositional phrase, and adjective."),
    (7, "С чего ты вообще взяла такую глупость?",
     "'Where did you get such nonsense at all?' Idiomatic interrogative prepositional phrase with subject pronoun, modal adverb, past verb, and accusative adjective-noun phrase."),
    (8, "Мне об этом лично сказал шеф Витя!",
     "'Chef Vitya told me about this personally!' Dative pronoun with prepositional phrase, manner adverb, past verb, and nominative title-name subject phrase."),
    (9, "Виктор опять придумал эту безумную историю!",
     "'Viktor again made up this insane story!' Subject noun with frequency adverb, past perfective verb, and accusative demonstrative-adjective-noun phrase."),
    (10, "Значит, ты совсем не ждёшь ребёнка?",
     "'So, you are not expecting a baby at all?' Logical connector with subject pronoun, degree adverb, negated present transitive verb, and genitive object noun."),
    (11, "Конечно нет, это просто наглая ложь!",
     "'Of course not, this is simply an insolent lie!' Parenthetical certainty phrase with negative particle, subject pronoun, modal particle, and nominative adjective-noun phrase."),
    (12, "Тогда тебе нужно срочно поговорить с Виктором.",
     "'Then you need to urgently speak with Viktor.' Temporal connector with dative pronoun, predicative word, manner adverb, infinitive, and instrumental prepositional name phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Shocked to learn that Chef Barinov spread rumors about her pregnancy, Victoria prepares to confront him immediately in the kitchen. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("anya", "Тогда тебе нужно срочно поговорить с Виктором.")
