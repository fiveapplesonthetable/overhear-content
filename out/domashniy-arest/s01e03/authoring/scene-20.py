ID = "domashniy-arest-s01e03-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 20
TITLE = "Прозвище на всю жизнь  (A Nickname for Life)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "slavik": "anja"}
LABELS = {"anya": "Аркадий", "slavik": "Славик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, Nina told jealous Samson to use his anger on Arkady and check the soldering iron. Meanwhile, in "
         "the communal kitchen, Arkady finds young Slavik sitting gloomily because his classmates gave him a humiliating "
         "nickname over Lyolya, and while the bored secret-service agents across the street munch dry bread rings at "
         "their post, Arkady talks the boy into stealing Judge Berg's little dog. Let's hear it in Russian first; "
         "don't worry about catching every word.")

STORY = [
 ("anya", "Чего ты такой грустный, боец?",
  "Why are you so sad, soldier?",
  [(651, "Чего"), (653, "боец")],
  "cue 651 'пригорюнился, кружок очумелый ручек' simplified to A1 'ты такой грустный'"),
 ("slavik", "Из-за вашей Лёли весь класс зовёт меня врунишкой!",
  "Because of your Lyolya the whole class calls me a little liar!",
  [(654, "из-за"), (654, "вашей Лёли"), (654, "меня весь класс")],
  "vulgar schoolyard nickname in cue 654 replaced with clean A1 'врунишкой'"),
 ("anya", "А Лёля здесь при чём?",
  "And what does Lyolya have to do with it?",
  [(655, "А Лёля здесь при чем")], ""),
 ("slavik", "Да при всём! У меня ничего не получается.",
  "Everything! Nothing is working out for me.",
  [(656, "Да при всем"), (665, "У меня не получается")], "'ничего' added"),
 ("anya", "Да это легко. Схватил собачку в парке и побежал.",
  "Come on, it's easy. Grab the little dog in the park and run.",
  [(666, "Да это легко. Схватил собачку и побежал")], "'в парке' added for clarity"),
 ("anya", "Толстая девочка тебя не догонит. А Лёля пойдёт с тобой на вечеринку.",
  "The chubby girl won't catch you. And Lyolya will go to the party with you.",
  [(667, "Толстая девочка тебя не догонит"), (668, "А Лёля пойдёт с тобой на вечеринку")], ""),
 ("slavik", "Я не буду красть собаку.",
  "I'm not going to steal a dog.",
  [(670, "Я не буду"), (670, "собаку")],
  "cue 670 misspells 'красть' as 'кресть'"),
 ("anya", "Послушай, мы её вернём. Это просто шутка.",
  "Listen, we'll give her back. It's just a prank.",
  [(671, "Послушай, мы её вернём")],
  "cue 672 'Это плёвое дело. Это розыгрыш.' simplified to 'Это просто шутка.'"),
 ("slavik", "Нет.",
  "No.",
  [(673, "Нет")], ""),
 ("anya", "Слушай, эти детские клички такие прилипчивые. Твой отец когда-то назвал меня очкариком.",
  "Listen, these childhood nicknames really stick. Your father once called me four-eyes.",
  [(675, "Слушай, эти детские клички"), (675, "такие прилипчивые"), (677, "твой отец")],
  "cue 677 'очконавт' -> 'очкарик'"),
 ("anya", "И вот так на всю жизнь — очкарик.",
  "And it stayed like that for my whole life: four-eyes.",
  [(678, "Вот так на всю жизнь")],
  "cue 678 'Очконавт' -> 'очкарик'"),
 ("anya", "Представь: тебе сорок лет, жена красавица, дети, бизнес. А тебя все зовут врунишкой!",
  "Imagine: you're forty, with a beautiful wife, children, a business. And everyone still calls you a little liar!",
  [(680, "жена красавица"), (681, "Дети, бизнес"), (682, "все зовут")],
  "cue 682 vulgar nickname replaced with 'врунишкой'"),
 ("anya", "Смотрите, врунишка новую машину купил! У врунишки сегодня день рождения!",
  "Look, the little liar bought a new car! It's the little liar's birthday today!",
  [(686, "новую"), (686, "купил"), (688, "смотрите"), (689, "сегодня день рождения")],
  "slang 'тачку' -> 'машину'; vulgar nickname -> 'врунишка'"),
 ("slavik", "Ладно, давайте ваш адрес.",
  "Alright, give me your address.",
  [(693, "Ладно, давайте ваш адрес")], ""),
 ("anya", "А вот это молодец.",
  "Now that's a good lad.",
  [(694, "А вот это молодец")], ""),
]

