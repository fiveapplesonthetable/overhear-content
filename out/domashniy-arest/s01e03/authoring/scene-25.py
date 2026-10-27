ID = "domashniy-arest-s01e03-scene-25"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 25
TITLE = "Чай с вишнёвым вареньем  (Tea with Cherry Jam)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "pasha": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "pasha": "Паша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Nina has no voice (two-role limit besides `anya`): her defensive remarks (853-854, 865-866) are "
               "narrated, while Samson and Pasha take the two other voices. Cues 858-861 ('горяченького чайка хлопня', "
               "'на бутер налегай') simplified to plain A1; transcription slips fixed: 'Денис' (863) -> 'Нина', "
               "'вишню варежем' (873) -> 'Вишнёвое варенье', 'Нинокому реально ух' (882) -> 'Нина ему чуть ухо', "
               "'душевого' (884) -> 'живого'. Crude/swearing lines 876, 886, 888, 894, 897 dropped or retold cleanly.")

INTRO = ("Back in the communal flat, Nina's scalpel has just nicked Arkady's ear, and the sight of real blood turns "
         "everything upside down. Last time, across the courtyard, Major Lavrov and Captain Zavarzin sent young "
         "Lyova away from their listening post. Here, big Samson panics over the bleeding cut, bandages Arkady's "
         "head, and starts fussing over him like a guest—just as Pasha walks in to see if Arkady has confessed. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("samson", "Остановилась там кровь уже? Смотри, сколько крови вылилось!",
  "Has the bleeding stopped yet? Look how much blood came out!",
  [(852, "Остановилась там кровь уже"), (856, "сколько"), (856, "вылилось")],
  "Nina's reply (853-854) narrated; 'кровища' -> 'крови'"),
 ("anya", "Самсон, не задуши меня.",
  "Samson, don't choke me.",
  [(857, "не задуши меня")], "'Самсон' added as Samson wraps the bandage too tightly"),
 ("samson", "Аркаша, держи горячий чай. И бутерброд с вареньем ешь.",
  "Arkasha, here's some hot tea. And eat a jam sandwich.",
  [(858, "держи"), (861, "с вареньем")],
  "cues 858-861 ('горяченького чайка хлопня', 'на бутер налегай') simplified to plain A1"),
 ("samson", "Нина, ну как ты могла? Живого человека ножом резать!",
  "Nina, how could you? Cutting a living person with a knife!",
  [(863, "ну как"), (864, "Живого человека ножом резать")],
  "cue 863 garbled 'Денис, ну как вы могли' -> 'Нина, ну как ты могла'"),
 ("anya", "Подожди, это что, абрикос? Я ненавижу абрикосы.",
  "Wait, what is this, apricot? I hate apricots.",
  [(868, "это что, абрикос"), (870, "Я ненавижу абрикосы")], ""),
 ("anya", "А есть у вас малина?",
  "Do you have raspberry?",
  [(871, "А есть у вас малина")], ""),
 ("samson", "Малины нет. Вишнёвое варенье есть, будешь?",
  "No raspberry. There's cherry jam, do you want some?",
  [(872, "Нет"), (873, "есть, будешь")],
  "cue 873 garbled 'вишню варежем' -> 'Вишнёвое варенье'"),
 ("anya", "Да. Несите вашу вишню.",
  "Yes. Bring your cherry.",
  [(874, "Да"), (875, "вишню")],
  "slang 'тащите вишню свою' -> 'Несите вашу вишню'; Nina's crude remark in 876 dropped"),
 ("pasha", "Ну что, признался?",
  "Well, did he confess?",
  [(877, "Ну что, признался")], ""),
 ("anya", "Самсон, кто это? Я хочу, чтобы он ушёл.",
  "Samson, who is that? I want him to leave.",
  [(878, "Самсон. Я хочу, чтобы он ушел")], "'кто это?' added"),
 ("samson", "У нас всё не так пошло. Нина ему чуть ухо не отрезала.",
  "Things went wrong for us. Nina nearly cut his ear off.",
  [(882, "У нас"), (882, "все"), (882, "не так пошло"), (882, "чуть не")],
  "cue 882 garbled 'Нинокому реально ух чуть не отрезало' -> 'Нина ему чуть ухо не отрезала'"),
 ("pasha", "Ну и что? Он должен страдать, а нам нужна информация.",
  "So what? He is supposed to suffer, and we need the information.",
  [(883, "Ну и что? Он должен"), (883, "страдать"), (883, "информацию")],
  "'а вы должны были получить информацию' -> 'а нам нужна информация'"),
 ("samson", "Нельзя так живого человека пытать!",
  "You can't torture a living person like that!",
  [(884, "человека"), (884, "пытать")],
  "cue 884 garbled 'душевого человека-то пытать' -> 'живого человека пытать'"),
 ("anya", "Так развяжите меня! Я всё скажу в полиции!",
  "Then untie me! I'll tell the police everything!",
  [(887, "Так развяжите меня")],
  "insult 'кретины' dropped; 'Я всё скажу в полиции' sets up 892"),
 ("anya", "Скажу, что ты нанял людей меня пытать. И не видать вам квартиры!",
  "I'll say that you hired people to torture me. And you'll never see that flat!",
  [(892, "скажу, что"), (892, "нанял"), (892, "пытать"), (893, "не видать"), (893, "квартиры")],
  "slang 'ментам' -> 'в полиции'; cue 892 'человека' -> 'людей меня'; 'тебе' -> 'вам'"),
 ("samson", "Не нужна нам такая квартира! Уходи отсюда!",
  "We don't need a flat like that! Get out of here!",
  [(894, "Квартиру")], "clean stand-in for Samson's crude refusal in 894"),
]

