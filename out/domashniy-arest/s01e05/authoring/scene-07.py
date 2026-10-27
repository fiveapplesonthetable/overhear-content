ID = "domashniy-arest-s01e05-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 7
TITLE = "Страшное лицо Костика  (Kostik's Scary Face)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostik": "anja"}
LABELS = {"anya": "Дядя Гриша", "kostik": "Костик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = ("Last time, two microloan debt collectors — Uncle Grisha and young Kostik — demanded a hundred and fifty "
         "thousand roubles from Marina, and she bravely pushed them out the door. Now, out on the stairs, Uncle Grisha "
         "scolds timid Kostik because nobody is afraid of them. Let's listen in Russian first; don't worry about "
         "catching every word.")

STORY = [
 ("kostik", "Да ладно, дядя Гриша, нормально мы отработали.",
  "Come on, Uncle Grisha, we did our job fine.",
  [(241, "Да ладно, дядя"), (242, "отработали. Нормально")],
  "cue 241 slip 'Игорь Ильич' -> 'Гриша'"),
 ("anya", "Ты слышал, что она сказала? Я вас не боюсь!",
  "Did you hear what she said? I'm not afraid of you!",
  [(243, "Ты слышал, что она сказала"), (244, "Я вас не боюсь")], ""),
 ("anya", "А нас должны бояться! Нас никто не боится!",
  "And people should be afraid of us! Nobody is afraid of us!",
  [(245, "А нас должны бояться"), (247, "Нас никто не боится")], ""),
 ("kostik", "Она боится, я видел.",
  "She is afraid, I saw it.",
  [(246, "Она боится, я видел")], ""),
 ("anya", "Мы уже неделю работаем! И нам никто денег не отдал.",
  "We've been working for a week already! And nobody has paid us any money.",
  [(248, "Мы уже неделю работаем, и нам никто"), (249, "денег не отдал")],
  "cues 248-249 split into two short sentences"),
 ("anya", "А всё почему? Потому что ты трус!",
  "And why is that? Because you're a coward!",
  [(250, "А все почему"), (251, "Потому что ты")],
  "crude 'цикло / ссыкло' (252) and 'в жопе вода' (256) cleaned to 'трус'"),
 ("kostik", "И что мне делать?",
  "And what should I do?",
  [(257, "И что мне делать")], ""),
 ("anya", "Мы же договорились: я пугаю, а ты иллюстрируешь!",
  "We agreed: I do the scaring, and you illustrate it!",
  [(258, "Мы же договорились"), (259, "Я пугаю"), (260, "А ты иллюстрируешь")], ""),
 ("kostik", "Так я иллюстрировал! Лицо страшное делал!",
  "But I was illustrating! I was making a scary face!",
  [(261, "Так я иллюстрировал"), (261, "лицо страшное")],
  "cue 261 slip 'дело' -> 'делал'"),
 ("anya", "Страшное лицо на своей жене будешь делать! А тут действовать надо!",
  "You can make a scary face at your wife! Here you have to take action!",
  [(262, "Страшное лицо на своей жене будешь делать"), (263, "А тут действовать надо")], ""),
 ("kostik", "И что мне надо было сделать?",
  "And what should I have done?",
  [(264, "И что мне надо"), (264, "сделать")],
  "word order smoothed"),
 ("anya", "Да хоть что-нибудь! Шкаф бы сломал.",
  "Anything at all! You could have broken a wardrobe.",
  [(265, "Да хоть что-нибудь"), (266, "Шкаф бы сломал")],
  "cue 267 'пацану в ухо вывернул' omitted"),
 ("anya", "Тогда они поймут, что мы серьёзные люди.",
  "Then they will understand that we are serious people.",
  [(268, "они"), (269, "что мы серьезные люди")],
  "cue 268 'Чтобы они поняли' made a standalone sentence"),
 ("kostik", "Так пойдём, давай вернёмся! Я всё переверну!",
  "Then let's go, let's go back! I'll turn everything upside down!",
  [(270, "Так пойдем, давай вернемся"), (271, "Я"), (271, "переверну")], ""),
 ("anya", "Нет! Мы сейчас пойдём пообедаем.",
  "No! Right now we'll go and have lunch.",
  [(273, "Нет! Мы сейчас пойдем, пообедаем")], ""),
]

OPENER = ("Let's walk through it. Going down the stairs of the communal flat, young Kostik tries to cheer up his "
          "grumpy boss, Uncle Grisha.")

WALK = [
 (0, "Да ладно, дядя Гриша, нормально мы отработали.",
  "'Come on, Uncle Grisha, we did our job fine.' The prefix on the verb means working through a task from start to "
  "finish. Uncle Grisha stops on the landing and glares at him."),
 (1, "Ты слышал, что она сказала? Я вас не боюсь!",
  "'Did you hear what she said? I'm not afraid of you!' Remember that the verb 'to be afraid' takes the genitive "
  "case: not afraid of you."),
 (2, "А нас должны бояться! Нас никто не боится!",
  "'And people should be afraid of us! Nobody is afraid of us!' For a debt collector, that is a professional "
  "disaster. Kostik tries to defend himself."),
 (3, None,
  "'She is afraid, I saw it.' Uncle Grisha counts up their week's results."),
 (4, "Мы уже неделю работаем! И нам никто денег не отдал.",
  "'We've been working for a week already! And nobody has paid us any money.' Notice the double negative: 'nobody "
  "did not give back money'."),
 (5, "А всё почему? Потому что ты трус!",
  "'And why is that? Because you're a coward!' Literally 'and all why?'. Kostik looks hurt."),
 (6, None,
  "'And what should I do?' Literally 'and what to me to do?'. Grisha reminds him of their division of labour."),
 (7, "Мы же договорились: я пугаю, а ты иллюстрируешь!",
  "'We agreed: I do the scaring, and you illustrate it!' Uncle Grisha is the talker, and Kostik is supposed to be "
  "the muscle."),
 (8, "Так я иллюстрировал! Лицо страшное делал!",
  "'But I was illustrating! I was making a scary face!' And Kostik pulls his funny frown again to show how scary he "
  "looked."),
 (9, "Страшное лицо на своей жене будешь делать!",
  "'You can make a scary face at your wife!' Literally 'on your own wife you will make'."),
 (9, "А тут действовать надо!",
  "'Here you have to take action!' Kostik asks for concrete instructions."),
 (10, None,
  "'And what should I have done?' Adding the past neuter 'was' to 'it is necessary' makes it 'should have'."),
 (11, "Да хоть что-нибудь! Шкаф бы сломал.",
  "'Anything at all! You could have broken a wardrobe.' With the conditional particle 'would', the past form means "
  "'you could have broken'."),
 (12, "Тогда они поймут, что мы серьёзные люди.",
  "'Then they will understand that we are serious people.' Suddenly Kostik gets fired up and turns back toward the "
  "stairs."),
 (13, "Так пойдём, давай вернёмся! Я всё переверну!",
  "'Then let's go, let's go back! I'll turn everything upside down!' But Uncle Grisha is in no hurry to skip a meal."),
 (14, "Нет! Мы сейчас пойдём пообедаем.",
  "'No! Right now we'll go and have lunch.' Intimidation can wait until after lunch."),
]

TRANSITION = "Now let's listen to the whole stairwell conversation again."

OUTRO = ("So Uncle Grisha and Kostik head off to have lunch before coming back to smash a wardrobe. Listen for 'I do "
         "the scaring, and you illustrate!' when you watch; see you in the next scene.")
CLOSING = ("anya", "Я пугаю, а ты иллюстрируешь!")
