ID = "domashniy-arest-s01e02-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = "Очередь в туалет  (The Toilet Queue)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyosha": "anja", "marina": "angelina"}
LABELS = {"anya": "Аркадий", "lyosha": "Лёша", "marina": "Марина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"

INTRO = ("Last time, Arkady spent a sleepless first night in his old room, while at his big house his deputy Pasha "
         "woke Arkady's wife Vika and demanded the money; she showed him a stash of about three million, but the "
         "rest was gone. Now it's morning in the communal flat, and there's a queue for the only toilet. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Маленькие умеют терпеть, а взрослые нет, понял?",
  "Little ones can hold on, but grown-ups can't, got it?",
  [(149, "Маленькие умеют терпеть, а взрослые нет, понял")], ""),
 ("lyosha", "Так нечестно.", "That's not fair.", [(150, "Так нечестно")], ""),
 ("anya", "Как тебя зовут, мальчик?", "What's your name, boy?", [(151, "Как тебя зовут, мальчик")], ""),
 ("lyosha", "Лёха.", "Lyokha.", [(152, "Лёха")], ""),
 ("anya", "Всё честно, Лёха. Взрослые не умеют ждать.", "It's all fair, Lyokha. Grown-ups can't wait.",
  [(153, "Всё честно, Лёха")],
  "second sentence new: a clean stand-in for the crude reason in cue 154"),
 ("lyosha", "Мама! Он идёт без очереди!", "Mum! He's jumping the queue!", [],
  "the boy calls his mother, who then comes to the door (her protest starts at cue 158)"),
 ("anya", "Послушайте, в чём дело, женщина? Здесь занято.",
  "Listen, what's the matter, woman? It's occupied.",
  [(158, "Послушайте, в чём дело, женщина"), (159, "занято")],
  "cue 159 'Не видите, занято здесь' simplified to 'Здесь занято'"),
 ("marina", "Вы взяточник! Вы лезете вперёд больного ребёнка.",
  "You're a bribe-taker! You're pushing in ahead of a sick child.",
  [(160, "вы, взяточник"), (162, "Вперёд больного ребёнка")],
  "cue 162 simplified: 'лезть' kept as 'Вы лезете'; 'в туалет' and 'это совсем гнусность' (a disgrace) dropped"),
 ("anya", "Я вас где-то видел, кажется.", "I think I've seen you somewhere.",
  [(163, "Я вас где-то видел, кажется")], ""),
 ("marina", "Я ваш советник по историческому наследию. Забыли?",
  "I'm your adviser on historical heritage. Have you forgotten?",
  [(164, "Я ваш советник по историческому наследию"), (165, "Забыли")], "the town name dropped"),
 ("anya", "Да, да. Но туалет — это пока не историческое наследие.",
  "Yes, yes. But the toilet isn't historical heritage yet.",
  [(166, "Да, да")], "second sentence simplifies cue 167 (none of this counts as historical heritage yet)"),
 ("anya", "Всё, извините.", "That's it, excuse me.", [(168, "Извините")], "'Всё' added: he shuts the door on her"),
 ("marina", "Запомните: зло всегда возвращается к правителю.", "Remember: evil always comes back to the ruler.",
  [(169, "Запомните, зло всегда возвращается")],
  "the cue's 'от правителя' (a slip) -> 'к правителю', as in the English subtitle"),
 ("anya", "Сталину расскажите.", "Tell that to Stalin.", [(171, "Сталину расскажите")], "'вот это' dropped"),
 ("lyosha", "Мама, а кто это?", "Mum, who is that?", [], "the boy asks about the stranger"),
 ("marina", "Это наш мэр, Лёша.", "That's our mayor, Lyosha.", [],
  "she knows him from the protest (cues 160, 164)"),
]

OPENER = ("Let's go back through it slowly. Arkady has just shoved his way to the toilet door, past a little boy "
          "on crutches, and he explains himself without any shame.")

