from pathlib import Path

ID = "kukhnya-s01e11-scene-22"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 22
TITLE = "Мудрый совет  (Wise Advice)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "rodion": "anja"}
LABELS = {"anya": "Костя", "rodion": "Родион"}
SOURCE_NAME = "Кухня s01e11"
SOURCE_FILE = Path("sources/kukhnya/s01/e11.ru.dual.srt")

INTRO = (
    "At the bar of Claude Monet, bartender Kostya is anxiously polishing a glass because an arrogant food critic is harassing Nastya. "
    "As the homeless philosopher Rodion savors his complimentary soup, he offers Kostya deep and unexpected wisdom. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("rodion", "Этот суп действительно очень вкусный и горячий.",
     "This soup is really very tasty and hot.",
     [(290, "Хорош супец.")], "praising soup"),
    ("rodion", "Костя, скажи честно, что с тобой случилось?",
     "Kostya, tell honestly, what happened with you?",
     [(291, "Костя, что с тобой?")], "asking bartender"),
    ("anya", "Всё нормально, я просто вытираю эту рюмку.",
     "Everything is fine, I am simply wiping this glass.",
     [(292, "Все нормально."), (293, "Эта рюмка уже полчаса трет.")], "downplaying anxiety"),
    ("rodion", "Ты моешь её уже целых полчаса.",
     "You have been washing it for a whole half hour already.",
     [(293, "Эта рюмка уже полчаса трет.")], "pointing out nervous habit"),
    ("anya", "У Насти за столом сидит важный критик.",
     "An important critic is sitting at Nastya's table.",
     [(295, "У Насти за столиком сидит тип очень важный."), (296, "Критик.")], "explaining situation"),
    ("anya", "Этот наглый мужчина грубо пристаёт к ней.",
     "This insolent man is rudely hitting on her.",
     [(297, "Он пристает к ней.")], "describing harassment"),
    ("anya", "Я боюсь сделать что-нибудь плохое для ресторана.",
     "I am afraid of doing something bad for the restaurant.",
     [(298, "А я сделать ничего не могу. Он же критик."), (299, "Не дай бог, что-нибудь плохое про наш ресторан напишет.")], "confessing hesitation"),
    ("rodion", "Понимаешь, проблема совсем не в этом критике.",
     "You see, the problem is not at all in this critic.",
     [(301, "Понимаешь, проблема тут не в том, кто он")], "starting philosophical advice"),
    ("rodion", "Главный вопрос здесь в том, кто ты.",
     "The main question here is in who you are.",
     [(301, "а кто ты.")], "reframing issue"),
    ("rodion", "Передай мне соль, пожалуйста, юный друг.",
     "Pass me the salt, please, young friend.",
     [(303, "Дай, пожалуйста, соль.")], "asking for condiment"),
    ("rodion", "Дворник он или критик — это совсем неважно.",
     "Whether he is a janitor or a critic—that is completely unimportant.",
     [(305, "А там уже дворник он или критик, это довольно-таки вторично.")], "minimizing social status"),
    ("rodion", "Позволяешь ты обижать свою девушку или нет?",
     "Do you allow someone to insult your girlfriend or not?",
     [(304, "Позволяешь ты ему это делать или нет?")], "asking core question"),
    ("rodion", "Жизнь твоя, и только ты принимаешь решение!",
     "The life is yours, and only you make the decision!",
     [(307, "Ну что, жизнь твоя, девушка твоя."), (308, "И решение твоя.")], "urging personal choice"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the philosophical advice, expressions of worry, and questions of self-respect."
)

WALK = [
    (0, "Этот суп действительно очень вкусный и горячий.",
     "'This soup is really very tasty and hot.' Demonstrative pronoun with subject noun, modal adverb, degree adverb, and coordinated predicate adjectives."),
    (1, "Костя, скажи честно, что с тобой случилось?",
     "'Kostya, tell honestly, what happened with you?' Direct address name with imperative verb, manner adverb, interrogative pronoun, and past reflexive verb."),
    (2, "Всё нормально, я просто вытираю эту рюмку.",
     "'Everything is fine, I am simply wiping this glass.' Indefinite subject pronoun with predicative adverb, subject pronoun, focusing particle, present verb, and accusative demonstrative-noun phrase."),
    (3, "Ты моешь её уже целых полчаса.",
     "'You have been washing it for a whole half hour already.' Subject pronoun with present verb, accusative pronoun, temporal particle, and quantitative adjective-noun phrase."),
    (4, "У Насти за столом сидит важный критик.",
     "'An important critic is sitting at Nastya's table.' Prepositional possessive name phrase with locative noun, present verb, and nominative adjective-noun phrase."),
    (5, "Этот наглый мужчина грубо пристаёт к ней.",
     "'This insolent man is rudely hitting on her.' Demonstrative-adjective-noun subject phrase with manner adverb, present verb, and prepositional personal pronoun."),
    (6, "Я боюсь сделать что-нибудь плохое для ресторана.",
     "'I am afraid of doing something bad for the restaurant.' Subject pronoun with present verb, infinitive, indefinite accusative phrase, and beneficiary prepositional noun."),
    (7, "Понимаешь, проблема совсем не в этом критике.",
     "'You see, the problem is not at all in this critic.' Parenthetical verb with subject noun, intensifying particle, negative particle, and locative prepositional phrase."),
    (8, "Главный вопрос здесь в том, кто ты.",
     "'The main question here is in who you are.' Nominative adjective-noun phrase with spatial adverb and relative locative interrogative clause."),
    (9, "Передай мне соль, пожалуйста, юный друг.",
     "'Pass me the salt, please, young friend.' Imperative verb with dative pronoun, accusative noun, politeness particle, and vocative adjective-noun phrase."),
    (10, "Дворник он или критик — это совсем неважно.",
     "'Whether he is a janitor or a critic—that is completely unimportant.' Disjunctive nominal subject clause with demonstrative pronoun, degree adverb, and short predicate adjective."),
    (11, "Позволяешь ты обижать свою девушку или нет?",
     "'Do you allow someone to insult your girlfriend or not?' Present verb with subject pronoun, infinitive, accusative possessive-noun phrase, and disjunctive conjunction-particle."),
    (12, "Жизнь твоя, и только ты принимаешь решение!",
     "'The life is yours, and only you make the decision!' Possessive subject phrase with coordinating conjunction, restrictive particle, subject pronoun, present verb, and direct object noun."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Inspired by Rodion's wise words about honor and boundaries, Kostya realizes that protecting Nastya matters far more than any critic's opinion. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("rodion", "Жизнь твоя, и только ты принимаешь решение!")
