ID = "kukhnya-s01e03-scene-05"
TITLE = "Паника на кухне  (Panic in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Макс", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = ("In this scene, Max runs into the kitchen terrified that Vika's ex-husband, a powerful prosecutor, "
         "will destroy him. Chef Viktor Barinov does not offer much sympathy and jokingly begins reciting Max's eulogy. "
         "Listen to the story in Russian first, and then we will review each line.")

STORY = [
 ("anya", "Шеф, у меня большие проблемы.", "Chef, I have big problems.",
  [], "new line"),
 ("chef", "Что опять стряслось, огузок?", "What happened again, runt?",
  [], "new line"),
 ("anya", "Меня ищет грозный прокурор.", "A terrible prosecutor is looking for me.",
  [], "new line"),
 ("chef", "И за что же он тебя ищет?", "And why is he looking for you?",
  [], "new line"),
 ("anya", "Он знает про меня и Вику.", "He knows about me and Vika.",
  [], "new line"),
 ("chef", "Ты спал с чужой женщиной?", "You slept with someone else's woman?",
  [(162, "спал с чужой")], ""),
 ("anya", "Я не знал, что она замужем.", "I did not know that she is married.",
  [], "new line"),
 ("chef", "Это был самый талантливый повар.", "He was the most talented cook.",
  [(161, "Это был самый талантливый")], "повар adapted from огузок for A1"),
 ("chef", "Которого я когда-либо знал.", "Whom I ever knew.",
  [(161, "которого я знал")], ""),
 ("anya", "Шеф, вы меня уже хороните?", "Chef, are you already burying me?",
  [], "new line"),
 ("chef", "С прокурором шутки плохи.", "You don't mess with a prosecutor.",
  [], "new line"),
 ("chef", "Он тебя быстро за решётку отправит.", "He will quickly send you behind bars.",
  [], "new line"),
 ("anya", "Что же мне теперь делать?", "What should I do now?",
  [], "new line"),
 ("chef", "Иди работай и не болтай.", "Go work and do not chat.",
  [], "new line"),
]

OPENER = "Let's review this funny kitchen panic step by step."

WALK = [
 (0, None,
  "'Chef, I have big problems.' Max approaches the head chef in total panic."),
 (1, None,
  "'What happened again, runt?' Barinov uses his classic condescending nickname."),
 (2, None,
  "'A terrible prosecutor is looking for me.' Explaining the scary encounter outside."),
 (3, None,
  "'And why is he looking for you?' Asking for the reason behind the threat."),
 (4, None,
  "'He knows about me and Vika.' Revealing his secret night out with Vika."),
 (5, None,
  "'You slept with someone else's woman?' Barinov instantly identifies the romantic mess."),
 (6, None,
  "'I did not know that she is married.' Max pleads ignorance about her past relationship."),
 (7, None,
  "'He was the most talented cook.' Barinov starts mockingly delivering Max's eulogy."),
 (8, None,
  "'Whom I ever knew.' Continuing the dramatic funeral speech."),
 (9, None,
  "'Chef, are you already burying me?' Max protests the chef's dark humor."),
 (10, None,
  "'You don't mess with a prosecutor.' A standard warning about cross-examining law enforcement."),
 (11, None,
  "'He will quickly send you behind bars.' Forecasting prison time for the rookie cook."),
 (12, None,
  "'What should I do now?' Asking desperately for practical advice."),
 (13, None,
  "'Go work and do not chat.' The chef orders him back to his culinary duties."),
]

TRANSITION = "Alright, let's hear the whole conversation once again."

OUTRO = ("That concludes our fifth scene. In Kukhnya, Chef Barinov's cynical wit is always on display, "
         "even when his staff is in serious trouble. See you next time!")

CLOSING = ("anya", "До встречи!")
