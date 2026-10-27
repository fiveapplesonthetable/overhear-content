"""s01e10 scene 12: Странное поведение Макса (Max's Strange Behavior)."""

ID = "kukhnya-s01e10-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 12
TITLE = "Странное поведение Макса  (Max's Strange Behavior)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Вика", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 88-94. Victoria grills bartender Kostya about why Max is acting awkwardly, and Kostya accidentally lets slip that Max is hiding from her."

INTRO = (
    "At the restaurant bar counter, art director Victoria firmly interrogates bartender Kostya about his friend Max's awkward behavior. "
    "Kostya attempts to feign ignorance, but accidentally lets slip that Max is deliberately avoiding Victoria, instantly confirming her deepest suspicions. "
    "Let's listen to their tense exchange in Russian first."
)

STORY = [
    ("anya", "Костя, что происходит с нашим Максом?",
     "Kostya, what is happening with our Max?",
     [(88, "А что происходит с Максом")], "asking about Max's behavior"),
    ("kostya", "А что вообще происходит с Максом?",
     "And what is happening with Max at all?",
     [(89, "А что происходит с Максом")], "feigning ignorance"),
    ("anya", "Это я тебя сейчас прямо спрашиваю!",
     "It is I who is asking you directly right now!",
     [(89, "Нет, это я тебя спрашиваю")], "demanding a direct answer"),
    ("kostya", "Я честно ничего не знаю, Вика.",
     "I honestly know nothing, Vika.",
     [(90, "Я не знаю")], "claiming ignorance"),
    ("anya", "Он твой лучший друг в ресторане!",
     "He is your best friend in the restaurant!",
     [], "appealing to their close friendship"),
    ("kostya", "Он мне совершенно ничего не говорил.",
     "He told me absolutely nothing.",
     [(91, "Он мне ничего не говорил")], "denying any conversation"),
    ("anya", "Ты явно скрываешь от меня правду.",
     "You are clearly concealing the truth from me.",
     [], "accusing him of hiding things"),
    ("kostya", "Я не знаю, почему он прячется!",
     "I do not know why he is hiding!",
     [(91, "почему он от вас прячется")], "accidentally letting slip the truth"),
    ("anya", "То есть Макс прячется от меня?",
     "So that means Max is hiding from me?",
     [(92, "То есть он от меня прячется")], "catching the slip-up"),
    ("kostya", "Что? Нет! Кто вообще прячется?",
     "What? No! Who is hiding at all?",
     [(93, "Что? Нет. Кто")], "trying frantically to backtrack"),
    ("anya", "Костя, не пытайся меня обмануть сейчас!",
     "Kostya, do not try to deceive me right now!",
     [(94, "Костя? Да")], "warning him not to lie"),
    ("kostya", "Вика, я правда ничего не знаю!",
     "Vika, I truly know nothing!",
     [(94, "Да")], "pleading innocence"),
]

OPENER = "Let's review how Victoria questions Kostya in the dining room line by line."

WALK = [
    (0, None,
     "'Kostya, what is happening with our Max?' Victoria opens the inquiry with a present tense reflexive verb and an instrumental phrase."),
    (1, None,
     "'And what is happening with Max at all?' Kostya repeats her question evasively using an adverb of generality."),
    (2, None,
     "'It is I who is asking you directly right now!' Victoria asserts authority using an emphatic demonstrative pronoun."),
    (3, None,
     "'I honestly know nothing, Vika.' Kostya insists on total ignorance using an adverb of manner and a negative pronoun."),
    (4, None,
     "'He is your best friend in the restaurant!' Victoria points out their strong bond using a superlative adjective."),
    (5, None,
     "'He told me absolutely nothing.' The bartender defends himself using an intensifying adverb with a negative verb."),
    (6, None,
     "'You are clearly concealing the truth from me.' Victoria levels an accusation using an imperfective verb with a prepositional object."),
    (7, None,
     "'I do not know why he is hiding!' Kostya inadvertently reveals the truth with a subordinate clause."),
    (8, None,
     "'So that means Max is hiding from me?' Victoria seizes upon his admission with a connecting phrase."),
    (9, None,
     "'What? No! Who is hiding at all?' Kostya scrambles to retract his statement with frantic exclamations."),
    (10, None,
     "'Kostya, do not try to deceive me right now!' Victoria issues a firm warning using a negative imperative and an infinitive."),
    (11, None,
     "'Vika, I truly know nothing!' Kostya makes a desperate final plea using an adverb of truthfulness."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about evasive answers, secret avoidance, and direct questioning in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Костя, не пытайся меня обмануть сейчас!")
