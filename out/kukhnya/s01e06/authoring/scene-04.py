ID = "kukhnya-s01e06-scene-04"
TITLE = "Баранина и трюфели  (Mutton and Truffles)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "timur": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "timur": "Тимур"}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"

INTRO = ("In this scene outside restaurant Claude Monet, Chef Viktor Barinov inspects meat from supplier Timur. "
         "After haggling over the quality of a lamb, Timur offers Barinov smuggled European truffles at a steep price. "
         "Listen to their funny bargaining dialogue in Russian first, and then we will examine every line.")

STORY = [
 ("chef", "Скажи честно, этот баран умер от старости?", "Tell me honestly, did this sheep die of old age?",
  [(7, "Скажи честно, Тимур, ведь этот баран умер от старости")], ""),
 ("timur", "Зачем обижаешь? Это молодой и вкусный ягнёнок!", "Why insult me? This is a young and tasty lamb!",
  [(8, "зачем обижаешь"), (9, "молодой и вкусный ягненок")], ""),
 ("chef", "У меня на кухне уже хватает баранов.", "I already have enough sheep in the kitchen.",
  [(12, "у меня такие бараны")], "clean A1"),
 ("timur", "Подожди, посмотри вот это отличное мясо!", "Wait, look at this excellent meat!",
  [(13, "подожди. Вот, посмотри вот этого"), (14, "на этом мясе")], ""),
 ("timur", "Клянусь, это самое лучшее свежее мясо!", "I swear, this is the best fresh meat!",
  [(14, "Клянусь"), (14, "на этом мясе")], ""),
 ("chef", "Да, этот ягнёнок действительно хороший.", "Yes, this lamb is really good.",
  [(15, "Да, это хороший")], ""),
 ("chef", "Хорошо, я беру это мясо.", "Fine, I will take this meat.",
  [(17, "Хорошо, беру")], ""),
 ("timur", "Шеф, дорогой, а трюфели тебе надо?", "Chef, my dear, do you need truffles?",
  [(18, "Шеф, брат, трюфеля надо")], ""),
 ("chef", "Ты опять предлагаешь мне контрабанду?", "Are you offering me contraband again?",
  [(20, "ты опять"), (21, "Контрабанду мне предлагаешь")], ""),
 ("chef", "Конечно надо! Почём ты их продаёшь?", "Of course I do! How much are you selling them for?",
  [(21, "Конечно, надо"), (22, "Почем")], ""),
 ("timur", "Тебе по-братски всего шестьсот евро за килограмм.", "For you as a friend, only six hundred euros per kilogram.",
  [(22, "Тебе по-братски всего"), (22, "600 евро за килограмм")], ""),
 ("chef", "Отлично, я беру эти трюфели!", "Great, I will take these truffles!",
  [(23, "беру, давай")], ""),
 ("timur", "Тогда цена выросла до семисот евро!", "Then the price has risen to seven hundred euros!",
  [(23, "Тогда 700")], ""),
 ("chef", "Тимур, не наглей и отдавай товар!", "Timur, don't get cheeky and hand over the goods!",
  [(24, "Тимур, не наглей")], ""),
]

OPENER = "Let's examine this humorous black-market negotiation step by step."

WALK = [
 (0, None,
  "'Tell me honestly, did this sheep die of old age?' Barinov questions the suspicious meat quality."),
 (1, "Зачем обижаешь?",
  "'Why insult me?' Timur takes theatrical offense at the accusation."),
 (1, "Это молодой и вкусный ягнёнок!",
  "'This is a young and tasty lamb!' Praising the tender meat enthusiastically."),
 (2, None,
  "'I already have enough sheep in the kitchen.' The chef jokes about his foolish cooks."),
 (3, None,
  "'Wait, look at this excellent meat!' Offering an alternative cut from the back of the van."),
 (4, None,
  "'I swear, this is the best fresh meat!' Vowing that the lamb is of the highest standard."),
 (5, None,
  "'Yes, this lamb is really good.' Barinov grudgingly acknowledges the genuine quality."),
 (6, None,
  "'Fine, I will take this meat.' Agreeing to purchase the lamb for the restaurant."),
 (7, None,
  "'Chef, my dear, do you need truffles?' The supplier pitches an exclusive underground luxury."),
 (8, None,
  "'Are you offering me contraband again?' Calling out the illicit origin of the delicacy."),
 (9, "Конечно надо!",
  "'Of course I do!' Barinov cannot resist premium French truffles."),
 (9, "Почём ты их продаёшь?",
  "'How much are you selling them for?' Inquiring about the price."),
 (10, None,
  "'For you as a friend, only six hundred euros per kilogram.' Quoting a supposedly friendly bargain rate."),
 (11, None,
  "'Great, I will take these truffles!' Agreeing to the lucrative deal without hesitation."),
 (12, None,
  "'Then the price has risen to seven hundred euros!' Timur audaciously hikes the price on the spot."),
 (13, None,
  "'Timur, don't get cheeky and hand over the goods!' Shutting down the greedy supplier with a firm command."),
]

TRANSITION = "Now let's listen to the whole conversation once again."

OUTRO = ("That concludes our fourth scene. In Kukhnya, sourcing gourmet culinary ingredients "
         "is often an adventure of its own behind the kitchen doors. See you next time!")

CLOSING = ("anya", "До встречи!")
