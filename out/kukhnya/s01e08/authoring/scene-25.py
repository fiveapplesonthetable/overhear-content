"""s01e08 scene 25: Две собаки (Two Dogs)."""

ID = "kukhnya-s01e08-scene-25"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 25
TITLE = "Две собаки  (Two Dogs)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Вика",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "In the restaurant Claude Monet, Chef Barinov has just found and returned Tyson the pet dog. "
    "At that exact moment, Victoria arrives holding an identical Shih Tzu puppy she frantically bought to replace him. "
    "Listen to their funny conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("chef", "Вика, посмотри на меня. Это что такое?",
     "Vika, look at me. What is this?",
     [(296, "Вика, это чё?")], "pointing at dog"),
    ("anya", "Шеф, это моя новая собачка!",
     "Chef, this is my new little dog!",
     [(297, "Это моя собачка!")], "nervous excuse"),
    ("anya", "Я её сегодня утром купила.",
     "I bought her this morning.",
     [(298, "Я её сегодня купила!")], "explaining purchase"),
    ("chef", "Зачем тебе собака такой же породы?",
     "Why do you need a dog of the same breed?",
     [], "asking about breed"),
    ("anya", "Мне просто очень понравился ваш Дайсон.",
     "I just really liked your Dyson.",
     [(299, "Мне просто так понравился Ваш Дайсон!")], "praising dog"),
    ("anya", "Я не удержалась и купила пёсика.",
     "I could not resist and bought a puppy.",
     [(300, "купил себе такого же пёсика!")], "justifying impulse"),
    ("chef", "Но они же совершенно одинаковые!",
     "But they are completely identical!",
     [], "pointing out similarity"),
    ("anya", "Извините, я их до сих пор путаю.",
     "Sorry, I still mix them up.",
     [(302, "Я их до сих пор путаю!")], "feigning confusion"),
    ("anya", "Кажется, вот это ваша, а вот эта моя.",
     "It seems this one is yours, and this one is mine.",
     [(301, "вот это ваша, а вот это моя!")], "swapping dogs"),
    ("chef", "Вика, а как зовут твоего пса?",
     "Vika, what is your dog's name?",
     [(304, "А твоего зовут как?")], "interrogating name"),
    ("anya", "Моего? Его зовут Максик!",
     "Mine? His name is Maxik!",
     [(306, "Максик?")], "blurted name"),
    ("chef", "А какая порода у этой собаки?",
     "And what breed is this dog?",
     [(307, "А порода?")], "testing knowledge"),
    ("anya", "Порода суши... Ой, шицу!",
     "Breed sushi... Oh, Shih Tzu!",
     [(308, "Суши. Ой, шицу.")], "flustered slip"),
    ("anya", "Как и ваша собака. Я пойду!",
     "Just like your dog. I will go!",
     [(309, "Как и ваша."), (310, "Ну, я пойду.")], "hasty exit"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Это что такое?",
     "'What is this?' — a common way to express confusion or surprise at a sight."),
    (1, "Шеф, это моя новая собачка!",
     "'Chef, this is my new little dog!' — note the diminutive feminine noun for a little dog."),
    (2, "Я её сегодня утром купила.",
     "'I bought her this morning.' — past tense feminine verb followed by the direct object pronoun."),
    (4, "Мне просто очень понравился ваш Дайсон.",
     "'I just really liked your Dyson.' — using the dative construction for liking someone or something."),
    (5, "Я не удержалась и купила пёсика.",
     "'I could not resist and bought a puppy.' — a natural colloquial expression for an impulsive purchase."),
    (7, "Извините, я их до сих пор путаю.",
     "'Sorry, I still mix them up.' — an apology combined with an imperfective present verb."),
    (8, "Кажется, вот это ваша, а вот эта моя.",
     "'It seems this one is yours, and this one is mine.' — contrasting possessive pronouns in the feminine."),
    (9, "Вика, а как зовут твоего пса?",
     "'Vika, what is your dog's name?' — a standard Russian question to ask what an animal is called."),
    (10, "Его зовут Максик!",
     "'His name is Maxik!' — an affectionate diminutive name blurted out in panic."),
    (12, "Ой, шицу!",
     "'Oh, Shih Tzu!' — a humorous mix-up between a food term and dog breed."),
    (13, "Как и ваша собака.",
     "'Just like your dog.' — wrapping up quickly to escape an awkward situation."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around two dogs, and for the words meaning 'look' and 'such'. You'll catch them now. See you next time."
CLOSING = ("anya", "Как и ваша собака. Я пойду!")
