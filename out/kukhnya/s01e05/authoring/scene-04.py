ID = "kukhnya-s01e05-scene-04"
TITLE = "Неловкое расставание  (An Awkward Breakup)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "angelina"}
LABELS = {"anya": "Макс", "nastya": "Настя"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = ("In this scene, Max meets waitress Nastya in the vegetable storeroom to clear up a huge misunderstanding. "
         "Nastya thinks they are on a romantic date and talking about their future, while Max frantically tries to explain they were never together. "
         "Listen to their comical conversation in Russian first, and then we will examine every line.")

STORY = [
 ("anya", "Настя, что ты сейчас делаешь?", "Nastya, what are you doing now?",
  [(50, "Что ты делаешь")], ""),
 ("nastya", "Ну, у нас же настоящее свидание!", "Well, we are on a real date!",
  [(50, "Ну, у нас же свидание")], "настоящее added"),
 ("anya", "Нет, Настя, у нас не свидание.", "No, Nastya, we are not on a date.",
  [(51, "Нет, Настя, у нас не свидание")], ""),
 ("anya", "Ты вчера всё не так поняла.", "You understood everything wrong yesterday.",
  [(52, "Ты вчера все не так поняла")], ""),
 ("anya", "Мы с тобой совсем не встречаемся.", "You and I are not dating at all.",
  [(53, "Мы с тобой не встречаемся")], "совсем added"),
 ("anya", "Я не твой парень.", "I am not your boyfriend.",
  [(53, "Я не твой парень")], ""),
 ("anya", "А ты не моя девушка.", "And you are not my girlfriend.",
  [(53, "а ты не моя девушка")], ""),
 ("nastya", "Ты что, меня сейчас бросаешь?", "Are you dumping me right now?",
  [(54, "Ты что, меня бросаешь")], "сейчас added"),
 ("anya", "Это вовсе не глупые шутки.", "These are not silly jokes at all.",
  [(55, "шуточки"), (56, "Это не шутки, Настя")], "adapted"),
 ("anya", "Между нами никогда ничего не было.", "Nothing ever happened between us.",
  [(58, "Между нами ничего не было")], "никогда added"),
 ("nastya", "А как же наш поцелуй?", "And what about our kiss?",
  [(60, "А поцелуй")], "как же наш added"),
 ("nastya", "А наши будущие дети?", "And what about our future children?",
  [(61, "А наши дети")], "будущие added"),
 ("anya", "Какие ещё дети, Настя?", "What children, Nastya?",
  [(62, "Какие дети")], "ещё, Настя added"),
 ("anya", "Да, если хочешь, я тебя бросаю!", "Yes, if you want, I am dumping you!",
  [(63, "да, я тебя бросаю")], "если хочешь added"),
]

OPENER = "Let's examine this hilarious breakup conversation step by step."

WALK = [
 (0, None,
  "'Nastya, what are you doing now?' Max pulls back in shock as she leans in."),
 (1, None,
  "'Well, we are on a real date!' Nastya assumes they are an official romantic couple."),
 (2, None,
  "'No, Nastya, we are not on a date.' Setting the record straight right away."),
 (3, None,
  "'You understood everything wrong yesterday.' Explaining that yesterday's event was a misunderstanding."),
 (4, None,
  "'You and I are not dating at all.' Firmly clarifying their actual relationship status."),
 (5, None,
  "'I am not your boyfriend.' Stating plainly that he is not her partner."),
 (6, None,
  "'And you are not my girlfriend.' Drawing a clear personal boundary."),
 (7, None,
  "'Are you dumping me right now?' Shocked and hurt by his blunt rejection."),
 (8, None,
  "'These are not silly jokes at all.' Making sure she takes his words seriously."),
 (9, None,
  "'Nothing ever happened between us.' Insisting that there is no romantic past between them."),
 (10, None,
  "'And what about our kiss?' Bringing up the awkward moment from yesterday."),
 (11, None,
  "'And what about our future children?' Dramatically jumping far ahead into the imagined future."),
 (12, None,
  "'What children, Nastya?' He is completely flabbergasted by her wild assumption."),
 (13, None,
  "'Yes, if you want, I am dumping you!' Finally giving in to end the absurd debate."),
]

TRANSITION = "Now let's listen to the whole dialogue one more time."

OUTRO = ("That concludes our fourth scene. In Kukhnya, clarifying relationship boundaries in the vegetable storeroom "
         "never goes quite as planned. See you next time!")

CLOSING = ("anya", "До встречи!")
