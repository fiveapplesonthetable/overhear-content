ID = "domashniy-arest-s01e12-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 1
TITLE = "Монастырская летопись  (Monastery Chronicle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "grigory": "anja"}
LABELS = {"anya": "Константин", "grigory": "Отец Григорий"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-28. In a medieval monastery scriptorium eight centuries ago, monk Konstantin "
    "painstakingly copies an ancient chronicle by hand while Father Grigory inspects his sloppy work."
)

INTRO = (
    "Eight hundred years ago, inside the quiet scriptorium of Sineozersk monastery, monk Konstantin is busy copying an ancient book. "
    "His mentor, Father Grigory, watches over him strictly and criticizes his slow and messy handwriting. "
    "Konstantin complains that his hand is going numb and that he feels deep dread in his soul. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ух ты, похвала от настоятеля!",
     "Oh wow, praise from the abbot!",
     [(1, "Ух ты, плюс")], ""),
    ("grigory", "За что тебе похвала, Константин?",
     "What praise do you deserve, Konstantin?",
     [(2, "За что, отец Григорий")], ""),
    ("grigory", "Ты пишешь слишком медленно и грязно.",
     "You write too slowly and messily.",
     [(3, "пишешь ты медленно и грязнишь")], ""),
    ("anya", "Я очень стараюсь писать красиво.",
     "I try very hard to write nicely.",
     [(4, "Возюкаешь ты и рад")], "adapted"),
    ("grigory", "Посмотри, какая кривая буква получилась!",
     "Look what a crooked letter turned out!",
     [(5, "куды хвост пошел")], "adapted"),
    ("grigory", "Исправляй эту ошибку прямо сейчас.",
     "Correct this mistake right now.",
     [(6, "Подчищай")], "adapted"),
    ("anya", "Господи, прости меня грешного.",
     "Lord, forgive me a sinner.",
     [(7, "Прости, господи")], ""),
    ("grigory", "У нас осталось очень мало времени.",
     "We have very little time left.",
     [(8, "Времени мало")], ""),
    ("grigory", "Скоро эту летопись повезут назад.",
     "Soon this chronicle will be taken back.",
     [(8, "рукопись обратно в Киев поедет")], "adapted"),
    ("anya", "Мне очень боязно на душе.",
     "I feel very frightened in my soul.",
     [(11, "боязно мне отец Григорий. Тревога")], ""),
    ("grigory", "Ты боишься из-за своих грехов!",
     "You are afraid because of your sins!",
     [(12, "Тебе боязно, потому что ты")], "adapted"),
    ("anya", "Моя рука уже совсем немеет.",
     "My hand is going completely numb.",
     [(15, "длань уж не имеет")], "adapted"),
    ("grigory", "Тогда молись и кайся усердно!",
     "Then pray and repent diligently!",
     [(19, "Молись и кайся")], ""),
    ("grigory", "Я сам закончу эту страницу!",
     "I will finish this page myself!",
     [(27, "Сам буду писать")], "adapted"),
]

OPENER = "Now let's examine Father Grigory and Konstantin's medieval dialogue line by line."

WALK = [
    (0, None,
     "'Oh wow, praise from the abbot!' Konstantin rejoices upon receiving unexpected approval."),
    (1, None,
     "'What praise do you deserve, Konstantin?' Father Grigory questions him sharply with a dative pronoun."),
    (2, None,
     "'You write too slowly and messily.' Father Grigory scolds him with two descriptive adverbs."),
    (3, None,
     "'I try very hard to write nicely.' Konstantin defends his penmanship using a reflexive verb with an infinitive."),
    (4, None,
     "'Look what a crooked letter turned out!' Father Grigory points out a flawed letter with an imperative verb."),
    (5, None,
     "'Correct this mistake right now.' The mentor demands immediate correction using an imperative transitive verb."),
    (6, None,
     "'Lord, forgive me a sinner.' Konstantin whispers a humble apology with an accusative pronoun."),
    (7, None,
     "'We have very little time left.' Father Grigory warns of the looming deadline with a genitive quantity phrase."),
    (8, None,
     "'Soon this chronicle will be taken back.' Father Grigory explains the manuscript return with a future verb."),
    (9, None,
     "'I feel very frightened in my soul.' Konstantin shares his inner unease using an impersonal dative construction."),
    (10, None,
     "'You are afraid because of your sins!' Father Grigory blames spiritual weakness using a causal preposition."),
    (11, None,
     "'My hand is going completely numb.' Konstantin complains of physical exhaustion with an intensifying adverb."),
    (12, None,
     "'Then pray and repent diligently!' Father Grigory prescribes spiritual discipline with paired imperatives."),
    (13, None,
     "'I will finish this page myself!' Father Grigory takes over the quill with an emphatic pronoun."),
]

TRANSITION = "Now let's listen to the monastery scriptorium scene again without interruption."
OUTRO = (
    "Father Grigory takes the manuscript away from Konstantin to finish the work himself. "
    "In the next scene, unexpected danger suddenly threatens the monastery."
)
CLOSING = ("grigory", "Я сам закончу эту страницу!")
