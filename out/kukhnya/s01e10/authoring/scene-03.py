ID = "kukhnya-s01e10-scene-03"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 3
TITLE = "Незнакомая гостья  (An Unknown Guest)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Костя", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 6. In the corridor outside the kitchen, bartender Kostya informs Chef Barinov "
    "that a young woman from television is asking to speak with him."
)

INTRO = (
    "In the corridor outside the bustling kitchen of Claude Monet, bartender Kostya approaches Chef Viktor Barinov "
    "with a message. An unfamiliar young woman has arrived at the restaurant specifically asking for the head chef, "
    "claiming to have an important proposal. Let's listen to their brief exchange in Russian first."
)

STORY = [
    ("anya", "Шеф, вас там какая-то девушка зовёт.",
     "Chef, some young woman is calling for you over there.",
     [(6, "Вас там какая-то девушка зовет.")], "adapted"),
    ("chef", "Кто она такая и что ей нужно?",
     "Who is she and what does she need?",
     [], "new"),
    ("anya", "Она сказала, что пришла с телевидения.",
     "She said that she came from television.",
     [], "new"),
    ("chef", "Я не хочу ни с кем говорить.",
     "I do not want to talk to anyone.",
     [], "new"),
    ("anya", "Она говорит, что дело очень важное.",
     "She says that the matter is very important.",
     [], "new"),
    ("chef", "У меня сейчас совершенно нет времени.",
     "I currently have absolutely no time.",
     [], "new"),
    ("anya", "Она ждёт вас возле главного входа.",
     "She is waiting for you near the main entrance.",
     [], "new"),
    ("chef", "Пусть зайдёт ко мне в кабинет.",
     "Let her come into my office.",
     [], "new"),
    ("anya", "Она просила выйти на одну минуту.",
     "She asked you to come out for one minute.",
     [], "new"),
    ("chef", "Ладно, Костя, я сейчас подойду сам.",
     "Fine, Kostya, I will come over myself now.",
     [], "new"),
    ("anya", "Спасибо, шеф, я передам ваши слова.",
     "Thank you, chef, I will convey your words.",
     [], "new"),
    ("chef", "И налей мне крепкого чёрного чая.",
     "And pour me some strong black tea.",
     [], "new"),
    ("anya", "Конечно, шеф, сделаю прямо сейчас.",
     "Of course, chef, I will do it right now.",
     [], "new"),
]

OPENER = "Now let's examine Kostya and Barinov's corridor conversation line by line."

WALK = [
    (0, None,
     "'Chef, some young woman is calling for you over there.' -- Kostya announces the unexpected visitor waiting outside."),
    (1, None,
     "'Who is she and what does she need?' -- The chef asks skeptically about her identity and purpose."),
    (2, None,
     "'She said that she came from television.' -- The bartender mentions her connection to television production."),
    (3, None,
     "'I do not want to talk to anyone.' -- Barinov grumbles that he wants to avoid all visitors."),
    (4, None,
     "'She says that the matter is very important.' -- Kostya emphasizes the urgency of her request."),
    (5, None,
     "'I currently have absolutely no time.' -- The chef insists that he has zero spare moments."),
    (6, None,
     "'She is waiting for you near the main entrance.' -- Kostya indicates her location in the restaurant foyer."),
    (7, None,
     "'Let her come into my office.' -- Barinov suggests meeting in the privacy of his office."),
    (8, None,
     "'She asked you to come out for one minute.' -- The bartender clarifies that she requested a quick lobby meeting."),
    (9, None,
     "'Fine, Kostya, I will come over myself now.' -- The chef relents and agrees to step outside."),
    (10, None,
     "'Thank you, chef, I will convey your words.' -- Kostya accepts the response to inform the visitor."),
    (11, None,
     "'And pour me some strong black tea.' -- Barinov orders a cup of strong tea for energy."),
    (12, None,
     "'Of course, chef, I will do it right now.' -- Kostya promises to prepare the tea immediately."),
]

TRANSITION = "Now let's listen to the corridor conversation again without interruption."
OUTRO = (
    "Curious despite his lingering hangover, Chef Barinov heads toward the entrance to discover "
    "what the television representative wants, while Kostya hurries to brew his tea."
)
CLOSING = ("anya", "Конечно, шеф, сделаю прямо сейчас.")
