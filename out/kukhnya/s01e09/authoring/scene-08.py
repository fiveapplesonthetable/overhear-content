"""s01e09 scene 08: Неожиданное родство (An Unexpected Kinship)."""

ID = "kukhnya-s01e09-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 8
TITLE = "Неожиданное родство  (An Unexpected Kinship)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 186-218. In the bar area, Max meets Barinov's young daughter Alisa and discovers that Chef Barinov and Victoria are connected through family ties."

INTRO = (
    "Near the bar in the Claude Monet dining room, Max arrives to fetch cognac for pastry chef Louis and notices art director Victoria with a young girl. "
    "Max teases Victoria about having children, only for the outspoken little girl to reveal that her father is the kitchen's boss, exposing unexpected family connections. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("max", "Вика, налей немного воды, пожалуйста.",
     "Vika, pour a little water, please.",
     [(193, "Костя, налей водички, пожалуйста")], "asking for some water"),
    ("anya", "Костя тебе нальёт, а мне некогда.",
     "Kostya will pour for you, and I have no time.",
     [(187, "Но мне сейчас встречать гостей, видите")], "directing him to the bartender"),
    ("max", "Ого, я не знал о твоих детях!",
     "Wow, I did not know about your children!",
     [(194, "Ой, я не знал, что у тебя есть дети")], "surprised by the child's presence"),
    ("anya", "Это не моя дочка, а моя племянница.",
     "This is not my daughter, but my niece.",
     [(196, "Это дочь моей сестры Алиса")], "clarifying their relationship"),
    ("max", "Она очень похожа на тебя внешне.",
     "She looks very much like you externally.",
     [], "observing family resemblance"),
    ("anya", "Её зовут Алиса, и она хорошая девочка.",
     "Her name is Alice, and she is a good girl.",
     [(196, "дочь моей сестры Алиса")], "introducing the niece"),
    ("max", "А почему она говорит про нашего шефа?",
     "And why is she talking about our chef?",
     [(203, "Мой папа тут главный")], "wondering about the girl's comments"),
    ("anya", "Потому что наш шеф — её родной папа!",
     "Because our chef is her own dad!",
     [(204, "Ты что, дочка шефа")], "revealing the surprising truth"),
    ("max", "Неужели шеф — твой близкий родственник?",
     "Can it be that the chef is your close relative?",
     [(206, "Получается, ты и родственница шефа")], "reacting with shock"),
    ("anya", "Это совершенно не твоё дело, Макс!",
     "That is completely none of your business, Max!",
     [(207, "Не твое дело")], "shutting down his inquiry"),
    ("max", "Теперь я понимаю многие странные вещи.",
     "Now I understand many strange things.",
     [], "piecing together the workplace dynamics"),
    ("anya", "Иди на кухню и работай молча!",
     "Go to the kitchen and work quietly!",
     [(208, "Ладно, я пошел")], "ordering him back to work"),
]

OPENER = "Let's review how Max discovers the surprising family connection of Victoria line by line."

WALK = [
    (0, None,
     "'Vika, pour a little water, please.' Max makes a polite request using an imperative verb and a genitive quantifier."),
    (1, None,
     "'Kostya will pour for you, and I have no time.' Victoria dismisses him with a future tense verb and the negative predicative."),
    (2, None,
     "'Wow, I did not know about your children!' Max expresses surprise using an interjection and a past tense verb."),
    (3, None,
     "'This is not my daughter, but my niece.' Victoria corrects his assumption with an adversative conjunction and family terms."),
    (4, None,
     "'She looks very much like you externally.' Max points out physical similarities with a short form adjective."),
    (5, None,
     "'Her name is Alice, and she is a good girl.' Victoria introduces the child with a standard naming construction."),
    (6, None,
     "'And why is she talking about our chef?' Max questions the mention of Barinov using an interrogative adverb."),
    (7, None,
     "'Because our chef is her own dad!' Victoria reveals the startling truth with an explanatory conjunction."),
    (8, None,
     "'Can it be that the chef is your close relative?' Max expresses disbelief using a modal particle of surprise."),
    (9, None,
     "'That is completely none of your business, Max!' Victoria deflects his curiosity with a firm defensive retort."),
    (10, None,
     "'Now I understand many strange things.' Max reflects on past events using a present tense verb and an accusative noun."),
    (11, None,
     "'Go to the kitchen and work quietly!' Victoria sends him back to cooking duties with two imperative verbs."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about unexpected relatives, family resemblances, and workplace secrets in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Иди на кухню и работай молча!")