OPENER = ("Let's go back through the conversation. Arkady comes into the kitchen and sees ten-year-old Slavik staring "
          "miserably at the table.")

WALK = [
 (0, None,
  "'Why are you so sad, soldier?' In casual Russian, 'of what' is often used to mean 'why'. He calls the boy "
  "'fighter' or 'soldier' to sound matey. Slavik blames Arkady."),
 (1, None,
  "'Because of your Lyolya the whole class calls me a little liar!' Remember, Slavik showed off Lyolya's photo at "
  "school and claimed she was his girlfriend; in the show the boys give him a much cruder nickname, which we have "
  "cleaned up to 'little liar'. Notice the instrumental ending '-oy' after 'calls me'."),
 (2, None,
  "'And what does Lyolya have to do with it?' A very common idiom: 'at what here is Lyolya?'. Slavik is in despair."),
 (3, "Да при всём!",
  "'Everything!' Literally 'at everything!', echoing the idiom right back."),
 (3, "У меня ничего не получается.",
  "'Nothing is working out for me.' While they talk, the episode cuts briefly to the surveillance room, where Captain "
  "Zavarzin begs for pizza and Major Lavrov makes him eat dry bread rings instead. Back in the kitchen, Arkady has a "
  "plan for Slavik."),
 (4, "Да это легко.",
  "'Come on, it's easy.' Three simple words."),
 (4, "Схватил собачку в парке и побежал.",
  "'Grab the little dog in the park and run.' Russian often uses past-tense verbs like 'grabbed and ran' to describe "
  "how quick and easy a future action will be."),
 (5, "Толстая девочка тебя не догонит.",
  "'The chubby girl won't catch you.' That is Judge Berg's daughter Polina, who walks little Lyutik in the park."),
 (5, "А Лёля пойдёт с тобой на вечеринку.",
  "'And Lyolya will go to the party with you.' If Lyolya shows up at Dimon's party as Slavik's girlfriend, his "
  "classmates will have to take back their teasing. Still, Slavik hesitates."),
 (6, None,
  "'I'm not going to steal a dog.' Compound future with 'I will not' plus the infinitive 'to steal'. Arkady softens it."),
 (7, "Послушай, мы её вернём.",
  "'Listen, we'll give her back.' 'Her' refers to the dog, which is feminine in Russian."),
 (7, "Это просто шутка.",
  "'It's just a prank.' Literally 'this is simply a joke'."),
 (8, None,
  "'No.' Slavik stands firm, so Arkady switches tactics and aims at the boy's pride."),
 (9, "Слушай, эти детские клички такие прилипчивые.",
  "'Listen, these childhood nicknames really stick.' The adjective at the end means 'sticky' or 'catchy'."),
 (9, "Твой отец когда-то назвал меня очкариком.",
  "'Your father once called me four-eyes.' Notice the instrumental ending '-om' after 'called me'. In fact, it was "
  "Samson himself as a boy, though Arkady blames Samson's father here."),
 (10, None,
  "'And it stayed like that for my whole life: four-eyes.' Literally 'and so onto the whole life'. Then he paints "
  "Slavik's future."),
 (11, "Представь: тебе сорок лет, жена красавица, дети, бизнес.",
  "'Imagine: you're forty, with a beautiful wife, children, a business.' Age in Russian uses the 'to' case: 'to you "
  "forty years'."),
 (11, "А тебя все зовут врунишкой!",
  "'And everyone still calls you a little liar!' Even when you are a grown-up businessman driving a Porsche, the "
  "schoolyard name follows you around."),
 (12, "Смотрите, врунишка новую машину купил!",
  "'Look, the little liar bought a new car!' Both 'new' and 'car' take the feminine accusative ending '-u'."),
 (12, "У врунишки сегодня день рождения!",
  "'It's the little liar's birthday today!' Literally 'by the little liar today is birthday'. That picture is too much "
  "for Slavik."),
 (13, None,
  "'Alright, give me your address.' He uses the polite plural command 'give' and 'your' because he is talking to an "
  "adult. Arkady beams."),
 (14, None,
  "'Now that's a good lad.' Literally 'and here this is a fine fellow'."),
]

TRANSITION = "Let's listen to the whole kitchen scene again from the beginning."

OUTRO = ("So Arkady scares poor Slavik with the thought of carrying a schoolyard nickname to his fortieth birthday, "
         "and sends him off to steal Judge Berg's dog. Listen for the nickname and the bargain when you watch; see you "
         "next time.")
CLOSING = ("anya", "Лёля точно придёт!")
