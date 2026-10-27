ID = "domashniy-arest-s01e06-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 31
TITLE = "Народный герой Иван Самсонов  (People's Hero Ivan Samsonov)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "mikhail": "anja", "samson": "angelina"}
LABELS = {"anya": "Нина", "mikhail": "Михаил Михайлович", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1129-1176. Arkady is absent, so Nina is `anya` (alisa, label Нина), Colonel Mikhail Mikhailovich is `mikhail` "
    "(anja, label Михаил Михайлович), and Samson is `samson` (angelina, label Самсон). The TV news report in cues "
    "1129-1134, Lavrov's excuses in 1139-1152, and Yulia's pout in 1166-1168 are narrated in the intro and walkthrough "
    "within the three-role limit. Slang 'угробили' (1142) -> 'погубили'; 'весь мозг проест' (1146) -> 'всю голову "
    "заморочит'; numbers '100' and '300' (1152-1153) written out as 'сто' and 'триста'; crude 'наплевать' (1168, 1170) "
    "-> 'всё равно'; ASR 'дядя Даня' (1172-1173) restored to 'дядя Аркадий'."
)

INTRO = (
    "At security-service headquarters and back in the Samsonovs' room at the communal flat. Last time, Arkady hurried "
    "his girlfriend Lyolya out the door to return to Marina, only for Marina to tell him that the moment had passed. "
    "Meanwhile, the evening television news praises people's hero Ivan Samsonov for rescuing a drowning boy from the "
    "river, and Colonel Mikhail Mikhailovich explodes at his agents. We'll hear it in Russian first; don't worry about "
    "catching every word."
)

STORY = [
 ("mikhail", "Ну что, вы довольны? Вы видели новости?",
  "Well, are you satisfied? Did you see the news?",
  [(1138, "Ну что, довольны")], "TV report 1129-1134 narrated in intro/walkthrough"),
 ("mikhail", "Вы и Самсонову рейтинг подняли!",
  "You both raised Samsonov's rating!",
  [(1141, "И Самсонову рейтинг подняли")], ""),
 ("mikhail", "И моего племянника в реке чуть не погубили!",
  "And you nearly killed my nephew in the river!",
  [(1142, "И моего племянника чуть не")], "'угробили' -> 'погубили'"),
 ("mikhail", "Мне его мать теперь всю голову заморочит!",
  "Now his mother will pester me to death!",
  [(1146, "Мне его мать теперь")], "slang 'весь мозг проест' -> 'всю голову заморочит'"),
 ("mikhail", "Вы его спиртом растёрли? И внутри тоже растёрли?!",
  "You rubbed him with alcohol? And on the inside too?!",
  [(1148, "его спиртом растерли"), (1150, "тоже растерли")], "'Изнутри' -> 'И внутри'"),
 ("mikhail", "Он к матери домой пьяный пришёл!",
  "He came home drunk to his mother!",
  [(1151, "Он к матери домой пьяный")], "'явился' -> 'пришёл'"),
 ("mikhail", "Это для тебя сто грамм мало!",
  "A hundred grams is a little for you!",
  [(1153, "Это для тебя")], "'100' -> 'сто'"),
 ("mikhail", "А для него это как триста!",
  "And for him it's like three hundred!",
  [(1153, "а для него как")], "'300' -> 'триста'"),
 ("mikhail", "Алло, Люся, привет! У Лёвы голова кружится?",
  "Hello, Lyusya, hi! Is Lyova's head spinning?",
  [(1154, "Люся, привет"), (1159, "Голова кружится")], ""),
 ("mikhail", "Пусть он одну ногу спустит на пол.",
  "Have him put one foot down on the floor.",
  [(1160, "пусть одну"), (1160, "на пол")], "'ножку спустят' -> 'ногу спустит'"),
 ("mikhail", "Не достаёт до пола? Подложи ему книгу под ногу!",
  "He can't reach the floor? Put a book under his foot!",
  [(1162, "Не достает до пола"), (1163, "подложи ему"), (1163, "под ногу")], "'что-нибудь' -> 'книгу'"),
 ("anya", "Юля, ну куда ты от нас уйдёшь?",
  "Yulia, where will you go away from us?",
  [(1166, "от вас"), (1167, "Ну, куда ты уйдешь")], ""),
 ("anya", "Ну как нам на тебя всё равно?",
  "How could we not care about you?",
  [(1170, "Ну как нам на тебя")], "crude 'наплевать' -> 'всё равно'"),
 ("anya", "Все прибежали тебя спасать — и я, и папа!",
  "Everyone came running to save you — both me and Dad!",
  [(1171, "Все прибежали тебя спасать, и я, и папа")], ""),
 ("anya", "И даже дядя Аркадий своим временем пожертвовал!",
  "And even Uncle Arkady sacrificed his own time!",
  [(1174, "Своим временем пожертвовал")], "garbled 'дядя Даня' (1172-1173) -> 'дядя Аркадий'"),
 ("samson", "Юля, ну иди сюда, не обижайся! Иди обниму!",
  "Yulia, come here, don't be upset! Come let me hug you!",
  [(1175, "ну иди сюда. Ну не обижайся"), (1176, "иди обниму")], "'Юль' -> 'Юля'"),
]

