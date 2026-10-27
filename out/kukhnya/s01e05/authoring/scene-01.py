ID = "kukhnya-s01e05-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = "Ссора из-за поцелуя  (A Quarrel Over a Kiss)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-15. Bartender Kostya is furious with Max after learning that Max kissed waitress Nastya, "
    "the girl Kostya has a massive crush on. Max desperately explains it was an exhausted misunderstanding."
)

INTRO = (
    "Morning at Claude Monet begins with high drama behind the bar. "
    "Bartender Kostya confronts Max in a fury after finding out Max kissed waitress Nastya during yesterday's shift. "
    "Max frantically tries to convince his best friend that the kiss was a sleep-deprived accident and that he has no feelings for Nastya. "
    "Let's listen to their argument in Russian first."
)

STORY = [
    ("anya", "Костя, привет. Почему ты сердишься?",
     "Kostya, hi. Why are you angry?",
     [], "new"),
    ("kostya", "Отвали, или я сломаю тебе нос!",
     "Back off, or I will break your nose!",
     [(6, "Отвали, или я тебе нос сломаю")], "adapted"),
    ("anya", "За что? Что я тебе сделал?",
     "What for? What did I do to you?",
     [(7, "За что")], "adapted"),
    ("kostya", "Ты вчера целовался с моей девушкой!",
     "Yesterday you kissed my girl!",
     [(7, "ты целовался с моей девушкой")], "adapted"),
    ("anya", "Это было совершенно случайное недоразумение.",
     "It was a completely accidental misunderstanding.",
     [(11, "это вообще недоразумение было")], "adapted"),
    ("kostya", "Вы целовались прямо в ресторане!",
     "You were kissing right in the restaurant!",
     [], "new"),
    ("anya", "Я вчера весь день хотел спать.",
     "I wanted to sleep all day yesterday.",
     [(12, "Я вчера весь день"), (12, "спать хотел")], "adapted"),
    ("anya", "Кстати, технически она пока не твоя.",
     "By the way, technically she is not yours yet.",
     [(13, "Кстати, технически она пока не твоя")], "adapted"),
    ("kostya", "Для меня это не имеет значения.",
     "For me that does not matter.",
     [], "new"),
    ("anya", "Между мной и Настей ничего нет!",
     "There is nothing between me and Nastya!",
     [(15, "между нами ничего нет")], "adapted"),
    ("kostya", "Ты предал нашу дружбу, Макс.",
     "You betrayed our friendship, Max.",
     [], "new"),
    ("anya", "Я докажу, что она мне безразлична.",
     "I will prove that she means nothing to me.",
     [], "new"),
    ("kostya", "Посмотрим, как ты это докажешь.",
     "We will see how you prove it.",
     [], "new"),
]

OPENER = "Now let's examine Max and Kostya's argument line by line."

WALK = [
    (0, None,
     "'Kostya, hi. Why are you angry?' Max tries to greet his tense friend with an informal greeting."),
    (1, None,
     "'Back off, or I will break your nose!' Kostya threatens him furiously with an imperative and future verb."),
    (2, None,
     "'What for? What did I do to you?' Max questions the sudden hostility with paired past questions."),
    (3, None,
     "'Yesterday you kissed my girl!' Kostya reveals the reason using a past reflexive verb."),
    (4, None,
     "'It was a completely accidental misunderstanding.' Max defends himself with descriptive neuter nouns and adjectives."),
    (5, None,
     "'You were kissing right in the restaurant!' Kostya emphasizes the public location with an adverb."),
    (6, None,
     "'I wanted to sleep all day yesterday.' Max explains his exhaustion using an infinitive of desire."),
    (7, None,
     "'By the way, technically she is not yours yet.' Max makes a technical point with an introductory parenthetical."),
    (8, None,
     "'For me that does not matter.' Kostya dismisses the technicality using a fixed negative idiom."),
    (9, None,
     "'There is nothing between me and Nastya!' Max insists on innocence with a prepositional pronoun phrase."),
    (10, None,
     "'You betrayed our friendship, Max.' Kostya expresses deep hurt with a past perfective verb."),
    (11, None,
     "'I will prove that she means nothing to me.' Max vows to make amends using a future perfective verb."),
    (12, None,
     "'We will see how you prove it.' Kostya remains skeptical with a future 1st person plural verb."),
]

TRANSITION = "Now let's listen to the friends' heated confrontation again without interruption."
OUTRO = (
    "Kostya walks away unconvinced, leaving Max determined to clear up the misunderstanding. "
    "In the next scene, waitress Nastya shares her romantic dreams with Sasha."
)
CLOSING = ("kostya", "Посмотрим, как ты это докажешь.")
