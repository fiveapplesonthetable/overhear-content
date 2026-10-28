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
     "'Let's try this.' — Notice the verb meaning 'let's (do it)' paired with the pronoun for 'we'."),
    (1, None,
     "'Jacques, where are you?' — Notice the noun meaning 'Jacques' paired with the pronoun for 'you'."),
    (2, None,
     "'I am here, I am coming!' — Notice the pronoun meaning 'I' paired with the adverb for 'here'."),
    (3, None,
     "'And who are you?' — Notice the pronoun meaning 'you' paired with the pronoun for 'who'."),
    (4, None,
     "'He is my neighbor.' — Notice the pronoun meaning 'he' paired with the det for 'my'."),
    (5, None,
     "'Can you imagine, we lived in Paris.' — Notice the verb meaning 'can you imagine, believe' paired with the pronoun for 'we'."),
    (6, None,
     "'Wait, we are not going to kiss.' — Notice the verb meaning 'wait' paired with the pronoun for 'we'."),
    (7, None,
     "'First we need to have a bite.' — Notice the adverb meaning 'first, at first' paired with the adverb for 'it is necessary'."),
    (8, None,
     "'Here, try this.' — Notice the verb meaning 'to try, to taste' paired with the pronoun for 'this'."),
    (9, None,
     "'This is very delicious.' — Notice the pronoun meaning 'this' paired with the adverb for 'very much'."),
    (10, None,
     "'He says that it is delicious?' — Notice the pronoun meaning 'he' paired with the verb for 'talks'."),
    (11, None,
     "'Yes, he likes it very much.' — Notice the pronoun meaning '(to) him' paired with the adverb for 'very much'."),
    (12, None,
     "'Thank you, my dear friend.' — Notice the interjection meaning 'thank you' paired with the det for 'my'."),
    (13, None,
     "'You are welcome, eat to your health.' — Notice the verb meaning 'eat' paired with the noun for 'health'."),
]

TRANSITION = "Now let us listen to the conversation once again."
OUTRO = "The conversation concludes the matter at hand."
CLOSING = ("anya", "Пожалуйста, кушай на здоровье.")
