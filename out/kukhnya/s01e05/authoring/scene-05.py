ID = "kukhnya-s01e05-scene-05"
TITLE = "Кулинарный спор  (A Culinary Bet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "fedya": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "fedya": "Федя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = ("In this scene, Max arrives late to the kitchen and gets scolded by Chef Viktor Barinov. "
         "To make matters worse, veteran fish cook Fedya insults Max's cooking skills, sparking an intense rivalry and a cooking bet. "
         "Listen to their fiery dialogue in Russian first, and then we will examine every line.")

STORY = [
 ("anya", "Доброе утро, шеф!", "Good morning, Chef!",
  [(69, "Доброе утро, шеф")], ""),
 ("chef", "Огузок, ты постоянно опаздываешь на работу.", "Runt, you are constantly late for work.",
  [(69, "Агузик"), (70, "Ты постоянно"), (71, "ты опять опоздал")], "clean A1"),
 ("anya", "Шеф, мне не выдали форму вовремя.", "Chef, they did not issue my uniform on time.",
  [(72, "мне"), (72, "форму не выдало")], "adapted"),
 ("chef", "Хватит оправданий, быстро иди работать!", "Enough excuses, quickly go to work!",
  [(68, "За работу")], "adapted"),
 ("fedya", "Ты так же плохо шутишь, как и готовишь.", "You joke as badly as you cook.",
  [(78, "Ты так же"), (78, "шутишь, как и готовишь")], "плохо used for A1"),
 ("anya", "Я не понял твоей шутки, Федя.", "I didn't understand your joke, Fedya.",
  [(79, "Не понял")], "extended"),
 ("fedya", "Это обычное состояние для твоего мозга.", "This is a normal state for your brain.",
  [(79, "привычное состояние для твоего мозга")], "обычное used for A1"),
 ("anya", "Ты хочешь сказать, что я плохо готовлю?", "Do you want to say that I cook badly?",
  [(80, "он сказал, что я"), (82, "ты хочешь сказать")], "adapted"),
 ("fedya", "Да, именно это я и говорю.", "Yes, that is exactly what I say.",
  [], "new line"),
 ("anya", "А ты думаешь, ты готовишь лучше меня?", "And do you think you cook better than me?",
  [(82, "ты лучше готовишь")], "adapted"),
 ("fedya", "Уж точно намного лучше тебя!", "Certainly much better than you!",
  [(83, "уж не хуже")], "adapted"),
 ("anya", "Тогда давай устроим кулинарный спор!", "Then let's make a culinary bet!",
  [(84, "Спорим")], "extended"),
 ("fedya", "Спорим, огузок! Я легко тебя выиграю!", "Wanna bet, runt! I will easily beat you!",
  [(84, "Спорим")], "extended"),
 ("anya", "Посмотрим, кто из нас лучший повар!", "We will see which of us is the best cook!",
  [(87, "кто из них победил")], "adapted"),
]

OPENER = "Let's examine this heated kitchen rivalry step by step."

WALK = [
 (0, None,
  "'Good morning, Chef!' Max greets Barinov nervously as he arrives late."),
 (1, None,
  "'Runt, you are constantly late for work.' Barinov berates him for lack of punctuality."),
 (2, None,
  "'Chef, they did not issue my uniform on time.' Blaming the cleaning staff for the delay."),
 (3, None,
  "'Enough excuses, quickly go to work!' Cutting off the rookie's explanations immediately."),
 (4, None,
  "'You joke as badly as you cook.' Fish chef Fedya throws a sharp culinary insult."),
 (5, None,
  "'I didn't understand your joke, Fedya.' Max turns to face the antagonistic cook."),
 (6, None,
  "'This is a normal state for your brain.' Fedya mocks his intelligence with another zinger."),
 (7, None,
  "'Do you want to say that I cook badly?' Challenging the offensive critique directly."),
 (8, None,
  "'Yes, that is exactly what I say.' Fedya doubles down without hesitation."),
 (9, None,
  "'And do you think you cook better than me?' Max questions the veteran's culinary superiority."),
 (10, None,
  "'Certainly much better than you!' Expressing complete confidence in his own professional skills."),
 (11, None,
  "'Then let's make a culinary bet!' Proposing a contest to settle the argument."),
 (12, None,
  "'Wanna bet, runt! I will easily beat you!' Accepting the challenge eagerly."),
 (13, None,
  "'We will see which of us is the best cook!' Setting the stage for an intense culinary duel."),
]

TRANSITION = "Now let's listen to the whole confrontation once again."

OUTRO = ("That concludes our fifth scene. In Kukhnya, pride and culinary rivalry can turn an ordinary morning "
         "into a fierce culinary competition. See you next time!")

CLOSING = ("anya", "До встречи!")
