ID = "kukhnya-s04e08-scene-15"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 8
SCENE = 15
TITLE = "Поиски вязальщицы  (Searching for a Knitter)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ainura": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "ainura": "Айнура", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S4.08"
SOURCE_FILE = "sources/kukhnya/s04/e08.ru.srt"
SOURCE_NOTE = "Cues 243-255. Max asks Ainura if she knows how to knit so she can fix his mother's unraveled shawl, and when the shawl ends up completely ruined, Max promises Vika he will lie just one last time."

INTRO = "In the kitchen of Claude Monet, Max pulls his mother's half-unraveled shawl out of his bag and asks Ainura if she knows how to knit. When the shawl ends up completely ruined during the day, Vika asks what they will do now, and Max promises to tell just one final lie!"

STORY = [
    ("anya", "Айнура, скажи, а ты хорошо умеешь вязать?", "Ainura, tell me, do you know how to knit well?", [(243, "Ай, ну, связать умеешь?")], "adapted"),
    ("ainura", "А что именно тебе сейчас нужно связать?", "And what exactly do you need knitted right now?", [(244, "А что нужно связать?")], "adapted"),
    ("anya", "Вот этот тёплый мамин платок надо срочно починить!", "This warm shawl of Mom's needs to be fixed urgently!", [], "new"),
    ("ainura", "Ой, а вязальные спицы у тебя с собой есть?", "Oh my, and do you have knitting needles with you?", [(245, "Ой-бой. А спецы есть у тебя?")], "adapted"),
    ("ainura", "Нет, Максим, такое я связать не умею.", "No, Maksim, I do not know how to knit something like that.", [(246, "Нет, не умею.")], "adapted"),
    ("anya", "Я же тебе говорил, всё будет нормально!", "I told you that everything will be fine!", [(247, "Я же тебе говорил, все будет нормально.")], "adapted"),
    ("vika", "Макс, и что же мы теперь делать будем?", "Max, and just what are we going to do now?", [(252, "что теперь делать будем?")], "adapted"),
    ("anya", "Не переживай, сейчас мы обязательно что-нибудь придумаем.", "Do not worry, right now we will definitely think of something.", [(253, "Что-нибудь придумаем.")], "adapted"),
    ("vika", "Ты что, опять будешь своей маме врать?", "What, are you going to lie to your mother again?", [(254, "Опять врать будешь, да?")], "adapted"),
    ("anya", "Вика, я обещаю тебе, это в последний раз!", "Vika, I promise you, this is for the last time!", [(255, "Вика, я обещаю, это последний раз, ладно?")], "adapted"),
    ("vika", "Твоё враньё никогда до добра не доводит!", "Your lying never leads to anything good!", [], "new"),
    ("anya", "Я просто куплю ей точно такой же платок!", "I will simply buy her the exact same shawl!", [], "new"),
]

OPENER = "Let's break down Max's search for a knitter and his new plan line by line."

WALK = [
    (0, None, "'Ainura, tell me, do you know how to knit well?' Present-tense verb 'know how' takes the imperfective infinitive 'to knit'."),
    (1, None, "'And what exactly do you need knitted right now?' Modal adverb 'needed' pairs with the perfective infinitive."),
    (2, None, "'This warm shawl of Mom's needs to be fixed urgently!' Possessive adjective 'Mom's' modifies the masculine noun 'shawl'."),
    (3, None, "'Oh my, and do you have knitting needles with you?' Seeing the tangled mess of yarn, Ainura backs away."),
    (4, None, "'No, Maksim, I do not know how to knit something like that.' Ainura wisely declines the impossible repair job."),
    (5, None, "'I told you that everything will be fine!' Even after the old shawl falls apart completely, Max stays upbeat."),
    (6, None, "'Max, and just what are we going to do now?' Compound future 'what will we do' expresses Vika's exasperation."),
    (7, None, "'Do not worry, right now we will definitely think of something.' Indefinite pronoun 'something or other' pairs with 'will invent'."),
    (8, None, "'What, are you going to lie to your mother again?' Imperfective infinitive 'to lie' follows the auxiliary 'will you'."),
    (9, None, "'Vika, I promise you, this is for the last time!' Max swears that one last fib will solve everything."),
    (10, None, "'Your lying never leads to anything good!' Neuter verbal noun 'lying' is the subject of the negative idiom."),
    (11, None, "'I will simply buy her the exact same shawl!' Max decides to buy a new shawl and tell his mother Vika knitted a replacement."),
]

TRANSITION = "Now let's hear the shawl crisis in the kitchen again without interruption."
OUTRO = "While Max buys a brand-new shawl to pass off as Vika's handiwork, Senya's lie to Marina backfires spectacularly in Denis's room. See you in the next scene."
CLOSING = ("anya", "Вика, я обещаю тебе, это в последний раз!")
CLOSING_TRANS = "Vika, I promise you, this is for the last time!"
