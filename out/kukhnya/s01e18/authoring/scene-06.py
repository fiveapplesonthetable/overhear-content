ID = "kukhnya-s01e18-scene-06"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 6
TITLE = "Хитрый план  (A Cunning Scheme)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Костя", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 134-139. At the bar, Max demonstrates a dishonest scheme to sell cheap cognac "
    "at exorbitant prices, but Kostya worries about breaking the law."
)

INTRO = (
    "Behind the bar counter at Claude Monet, Max reveals a dishonest scheme to swap alcohol "
    "and overcharge unsuspecting patrons for cheap drinks. Horrified by the illegal trick, "
    "Kostya warns Max about the consequences. Let us listen to their conversation in Russian first."
)

STORY = [
    ("max", "Вот, смотри, я покажу тебе хитрый способ.",
     "Here, look, I will show you a clever method.",
     [(134, "Я показал тебе еще один способ.")], "adapted"),
    ("anya", "Какой ещё способ ты хочешь показать?",
     "What other method do you want to show?",
     [], "new"),
    ("max", "Гости часто совсем не разбираются в алкоголе.",
     "Guests often do not understand alcohol at all.",
     [(135, "Гости не разбираются в том, что пьют.")], "adapted"),
    ("anya", "И что ты придумал сделать сейчас?",
     "And what did you come up with doing now?",
     [], "new"),
    ("max", "Мы продали дешёвый коньяк за тысячу рублей!",
     "We sold cheap cognac for a thousand rubles!",
     [(136, "И мы ему коньяк за 300 рублей продали за 1000.")], "adapted"),
    ("anya", "Ты с ума сошёл, это настоящий обман!",
     "Have you lost your mind, this is real deception!",
     [], "new"),
    ("max", "Зато мы быстро заработали лёгкие деньги.",
     "On the plus side, we quickly earned easy money.",
     [], "new"),
    ("anya", "Если нас поймают, нас сразу посадят!",
     "If they catch us, they will immediately jail us!",
     [(137, "Так если поймают, нас посадят.")], "adapted"),
    ("max", "Не бойся, никто никогда не узнает правду.",
     "Do not be afraid, no one will ever know the truth.",
     [(138, "Не посадят")], "adapted"),
    ("anya", "Закон строго против таких опасных дел.",
     "The law is strictly against such dangerous business.",
     [], "new"),
    ("max", "Ты умный парень, ты защитишь нас.",
     "You are a smart guy, you will protect us.",
     [(138, "ты же будущий юрист."), (139, "Отмажешь.")], "adapted"),
    ("anya", "Я не стану защищать такие опасные дела.",
     "I will not defend such dangerous schemes.",
     [], "new"),
    ("max", "Успокойся, давай просто спрячем эти деньги!",
     "Calm down, let us simply hide this money!",
     [], "new"),
]

OPENER = "Now let us examine Max and Kostya's debate over the scam line by line."

WALK = [
    (0, None,
     "'Here, look, I will show you a clever method.' -- Max offers to demonstrate a lucrative bar secret to his friend."),
    (1, None,
     "'What other method do you want to show?' -- Kostya asks with skepticism about what Max has planned."),
    (2, None,
     "'Guests often do not understand alcohol at all.' -- The cook claims that diners cannot distinguish cheap drinks."),
    (3, None,
     "'And what did you come up with doing now?' -- The bartender questions the morality of Max's proposal."),
    (4, None,
     "'We sold cheap cognac for a thousand rubles!' -- Max brags about the huge markup he successfully pulled off."),
    (5, None,
     "'Have you lost your mind, this is real deception!' -- Kostya expresses outrage at the blatant theft."),
    (6, None,
     "'On the plus side, we quickly earned easy money.' -- Max rationalizes the dishonest trick with quick profit."),
    (7, None,
     "'If they catch us, they will immediately jail us!' -- The terrified bartender fears severe criminal punishment."),
    (8, None,
     "'Do not be afraid, no one will ever know the truth.' -- Max dismisses the risk and urges his friend not to panic."),
    (9, None,
     "'The law is strictly against such dangerous business.' -- Kostya reminds him that breaking the rules brings ruin."),
    (10, None,
     "'You are a smart guy, you will protect us.' -- Max relies on Kostya's intelligence to keep them out of trouble."),
    (11, None,
     "'I will not defend such dangerous schemes.' -- Kostya firmly refuses to endorse any illegal wrongdoing."),
    (12, None,
     "'Calm down, let us simply hide this money!' -- Max ends the argument and stashes the extra cash away."),
]

TRANSITION = "Now let us listen to Max and Kostya once again."
OUTRO = (
    "Despite Kostya's strong moral protests, Max pockets the illicit profit, "
    "leaving Kostya nervous about potential consequences."
)
CLOSING = ("max", "Успокойся, давай просто спрячем эти деньги!")
