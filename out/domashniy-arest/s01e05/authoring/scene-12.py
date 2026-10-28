ID = "domashniy-arest-s01e05-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 12
TITLE = "Синяк от руля  (Bruise from the Steering Wheel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "golovkin": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "golovkin": "Головкин", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = ("Last time, General Kruglov mixed up Sineozersk with a poison case in the Urals before ordering Lavrov "
         "to continue Operation Golden Billion and bring the man from the archives to the next briefing. After "
         "Marina leaves Lavrov an urgent voice message asking for his help, Golovkin brings Samson and Nina out "
         "to his country house so Samson can recover away from Arkady. We'll hear it in Russian first; don't "
         "worry about catching every word.")

STORY = [
 ("anya", "Дань, я думал, у тебя дача. А у тебя прямо дом!",
  "Danya, I thought you had a cottage. And you have a real house!",
  [(433, "Дань, я думал у тебя дача"), (433, "а у тебя прям дом")],
  "'дача-дача ... прям дом' -> 'дача ... прямо дом'; Marina voicemail 430-432 bridged in INTRO"),
 ("golovkin", "Ну, Антон, скажешь тоже, дом.",
  "Come on, Anton, you call this a house.",
  [(434, "Ну, Антон"), (434, "дом")],
  "garbled 'ж уж дом' -> 'скажешь тоже, дом'; 435-438 omitted"),
 ("anya", "А ремонт сделал сам?",
  "And did you do the renovation yourself?",
  [(439, "А ремонт сделал сам")], ""),
 ("golovkin", "Что, стыки везде неровные?",
  "What, are the seams uneven everywhere?",
  [(441, "Что, стыки везде неровные")], ""),
 ("anya", "О, смотри, у тебя вон щели! Я же строитель, я разбираюсь.",
  "Oh, look, you have gaps over there! I'm a builder, I know my stuff.",
  [(444, "О, смотри, у тебя вон щели"), (445, "Я ж строитель, я разбираюсь")],
  "'у тебя слон сюда влезет' trimmed; 'ж' -> 'же'"),
 ("nina", "А мне, Дань, нравится. Молодец, очень уютно.",
  "Well I like it, Danya. Good job, it's very cosy.",
  [(446, "мне"), (446, "нравится. Молодец, очень уютно")],
  "toilet crude joke in 448-451 omitted"),
 ("anya", "Это что такое у меня?",
  "What is this I have here?",
  [(452, "Это что такое у меня")], ""),
 ("nina", "Синяк.",
  "A bruise.",
  [(453, "Синяк")], ""),
 ("anya", "Это от руля синяк! В какой машине? Ты машину разбил, что ли?",
  "That's a bruise from a steering wheel! In what car? Did you wreck the car or what?",
  [(455, "Это от руля синяк"), (459, "В какой машине? Ты еще"), (459, "разбил, что ли")],
  "slang 'быху/Бэху' -> 'машину'; 'дуру-то не включай' in 460 omitted"),
 ("golovkin", "Ты бандитов поймал! Которые банкомат на Гарибальди ограбили.",
  "You caught bandits! Who robbed the ATM on Garibaldi Street.",
  [(461, "Ты бандитов поймал"), (462, "которые банкомат на Гарибальде ограбили")], ""),
 ("anya", "Нин, что он говорит?",
  "Nina, what is he saying?",
  [(463, "чего он")],
  "slang 'Минты, чего он гонит-то?' -> 'Нин, что он говорит?'"),
 ("nina", "Да нет, он всё правильно говорит!",
  "No, he's telling it all right!",
  [(464, "Да нет, он все правильно говорит")], ""),
 ("golovkin", "Они прыгнули в машину и уехали.",
  "They jumped into a car and drove off.",
  [(470, "прыгнули в машину и уехали")],
  "'ментов вырубили' omitted"),
 ("golovkin", "Ты за ними поехал на машине. И сразу в лоб!",
  "You drove after them in the car. And rammed them head-on!",
  [(471, "Ты за ними поехал на"), (473, "И сразу в лоб")],
  "slang 'на Бэхе' -> 'на машине'"),
 ("golovkin", "Ты что, ничего не помнишь?",
  "Don't you remember anything at all?",
  [(476, "Ты что, не помнишь, что ли, ничего")], ""),
 ("anya", "Я так вспоминаю. Значит, машину разбил, что ли?",
  "I'm trying to recall it. So I wrecked the car, then?",
  [(477, "Я так вспоминаю"), (478, "А, значит"), (478, "разбил, что ли")],
  "slang 'Бэху-то' -> 'машину'"),
 ("golovkin", "А машина застрахована, не расстраивайся.",
  "And the car is insured, don't be upset.",
  [(479, "машина-то застрахована"), (480, "Не расстраивайся")], ""),
]