WALK = [
 (0, None,
  "'Little ones can hold on, but grown-ups can't, got it?' The verb that follows 'little ones' means 'can', in the "
  "sense of 'know how to'. At the end he checks the boy has understood, with a masculine past form, because he's "
  "talking to a boy. The boy protests."),
 (1, None,
  "'That's not fair.' Notice that 'not' is glued to the word for 'fair' here, and it makes one word: 'unfair'. "
  "Arkady pretends to be friendly."),
 (2, None,
  "'What's your name, boy?' Literally, 'how do they call you?'. It's the normal way to ask a name, and you'll use "
  "it all the time. The answer is just one word."),
 (3, None,
  "'Lyokha.' A casual, boyish form of Alexei. Elsewhere you'll also hear him called Lyosha. Arkady then uses the "
  "name against him."),
 (4, "Всё честно, Лёха.",
  "'It's all fair, Lyokha.' The same word for 'fair', now without the 'not'. Then comes his reason."),
 (4, "Взрослые не умеют ждать.",
  "'Grown-ups can't wait.' The same 'know how to' verb as before, now with 'not', and then the verb 'to wait'. "
  "That's a neat pattern: 'know how' plus a verb in its dictionary form. Lyosha calls for help."),
 (5, "Мама!",
  "'Mum!' Exactly what you'd expect."),
 (5, "Он идёт без очереди!",
  "'He's jumping the queue!' Word for word: 'he goes without queue'. It's the classic complaint in any line in "
  "Russia. Soon someone is knocking on the toilet door."),
 (6, "Послушайте, в чём дело, женщина?",
  "'Listen, what's the matter, woman?' He starts with the polite command form of 'listen'. But calling a stranger "
  "simply 'woman' sounds rude and old-fashioned."),
 (6, "Здесь занято.",
  "'It's occupied.' Literally 'here is taken'. It's the word you'll hear through any locked toilet door. The woman "
  "outside is not impressed."),
 (7, "Вы взяточник!",
  "'You're a bribe-taker!' She uses the polite 'you', but there's nothing polite about the rest. Remember, Arkady "
  "was arrested for taking a bribe."),
 (7, "Вы лезете вперёд больного ребёнка.",
  "'You're pushing in ahead of a sick child.' The verb literally means 'climb', and it's the word for barging in. "
  "'Ahead of' is followed by a special form of the words for 'sick' "
  "and 'child', the form that means 'of'. Now Arkady takes a proper look at her."),
 (8, None,
  "'I think I've seen you somewhere.' The verb is past, masculine, because Arkady is a man. The little word at the "
  "end means 'it seems'. She reminds him who she is."),
 (9, "Я ваш советник по историческому наследию.",
  "'I'm your adviser on historical heritage.' She is Marina Sergeyevna, the lecturer who led the "
  "protest to save the old monastery wall, and Arkady invited her onto a council about it. And she lives right "
  "here, in this flat."),
 (9, "Забыли?",
  "'Have you forgotten?' One word does the whole job: it's the past tense in the polite 'you' form."),
 (10, None,
  "'Yes, yes. But the toilet isn't historical heritage yet.' The word in the middle means 'for now', or 'yet'. "
  "He's mocking her, from behind a locked door."),
 (11, None,
  "'That's it, excuse me.' The polite 'excuse me', but here it really means 'go away'. Marina has a parting shot."),
 (12, None,
  "'Remember: evil always comes back to the ruler.' It's a polite command, 'remember', then a little proverb. "
  "The last words mean 'to the ruler'. Arkady has an answer ready."),
 (13, None,
  "'Tell that to Stalin.' The name has an ending that means 'to'. In other words: some rulers did very well, "
  "thank you. Lyosha still doesn't know who the rude man is."),
 (14, None,
  "'Mum, who is that?' A small word for 'and' or 'but' in front of 'who' makes it a curious, natural question. "
  "His mother tells him."),
 (15, None,
  "'That's our mayor, Lyosha.' Just 'this is our mayor', with no word for 'is'. A moment later Arkady's own former "
  "bodyguards burst in while he's still in there; they apologise, then drag him away 'with frightening "
  "rudeness', exactly as ordered."),
]

TRANSITION = "Now let's hear the whole scene once more, from the start of the queue."

OUTRO = ("That's the toilet queue, and Arkady's first morning didn't end well. Listen out for the complaint "
         "about jumping the queue and the word you hear through every locked door; see you next time.")
CLOSING = ("lyosha", "Мама, туалет свободен!")
