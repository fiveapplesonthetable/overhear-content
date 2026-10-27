"""s01e09 scene 09: Тихий час в зале (Quiet Time in the Dining Room)."""

ID = "kukhnya-s01e09-scene-09"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 9
TITLE = "Тихий час в зале  (Quiet Time in the Dining Room)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "alisa": "anja"}
LABELS = {"anya": "Вика", "alisa": "Алиса"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 219-223. In the Claude Monet dining room, Victoria seats her niece Alisa at a corner table and asks her to behave quietly while she prepares for the arriving banquet."

INTRO = (
    "In the main dining room of Claude Monet, art director Victoria seats her energetic niece Alisa at a quiet corner table. "
    "With important banquet guests expected to arrive shortly, Victoria asks the little girl to play calmly and not cause any commotion in the restaurant. "
    "Let's listen to their gentle exchange in Russian first."
)

STORY = [
    ("anya", "Алиса, садись скорее за этот стол.",
     "Alice, sit down at this table quickly.",
     [(219, "Садись")], "seating the girl at a table"),
    ("alisa", "Тётя Вика, мы будем играть здесь?",
     "Aunt Vika, will we play here?",
     [], "asking about playtime"),
    ("anya", "Нет, мне нужно сейчас много работать.",
     "No, I need to work a lot right now.",
     [(220, "Алиса, мне нужно сейчас поработать")], "explaining work duties"),
    ("alisa", "А что мне делать одной тут?",
     "And what am I to do here alone?",
     [], "wondering how to pass the time"),
    ("anya", "Посиди тихонечко и спокойно поиграй.",
     "Sit quietly and play calmly.",
     [(221, "Ты, пожалуйста, посиди тихонечко, поиграй")], "asking for quiet behavior"),
    ("alisa", "Скоро придут важные гости ресторана?",
     "Will important restaurant guests arrive soon?",
     [], "asking about arriving visitors"),
    ("anya", "Да, скоро начнётся большой банкет.",
     "Yes, a big banquet will begin soon.",
     [], "confirming the upcoming event"),
    ("alisa", "Я обещаю вести себя очень хорошо.",
     "I promise to behave very well.",
     [(222, "И само спокойствие, тетя Вик")], "promising good behavior"),
    ("anya", "Ты меня точно не подведёшь сегодня?",
     "You definitely will not let me down today?",
     [], "verifying her commitment"),
    ("alisa", "Я буду само спокойствие, честное слово!",
     "I will be calmness itself, honest word!",
     [(222, "И само спокойствие")], "giving a solemn promise"),
    ("anya", "Ты настоящая умница, дорогая племянница.",
     "You are a real clever girl, dear niece.",
     [(223, "Умница, играй")], "praising her cooperation"),
    ("alisa", "Я просто буду тихо рисовать картинки.",
     "I will simply draw pictures quietly.",
     [], "explaining her planned activity"),
]

OPENER = "Let's examine how Victoria and little Alisa reach a calm agreement line by line."

WALK = [
    (0, None,
     "'Alice, sit down at this table quickly.' Victoria gives a direct instruction using an imperative verb and an accusative prepositional phrase."),
    (1, None,
     "'Aunt Vika, will we play here?' Alisa eagerly inquires about activities using a compound future tense verb."),
    (2, None,
     "'No, I need to work a lot right now.' Victoria sets boundaries using a dative experiencer with a predicative."),
    (3, None,
     "'And what am I to do here alone?' The little girl wonders about spending time independently."),
    (4, None,
     "'Sit quietly and play calmly.' Victoria gently instructs her with two coordinating imperative verbs."),
    (5, None,
     "'Will important restaurant guests arrive soon?' Alisa asks about the expected visitors with a future tense verb."),
    (6, None,
     "'Yes, a big banquet will begin soon.' Victoria explains the upcoming occasion with an adjective and a noun."),
    (7, None,
     "'I promise to behave very well.' Alisa offers reassurance with a standard reflexive behavioral expression."),
    (8, None,
     "'You definitely will not let me down today?' Victoria playfully checks the girl's reliability with a perfective future verb."),
    (9, None,
     "'I will be calmness itself, honest word!' The niece quotes a playful idiom expressing total composure."),
    (10, None,
     "'You are a real clever girl, dear niece.' Victoria warmly praises the child with an affectionate noun phrase."),
    (11, None,
     "'I will simply draw pictures quietly.' Alisa settles into her seat with a calm creative plan."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about seating children, encouraging calm behavior, and preparing for events in Russian. "
    "See you next time!"
)

CLOSING = ("alisa", "Я просто буду тихо рисовать картинки.")
