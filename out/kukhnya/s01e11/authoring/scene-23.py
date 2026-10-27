from pathlib import Path

ID = "kukhnya-s01e11-scene-23"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 23
TITLE = "Урок для критика  (A Lesson for the Critic)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "anja"}
LABELS = {"anya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня s01e11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")

INTRO = (
    "At the pass window of Claude Monet, line cooks Senya and Fedya watch in shock as bartender Kostya confronts the arrogant restaurant critic. "
    "Defending Nastya from further insults, Kostya delivers an unforgettable drink to the rude patron. "
    "Let's listen to the cooks' amazed reaction in Russian."
)

STORY = [
    ("anya", "Ты видел, что сейчас произошло в зале?",
     "Did you see what just happened in the hall?",
     [], "asking cook"),
    ("fedya", "Наш бармен смело подошёл к столику критика.",
     "Our bartender boldly stepped up to the critic's table.",
     [], "narrating confrontation"),
    ("anya", "Этот критик опять грубо обижал нашу Настю.",
     "This critic was rudely insulting our Nastya again.",
     [], "mentioning harassment"),
    ("fedya", "Костя не стал терпеть такое наглое поведение.",
     "Kostya did not start tolerating such insolent behavior.",
     [], "praising bartender's stance"),
    ("anya", "Что, гость заказал напиток из бара сейчас?",
     "What, did the guest order a drink from the bar now?",
     [(311, "что-то из вары заказал?")], "asking about order"),
    ("fedya", "Точно, он получил заказ по полной программе!",
     "Exactly, he received an order to the fullest program!",
     [(311, "Точно, по полной заказал.")], "confirming confrontation"),
    ("anya", "Костя вылил стакан прямо на его костюм!",
     "Kostya poured a glass right onto his suit!",
     [], "describing action"),
    ("fedya", "Наш тихий бармен оказался настоящим храбрым героем.",
     "Our quiet bartender turned out to be a real brave hero.",
     [], "expressing admiration"),
    ("anya", "Теперь этот важный критик весь мокрый сидит.",
     "Now this important critic sits completely wet.",
     [], "observing soaked critic"),
    ("fedya", "Но шеф будет ужасно зол из-за скандала.",
     "But the chef will be terribly angry because of the scandal.",
     [], "fearing Barinov's reaction"),
    ("anya", "Виктория уже быстро бежит в обеденный зал.",
     "Victoria is already quickly running into the dining hall.",
     [], "noting management arrival"),
    ("fedya", "Косте сейчас точно грозит очень быстрое увольнение.",
     "A very swift dismissal definitely threatens Kostya right now.",
     [], "predicting firing"),
    ("anya", "Зато он храбро защитил свою любимую девушку!",
     "At least he courageously protected his beloved girl!",
     [], "applauding bravery"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice workplace banter, expressions of surprise, and descriptions of dramatic actions."
)

WALK = [
    (0, "Ты видел, что сейчас произошло в зале?",
     "'Did you see what just happened in the hall?' Subject pronoun with past verb, relative pronoun, temporal adverb, past verb, and prepositional phrase."),
    (1, "Наш бармен смело подошёл к столику критика.",
     "'Our bartender boldly stepped up to the critic's table.' Possessive determiner with subject noun, manner adverb, past verb, and dative prepositional phrase."),
    (2, "Этот критик опять грубо обижал нашу Настю.",
     "'This critic was rudely insulting our Nastya again.' Demonstrative subject phrase with temporal adverb, manner adverb, past verb, and accusative possessive-name phrase."),
    (3, "Костя не стал терпеть такое наглое поведение.",
     "'Kostya did not start tolerating such insolent behavior.' Subject noun with negated past modal verb, infinitive, and accusative demonstrative-adjective-noun phrase."),
    (4, "Что, гость заказал напиток из бара сейчас?",
     "'What, did the guest order a drink from the bar now?' Interrogative particle with subject noun, past verb, direct object noun, and prepositional phrase."),
    (5, "Точно, он получил заказ по полной программе!",
     "'Exactly, he received an order to the fullest program!' Affirmative adverb with subject pronoun, past verb, direct object noun, and idiomatic prepositional phrase."),
    (6, "Костя вылил стакан прямо на его костюм!",
     "'Kostya poured a glass right onto his suit!' Subject name with past transitive verb, direct object noun, spatial adverb, and prepositional phrase."),
    (7, "Наш тихий бармен оказался настоящим храбрым героем.",
     "'Our quiet bartender turned out to be a real brave hero.' Possessive-adjective-noun subject with past copular verb and instrumental predicate adjective-noun phrase."),
    (8, "Теперь этот важный критик весь мокрый сидит.",
     "'Now this important critic sits completely wet.' Temporal adverb with demonstrative-adjective-noun phrase, quantifier, predicate adjective, and present verb."),
    (9, "Но шеф будет ужасно зол из-за скандала.",
     "'But the chef will be terribly angry because of the scandal.' Adversative conjunction with subject noun, future copula, degree adverb, short adjective, and causal prepositional phrase."),
    (10, "Виктория уже быстро бежит в обеденный зал.",
     "'Victoria is already quickly running into the dining hall.' Subject name with temporal particle, manner adverb, present motion verb, and prepositional phrase."),
    (11, "Косте сейчас точно грозит очень быстрое увольнение.",
     "'A very swift dismissal definitely threatens Kostya right now.' Dative pronoun with temporal adverb, modal particle, present verb, and adjective-noun subject phrase."),
    (12, "Зато он храбро защитил свою любимую девушку!",
     "'At least he courageously protected his beloved girl!' Contrastive conjunction with subject pronoun, manner adverb, past verb, and accusative possessive-adjective-noun phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Although Kostya faces certain termination for soaking the critic, the kitchen crew respects him deeply for defending Nastya. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("anya", "Зато он храбро защитил свою любимую девушку!")
