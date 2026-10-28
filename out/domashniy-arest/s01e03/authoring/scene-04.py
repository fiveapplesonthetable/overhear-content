ID = "domashniy-arest-s01e03-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = "Квартира с балконом  (A Flat with a Balcony)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "pasha": "Паша", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Cues 150-197. Arkady is absent; Samson is the viewpoint character (anya, label Самсон). "
               "Technical renovation terms (155, 161-163, 165) and the crude verb in cue 185 ('хреначишь') "
               "are simplified to A1.")

INTRO = ("Across town in a brand-new building, a few minutes later. Last time, Major Lavrov and Captain Zavarzin "
         "decided to plant a listening bug in Arkady's room. "
         "Meanwhile Pasha, the acting mayor, has brought Samson and Nina to a bright, newly renovated three-room "
         "flat to show them what they will get if they make Arkady tell where his money is hidden. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("pasha", "Проходите, пожалуйста! Как видите, большой коридор, а там кухня.",
  "Come on in, please! As you can see, a big hall, and the kitchen is over there.",
  [(154, "проходите"), (156, "Как видите"), (156, "коридор"), (157, "Там кухня")],
  "'просторный' -> 'большой'"),
 ("pasha", "Всё уже работает. А какой тут балкон!",
  "Everything works already. And look what a balcony there is here!",
  [(160, "Все уже"), (164, "балкон")],
  "cues 160-165 simplified"),
 ("pasha", "Можно сразу заезжать и жить. С мебелью мы тоже поможем.",
  "You can move right in and live here. We'll help with the furniture too.",
  [(168, "можно заезжать и жить"), (169, "с мебелью тоже поможем")], ""),
 ("pasha", "Ордер выписан на Самсонова Ивана Васильевича. Ну, что скажете, друзья?",
  "The occupancy order is made out to Samsonov Ivan Vasilyevich. Well, what do you say, my friends?",
  [(170, "Ордер выписан на Самсонова Ивана Васильевича"), (171, "Ну, что скажете, друзья")], ""),
 ("nina", "Ну, мы согласны!",
  "Well, we agree!",
  [(172, "Ну, мы согласны")], ""),
 ("anya", "Что согласны? Нет! Вы предлагаете человека пытать за эту квартиру?",
  "What do you mean, we agree? No! Are you asking me to torture a man for this flat?",
  [(174, "Что согласны? Нет"), (176, "человека пытать за эту квартиру")],
  "'Надо предлагать' -> 'Вы предлагаете'"),
 ("nina", "Он согласен, согласен!",
  "He agrees, he agrees!",
  [(175, "Согласны")], "adapted from cues 175/177"),
 ("pasha", "Зачем так грубо, Иван? Надо просто добыть информацию.",
  "Why put it so roughly, Ivan? You just need to get the information.",
  [(178, "зачем так грубо"), (178, "Иван"), (180, "Просто добыть информацию")], ""),
 ("anya", "Да? А как? Он же просто так не скажет!",
  "Yeah? And how? He won't tell me just like that!",
  [(181, "Да? А как"), (182, "не скажу")], "'не скажу' adapted to 3rd person 'не скажет'"),
 ("anya", "Всё, пошли отсюда, Нина.",
  "That's it, let's get out of here, Nina.",
  [(187, "Все, пошли отсюда")], "'Нина' added"),
 ("nina", "Подожди, Ваня! Он сделает всё.",
  "Wait, Vanya! He'll do everything.",
  [(188, "Подожди"), (190, "Он сделает все")], "'Ваня' from cue 184"),
 ("pasha", "Ну ладно, вы тут между собой договоритесь.",
  "All right, you two sort it out between yourselves here.",
  [(192, "Ну ладно, вы между собой тут")], "'разберитесь пока там' -> 'договоритесь' (from 193)"),
 ("anya", "Я никого пытать не буду, ясно? У меня дед три года партизанил!",
  "I'm not going to torture anyone, got it? My grandfather was a partisan for three years!",
  [(194, "Я никого пытать не буду, ясно"), (195, "У меня"), (195, "дед три года партизанил")], ""),
 ("nina", "Кто тебя заставляет пытать, Самсон? Мы так его припугнём, и всё.",
  "Who is making you torture anyone, Samson? We'll just give him a scare, that's all.",
  [(196, "Самсон? Кто тебя заставляет пытать"), (197, "Мы так его припугнем, и все")], ""),
 ("nina", "Он же слабый, сразу всё расскажет!",
  "He's weak, after all—he'll tell us everything straight away!",
  [(197, "Он же"), (197, "сразу")], "'хлипкий, сразу расклеивается' -> 'слабый, сразу всё расскажет'"),
]

