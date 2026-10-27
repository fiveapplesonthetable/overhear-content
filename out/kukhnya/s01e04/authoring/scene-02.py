ID = "kukhnya-s01e04-scene-02"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = "Встреча конкурентов  (Encounter of the Competitors)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Елена", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 6-19. Chef Viktor Barinov runs into rival head chef Elena Sokolova on the street. "
    "Barinov mocks her hiring ads, while Elena subtly hints that Claude Monet's own cooks are applying to work for her."
)

INTRO = (
    "Outside the restaurant, Chef Viktor Barinov bumps into his culinary rival, Elena Sokolova. "
    "Barinov mocks Arcobaleno's newspaper advertisements for new kitchen staff, asserting that real cooks never answer ads. "
    "Elena smoothly retorts that top talent from respectable kitchens has already applied, hinting that Claude Monet staff might be among them. "
    "Let's listen to their confrontation in Russian first."
)

STORY = [
    ("chef", "Елена, вы набираете поваров по объявлению?",
     "Elena, are you hiring cooks through an ad?",
     [(6, "вы персонал по объявлению набираете")], "adapted"),
    ("anya", "Здравствуйте, Виктор Петрович. Да, мы расширяемся.",
     "Hello, Viktor Petrovich. Yes, we are expanding.",
     [(6, "Виктор Петрович")], "adapted"),
    ("chef", "Поставьте лучше табличку возле метро!",
     "You had better put a sign near the metro!",
     [(7, "Вы бы лучше табличку у метро поставили")], "adapted"),
    ("anya", "В этом нет никакой необходимости.",
     "There is no need for that.",
     [(9, "в этом нет необходимости")], "adapted"),
    ("chef", "Нормальные профессионалы не ищут работу по газетам.",
     "Normal professionals do not look for work in newspapers.",
     [(8, "проходимость профессиональных поваров выше")], "adapted"),
    ("anya", "Ко мне уже пришли отличные кандидаты.",
     "Excellent candidates have already come to me.",
     [(10, "пришло несколько отличных поваров")], "adapted"),
    ("chef", "И из каких ресторанов эти люди?",
     "And from which restaurants are these people?",
     [], "new"),
    ("anya", "Некоторые работают в очень достойных местах.",
     "Some work in very respectable places.",
     [(11, "некоторые из них работают в достойных ресторанах")], "adapted"),
    ("chef", "Неужели кто-то уходит из хороших ресторанов?",
     "Could someone really be leaving good restaurants?",
     [], "new"),
    ("anya", "Может быть, даже из вашего ресторана.",
     "Maybe even from your restaurant.",
     [(13, "если вы считаете свой ресторан")], "adapted"),
    ("chef", "Я съем колпак, если мои повара уйдут!",
     "I will eat my chef's hat if my cooks leave!",
     [(14, "Я съем свой колпак, если узнаю, что кто-то из моих")], "adapted"),
    ("anya", "Тогда заранее желаю вам приятного аппетита!",
     "Then in advance I wish you bon appétit!",
     [(15, "Тогда приятного аппетита")], "adapted"),
    ("chef", "Мои люди преданы мне до конца.",
     "My people are loyal to me to the end.",
     [], "new"),
]

OPENER = "Now let's examine Barinov and Elena's witty street dialogue line by line."

WALK = [
    (0, None,
     "'Elena, are you hiring cooks through an ad?' Barinov starts the banter with an accusative plural noun."),
    (1, None,
     "'Hello, Viktor Petrovich. Yes, we are expanding.' Elena greets him politely and mentions business growth."),
    (2, None,
     "'You had better put a sign near the metro!' The chef suggests a sarcastic alternative with a comparative adverb."),
    (3, None,
     "'There is no need for that.' Elena dismisses the mockery with a genitive negation structure."),
    (4, None,
     "'Normal professionals do not look for work in newspapers.' Barinov insults applicant quality with a generalized plural."),
    (5, None,
     "'Excellent candidates have already come to me.' Elena counters confidently with a past perfective verb."),
    (6, None,
     "'And from which restaurants are these people?' Barinov inquires skeptically using an interrogative prepositional phrase."),
    (7, None,
     "'Some work in very respectable places.' Elena hints at high standards with an adjective and prepositional noun."),
    (8, None,
     "'Could someone really be leaving good restaurants?' Barinov questions worker loyalty with an emphatic particle."),
    (9, None,
     "'Maybe even from your restaurant.' Elena drops a sharp hint using a parenthetical phrase and pronoun."),
    (10, None,
     "'I will eat my chef's hat if my cooks leave!' Barinov makes an outrageous wager using a future transitive verb."),
    (11, None,
     "'Then in advance I wish you bon appétit!' Elena playfully retorts with a polite festive greeting."),
    (12, None,
     "'My people are loyal to me to the end.' Barinov reasserts team loyalty with a short predicate adjective."),
]

TRANSITION = "Now let's listen to the rival chefs' conversation again without interruption."
OUTRO = (
    "Barinov scoffs at the suggestion that his staff would abandon Claude Monet, but unease begins to take root. "
    "In the next scene, Barinov discovers Max sleeping on the job during a frantic dinner rush."
)
CLOSING = ("chef", "Мои люди преданы мне до конца.")
