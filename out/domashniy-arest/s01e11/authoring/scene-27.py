"""s01e11 scene 27: Внутренний ресурс (Inner Resilience)."""

ID = "domashniy-arest-s01e11-scene-27"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 27
TITLE = "Внутренний ресурс  (Inner Resilience)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "officer": "anja",
}
LABELS = {
    "anya": "Самсон",
    "officer": "Лавров",
}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"
SOURCE_NOTE = "Cues 714-727. Pushed by stimulants, Samsonov meets Major Lavrov and boasts of his inner power before the big visit."

INTRO = (
    "Hyped up on experimental stimulants before his meeting with Vladimir Putin, Ivan Samsonov marches into "
    "the room with intense energy. Major Lavrov watches with concern as Samsonov proclaims his readiness to lead. "
    "Let's listen in Russian first."
)

STORY = [
    ("anya", "Приветствую всех! Я Иван Самсонов.",
     "Greetings to everyone! I am Ivan Samsonov.",
     [(715, "Приветствую."), (716, "Иван Самсонов.")], ""),

    ("officer", "Здравствуйте, Иван. Проходите сюда, пожалуйста.",
     "Hello, Ivan. Come in here, please.",
     [(714, "Прошу, пожалуйста. Пожалуйста, вот.")], ""),

    ("anya", "Это мой политтехнолог и мой психиатр.",
     "This is my political consultant and my psychiatrist.",
     [(719, "Это мой политикнолог."), (720, "Мой психиатр.")], ""),

    ("officer", "Мы внимательно слушаем вас, Иван.",
     "We are listening to you carefully, Ivan.",
     [(723, "Слушаю вас.")], ""),

    ("officer", "Что доктора вообще сделали с вами?",
     "What did the doctors actually do with you?",
     [(724, "Что вы с ним сделали?")], ""),

    ("anya", "Ничего страшного со мной не делали.",
     "They did not do anything bad with me.",
     [(725, "Ничего.")], ""),

    ("anya", "У меня просто мощный внутренний ресурс.",
     "I simply have a powerful inner resilience.",
     [(726, "У него просто очень мощный внутренний ресурс.")], ""),

    ("officer", "Вы кажетесь слишком возбуждённым и резким.",
     "You seem too excited and abrupt.",
     [], ""),

    ("anya", "Я готов говорить с любым человеком!",
     "I am ready to speak with any person!",
     [], ""),

    ("officer", "Главное, не говорите лишних глупостей.",
     "The main thing is do not say unnecessary foolishness.",
     [], ""),

    ("anya", "Я простой человек из народа.",
     "I am a simple person from the people.",
     [], ""),

    ("officer", "Мы надеемся на ваше благоразумие.",
     "We rely on your good sense.",
     [], ""),

    ("anya", "Я обязательно одержу чистую победу.",
     "I will definitely win a clean victory.",
     [], ""),

    ("officer", "Тогда садитесь и повторите вашу речь.",
     "Then sit down and repeat your speech.",
     [], ""),
]

OPENER = (
    "Let's examine the dialogue line by line. Notice the expressions used to describe personal "
    "readiness and official meetings."
)

WALK = [
    (0, None,
     "'Greetings to everyone! I am Ivan Samsonov.' Formal introductory greeting with first person present verb and nominative name."),
    (1, None,
     "'Hello, Ivan. Come in here, please.' Polite imperative with locative adverb and standard courtesy particle."),
    (2, None,
     "'This is my political consultant and my psychiatrist.' Demonstrative pronoun introducing two coordinated masculine predicate nouns."),
    (3, None,
     "'We are listening to you carefully, Ivan.' First person plural present verb with manner adverb and formal accusative pronoun."),
    (4, None,
     "'What did the doctors actually do with you?' Interrogative past tense clause with prepositional phrase indicating affected party."),
    (5, None,
     "'They did not do anything bad with me.' Negative genitive pronoun with past tense plural verb and instrumental phrase."),
    (6, None,
     "'I simply have a powerful inner resilience.' Possessive dative construction with nominative masculine noun phrase."),
    (7, None,
     "'You seem too excited and abrupt.' Second person reflexive verb governing coordinated instrumental adjectives."),
    (8, None,
     "'I am ready to speak with any person!' Short predicative adjective with infinitive and prepositional instrumental complement."),
    (9, None,
     "'The main thing is do not say unnecessary foolishness.' Neuter adjective functioning as topic followed by negative imperative verb."),
    (10, None,
     "'I am a simple person from the people.' Descriptive nominative predicate phrase with genitive origin complement."),
    (11, None,
     "'We rely on your good sense.' Present tense reflexive verb governing a prepositional accusative object."),
    (12, None,
     "'I will definitely win a clean victory.' Future perfective transitive verb with adverb and accusative direct object."),
    (13, None,
     "'Then sit down and repeat your speech.' Two coordinated imperative verbs with temporal adverb and accusative object."),
]

TRANSITION = "Now let's listen to Samsonov's determined declaration once again at normal speed."

OUTRO = (
    "Samsonov remains convinced that his raw inner power will carry him through the high-stakes "
    "political encounter. See you next time!"
)

CLOSING = ("anya", "Я обязательно одержу чистую победу.")
