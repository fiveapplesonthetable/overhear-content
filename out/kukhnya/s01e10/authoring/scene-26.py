ID = "kukhnya-s01e10-scene-26"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 26
TITLE = "Серьёзный разговор  (A Serious Talk)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 188. Overhearing the shocking gossip about Victoria's pregnancy in the corridor, "
    "Chef Viktor sternly orders Max to follow him into his office for a private talk."
)

INTRO = (
    "In the corridor outside the bustling kitchen, Chef Viktor Petrovich overhears Max "
    "speaking about Victoria. Stunned by what he hears, the head chef immediately grabs "
    "the bewildered young cook and marches him into his private office for an urgent confrontation. "
    "Let us listen to their tense exchange in Russian first."
)

STORY = [
    ("chef", "Пойдём со мной в мой кабинет.",
     "Come with me into my office.",
     [(188, "пойдем со мной")], "adapted"),
    ("anya", "Шеф, куда мы сейчас идём?",
     "Chef, where are we going now?",
     [], "new"),
    ("chef", "Нам нужен очень серьёзный разговор.",
     "We need a very serious conversation.",
     [], "new"),
    ("anya", "Вы всё слышали на кухне?",
     "Did you hear everything in the kitchen?",
     [], "new"),
    ("chef", "Я слышал каждое твоё слово.",
     "I heard every word of yours.",
     [], "new"),
    ("anya", "Я сам ничего не понимаю.",
     "I myself do not understand anything.",
     [], "new"),
    ("chef", "Ты устроил настоящий большой скандал.",
     "You caused a real big scandal.",
     [], "new"),
    ("anya", "Я не хотел никого обидеть.",
     "I did not want to offend anyone.",
     [], "new"),
    ("chef", "Заходи в комнату и закрой дверь.",
     "Go into the room and close the door.",
     [], "new"),
    ("anya", "Хорошо, я уже закрываю дверь.",
     "Good, I am already closing the door.",
     [], "new"),
    ("chef", "Сядь на стул и слушай меня.",
     "Sit on a chair and listen to me.",
     [], "new"),
    ("anya", "Я внимательно слушаю вас, шеф.",
     "I am listening to you attentively, chef.",
     [], "new"),
    ("chef", "Теперь твоя жизнь сильно изменится.",
     "Now your life will change greatly.",
     [], "new"),
]

OPENER = "Now let us examine the dialogue between Chef Viktor and Max line by line."

WALK = [
    (0, None,
     "'Come with me into my office.' -- Viktor commands Max to follow him for a private discussion."),
    (1, None,
     "'Chef, where are we going now?' -- The cook nervously asks where they are heading."),
    (2, None,
     "'We need a very serious conversation.' -- The chef insists that they must speak urgently."),
    (3, None,
     "'Did you hear everything in the kitchen?' -- Max asks if Viktor overheard the scandalous news."),
    (4, None,
     "'I heard every word of yours.' -- The chef confirms that he heard the entire revelation."),
    (5, None,
     "'I myself do not understand anything.' -- Max confesses that he feels completely overwhelmed."),
    (6, None,
     "'You caused a real big scandal.' -- Viktor points out that the boy has triggered major chaos."),
    (7, None,
     "'I did not want to offend anyone.' -- The young man insists that he meant no harm."),
    (8, None,
     "'Go into the room and close the door.' -- The chef orders privacy before addressing the matter."),
    (9, None,
     "'Good, I am already closing the door.' -- Max complies obediently with the command."),
    (10, None,
     "'Sit on a chair and listen to me.' -- Viktor tells him to sit down and pay close attention."),
    (11, None,
     "'I am listening to you attentively, chef.' -- The young cook prepares to receive stern advice."),
    (12, None,
     "'Now your life will change greatly.' -- Viktor ominously predicts significant changes ahead."),
]

TRANSITION = "Now let us listen to the tense conversation once again without interruption."
OUTRO = (
    "With the office door firmly shut, Viktor Petrovich prepares to give Max a stern lecture "
    "on family responsibilities and the chaotic consequences of his actions."
)
CLOSING = ("chef", "Теперь твоя жизнь сильно изменится.")
