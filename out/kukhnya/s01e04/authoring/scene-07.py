"""s01e04 scene 07: Костя влюбился (Kostya Is in Love)."""

ID = "kukhnya-s01e04-scene-07"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = "Костя влюбился  (Kostya Is in Love)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja", "kostya": "angelina"}
LABELS = {"anya": "Настя", "max": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = (
    "Near the bar of Claude Monet, Max notices bartender Kostya staring admiringly at waitress Nastya. "
    "Teasing his friend about his secret crush, Max pushes the nervous bartender to give Nastya a compliment. "
    "Listen to their playful conversation in Russian first."
)

STORY = [
    ("max", "Костя, посмотри на Настю.",
     "Kostya, look at Nastya.",
     [(59, "Костян, смотри")], "pointing out Nastya"),
    ("kostya", "Она очень красивая девушка.",
     "She is a very pretty girl.",
     [(61, "Красивое")], "admiring her"),
    ("max", "Она тебе нравится? Признайся честно!",
     "Do you like her? Admit it honestly!",
     [(62, "Она чё, тебе нравится")], "teasing his friend"),
    ("kostya", "Ну ладно, она мне очень нравится.",
     "Well all right, I like her very much.",
     [(64, "Костян втюрился")], "confessing his feelings"),
    ("max", "Тогда скажи ей приятный комплимент.",
     "Then give her a nice compliment.",
     [(68, "хочет сказать")], "encouraging action"),
    ("kostya", "Я боюсь, я не умею говорить.",
     "I am afraid, I cannot talk smoothly.",
     [(67, "Зачем")], "hesitating nervously"),
    ("anya", "Привет, мальчики! О чём вы говорите?",
     "Hi, boys! What are you talking about?",
     [(69, "Чё надо")], "approaching the bar"),
    ("max", "Костя хочет сказать тебе важные слова.",
     "Kostya wants to tell you important words.",
     [(68, "Тебе тут Костян что-то хочет сказать")], "putting Kostya on the spot"),
    ("kostya", "Настя, у тебя очень красивая причёска!",
     "Nastya, you have a very pretty hairstyle!",
     [(71, "очень красивая")], "blurting out a compliment"),
    ("anya", "Спасибо, Костя! Ты очень милый парень.",
     "Thank you, Kostya! You are a very sweet guy.",
     [], "smiling warmly"),
    ("kostya", "Ты слышал? Она назвала меня милым!",
     "Did you hear? She called me sweet!",
     [], "celebrating excitedly"),
    ("max", "Видишь? Главное — всегда быть смелым!",
     "See? The main thing is to always be brave!",
     [(74, "будь смелее")], "giving parting advice"),
]

OPENER = "Let's review this romantic encounter by the bar line by line."

WALK = [
    (0, None,
     "'Kostya, look at Nastya.' Max directs his friend's attention toward the dining room."),
    (1, None,
     "'She is a very pretty girl.' Kostya cannot hide his genuine admiration for the waitress."),
    (2, None,
     "'Do you like her? Admit it honestly!' Max playfully presses for a confession."),
    (3, None,
     "'Well all right, I like her very much.' Kostya finally admits his romantic feelings."),
    (4, None,
     "'Then give her a nice compliment.' Max urges him to take immediate initiative."),
    (5, None,
     "'I am afraid, I cannot talk smoothly.' Kostya struggles with sudden stage fright."),
    (6, None,
     "'Hi, boys! What are you talking about?' Nastya walks up and catches them whispering."),
    (7, None,
     "'Kostya wants to tell you important words.' Max leaves no room for his friend to back down."),
    (8, None,
     "'Nastya, you have a very pretty hairstyle!' Kostya delivers his compliment with nervous sincerity."),
    (9, None,
     "'Thank you, Kostya! You are a very sweet guy.' Nastya responds with genuine appreciation."),
    (10, None,
     "'Did you hear? She called me sweet!' Kostya turns to Max in pure astonishment."),
    (11, None,
     "'See? The main thing is to always be brave!' Max reminds him of the value of courage."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal speed."

OUTRO = (
    "Thrilled by Nastya's warm reaction, Kostya gains newfound confidence behind the bar. "
    "See you next time!"
)

CLOSING = ("max", "Видишь? Главное — всегда быть смелым!")
