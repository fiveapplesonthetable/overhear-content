ID = "domashniy-arest-s01e03-scene-05"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 5
TITLE = "Жучок на липучке  (The Sticky Bug)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lavrov": "anja", "zavarzin": "angelina"}
LABELS = {"anya": "Марина", "lavrov": "Лавров", "zavarzin": "Заварзин"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Cues 198-214. Arkady is absent, so Marina Sergeyevna is the viewpoint character (anya, label Марина). "
               "Cue 204 ('Мне что, его кураулить, что ли?') simplified to 'Мне что, ждать у двери?'. "
               "Cue 210 (where Marina names the condom wrapper) is retold cleanly as 'Что это? Зачем мне это?', "
               "with the narrator explaining neutrally that the second bug is disguised inside a small foil packet.")

INTRO = ("Outside in the courtyard, Marina meets the two security agents from Moscow, Major Lavrov and Captain "
         "Zavarzin. Last time, Pasha showed Samson and Nina a bright new three-room flat and promised it was theirs "
         "if they could scare Arkady into saying where he hid his money. Now the two agents have their own job for "
         "Marina: they hand her a tiny listening bug to hide inside Arkady's room. We'll hear the scene in Russian "
         "first; don't worry about catching every word.")

STORY = [
 ("lavrov", "Это нужно поставить в комнате Аникеева.",
  "This needs to be put in Anikeev's room.",
  [(198, "Это нужно"), (198, "в комнате Аникеева")], "'установить' -> 'поставить'"),
 ("zavarzin", "Это просто, он на липучке.",
  "It's simple, it's on a sticky pad.",
  [(199, "Это просто, он на липучке")], ""),
 ("lavrov", "Лепите на уровне головы, в тихое место.",
  "Stick it at head height, in a quiet spot.",
  [(200, "Лепите"), (200, "на уровне головы"), (201, "место")],
  "'где-нибудь' dropped; 'неприметное место и все' -> 'тихое место'"),
 ("anya", "Как я это сделаю? Он всё время в комнате.",
  "How will I do that? He's in the room all the time.",
  [(202, "Как я это сделаю, он все время в комнате")], "split into two sentences"),
 ("zavarzin", "Но он же выходит в туалет, на кухню.",
  "But he goes out to the bathroom, to the kitchen.",
  [(203, "Но он же выходит в туалет"), (203, "на кухню")], "'душ принять' dropped"),
 ("anya", "Мне что, ждать у двери?",
  "What, am I supposed to wait by the door?",
  [(204, "Мне что")], "cue 204 'его кураулить, что ли?' (stake him out, garbled) simplified to 'ждать у двери?'"),
 ("anya", "Я этим никогда не занималась. Что я здесь делаю?",
  "I've never done anything like this. What am I doing here?",
  [(205, "этим никогда не занималась"), (206, "Что я здесь делаю")], "'вообще' dropped"),
 ("anya", "Хорошо, давайте я попробую.",
  "Fine, let me try.",
  [(207, "Хорошо, давайте я попробую")], "first 'хорошо' dropped"),
 ("lavrov", "Подождите, это образец. А вот ваш.",
  "Wait, that's a sample. And here is yours.",
  [(208, "Это образец"), (209, "Ваш")], "'Подождите' and 'А вот' added"),
 ("anya", "Что это? Зачем мне это?",
  "What is this? Why are you giving me this?",
  [], "clean stand-in for cue 210 (where Marina sees the small foil packet)"),
 ("lavrov", "Там внутри такой же жучок.",
  "There's the same kind of bug inside.",
  [(211, "Там внутри такой же жучок")], ""),
 ("zavarzin", "Марина Сергеевна, упаковка маскирующая. Не вызывает подозрений.",
  "Marina Sergeyevna, the packaging is camouflage. It doesn't raise suspicion.",
  [(212, "Марина Сергеевна, упаковка маскирующая"), (213, "не вызывает подозрений")], ""),
 ("lavrov", "Такая вещь есть у каждого.",
  "Everyone has one of these.",
  [(213, "Есть у каждого")], "'Такая вещь' added"),
 ("anya", "У меня нет.",
  "I don't.",
  [(214, "У меня нет")], ""),
]

