ID = "domashniy-arest-s01e07-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 28
TITLE = "Лук, соль, перец  (Onion, Salt, Pepper)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "danya": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "danya": "Даня", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1074-1107 (with merged Scene 26 in cues 979-992 covered in the INTRO bridge). ASR 'до гистанцев на рынке' "
    "(1078, for 'у дагестанцев на рынке') is simplified to 'на рынке', crude 'Хрень, тебе туда какой-то напихали' (1081) "
    "is cleaned to 'тебе туда плохое мясо положили', and ASR 'Чей же с ущем вкуснее. Да, Ниноль?' (1087, for 'Чей шашлычок "
    "вкуснее? Да, Нинок?') is restored to 'чей шашлык вкуснее! Да, Нина?'. Yulya and Slavik's brief lines over the last "
    "piece (1090-1094) are narrated in WALK so Samson, Danya, and Nina hold the three voices."
)

INTRO = (
    "In the snowy forest clearing. Back in the communal flat, Arkady had just guilted a mortified Marina into helping "
    "him with his zipper using a rubber dishwashing glove, ending in a painful pinch. Out in the snowy woods, Slavik "
    "and polite lawyer Danya had just brought a limping Samsonov back up from the ravine after Danya rescued him; "
    "although Samsonov boasted he would have climbed out fine on his own, Slavik revealed that his dad had begged him "
    "to run for Uncle Danya before Danya invited everyone down to the grill he had already set up. Now both men are "
    "grilling skewers of shashlik over the coals. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
    ("anya", "Ну что, семья, ещё пять минут!",
     "Well, family, five more minutes!",
     [(1074, "Ну что, семья, пять минут")], ""),
    ("anya", "И папин шашлык скоро будет готов!",
     "And Dad's shashlik will soon be ready!",
     [(1075, "будет готов")], "'папкин шашлычок' -> 'папин шашлык' (A1)"),
    ("danya", "И мой тоже готов! А ты где мясо берёшь?",
     "And mine is ready too! Where do you get your meat?",
     [(1076, "тоже"), (1077, "А ты где мясо берешь")], ""),
    ("anya", "Я всегда на рынке беру. Они сами маринуют.",
     "I always get it at the market. They marinate it themselves.",
     [(1078, "на рынке"), (1079, "Они маринуют"), (1085, "Я всегда")], "ASR 'до гистанцев' omitted"),
    ("danya", "Понятно. Наверное, тебе туда плохое мясо положили.",
     "Got it. They probably put bad meat in there for you.",
     [(1080, "Понятно"), (1081, "тебе туда"), (1081, "наверное")], "'Хрень ... напихали' -> 'плохое мясо положили'"),
    ("anya", "Зато пахнет вкусно! Я всегда у них беру.",
     "Still, it smells delicious! I always buy from them.",
     [(1082, "пахнет вкусно"), (1085, "Я всегда у них беру")], ""),
    ("danya", "Конечно, вкусно! Это мой шашлык пахнет, ветер отсюда.",
     "Of course it's delicious! That's my shashlik smelling, the wind is from here.",
     [(1083, "конечно, вкусно"), (1084, "пахнет, ветер"), (1084, "отсюда")], ""),
    ("anya", "Ну, сейчас проверим, чей шашлык вкуснее! Да, Нина?",
     "Well, let's check right now whose shashlik is tastier! Right, Nina?",
     [(1086, "проверим"), (1087, "вкуснее")], "ASR 'Чей же с ущем вкуснее. Да, Ниноль?' restored"),
    ("nina", "Даня, дай мне последний кусочек! Очень вкусное мясо!",
     "Danya, give me the last little piece! Very tasty meat!",
     [(1090, "последний кусочек")], "adapted from cues 1090-1092"),
    ("danya", "Успокойтесь, я ещё сделаю! Куда ставить тарелку?",
     "Calm down, I'll make more! Where should I put the plate?",
     [(1095, "Успокойтесь"), (1097, "Куда ставить")], ""),
    ("anya", "А почему мой шашлык никто не ест? Мяса полно!",
     "And why is nobody eating my shashlik? There's plenty of meat!",
     [(1097, "Мяса полно")], "'рубайте' (1097) omitted for A1"),
    ("nina", "Да нет, Ваня, оно очень жёсткое.",
     "No, Vanya, it's very tough.",
     [(1098, "Да нет, оно жесткое")], ""),
    ("anya", "Как жёсткое? Вы же всегда его любили!",
     "What do you mean tough? You always loved it!",
     [(1099, "Вы всегда любили")], ""),
    ("nina", "Это потому, что другого не было! Ешь сам.",
     "That's because there was nothing else! Eat it yourself.",
     [(1100, "другого не было")], ""),
    ("anya", "Я сам всё съем! Даня, как ты готовишь мясо?",
     "I'll eat it all myself! Danya, how do you prepare the meat?",
     [(1103, "Я сам все съем")], "Samsonov asking Danya for his marinade recipe before cue 1107"),
    ("danya", "Попробуй! Лук, соль, перец — и всё.",
     "Try it! Onion, salt, pepper — and that's all.",
     [(1105, "попробуй"), (1107, "Лук, соль, перец"), (1107, "Все")], ""),
]

