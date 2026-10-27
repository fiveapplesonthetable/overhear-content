from pathlib import Path

ID = "kukhnya-s01e10-scene-40"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 40
TITLE = "Звонок владельца  (The Owner's Call)"
LEVEL = "A1"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"anya": "Шеф", "senya": "Сеня"}
SOURCE_NAME = "Кухня s01e10"
SOURCE_FILE = Path("sources/kukhnya/s01/e10.ru.dual.srt")

INTRO = (
    "In the back room of Claude Monet, Chef Barinov is engrossed in an intense televised football match. "
    "His viewing is interrupted when Senya rushes in to report that restaurant owner Dmitry Nagiyev urgently wants to see him. "
    "Let's listen to their conversation in Russian."
)

STORY = [
    ("anya", "Сеня, не мешай мне смотреть футбол!",
     "Senya, don't disturb me watching football!",
     [(286, "футбол начинается")], "demanding quiet for game"),
    ("senya", "Шеф, вас срочно зовёт Дмитрий Владимирович!",
     "Chef, Dmitry Vladimirovich is urgently calling you!",
     [(289, "вас Дмитрий Владимирович зовет")], "delivering urgent summons"),
    ("anya", "Почему хозяин звонит именно в этот момент?",
     "Why does the owner call at this exact moment?",
     [(289, "Дмитрий Владимирович")], "grumbling about bad timing"),
    ("senya", "Он сказал, что это очень срочное дело.",
     "He said that this is a very urgent matter.",
     [(289, "зовет")], "emphasizing urgency"),
    ("anya", "Я знаю этого человека целых двадцать лет.",
     "I have known this man for a whole twenty years.",
     [(288, "Я же вас 20 лет знаю")], "reflecting on long acquaintance"),
    ("senya", "Он ждёт вас прямо сейчас возле зала.",
     "He is waiting for you right now near the hall.",
     [(290, "Шеф")], "urging Barinov to hurry"),
    ("anya", "Наша команда ведёт в счёте два ноль!",
     "Our team is leading in the score two-nil!",
     [(292, "Следи за счетом")], "pointing at match score"),
    ("senya", "Я обещаю внимательно следить за футбольным счётом.",
     "I promise to attentively watch the football score.",
     [(292, "Следи за счетом")], "promising to monitor game"),
    ("anya", "Если наша команда проиграет, я накажу тебя!",
     "If our team loses, I will punish you!",
     [(292, "Следи за счетом")], "threatening cook"),
    ("senya", "Шеф, я не отойду от экрана телевизора.",
     "Chef, I will not step away from the TV screen.",
     [(292, "Следи за счетом")], "reassuring vigilance"),
    ("anya", "Ладно, я пойду и выслушаю Дмитрия Нагиева.",
     "Fine, I will go and listen to Dmitry Nagiyev.",
     [(290, "Шеф")], "reluctantly agreeing to go"),
    ("senya", "Удачи вам в разговоре с нашим хозяином!",
     "Good luck to you in the talk with our master!",
     [(289, "Дмитрий Владимирович")], "wishing luck"),
    ("anya", "Смотри в оба и внимательно следи за счётом!",
     "Keep your eyes peeled and attentively watch the score!",
     [(292, "Следи за счетом")], "leaving final command"),
]

OPENER = (
    "Let's examine the dialogue sentence by sentence. "
    "Notice the workplace hierarchy, sports fandom expressions, and urgent managerial summons."
)

WALK = [
    (0, "Сеня, не мешай мне смотреть футбол!",
     "'Senya, don't disturb me watching football!' Direct address name with negative imperative verb, dative pronoun, imperfective infinitive, and direct object noun."),
    (1, "Шеф, вас срочно зовёт Дмитрий Владимирович!",
     "'Chef, Dmitry Vladimirovich is urgently calling you!' Direct address title with accusative pronoun, manner adverb, present verb, and nominative full name phrase."),
    (2, "Почему хозяин звонит именно в этот момент?",
     "'Why does the owner call at this exact moment?' Interrogative adverb with nominative subject noun, present verb, emphatic particle, and locative prepositional phrase."),
    (3, "Он сказал, что это очень срочное дело.",
     "'He said that this is a very urgent matter.' Subject pronoun with past verb, subordinating conjunction, demonstrative pronoun, degree adverb, and nominative adjective-noun phrase."),
    (4, "Я знаю этого человека целых двадцать лет.",
     "'I have known this man for a whole twenty years.' Subject pronoun with present verb, accusative demonstrative-noun phrase, quantitative adjective, and cardinal numeral-noun phrase."),
    (5, "Он ждёт вас прямо сейчас возле зала.",
     "'He is waiting for you right now near the hall.' Subject pronoun with present transitive verb, accusative pronoun, temporal idiomatic phrase, and genitive prepositional noun phrase."),
    (6, "Наша команда ведёт в счёте два ноль!",
     "'Our team is leading in the score two-nil!' Possessive determiner with subject noun, present verb, locative prepositional noun, and cardinal score numerals."),
    (7, "Я обещаю внимательно следить за футбольным счётом.",
     "'I promise to attentively watch the football score.' Subject pronoun with present performative verb, manner adverb, imperfective infinitive, and prepositional adjective-noun phrase."),
    (8, "Если наша команда проиграет, я накажу тебя!",
     "'If our team loses, I will punish you!' Conditional conjunction with possessive determiner, subject noun, future verb, subject pronoun, future verb, and accusative pronoun."),
    (9, "Шеф, я не отойду от экрана телевизора.",
     "'Chef, I will not step away from the TV screen.' Direct address title with subject pronoun, negated future verb, and genitive prepositional compound-noun phrase."),
    (10, "Ладно, я пойду и выслушаю Дмитрия Нагиева.",
     "'Fine, I will go and listen to Dmitry Nagiyev.' Particle of agreement with subject pronoun, future motion verb, coordinating conjunction, future verb, and accusative name phrase."),
    (11, "Удачи вам в разговоре с нашим хозяином!",
     "'Good luck to you in the talk with our master!' Genitive wish noun with dative pronoun, locative prepositional phrase, and instrumental prepositional possessive-noun phrase."),
    (12, "Смотри в оба и внимательно следи за счётом!",
     "'Keep your eyes peeled and attentively watch the score!' Idiomatic imperative phrase with coordinating conjunction, manner adverb, imperative verb, and prepositional phrase."),
]

TRANSITION = "Now let's listen to the entire exchange one more time at normal speed."

OUTRO = (
    "Reluctantly leaving his televised football match, Chef Barinov leaves Senya in charge of the score and heads out to meet Nagiyev. "
    "Great work practicing conversational Russian!"
)

CLOSING = ("anya", "Смотри в оба и внимательно следи за счётом!")
