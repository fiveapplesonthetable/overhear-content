ID = "kukhnya-s01e14-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 19
TITLE = "План Макса  (Max's Plan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Макс', 'leva': 'Илья', 'guest': 'Саша'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In a brief moment of chaos, Max realizes he needs to take control of a difficult situation. He tells his colleagues that they will figure it out and urges them to go. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Ладно, мы разберёмся с этим.",
     "Alright, we will figure this out.",
     [(280, 'Ладно, разберёмся.')], "adapted"),
    ("anya", "Всё будет хорошо.",
     "Everything will be fine.",
     [], "exact"),
    ("leva", "Что нам делать сейчас?",
     "What should we do now?",
     [], "exact"),
    ("anya", "Поехали.",
     "Let's go.",
     [(281, 'Поехали.')], "adapted"),
    ("guest", "Куда мы едем?",
     "Where are we going?",
     [], "exact"),
    ("anya", "Мы никуда не едем.",
     "We are not going anywhere.",
     [], "exact"),
    ("anya", "Это значит, что мы начинаем.",
     "It means that we are starting.",
     [], "exact"),
    ("leva", "Теперь я всё понял.",
     "Now I understand everything.",
     [(282, 'Теперь')], "adapted"),
    ("guest", "Тогда давайте работать.",
     "Then let's work.",
     [], "exact"),
    ("anya", "Да, за работу.",
     "Yes, back to work.",
     [], "exact"),
    ("leva", "У нас мало времени.",
     "We have little time.",
     [], "new"),
    ("guest", "Мы должны успеть.",
     "We must be in time.",
     [], "new"),
    ("anya", "Конечно мы успеем.",
     "Of course we will be in time.",
     [], "new"),
    ("leva", "Тогда начинаем прямо сейчас.",
     "Then we start right now.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Alright, we will figure this out.' The reflexive ending on the verb for 'will sort this out' turns the action back onto the subject."),
    (1, None,
     "'Everything will be fine.' Notice the word order: 'will be' comes first, and 'good' finishes the sentence. Ilya answers straight away."),
    (2, None,
     "'What should we do now?' Here 'what' sets up the idea, while 'now' comes at the end for emphasis."),
    (3, None,
     "'Let's go.' You'll hear 'here we go' all the time in the show, here connected with 'here we go'."),
    (4, None,
     "'Where are we going?' The key word here means 'where to', which Sasha combines with 'we'. Then Max replies."),
    (5, None,
     "'We are not going anywhere.' Max starts with 'we' and pairs it with 'nowhere' to make the point clear."),
    (6, None,
     "'It means that we are starting.' Max puts 'this' up front so the listener immediately catches the tone, followed by 'then'."),
    (7, None,
     "'Now I understand everything.' In Russian, 'now' leads into 'understood?' in a very natural everyday phrasing. And Sasha jumps in."),
    (8, None,
     "'Then let's work.' The key word here means 'back then', which Sasha combines with 'let's'."),
    (9, None,
     "'Yes, back to work.' A compact expression built around 'job' and 'job'."),
    (10, None,
     "'We have little time.' Ilya starts with 'us' and pairs it with 'little' to make the point clear. Sasha answers straight away."),
    (11, None,
     "'We must be in time.' Notice the word order: 'we' comes first, and 'to make it' finishes the sentence."),
    (12, None,
     "'Of course we will be in time.' Listen for the word meaning 'of course' right alongside 'we' in this line."),
    (13, None,
     "'Then we start right now.' The first content word means 'back then', and 'now' rounds out the thought."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around max's plan, and for the words meaning 'will sort this out' and 'will be'. You'll catch them now. See you next time."
CLOSING = ("leva", "Тогда начинаем прямо сейчас.")
