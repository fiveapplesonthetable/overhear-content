ID = "domashniy-arest-s01e04-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 3
TITLE = "Завтрак на кухне  (Breakfast in the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "anja", "klavdia": "angelina"}
LABELS = {"anya": "Аркадий", "nina": "Нина", "klavdia": "Клавдия Викторовна"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = ("Cues 72-112. Curses and vulgarities in cues 83 ('алкаша'), 88-90 ('Чтоб ты сдох', 'сожрал'), "
               "and 101-105 ('говно', 'подавились') are replaced with clean A1 language. Numbers in cues 86-87 "
               "are written out as words. Samson's brief entrance (96) and the TV news report at the end "
               "(108-112) are told by the narrator and folded into Nina's last line.")

INTRO = ("Back in the communal flat, later that morning. Last time, the Moscow strategist Ilona tricked her "
         "pushy taxi driver into pulling over under Devil's Bridge. "
         "Now Arkady is back from the hospital with a bandage around his head, and in the shared kitchen he "
         "finds Nina and old Klavdia Viktorovna watching the famous Soviet singer Lev Leshchenko on television. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Почему меня все бьют в этом доме?",
  "Why does everyone beat me in this house?",
  [(72, "Почему меня все бьют в этом доме")], ""),
 ("nina", "А это кто поёт?",
  "And who is that singing?",
  [(74, "А это кто")], "'поёт' added"),
 ("klavdia", "Вот молодёжь, ничего не знают! Это же Лещенко! Звезда!",
  "Young people these days, they don't know anything! That's Leshchenko! A star!",
  [(75, "Вот молодежь"), (76, "Ничего"), (76, "не знают"), (77, "Это же Лещенко"), (78, "Звезда")],
  "'кроме своего Баскова' dropped"),
 ("klavdia", "Он за мной после концерта ухаживал. В Москву звал замуж!",
  "He courted me after a concert once. He asked me to marry him and come to Moscow!",
  [(79, "после концерта"), (81, "В Москву звал замуж")],
  "slang 'кадрил' -> 'ухаживал'"),
 ("anya", "А в Париж вас никто замуж не звал?",
  "And nobody asked you to marry him and move to Paris?",
  [(82, "А в"), (82, "вас"), (82, "звал замуж")],
  "'в Париже вас, Ален Делоне' simplified to 'в Париж вас никто'"),
 ("klavdia", "А я вышла за своего Гришу. Теперь меня рядом с ним похоронить не хотят!",
  "And instead I married my Grisha. Now they won't even bury me next to him!",
  [(83, "А я"), (83, "за своего"), (84, "теперь меня"), (84, "с ним"), (84, "похоронить не хотят")],
  "'выскочила за своего Гришко-алкаша' -> 'вышла за своего Гришу'"),
 ("nina", "Да потому что там всё за взятки.",
  "That's because everything there takes a bribe.",
  [(85, "Да потому что там"), (85, "за взятки")], ""),
 ("anya", "Да какие там взятки? Сто пятьдесят тысяч рублей.",
  "What sort of bribes could there be? A hundred and fifty thousand roubles.",
  [(86, "Да какие там взятки"), (86, "тысяч рублей")],
  "'150' written out as words; 'максимум' dropped"),
 ("klavdia", "А тебе этого мало? У меня пенсия двенадцать тысяч!",
  "And is that a small sum to you? My pension is twelve thousand!",
  [(87, "А тебе этого мало? У меня пенсия"), (87, "тысяч")],
  "'12' written out as words"),
 ("klavdia", "Ты икру мою съел! И коньяк выпил у бедной старухи!",
  "You ate up my caviar! And you drank a poor old woman's cognac!",
  [(90, "Икру мою"), (91, "Коньяк выпил у"), (91, "старухи")],
  "curses in 88-89 dropped; 'сожрал' -> 'съел'; 'нищей' -> 'бедной'"),
 ("anya", "Я же вам сказал, что всё верну! Какая вы жадная женщина.",
  "I told you I'll pay it all back! What a greedy woman you are.",
  [(92, "Я же вам сказал"), (92, "верну"), (93, "Какая вы жадная женщина")], ""),
 ("anya", "В гроб с собой икру не положишь!",
  "You can't put caviar in your coffin to take with you!",
  [(94, "В гроб с собой икру не положишь")], ""),
 ("klavdia", "Да лучше в гроб, чем тебе! Плохой ты человек, Аркадий.",
  "Better into my coffin than to you! You're a bad man, Arkady.",
  [(95, "Да лучше в гроб, чем тебе"), (88, "Аркадий"), (101, "человек")],
  "cue 101 'Говно человек' cleaned up to 'Плохой ты человек'"),
 ("nina", "Клавдия Викторовна, здесь же ребёнок, мы завтракаем. А телевизор, между прочим, наш!",
  "Klavdia Viktorovna, there's a child here, we're having breakfast. And the television, by the way, is ours!",
  [(102, "Клавдия Викторовна"), (103, "здесь же ребенок"), (103, "завтракаем"),
   (107, "Телевизор, между прочим, наш")], "cues 104-105 omitted"),
 ("nina", "Ой, смотрите, Самсона по телевизору показывают! Уже несколько миллионов просмотров!",
  "Oh, look, they're showing Samson on television! Several million views already!",
  [(111, "уже несколько миллионов просмотров")],
  "folds the TV news report in cues 108-111 into Nina's reaction"),
]

