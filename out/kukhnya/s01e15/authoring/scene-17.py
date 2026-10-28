ID = "kukhnya-s01e15-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 17
TITLE = "Желание переехать  (Desire to Move In)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Макс', 'leva': 'Вика'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Max arrives at Victoria's apartment and awkwardly asks to move in with her. He tries to sound independent, but eventually admits his true feelings. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Привет, Макс.",
     "Hi, Max.",
     [(335, 'Привет.')], "adapted"),
    ("leva", "Привет.",
     "Hi.",
     [(335, 'Привет.')], "adapted"),
    ("anya", "Я хочу переехать к тебе.",
     "I want to move to your place.",
     [(336, 'Я хочу переехать к тебе.')], "adapted"),
    ("leva", "Тебе негде жить?",
     "Do you have nowhere to live?",
     [(337, 'Что, негде жить?')], "adapted"),
    ("anya", "Нет, у меня миллион вариантов.",
     "No, I have a million options.",
     [(337, 'Да нет, просто...'), (338, 'Да миллион вариантов.')], "adapted"),
    ("anya", "Костя зовёт меня назад.",
     "Kostya is calling me back.",
     [(338, 'Просто Костя назад зовет,')], "adapted"),
    ("anya", "Лёва тоже приглашает жить.",
     "Leva is also inviting me to live.",
     [(338, 'Лёва тоже приглашает,')], "adapted"),
    ("anya", "Но я готов жить с тобой.",
     "But I am ready to live with you.",
     [(339, 'Но я готов жить с тобой.')], "adapted"),
    ("leva", "Что ты хочешь сказать?",
     "What do you want to say?",
     [], "new"),
    ("anya", "Я хочу жить с тобой.",
     "I want to live with you.",
     [(340, 'В смысле, хочу.')], "adapted"),
    ("anya", "Я не хочу быть без тебя.",
     "I do not want to be without you.",
     [(341, 'В смысле, не хочу без тебя.')], "adapted"),
    ("leva", "Это очень приятно слышать.",
     "That is very pleasant to hear.",
     [], "new"),
    ("anya", "Правда?",
     "Really?",
     [], "new"),
    ("leva", "Да, я тебе верю.",
     "Yes, I believe you.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Hi, Max.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'hi' straight to 'Max'."),
    (1, None,
     "'Hi.' In Russian, 'hi' leads into 'hi' in a very natural everyday phrasing."),
    (2, None,
     "'I want to move to your place.' Here 'I' sets up the idea, while 'for you' comes at the end for emphasis. Then Vika replies."),
    (3, None,
     "'Do you have nowhere to live?' Here 'for you' sets up the idea, while 'to live' comes at the end for emphasis."),
    (4, None,
     "'No, I have a million options.' You'll hear 'me' all the time in the show, here connected with 'options'."),
    (5, None,
     "'Kostya is calling me back.' — Notice the proper name meaning 'Kostya' paired with the verb for 'calls'."),
    (6, None,
     "'Leva is also inviting me to live.' — Notice the proper name meaning 'Lyova' paired with the adverb for 'too'."),
    (7, None,
     "'But I am ready to live with you.' In Russian, 'I' leads into 'you' in a very natural everyday phrasing."),
    (8, None,
     "'What do you want to say?' Vika starts with 'what' and pairs it with 'you' to make the point clear. Max answers straight away."),
    (9, None,
     "'I want to live with you.' A compact expression built around 'I' and 'you'."),
    (10, None,
     "'I do not want to be without you.' Listen for the word meaning 'I' right alongside 'want' in this line."),
    (11, None,
     "'That is very pleasant to hear.' In Russian, 'this' leads into 'to hear' in a very natural everyday phrasing. Then Max replies."),
    (12, None,
     "'Really?' Notice the word order: 'honestly' comes first, and 'honestly' finishes the sentence."),
    (13, None,
     "'Yes, I believe you.' Here 'I' sets up the idea, while 'believe' comes at the end for emphasis."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around desire to move in, and for the words meaning 'want' and 'to move in'. You'll catch them now. See you next time."
CLOSING = ("leva", "Да, я тебе верю.")
