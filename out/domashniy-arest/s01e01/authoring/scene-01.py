ID = "domashniy-arest-s01e01-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = "Подарки из Венгрии  (Gifts from Hungary)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "father": "anja", "samson": "angelina"}
LABELS = {"anya": "Аркадий", "father": "Отец Самсона", "samson": "Ваня"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"

INTRO = ("This series is called House Arrest, and its hero is Arkady, the mayor of Sineozersk, a small Russian town; "
         "he grew up in a communal flat, one flat shared by several families. "
         "In this first episode he is caught taking a bribe and sent home under house arrest, back to that same flat, "
         "right next door to Samson, the boy who used to bully him. "
         "But we start in the nineteen eighties: Samson, then just little Vanya, sees his father come home from "
         "Hungary with presents, and little Arkady can only watch. "
         "We'll hear it all in Russian first; don't worry about catching every word.")

STORY = [
 ("samson", "Привет, папа!", "Hi, Dad!",
  [(20, "Привет")], "greeting from cues 19-20; 'папа' added (cue 30: 'Здрасте, пап!')"),
 ("father", "Привет! Смотри, что у меня есть.", "Hi! Look what I've got.",
  [(52, "смотри")], "'Привет!' and 'что у меня есть' new"),
 ("samson", "Ого, магнитофон! Японский!", "Wow, a tape recorder! A Japanese one!",
  [(58, "Ого")], "cues 21/23 'Мафон' (slang) -> магнитофон; cue 24 'Маденжапан' (made in Japan) -> Японский"),
 ("anya", "Здравствуйте! Как там в Венгрии?", "Hello! How was Hungary?",
  [(27, "как там в Венгрии")],
  "a neighbour's question given to Arkady; 'Здравствуйте' = full form of 'Здрасте' (cue 28)"),
 ("father", "Хорошо! Там всё нормально.", "Good! Everything's fine over there.",
  [(49, "нормально")], "cue 49 'там все ... нормально все' (said of his jacket) shortened; 'Хорошо!' new"),
 ("samson", "Папа, а жвачку ты привёз?", "Dad, did you bring any gum?",
  [(31, "привез")], "'Пап, а как ты жвачки-то привез?' simplified"),
 ("father", "Жвачку? Денег не хватило.", "Gum? I didn't have enough money.",
  [(32, "не хватило")], "'Валюты' (foreign currency) -> 'Денег' (money); he is teasing"),
 ("samson", "Ну, папа!", "Oh, come on, Dad!",
  [(33, "Ну, пап")], "'пап' -> 'папа'"),
 ("father", "Ладно, держи. Вот, смотри.", "All right, here you go. There, look.",
  [(35, "Ладно"), (52, "держи, вот, смотри")], ""),
 ("samson", "Сколько жвачки! Класс!", "So much gum! Cool!",
  [(47, "Класс")], "'Сколько жвачки!' new (cue 59: 'look how much you've got')"),
 ("father", "А это тебе. Машинка!", "And this is for you. A toy car!",
  [(38, "это тебе")], "'Машинка!' new (the toy car of cue 53)"),
 ("samson", "Спасибо, папа!", "Thanks, Dad!", [], ""),
 ("father", "Со всеми поделись поровну, понял?", "Share it all equally with everyone, understand?",
  [(61, "со всеми"), (61, "поровну"), (61, "понял")], "'чтоб со всеми поделился поровну' -> imperative 'поделись'"),
 ("samson", "Понял.", "Got it.", [], ""),
 ("anya", "А можно я пойду посмотрю?", "Can I go and have a look?",
  [(65, "А можно я пойду посмотрю")], ""),
 ("anya", "Нельзя? Ладно, пойду учить уроки.", "Not allowed? All right, I'll go and do my homework.",
  [(66, "Уроки")], "the adult's answer (cue 66 'Уроки учи', 'do your homework') turned into Arkady's reply; 'Нельзя? Ладно, пойду учить' new"),
]

OPENER = ("Let's go back through it slowly. The door bangs, and the whole corridor knows that Vanya's father "
          "is home from abroad.")

WALK = [
 (0, None,
  "'Hi, Dad!' This is the casual hello, for family and friends. Dad has something to show him."),
 (1, "Смотри, что у меня есть.",
  "'Look what I've got.' Literally, 'look, what is at me'. That's how you say you have something: at me there is. "
  "The first thing out of the suitcase is a big one."),
 (2, None,
  "'Wow, a tape recorder! A Japanese one!' In the Soviet nineteen eighties that was a real treasure. "
  "Little Arkady is watching from the doorway, and he greets the father politely."),
 (3, "Здравствуйте!",
  "'Hello!' This is the long, polite hello, the one a child uses with a grown-up. Then he asks a question a neighbour "
  "asked."),
 (3, "Как там в Венгрии?",
  "'How was it there in Hungary?' Literally, 'how is it there, in Hungary'. After the little word for 'in', the "
  "country's name changes its ending. The father keeps it short."),
 (4, None,
  "'Good! Everything's fine over there.' The word for 'fine' looks a lot like 'normal'. Vanya only cares about one thing."),
 (5, None,
  "'Dad, did you bring any gum?' There's no word for 'did' here: the question is in his voice. "
  "And the verb ends in a plain consonant because the person who brought it, Dad, is a man. Dad likes to tease."),
 (6, None,
  "'Gum? I didn't have enough money.' The word for money is plural in Russian, like 'funds'. Vanya is not having it."),
 (7, None,
  "'Oh, come on, Dad!' The first little word does the work of 'oh, come on'. So Dad gives in."),
 (8, "Ладно, держи.",
  "'All right, here you go.' The second word literally means 'hold', and you hear it whenever someone hands "
  "something over. Then he points."),
 (8, "Вот, смотри.",
  "'There, look.' And Vanya can't believe his luck."),
 (9, None,
  "'So much gum! Cool!' The second word really means 'class', but kids use it for 'cool' or 'great'. "
  "There's one more present."),
 (10, None,
  "'And this is for you. A toy car!' The word for the car ends in a little suffix that makes things small, "
  "so it's a little car, a toy. Vanya remembers his manners."),
 (11, None,
  "'Thanks, Dad!' Then Dad gives an instruction."),
 (12, None,
  "'Share it all equally with everyone, understand?' The verb is a command. And the last word is the past tense of "
  "'understand', but it means 'got it?', right now. Vanya promises."),
 (13, None,
  "'Got it.' One word, same verb, now as an answer. Keep an eye on that promise. Meanwhile Arkady has a question too."),
 (14, None,
  "'Can I go and have a look?' Literally, 'can I go, I'll look'. Two verbs side by side, a very natural way to talk. "
  "An adult in his room says no."),
 (15, None,
  "'Not allowed? All right, I'll go and do my homework.' The first word means 'it's not allowed', the opposite of the 'can I' "
  "he just asked with. And homework is literally 'to learn lessons'. That's all he gets this time."),
]

TRANSITION = "Now the whole scene again, from the knock at the door."

OUTRO = ("That's the first scene, and the show's whole story starts with this one suitcase of presents. "
         "Next time we'll find out what happens to that little toy car; see you then.")
CLOSING = ("anya", "Пока!")
