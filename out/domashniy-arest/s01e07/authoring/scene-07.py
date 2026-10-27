ID = "domashniy-arest-s01e07-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 7
TITLE = "Упал с лестницы  (Fell Down the Stairs)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina", "marina": "anja"}
LABELS = {"anya": "Аркадий", "ilona": "Илона", "marina": "Марина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

INTRO = ("Last time, outside Marina's door, Arkady dropped to his knees and kissed Ilona's boots until she agreed to "
         "help him break up Marina and Eduard, just before a loud crash echoed from the stairwell. Now Marina and "
         "Eduard rush out to find Arkady lying on the stairs while Ilona calls for an ambulance. Let's listen in "
         "Russian first.")

STORY = [
 ("ilona", "Марина! Аркадий Борисович с лестницы упал!",
  "Marina! Arkady Borisovich fell down the stairs!",
  [(285, "Марина"), (289, "Аркадий Борисович с лестницы упал")],
  "cue 286 omitted"),
 ("ilona", "Алло! Нам срочно нужна скорая помощь!",
  "Hello! We urgently need an ambulance!",
  [(287, "Алло"), (288, "Нам срочно нужна"), (288, "скорая помощь")], ""),
 ("marina", "Что случилось?",
  "What happened?",
  [(290, "Что случилось")], ""),
 ("ilona", "Да полез паутину снимать. И вот упал!",
  "He climbed up to clear cobwebs. And fell!",
  [(291, "полез"), (292, "паутину снимать"), (293, "и вот упал")],
  "cue 293 'идиот' omitted"),
 ("ilona", "Он хотел вас на чай пригласить. Но говорит, тут не убрано у него.",
  "He wanted to invite you for tea. But he says his place isn't tidy.",
  [(294, "Хотел"), (294, "на чай"), (294, "пригласить"), (295, "говорит, не убрано тут у него")], ""),
 ("anya", "Зачем ты ей рассказываешь? Это была тайна!",
  "Why are you telling her? That was a secret!",
  [(296, "Зачем ты ей рассказываешь? Это была тайна")], ""),
 ("anya", "Иди отсюда! Ты мне уже ухо чуть не отрезала!",
  "Go away! You nearly cut my ear off last time!",
  [(298, "Иди отсюда! Ты мне уже ухо чуть не отрезала")],
  "replying to Nina's offer in cue 297"),
 ("ilona", "Не надо! Сказали не трогать и вообще не шевелить!",
  "Don't! They said not to touch him and not to move him at all!",
  [(299, "Не надо"), (299, "Сказали не трогать"), (300, "Вообще"), (300, "не шевелить")], ""),
 ("marina", "Вам больно?",
  "Are you in pain?",
  [(301, "Вам больно")], ""),
 ("anya", "Я ничего не вижу! Где мои очки?",
  "I can't see anything! Where are my glasses?",
  [(302, "Я ничего не вижу. Где мои очки")], ""),
 ("marina", "Вон очки лежат.",
  "There lie your glasses.",
  [(303, "Вон"), (303, "очки лежат")], ""),
 ("anya", "Вы же поедете со мной в больницу? Пожалуйста!",
  "You will ride with me to the hospital, won't you? Please!",
  [(305, "Вы же поедете"), (306, "со мной в больницу"), (307, "Пожалуйста")], ""),
 ("marina", "Ну, не знаю.",
  "Well, I don't know.",
  [(308, "Ну, знаю")],
  "cue 308 ASR 'Ну, знаю' -> 'Ну, не знаю'"),
 ("anya", "Вы даже можете его с собой взять. Вот этого!",
  "You can even take him along with you. That one!",
  [(309, "Вы даже можете его с собой взять"), (309, "Этого")], ""),
 ("anya", "Главное, чтобы вы были рядом, как друг. Пожалуйста, мне очень больно!",
  "The main thing is that you are nearby, as a friend. Please, I'm in a lot of pain!",
  [(311, "Главное, чтобы вы были рядом"), (312, "Как друг. Пожалуйста, мне очень больно")], ""),
]

OPENER = ("Let's walk through the scene. On the stairwell landing, Ilona puts on an Oscar-worthy performance while "
          "Arkady groans on the steps.")

WALK = [
 (0, "Марина! Аркадий Борисович с лестницы упал!",
  "'Marina! Arkady Borisovich fell down the stairs!' Notice the preposition with the genitive case for 'down from the "
  "stairs'. Ilona speaks into her phone to the prison service."),
 (1, "Алло! Нам срочно нужна скорая помощь!",
  "'Hello! We urgently need an ambulance!' Literally 'rapid help is urgently needed to us'. Marina hurries out in her "
  "robe."),
 (2, "Что случилось?",
  "'What happened?' Ilona smoothly delivers the romantic story she and Arkady just invented."),
 (3, "Да полез паутину снимать. И вот упал!",
  "'He climbed up to clear cobwebs. And fell!' And why was Arkady cleaning the stairwell?"),
 (4, "Он хотел вас на чай пригласить. Но говорит, тут не убрано у него.",
  "'He wanted to invite you for tea. But he says his place isn't tidy.' From the floor, Arkady pretends to be "
  "embarrassed."),
 (5, "Зачем ты ей рассказываешь? Это была тайна!",
  "'Why are you telling her? That was a secret!' Neighbour Nina comes out and offers to examine him since she is a "
  "nurse, which terrifies Arkady."),
 (6, "Иди отсюда! Ты мне уже ухо чуть не отрезала!",
  "'Go away! You nearly cut my ear off last time!' Ilona quickly blocks Nina from examining Arkady and discovering he "
  "isn't hurt at all."),
 (7, "Не надо! Сказали не трогать и вообще не шевелить!",
  "'Don't! They said not to touch him and not to move him at all!' Sympathetic Marina kneels beside Arkady."),
 (8, "Вам больно?",
  "'Are you in pain?' Literally 'is it painful to you?' Arkady squints dramatically."),
 (9, "Я ничего не вижу! Где мои очки?",
  "'I can't see anything! Where are my glasses?' Marina spots them on the step."),
 (10, "Вон очки лежат.",
  "'There lie your glasses.' Arkady reaches for Marina's hand."),
 (11, "Вы же поедете со мной в больницу? Пожалуйста!",
  "'You will ride with me to the hospital, won't you? Please!' Marina hesitates, glancing back at Eduard."),
 (12, "Ну, не знаю.",
  "'Well, I don't know.' Arkady generously waves a hand toward fuming Eduard."),
 (13, "Вы даже можете его с собой взять. Вот этого!",
  "'You can even take him along with you. That one!' Eduard bristlingly asks what he means by 'that one', and Arkady "
  "gives Marina his most pitiful look."),
 (14, "Главное, чтобы вы были рядом, как друг. Пожалуйста, мне очень больно!",
  "'The main thing is that you are nearby, as a friend. Please, I'm in a lot of pain!' And tender-hearted Marina "
  "agrees to go with him to the hospital, ruining Eduard's evening."),
]

TRANSITION = "Now let's hear the whole stairwell scene again from start to finish."

OUTRO = ("So Ilona and Arkady's staged fall works like a charm: instead of spending a romantic evening with Eduard, "
         "Marina rides in the ambulance with Arkady to the hospital. See you next time.")
CLOSING = ("anya", "Пожалуйста, мне очень больно!")
