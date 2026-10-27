from pathlib import Path

ID = "kukhnya-s01e10-scene-37"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 37
TITLE = "Внезапное предложение  (A Sudden Proposal)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")

INTRO = (
    "Furious about the false rumor, Victoria confronts Chef Barinov and Max in the dining area. "
    "To turn the tables on Vika in front of her sister Tanya, Max steps up boldly, introduces himself as the future father, "
    "and suddenly asks Victoria to marry him. Let's listen to their conversation in Russian."
)

STORY = [
    ("vika", "Витя, зачем ты обманул Таню про меня?",
     "Vitya, why did you lie to Tanya about me?",
     [(259, "что Таня про меня")], "confronting about lie"),
    ("anya", "Шеф, я могу всё подробно объяснить сейчас.",
     "Chef, I can explain everything in detail now.",
     [(263, "колись")], "trying to de-escalate"),
    ("vika", "Ты, мальчик, сегодня выбрал не ту девушку!",
     "You, boy, picked the wrong girl today!",
     [(264, "мальчик, не на ту нарвался")], "warning Max"),
    ("anya", "А сейчас мы устроим настоящее весёлое шоу.",
     "And now we will put on a real fun show.",
     [(266, "будем делать шоу")], "deciding to bluff"),
    ("anya", "Здравствуйте, Татьяна, давайте знакомиться, я Максим.",
     "Hello, Tatyana, let's get acquainted, I am Maxim.",
     [(267, "познакомиться. Максим"), (268, "Татьяна")], "introducing himself"),
    ("vika", "Макс, прекрати немедленно этот глупый цирк!",
     "Max, stop this silly circus immediately!",
     [(266, "доигралась")], "demanding he stop"),
    ("anya", "Я отец вашего будущего прекрасного племянника!",
     "I am the father of your future wonderful nephew!",
     [(269, "Отец вашего будущего племянника")], "announcing fatherhood"),
    ("vika", "Ты ведёшь себя как полный сумасшедший!",
     "You are behaving like a complete madman!",
     [(274, "Ты же блефуешь")], "scolding Max"),
    ("anya", "Мы же теперь самые близкие родные люди.",
     "We are now the closest family members.",
     [(271, "мы ж теперь родственники")], "claiming family bond"),
    ("anya", "Я хочу сказать всем вам кое-что важное.",
     "I want to say something important to you all.",
     [(272, "кое-что важное")], "building anticipation"),
    ("anya", "Вика, выходи за меня замуж прямо сейчас!",
     "Vika, marry me right now!",
     [(273, "выходи за меня замуж")], "proposing marriage"),
    ("vika", "Ты просто нагло и открыто сейчас блефуешь!",
     "You are simply insolently and openly bluffing now!",
     [(274, "Ты же блефуешь")], "calling his bluff"),
    ("anya", "Я говорю совершенно серьёзно перед твоей сестрой!",
     "I am speaking completely seriously in front of your sister!",
     [(274, "блефуешь")], "insisting on proposal"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the romantic bluffing, bold public theatricals, and marriage proposal idioms."
)

WALK = [
    (0, "Витя, зачем ты обманул Таню про меня?",
     "'Vitya, why did you lie to Tanya about me?' Direct address name with interrogative adverb, subject pronoun, past verb, dative name, and prepositional pronoun."),
    (1, "Шеф, я могу всё подробно объяснить сейчас.",
     "'Chef, I can explain everything in detail now.' Direct address title with subject pronoun, modal verb, collective pronoun, manner adverb, infinitive, and temporal adverb."),
    (2, "Ты, мальчик, сегодня выбрал не ту девушку!",
     "'You, boy, picked the wrong girl today!' Subject pronoun and vocative noun with temporal adverb, past verb, negative particle, and demonstrative adjective-noun phrase."),
    (3, "А сейчас мы устроим настоящее весёлое шоу.",
     "'And now we will put on a real fun show.' Coordinating conjunction and temporal adverb with subject pronoun, future verb, and accusative adjective-noun phrase."),
    (4, "Здравствуйте, Татьяна, давайте знакомиться, я Максим.",
     "'Hello, Tatyana, let's get acquainted, I am Maxim.' Polite greeting and vocative name with hortative infinitive construction, subject pronoun, and predicative name."),
    (5, "Макс, прекрати немедленно этот глупый цирк!",
     "'Max, stop this silly circus immediately!' Vocative name with imperative verb, temporal adverb, and demonstrative evaluative adjective-noun phrase."),
    (6, "Я отец вашего будущего прекрасного племянника!",
     "'I am the father of your future wonderful nephew!' Subject pronoun with nominative noun, possessive determiner, and genitive future adjective-noun phrase."),
    (7, "Ты ведёшь себя как полный сумасшедший!",
     "'You are behaving like a complete madman!' Subject pronoun with present reflexive verb, comparative conjunction, and qualitative adjective-noun phrase."),
    (8, "Мы же теперь самые близкие родные люди.",
     "'We are now the closest family members.' Subject pronoun with emphatic particle, temporal adverb, superlative adjective, and nominative adjective-noun phrase."),
    (9, "Я хочу сказать всем вам кое-что важное.",
     "'I want to say something important to you all.' Subject pronoun with present modal verb, infinitive, dative pronouns, and indefinite neuter adjective-noun phrase."),
    (10, "Вика, выходи за меня замуж прямо сейчас!",
     "'Vika, marry me right now!' Vocative name with imperative motion verb, accusative prepositional pronoun phrase, and temporal idiomatic phrase."),
    (11, "Ты просто нагло и открыто сейчас блефуешь!",
     "'You are simply insolently and openly bluffing now!' Subject pronoun with limiting particle, adverbs joined by coordinating conjunction, temporal adverb, and present verb."),
    (12, "Я говорю совершенно серьёзно перед твоей сестрой!",
     "'I am speaking completely seriously in front of your sister!' Subject pronoun with present verb, degree adverb, manner adverb, and instrumental prepositional possessive-noun phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Trapped by his own dramatic theatricals in front of Tanya and Chef Barinov, Max takes a bold gamble by publicly proposing to Victoria. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("anya", "Я говорю совершенно серьёзно перед твоей сестрой!")
