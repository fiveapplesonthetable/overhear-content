ID = "kukhnya-s01e02-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "Опоздание на смену  (Late for the Shift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 7-22. Max arrives late to the kitchen, causing Chef Viktor Barinov to win a bet against the kitchen staff. "
    "In response, the chef sarcastically assigns Max to heavy unloading duty instead of actual cooking."
)

INTRO = (
    "Max arrives two hours late to his morning shift at Claude Monet, sending the kitchen into a flurry. "
    "Head chef Viktor Barinov celebrates winning a betting pool on Max's tardiness and collects money from the cooks. "
    "As punishment, Barinov refuses to let Max cook, assigning him to unload heavy deliveries all day. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("chef", "Лавров, ты опоздал на два часа!",
     "Lavrov, you are two hours late!",
     [(9, "ты опоздал на два часа")], ""),
    ("chef", "Он опоздал, значит, я выиграл спор!",
     "He is late, meaning I won the bet!",
     [(12, "Он опоздал, я выиграл")], "adapted"),
    ("chef", "Все, кто ставил, скидывайтесь быстро!",
     "Everyone who bet, pay up quickly!",
     [(13, "Все, кто ставил, скидывайтесь"), (14, "Быстро, быстро")], ""),
    ("anya", "Шеф, простите, я попал в пробку.",
     "Chef, forgive me, I got stuck in a traffic jam.",
     [], "new"),
    ("chef", "Ты поднял мне настроение сегодня утром.",
     "You lifted my mood this morning.",
     [(15, "ты мне поднял настроение")], "adapted"),
    ("chef", "Поэтому я награждаю тебя важным делом.",
     "Therefore I reward you with an important task.",
     [(16, "я тебя награждаю очень важным")], "adapted"),
    ("chef", "Ты будешь целый день разгружать продукты!",
     "You will unload groceries the whole day!",
     [(17, "Ты будешь разгружать продукты")], "adapted"),
    ("anya", "Шеф, но я думал, я буду готовить.",
     "Chef, but I thought I would be cooking.",
     [(19, "Шеф, я думал, я буду готовить")], ""),
    ("chef", "Ты приписал себе две несуществующие способности!",
     "You credited yourself with two non-existent abilities!",
     [(20, "приписал себе две несуществующие способности")], ""),
    ("chef", "Способность думать и способность готовить!",
     "The ability to think and the ability to cook!",
     [(21, "Думать и готовить")], "adapted"),
    ("anya", "Я очень хорошо учился в кулинарном колледже.",
     "I studied very well at the culinary college.",
     [], "new"),
    ("chef", "А здесь ресторан, а не твой колледж!",
     "And here is a restaurant, not your college!",
     [], "new"),
    ("chef", "А ну живо иди работать, огузок!",
     "Now go to work immediately, oguzok!",
     [(22, "А ну, мах")], "adapted"),
]

OPENER = "Now let's examine Chef Barinov and Max's heated kitchen exchange line by line."

WALK = [
    (0, None,
     "'Lavrov, you are two hours late!' The chef confronts Max with a past tense verb and duration phrase."),
    (1, None,
     "'He is late, meaning I won the bet!' Barinov gloats to the staff using a parenthetical conjunction and past verb."),
    (2, None,
     "'Everyone who bet, pay up quickly!' The chef demands his winnings using an imperative reflexive verb."),
    (3, None,
     "'Chef, forgive me, I got stuck in a traffic jam.' Max apologizes humbly with an imperative verb and idiomatic excuse."),
    (4, None,
     "'You lifted my mood this morning.' Barinov speaks with heavy irony using a past transitive verb."),
    (5, None,
     "'Therefore I reward you with an important task.' The head chef mocks Max using an instrumental reward construction."),
    (6, None,
     "'You will unload groceries the whole day!' Barinov delivers the punishment with an imperfective future verb."),
    (7, None,
     "'Chef, but I thought I would be cooking.' Max protests politely with past and future verbs."),
    (8, None,
     "'You credited yourself with two non-existent abilities!' Barinov ridicules him with a past perfective verb."),
    (9, None,
     "'The ability to think and the ability to cook!' The chef lists the missing skills with paired infinitives."),
    (10, None,
     "'I studied very well at the culinary college.' Max defends his credentials using a past reflexive verb."),
    (11, None,
     "'And here is a restaurant, not your college!' The chef draws a firm line with contrastive conjunctions."),
    (12, None,
     "'Now go to work immediately, oguzok!' Barinov barks his signature insult using imperative verbs."),
]

TRANSITION = "Now let's listen to the kitchen reprimand again without interruption."
OUTRO = (
    "Barinov sends Max off to unload boxes of provisions in disgrace. "
    "In the next scene, waitress Nastya rushes into the kitchen with startling news."
)
CLOSING = ("chef", "А ну живо иди работать, огузок!")