OPENER = ("Let's walk through it line by line. Major Lavrov holds up a tiny microphone and gives Marina her "
          "instructions.")

WALK = [
 (0, None,
  "'This needs to be put in Anikeev's room.' Literally, 'this is necessary to put'. Anikeev's surname takes the "
  "'of' ending, meaning 'room of Anikeev'. Captain Zavarzin reassures her."),
 (1, None,
  "'It's simple, it's on a sticky pad.' He calls the little bug 'he' because the Russian word for a bug is "
  "masculine. The last word comes from the verb 'to stick', so it means a sticky pad or Velcro. Lavrov tells her "
  "where it goes."),
 (2, None,
  "'Stick it at head height, in a quiet spot.' He uses the polite plural command form because they address Marina "
  "respectfully. 'At the level of the head' uses the 'of' form of 'head'. Marina sees an obvious problem."),
 (3, "Как я это сделаю?",
  "'How will I do that?' A perfective verb in the present form always points to the future: 'how will I get that "
  "done?'"),
 (3, "Он всё время в комнате.",
  "'He's in the room all the time.' Russian needs no word for 'is' in the present tense, just 'he all time in "
  "room'. Zavarzin points out that even someone under house arrest leaves his room."),
 (4, None,
  "'But he goes out to the bathroom, to the kitchen.' Notice how 'in the room' used the location ending, while "
  "'to the bathroom' and 'to the kitchen' use the accusative ending for movement towards a place."),
 (5, None,
  "'What, am I supposed to wait by the door?' Literally, 'to me what, to wait by the door?' Using 'to me' with an "
  "infinitive is how Russian asks 'am I supposed to do this?'. Suddenly she wonders how she got into this mess."),
 (6, "Я этим никогда не занималась.",
  "'I've never done anything like this.' Because Marina is a woman, the past-tense verb ends in 'a' before the "
  "reflexive ending. And Russian stacks negatives: 'never not did'."),
 (6, "Что я здесь делаю?",
  "'What am I doing here?' Four simple everyday words. Then she sighs and gives in."),
 (7, None,
  "'Fine, let me try.' Literally, 'let's I will try', a polite, natural way to offer to give something a go. She "
  "reaches for the bug, but Lavrov stops her."),
 (8, "Подождите, это образец.",
  "'Wait, that's a sample.' That first bug was only for demonstration."),
 (8, "А вот ваш.",
  "'And here is yours.' He hands her a small square foil packet instead. Marina stares at it in disbelief."),
 (9, None,
  "'What is this? Why are you giving me this?' Literally, 'for what to me this?'. To make sure nobody suspects a "
  "listening device if it is found in her pocket, they have hidden it inside a small foil wrapper."),
 (10, None,
  "'There's the same kind of bug inside.' Literally, 'there inside is such-same little beetle'. In Russian, a "
  "listening bug is affectionately called a 'little beetle'. Zavarzin explains the disguise."),
 (11, "Марина Сергеевна, упаковка маскирующая.",
  "'Marina Sergeyevna, the packaging is camouflage.' He addresses her by first name and father's name, completely "
  "deadpan."),
 (11, "Не вызывает подозрений.",
  "'It doesn't raise suspicion.' Literally, 'does not call out suspicions', in the plural 'of' form after a "
  "negative. Lavrov adds a helpful remark."),
 (12, None,
  "'Everyone has one of these.' Literally, 'such a thing is at everyone'. Marina has the last word."),
 (13, None,
  "'I don't.' Literally, 'at me there isn't', the exact mirror of 'at everyone there is'."),
]

TRANSITION = "Now let's listen to the whole conversation again from the beginning."

OUTRO = ("So Marina walks back to the communal flat with a listening bug disguised in a foil wrapper in her pocket. "
         "Next we'll see Samson try to earn his new flat from Arkady; see you then.")
CLOSING = ("anya", "Давайте я попробую.")
