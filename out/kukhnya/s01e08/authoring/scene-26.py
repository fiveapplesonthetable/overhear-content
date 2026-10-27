"""s01e08 scene 26: Неожиданная встреча (An Unexpected Encounter)."""

ID = "kukhnya-s01e08-scene-26"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 26
TITLE = "Неожиданная встреча  (An Unexpected Encounter)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Айнура",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "After walking out on the Claude Monet kitchen, Chef Barinov is hiding in a dark storage room with a bottle. "
    "Ainura, the restaurant cleaner, stumbles upon his hiding place and catches him by surprise. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Здравствуй, шеф.",
     "Hello, Chef.",
     [(311, "Здравствуй")], "discovering hideout"),
    ("anya", "Вот ты где прячешься!",
     "Here is where you are hiding!",
     [], "finding him"),
    ("chef", "Айнура, это ты?",
     "Ainura, is that you?",
     [(312, "Ай, нура.")], "surprised recognition"),
    ("chef", "Не шуми, пожалуйста, так громко.",
     "Do not make noise so loudly, please.",
     [], "shushing her"),
    ("anya", "Я долго искала тебя везде.",
     "I looked for you everywhere for a long time.",
     [], "explaining search"),
    ("chef", "Садись рядом, выпьешь со мной?",
     "Sit down next to me, want a drink with me?",
     [(313, "Выпьешь?")], "offering drink"),
    ("anya", "Ой, шеф, я же на работе!",
     "Oh, Chef, I am at work after all!",
     [(314, "я же на работе.")], "refusing politely"),
    ("anya", "Мне ещё нужно мыть полы.",
     "I still need to wash the floors.",
     [], "mentioning chores"),
    ("chef", "Бросай работу, отдохни немного.",
     "Drop the work, rest a little.",
     [], "urging to relax"),
    ("anya", "Ты сидишь один в темноте.",
     "You are sitting alone in the dark.",
     [], "observing gloom"),
    ("chef", "Здесь тихо и никто не мешает.",
     "It is quiet here and nobody bothers me.",
     [], "enjoying solitude"),
    ("anya", "Но тебе нельзя здесь оставаться.",
     "But you cannot stay here.",
     [], "insisting he leave"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Здравствуй, шеф.",
     "'Hello, Chef.' — a simple respectful greeting to an employer."),
    (1, "Вот ты где прячешься!",
     "'Here is where you are hiding!' — using the pointing particle to highlight a location."),
    (2, "Айнура, это ты?",
     "'Ainura, is that you?' — a short question expressing recognition and surprise."),
    (3, "Не шуми, пожалуйста, так громко.",
     "'Do not make noise so loudly, please.' — a polite negative imperative asking for silence."),
    (4, "Я долго искала тебя везде.",
     "'I looked for you everywhere for a long time.' — past tense verb followed by time and place adverbs."),
    (5, "Садись рядом, выпьешь со мной?",
     "'Sit down next to me, want a drink with me?' — an imperative verb followed by an informal future offer."),
    (6, "Ой, шеф, я же на работе!",
     "'Oh, Chef, I am at work after all!' — an emphatic reminder of professional duties during a shift."),
    (7, "Мне ещё нужно мыть полы.",
     "'I still need to wash the floors.' — a dative necessity structure with an infinitive."),
    (8, "Бросай работу, отдохни немного.",
     "'Drop the work, rest a little.' — consecutive imperative verbs urging someone to take a break."),
    (9, "Ты сидишь один в темноте.",
     "'You are sitting alone in the dark.' — a descriptive observation of solitude in a prepositional phrase."),
    (10, "Здесь тихо и никто не мешает.",
     "'It is quiet here and nobody bothers me.' — an impersonal predicate paired with a negative pronoun."),
    (11, "Но тебе нельзя здесь оставаться.",
     "'But you cannot stay here.' — a modal dative construction expressing prohibition."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("anya", "Ой, шеф, я же на работе!")
