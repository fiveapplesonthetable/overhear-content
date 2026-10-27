ID = "kukhnya-s01e02-scene-04"
TITLE = "Где мой нож?  (Where Is My Knife?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = ("This scene is set in the kitchen of Claude Monet from the second episode. "
         "Chef Viktor Barinov discovers that his favorite knife has disappeared, "
         "and he halts all work until someone finds it. "
         "Listen to the Russian story first, and then we will review the phrases together.")

STORY = [
 ("chef", "А где мой нож?", "And where is my knife?",
  [(76, "где мой нож")], ""),
 ("chef", "Кто взял мой нож?", "Who took my knife?",
  [(80, "Кто взял мой нож")], ""),
 ("anya", "Шеф, я не брала.", "Chef, I didn't take it.",
  [], "new line"),
 ("chef", "Повторяю. Кто взял мой нож?", "I repeat: who took my knife?",
  [(81, "Повторяю"), (82, "Кто взял мой нож")], ""),
 ("anya", "Я не знаю, шеф.", "I don't know, chef.",
  [], "new line"),
 ("chef", "Никто отсюда домой не уйдёт.", "Nobody will go home from here.",
  [(87, "никто из вас отсюда домой не уйдет")], "из вас dropped for brevity"),
 ("chef", "Пока вы не найдёте нож.", "Until you find the knife.",
  [(87, "Пока вы мне не найдете нож")], "мне dropped"),
 ("anya", "Понятно, шеф.", "Understood, chef.",
  [(88, "Понятно")], ""),
 ("chef", "Я не буду ничего готовить.", "I will not cook anything.",
  [(89, "Не буду ничего готовить")], ""),
 ("chef", "Так, все ищем нож.", "Right, everyone, look for the knife.",
  [(90, "Так, все ищем нож")], ""),
 ("chef", "Живо!", "Quick!",
  [(91, "Живо")], ""),
 ("anya", "А что за проблема?", "What is the problem?",
  [(92, "А что за проблема")], ""),
 ("anya", "Мы такой же нож купим.", "We will buy the same knife.",
  [(92, "такой же нож купим")], "simplified for A1"),
 ("chef", "А ты знаешь, что это за нож?", "And do you know what kind of knife this is?",
  [(93, "А ты знаешь, что это за нож")], ""),
]

OPENER = "Let's examine the chef's furious search line by line."

WALK = [
 (0, None,
  "'And where is my knife?' The chef opens with a sharp question, using the question word for 'where' and the possessive for 'my'."),
 (1, None,
  "'Who took my knife?' He demands to know who took it, using the past-tense verb for 'took'."),
 (2, None,
  "'Chef, I didn't take it.' Anya answers at once. The feminine ending on the past verb shows the speaker is a woman."),
 (3, "Повторяю.",
  "'I repeat.' A single verb in the first person present showing that his patience is gone."),
 (3, "Кто взял мой нож?",
  "'Who took my knife?' Shouting the same question again to the whole kitchen floor."),
 (4, None,
  "'I don't know, chef.' A simple and honest negative response."),
 (5, None,
  "'Nobody will go home from here.' A sweeping threat using a double negative, literally 'nobody from here home will not go'."),
 (6, None,
  "'Until you find the knife.' Setting a clear condition for leaving work."),
 (7, None,
  "'Understood, chef.' A short acknowledgement of the order."),
 (8, None,
  "'I will not cook anything.' The chef goes on strike, refusing to prepare food without his favorite tool."),
 (9, None,
  "'Right, everyone, look for the knife.' The chef includes himself in the search with the first-person plural verb."),
 (10, None,
  "'Quick!' A one-word command urging everyone to move lively."),
 (11, None,
  "'What is the problem?' Anya asks casually, not yet grasping the gravity of the situation."),
 (12, None,
  "'We will buy the same knife.' Anya suggests a simple solution, offering to purchase a replacement."),
 (13, None,
  "'And do you know what kind of knife this is?' The chef responds with disbelief that she thinks his prized blade can simply be bought in a store."),
]

TRANSITION = "Alright, let's hear the whole conversation once again."

OUTRO = ("That concludes our fourth scene. When you watch the second episode of Kukhnya, "
         "listen for the chef shouting about his missing knife and declaring that nobody goes home until it is found. "
         "See you next time!")

CLOSING = ("anya", "До встречи!")