OPENER = (
    "Let's go through the scene line by line. Standing proudly over the smoky grill in the snow, Samsonov calls out "
    "to his family."
)

WALK = [
    (0, None,
     "'Well, family, five more minutes!' After the numeral 'five', the noun 'minutes' stands in the genitive plural."),
    (1, None,
     "'And Dad's shashlik will soon be ready!' The short masculine adjective 'ready' serves as the predicate."),
    (2, None,
     "'And mine is ready too! Where do you get your meat?' Lawyer Danya is grilling his own skewers right next to "
     "Samsonov."),
    (3, None,
     "'I always get it at the market. They marinate it themselves.' Samsonov brags about buying pre-marinated meat in "
     "a plastic bucket at the town market."),
    (4, None,
     "'Got it. They probably put bad meat in there for you.' Danya gently warns him that pre-marinated market buckets "
     "often hide tough scraps."),
    (5, None,
     "'Still, it smells delicious! I always buy from them.' The conjunction at the start means 'on the other hand, "
     "to make up for it'."),
    (6, None,
     "'Of course it's delicious! That's my shashlik smelling, the wind is from here.' Danya smiles and points out "
     "which way the breeze is blowing."),
    (7, None,
     "'Well, let's check right now whose shashlik is tastier! Right, Nina?' Notice the comparative adjective 'tastier'."),
    (8, None,
     "'Danya, give me the last little piece! Very tasty meat!' Minutes later, Nina, Yulya, and Slavik are fighting "
     "over the very last skewer from Danya's platter."),
    (9, None,
     "'Calm down, I'll make more! Where should I put the plate?' While Yulya and Slavik argue over who was first in "
     "line, Danya promises a second batch."),
    (10, None,
     "'And why is nobody eating my shashlik? There's plenty of meat!' The predicative word 'plenty' takes the genitive "
     "singular of mass nouns like 'meat'."),
    (11, None,
     "'No, Vanya, it's very tough.' Nina waves Samsonov's platter away with brutal honesty."),
    (12, None,
     "'What do you mean tough? You always loved it!' Samsonov is hurt and reminds them that they ate his barbecue "
     "every year before."),
    (13, "Это потому, что другого не было!",
     "'That's because there was nothing else!' With negative 'was not', 'other' stands in the genitive singular."),
    (13, "Ешь сам.",
     "'Eat it yourself.' Nina leaves the entire platter of tough skewers to Samsonov."),
    (14, None,
     "'I'll eat it all myself! Danya, how do you prepare the meat?' Chewing stubbornly on his own tough skewer, "
     "Samsonov finally caves and asks Danya for his secret."),
    (15, None,
     "'Try it! Onion, salt, pepper — and that's all.' Danya offers him a tender piece and shares his simple recipe."),
]

TRANSITION = "Now let's hear the whole scene again, from start to finish."

OUTRO = (
    "So everyone devoured Danya's tender shashlik seasoned with nothing but onion, salt, and pepper, leaving "
    "Samsonov even more desperate to outshine Danya after lunch. See you in the next scene."
)
CLOSING = ("danya", "Лук, соль, перец — и всё.")