OPENER = "Let's take the scene line by line. Colonel Mikhail Mikhailovich glares at Lavrov and Zavarzin."

WALK = [
 (0, None,
  "'Well, are you satisfied? Did you see the news?' Instead of catching Samson in a scandal, their park operation "
  "turned him into a local hero on television."),
 (1, None,
  "'You both raised Samsonov's rating!' After 'raised the rating', Samsonov is in the dative case: 'to Samsonov'."),
 (2, None,
  "'And you nearly killed my nephew in the river!' Because short little Lieutenant Lyova was wearing Yulia's pink "
  "jacket on the bridge, Samson mistook him for a drowning schoolboy and dragged him out of the icy water."),
 (3, None,
  "'Now his mother will pester me to death!' Literally, 'will muddle my whole head'. Lavrov protests that they rubbed "
  "Lyova down with medical alcohol so he wouldn't catch a cold."),
 (4, None,
  "'You rubbed him with alcohol? And on the inside too?!' The noun 'alcohol' is in the instrumental case: 'with "
  "alcohol'."),
 (5, None,
  "'He came home drunk to his mother!' Lavrov mutters that they only gave him a 'frontline hundred grams' to warm up."),
 (6, None,
  "'A hundred grams is a little for you!' Notice the spoken genitive form after 'one hundred'."),
 (7, None,
  "'And for him it's like three hundred!' Just then the colonel's phone rings: it is his sister Lyusya, Lyova's mother."),
 (8, None,
  "'Hello, Lyusya, hi! Is Lyova's head spinning?' Poor Lyova is lying in bed with the room spinning around him."),
 (9, None,
  "'Have him put one foot down on the floor.' That old Russian folk remedy is called 'grounding' yourself when you "
  "have had too much to drink. But Lyusya reports a problem."),
 (10, "Подложи ему книгу под ногу!",
  "'He can't reach the floor? Put a book under his foot!' Because Lyova's legs are too short to reach the floor from "
  "the bed! Meanwhile, back at the communal flat, teenage Yulia is pouting that she will run away because nobody "
  "cares about her. Nina sits beside her."),
 (11, None,
  "'Yulia, where will you go away from us?' Nina speaks gently to her daughter."),
 (12, None,
  "'How could we not care about you?' Literally, 'how could it be all the same to us about you?'."),
 (13, None,
  "'Everyone came running to save you — both me and Dad!' When they thought she was going to jump off the bridge, "
  "the whole family raced to the park."),
 (14, None,
  "'And even Uncle Arkady sacrificed his own time!' After the verb 'sacrificed', 'his own time' takes the "
  "instrumental case. Then Samson opens his arms wide."),
 (15, None,
  "'Yulia, come here, don't be upset! Come let me hug you!' Literally, 'come, I will hug'. And the Samsonov family "
  "hugs tightly on the sofa."),
]

TRANSITION = "Now let's hear the whole scene once more, start to finish."

OUTRO = (
    "And that brings Episode Six to a close! While poor Lieutenant Lyova lies in bed unable to reach the floor with "
    "his short legs, Samson has accidentally become a television hero again, Ignatyev is funding his campaign, and "
    "Yulia is safely back in her parents' arms. See you in Episode Seven."
)
CLOSING = ("samson", "Юля, ну иди сюда, не обижайся! Иди обниму!")
