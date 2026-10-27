ID = "domashniy-arest-s01e08-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 5
TITLE = "Вот танк государство может  (A Tank the State Can Handle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "doctor": "anja"}
LABELS = {"anya": "Лёша", "doctor": "Доктор"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 80-84. In the clinic hallway, young Lyosha approaches the doctor with his broken green toy tank. "
    "The doctor explains that he only repairs people, but dryly notes that the state always has money for tanks. "
    "Title song in cue 85 is omitted."
)

INTRO = (
    "In our last scene, Marina was told that the clinic has run out of surgery quotas for the year and that Lyosha "
    "will have to wait until next year. "
    "Stepping out into the hospital corridor on his crutches, ten-year-old Lyosha stops the doctor to show him his "
    "broken toy tank, leading to a bitter and humorous exchange about what the state can and cannot fix. "
    "Let's listen to the short scene in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya", "Доктор, подождите минутку, пожалуйста!",
     "Doctor, wait a minute, please!",
     [], "added opening request"),
    ("doctor", "Что такое, малыш? У тебя что-то болит?",
     "What is the matter, sweetie? Does something hurt you?",
     [], "added doctor reaction"),
    ("anya", "У меня танк сломался.",
     "My tank broke.",
     [(80, "У меня танк сломался")], ""),
    ("anya", "Можете починить?",
     "Can you fix it?",
     [(80, "Можете починить")], ""),
    ("doctor", "Танк? Ну-ка, покажи мне.",
     "A tank? Let me see.",
     [(81, "Танк? Ну-ка")], "'покажи мне' added"),
    ("doctor", "Нет, брат, танк я не могу чинить.",
     "No, buddy, I cannot fix tanks.",
     [(82, "Нет, брат, танк я не могу чинить")], ""),
    ("doctor", "Я ведь только людей лечу.",
     "I only treat people, after all.",
     [(82, "Я только людей")], "'лечу' supplied for elliptical phrase"),
    ("anya", "А государство может починить танк?",
     "And can the state fix a tank?",
     [(83, "А государство может")], "'починить танк' added"),
    ("doctor", "Вот танк государство точно может!",
     "Now a tank — the state certainly can fix that!",
     [(84, "Вот танк государство может")], "'точно' added for emphasis"),
    ("doctor", "На танки у государства деньги всегда есть.",
     "For tanks the state always has money.",
     [], "added ironic contrast"),
    ("anya", "Спасибо, доктор! Я сам попробую починить.",
     "Thank you, Doctor! I will try to fix it myself.",
     [], "added polite child reply"),
    ("doctor", "Иди к маме, малыш! Не грусти.",
     "Go to your mama, sweetie! Don't be sad.",
     [], "added encouraging doctor closing"),
]

OPENER = (
    "Now let's examine this poignant corridor conversation line by line. "
    "Lyosha leans on his forearm crutches and holds out his toy."
)

WALK = [
    (0, None,
     "'Doctor, wait a minute, please!' Lyosha uses the polite imperative with the diminutive noun for 'minute'."),
    (1, None,
     "'What is the matter, sweetie? Does something hurt you?' The doctor stops kindly in the hallway."),
    (2, None,
     "'My tank broke.' Notice the reflexive past verb used for inanimate objects breaking down."),
    (3, None,
     "'Can you fix it?' An infinitive question with the polite plural verb 'can'."),
    (4, None,
     "'A tank? Let me see.' The colloquial particle encourages someone to show something."),
    (5, None,
     "'No, buddy, I cannot fix tanks.' The doctor addresses the boy warmly as 'brother' or 'buddy'."),
    (6, None,
     "'I only treat people, after all.' The 1st person singular present verb means 'I treat' or 'I cure'."),
    (7, None,
     "'And can the state fix a tank?' Lyosha remembers what his mother told him about the state helping."),
    (8, None,
     "'Now a tank — the state certainly can fix that!' The doctor gives a dry, ironic answer."),
    (9, None,
     "'For tanks the state always has money.' Notice the preposition for 'for/onto' with the accusative plural."),
    (10, None,
     "'Thank you, Doctor! I will try to fix it myself.' The emphatic pronoun means 'myself' in the masculine singular."),
    (11, None,
     "'Go to your mama, sweetie! Don't be sad.' The negative imperative urges the boy not to lose heart."),
]

TRANSITION = "Now let's listen to the entire corridor conversation again in Russian."
OUTRO = (
    "Lyosha's broken toy tank becomes a recurring symbol in the episode. "
    "Next the title sequence rolls as Samsonov's disappearance throws the entire campaign into crisis; see you there."
)
CLOSING = ("doctor", "Вот танк государство точно может!")
