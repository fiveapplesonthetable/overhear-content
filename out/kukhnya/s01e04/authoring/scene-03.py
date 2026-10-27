ID = "kukhnya-s01e04-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = "Сон на смене  (Asleep on the Shift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 20-35. During a frantic lunch rush at Claude Monet, Chef Viktor Barinov discovers "
    "Max sound asleep in the back storage room on a stack of vegetable crates."
)

INTRO = (
    "During a high-pressure rush at Claude Monet, Chef Viktor Barinov barks orders across the kitchen line. "
    "Noticing that Max is missing from his station, Barinov searches the back storage area and discovers him sound asleep on vegetable crates. "
    "Caught red-handed, Max struggles to excuse his midday nap. "
    "Let's listen to their fiery confrontation in Russian first."
)

STORY = [
    ("chef", "На кухне сегодня страшная спешка!",
     "There is a terrible rush in the kitchen today!",
     [(21, "Быстрее, девочки, двигаемся")], "adapted"),
    ("anya", "Шеф, я не слышал ваших криков.",
     "Chef, I did not hear your shouts.",
     [], "new"),
    ("chef", "Ты что здесь делаешь в темноте?",
     "What are you doing here in the dark?",
     [(24, "Ты что здесь шляешься")], "adapted"),
    ("anya", "Я просто прилёг на пять минут.",
     "I simply lay down for five minutes.",
     [(34, "прилег на пять минут заснуть")], "adapted"),
    ("chef", "Огузок, ты спишь прямо на ящиках?!",
     "Oguzok, are you sleeping right on the crates?!",
     [(33, "Ты что здесь дрыхнешь")], "adapted"),
    ("anya", "Простите, шеф, я очень сильно устал.",
     "Forgive me, chef, I was very tired.",
     [], "new"),
    ("chef", "У тебя идёт дневная рабочая смена!",
     "You have a daytime work shift going on!",
     [], "new"),
    ("anya", "Я не мог заснуть всю ночь.",
     "I could not fall asleep all night.",
     [(35, "Всю ночь не мог")], "adapted"),
    ("chef", "Меня совершенно не волнуют твои ночи.",
     "Your nights do not concern me at all.",
     [], "new"),
    ("anya", "Наверное, у меня сложная акклиматизация.",
     "Probably I have difficult acclimatization.",
     [(35, "акклиматизация, наверное")], "adapted"),
    ("chef", "Какая ещё к чёрту акклиматизация?!",
     "What on earth kind of acclimatization?!",
     [], "new"),
    ("chef", "А ну живо вставай и иди работать!",
     "Now get up immediately and go to work!",
     [], "new"),
    ("anya", "Уже встаю, шеф, всё понял.",
     "Already getting up, chef, understood everything.",
     [], "new"),
]

OPENER = "Now let's examine Barinov and Max's heated storage room exchange line by line."

WALK = [
    (0, None,
     "'There is a terrible rush in the kitchen today!' Barinov barks about kitchen urgency with an exclamatory phrase."),
    (1, None,
     "'Chef, I did not hear your shouts.' Max speaks apologetically with a genitive plural noun."),
    (2, None,
     "'What are you doing here in the dark?' Barinov confronts him sharply in the dim backroom."),
    (3, None,
     "'I simply lay down for five minutes.' Max makes an innocent excuse using a past perfective verb."),
    (4, None,
     "'Oguzok, are you sleeping right on the crates?!' Barinov expresses outrage using an emphatic particle and prepositional plural."),
    (5, None,
     "'Forgive me, chef, I was very tired.' Max asks for pardon with an imperative and past verb."),
    (6, None,
     "'You have a daytime work shift going on!' The chef reminds him of his duties with a present active verb."),
    (7, None,
     "'I could not fall asleep all night.' Max explains his fatigue using an accusative duration phrase."),
    (8, None,
     "'Your nights do not concern me at all.' Barinov rejects personal excuses with an imperfective present verb."),
    (9, None,
     "'Probably I have difficult acclimatization.' Max attempts a humorous medical defense with a predicate noun."),
    (10, None,
     "'What on earth kind of acclimatization?!' Barinov explodes with an idiomatic exclamation of disbelief."),
    (11, None,
     "'Now get up immediately and go to work!' The head chef drives Max back into action with paired imperatives."),
    (12, None,
     "'Already getting up, chef, understood everything.' Max quickly complies with a present active verb and past agreement."),
]

TRANSITION = "Now let's listen to the storage room reprimand again without interruption."
OUTRO = (
    "Max scrambles back to his station under Barinov's watchful glare. "
    "In the next scene, the kitchen staff reacts to rumors about defecting to the rival restaurant."
)
CLOSING = ("anya", "Уже встаю, шеф, всё понял.")
