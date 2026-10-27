ID = "domashniy-arest-s01e04-scene-25"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 25
TITLE = "Ужин в ресторане  (Dinner at the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "waiter": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "waiter": "Официант", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1020-1052. Arkady is absent; Samson is the viewpoint character (anya, label Самсон). Transcription slips "
    "'на святых' (1020, for 'на семь тысяч'), 'А не кейв' (1023-1024, for 'Аникеев'), and 'Бен' (1047, for 'Вань') "
    "are corrected; menu items in cues 1031-1043 ('шампанское Розовый младший андон', 'башня из морепродуктов', "
    "'равиоли / маленькие пельмешки') and slang in 1048-1049 ('шипучка. Барбариска.') are simplified to A1."
)

INTRO = (
    "Across town that evening, outside an expensive Italian restaurant. Last time, Ilona locked herself in the "
    "bathroom and forwarded Klavdia's video of drunk Samson to Pasha's campaign team. Meanwhile, Samson and Nina are "
    "out in the luxury car from the dealership, and Samson spots the restaurant that invited him for a free dinner "
    "worth seven thousand roubles. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("anya", "Слушай, Нина, это же тот самый ресторан!",
  "Listen, Nina, this is that very restaurant!",
  [(1020, "Слушай"), (1020, "это же")], "'Нинка ... та самая Франческа' -> 'Нина ... тот самый ресторан'"),
 ("anya", "У нас там подарок на семь тысяч! Пошли сходим!",
  "We have a gift for seven thousand there! Come on, let's go!",
  [(1020, "у нас"), (1022, "пошли сходим")],
  "cue 1020 'депозит на святых' (garbled 'на семь тысяч') -> 'подарок на семь тысяч'"),
 ("nina", "Аникеев же запретил! Нам нельзя пить.",
  "But Anikeev forbade it! We mustn't drink.",
  [(1023, "запретил")], "cue 1023 'А не кейв' (garbled 'Аникеев') -> 'Аникеев же'; 'Нам нельзя пить.' added"),
 ("anya", "Ну ладно, брось! Мы только поедим.",
  "Oh come on, stop it! We'll only eat.",
  [(1024, "Ну ладно"), (1024, "брось")], "'Мы только поедим.' added"),
 ("waiter", "Добрый вечер! Мы очень рады видеть вас в нашем ресторане.",
  "Good evening! We are very glad to see you in our restaurant.",
  [(1028, "Добрый вечер"), (1029, "Мы рады"), (1029, "вас в нашем ресторане")], "'приветствовать' -> 'очень ... видеть'"),
 ("waiter", "Вот наше лучшее розовое шампанское.",
  "Here is our best pink champagne.",
  [(1031, "шампанское")], "cue 1031 simplified to A1"),
 ("anya", "Отлично! Давай розовое.",
  "Great! Give us the pink one.",
  [(1036, "отлично"), (1033, "Давай")], "'розовый' -> 'розовое'"),
 ("waiter", "У нас есть большая тарелка рыбы и крабов.",
  "We have a big platter of fish and crabs.",
  [(1035, "краб")], "cues 1034-1035 ('башня из морепродуктов...') simplified to A1"),
 ("waiter", "А потом итальянские пельмени. Все гости их очень любят.",
  "And then Italian dumplings. All the guests love them very much.",
  [(1037, "А")], "cues 1037-1040 (the waiter explaining ravioli as little dumplings) simplified to A1"),
 ("anya", "Пельмени мы будем, да, Нина? Неси всё!",
  "We'll have the dumplings, right, Nina? Bring everything!",
  [(1042, "будем, да, Нина"), (1044, "все")], "'Пельмеши' -> 'Пельмени мы'; 'Тащи' -> 'Неси'"),
 ("waiter", "Хорошо! Приятного вечера.",
  "Very well! Have a pleasant evening.",
  [(1046, "Приятного вечера")], "'Хорошо!' added"),
 ("nina", "Ваня, может, не надо шампанское?",
  "Vanya, maybe we shouldn't have champagne?",
  [(1047, "может, не надо")], "cue 1047 'Бен' (garbled 'Вань') -> 'Ваня'; 'шампанское' added"),
 ("anya", "Нина, это же просто сладкая вода!",
  "Nina, it's just sweet water!",
  [(1048, "Нина, это")], "cues 1048-1049 ('шипучка. Барбариска.') -> 'же просто сладкая вода!'"),
 ("anya", "Давай, за нашу новую жизнь! Очень вкусно!",
  "Come on, to our new life! Very tasty!",
  [(1050, "Давай, за нашу новую жизнь"), (1051, "Вкусно")], "'Очень' added"),
]

