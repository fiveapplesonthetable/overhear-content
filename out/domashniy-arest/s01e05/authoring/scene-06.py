"""
Scene 06 authoring module — Домашний арест S01E05.

Кредит закрыт (The loan is closed)
Cues 203–240 (00:11:14,880 – 00:12:40,020).
"""

ID = "domashniy-arest-s01e05-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = "Кредит закрыт  (The loan is closed)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"

SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
CUE_RANGE = (203, 240)

VOICES = {
    "narrator": "sky",
    "anya": "alisa",      # Марина
    "grisha": "anja",     # Дядя Гриша
    "kostik": "angelina", # Костик
}

LABELS = {
    "anya": "Марина",
    "grisha": "Дядя Гриша",
    "kostik": "Костик",
}

INTRO = (
    "Right after Arkady sends Ilona off to negotiate with the Society of the Blind, "
    "a commotion erupts in the corridor of the communal flat. "
    "Two debt collectors from a microloan agency — burly Uncle Grisha and nervous young Kostik — "
    "corner Marina Sergeyevna and her young son Lyosha, demanding an outrageous sum in interest. "
    "Listen to the Russian confrontation first; don't worry about catching every word."
)

STORY = [
    ("grisha",
     "Женщина, вы мелкими буквами не читаете. Наша фирма в этом не виновата.",
     "Ma'am, you don't read the small print. Our firm isn't to blame for that.",
     [(203, "Женщина"), (203, "вы мелкими буквами не читаете"), (203, "в этом не виновата")],
     "split into two short sentences"),
    ("anya",
     "Я уже вам сто раз говорила. Я брала двадцать тысяч, вернула тридцать!",
     "I've already told you a hundred times. I borrowed twenty thousand, paid back thirty!",
     [(204, "Я уже вам сто раз говорила")],
     "numbers written out as words"),
    ("anya",
     "Кредит закрыт!",
     "The loan is closed!",
     [(204, "кредит закрыт")],
     ""),
    ("grisha",
     "Будьте добры, верните сто пятьдесят тысяч рублей.",
     "Be so kind, return one hundred and fifty thousand roubles.",
     [(205, "Будьте добры, верните"), (205, "тысяч рублей")],
     "number written out as words"),
    ("anya",
     "Я не понимаю, вы мне угрожаете? Что вы сделаете?",
     "I don't understand, are you threatening me? What will you do?",
     [(206, "Я не понимаю"), (206, "мне угрожаете"), (207, "Что вы сделаете")],
     ""),
    ("grisha",
     "А мы многое что можем сделать. Вот, например, мальчик.",
     "Oh, there's plenty we can do. Here, for example, is the boy.",
     [(208, "А мы многое что можем сделать"), (209, "Вот, например, мальчик")],
     "omitted crude threats in cues 210 and 213"),
    ("anya",
     "Лёша! Давай, Лёша, уйди.",
     "Lyosha! Come on, Lyosha, go inside.",
     [(211, "Леша"), (220, "Давай, Леша, уйди")],
     ""),
    ("anya",
     "Я сейчас в полицию позвоню! Пошли вон отсюда!",
     "I'll call the police right now! Get out of here!",
     [(214, "полицию позвоню"), (217, "пошли вон отсюда")],
     ""),
    ("anya",
     "Убирайтесь отсюда!",
     "Clear out of here!",
     [(222, "Убирайтесь отсюда")],
     ""),
    ("kostik",
     "Верните деньги!",
     "Return the money!",
     [(224, "Верните деньги")],
     ""),
    ("anya",
     "Ни копейки от меня не получите!",
     "You won't get a single kopek from me!",
     [(225, "копейки от меня не получите")],
     ""),
    ("grisha",
     "Мы вернёмся!",
     "We'll be back!",
     [(229, "Мы вернёмся")],
     ""),
    ("anya",
     "Ну, а вы что смотрите?",
     "Well, and what are you staring at?",
     [(230, "Ну, а вы что смотрите")],
     ""),
    ("anya",
     "Я, между прочим, кредит на лечение сына брала!",
     "By the way, I took the loan for my son's treatment!",
     [(236, "Я между прочим кредит на лечение сына брала")],
     ""),
]

OPENER = (
    "Let's walk through the confrontation in the corridor and see how Marina stands up to the two debt collectors."
)

WALK = [
    (0, "Женщина, вы мелкими буквами не читаете.",
     "The older collector, Uncle Grisha, addresses Marina bluntly: 'Woman, you do not read the small letters' — meaning the fine print in the contract."),
    (0, "Наша фирма в этом не виновата.",
     "'Our firm isn't to blame for that.' Notice the word order: 'our' comes first, and 'at fault' finishes the sentence."),
    (1, "Я уже вам сто раз говорила.",
     "Marina stands her ground: 'I already told you a hundred times.' Notice the feminine past-tense ending on the verb."),
    (1, "Я брала двадцать тысяч, вернула тридцать!",
     "'I borrowed twenty thousand, paid back thirty!' A compact expression built around 'I' and 'thirty'."),
    (2, None,
     "She finishes firmly: 'The loan is closed!'"),
    (3, None,
     "Uncle Grisha replies with mock politeness: 'Be so kind, return one hundred and fifty thousand roubles.'"),
    (4, "Я не понимаю, вы мне угрожаете?",
     "Marina stares at him: 'I do not understand, are you threatening me?'"),
    (4, "Что вы сделаете?",
     "And she challenges him directly: 'What will you do?'"),
    (5, "А мы многое что можем сделать.",
     "Grisha steps closer: 'Oh, there's plenty we can do.'"),
    (5, "Вот, например, мальчик.",
     "He gestures toward her young son on crutches: 'Here, for example, is the boy.'"),
    (6, "Лёша!",
     "Marina immediately steps in front of her son: 'Lyosha!'"),
    (6, "Давай, Лёша, уйди.",
     "She urges the boy toward their room: 'Come on, Lyosha, go inside.'"),
    (7, "Я сейчас в полицию позвоню!",
     "Furious, Marina shouts at the collectors: 'I'll call the police right now!'"),
    (7, "Пошли вон отсюда!",
     "'Get out of here!' Marina uses an urgent command built around the verb for 'get out'."),
    (8, None,
     "She pushes them toward the front door: 'Clear out of here!'"),
    (9, None,
     "Young Kostik tries to sound menacing as he backs out: 'Return the money!'"),
    (10, None,
     "Marina yells back: 'You won't get a single kopek from me!'"),
    (11, None,
     "From the doorway, Uncle Grisha calls out a parting warning: 'We'll be back!'"),
    (12, None,
     "Once the door slams shut, Marina turns on Arkady and Klavdia Viktorovna watching from the hallway: 'Well, and what are you staring at?'"),
    (13, None,
     "When Arkady mutters that people should think before taking out loans, Marina snaps back: "
     "'By the way, I took the loan for my son\'s treatment!'"),
]

TRANSITION = (
    "Now listen to the entire confrontation in the corridor once more from start to finish."
)

OUTRO = (
    "Marina slams her room door, while out on the stairwell Uncle Grisha lectures young Kostik "
    "on why nobody is afraid of them."
)

CLOSING = ("anya", "Кредит закрыт!")
