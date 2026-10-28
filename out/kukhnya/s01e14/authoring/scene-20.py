ID = "kukhnya-s01e14-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 14
SCENE = 20
TITLE = "Сосед из Парижа  (A Neighbor from Paris)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "leva": "anja", "guest": "angelina"}
LABELS = {'anya': 'Виктор', 'leva': 'Жак', 'guest': 'Дмитрий'}
SOURCE_NAME = "Кухня (Kukhnya) S1.14"
SOURCE_FILE = "sources/kukhnya/s01/e14.ru.dual.srt"
SOURCE_NOTE = "Cues."

INTRO = (
    "Chef Victor wants to impress someone with his French friend Jacques. Jacques mumbles in French and tries to kiss Victor. Victor stops him and offers him some food first. Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Давайте мы попробуем это.",
     "Let's try this.",
     [(283, 'давайте попробуем.')], "adapted"),
    ("anya", "Жак, ты где?",
     "Jacques, where are you?",
     [(284, 'Жак!')], "adapted"),
    ("leva", "Я здесь, я иду!",
     "I am here, I am coming!",
     [(285, 'Жак! Несу, несу!')], "adapted"),
    ("guest", "А вы кто такой?",
     "And who are you?",
     [(288, 'А вы кто? Сосед.')], "adapted"),
    ("anya", "Он мой сосед.",
     "He is my neighbor.",
     [(288, 'Сосед.')], "adapted"),
    ("guest", "Представляешь, мы жили в Париже.",
     "Can you imagine, we lived in Paris.",
     [(290, 'Его. Представляешь, мы с ним жили в Париже на соседних улицах.')], "adapted"),
    ("anya", "Подожди, мы не будем целоваться.",
     "Wait, we are not going to kiss.",
     [(293, 'Подожди, целоваться.')], "adapted"),
    ("anya", "Сначала надо закусить.",
     "First we need to have a bite.",
     [(294, 'Сначала закусить.')], "adapted"),
    ("anya", "На, попробуй это.",
     "Here, try this.",
     [(295, 'На, попробуй.')], "adapted"),
    ("leva", "Это очень вкусно.",
     "This is very delicious.",
     [(296, 'Очень вкусно.')], "adapted"),
    ("guest", "Он говорит, что это вкусно?",
     "He says that it is delicious?",
     [], "new"),
    ("anya", "Да, ему очень нравится.",
     "Yes, he likes it very much.",
     [], "new"),
    ("leva", "Спасибо, мой дорогой друг.",
     "Thank you, my dear friend.",
     [], "new"),
    ("anya", "Пожалуйста, кушай на здоровье.",
     "You are welcome, eat to your health.",
     [], "new"),
]

OPENER = "Now let us examine the conversation line by line."

WALK = [
    (0, None,
     "'Let's try this.' The first content word means 'let's', and 'this' rounds out the thought."),
    (1, None,
     "'Jacques, where are you?' Listen for the word meaning 'Jacques' right alongside 'you' in this line."),
    (2, None,
     "'I am here, I am coming!' Here 'I' sets up the idea, while 'going' comes at the end for emphasis. Dmitry answers straight away."),
    (3, None,
     "'And who are you?' In Russian, 'you' leads into 'who' in a very natural everyday phrasing."),
    (4, None,
     "'He is my neighbor.' The key word here means 'he', which Viktor combines with 'neighbour'."),
    (5, None,
     "'Can you imagine, we lived in Paris.' Dmitry starts with 'can you imagine' and pairs it with 'we' to make the point clear. Then Viktor replies."),
    (6, None,
     "'Wait, we are not going to kiss.' Viktor puts 'wait' up front so the listener immediately catches the tone, followed by 'we'."),
    (7, None,
     "'First we need to have a bite.' In Russian, 'first' leads into 'have a bite' in a very natural everyday phrasing."),
    (8, None,
     "'Here, try this.' Notice the word order: 'to try' comes first, and 'this' finishes the sentence."),
    (9, None,
     "'This is very delicious.' A compact expression built around 'this' and 'it's tasty'."),
    (10, None,
     "'He says that it is delicious?' Listen for the word meaning 'he' right alongside 'talks' in this line."),
    (11, None,
     "'Yes, he likes it very much.' The reflexive ending on the verb for 'is pleasing' turns the action back onto the subject."),
    (12, None,
     "'Thank you, my dear friend.' Notice the word order: 'thank you' comes first, and 'friend' finishes the sentence."),
    (13, None,
     "'You are welcome, eat to your health.' Viktor starts with 'eat' and pairs it with 'health' to make the point clear."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around a neighbor from paris, and for the words meaning 'let's' and 'try'. You'll catch them now. See you next time."
CLOSING = ("anya", "Пожалуйста, кушай на здоровье.")
