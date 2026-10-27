"""s01e10 scene 19: Маленькая победа (A Small Victory)."""

ID = "kukhnya-s01e10-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 19
TITLE = "Маленькая победа  (A Small Victory)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Лёва", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 153-155. Chef Barinov returns to the kitchen clutching the cash for the caviar, gloating to Lyova that his gamble will pay off."

INTRO = (
    "Clutching the envelope of cash intended for caviar, Chef Barinov triumphantly returns to the kitchen in high spirits. "
    "Convinced his secret sports gamble will pay off handsomely, he proudly shares his excitement with his sous-chef, Lyova. "
    "Let's listen to their brief exchange in Russian."
)

STORY = [
    ("chef", "Это просто настоящий праздник какой-то!", "This is simply some kind of real holiday!",
     [(153, "Это просто праздник какой-то")], ""),
    ("anya", "Шеф, почему вы так радостно улыбаетесь?", "Chef, why are you smiling so joyfully?",
     [], ""),
    ("chef", "Всё складывается даже лучше наших планов.", "Everything is turning out even better than our plans.",
     [], ""),
    ("anya", "Вы уже решили проблему с плитой?", "Have you already solved the problem with the stove?",
     [], ""),
    ("chef", "Плита вернётся на кухню вовремя, Лёва.", "The stove will return to the kitchen on time, Lyova.",
     [], ""),
    ("chef", "Не говори потом, что я не слушаю.", "Do not say later that I do not listen.",
     [(154, "Не говори потом")], ""),
    ("anya", "Я просто переживаю за вечерний сервис.", "I am simply worried about the evening service.",
     [], ""),
    ("chef", "Сегодня вечером наш ресторан заработает состояние.", "Tonight our restaurant will make a fortune.",
     [], ""),
    ("anya", "Ладно, шеф, я вернусь к работе.", "All right, chef, I will get back to work.",
     [(155, "Ладно")], ""),
    ("chef", "Иди и проследи за горячим цехом.", "Go and supervise the hot kitchen section.",
     [], ""),
    ("anya", "Сделаю всё в лучшем виде, шеф.", "I will do everything in the best way, chef.",
     [], ""),
    ("chef", "Вот это правильный и бодрый настрой.", "Now that is the right and cheerful attitude.",
     [], ""),
]

OPENER = "Let's examine how Chef Barinov celebrates his sudden financial windfall and gives directions to his sous-chef."

WALK = [
    (0, None,
     "'This is simply some kind of real holiday!' An enthusiastic exclamatory expression used to celebrate unexpected good fortune for the speaker."),
    (4, None,
     "'The stove will return to the kitchen on time, Lyova.' A confident future tense promise meant to ease a colleague's worry about work."),
    (6, None,
     "'Do not say later that I do not listen.' A defensive negative imperative reminding a partner of past advice and decisions."),
    (8, None,
     "'Tonight our restaurant will make a fortune.' An optimistic predictive statement expressing high expectations of success for the business."),
]

TRANSITION = "Now, let's hear Chef Barinov celebrate his small triumph once more."

OUTRO = (
    "Now you know how to express celebration, discuss kitchen readiness, and encourage colleagues in Russian. "
    "Keep practicing these positive conversational phrases as you continue learning."
)

CLOSING = ("chef", "Удача сегодня на нашей стороне.")
