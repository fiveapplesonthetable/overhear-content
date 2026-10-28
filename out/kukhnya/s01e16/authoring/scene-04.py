ID = "kukhnya-s01e16-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 4
TITLE = "Любопытный Макс  (Curious Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Макс', 'leva': 'Виктор'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the kitchen, Max is bored and looking for a distraction. He approaches Chef Victor and curiously asks about the special dish the chef is preparing, but Victor quickly shuts him down. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Шеф.",
     "Chef.",
     [(33, 'Шеф.')], "adapted"),
    ("leva", "Что тебе надо?",
     "What do you need?",
     [], "new"),
    ("anya", "А что вы готовите?",
     "And what are you preparing?",
     [(34, 'А что вы готовите?')], "adapted"),
    ("leva", "А тебе какое дело?",
     "And what is it to you?",
     [(34, 'Тебе какое дело?')], "adapted"),
    ("leva", "Тебе нечем заняться?",
     "Do you have nothing to do?",
     [(35, 'Тебе что, заняться нечем?')], "adapted"),
    ("anya", "У меня есть пять минут.",
     "I have five minutes.",
     [(35, 'Ну, у меня пять минут есть,')], "adapted"),
    ("anya", "Я хотел поучиться у вас.",
     "I wanted to learn from you.",
     [(35, 'я хотел поучиться у вас.')], "adapted"),
    ("leva", "Иди работай.",
     "Go work.",
     [], "new"),
    ("anya", "А можно попробовать?",
     "And can I try it?",
     [(36, 'А можно попробовать?')], "adapted"),
    ("leva", "Нет, нельзя.",
     "No, you cannot.",
     [], "new"),
    ("anya", "Почему?",
     "Why?",
     [], "new"),
    ("leva", "Потому что я так сказал.",
     "Because I said so.",
     [], "new"),
    ("anya", "Ладно, я понял.",
     "Alright, I understand.",
     [], "new"),
    ("leva", "Тогда иди отсюда.",
     "Then go from here.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Chef.' — Built around the key proper name meaning 'chef, boss'."),
    (1, None,
     "'What do you need?' The key word here means 'what', which Viktor combines with 'for you'. And Max jumps in."),
    (2, None,
     "'And what are you preparing?' Max puts 'what' up front so the listener immediately catches the tone, followed by 'you'."),
    (3, None,
     "'And what is it to you?' Viktor uses the casual singular 'you' with 'for you', as close colleagues and friends do."),
    (4, None,
     "'Do you have nothing to do?' In Russian, 'for you' leads into 'to attend to' in a very natural everyday phrasing. Max answers straight away."),
    (5, None,
     "'I have five minutes.' Max starts with 'me' and pairs it with 'there is' to make the point clear."),
    (6, None,
     "'I wanted to learn from you.' The key word here means 'I', which Max combines with 'wanted'."),
    (7, None,
     "'Go work.' Listen for the word meaning 'go' right alongside 'work' in this line. Then Max replies."),
    (8, None,
     "'And can I try it?' The first content word means 'may', and 'to taste' rounds out the thought."),
    (9, None,
     "'No, you cannot.' A compact expression built around 'not allowed' and 'not allowed'."),
    (10, None,
     "'Why?' Listen for the word meaning 'why' right alongside 'why' in this line. And Viktor jumps in."),
    (11, None,
     "'Because I said so.' The question word for 'what' comes right at the start, followed directly by 'said'."),
    (12, None,
     "'Alright, I understand.' Notice the word order: 'I' comes first, and 'understood?' finishes the sentence."),
    (13, None,
     "'Then go from here.' The key word here means 'back then', which Viktor combines with 'go'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around curious max, and for the words meaning 'to cook' and 'what a'. You'll catch them now. See you next time."
CLOSING = ("leva", "Тогда иди отсюда.")
