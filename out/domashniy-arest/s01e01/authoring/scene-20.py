ID = "domashniy-arest-s01e01-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 20
TITLE = "Белый Кайен  (A White Cayenne)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "angelina", "samson": "anja"}
LABELS = {"anya": "Аркадий", "vika": "Вика", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"

INTRO = ("Still in the communal flat. Last time, the Samsonovs wrote their wish list, a flat, a car, a spa and a "
         "university place, and Arkady promised it all, just as his deputy turned up at the door. "
         "Now his wife Vika and his deputy Pasha come in with his things, and Arkady wants to show the family "
         "he means business. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Вика, Паша! Как я рад. Проходите, пожалуйста.", "Vika, Pasha! I'm so glad. Come in, please.",
  [(778, "Вика, Паша"), (778, "Как я рад"), (778, "Проходите, пожалуйста")], ""),
 ("vika", "Я тебе вещи привезла.", "I've brought you your things.",
  [(779, "вещи привезла")], "'тут' dropped"),
 ("anya", "Очень хорошо. Ну что, давайте знакомиться.", "Very good. Well then, let's introduce everyone.",
  [(780, "очень хорошо"), (781, "Ну что, давайте знакомиться")], ""),
 ("anya", "Это Паша, мой заместитель. Это Ваня, друг моего детства.",
  "This is Pasha, my deputy. This is Vanya, my childhood friend.",
  [(782, "Это Паша, мой заместитель"), (783, "Это Ваня, друг моего детства")], ""),
 ("anya", "А это моя жена Виктория.", "And this is my wife, Victoria.",
  [(785, "А это моя"), (785, "Виктория")], "'супруга' -> the everyday 'жена'"),
 ("vika", "Аркаша, что с пальцем?", "Arkasha, what's happened to your finger?",
  [(786, "Аркаша, что с пальцем")], ""),
 ("anya", "Ничего страшного. Теперь мы одна команда.", "Nothing serious. Now we're one team.",
  [(787, "Ничего страшного"), (790, "теперь мы одна команда")], ""),
 ("anya", "Вика, ты на какой машине сегодня приехала?", "Vika, which car did you come in today?",
  [(791, "Вика, ты на какой машине сегодня приехала")], ""),
 ("vika", "На Кайене.", "The Cayenne.",
  [], "cue 792 is mistranscribed ('На колене'); the English and the next line show it is the Cayenne"),
 ("anya", "На белом? Давай сюда ключи.", "The white one? Give me the keys.",
  [(793, "На белом"), (793, "давай сюда ключи")], ""),
 ("anya", "Ваня, это теперь твоё. И это только начало.", "Vanya, this is yours now. And it's only the beginning.",
  [(796, "Ваня, это теперь твое"), (796, "и это только начало")], ""),
 ("vika", "В смысле?", "What do you mean?",
  [(798, "В смысле")], ""),
 ("anya", "Я потом всё объясню.", "I'll explain everything later.",
  [(799, "Я потом все объясню")], ""),
 ("samson", "Это теперь наша машина?", "So this is our car now?",
  [], "stands in for the children's question in 800 ('Пап, у нас что, теперь Каен есть?')"),
 ("anya", "Да. Спускайтесь вниз, она там стоит.", "Yes. Go downstairs, it's parked there.",
  [(804, "Спускайтесь вниз"), (804, "там стоит")], "'он' (the Cayenne) -> 'она' (the car, after Samson's 'машина'); 'на улицу' dropped"),
 ("samson", "Нина, дети, пойдём посмотрим!", "Nina, kids, let's go and have a look!",
  [(806, "Пойдем")], "806 slang 'заценим аппарат' -> 'посмотрим'; 'Нина, дети' added"),
 ("anya", "Да, сходите. Не перепутайте!", "Yes, go on. Don't mix it up with another one!",
  [(807, "Да, сходите"), (812, "Не перепутайте")], "the joke about the many Cayennes in the yard (810-811) left to the narrator"),
]

OPENER = "Let's go back through it. Arkady greets his visitors like a host at a party, even in this shabby corridor."

WALK = [
 (0, "Вика, Паша!",
  "He greets them by name: Vika, his wife, and Pasha, his deputy."),
 (0, "Как я рад.",
  "'I'm so glad.' The word for 'glad' is in the masculine form, because Arkady is a man. A woman would add an 'a' at the end."),
 (0, "Проходите, пожалуйста.",
  "'Come in, please.' A polite command, and the ending is plural, because there are two guests. Vika has brought something."),
 (1, None,
  "'I've brought you your things.' The verb ends in 'la', because Vika is a woman. A man would leave off the 'a'. Arkady is pleased, and starts the introductions."),
 (2, None,
  "'Very good. Well then, let's introduce everyone.' Literally 'let's get acquainted'. You'll hear it whenever strangers meet."),
 (3, "Это Паша, мой заместитель.",
  "'This is Pasha, my deputy.' The pattern is simple: 'this', the name, then who the person is. No word for 'is' is needed."),
 (3, "Это Ваня, друг моего детства.",
  "'This is Vanya, my childhood friend.' Literally 'friend of my childhood'. That's a generous way to describe the man who broke his finger earlier today. Then Nina and the children are introduced, and finally his wife."),
 (4, None,
  "'And this is my wife, Victoria.' Victoria is the full form of her name, a little more formal. Vika notices something."),
 (5, None,
  "'Arkasha, what's happened to your finger?' Literally 'what with the finger?' She uses the affectionate form of his name. He plays it down."),
 (6, None,
  "'Nothing serious. Now we're one team.' The first phrase means 'nothing terrible', the normal way to say it's no big deal. And then his big idea, team spirit."),
 (7, None,
  "'Vika, which car did you come in today?' In Russian you arrive 'on' a car, so the word for 'on' comes first. Vika answers in the same way."),
 (8, None,
  "'The Cayenne.' That's her white Porsche, a very expensive car. The name is masculine in Russian."),
 (9, None,
  "'The white one? Give me the keys.' 'White' is masculine, to match the car's name. And the second sentence is a blunt way of saying 'hand them over'. Arkady turns to Samson."),
 (10, None,
  "'Vanya, this is yours now. And it's only the beginning.' The word for 'yours' here is the casual one, for a friend. Vika is speechless."),
 (11, None,
  "'What do you mean?' Literally 'in what sense?' A very common way to show you don't understand, or don't like what you hear."),
 (12, None,
  "'I'll explain everything later.' The verb is a completed action, so it points to the future. In the show, he keeps saying 'later' to her. Samson can't believe his luck."),
 (13, None,
  "'So this is our car now?' The word for 'our' is feminine, to match the car. In the show it's the children who ask, and Arkady answers them."),
 (14, None,
  "'Yes. Go downstairs, it's parked there.' Literally 'she stands there', because the car is feminine. In Russian, a parked car stands. Samson gathers the family."),
 (15, None,
  "'Nina, kids, let's go and have a look!' Two verbs side by side: 'let's go', and 'we'll look'. The family runs down the stairs."),
 (16, None,
  "'Yes, go on. Don't mix it up with another one!' It's a joke: in the show he adds that there are lots of Cayennes in their yard, which there certainly are not."),
]

TRANSITION = "And now the whole scene one more time."

OUTRO = ("Arkady has just given away his wife's car, and she is not happy about it at all. "
         "You did well with this one; see you next time.")
CLOSING = ("samson", "Пошли смотреть!")
