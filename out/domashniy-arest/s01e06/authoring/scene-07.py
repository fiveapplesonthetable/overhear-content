ID = "domashniy-arest-s01e06-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = "Побитая бамбуком панда  (A Panda Beaten with Bamboo)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina"}
LABELS = {"anya": "Аркадий", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"

INTRO = ("Last time, at the security service office, Major Lavrov got permission from General Kruglov in Moscow to "
         "discredit Samsonov before the election. Meanwhile, in the communal flat, Arkady angrily phones his "
         "girlfriend Lyolya while Ilona goes through their list of possible campaign sponsors. We'll hear the scene "
         "in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Послушай, Лёля, я столько в тебя вложил! Хочу тебя увидеть.",
  "Listen, Lyolya, I invested so much in you! I want to see you.",
  [(240, "Послушай, Леля, я столько в тебя вложил"), (241, "хочу")],
  "cue 241 crude 'получить просто маленький сексуальный дивиденд' -> 'тебя увидеть'"),
 ("anya", "Приезжай сейчас! Иначе я перестану давать тебе деньги!",
  "Come over right now! Otherwise I'll stop giving you money!",
  [(243, "сейчас"), (243, "я перестану давать тебе деньги")],
  "cue 243 shortened into two short A1 sentences"),
 ("anya", "Я выйду отсюда и верну свои деньги!",
  "I'll get out of here and get my money back!",
  [(245, "выйду отсюда, верну"), (245, "свои деньги")], ""),
 ("anya", "Послушай, не клади трубку! Ах ты, неблагодарная!",
  "Listen, don't hang up! Oh, you ungrateful girl!",
  [(247, "Послушай, не клади трубку"), (249, "Ах ты, неблагодарная")],
  "cue 249 'содержанка' omitted"),
 ("ilona", "Так, Сизов отказал, Гапоненко отказал. Добрецова вообще в городе нет.",
  "Right, Sizov refused, Gaponenko refused. Dobretsov isn't in town at all.",
  [(250, "Так"), (250, "отказал"), (251, "отказал"), (252, "вообще в городе нет")],
  "cues 250-252 ASR 'Сиземов/Габуленко/Добрецка' -> 'Сизов/Гапоненко/Добрецова'"),
 ("ilona", "Мы не можем продолжать кампанию без спонсоров. Нам даже плакаты напечатать не на что.",
  "We cannot continue the campaign without sponsors. We don't even have money to print posters.",
  [(253, "Мы не можем продолжать"), (253, "без спонсоров"), (254, "Нам даже"), (254, "плакаты напечатать не на что")],
  "cue 253 ASR 'компанию' -> 'кампанию'"),
 ("anya", "Ничего, она ещё пожалеет! Да слышу я, слышу.",
  "Never mind, she'll regret it yet! Yes, I hear you, I hear you.",
  [(255, "Ничего, она еще пожалеет"), (257, "Да слышу я, слышу")], ""),
 ("ilona", "Ну и что делать будем?",
  "So what are we going to do?",
  [(258, "Ну и что делать будем")], ""),
 ("anya", "А вот что будем делать. Иди сюда, ну пожалуйста!",
  "Here is what we're going to do. Come here, please!",
  [(259, "А вот что будем делать"), (261, "Иди сюда"), (263, "Ну пожалуйста")], ""),
 ("ilona", "Ты с ума сошёл? У нас с тобой только деловые отношения!",
  "Have you lost your mind? Between you and me it's strictly business!",
  [(262, "С ума сошел"), (265, "мы с тобой"), (266, "только деловые отношения")], ""),
 ("ilona", "Не надо на меня смотреть, как побитая бамбуком панда!",
  "Don't look at me like a panda beaten with bamboo!",
  [(270, "Не надо"), (270, "на меня смотреть, как побитая бамбуком панда")], ""),
 ("ilona", "Лучше придумай, где нам денег взять!",
  "Better think of where we can get money!",
  [(271, "Лучше придумай, где нам денег взять")], ""),
 ("anya", "Ни у кого в городе нет денег, кроме Игнатьева.",
  "Nobody in town has any money, except Ignatyev.",
  [(273, "ни у кого в"), (273, "городе"), (274, "кроме")],
  "cue 273 ASR 'Едет' -> 'денег', cue 274 ASR 'Гнатьева' -> 'Игнатьева'"),
 ("ilona", "А это кто?",
  "And who is that?",
  [(275, "А это кто")], ""),
 ("anya", "Это мясокомбинат. Но он не даст, он нас ненавидит.",
  "That's the meatpacking plant. But he won't give any, he hates us.",
  [(276, "Но он"), (276, "не даст"), (277, "Он нас ненавидит")],
  "cue 276 ASR 'Мяшекомбинат' -> 'мясокомбинат'"),
 ("anya", "Я хотел просто в его бизнес войти. Ну давай поцелуемся!",
  "I just wanted to get into his business. Come on, let's kiss!",
  [(280, "я хотел просто в его бизнес войти"), (282, "ну давай")],
  "cue 280 'сучонок' omitted; cue 282 crude 'потрахаемся' -> 'поцелуемся'"),
]

