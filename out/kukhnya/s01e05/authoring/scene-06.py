ID = "kukhnya-s01e05-scene-06"
TITLE = "Кулинарная битва  (A Culinary Battle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja", "fedya": "angelina"}
LABELS = {"anya": "Макс", "senya": "Сеня", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = ("In this scene, meat cook Senya organizes a kitchen betting pool as fish cook Fedya and rookie Max "
         "prepare for a head-to-head culinary duel. With cod as the secret ingredient, the entire kitchen wagers on the outcome. "
         "Listen to the lively conversation in Russian first, and then we will examine every line.")

STORY = [
 ("senya", "Итак, повара, делаем ставки и записываемся!", "So, cooks, place bets and sign up!",
  [(85, "Итак, ставим и записываемся")], ""),
 ("senya", "Сейчас Федя и Макс приготовят по блюду.", "Now Fedya and Max will prepare a dish each.",
  [(86, "Сейчас Федя"), (86, "будут готовить по одному блюду")], "Макс used, clean A1"),
 ("senya", "А шеф попробует и выберет победителя.", "And the chef will taste and choose the winner.",
  [(87, "А шеф попробует"), (87, "кто из них победил")], "выберет победителя adapted"),
 ("anya", "Какой главный продукт для нашего блюда?", "What is the main ingredient for our dish?",
  [(88, "Выбираем главный продукт для блюда")], "adapted into question"),
 ("senya", "Главный продукт сегодняшнего конкурса — треска!", "The main ingredient of today's contest is cod!",
  [(88, "главный продукт")], "треска added from srt context"),
 ("fedya", "Тебе конец, огузок!", "You are finished, runt!",
  [(89, "И конец")], "огузок added"),
 ("fedya", "Я готовил всю рыбу в океане!", "I have cooked all the fish in the ocean!",
  [(89, "Я готовил всю рыбу, которая плавает в океане")], "concise A1"),
 ("anya", "Рыбу я тоже умею готовить.", "I also know how to cook fish.",
  [], "new line"),
 ("fedya", "Посмотрим на твои жалкие умения.", "We will see your pathetic skills.",
  [], "new line"),
 ("senya", "Кто ставит пятьсот рублей на Федю?", "Who bets five hundred rubles on Fedya?",
  [(95, "пятьсот рублей"), (95, "для ставки")], "extended"),
 ("fedya", "Все повара на кухне ставят на меня.", "All the cooks in the kitchen bet on me.",
  [(90, "Спасибо")], "new line"),
 ("anya", "А я всё равно докажу свой талант!", "And I will prove my talent anyway!",
  [], "new line"),
 ("senya", "Время пошло, начинаем готовить прямо сейчас!", "Time has started, begin cooking right now!",
  [], "new line"),
 ("anya", "Я сделаю самый лучший соус.", "I will make the best sauce.",
  [], "new line"),
]

OPENER = "Let's examine this exciting kitchen showdown step by step."

WALK = [
 (0, None,
  "'So, cooks, place bets and sign up!' Senya acts as the bookmaker for the culinary battle."),
 (1, None,
  "'Now Fedya and Max will prepare a dish each.' Announcing the rules of the cooking contest."),
 (2, None,
  "'And the chef will taste and choose the winner.' Barinov will serve as the ultimate judge."),
 (3, None,
  "'What is the main ingredient for our dish?' Max asks about the mystery basket ingredient."),
 (4, None,
  "'The main ingredient of today's contest is cod!' Revealing the surplus fish they need to use up."),
 (5, None,
  "'You are finished, runt!' Fedya taunts his inexperienced opponent."),
 (6, None,
  "'I have cooked all the fish in the ocean!' Boasting about his vast seafood expertise."),
 (7, None,
  "'I also know how to cook fish.' Refusing to back down in front of the crew."),
 (8, None,
  "'We will see your pathetic skills.' Dismissing Max's confidence with a smirk."),
 (9, None,
  "'Who bets five hundred rubles on Fedya?' Collecting cash from the eager kitchen spectators."),
 (10, None,
  "'All the cooks in the kitchen bet on me.' Fedya revels in the universal support of his colleagues."),
 (11, None,
  "'And I will prove my talent anyway!' Max stays determined despite being the underdog."),
 (12, None,
  "'Time has started, begin cooking right now!' Senya starts the official competition timer."),
 (13, None,
  "'I will make the best sauce.' Max plans his winning culinary strategy."),
]

TRANSITION = "Now let's listen to the whole conversation once again."

OUTRO = ("That concludes our sixth scene. In Kukhnya, cooking contests between proud chefs "
         "are always filled with fierce banter and high stakes. See you next time!")

CLOSING = ("anya", "До встречи!")
