ID = "kukhnya-s01e20-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 5
TITLE = "Серьёзный разговор  (Serious Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "anja"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
LABELS = {"anya": "Костя", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 5"

INTRO = "Nastya approaches Kostya at work for a serious conversation. Kostya is terrified that she wants to talk about marriage. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("nastya", "Костя, нам нужно серьёзно поговорить.",
     "Kostya, we need to talk seriously.",
     [(135, 'Костя')], "adapted"),
    ("nastya", "Я хотела с тобой кое-что обсудить.",
     "I wanted to discuss something with you.",
     [(135, 'я хотела с тобой кое-что обсудить')], "adapted"),
    ("anya", "Подожди минуту, я сейчас вернусь.",
     "Wait a minute, I will be right back.",
     [(136, 'Подожди')], "adapted"),
    ("nastya", "Это очень важный разговор для нас.",
     "This is a very important conversation for us.",
     [], "new"),
    ("anya", "Я понимаю, но мне нужно идти.",
     "I understand, but I need to go.",
     [], "new"),
    ("nastya", "Ты снова убегаешь от моих вопросов?",
     "Are you running away from my questions again?",
     [], "new"),
    ("anya", "Нет, я никуда от тебя не убегаю.",
     "No, I am not running away from you anywhere.",
     [], "new"),
    ("nastya", "Тогда почему ты не хочешь меня слушать?",
     "Then why do you not want to listen to me?",
     [], "new"),
    ("anya", "Я хочу слушать, но не сейчас.",
     "I want to listen, but not now.",
     [], "new"),
    ("nastya", "Мы же идём по высокой лестнице.",
     "We are walking on a high staircase, right?",
     [], "new"),
    ("anya", "Кажется, у меня просто живот скрутило.",
     "It seems my stomach simply cramped up.",
     [(137, 'Кажется, живот скрутило')], "adapted"),
    ("anya", "Мне срочно нужно в туалет.",
     "I urgently need to go to the toilet.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Kostya, we need to talk seriously.' -- ENG She approaches him with a very determined expression."),
    (1, None,
     "'I wanted to discuss something with you.' -- ENG She insists on having an important talk immediately."),
    (2, None,
     "'Wait a minute, I will be right back.' -- ENG He panics and tries to delay the inevitable discussion."),
    (3, None,
     "'This is a very important conversation for us.' -- ENG She refuses to let him escape so easily."),
    (4, None,
     "'I understand, but I need to go.' -- ENG He desperately looks for a way out."),
    (5, None,
     "'Are you running away from my questions again?' -- ENG She notices his obvious reluctance to engage."),
    (6, None,
     "'No, I am not running away from you anywhere.' -- ENG He nervously denies avoiding her."),
    (7, None,
     "'Then why do you not want to listen to me?' -- ENG She challenges his poor excuses."),
    (8, None,
     "'I want to listen, but not now.' -- ENG He promises to hear her out later."),
    (9, None,
     "'We are walking on a high staircase, right?' -- ENG She brings up her intense romantic metaphor again."),
    (10, None,
     "'It seems my stomach simply cramped up.' -- ENG He suddenly fakes a severe digestive issue."),
    (11, None,
     "'I urgently need to go to the toilet.' -- ENG He quickly runs away to avoid the wedding topic."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya successfully dodges the conversation by faking a sudden illness, buying himself a little more time."
CLOSING = ("anya", "Мне срочно нужно в туалет.")
