ID = "kukhnya-s01e15-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 20
TITLE = "Ожидание Макса  (Waiting for Max)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Илья', 'leva': 'Сеня'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Back at the restaurant, the staff is waiting to see if Max will finally return to work after everything that happened. They discuss his possible arrival. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Тебя это тоже волнует?",
     "Does this worry you too?",
     [(372, 'Тебя это тоже воспринимает?')], "adapted"),
    ("leva", "Что именно?",
     "What exactly?",
     [], "new"),
    ("anya", "Например, Макс придёт или нет?",
     "For example, will Max come or not?",
     [(373, 'Например, зайдет Макс или нет?')], "adapted"),
    ("leva", "Я думаю, он придёт.",
     "I think he will come.",
     [], "new"),
    ("anya", "Он любит нашу кухню.",
     "He loves our kitchen.",
     [], "new"),
    ("leva", "И он любит работать.",
     "And he loves to work.",
     [], "new"),
    ("anya", "А как же шеф?",
     "And what about the chef?",
     [], "new"),
    ("leva", "Шеф его простит.",
     "The chef will forgive him.",
     [], "new"),
    ("anya", "Они помирятся.",
     "They will make peace.",
     [], "new"),
    ("leva", "Конечно помирятся.",
     "Of course they will make peace.",
     [], "new"),
    ("anya", "Тогда всё будет хорошо.",
     "Then everything will be fine.",
     [], "new"),
    ("leva", "Да, просто ждём.",
     "Yes, we are just waiting.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Does this worry you too?' Here 'you' sets up the idea, while 'to worry' comes at the end for emphasis."),
    (1, None,
     "'What exactly?' You'll hear 'what' all the time in the show, here connected with 'what'."),
    (2, None,
     "'For example, will Max come or not?' Here 'for example' sets up the idea, while 'will come' comes at the end for emphasis. Senya answers straight away."),
    (3, None,
     "'I think he will come.' Senya starts with 'I' and pairs it with 'I think' to make the point clear."),
    (4, None,
     "'He loves our kitchen.' Ilya puts 'he' up front so the listener immediately catches the tone, followed by 'loves'."),
    (5, None,
     "'And he loves to work.' The key word here means 'he', which Senya combines with 'loves'. Then Ilya replies."),
    (6, None,
     "'And what about the chef?' Ilya puts 'how' up front so the listener immediately catches the tone, followed by 'chef'."),
    (7, None,
     "'The chef will forgive him.' — Notice the proper name meaning 'chef, boss' paired with the pronoun for 'him'."),
    (8, None,
     "'They will make peace.' The first content word means 'they', and 'to make up' rounds out the thought. And Senya jumps in."),
    (9, None,
     "'Of course they will make peace.' A compact expression built around 'of course' and 'to make up'."),
    (10, None,
     "'Then everything will be fine.' The first content word means 'back then', and 'good' rounds out the thought."),
    (11, None,
     "'Yes, we are just waiting.' A compact expression built around 'just' and 'we wait'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around waiting for max, and for the words meaning 'to worry' and 'will come'. You'll catch them now. See you next time."
CLOSING = ("leva", "Да, просто ждём.")