OPENER = (
    "Let's go through it line by line. Samson slows down in front of the restaurant lights and points through the "
    "window."
)

WALK = [
 (0, None,
  "'Listen, Nina, this is that very restaurant!' The two words before 'restaurant' mean 'that very, the exact same'."),
 (1, "У нас там подарок на семь тысяч!",
  "'We have a gift for seven thousand there!' Earlier, Yulia told them the restaurant had given candidate Samsonov a "
  "seven-thousand-rouble dinner voucher."),
 (1, "Пошли сходим!",
  "'Come on, let's go!' Russians often pair 'went' with 'we'll go and come back' as a lively way to say 'let's pop "
  "in'. Nina remembers Arkady's strict campaign rule."),
 (2, None,
  "'But Anikeev forbade it! We mustn't drink.' Literally, 'to us it is forbidden to drink'. Samson waves her worry "
  "aside."),
 (3, None,
  "'Oh come on, stop it! We'll only eat.' The command literally means 'throw it, drop it'. Inside, a polite waiter "
  "recognises the famous candidate at once."),
 (4, None,
  "'Good evening! We are very glad to see you in our restaurant.' The short plural adjective 'glad' is followed by "
  "the infinitive 'to see'."),
 (5, None,
  "'Here is our best pink champagne.' Because 'champagne' is a neuter noun in Russian, 'our', 'best', and 'pink' all "
  "take neuter endings."),
 (6, None,
  "'Great! Give us the pink one.' Samson uses the neuter adjective on its own to mean 'the pink one'."),
 (7, None,
  "'We have a big platter of fish and crabs.' After 'platter', both 'of fish' and 'of crabs' stand in the genitive "
  "case. Then the waiter suggests ravioli, and explains what they are."),
 (8, None,
  "'And then Italian dumplings. All the guests love them very much.' In the show, when Samson asks what ravioli are, "
  "the waiter explains that they are little dumplings, which immediately wins Samson over."),
 (9, None,
  "'We'll have the dumplings, right, Nina? Bring everything!' Using 'we will' directly with a food noun is the "
  "everyday Russian way to say 'we'll have the dumplings'."),
 (10, None,
  "'Very well! Have a pleasant evening.' This wish stands in the genitive case because 'I wish you' is understood. "
  "As the waiter pours the sparkling wine, Nina looks uneasy."),
 (11, None,
  "'Vanya, maybe we shouldn't have champagne?' Literally, 'maybe not needed champagne?' Samson laughs it off."),
 (12, None,
  "'Nina, it's just sweet water!' In the show he calls pink champagne fizzy candy-water, not real alcohol at all."),
 (13, None,
  "'Come on, to our new life! Very tasty!' A Russian toast always uses the preposition 'for' with the accusative "
  "case: 'for our new life!'"),
]

TRANSITION = "Now let's hear the whole restaurant scene once more, start to finish."

OUTRO = (
    "So while Arkady has no idea where his candidate is, Samson and Nina are clinking glasses of pink champagne — "
    "with the dealership's luxury car parked outside. See you next time."
)
CLOSING = ("anya", "За нашу новую жизнь!")
