ID = "domashniy-arest-s01e07-scene-24"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 24
TITLE = "Главное — чтобы был рычаг  (The Main Thing Is a Lever)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "slavik": "angelina", "danya": "anja"}
LABELS = {"anya": "Самсон", "slavik": "Славик", "danya": "Даня"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = ("Cues 896-914. Arkady is absent -> anya = Самсон (alisa), slavik = Славик (angelina), danya = Даня (anja). "
               "ASR typos restored: 'аппетитно гуляем' (903) -> 'аппетит нагуляем', 'баранхит' (904) -> 'бронхит', "
               "'Дядь' (905) -> 'Даня', 'покрыши' (907) -> 'погреются', 'Что я требовал доказать' (909) -> 'Что и требовалось "
               "доказать', 'Ветхих обнял' (910) -> 'Ветка сухая', 'разберчик' (911) -> 'разведчик', 'щиплешь' (912) -> "
               "'щепки собираешь', 'ломанем' (913) -> 'сломаем'.")

INTRO = ("Deep in the snowy forest a few minutes later. Last time, back in the kitchen, Arkady apologized for being a burden "
         "and provoked Eduard into storming out, leaving Marina to realize Arkady could not hold a spoon with his casts. "
         "Now Samsonov is marching his son Slavik and Danya through knee-deep snow in search of firewood. We'll hear it "
         "in Russian first; don't worry about catching every word.")

STORY = [
 ("slavik", "Папа, слушай, ну нет дров.",
  "Dad, listen, there's no firewood.",
  [(896, "слушай, ну нет дров")], ""),
 ("slavik", "Пойдём обратно. Давно уже ходим.",
  "Let's head back. We've been walking for a long time.",
  [(897, "Пойдем обратно. Давно уже ходим")], ""),
 ("slavik", "Далеко же уже ушли.",
  "We've already gone so far.",
  [(898, "Далеко же уже ушли")], ""),
 ("anya", "Не вздумай, сынок. Всегда были. Сейчас найдём.",
  "Don't even think about it, son. There always was. We'll find some now.",
  [(899, "Не вздумай, сынок. Всегда были. Сейчас найдем")], ""),
 ("slavik", "Папа, да никогда не было!",
  "Dad, there never was!",
  [(900, "да никогда не было")], ""),
 ("slavik", "Всегда по три часа ходим.",
  "We always walk for three hours.",
  [(901, "Всегда по три часа ходим")], ""),
 ("danya", "Ничего страшного. Сейчас зато аппетит нагуляем.",
  "No big deal. At least we'll walk up an appetite now.",
  [(902, "ничего страшного"), (903, "Сейчас зато")],
  "ASR 'аппетитно гуляем' -> 'аппетит нагуляем'"),
 ("slavik", "И бронхит!",
  "And bronchitis!",
  [(904, "И")],
  "ASR 'баранхит' -> 'бронхит'"),
 ("anya", "Даня, а ты что, замёрз?",
  "Danya, are you cold or what?",
  [(905, "а ты что, замерз")],
  "ASR 'Дядь' -> 'Даня'"),
 ("danya", "А девчонкам что делать?",
  "And what are the girls supposed to do?",
  [(906, "девчонкам что")], ""),
 ("anya", "В машине погреются!",
  "They'll warm up in the car!",
  [(907, "В машине")],
  "ASR 'покрыши' -> 'погреются'"),
 ("anya", "Вот, что и требовалось доказать!",
  "There, which is what needed to be proved!",
  [(909, "доказать")],
  "ASR 'Что я требовал доказать' -> 'Что и требовалось доказать'"),
 ("anya", "Ветка сухая! Смотри, наш разведчик.",
  "The branch is dry! Look, our scout.",
  [(911, "Смотри, наш")],
  "ASR 'Ветхих обнял' -> 'Ветка сухая'; 'разберчик' -> 'разведчик'"),
 ("anya", "Да что ты щепки собираешь? Сейчас мы её сломаем!",
  "Why are you gathering splinters? We'll break it right now!",
  [(912, "Да что ты"), (913, "Сейчас мы ее")],
  "ASR 'щиплешь' -> 'щепки собираешь'; slang 'ломанем' -> 'сломаем'"),
 ("anya", "Главное, сынок, чтобы был рычаг!",
  "The main thing, son, is to have a lever!",
  [(914, "Главное"), (914, "чтобы был рычаг")],
  "colloquial 'сына' -> 'сынок'"),
]

OPENER = "Let's go through the scene line by line. First, trudging through the deep snow among bare birch trees, Slavik begs his father to turn back."

WALK = [
 (0, None,
  "'Dad, listen, there's no firewood.' After 'no', the word for firewood stands in the genitive plural."),
 (1, None,
  "'Let's head back. We've been walking for a long time.' Russian uses the present tense with 'already for a long time' for an action that started in the past and continues now."),
 (2, None,
  "'We've already gone so far.' Slavik points out how deep into the woods they have wandered."),
 (3, None,
  "'Don't even think about it, son. There always was. We'll find some now.' Samson refuses to admit that Danya's store-bought charcoal was a better idea."),
 (4, None,
  "'Dad, there never was!' Slavik is fed up with his father's stubborn optimism in the freezing cold."),
 (5, None,
  "'We always walk for three hours.' Slavik exposes how his dad's forest trips actually go every time."),
 (6, None,
  "'No big deal. At least we'll walk up an appetite now.' Cheerful Danya tries to be a good sport and keep the peace."),
 (7, None,
  "'And bronchitis!' Slavik adds a dark joke about freezing to death in the snow."),
 (8, None,
  "'Danya, are you cold or what?' Samson teases Danya for shivering in his stylish city coat."),
 (9, None,
  "'And what are the girls supposed to do?' Danya is worried about Nina and Klavdia Viktorovna waiting back by the cars."),
 (10, None,
  "'They'll warm up in the car!' Samson dismisses the women's comfort and keeps searching the trees."),
 (11, None,
  "'There, which is what needed to be proved!' Samson spots a dead tree overhanging a steep snowy ravine and uses the classic geometry phrase for 'Q.E.D.'"),
 (12, None,
  "'The branch is dry! Look, our scout.' He praises Danya as Danya starts breaking off small twigs."),
 (13, None,
  "'Why are you gathering splinters? We'll break it right now!' Samson pushes Danya aside and grabs the thick main branch with both hands."),
 (14, None,
  "'The main thing, son, is to have a lever!' He hangs his full weight on the branch—and it snaps, sending Samson tumbling headfirst down into the ravine."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = ("Next time, back in the communal kitchen, Eduard catches Marina spoon-feeding porridge to Arkady and loses his temper. "
         "Well done following that snowy forest trek in Russian. See you in the next scene.")
CLOSING = ("anya", "Главное — чтобы был рычаг!")
