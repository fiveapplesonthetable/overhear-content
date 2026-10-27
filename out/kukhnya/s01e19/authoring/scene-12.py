ID = "kukhnya-s01e19-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 19
SCENE = 12
TITLE = "Ревность на парковке  (Jealousy in the Parking Lot)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.19"
SOURCE_FILE = "sources/kukhnya/s01/e19.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 219-232. In the parking lot outside Claude Monet, Victoria catches Max spying on her. "
    "She clarifies that the client is a potential buyer for the restaurant and asks Max to drive her car home."
)

INTRO = (
    "In the parking lot outside Claude Monet, Victoria heads toward an expensive luxury car. "
    "Catching Max lurking nearby, she questions his motives, defends her business meeting, and asks for a favor. "
    "Let's listen to their confrontation in Russian first."
)

OPENER = "Now let's examine the conversation line by line."

STORY = [
    ("vika", "Макс, ты что здесь делаешь?",
     "Max, what are you doing here?",
     [(219, "Ты что здесь делаешь?")], "adapted"),
    ("anya", "Я просто стою и дышу воздухом.",
     "I am just standing and breathing air.",
     [(222, "Вот стою, воздухом дышу.")], "adapted"),
    ("vika", "Ты что, опять следишь за мной?",
     "Are you following me again?",
     [(221, "Ты что, следишь за мной?")], "adapted"),
    ("anya", "У тебя же сейчас важная деловая встреча.",
     "You have an important business meeting right now.",
     [(224, "У тебя же там встреча деловая.")], "adapted"),
    ("vika", "Макс, скажи честно, ты ревнуешь?",
     "Max, tell the truth, are you jealous?",
     [(225, "Макс, ты что, ревнуешь?")], "adapted"),
    ("anya", "Я совсем не ревную тебя, Вика.",
     "I am not jealous of you at all, Vika.",
     [(228, "Да я не ревную.")], "adapted"),
    ("vika", "Это встреча по поводу продажи ресторана.",
     "This is a meeting regarding the sale of the restaurant.",
     [(226, "Это просто деловая встреча с покупателем по поводу"), (227, "возможной продажи ресторана.")], "adapted"),
    ("anya", "Я спокоен, езжай на свою встречу.",
     "I am calm, go to your meeting.",
     [(223, "Ты давай, езжай.")], "adapted"),
    ("vika", "Отгони, пожалуйста, мою машину домой.",
     "Please drive my car home.",
     [(230, "Кстати, отгони, пожалуйста, мою машину домой.")], "adapted"),
    ("anya", "А ты поедешь на его машине?",
     "And you will go in his car?",
     [(231, "Я поеду на его машине.")], "adapted"),
    ("vika", "Да, мы поедем вместе на переговоры.",
     "Yes, we will go together to negotiations.",
     [], "new"),
    ("vika", "Мне уже пора ехать, пока, Макс.",
     "It is time for me to go, bye, Max.",
     [(232, "Ну ладно, пока, мне пора.")], "adapted"),
    ("anya", "Да, конечно, счастливого пути, Вика.",
     "Yes, of course, safe travels, Vika.",
     [(232, "Да, конечно, пока.")], "adapted"),
]

WALK = [
    (0, None,
     "'Max, what are you doing here?' -- Victoria spots him waiting outside the restaurant."),
    (1, None,
     "'I am just standing and breathing air.' -- Max invents a clumsy excuse for lurking nearby."),
    (2, None,
     "'Are you following me again?' -- Victoria directly calls out his stalking behavior."),
    (3, None,
     "'You have an important business meeting right now.' -- Max references the client with subtle sarcasm."),
    (4, None,
     "'Max, tell the truth, are you jealous?' -- Victoria confronts his unspoken emotional state."),
    (5, None,
     "'I am not jealous of you at all, Vika.' -- The proud cook firmly denies his jealousy."),
    (6, None,
     "'This is a meeting regarding the sale of the restaurant.' -- Victoria clarifies the serious commercial context."),
    (7, None,
     "'I am calm, go to your meeting.' -- Max feigns indifferent composure."),
    (8, None,
     "'Please drive my car home.' -- Victoria entrusts him with her car keys as a practical errand."),
    (9, None,
     "'And you will go in his car?' -- Max notes the uncomfortable detail of their shared ride."),
    (10, None,
     "'Yes, we will go together to negotiations.' -- Victoria confirms her travel arrangement without hesitation."),
    (11, None,
     "'It is time for me to go, bye, Max.' -- Victoria wraps up their conversation and turns to leave."),
    (12, None,
     "'Yes, of course, safe travels, Vika.' -- Max bids her farewell while holding the car keys."),
]

TRANSITION = "Now let's listen to the parking lot exchange once again without interruption."

OUTRO = (
    "Holding Victoria's car keys in the empty parking lot, Max watches her drive away with the wealthy investor, "
    "wondering what the future holds for Claude Monet and their fragile relationship."
)

CLOSING = ("anya", "Да, конечно, счастливого пути, Вика.")
