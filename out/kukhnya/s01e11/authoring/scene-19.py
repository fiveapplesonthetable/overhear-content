"""s01e11 scene 19: Проблемный гость (A Difficult Guest)."""

ID = "kukhnya-s01e11-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 19
TITLE = "Проблемный гость  (A Difficult Guest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "kostya": "anja",
}
LABELS = {
    "anya": "Настя",
    "kostya": "Костя",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"

INTRO = (
    "At the bar in Claude Monet, Kostya tries to apologize to Nastya for their recent disagreement. "
    "Nastya is visibly stressed and explains that an influential restaurant critic at her table is bothering her, "
    "warning Kostya not to start a fight. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("kostya", "Настя, ну прости меня за вчерашнее.",
     "Nastya, please forgive me for yesterday.",
     [(232, "Ну, прости меня.")], "asking forgiveness"),
    ("anya", "Костя, сейчас вообще не до этого.",
     "Kostya, now is really not the time.",
     [(233, "Костя, давай потом поговорим, ладно?"), (234, "Сейчас вообще не до этого.")], "brushing off"),
    ("kostya", "Что случилось? У тебя проблемы?",
     "What happened? Do you have problems?",
     [], "asking reason"),
    ("anya", "У меня за столиком проблемный гость.",
     "I have a difficult guest at the table.",
     [(234, "У меня гость проблемный.")], "explaining trouble"),
    ("kostya", "Он что, хамит тебе?",
     "Is he being rude to you?",
     [(235, "Чего? Он что, хамит тебя, что ли?")], "getting suspicious"),
    ("anya", "Хуже. Он постоянно пристаёт ко мне.",
     "Worse. He is constantly bothering me.",
     [(236, "Он пристает ко мне.")], "confiding truth"),
    ("kostya", "Что? Я сейчас пойду разберусь!",
     "What? I will go sort it out right now!",
     [(237, "Чего? Сейчас я пойду с ним поговорю.")], "acting protective"),
    ("anya", "Костя, стой! Не ходи туда.",
     "Kostya, stop! Do not go there.",
     [(238, "Костя, не ходи никуда, ладно?")], "stopping him"),
    ("kostya", "Почему я должен стоять и смотреть?",
     "Why should I stand and watch?",
     [], "questioning inaction"),
    ("anya", "Этот человек — важный ресторанный критик.",
     "This man is an important restaurant critic.",
     [(239, "Это критик.")], "revealing identity"),
    ("kostya", "И что он может сделать?",
     "And what can he do?",
     [], "challenging influence"),
    ("anya", "Он может написать ужасную статью.",
     "He can write a terrible article.",
     [(240, "Потом знаешь, какую статью может написать на наш ресторан?")], "warning of consequences"),
    ("anya", "Сделай заказ быстрее, я пойду в зал.",
     "Make the order faster, I will go to the hall.",
     [(241, "Так что давай лучше сделай мне заказ побыстрее, и все.")], "urging haste"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Настя, ну прости меня за вчерашнее.",
     "'Nastya, please forgive me for yesterday.' — conversational imperative followed by a prepositional object."),
    (1, "Костя, сейчас вообще не до этого.",
     "'Kostya, now is really not the time.' — colloquial negative idiom expressing inappropriate timing."),
    (3, "У меня за столиком проблемный гость.",
     "'I have a difficult guest at the table.' — possessive prepositional construction with a descriptive noun."),
    (5, "Хуже. Он постоянно пристаёт ко мне.",
     "'Worse. He is constantly bothering me.' — comparative adverb paired with a verb of unwelcome attention."),
    (6, "Что? Я сейчас пойду разберусь!",
     "'What? I will go sort it out right now!' — interjection followed by future verbs of intention."),
    (7, "Костя, стой! Не ходи туда.",
     "'Kostya, stop! Do not go there.' — urgent negative imperative directed at an impulsive partner."),
    (9, "Этот человек — важный ресторанный критик.",
     "'This man is an important restaurant critic.' — demonstrative pronoun subject with an adjective phrase."),
    (11, "Он может написать ужасную статью.",
     "'He can write a terrible article.' — modal verb governing a perfective infinitive and accusative object."),
    (12, "Сделай заказ быстрее, я пойду в зал.",
     "'Make the order faster, I will go to the hall.' — compound sentence with imperative and future motion."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around a difficult guest, and for the words meaning 'forgive' and 'yesterday's'. You'll catch them now. See you next time."
CLOSING = ("anya", "Сделай заказ быстрее, я пойду в зал.")
