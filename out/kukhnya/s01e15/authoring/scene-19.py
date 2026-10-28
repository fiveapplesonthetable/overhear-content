ID = "kukhnya-s01e15-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 15
SCENE = 19
TITLE = "Омлет шефа  (The Chef's Omelet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Виктор', 'leva': 'Лёва', 'guest': 'Мама'}
SOURCE_NAME = "Кухня (Kukhnya) S1.15"
SOURCE_FILE = "sources/kukhnya/s01/e15.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "In the morning, Chef Victor cooks breakfast for Leva and his mother. Leva wonders if this is Victor's way of apologizing for his earlier deception. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Доброе утро, Виктор.",
     "Good morning, Viktor.",
     [(366, 'Доброе утро. Доброе, доброе.')], "adapted"),
    ("guest", "Доброе утро.",
     "Good morning.",
     [(366, 'Доброе, доброе.')], "adapted"),
    ("guest", "Виктор приготовил такой омлет.",
     "Victor prepared such an omelet.",
     [(367, 'Виктор Петрович приготовил такой омлет.')], "adapted"),
    ("leva", "Это типа извинения?",
     "Is this a kind of apology?",
     [(368, 'Это типа извинения?')], "adapted"),
    ("anya", "Это типа омлет.",
     "This is a kind of omelet.",
     [(369, 'Это типа омлет.')], "adapted"),
    ("anya", "Ешь давай.",
     "Come on, eat.",
     [(370, 'Ешь давай, я на работу опоздаю.')], "adapted"),
    ("anya", "Я опоздаю на работу.",
     "I will be late for work.",
     [(370, 'я на работу опоздаю.')], "adapted"),
    ("guest", "Да, кушайте быстрее.",
     "Yes, eat faster.",
     [], "new"),
    ("leva", "Ладно, я съем это.",
     "Alright, I will eat this.",
     [], "new"),
    ("anya", "Это очень вкусно.",
     "This is very delicious.",
     [], "new"),
    ("guest", "Нам пора идти.",
     "It is time for us to go.",
     [], "new"),
    ("leva", "Спасибо за завтрак.",
     "Thank you for the breakfast.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Good morning, Viktor.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'good' straight to 'Viktor'."),
    (1, None,
     "'Good morning.' Notice the word order: 'good' comes first, and 'morning' finishes the sentence."),
    (2, None,
     "'Victor prepared such an omelet.' — Notice the proper name meaning 'Viktor' paired with the verb for 'cooked'."),
    (3, None,
     "'Is this a kind of apology?' The first content word means 'this', and 'apologies' rounds out the thought."),
    (4, None,
     "'This is a kind of omelet.' The key word here means 'this', which Viktor combines with 'guy'."),
    (5, None,
     "'Come on, eat.' In Russian, 'eat' leads into 'let's' in a very natural everyday phrasing."),
    (6, None,
     "'I will be late for work.' Viktor starts with 'I' and pairs it with 'to be late' to make the point clear."),
    (7, None,
     "'Yes, eat faster.' the speaker puts 'eat' up front so the listener immediately catches the tone, followed by 'faster'. And Lyova jumps in."),
    (8, None,
     "'Alright, I will eat this.' The key word here means 'I', which Lyova combines with 'to eat up'."),
    (9, None,
     "'This is very delicious.' A compact expression built around 'this' and 'it's tasty'."),
    (10, None,
     "'It is time for us to go.' Listen for the word meaning 'us' right alongside 'it's time' in this line. Lyova answers straight away."),
    (11, None,
     "'Thank you for the breakfast.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'thank you' straight to 'breakfast'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around the chef's omelet, and for the words meaning 'good' and 'morning'. You'll catch them now. See you next time."
CLOSING = ("leva", "Спасибо за завтрак.")
