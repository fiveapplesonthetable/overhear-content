"""Scene 36 — Jedis and Samsonov (s01e11, 01:07:57–01:09:16)."""

ID = "domashniy-arest-s01e11-scene-36"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 11
SCENE = 36
TITLE = "Джедаи и Самсонов  (Jedis and Samsonov)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.11"
SOURCE_FILE = "sources/domashniy-arest/s01/e11.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "samson": "anja",
    "yulia": "angelina",
}

LABELS = {
    "anya": "Нина",
    "samson": "Самсон",
    "yulia": "Юля",
}

INTRO = (
    "Ivan Samsonov returns to his communal apartment room after the street brawl, where his wife "
    "Nina and daughter Yulia attend to him while watching breaking news of his political campaign on television."
)

STORY = [
    ("samson", "Я сам дойду до дивана.",
     "I will reach the sofa myself.",
     [(1121, "Сам, сам, сам.")], "Samson walks in"),

    ("anya", "Считай, ты родился под счастливой звездой.",
     "Consider that you were born under a lucky star.",
     [(1122, "Ну что, считай,")], "Nina reflects on his luck"),

    ("samson", "Мне хватило на сегодня этих джедаев.",
     "I have had enough of these Jedis today.",
     [(1123, "Мне хватило на сегодня")], "Samson complains"),

    ("anya", "Юля, дай аптечку скорее!",
     "Yulia, bring the first aid kit quickly!",
     [(1124, "Юль, дай аптечку.")], "Nina calls Yulia"),

    ("yulia", "Сейчас, мама, я уже несу!",
     "Right away, Mom, I'm already bringing it!",
     [(1125, "Сейчас.")], "Yulia replies"),

    ("samson", "Не надо никакую аптечку нести.",
     "There is no need to bring any first aid kit.",
     [(1127, "Да не надо никакую аптечку,")], "Samson refuses treatment"),

    ("samson", "Меня уже обкололи сегодня врачи.",
     "The doctors already gave me injections today.",
     [(1127, "меня уже обкололи сегодня.")], "Samson explains"),

    ("yulia", "Мама, посмотри скорее на телевизор!",
     "Mom, look quickly at the TV!",
     [(1128, "Мама!")], "Yulia sees news"),

    ("yulia", "Там показывают народного кандидата Самсонова!",
     "They are showing people's candidate Samsonov there!",
     [(1129, "народный кандидат Иван Самсонов")], "TV report"),

    ("anya", "Все говорят, а Самсонов делает!",
     "Everyone talks, but Samsonov acts!",
     [(1130, "все говорят, а Самсонов делает.")], "Nina quotes slogan"),

    ("yulia", "А теперь перешли к другим новостям.",
     "And now they moved on to other news.",
     [(1131, "А теперь к другим новостям.")], "TV news shifts"),

    ("samson", "Президент отменил важную встречу?",
     "Did the president cancel the important meeting?",
     [(1132, "отменил встречу.")], "Samson notices political news"),

    ("anya", "Ну, теперь точно всё закончилось.",
     "Well, now everything has definitely ended.",
     [(1133, "Ну, теперь точно все.")], "Nina concludes"),

    ("samson", "Можешь перезвонить мне немного позже?",
     "Can you call me back a little later?",
     [(1134, "Можешь перезвонить?")], "Samson answers phone"),
]

OPENER = "Let's explore Samsonov's return to his apartment after the brawl."

WALK = [
    (0, None,
     "'I will reach the sofa myself.' Samson insists that he is able to walk on his own feet."),
    (1, None,
     "'Consider that you were born under a lucky star.' The Russian idiom describes surviving remarkable fortune."),
    (2, None,
     "'I have had enough of these Jedis today.' Samson complains about the bizarre martial artists."),
    (3, None,
     "'Yulia, bring the first aid kit quickly!' Nina urgently asks their daughter for medical supplies."),
    (4, None,
     "'Right away, Mom, I'm already bringing it!' Yulia hurries to help her injured father."),
    (5, None,
     "'There is no need to bring any first aid kit.' Samson stubbornly brushes off his wife's concern."),
    (6, None,
     "'The doctors already gave me injections today.' The colloquial verb refers to receiving medical shots."),
    (7, None,
     "'Mom, look quickly at the TV!' Yulia urgently alerts her mother to the breaking broadcast."),
    (8, None,
     "'They are showing people's candidate Samsonov there!' The television news reports on Ivan's eccentric campaign."),
    (9, None,
     "'Everyone talks, but Samsonov acts!' The campaign catchphrase contrasts mere empty words with decisive action."),
    (10, None,
     "'And now they moved on to other news.' The television announcer transitions to the next news story."),
    (11, None,
     "'Did the president cancel the important meeting?' Samson reacts to the sudden political announcement."),
    (12, None,
     "'Well, now everything has definitely ended.' Nina reflects that the dramatic day has finally drawn to a close."),
    (13, None,
     "'Can you call me back a little later?' Samson politely asks the caller to phone back later."),
]

TRANSITION = "Now let's listen to the scene between Samsonov, Nina, and Yulia once more."

OUTRO = "After a chaotic day of campaigning and fighting, the Samsonov family watches their own rise on television."

CLOSING = ("samson", "Можешь перезвонить мне немного позже?")
