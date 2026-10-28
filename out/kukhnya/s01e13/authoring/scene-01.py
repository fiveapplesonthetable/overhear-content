"""s01e13 scene 01: Следующий шаг (The Next Step)."""

ID = "kukhnya-s01e13-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 13
SCENE = 1
TITLE = "Следующий шаг  (The Next Step)"
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
SOURCE_NAME = "Кухня (Kukhnya) S1.13"
SOURCE_FILE = "sources/kukhnya/s01/e13.ru.dual.srt"

INTRO = (
    "At the bar in Claude Monet, Nastya approaches Kostya with a sweet proposition: "
    "she wants to spend the evening at his apartment to take the next step in their romance. "
    "Delighted and flustered, Kostya rushes off to buy candles to make the night special. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Костя, что ты сейчас делаешь?",
     "Kostya, what are you doing right now?",
     [(1, "Что делаешь?")], "asking activity"),
    ("kostya", "Я стою и натираю бокалы.",
     "I am standing and polishing glasses.",
     [(2, "Стою, бокал натираю.")], "explaining duty"),
    ("anya", "А я хочу остаться у тебя сегодня.",
     "And I want to stay at your place today.",
     [(3, "хочу остаться у тебя?")], "proposing sleepover"),
    ("kostya", "У меня? Тебя кто-то выгнал?",
     "At my place? Did someone kick you out?",
     [(4, "Тебя что, Саша выгнала?")], "asking playfully"),
    ("anya", "Нет, нам пора сделать следующий шаг.",
     "No, it is time for us to take the next step.",
     [(5, "нам уже пора сделать следующий шаг.")], "explaining romantic intent"),
    ("kostya", "Ты хочешь выйти замуж?",
     "Do you want to get married?",
     [(6, "Жениться, что ли?")], "guessing wildly"),
    ("anya", "Костик, ты такой смешной!",
     "Kostik, you are so funny!",
     [(7, "Костик такой смешной.")], "teasing fondly"),
    ("anya", "Мы просто проведём этот вечер вместе.",
     "We will simply spend this evening together.",
     [(8, "сегодня вечером мы с тобой...")], "clarifying plan"),
    ("kostya", "И мы никому ничего не скажем?",
     "And we will not tell anyone anything?",
     [(13, "а мы никому ничего не скажем?")], "seeking reassurance"),
    ("anya", "Это будет наш маленький секрет.",
     "This will be our little secret.",
     [(16, "и мы никому ничего не скажем.")], "agreeing on privacy"),
    ("kostya", "Отлично, это звучит очень логично.",
     "Great, that sounds very logical.",
     [(17, "Логично.")], "approving idea"),
    ("kostya", "Я быстро куплю красивые свечи.",
     "I will quickly buy beautiful candles.",
     [(18, "аромасвечки куплю")], "planning ambiance"),
    ("anya", "Хорошо, сделай этот вечер волшебным!",
     "Good, make this evening magical!",
     [(20, "Чтобы все было волшебно.")], "giving encouragement"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Костя, что ты сейчас делаешь?",
     "'Kostya, what are you doing right now?' — informal present tense question with a temporal adverb."),
    (2, "А я хочу остаться у тебя сегодня.",
     "'And I want to stay at your place today.' — modal desire governing a reflexive perfective infinitive."),
    (4, "Нет, нам пора сделать следующий шаг.",
     "'No, it is time for us to take the next step.' — impersonal predicative construction with an accusative object."),
    (5, "Ты хочешь выйти замуж?",
     "'Do you want to get married?' — idiomatic verbal expression for a woman getting married."),
    (6, "Костик, ты такой смешной!",
     "'Kostik, you are so funny!' — affectionate diminutive vocative followed by an exclamatory phrase."),
    (7, "Мы просто проведём этот вечер вместе.",
     "'We will simply spend this evening together.' — future perfective verb governing an accusative time phrase."),
    (8, "И мы никому ничего не скажем?",
     "'And we will not tell anyone anything?' — negative future sentence with double negative pronouns."),
    (9, "Это будет наш маленький секрет.",
     "'This will be our little secret.' — demonstrative pronoun subject with future copular predicate."),
    (11, "Я быстро куплю красивые свечи.",
     "'I will quickly buy beautiful candles.' — first person singular future verb with an accusative object."),
    (12, "Хорошо, сделай этот вечер волшебным!",
     "'Good, make this evening magical!' — informal imperative verb governing an instrumental adjective."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around the next step, and for the words meaning 'are you doing' and 'am standing'. You'll catch them now. See you next time."
CLOSING = ("anya", "Хорошо, сделай этот вечер волшебным!")
