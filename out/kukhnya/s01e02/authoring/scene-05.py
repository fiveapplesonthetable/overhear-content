ID = "kukhnya-s01e02-scene-05"
TITLE = "Японский нож  (The Japanese Knife)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "senya": "anja"}
LABELS = {"senya": "Сеня"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = ("In this scene, Anya and Senya quietly discuss why Chef Barinov is so protective of his lost knife. "
         "Senya explains that it is an irreplaceable Japanese blade, and everyone must search thoroughly. "
         "Listen to the conversation in Russian first, and then we will examine it in English.")

STORY = [
 ("anya", "Почему нельзя купить такой нож?", "Why can't we buy such a knife?",
  [], "new line"),
 ("senya", "По-быстрому такой нож купить не получится.", "You can't buy such a knife in a hurry.",
  [(95, "быстрому такой нож купить не получится")], ""),
 ("anya", "А сколько он стоит?", "And how much does it cost?",
  [], "new line"),
 ("senya", "Это дорогой японский нож.", "This is an expensive Japanese knife.",
  [], "new line"),
 ("senya", "Шеф заказывал его очень долго.", "The chef ordered it for a very long time.",
  [], "new line"),
 ("anya", "И он очень острый?", "And is it very sharp?",
  [], "new line"),
 ("senya", "Самый острый нож на кухне.", "The sharpest knife in the kitchen.",
  [], "new line"),
 ("anya", "Где же он может быть?", "Where could it possibly be?",
  [], "new line"),
 ("senya", "Мы уже везде искали.", "We already looked everywhere.",
  [], "new line"),
 ("anya", "Может, кто-то взял его домой?", "Maybe someone took it home?",
  [], "new line"),
 ("senya", "Никто не посмеет это сделать.", "Nobody would dare do that.",
  [], "new line"),
 ("senya", "Шеф сразу всех уволит.", "The chef will fire everyone immediately.",
  [], "new line"),
 ("senya", "Давай нож ищи скорее.", "Come on, look for the knife quickly.",
  [(97, "Давай нож ищи")], ""),
 ("anya", "Хорошо. Я посмотрю здесь.", "All right. I will look here.",
  [], "new line"),
]

OPENER = "Let's explore why this particular kitchen knife is so valuable to the chef."

WALK = [
 (0, None,
  "'Why can't we buy such a knife?' Anya wonders why replacing the tool is so complicated."),
 (1, None,
  "'You can't buy such a knife in a hurry.' Senya explains using the impersonal verb indicating that something will not work out."),
 (2, None,
  "'And how much does it cost?' Asking about the financial value of the missing blade."),
 (3, None,
  "'This is an expensive Japanese knife.' Identifying the special craftsmanship and origin of the chef's tool."),
 (4, None,
  "'The chef ordered it for a very long time.' Emphasizing how much effort went into acquiring it."),
 (5, None,
  "'And is it very sharp?' Anya asks about its cutting quality."),
 (6, None,
  "'The sharpest knife in the kitchen.' A superlative construction meaning 'the most sharp'."),
 (7, None,
  "'Where could it possibly be?' The emphatic particle adds urgency to the question."),
 (8, None,
  "'We already looked everywhere.' Expressing frustration that all obvious places have been checked."),
 (9, None,
  "'Maybe someone took it home?' Suggesting a possible theft or accidental removal."),
 (10, None,
  "'Nobody would dare do that.' The verb expresses courage or audacity to commit a forbidden act."),
 (11, None,
  "'The chef will fire everyone immediately.' Describing the drastic consequence if the knife was stolen."),
 (12, None,
  "'Come on, look for the knife quickly.' A renewed push to continue the kitchen search."),
 (13, "Хорошо.",
  "'All right.' A brief agreement to comply."),
 (13, "Я посмотрю здесь.",
  "'I will look here.' Promising to inspect her current station."),
]

TRANSITION = "Alright, let's hear the whole dialogue once more."

OUTRO = ("That is our fifth scene. In Kukhnya, Barinov's beloved Japanese knife turns out to be hidden "
         "in the most unexpected place. See you next time!")

CLOSING = ("anya", "До встречи!")