OPENER = ("Let's walk through it step by step. Arkady walks into the kitchen holding his bandaged head and "
          "complains to the whole room.")

WALK = [
 (0, None,
  "'Why does everyone beat me in this house?' Literally 'why do all beat me in this house?'. Nobody feels sorry "
  "for him. Instead, Nina looks at the little television on the counter."),
 (1, None,
  "'And who is that singing?' Old Klavdia Viktorovna is shocked that Nina doesn't recognise her idol, the famous "
  "Soviet singer Lev Leshchenko."),
 (2, None,
  "'Young people these days, they don't know anything! That's Leshchenko! A star!' And then Klavdia shares a "
  "proud memory from her youth."),
 (3, None,
  "'He courted me after a concert once. He asked me to marry him and come to Moscow!' In Russian, a woman says "
  "'he called me into marriage', using a special adverb that applies only to women marrying a man. Arkady "
  "can't resist teasing her."),
 (4, None,
  "'And nobody asked you to marry him and move to Paris?' Klavdia ignores him and sighs over the choice she "
  "made instead."),
 (5, "А я вышла за своего Гришу.",
  "'And instead I married my Grisha.' Literally 'I went out behind my Grisha', the standard phrase for a woman "
  "marrying a man."),
 (5, "Теперь меня рядом с ним похоронить не хотят!",
  "'Now they won't even bury me next to him!' Keep that wish in mind—being buried beside her late husband "
  "Grisha is going to matter later in this episode. Nina knows why the cemetery refuses."),
 (6, None,
  "'That's because everything there takes a bribe.' Arkady scoffs, as an expert on bribes."),
 (7, None,
  "'What sort of bribes could there be? A hundred and fifty thousand roubles.' That is how much the cemetery "
  "director wants for a plot next to Grisha. Klavdia is furious."),
 (8, None,
  "'And is that a small sum to you? My pension is twelve thousand!' Literally 'and to you of this is little?'. "
  "Then she reminds Arkady what he did in episode two, when he broke into her padlocked fridge."),
 (9, None,
  "'You ate up my caviar! And you drank a poor old woman's cognac!' Both verbs are perfective past forms: "
  "he ate it all up and drank it all down."),
 (10, None,
  "'I told you I'll pay it all back! What a greedy woman you are.' And he adds a dark joke."),
 (11, None,
  "'You can't put caviar in your coffin to take with you!' Literally 'into the coffin with yourself you won't "
  "put caviar'."),
 (12, None,
  "'Better into my coffin than to you! You're a bad man, Arkady.' Just then Samson comes in for breakfast, and "
  "Nina tries to calm the old lady down—and switches the channel."),
 (13, "Клавдия Викторовна, здесь же ребёнок, мы завтракаем.",
  "'Klavdia Viktorovna, there's a child here, we're having breakfast.'"),
 (13, "А телевизор, между прочим, наш!",
  "'And the television, by the way, is ours!' Remember that Klavdia wants a television of her very own. And the "
  "moment Nina changes the channel, a breaking news report comes on."),
 (14, None,
  "'Oh, look, they're showing Samson on television! Several million views already!' It's the video from episode "
  "one, where Samson threw the corrupt mayor out the window and said ordinary people can't live decent lives "
  "because of crooks like him—and the whole country is watching it."),
]

TRANSITION = "Now let's listen to the whole kitchen scene again from the beginning."

OUTRO = ("So Klavdia dreams of her own television and a cemetery plot beside her husband Grisha, while Samson "
         "has suddenly become an internet star with millions of views. Next we'll follow Samson and Nina to the "
         "job centre and a luxury car showroom; see you then.")
CLOSING = ("anya", "Почему меня все бьют в этом доме?")