OPENER = ("Let's go through it line by line. Nina says there is barely a scratch, but Samson is horrified by the "
          "blood and wraps a thick white bandage around Arkady's head.")

WALK = [
 (0, "Остановилась там кровь уже?",
  "'Has the bleeding stopped yet?' Literally 'did the blood stop there already?'. The word for 'blood' is "
  "feminine, so the past verb ends in the feminine form."),
 (0, "Смотри, сколько крови вылилось!",
  "'Look how much blood came out!' After 'how much', 'blood' takes its genitive ending. Samson winds the "
  "bandage so tightly round Arkady's neck and chin that Arkady can hardly breathe."),
 (1, None,
  "'Samson, don't choke me.' Even tied to a chair, Arkady sounds more annoyed than frightened now. Samson "
  "rushes to make him feel better."),
 (2, "Аркаша, держи горячий чай.",
  "'Arkasha, here's some hot tea.' Literally 'hold hot tea'—and since Arkady's hands are tied, Samson holds the "
  "mug for him."),
 (2, "И бутерброд с вареньем ешь.",
  "'And eat a jam sandwich.' Literally 'a sandwich with jam', because sweet things are good for shock. Then "
  "Samson turns on Nina, while putting Arkady's glasses back on for him."),
 (3, "Нина, ну как ты могла?",
  "'Nina, how could you?' The past verb has the feminine ending because he is speaking to his wife."),
 (3, "Живого человека ножом резать!",
  "'Cutting a living person with a knife!' Notice 'with a knife' is a single word in the instrumental case, "
  "the form for the tool you use. Nina apologises and says Arkady provoked her, while Arkady tastes the "
  "sandwich and frowns."),
 (4, "Подожди, это что, абрикос?",
  "'Wait, what is this, apricot?' He is tied to a chair with a bandaged head, and he's complaining about the "
  "flavour of the jam."),
 (4, "Я ненавижу абрикосы.",
  "'I hate apricots.' Then he makes a polite request."),
 (5, None,
  "'Do you have raspberry?' Literally 'is there by you raspberry?'. Samson checks the kitchen shelf."),
 (6, "Малины нет.",
  "'No raspberry.' Because it is absent, 'raspberry' switches to the genitive case."),
 (6, "Вишнёвое варенье есть, будешь?",
  "'There's cherry jam, do you want some?' Using 'will you?' on its own is the everyday Russian way to offer "
  "food or drink. Arkady gives his royal approval."),
 (7, None,
  "'Yes. Bring your cherry.' Just then the door opens, and Pasha—the man who promised Samson and Nina the "
  "three-room flat—walks in."),
 (8, None,
  "'Well, did he confess?' One short masculine past verb. Arkady can't see Pasha clearly behind him, or "
  "pretends not to."),
 (9, "Самсон, кто это?",
  "'Samson, who is that?' Then he gives Samson an order as if Samson were his butler."),
 (9, "Я хочу, чтобы он ушёл.",
  "'I want him to leave.' After 'so that'—which is how Russian says 'want someone to do something'—the verb "
  "always goes into the past tense. Samson awkwardly explains the situation to Pasha."),
 (10, "У нас всё не так пошло.",
  "'Things went wrong for us.' Literally 'by us everything went not so'."),
 (10, "Нина ему чуть ухо не отрезала.",
  "'Nina nearly cut his ear off.' There is that 'nearly didn't' pattern again: 'almost cut off'. Pasha doesn't "
  "care at all."),
 (11, "Ну и что?",
  "'So what?' Cold and smooth as ever."),
 (11, "Он должен страдать, а нам нужна информация.",
  "'He is supposed to suffer, and we need the information.' Even big Samson is shocked by how cold Pasha is."),
 (12, None,
  "'You can't torture a living person like that!' Samson only ever meant to scare Arkady, not hurt him. And now "
  "Arkady sees his chance to break Pasha's deal completely."),
 (13, "Так развяжите меня!",
  "'Then untie me!' He shouts to Samson and Nina, and then threatens Pasha."),
 (13, "Я всё скажу в полиции!",
  "'I'll tell the police everything!' Literally 'I will say everything in the police'."),
 (14, "Скажу, что ты нанял людей меня пытать.",
  "'I'll say that you hired people to torture me.' And then he turns the threat on Samson and Nina's reward."),
 (14, "И не видать вам квартиры!",
  "'And you'll never see that flat!' Literally 'not to see to you of the flat'—a vivid Russian idiom for 'you "
  "can kiss that flat goodbye'. Pasha and Samson square up to each other, and Samson has had enough."),
 (15, None,
  "'We don't need a flat like that! Get out of here!' Samson throws away the dream of the three-room flat "
  "rather than torture a man for Pasha, and Pasha leaves empty-handed."),
]

TRANSITION = "Let's hear the whole scene with the bandage and the cherry jam again."

OUTRO = ("So Nina's accidental cut ended the torture session, Samson gave up the three-room flat and threw Pasha "
         "out, and Arkady is still tied to his chair drinking tea. Next time, young Slavik walks in with a very "
         "surprising delivery.")
CLOSING = ("anya", "Так развяжите меня!")