OPENER = ("Let's go back through the scene. Pasha opens the door of a bright, empty flat and waves Samson "
          "and Nina inside.")

WALK = [
 (0, None,
  "'Come on in, please! As you can see, a big hall, and the kitchen is over there.' After thirty years in a "
  "crowded communal flat, a private hallway and kitchen of their own sound like a dream."),
 (1, None,
  "'Everything works already. And look what a balcony there is here!' Literally 'what a balcony here'."),
 (2, None,
  "'You can move right in and live here. We'll help with the furniture too.' After 'with', the noun for "
  "'furniture' takes the instrumental ending. Then Pasha pulls out the official housing document."),
 (3, "Ордер выписан на Самсонова Ивана Васильевича.",
  "'The occupancy order is made out to Samsonov Ivan Vasilyevich.' Official Russian documents always put the "
  "surname first, then the first name and father's name."),
 (3, "Ну, что скажете, друзья?",
  "'Well, what do you say, my friends?' Literally 'what will you say'. Nina doesn't hesitate for a second."),
 (4, None,
  "'Well, we agree!' The word for 'agree' is a short adjective, here in the plural form for 'we'. Samson is "
  "horrified."),
 (5, "Что согласны? Нет!",
  "'What do you mean, we agree? No!' The first content word means 'what do you mean', and 'agree' rounds out the thought."),
 (5, "Вы предлагаете человека пытать за эту квартиру?",
  "'Are you asking me to torture a man for this flat?' Literally 'you offer to torture a person for this flat?'. "
  "Nina tries to speak for him."),
 (6, None,
  "'He agrees, he agrees!' Notice how the ending changes: for 'we' it ended in '-y', and for 'he' it is the "
  "masculine singular form. Pasha puts on a hurt expression."),
 (7, None,
  "'Why put it so roughly, Ivan? You just need to get the information.' Literally 'why so coarsely'. Samson "
  "is not fooled."),
 (8, None,
  "'Yeah? And how? He won't tell me just like that!' And he heads for the door."),
 (9, None,
  "'That's it, let's get out of here, Nina.' Literally 'went from here', a casual way to say 'let's go'. Nina "
  "grabs his arm."),
 (10, None,
  "'Wait, Vanya! He'll do everything.' Pasha prudently steps out to let husband and wife argue in private."),
 (11, None,
  "'All right, you two sort it out between yourselves here.' Literally 'come to an agreement between yourselves'. "
  "As soon as Pasha is gone, Samson puts his foot down."),
 (12, "Я никого пытать не буду, ясно?",
  "'I'm not going to torture anyone, got it?' Russian uses a double negative here: literally 'I nobody to "
  "torture will not'."),
 (12, "У меня дед три года партизанил!",
  "'My grandfather was a partisan for three years!' Meaning his grandfather fought the occupiers in the war, "
  "so Samson refuses to act like a torturer. Nina rolls her eyes."),
 (13, "Кто тебя заставляет пытать, Самсон?",
  "'Who is making you torture anyone, Samson?' Nina uses the casual singular 'you' with 'who', as close colleagues and friends do."),
 (13, "Мы так его припугнём, и всё.",
  "'We'll just give him a scare, that's all.' The verb has a little prefix that means 'a bit': just scare him "
  "a little."),
 (14, None,
  "'He's weak, after all—he'll tell us everything straight away!' And with that, Nina talks Samson into trying."),
]

TRANSITION = "Now let's hear the whole scene in the new flat again from the start."

OUTRO = ("So Nina is determined to keep that three-room flat with a balcony, and Samson reluctantly agrees to "
         "give Arkady a scare. Next we'll see Marina get her instructions from the agents; see you next time.")
CLOSING = ("nina", "Мы согласны!")
