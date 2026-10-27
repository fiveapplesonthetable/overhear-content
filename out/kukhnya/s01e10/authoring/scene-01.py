ID = "kukhnya-s01e10-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 1
TITLE = "Поздний вечер  (A Late Evening)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "syn": "anja"}
LABELS = {"anya": "Мама", "syn": "Сын"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-3. Returning home late after school, a young boy apologizes to his mother, "
    "who warns him about his father's gambling losses."
)

INTRO = (
    "In a family home late in the evening, a schoolboy creeps into the apartment long after his classes have ended. "
    "He nervously apologizes to his mother for the delay, only to learn that his father has once again lost all "
    "their money in a game of chance. Let's listen to their quiet conversation in Russian first."
)

STORY = [
    ("syn", "Извини, мама, я сильно опоздал сегодня.",
     "Sorry, mom, I was very late today.",
     [(1, "Извини")], "adapted"),
    ("anya", "Почему ты пришёл так поздно домой?",
     "Why did you come home so late?",
     [], "new"),
    ("syn", "Я долго гулял с моими друзьями.",
     "I walked for a long time with my friends.",
     [(1, "Я с друзьями")], "adapted"),
    ("anya", "Тебе повезло, что папа спит.",
     "You got lucky that dad is sleeping.",
     [(2, "повезло, что папочка не видел")], "adapted"),
    ("syn", "А папа разве сердится на меня?",
     "Is dad really angry with me?",
     [], "new"),
    ("anya", "Папа опять проиграл все наши деньги.",
     "Dad lost all our money again.",
     [(3, "Он опять все")], "adapted"),
    ("syn", "Он снова играл на наши деньги?",
     "Did he play with our money again?",
     [], "new"),
    ("anya", "Да, он делал ставки на футбол.",
     "Yes, he placed bets on football.",
     [], "new"),
    ("syn", "И его любимая команда опять проиграла?",
     "And his favorite team lost again?",
     [], "new"),
    ("anya", "Да, его любимый Спартак снова проиграл.",
     "Yes, his favorite Spartak lost again.",
     [], "new"),
    ("syn", "Теперь у нас совсем нет денег?",
     "Now do we have no money at all?",
     [], "new"),
    ("anya", "Ничего, сынок, мы со всем справимся.",
     "It is alright, son, we will cope with everything.",
     [], "new"),
    ("syn", "Я завтра найду себе хорошую работу.",
     "Tomorrow I will find myself a good job.",
     [], "new"),
]

OPENER = "Now let's examine the mother and son's late evening exchange line by line."

WALK = [
    (0, None,
     "'Sorry, mom, I was very late today.' -- The boy apologizes sincerely for being late."),
    (1, None,
     "'Why did you come home so late?' -- His mother questions the reason for his extended absence."),
    (2, None,
     "'I walked for a long time with my friends.' -- He explains that he was spending time with schoolmates."),
    (3, None,
     "'You got lucky that dad is sleeping.' -- She warns him that his father's slumber prevented an argument."),
    (4, None,
     "'Is dad really angry with me?' -- The son asks whether his tardiness caused his father anger."),
    (5, None,
     "'Dad lost all our money again.' -- The mother delivers the grim news of another gambling loss."),
    (6, None,
     "'Did he play with our money again?' -- The boy asks if their money was gambled away."),
    (7, None,
     "'Yes, he placed bets on football.' -- She confirms that sports betting consumed their finances."),
    (8, None,
     "'And his favorite team lost again?' -- The son correctly guesses the disastrous match outcome."),
    (9, None,
     "'Yes, his favorite Spartak lost again.' -- The mother confirms Spartak's disappointing defeat."),
    (10, None,
     "'Now do we have no money at all?' -- The son realizes the full gravity of their financial hardship."),
    (11, None,
     "'It is alright, son, we will cope with everything.' -- The mother offers comforting reassurance."),
    (12, None,
     "'Tomorrow I will find myself a good job.' -- The boy bravely vows to help earn income."),
]

TRANSITION = "Now let's listen to the quiet conversation again without interruption."
OUTRO = (
    "With heartfelt promises to find work and face hardships together, the mother and son conclude "
    "their quiet conversation, ready to support each other through family adversity."
)
CLOSING = ("syn", "Я завтра найду себе хорошую работу.")
