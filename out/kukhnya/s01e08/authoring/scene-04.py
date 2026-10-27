ID = "kukhnya-s01e08-scene-04"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 4
TITLE = "Смелое пари  (A Bold Bet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Елена", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 32-42. Refusing to tolerate Barinov's dismissive remarks, Elena challenges him "
    "to a bet on live television: if she survives one full shift in his kitchen, he must buy her dinner."
)

INTRO = (
    "Pushed to her limit by Barinov's blatant condescension on live air, Elena Sokolova seizes the moment "
    "to turn the tables. She proposes a public wager before millions of viewers: she will work a full dinner shift "
    "in Barinov's kitchen at Claude Monet, and if she succeeds without quitting, he must take her out to dinner. "
    "Let's listen to their wager in Russian first."
)

STORY = [
    ("anya", "Виктор, вы ведёте себя очень грубо!",
     "Viktor, you are behaving very rudely!",
     [(32, "Вы какой-то женоненавистник")], "adapted"),
    ("chef", "Я прекрасно отношусь ко всем женщинам.",
     "I treat all women wonderfully.",
     [(33, "Я прекрасно отношусь к женщинам"), (34, "Я вообще люблю женщин")], "adapted"),
    ("anya", "Тогда почему вы так обижаете меня?",
     "Then why do you insult me like that?",
     [], "new"),
    ("chef", "Вы не сможете работать целый день.",
     "You will not be able to work a whole day.",
     [(37, "вы, например, на моей кухне и дня не продержались бы")], "adapted"),
    ("anya", "А давайте поспорим прямо сейчас!",
     "Then let us bet right now!",
     [(38, "А давайте заключим пари")], "adapted"),
    ("chef", "О чём вы хотите спорить со мной?",
     "What do you want to bet about with me?",
     [], "new"),
    ("anya", "Я отработаю полную смену на кухне.",
     "I will work a full shift in the kitchen.",
     [(39, "Вот если я продержусь на вашей кухне день")], "adapted"),
    ("chef", "Мои повара быстро сломают вашу гордость.",
     "My cooks will quickly break your pride.",
     [], "new"),
    ("anya", "Если я справлюсь, вы оплатите ужин!",
     "If I cope, you will pay for dinner!",
     [(39, "вы приглашайте меня на ужин")], "adapted"),
    ("chef", "А если вы сбежите через час?",
     "And if you run away after an hour?",
     [], "new"),
    ("anya", "Тогда вы выиграете наш главный спор.",
     "Then you will win our main bet.",
     [], "new"),
    ("chef", "Договорились, завтра жду вас на кухне!",
     "Agreed, tomorrow I expect you in the kitchen!",
     [(41, "Виктор, вы принимаете пари")], "adapted"),
    ("anya", "Все зрители будут свидетелями нашего спора.",
     "All viewers will be witnesses of our bet.",
     [(40, "Дорогие друзья, какой неожиданный поворот событий")], "adapted"),
]

OPENER = "Now let's examine Elena and Barinov's public wager line by line."

WALK = [
    (0, None,
     "'Viktor, you are behaving very rudely!' Elena confronts the chef's chauvinistic hostility on air."),
    (1, None,
     "'I treat all women wonderfully.' Barinov attempts to defend his public reputation with an adverbial phrase."),
    (2, None,
     "'Then why do you insult me like that?' Elena points out the contradiction in his disrespectful attitude."),
    (3, None,
     "'You will not be able to work a whole day.' Barinov insists on the crushing difficulty of his kitchen line."),
    (4, None,
     "'Then let us bet right now!' Elena boldly initiates the wager with an imperative proposal."),
    (5, None,
     "'What do you want to bet about with me?' Barinov inquires about the terms of the challenge."),
    (6, None,
     "'I will work a full shift in the kitchen.' Elena outlines the scope of her guest shift with a future verb."),
    (7, None,
     "'My cooks will quickly break your pride.' Barinov predicts that his tough crew will overwhelm her."),
    (8, None,
     "'If I cope, you will pay for dinner!' Elena states her condition for victory using a future perfective verb."),
    (9, None,
     "'And if you run away after an hour?' Barinov anticipates her swift retreat under pressure."),
    (10, None,
     "'Then you will win our main bet.' Elena accepts the penalty of conceding the dispute."),
    (11, None,
     "'Agreed, tomorrow I expect you in the kitchen!' Barinov commits to the wager with an energetic imperative agreement."),
    (12, None,
     "'All viewers will be witnesses of our bet.' Elena locks in the public challenge before the live audience."),
]

TRANSITION = "Now let's listen to the public wager again without interruption."
OUTRO = (
    "Cornered on live television, Chef Barinov accepts the wager, setting up an unforgettable showdown "
    "in the Claude Monet kitchen on tomorrow's dinner shift."
)
CLOSING = ("anya", "Все зрители будут свидетелями нашего спора.")
