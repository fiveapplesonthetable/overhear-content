ID = "kukhnya-s01e01-scene-06"
TITLE = "Проигрыш Спартака  (Spartak's Loss)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

INTRO = ("In this scene, Anya arrives at the kitchen of restaurant Claude Monet on a very tense morning. "
         "The cooks are whispering nervously because Chef Viktor Barinov is approaching in a terrible mood. "
         "Listen to the Russian dialogue first, and then we will review the phrases together in English.")

STORY = [
 ("anya", "Почему на кухне так тихо?", "Why is the kitchen so quiet?",
  [], "new line"),
 ("senya", "Шеф идёт. Опять злой.", "Chef is coming. Angry again.",
  [(60, "О, опять")], "О, опять adapted"),
 ("anya", "Что случилось? Опять футбол?", "What happened? Football again?",
  [(61, "Вчера Спартак")], "Вчера Спартак adapted"),
 ("senya", "Да, вчера играл Спартак.", "Yes, yesterday Spartak played.",
  [(61, "Вчера Спартак")], ""),
 ("anya", "И сколько он проиграл?", "And how much did he lose?",
  [(61, "Сколько")], ""),
 ("senya", "Сто штук.", "A hundred grand.",
  [(62, "Сто штук")], ""),
 ("anya", "Ничего себе! Сто тысяч рублей?", "Unbelievable! A hundred thousand rubles?",
  [(63, "Ничего себе")], ""),
 ("senya", "Да, ровно сто тысяч.", "Yes, exactly one hundred thousand.",
  [], "new line"),
 ("senya", "Они всегда проигрывают перед сменой.", "They always lose before his shift.",
  [(63, "всегда перед моей сменой")], "adapted from сменой-то проигрывают"),
 ("anya", "И что теперь делать?", "And what do we do now?",
  [], "new line"),
 ("senya", "Молчи и просто работай.", "Stay silent and just work.",
  [], "new line"),
 ("senya", "Не зли шефа сегодня.", "Do not anger the chef today.",
  [], "new line"),
 ("anya", "Понятно. Буду очень осторожной.", "Understood. I will be very careful.",
  [], "new line"),
 ("senya", "Вот и молодец. За работу!", "Good job. To work!",
  [], "new line"),
]

OPENER = "Let's break down this tense kitchen conversation sentence by sentence."

WALK = [
 (0, None,
  "'Why is the kitchen so quiet?' A question asking about the unusually tense atmosphere on the kitchen floor."),
 (1, "Шеф идёт.",
  "'Chef is coming.' A short subject and verb warning that the boss is approaching."),
 (1, "Опять злой.",
  "'Angry again.' The adverb for 'again' paired with the short adjective describing the chef's foul mood."),
 (2, "Что случилось?",
  "'What happened?' The standard past-tense question for finding out what went wrong."),
 (2, "Опять футбол?",
  "'Football again?' Anya guesses the reason behind the chef's predictable anger."),
 (3, None,
  "'Yes, yesterday Spartak played.' Confirming that Barinov's beloved football team was on the pitch last night."),
 (4, None,
  "'And how much did he lose?' Asking about the size of the chef's gambling bet."),
 (5, None,
  "'A hundred grand.' Slang for one hundred thousand rubles."),
 (6, "Ничего себе!",
  "'Unbelievable!' A very common Russian idiom expressing shock and astonishment."),
 (6, "Сто тысяч рублей?",
  "'A hundred thousand rubles?' Clarifying the enormous sum of money that was lost."),
 (7, None,
  "'Yes, exactly one hundred thousand.' The adverb emphasizes the precise and painful total."),
 (8, None,
  "'They always lose before his shift.' Senya complains about the terrible timing of the football club's losses."),
 (9, None,
  "'And what do we do now?' An essential phrase using the infinitive to ask what course of action to take."),
 (10, "Молчи и просто работай.",
  "'Stay silent and just work.' Two sharp imperatives advising head-down survival."),
 (11, None,
  "'Do not anger the chef today.' A negative imperative warning against provoking the temperamental head chef."),
 (12, "Понятно.",
  "'Understood.' A single word expressing comprehension and readiness."),
 (12, "Буду очень осторожной.",
  "'I will be very careful.' Using the future tense with the instrumental case for the adjective."),
 (13, "За работу!",
  "'To work!' A short and spirited call to action."),
]

TRANSITION = "Alright, let's hear the whole conversation once again."

OUTRO = ("That wraps up our sixth scene. In Kukhnya, Chef Barinov's football obsession and terrible temper "
         "are legendary, and the kitchen staff quickly learns when to stay out of his way. See you next time!")

CLOSING = ("anya", "До встречи!")
