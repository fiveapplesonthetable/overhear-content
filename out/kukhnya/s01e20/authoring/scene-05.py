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
     "'Kostya, we need to talk seriously.' Russian expresses this impersonally, literally saying 'to me' or 'to you' with 'to talk'."),
    (1, None,
     "'I wanted to discuss something with you.' A compact expression built around 'I' and 'to discuss'."),
    (2, None,
     "'Wait a minute, I will be right back.' Here 'wait' sets up the idea, while 'will come back' comes at the end for emphasis. And Nastya jumps in."),
    (3, None,
     "'This is a very important conversation for us.' You'll hear 'this' all the time in the show, here connected with 'us'."),
    (4, None,
     "'I understand, but I need to go.' The key word here means 'I', which Kostya combines with 'understand'."),
    (5, None,
     "'Are you running away from my questions again?' In Russian, 'you' leads into 'questions' in a very natural everyday phrasing. Kostya answers straight away."),
    (6, None,
     "'No, I am not running away from you anywhere.' Kostya uses the casual singular 'you' with 'I', as close colleagues and friends do."),
    (7, None,
     "'Then why do you not want to listen to me?' The little negative word sits right in front of the verb for 'do you want', just like 'not' in English."),
    (8, None,
     "'I want to listen, but not now.' The first content word means 'I', and 'now' rounds out the thought. Then Nastya replies."),
    (9, None,
     "'We are walking on a high staircase, right?' Nastya puts 'we' up front so the listener immediately catches the tone, followed by 'are going'."),
    (10, None,
     "'It seems my stomach simply cramped up.' Listen for the word meaning 'it seems' right alongside 'me' in this line."),
    (11, None,
     "'I urgently need to go to the toilet.' Russian expresses this impersonally, literally saying 'to me' or 'to you' with 'toilet'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya successfully dodges the conversation by faking a sudden illness, buying himself a little more time."
CLOSING = ("anya", "Мне срочно нужно в туалет.")
