"""s01e10 scene 31: Секретный рецепт (The Secret Recipe)."""

ID = "kukhnya-s01e10-scene-31"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 31
TITLE = "Секретный рецепт  (The Secret Recipe)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "fedya": "anja",
}
LABELS = {
    "anya": "Сеня",
    "fedya": "Федя",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"

INTRO = (
    "In the kitchen of Claude Monet, cooks Senya and Fedya have bought cheap pike caviar to replace sturgeon caviar. "
    "To pull off the trick, Senya prepares special food dye to turn the golden caviar pitch black. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("fedya", "Сеня, ты уверен в этой идее?",
     "Senya, are you sure about this idea?",
     [], "expressing doubt"),
    ("anya", "Конечно, это гениальный план!",
     "Of course, this is a brilliant plan!",
     [], "boasting confidence"),
    ("fedya", "Она же совсем жёлтая, как песок.",
     "It is completely yellow, like sand.",
     [], "pointing at color"),
    ("anya", "Сейчас мы её аккуратно покрасим.",
     "Now we will carefully dye it.",
     [(207, "Давай")], "explaining method"),
    ("fedya", "Какой краской ты будешь красить?",
     "What dye will you paint it with?",
     [], "asking about dye"),
    ("anya", "У меня есть специальный чёрный краситель.",
     "I have a special black food coloring.",
     [], "revealing ingredient"),
    ("fedya", "А гости ничего не заметят?",
     "And the guests will not notice anything?",
     [], "worrying about discovery"),
    ("anya", "Они подумают, что это дорогая икра.",
     "They will think that this is expensive caviar.",
     [], "reassuring friend"),
    ("fedya", "Тогда давай быстро начнём работу.",
     "Then let us quickly begin the work.",
     [], "agreeing to help"),
    ("anya", "Бери большую ложку и перемешивай.",
     "Take the big spoon and stir.",
     [], "directing action"),
    ("fedya", "Смотри, цвет уже начинает меняться.",
     "Look, the color is already starting to change.",
     [], "observing result"),
    ("anya", "Отлично, получается настоящая осетровая икра!",
     "Excellent, it is turning out like real sturgeon caviar!",
     [], "celebrating progress"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Сеня, ты уверен в этой идее?",
     "'Senya, are you sure about this idea?' — short adjective expressing certainty with a prepositional object."),
    (1, "Конечно, это гениальный план!",
     "'Of course, this is a brilliant plan!' — emphatic introductory word followed by a demonstrative clause."),
    (3, "Сейчас мы её аккуратно покрасим.",
     "'Now we will carefully dye it.' — future perfective verb with an adverb of manner."),
    (5, "У меня есть специальный чёрный краситель.",
     "'I have a special black food coloring.' — standard Russian possessive structure in the nominative."),
    (6, "А гости ничего не заметят?",
     "'And the guests will not notice anything?' — negative pronoun with a future perfective verb."),
    (7, "Они подумают, что это дорогая икра.",
     "'They will think that this is expensive caviar.' — future verb introducing an indirect statement."),
    (9, "Бери большую ложку и перемешивай.",
     "'Take the big spoon and stir.' — two consecutive imperative verbs directing food preparation."),
    (10, "Смотри, цвет уже начинает меняться.",
     "'Look, the color is already starting to change.' — imperative calling attention to an active change."),
    (11, "Отлично, получается настоящая осетровая икра!",
     "'Excellent, it is turning out like real sturgeon caviar!' — predicative adverb with a reflexive verb."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("anya", "Отлично, получается настоящая осетровая икра!")
