ID = "kukhnya-s01e18-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 19
TITLE = "Экономия на бармене  (Saving on the Bartender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja"}
LABELS = {"anya": "Костя", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = "Scene 19"

INTRO = "The austerity measures continue across the restaurant. Nagiyev confronts Kostya the bartender to deliver some bad news. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
    ("anya", "Я просто делал свою работу.",
     "I was just doing my job.",
     [], "new"),
    ("nagiyev", "Мы экономим на всём.",
     "We are saving on everything.",
     [], "new"),
    ("nagiyev", "Мы сэкономили на бармене.",
     "We saved on the bartender.",
     [(351, 'на Бармене сэкономили')], "adapted"),
    ("anya", "Вы не можете меня уволить.",
     "You cannot fire me.",
     [], "new"),
    ("nagiyev", "Ты уволен, балбес.",
     "You are fired, idiot.",
     [(352, 'Ты уволен, балбес')], "adapted"),
    ("anya", "Балбес, да?",
     "An idiot, huh?",
     [(353, 'Балбес, да')], "adapted"),
    ("anya", "Это очень несправедливо.",
     "This is very unfair.",
     [], "new"),
    ("nagiyev", "Ресторан в трудном положении.",
     "The restaurant is in a difficult situation.",
     [], "new"),
    ("anya", "Кто будет наливать напитки?",
     "Who will pour drinks?",
     [], "new"),
    ("nagiyev", "Это больше не твоя проблема.",
     "This is no longer your problem.",
     [], "new"),
    ("anya", "Хорошо, я уйду сегодня.",
     "Fine, I will leave today.",
     [], "new"),
    ("nagiyev", "Вот и отлично.",
     "That is excellent.",
     [], "new"),
]

OPENER = "Let us break down this interaction."

WALK = [
    (0, None,
     "'I was just doing my job.' The verb for 'were doing' is in the masculine past tense, marked by that 'l' sound at the end."),
    (1, None,
     "'We are saving on everything.' Notice the word order: 'we' comes first, and 'everything' finishes the sentence."),
    (2, None,
     "'We saved on the bartender.' Here 'we' sets up the idea, while 'bartender' comes at the end for emphasis."),
    (3, None,
     "'You cannot fire me.' The first content word means 'you', and 'to fire' rounds out the thought."),
    (4, None,
     "'You are fired, idiot.' The key word here means 'you', which Dmitry combines with 'fired'. Then Kostya replies."),
    (5, None,
     "'An idiot, huh?' Here 'blockhead' sets up the idea, while 'blockhead' comes at the end for emphasis."),
    (6, None,
     "'This is very unfair.' Kostya puts 'this' up front so the listener immediately catches the tone, followed by 'very much'."),
    (7, None,
     "'The restaurant is in a difficult situation.' In Russian, 'restaurant' leads into 'position' in a very natural everyday phrasing. And Kostya jumps in."),
    (8, None,
     "'Who will pour drinks?' The first content word means 'who', and 'drinks' rounds out the thought."),
    (9, None,
     "'This is no longer your problem.' Notice the word order: 'this' comes first, and 'problem' finishes the sentence."),
    (10, None,
     "'Fine, I will leave today.' You'll hear 'good' all the time in the show, here connected with 'today'. Dmitry answers straight away."),
    (11, None,
     "'That is excellent.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'perfect' straight to 'perfect'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Kostya realizes he has lost his job as part of the severe cost-cutting strategy."
CLOSING = ("nagiyev", "Вот и отлично.")
