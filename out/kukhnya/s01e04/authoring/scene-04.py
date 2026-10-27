ID = "kukhnya-s01e04-scene-04"
TITLE = "Сладкий сон  (A Sweet Dream)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = ("In this scene, Max falls asleep in the restaurant dining room and has an affectionate dream about Chef Viktor Barinov. "
         "Barinov violently wakes him up and demands to know why he is sleeping during working hours. "
         "Listen to their funny confrontation in Russian first, and then we will examine every line.")

STORY = [
 ("anya", "Ты молодец, Витька.", "Good job, Vitka.",
  [(30, "Ты молодец, Витька")], ""),
 ("anya", "Витюшенька, мой огузок.", "Vityushenka, my little runt.",
  [(31, "Витюшенька"), (31, "Мой Агузак")], "огузок adapted"),
 ("chef", "Ты что, совсем с ума сошёл?", "Have you completely lost your mind?",
  [(32, "Ты что, совсем")], "clean A1"),
 ("chef", "Ты что здесь спишь?", "Why are you sleeping here?",
  [(33, "Ты что здесь")], "clean A1"),
 ("anya", "Шеф, простите меня, пожалуйста.", "Chef, please forgive me.",
  [(33, "Шеф, я")], ""),
 ("anya", "Я прилёг на пять минут.", "I lay down for five minutes.",
  [(34, "прилег на пять минут заснуть")], "adapted"),
 ("chef", "На кухне спать нельзя!", "You cannot sleep in the kitchen!",
  [], "new line"),
 ("anya", "Я всю ночь не мог уснуть.", "I could not sleep all night.",
  [(35, "Всю ночь не мог")], ""),
 ("chef", "Почему ты ночью не спал?", "Why didn't you sleep at night?",
  [], "new line"),
 ("anya", "Наверное, это акклиматизация.", "Probably it is acclimatization.",
  [(35, "акклиматизация, наверное")], ""),
 ("chef", "Какая ещё акклиматизация?", "What acclimatization?",
  [], "new line"),
 ("anya", "Я ещё не привык к Москве.", "I am not used to Moscow yet.",
  [], "new line"),
 ("chef", "Быстро вставай и мой посуду!", "Quickly get up and wash dishes!",
  [], "new line"),
 ("anya", "Уже встаю, шеф.", "Already getting up, Chef.",
  [], "new line"),
]

OPENER = "Let's examine this hilarious wake-up call line by line."

WALK = [
 (0, None,
  "'Good job, Vitka.' Max talks to the chef in a tender dream."),
 (1, None,
  "'Vityushenka, my little runt.' Dreaming that he is the boss of Chef Barinov."),
 (2, None,
  "'Have you completely lost your mind?' Viktor Barinov roars in shock and anger."),
 (3, None,
  "'Why are you sleeping here?' Demanding an immediate explanation from the rookie."),
 (4, None,
  "'Chef, please forgive me.' Max wakes up in total fear."),
 (5, None,
  "'I lay down for five minutes.' Trying to downplay his unauthorized nap."),
 (6, None,
  "'You cannot sleep in the kitchen!' Laying down strict workplace rules."),
 (7, None,
  "'I could not sleep all night.' Explaining his severe exhaustion."),
 (8, None,
  "'Why didn't you sleep at night?' Barinov questions the young cook."),
 (9, None,
  "'Probably it is acclimatization.' Blaming his move to the capital."),
 (10, None,
  "'What acclimatization?' The chef dismisses the excuse completely."),
 (11, None,
  "'I am not used to Moscow yet.' Describing his difficult transition to city life."),
 (12, None,
  "'Quickly get up and wash dishes!' Barking orders to get him back to work."),
 (13, None,
  "'Already getting up, Chef.' Hurrying to obey before the chef gets angrier."),
]

TRANSITION = "Now let's listen to the whole dialogue one more time."

OUTRO = ("That concludes our fourth scene. In Kukhnya, calling your temperamental boss by an affectionate diminutive "
         "is definitely not the best way to keep your job. See you next time!")

CLOSING = ("anya", "До встречи!")
