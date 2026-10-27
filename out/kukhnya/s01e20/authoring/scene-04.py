ID = "kukhnya-s01e20-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 4
TITLE = "Дорогой подарок  (Expensive Gift)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "anja"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
LABELS = {"anya": "Макс", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 4"

INTRO = "Max calls Vika to discuss the expensive ring she sent him. He tries to subtly figure out if she really expects him to buy it. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Привет. Я хотел узнать насчёт подарка.",
     "Hi. I wanted to find out about the gift.",
     [(114, 'Я хотел узнать')], "adapted"),
    ("anya", "Тебе понравилось это красивое кольцо?",
     "Did you like this beautiful ring?",
     [(115, 'Тебе понравилось')], "adapted"),
    ("vika", "Да, оно очень красивое.",
     "Yes, it is very beautiful.",
     [(115, 'Да, красивое')], "adapted"),
    ("anya", "А ты знаешь, сколько оно стоит?",
     "And do you know how much it costs?",
     [(116, 'знаешь, сколько оно стоит')], "adapted"),
    ("anya", "Ты считаешь, это нормально для подарка?",
     "You consider this normal for a gift?",
     [(119, 'считаешь, для подарка это нормально')], "adapted"),
    ("vika", "Конечно. Таня выбирала подарок для себя.",
     "Of course. Tanya was choosing a gift for herself.",
     [(123, 'выбирала подарок')], "adapted"),
    ("vika", "Она просто прислала мне фотографию.",
     "She simply sent me a photograph.",
     [(123, 'прислала мне фотографию')], "adapted"),
    ("anya", "А я сам хотел подарить тебе кольцо.",
     "But I wanted to gift you a ring myself.",
     [(126, 'сам хотел тебе кольцо подарить')], "adapted"),
    ("vika", "Она подрезала твой подарок?",
     "She undercut your gift?",
     [(127, 'подрезала подарок мой')], "adapted"),
    ("vika", "Я скажу ей выбрать что-то другое.",
     "I will tell her to choose something else.",
     [(129, 'Пусть она что-нибудь другое выберет')], "adapted"),
    ("vika", "А ты мне подаришь это кольцо.",
     "And you will gift me this ring.",
     [(130, 'А ты мне подаришь кольцо')], "adapted"),
    ("anya", "Зачем же? Она же уже купила.",
     "Why then? She already bought it.",
     [(132, 'Зачем же? Она же уже купила')], "adapted"),
    ("vika", "Нет, она просто просила совета.",
     "No, she was simply asking for advice.",
     [(133, 'она просто выбирала, советовала')], "adapted"),
    ("vika", "Я сейчас ей позвоню.",
     "I will call her now.",
     [(134, 'Я сейчас ей позвоню')], "adapted"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Hi. I wanted to find out about the gift.' -- ENG He nervously calls her to discuss the photo."),
    (1, None,
     "'Did you like this beautiful ring?' -- ENG He casually asks for her opinion on the jewelry."),
    (2, None,
     "'Yes, it is very beautiful.' -- ENG She confirms that she absolutely loves the piece."),
    (3, None,
     "'And do you know how much it costs?' -- ENG He points out the incredibly high price tag."),
    (4, None,
     "'You consider this normal for a gift?' -- ENG He questions whether such an extravagant present is reasonable."),
    (5, None,
     "'Of course. Tanya was choosing a gift for herself.' -- ENG She reveals that the ring was never for her."),
    (6, None,
     "'She simply sent me a photograph.' -- ENG She explains why she forwarded the image to him."),
    (7, None,
     "'But I wanted to gift you a ring myself.' -- ENG He foolishly tries to sound generous and romantic."),
    (8, None,
     "'She undercut your gift?' -- ENG She asks if her friend ruined his secret plan."),
    (9, None,
     "'I will tell her to choose something else.' -- ENG She decides to intervene to save his surprise."),
    (10, None,
     "'And you will gift me this ring.' -- ENG She happily accepts his fake offer to buy it."),
    (11, None,
     "'Why then? She already bought it.' -- ENG He desperately tries to stop her from calling Tanya."),
    (12, None,
     "'No, she was simply asking for advice.' -- ENG She clarifies that the purchase is not final yet."),
    (13, None,
     "'I will call her now.' -- ENG She hangs up, leaving him trapped in a lie."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max accidentally traps himself into buying the ring when his attempt to look generous backfires."
CLOSING = ("vika", "Я сейчас ей позвоню.")
