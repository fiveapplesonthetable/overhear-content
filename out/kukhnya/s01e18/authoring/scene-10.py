ID = "kukhnya-s01e18-scene-10"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 10
TITLE = "Плохая рыба  (Bad Fish)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "fedya": "anja"}
LABELS = {"anya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 10"

INTRO = "In the locker room, Fedya checks on Senya who is feeling very sick. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("fedya", "У тебя все хорошо?",
     "Are you all right?",
     [(1, "девушки")], "adapted"),
    ("anya", "Нет, мне очень плохо.",
     "No, I am very bad.",
     [(1, "девушки")], "adapted"),
    ("fedya", "Я же тебе говорил.",
     "I told you.",
     [(1, "девушки")], "adapted"),
    ("fedya", "Не ешь эту рыбу.",
     "Do not eat that fish.",
     [(1, "девушки")], "adapted"),
    ("anya", "Я думал, она нормальная.",
     "I thought she was normal.",
     [(1, "девушки")], "new"),
    ("fedya", "Ты уголь пил?",
     "Did you drink charcoal?",
     [(1, "девушки")], "adapted"),
    ("anya", "Ага, две пачки сожрал.",
     "Yeah, I ate two packs.",
     [(1, "девушки")], "adapted"),
    ("fedya", "Ни хрена себе.",
     "No shit.",
     [(1, "девушки")], "adapted"),
    ("anya", "У меня болит живот.",
     "My stomach hurts.",
     [(1, "девушки")], "new"),
    ("fedya", "Тебе надо пойти домой.",
     "You need to go home.",
     [(1, "девушки")], "new"),
    ("anya", "Я не могу работать сегодня.",
     "I cannot work today.",
     [(1, "девушки")], "new"),
    ("fedya", "Иди домой и отдыхай.",
     "Go home and rest.",
     [(1, "девушки")], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'Are you all right?' Fedya puts 'you' up front so the listener immediately catches the tone, followed by 'good'."),
    (1, None,
     "'No, I am very bad.' Notice the word order: 'to me' comes first, and 'badly' finishes the sentence. Fedya answers straight away."),
    (2, None,
     "'I told you.' Here 'I' sets up the idea, while 'said' comes at the end for emphasis."),
    (3, None,
     "'Do not eat that fish.' You'll hear 'eat' all the time in the show, here connected with 'fish'."),
    (4, None,
     "'I thought she was normal.' The key word here means 'I', which Senya combines with 'thought'. Then Fedya replies."),
    (5, None,
     "'Did you drink charcoal?' There is no question word here — in Russian, rising intonation on 'was drinking' is enough to make it a question."),
    (6, None,
     "'Yeah, I ate two packs.' Senya puts 'yeah' up front so the listener immediately catches the tone, followed by 'two'."),
    (7, None,
     "'No shit.' In Russian, 'horseradish' leads into 'yourself' in a very natural everyday phrasing. And Senya jumps in."),
    (8, None,
     "'My stomach hurts.' The first content word means 'me', and 'belly' rounds out the thought."),
    (9, None,
     "'You need to go home.' Listen for the word meaning 'for you' right alongside 'it is necessary' in this line."),
    (10, None,
     "'I cannot work today.' Listen for the word meaning 'I' right alongside 'can' in this line. Fedya answers straight away."),
    (11, None,
     "'Go home and rest.' A compact expression built around 'go' and 'rest'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Fedya shakes his head, knowing his friend should have listened to him."
CLOSING = ("fedya", "Иди домой и отдыхай.")