OPENER = ("Let's walk through it. Stepping inside Golovkin's wooden country house, Samson looks around with a "
          "builder's eye.")

WALK = [
 (0, "Дань, я думал, у тебя дача.",
  "'Danya, I thought you had a cottage.' 'Danya' is the short vocative form of Daniil."),
 (0, "А у тебя прямо дом!",
  "'And you have a real house!' Golovkin brushes off the praise modestly."),
 (1, None,
  "'Come on, Anton, you call this a house.' Then Samson inspects the woodwork more closely."),
 (2, None,
  "'And did you do the renovation yourself?' Golovkin immediately guesses what's coming."),
 (3, None,
  "'What, are the seams uneven everywhere?' Samson points right at the wall planks."),
 (4, "О, смотри, у тебя вон щели!",
  "'Oh, look, you have gaps over there!' the speaker puts 'oh' up front so the listener immediately catches the tone, followed by 'look'."),
 (4, "Я же строитель, я разбираюсь.",
  "'I'm a builder, I know my stuff.' That reflexive verb literally means 'I sort things out, I understand a "
  "subject well'. Nina steps in politely."),
 (5, "А мне, Дань, нравится.",
  "'Well I like it, Danya.' Notice the dative 'to me'."),
 (5, "Молодец, очень уютно.",
  "'Good job, it's very cosy.' Then Samson opens his shirt collar and looks down at his chest."),
 (6, None,
  "'What is this I have here?' Nina glances at the mark."),
 (7, None,
  "'A bruise.' Samson looks closer and recognizes the shape."),
 (8, "Это от руля синяк!",
  "'That's a bruise from a steering wheel!' After 'from', the noun 'steering wheel' is in the genitive case."),
 (8, "В какой машине? Ты машину разбил, что ли?",
  "'In what car? Did you wreck the car or what?' Remember, in Episode 4 Golovkin actually hit drunken Samson "
  "with his car! As Nina freezes, Golovkin invents a second heroic story on the spot."),
 (9, "Ты бандитов поймал!",
  "'You caught bandits!' Golovkin blurts out."),
 (9, "Которые банкомат на Гарибальди ограбили.",
  "'Who robbed the ATM on Garibaldi Street.' Remember the exploded ATM from Scene 1! Samson looks at Nina "
  "suspiciously."),
 (10, None,
  "'Nina, what is he saying?' Nina plays along with the lie."),
 (11, None,
  "'No, he's telling it all right!' Notice that 'yes no' at the start simply means an emphatic 'no!'. Encouraged, "
  "Golovkin elaborates."),
 (12, None,
  "'They jumped into a car and drove off.' And according to Golovkin, Samson gave chase."),
 (13, "Ты за ними поехал на машине.",
  "'You drove after them in the car.' In Russian, 'you' leads into 'car' in a very natural everyday phrasing."),
 (13, "И сразу в лоб!",
  "'And rammed them head-on!' Literally 'and right into the forehead!'. Golovkin acts amazed that Samson forgot."),
 (14, None,
  "'Don't you remember anything at all?' Flattered again, Samson pretends it's coming back to him."),
 (15, "Я так вспоминаю.",
  "'I'm trying to recall it.' You'll hear 'I' all the time in the show, here connected with 'am recalling'."),
 (15, "Значит, машину разбил, что ли?",
  "'So I wrecked the car, then?' Golovkin waves it away."),
 (16, None,
  "'And the car is insured, don't be upset.' Listen for the word meaning 'car' right alongside 'is insured' in this line."),
]

TRANSITION = "Now let's hear the whole conversation again from the beginning."

OUTRO = ("So when Samson spots a steering-wheel-shaped bruise on his chest from being hit by Golovkin's car, "
         "Golovkin connects it to the exploded ATM on Garibaldi Street and convinces Samson he rammed a gang of "
         "bank robbers head-on. Listen for 'I'm a builder, I know my stuff' and the emphatic 'yes no'; see you in "
         "the next scene.")
CLOSING = ("anya", "Я же строитель, я разбираюсь.")
