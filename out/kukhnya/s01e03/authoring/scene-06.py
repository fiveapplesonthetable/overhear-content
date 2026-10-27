ID = "kukhnya-s01e03-scene-06"
TITLE = "Ложная тревога  (A False Alarm)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja"}
LABELS = {"anya": "Макс", "kostya": "Костя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = ("In this scene, Max sprints to the bar and accuses bartender Kostya of betraying him to the prosecutor. "
         "To Max's immense relief, it turns out the scary customer was only asking for directions to the restroom. "
         "Listen to the conversation in Russian first, and then we will examine every line.")

STORY = [
 ("anya", "Костя, зачем ты ему сказал?", "Kostya, why did you tell him?",
  [(163, "Зачем ты ему сказал")], ""),
 ("anya", "Мне же теперь полный конец.", "I am completely finished now.",
  [(163, "Мне ж теперь конец")], "полный added for flow"),
 ("kostya", "Кому я сказал?", "Who did I tell?",
  [(164, "Кому")], ""),
 ("anya", "Тому мужику в костюме.", "That man in the suit.",
  [(164, "Этому мужику")], "adapted"),
 ("anya", "Чего он у тебя спрашивал?", "What was he asking you?",
  [(164, "Чего он спрашивал")], "у тебя added"),
 ("kostya", "Да успокойся ты наконец.", "Oh, calm down already.",
  [], "new line"),
 ("kostya", "Он просто спрашивал про туалет.", "He was simply asking about the restroom.",
  [(165, "Он спрашивал, где туалет")], "adapted"),
 ("anya", "Серьёзно? Только про туалет?", "Seriously? Only about the restroom?",
  [], "new line"),
 ("kostya", "Да, он искал туалет.", "Yes, he was looking for the restroom.",
  [], "new line"),
 ("anya", "А про меня не спрашивал?", "And he didn't ask about me?",
  [], "new line"),
 ("kostya", "Кому ты вообще нужен?", "Who needs you anyway?",
  [], "new line"),
 ("anya", "Слава богу, пронесло.", "Thank goodness, dodged a bullet.",
  [], "new line"),
 ("kostya", "Ты чего такой нервный сегодня?", "Why are you so nervous today?",
  [], "new line"),
 ("anya", "Неважно, налей мне скорее воды.", "Never mind, pour me some water quickly.",
  [], "new line"),
]

OPENER = "Let's break down this hilarious misunderstanding line by line."

WALK = [
 (0, None,
  "'Kostya, why did you tell him?' Max rushes to the bar in total agitation."),
 (1, None,
  "'I am completely finished now.' Convinced that Kostya leaked his secret to the prosecutor."),
 (2, None,
  "'Who did I tell?' Kostya has no idea what Max is talking about."),
 (3, None,
  "'That man in the suit.' Referring to prosecutor Vadim."),
 (4, None,
  "'What was he asking you?' Trying to find out what information was compromised."),
 (5, None,
  "'Oh, calm down already.' The bartender tells him to stop overreacting."),
 (6, None,
  "'He was simply asking about the restroom.' Revealing the comically innocent reality."),
 (7, "Серьёзно?",
  "'Seriously?' Max cannot believe his sudden change of fortune."),
 (7, "Только про туалет?",
  "'Only about the restroom?' Double checking that no names were mentioned."),
 (8, None,
  "'Yes, he was looking for the restroom.' Reconfirming the simple question."),
 (9, None,
  "'And he didn't ask about me?' Making sure his own name never came up."),
 (10, None,
  "'Who needs you anyway?' Kostya's blunt reality check."),
 (11, None,
  "'Thank goodness, dodged a bullet.' An expression of immense relief."),
 (12, None,
  "'Why are you so nervous today?' Noticing Max's unusually erratic behavior."),
 (13, None,
  "'Never mind, pour me some water quickly.' Asking for water to calm his racing heart."),
]

TRANSITION = "Alright, let's hear the whole conversation once again."

OUTRO = ("That wraps up our sixth scene. In Kukhnya, high tension often turns into pure comedy "
         "in a matter of seconds. See you next time!")

CLOSING = ("anya", "До встречи!")
