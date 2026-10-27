ID = "domashniy-arest-s01e03-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 15
TITLE = "Одноклассники  (Old Classmates)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "golovkin": "anja", "samson": "angelina"}
LABELS = {"anya": "Нина", "golovkin": "Даня", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, Arkady tried to pressure Judge Berg over a flat he got for Berg's mother, and accidentally "
         "let slip in front of Golovkin that he handed out waiting-list flats through connections. As Golovkin "
         "leaves Arkady's room and walks down the communal corridor, he runs into Nina and Samson — and Nina "
         "recognises her old school classmate. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Данька Головкин, господи! Вань, это Данька Головкин, помнишь его?",
  "Danka Golovkin, goodness! Vanya, this is Danka Golovkin, do you remember him?",
  [(484, "Данька Головкин, господи"), (485, "Вань, это Данька Головкин, помнишь его")], ""),
 ("samson", "Конечно помню. Школьный друг твой.",
  "Of course I remember. Your school friend.",
  [(486, "Конечно помню")],
  "cue 486 'школьного твоего, Романова' (mistranscribed) -> 'Школьный друг твой'"),
 ("anya", "Вань, иди, я сейчас приду.",
  "Vanya, go on, I'll come right now.",
  [(487, "Вань, иди"), (487, "сейчас приду")],
  "'я' added"),
 ("anya", "Слушай, ну сто лет не виделись, да?",
  "Listen, we haven't seen each other in a hundred years, right?",
  [(488, "Слушай, ну сто лет не виделись, да")], ""),
 ("golovkin", "Девятнадцать лет.",
  "Nineteen years.",
  [(489, "Девятнадцать")],
  "'лет' added"),
 ("anya", "Да? Слушай, ты так изменился, расцвёл!",
  "Really? Listen, you've changed so much, you've blossomed!",
  [(490, "Да"), (491, "Слушай"), (491, "расцвел")],
  "cue 491 'ну ты прям такой стал' -> 'ты так изменился'"),
 ("golovkin", "А ты совсем не изменилась. Ты такая же красавица!",
  "And you haven't changed at all. You're just as beautiful!",
  [(492, "не изменилась"), (493, "Ты такая же красавица")],
  "cue 492 'тоже' -> 'совсем', statement"),
 ("anya", "Спасибо, спасибо! А ты заикаешься меньше.",
  "Thank you, thank you! And you stutter less.",
  [(495, "Спасибо, спасибо"), (496, "Заикаешься меньше")],
  "'А ты' added"),
 ("anya", "Извини, я не хотела обидеть. А ты что здесь делаешь?",
  "Sorry, I didn't mean to offend you. And what are you doing here?",
  [(497, "Извини, я не хотела"), (498, "А ты что здесь")],
  "cue 497 'больному' -> 'обидеть'; 'делаешь-то' -> 'делаешь'"),
 ("golovkin", "А я адвокат у этого соседа. У Аникеева.",
  "I'm the lawyer for that neighbour. For Anikeev.",
  [(499, "А я адвокат у этого")],
  "'соседа. У Аникеева' added to complete cue 499"),
 ("anya", "Ты адвокат? Здорово, молодец!",
  "You're a lawyer? That's great, well done!",
  [(500, "Адвокат"), (501, "Здорово")],
  "'Ты' and 'молодец' added"),
 ("samson", "Нина, ну ты идёшь? Я жду!",
  "Nina, well, are you coming? I'm waiting!",
  [],
  "cue 502 'Не, ну идешь я здесь' is a garbled transcription of Samson calling from the room"),
 ("anya", "Да, Вань, иду сейчас! Ну, Даня, пока.",
  "Yes, Vanya, I'm coming now! Well, Danya, bye.",
  [(503, "Да, Вань, иду сейчас"), (504, "пока"), (505, "Ну, Даня")], ""),
 ("golovkin", "Ну давай, пока, Нина.",
  "Well, take care, bye, Nina.",
  [(504, "Ну давай, пока")],
  "'Нина' added"),
]

OPENER = ("Let's go through their meeting in the corridor. Notice that Arkady isn't in this scene, so Nina is our "
          "main speaker.")

WALK = [
 (0, "Данька Головкин, господи!",
  "'Danka Golovkin, goodness!' 'Danka' is the familiar schoolyard form of Danila. She turns to her husband Samson, "
  "whose real name is Vanya."),
 (0, "Вань, это Данька Головкин, помнишь его?",
  "'Vanya, this is Danka Golovkin, do you remember him?' In spoken Russian, names ending in a vowel often lose "
  "that final vowel when you call someone: 'Vanya' becomes 'Van'. Samson grumbles."),
 (1, None,
  "'Of course I remember. Your school friend.' Samson looks at him with immediate suspicion, so Nina sends Samson "
  "on to their room."),
 (2, None,
  "'Vanya, go on, I'll come right now.' 'I will come' is the perfective future. Then she turns back to Danya."),
 (3, None,
  "'Listen, we haven't seen each other in a hundred years, right?' Just as in English, 'a hundred years' means "
  "'ages'. The verb has the reflexive ending, which here means 'each other'. Danya gives the exact number."),
 (4, None,
  "'Nineteen years.' Exact and lawyerly. Nina smiles."),
 (5, None,
  "'Really? Listen, you've changed so much, you've blossomed!' Both past-tense verbs are masculine, because she is "
  "speaking to a man. The second verb literally means 'came into bloom'. Danya returns the compliment."),
 (6, "А ты совсем не изменилась.",
  "'And you haven't changed at all.' Now the same verb has the feminine past ending before the reflexive suffix, "
  "because he is speaking to Nina."),
 (6, "Ты такая же красавица!",
  "'You're just as beautiful!' Literally 'such the same beauty'. Nina is delighted, and notices something else."),
 (7, None,
  "'Thank you, thank you! And you stutter less.' Then she realises that might sound tactless."),
 (8, "Извини, я не хотела обидеть.",
  "'Sorry, I didn't mean to offend you.' 'I didn't want' has the feminine past ending."),
 (8, "А ты что здесь делаешь?",
  "'And what are you doing here?' Danya points back towards Arkady's door."),
 (9, None,
  "'I'm the lawyer for that neighbour. For Anikeev.' The preposition 'by, at' with the genitive case is a natural "
  "way to say whose lawyer you are. Nina is impressed."),
 (10, None,
  "'You're a lawyer? That's great, well done!' That last word literally means 'fine fellow' and is used for 'good "
  "job!' or 'well done!'. From inside their room, Samson calls out impatiently."),
 (11, None,
  "'Nina, well, are you coming? I'm waiting!' So they say a quick goodbye."),
 (12, None,
  "'Yes, Vanya, I'm coming now! Well, Danya, bye.' And Danya replies warmly."),
 (13, None,
  "'Well, take care, bye, Nina.'"),
]

TRANSITION = "Now let's hear the whole corridor scene again from the top."

OUTRO = ("So Nina and Danila Golovkin are old classmates who haven't seen each other in nineteen years — and "
         "Samson is already jealous. Listen for the masculine and feminine past forms of 'changed'; see you next "
         "time.")
CLOSING = ("golovkin", "Ты такая же красавица!")
