ID = "kukhnya-s04e05-scene-03"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 5
SCENE = 3
TITLE = "Разговор с Германом  (Talking with German)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "german": "anja"}
LABELS = {"anya": "Макс", "german": "Герман"}
SOURCE_NAME = "Кухня (Kukhnya) S4.05"
SOURCE_FILE = "sources/kukhnya/s04/e05.ru.srt"
SOURCE_NOTE = "Cues 41-51. Max nervously enters German Land's office to ask about the vacant sous-chef position, and German surprises him by immediately accepting his candidacy."

INTRO = "Outside the chef's office at Claude Monet, Max gathers his courage and steps inside to speak with German Land. Expecting a harsh rejection, Max tentatively offers to try working as sous-chef, only to receive a remarkably warm answer."

STORY = [
    ("anya", "Я хотел поговорить с вами лично.", "I wanted to talk with you in person.", [(42, "Я сам, в смысле, хотел поговорить.")], "adapted"),
    ("german", "Ну хорошо, я вас внимательно слушаю.", "Well all right, I am listening to you closely.", [(43, "Ну-ну, я вас слушаю.")], "adapted"),
    ("anya", "Сейчас у вас на кухне нет су-шефа.", "Right now you do not have a sous-chef in the kitchen.", [(44, "у вас нет су-шефа.")], "adapted"),
    ("anya", "Я бы мог попробовать эту работу.", "I could try this job.", [(45, "Я бы мог попробовать")], "adapted"),
    ("anya", "Конечно, если вы совсем не против.", "Of course, if you do not mind at all.", [(45, "если вы как бы не против.")], "adapted"),
    ("german", "Вы хотите стать моим новым су-шефом?", "You want to become my new sous-chef?", [(46, "Вы?")], "adapted"),
    ("anya", "Ну, если нет, тогда сразу извините.", "Well, if not, then excuse me right away.", [(47, "Ну, нет, так нет.")], "adapted"),
    ("german", "Да нет, ну почему же сразу нет?", "Oh no, why would it be no right away?", [(47, "Да нет, ну почему же?")], "adapted"),
    ("german", "Мне как раз нужен такой су-шеф.", "I happen to need just such a sous-chef.", [(48, "Мне как раз нужен вот такой"), (49, "су-шеф.")], "adapted"),
    ("german", "Молодой и уверенный в себе человек.", "A young and self-confident person.", [(48, "молодой, уверенный в себе")], "adapted"),
    ("german", "Но вижу, вы не очень рады.", "But I see you are not very glad.", [(50, "Это вы не очень рады.")], "adapted"),
    ("anya", "Я просто очень сдержанный и серьёзный повар.", "I am simply a very reserved and serious cook.", [(50, "А, я просто не только молодой и уверенный,"), (51, "но еще очень сдержанный.")], "adapted"),
]

OPENER = "Let's examine Max's surprising interview with German line by line."

WALK = [
    (0, None, "'I wanted to talk with you in person.' Max opens politely using a past-tense modal verb and instrumental pronoun."),
    (1, None, "'Well all right, I am listening to you closely.' German invites him to speak using a present-tense verb and polite accusative pronoun."),
    (2, None, "'Right now you do not have a sous-chef in the kitchen.' The negative existential word governs the genitive singular of the job title."),
    (3, None, "'I could try this job.' The conditional particle combines with the past tense of 'can' to soften the proposal."),
    (4, None, "'Of course, if you do not mind at all.' A conditional conjunction introduces the predicative adverb meaning opposed or against."),
    (5, None, "'You want to become my new sous-chef?' German checks his ambition using an infinitive that takes the instrumental case."),
    (6, None, "'Well, if not, then excuse me right away.' Max backs away nervously with a polite plural imperative of apology."),
    (7, None, "'Oh no, why would it be no right away?' Colloquial affirmation-negation expresses warm reassurance rather than refusal."),
    (8, None, "'I happen to need just such a sous-chef.' A dative pronoun pairs with the masculine short adjective for needed."),
    (9, None, "'A young and self-confident person.' Two descriptive adjectives depict the ideal candidate for the kitchen post."),
    (10, None, "'But I see you are not very glad.' A plural short-form predicate adjective matches the polite second-person pronoun."),
    (11, None, "'I am simply a very reserved and serious cook.' Max explains his stunned expression with a participle-based adjective meaning restrained."),
]

TRANSITION = "Now let's listen to the entire office interview without interruption."
OUTRO = "To Max's astonishment, German appoints him sous-chef on the spot, setting up a proud announcement in front of the whole kitchen brigade. See you in the next scene."
CLOSING = ("german", "Мне как раз нужен такой су-шеф.")
CLOSING_TRANS = "I happen to need just such a sous-chef."
