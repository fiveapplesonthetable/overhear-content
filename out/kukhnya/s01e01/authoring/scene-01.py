ID = "kukhnya-s01e01-scene-01"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "Знакомство в клубе  (Meeting at the Club)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1-21. Outside a nightclub, aspiring young chef Maksim Lavrov defends a beautiful stranger named Vika. "
    "While inspecting his bruised nose, they discover that they both work in restaurants."
)

INTRO = (
    "Aspiring young cook Maksim Lavrov arrives in Moscow dreaming of culinary fame. "
    "Outside a crowded nightclub, he steps in to defend a striking young woman named Vika and gets punched in the face. "
    "As Vika checks his bruised nose, they strike up an easy conversation and realize they share a passion for the restaurant world. "
    "Let's listen to their meeting in Russian first."
)

STORY = [
    ("anya", "Девушка, с вами всё в порядке?",
     "Miss, are you all right?",
     [(13, "Слышь, мужик, ты как сейчас девушку ведёшь")], "adapted"),
    ("vika", "Да, спасибо за вашу помощь.",
     "Yes, thank you for your help.",
     [], "new"),
    ("vika", "Ой, кажется, у вас сломан нос!",
     "Oh, it looks like your nose is broken!",
     [(15, "А мне кажется, у меня нос сломан")], "adapted"),
    ("anya", "Мой нос — это мой главный инструмент.",
     "My nose is my main instrument.",
     [(16, "Это же мой инструмент")], "adapted"),
    ("vika", "Почему нос так важен для вас?",
     "Why is your nose so important to you?",
     [], "new"),
    ("anya", "Завтра у меня важное собеседование на работу.",
     "Tomorrow I have an important job interview.",
     [(14, "мне просто на собеседование завтра")], "adapted"),
    ("vika", "Кем вы хотите устроиться на работу?",
     "What job do you want to get?",
     [(17, "А ты кем устраиваешься")], "adapted"),
    ("anya", "Я хочу работать поваром в ресторане.",
     "I want to work as a cook in a restaurant.",
     [(18, "поваром в ресторан")], "adapted"),
    ("vika", "Правда? Я тоже работаю в ресторане!",
     "Really? I work in a restaurant too!",
     [(19, "А я тоже в ресторане работаю"), (20, "Да ну? Да")], "adapted"),
    ("anya", "Значит, у нас с тобой много общего.",
     "So you and I have a lot in common.",
     [(21, "У нас с тобой много общего")], ""),
    ("vika", "Ты очень милый и смелый парень.",
     "You are a very sweet and brave guy.",
     [], "new"),
    ("anya", "Может быть, пойдём выпьем вместе кофе?",
     "Maybe we should go drink coffee together?",
     [], "new"),
    ("vika", "С большим удовольствием, пойдём скорее!",
     "With great pleasure, let's go quickly!",
     [], "new"),
]

OPENER = "Now let's examine Max and Vika's club meeting line by line."

WALK = [
    (0, None,
     "'Miss, are you all right?' Max checks on her safety with a polite second-person plural pronoun."),
    (1, None,
     "'Yes, thank you for your help.' Vika thanks him politely using a prepositional gratitude phrase."),
    (2, None,
     "'Oh, it looks like your nose is broken!' Vika notices his injury with a parenthetical verb and passive participle."),
    (3, None,
     "'My nose is my main instrument.' Max explains his vocational tool with a demonstrative predicate."),
    (4, None,
     "'Why is your nose so important to you?' Vika inquires with a short predicate adjective and genitive pronoun."),
    (5, None,
     "'Tomorrow I have an important job interview.' Max mentions his appointment using a genitive possession clause."),
    (6, None,
     "'What job do you want to get?' Vika asks using an instrumental interrogative pronoun and infinitive."),
    (7, None,
     "'I want to work as a cook in a restaurant.' Max declares his dream career using an instrumental profession noun."),
    (8, None,
     "'Really? I work in a restaurant too!' Vika reveals her workplace with an adverb of similarity."),
    (9, None,
     "'So you and I have a lot in common.' Max draws a romantic connection using a genitive quantity construction."),
    (10, None,
     "'You are a very sweet and brave guy.' Vika compliments his courage with descriptive adjectives."),
    (11, None,
     "'Maybe we should go drink coffee together?' Max invites her out with an imperative future verb and infinitive."),
    (12, None,
     "'With great pleasure, let's go quickly!' Vika eagerly accepts using an instrumental phrase of enthusiasm."),
]

TRANSITION = "Now let's listen to their conversation outside the nightclub again without interruption."
OUTRO = (
    "Max and Vika hit it off immediately and head inside the bar together. "
    "In the next scene, they share cocktails and talk about their dreams."
)
CLOSING = ("anya", "Значит, у нас с тобой много общего.")
