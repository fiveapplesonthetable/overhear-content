ID = "kukhnya-s01e16-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 16
SCENE = 12
TITLE = "Крысы в холодильнике  (Rats in the Fridge)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja"}
LABELS = {'anya': 'Шеф', 'leva': 'Лановский'}
SOURCE_NAME = "Кухня (Kukhnya) S1.16"
SOURCE_FILE = "sources/kukhnya/s01/e16.ru.dual.srt"
SOURCE_NOTE = "Cues 153-167."

INTRO = (
    "Lanovsky compares people without documents to rats. He gets a phone call saying they found them in the fridge. He tells Viktor to come with him. Let us listen to their conversation in Russian first."
)

STORY = [
    ("leva", "В этом мире крысы — враги.",
     "In this world rats are enemies.",
     [(154, "поскольку в нашем мире крысы это же враги.")], "adapted"),
    ("leva", "Их все очень ненавидят.",
     "Everyone hates them very much.",
     [(155, "Их все ненавидят.")], "adapted"),
    ("leva", "И вы тоже крыс не любите.",
     "And you also do not like rats.",
     [(156, "И мне кажется, что вы ведь тоже крыс недолюбливаете.")], "adapted"),
    ("leva", "Мыши очень похожи на них.", "Mice are very similar to them.", [], "new"),
    ("anya", "Да, я их не люблю.",
     "Yes, I do not like them.",
     [(157, "Недолюбливаю.")], "adapted"),
    ("leva", "Они как милые мыши.",
     "They are like cute mice.",
     [(159, "И при всем при том, они ничем не отличаются от милых белок,")], "adapted"),
    ("leva", "Но крыс все ненавидят.",
     "But everyone hates rats.",
     [(161, "Только белок-то все любят, а крыс ненавидят.")], "adapted"),
    ("leva", "Извините, мне звонят.",
     "Excuse me, they are calling me.",
     [(163, "Извините.")], "adapted"),
    ("leva", "Да, я вас слушаю.",
     "Yes, I am listening to you.",
     [(164, "Я слушаю.")], "adapted"),
    ("leva", "Где они? В холодильнике?",
     "Where are they? In the fridge?",
     [(165, "Где? В холодильнике?")], "adapted"),
    ("leva", "Замечательно, мы сейчас идём.",
     "Great, we are going now.",
     [(166, "Замечательно. Сейчас идем.")], "adapted"),
    ("leva", "Виктор Петрович, пойдёмте со мной.",
     "Viktor Petrovich, let us go with me.",
     [(167, "Виктор Петрович, вы не могли бы пройти со мной?")], "adapted"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'In this world rats are enemies.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'that' straight to 'enemy'."),
    (1, None,
     "'Everyone hates them very much.' You'll hear 'them' all the time in the show, here connected with 'hate'."),
    (2, None,
     "'And you also do not like rats.' The first content word means 'you', and 'to love' rounds out the thought."),
    (3, None,
     "'Mice are very similar to them.' You'll hear 'mouse' all the time in the show, here connected with 'them'. Chef Viktor answers straight away."),
    (4, None,
     "'Yes, I do not like them.' The key word here means 'I', which Chef Viktor combines with 'them'."),
    (5, None,
     "'They are like cute mice.' You'll hear 'they' all the time in the show, here connected with 'mouse'."),
    (6, None,
     "'But everyone hates rats.' In Russian, 'rat' leads into 'hate' in a very natural everyday phrasing."),
    (7, None,
     "'Excuse me, they are calling me.' the speaker starts with 'sorry' and pairs it with 'to me' to make the point clear."),
    (8, None,
     "'Yes, I am listening to you.' The first content word means 'I', and 'I'm listening' rounds out the thought."),
    (9, None,
     "'Where are they? In the fridge?' the speaker starts with 'where' and pairs it with 'they' to make the point clear."),
    (10, None,
     "'Great, we are going now.' Here 'wonderful' sets up the idea, while 'are going' comes at the end for emphasis."),
    (11, None,
     "'Viktor Petrovich, let us go with me.' You'll hear 'Viktor' all the time in the show, here connected with 'me'."),
]



TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around rats in the fridge, and for the words meaning 'world' and 'rat'. You'll catch them now. See you next time."
CLOSING = ("leva", "Виктор Петрович, пойдёмте со мной.")