OPENER = ("Let's go through the scene step by step. Arkady is on the phone with his spoiled girlfriend Lyolya, who "
          "refuses to visit him in the communal flat.")

WALK = [
 (0, "Послушай, Лёля, я столько в тебя вложил! Хочу тебя увидеть.",
  "'Listen, Lyolya, I invested so much in you! I want to see you.' Then he tries threatening to cut off her allowance."),
 (1, "Приезжай сейчас! Иначе я перестану давать тебе деньги!",
  "'Come over right now! Otherwise I'll stop giving you money!' Lyolya points out that his accounts are frozen anyway."),
 (2, "Я выйду отсюда и верну свои деньги!",
  "'I'll get out of here and get my money back!' Notice the future tense of two perfective verbs: 'I will walk out' "
  "and 'I will return'. Lyolya hangs up on him."),
 (3, "Послушай, не клади трубку! Ах ты, неблагодарная!",
  "'Listen, don't hang up! Oh, you ungrateful girl!' Literally 'do not lay down the receiver'. Meanwhile, Ilona has "
  "finished calling local businessmen."),
 (4, "Так, Сизов отказал, Гапоненко отказал. Добрецова вообще в городе нет.",
  "'Right, Sizov refused, Gaponenko refused. Dobretsov isn't in town at all.' Every single businessman is afraid to "
  "back Samsonov."),
 (5, "Мы не можем продолжать кампанию без спонсоров. Нам даже плакаты напечатать не на что.",
  "'We cannot continue the campaign without sponsors. We don't even have money to print posters.' Still staring at his "
  "phone, Arkady mutters about Lyolya before answering Ilona."),
 (6, "Ничего, она ещё пожалеет! Да слышу я, слышу.",
  "'Never mind, she'll regret it yet! Yes, I hear you, I hear you.' Ilona demands a plan."),
 (7, "Ну и что делать будем?",
  "'So what are we going to do?' Arkady suddenly reaches over to hug Ilona."),
 (8, "А вот что будем делать. Иди сюда, ну пожалуйста!",
  "'Here is what we're going to do. Come here, please!' Ilona immediately pushes him back and whacks him with her "
  "notebook."),
 (9, "Ты с ума сошёл? У нас с тобой только деловые отношения!",
  "'Have you lost your mind? Between you and me it's strictly business!' Arkady rubs his cheek with big sad eyes."),
 (10, "Не надо на меня смотреть, как побитая бамбуком панда!",
  "'Don't look at me like a panda beaten with bamboo!' And she brings him straight back to the campaign."),
 (11, "Лучше придумай, где нам денег взять!",
  "'Better think of where we can get money!' Arkady sighs that all the local businessmen are broke after paying into "
  "Pasha's cluster — except one."),
 (12, "Ни у кого в городе нет денег, кроме Игнатьева.",
  "'Nobody in town has any money, except Ignatyev.' Notice the double negative with the preposition 'except' plus the "
  "genitive case. Ilona doesn't know the name."),
 (13, None,
  "'And who is that?' Arkady explains."),
 (14, "Это мясокомбинат. Но он не даст, он нас ненавидит.",
  "'That's the meatpacking plant. But he won't give any, he hates us.' Why does Ignatyev hate City Hall?"),
 (15, "Я хотел просто в его бизнес войти. Ну давай поцелуемся!",
  "'I just wanted to get into his business. Come on, let's kiss!' Even after explaining how he tried to squeeze "
  "Ignatyev's plant, Arkady still tries his luck, and Ilona walks out to visit Ignatyev herself."),
]

TRANSITION = "Now let's listen to the whole conversation between Arkady and Ilona again."

OUTRO = ("So Ilona has a new target: Veniamin Igorevich Ignatyev, the wealthy owner of the Sineozersk meatpacking "
         "plant. See you in the next scene.")
CLOSING = ("ilona", "Лучше придумай, где нам денег взять!")
