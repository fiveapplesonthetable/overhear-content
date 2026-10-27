"""s01e05 scene 08: Звонок от мамы (Call from Mom)."""

ID = "kukhnya-s01e05-scene-08"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = "Звонок от мамы  (Call from Mom)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Макс", "senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = (
    "In the noisy restaurant kitchen, cook Senya calls Max over to answer an unexpected phone call. "
    "Senya claims Max's mother is calling all the way from Voronezh. "
    "Max takes the phone and pretends to chat with his mom while secretly receiving cooking instructions for a complicated fish dish. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("senya", "Лавров, возьми трубку, это тебя!",
     "Lavrov, pick up the receiver, it is for you!",
     [(122, "Лавров, тебя")], "calling Max to the phone"),
    ("anya", "Кто звонит мне на кухню?",
     "Who is calling me in the kitchen?",
     [(124, "Кто? Мама?")], "asking in surprise"),
    ("senya", "Говорят, что звонит твоя мама.",
     "They say that your mother is calling.",
     [(123, "Мама")], "explaining who is calling"),
    ("anya", "Мама? Откуда она знает этот номер?",
     "Mom? How does she know this number?",
     [(125, "А откуда она знает этот номер")], "wondering how she got the number"),
    ("senya", "Ответь скорее и спроси сам.",
     "Answer quickly and ask yourself.",
     [], "urging him to answer"),
    ("anya", "Алло, мама? Да, я слушаю.",
     "Hello, Mom? Yes, I am listening.",
     [(126, "Алло, мама? Да, мама я")], "picking up the phone"),
    ("anya", "Форель с жульеном? Понял, мамуля.",
     "Trout with julienne? Understood, Mommy.",
     [(127, "Будешь готовить форель с обычным жильеном")], "listening to recipe instructions"),
    ("anya", "Сначала удалить хребет и охладить филе?",
     "First remove the backbone and chill the fillet?",
     [(128, "выпотроши рыбу, удали хребет")], "repeating the culinary steps"),
    ("anya", "Спасибо за совет, целую тебя!",
     "Thank you for the advice, kisses!",
     [(131, "Целую тебя пока")], "thanking the caller"),
    ("anya", "Я перезвоню вечером, сейчас очень занят.",
     "I will call back in the evening, I am very busy now.",
     [(130, "Да я тебе попозже перезвоню")], "hanging up quickly"),
    ("senya", "Твоя мама отлично разбирается в рыбе?",
     "Does your mother understand fish well?",
     [(132, "Мама из Воронежа")], "asking curiously"),
    ("anya", "Да, в Воронеже все любят рыбу!",
     "Yes, in Voronezh everyone loves fish!",
     [(133, "Ну да")], "covering up the secret"),
]

OPENER = "Let's review this humorous kitchen conversation line by line."

WALK = [
    (0, None,
     "'Lavrov, pick up the receiver, it is for you!' Senya calls Max to answer the kitchen landline."),
    (1, None,
     "'Who is calling me in the kitchen?' Max is surprised that anyone would reach him at work."),
    (2, None,
     "'They say that your mother is calling.' Senya relays the message from the other end of the line."),
    (3, None,
     "'Mom? How does she know this number?' Max wonders how his mother could possibly know the kitchen number."),
    (4, None,
     "'Answer quickly and ask yourself.' Senya hands over the receiver with an impatient grin."),
    (5, None,
     "'Hello, Mom? Yes, I am listening.' Max speaks cautiously into the receiver."),
    (6, None,
     "'Trout with julienne? Understood, Mommy.' Max pretends to chat with his mother while hearing the recipe."),
    (7, None,
     "'First remove the backbone and chill the fillet?' Max repeats the key culinary instructions as if they were family news."),
    (8, None,
     "'Thank you for the advice, kisses!' Max wraps up the suspicious call with affectionate words."),
    (9, None,
     "'I will call back in the evening, I am very busy now.' Max quickly hangs up before anyone overhears too much."),
    (10, None,
     "'Does your mother understand fish well?' Senya questions Max with mild suspicion."),
    (11, None,
     "'Yes, in Voronezh everyone loves fish!' Max invents a quick excuse to protect his secret."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Max cleverly avoids suspicion in the kitchen and memorizes the recipe for the trout dish. "
    "See you next time!"
)

CLOSING = ("anya", "Да, в Воронеже все любят рыбу!")
