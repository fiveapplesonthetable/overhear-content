ID = "domashniy-arest-s01e02-scene-17"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = "Телефон губернатора  (The Governor's Number)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "slavik": "anja", "yulia": "angelina"}
LABELS = {"anya": "Аркадий", "slavik": "Славик", "yulia": "Юля"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
SOURCE_NOTE = ("Arkady is `anya` (label Аркадий); Slavik and Yulia speak. Lyosha is present but silent (the crude "
               "cue 532 about him is left out). The kids say вы to Arkady, he says ты to them. Cues 499-502 (the "
               "chief at headquarters) and 535-538 (the governor's judo coach) belong to the neighbouring scenes' "
               "action and are not used.")

INTRO = ("Back in the communal flat, Arkady has just traded his blocked iPhone to young Slavik, the Samsonovs' son, "
         "for the boy's old push-button phone. Last time, at security headquarters, the agents from Moscow explained "
         "their secret operation to a general, and the plan goes on. Now Arkady wants to ring the governor, the one "
         "man who might get him out, but the number is in the iPhone he has just given away. We'll hear it in "
         "Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Что за меню здесь? Как позвонить?", "What's this menu here? How do I make a call?",
  [(503, "меню здесь")], "'дебильное' (idiotic) dropped; 'Как позвонить?' simplifies cue 504 'Ну как выйти в номера?'"),
 ("slavik", "Вот так, и трубочка.", "Like this, and there's the little phone.",
  [(505, "Вот так"), (505, "и трубочка")], "'вот проводите' dropped"),
 ("anya", "Так, дай айфон.", "Right, give me the iPhone.", [(506, "Так, дай айфон")], ""),
 ("slavik", "Зачем? Мы поменялись, он мой.", "What for? We swapped, it's mine.",
  [(507, "Зачем"), (507, "Поменялись, он мой")], "'Мы' added"),
 ("anya", "Мне нужно посмотреть телефон губернатора. Дай сюда.",
  "I need to look up the governor's number. Give it here.",
  [(508, "телефон губернатора"), (508, "Дай сюда")], "word order of cue 508 made standard (нужно before the verb)"),
 ("slavik", "Только из моих рук.", "Only if I hold it.", [(509, "Только из моих рук")], ""),
 ("anya", "Ну ты и жадина!", "You're such a greedy little thing!",
  [], "new: clean stand-in for cue 510 'зажилоб у тебя страшный' (what a miser you are)"),
 ("anya", "Губернатор... Вот он. Свин.", "The governor... Here he is. 'Pig'.",
  [(511, "Губернатор"), (513, "Свин")], "'Вот он' new: Arkady finds the contact"),
 ("slavik", "Свин? Это свинка Пеппа!", "'Pig'? That's Peppa Pig!",
  [(514, "Свинка")], "the cue spells 'Пепа'; standard 'Пеппа' used, so only 'Свинка' is cited"),
 ("anya", "Не смейся. Диктуй номер.", "Don't laugh. Read me the number.",
  [], "new: links to cues 515-520, where the digits are read out"),
 ("slavik", "Восемь, девять, шесть, шесть...", "Eight, nine, six, six...",
  [], "cues 515-516 '8' / '966' written out as words (digits are not allowed in spoken lines)"),
 ("anya", "Так, ребята, выйдите из комнаты.", "Right, kids, go out of the room.",
  [(522, "ребята, выйдите из комнаты")], "'Ну-ка' -> 'Так' (from cue 521)"),
 ("anya", "Мне с губернатором нужно поговорить.", "I need to talk to the governor.",
  [(523, "Мне с губернатором нужно поговорить")], ""),
 ("yulia", "Это наша комната.", "This is our room.", [(525, "Это наша комната")],
  "speaker not marked in the subtitles; given to Yulia"),
 ("anya", "Слово мэра уже ничего не значит?", "Doesn't the mayor's word mean anything any more?",
  [(528, "Слово мэра уже ничего не значит")], "said as a question, as in the English subtitle"),
 ("yulia", "А вы мне тоже айфон подарите?", "Will you give me an iPhone too?",
  [(530, "А вы мне тоже"), (530, "айфон подарите")], "'седьмой' (seventh, the model) dropped"),
 ("anya", "Подарю, всё вам подарю!", "I will, I'll give you everything!",
  [(531, "Подарю"), (531, "вам подарю")], "the cue's 'все' read as 'всё' (everything)"),
]

OPENER = ("Let's take it slowly. Arkady is holding a phone with buttons instead of a screen, and he has forgotten "
          "how these things work.")

WALK = [
 (0, "Что за меню здесь?",
  "'What's this menu here?' The first two words together mean 'what kind of', a very common way to ask about "
  "something strange. Then the question that matters."),
 (0, "Как позвонить?",
  "'How do I make a call?' Just 'how' and the verb 'to call', with no 'I' at all. Slavik shows him."),
 (1, None,
  "'Like this, and there's the little phone.' He means the small green receiver key on the keypad. The ending of "
  "that word makes it small and cute, like adding 'little'. Now Arkady needs his old iPhone back."),
 (2, None,
  "'Right, give me the iPhone.' He uses the short command for one person he knows well. Slavik is not having it."),
 (3, None,
  "'What for? We swapped, it's mine.' The phone is masculine in Russian, so it's 'he' and not 'it'. Arkady "
  "explains."),
 (4, "Мне нужно посмотреть телефон губернатора.",
  "'I need to look up the governor's number.' Literally, 'to me it's necessary to look'. And the word for phone "
  "also means a phone number. The governor comes after it with the ending for 'of'."),
 (4, "Дай сюда.",
  "'Give it here.' The second word means 'to here', with movement. The boy sets a condition."),
 (5, None,
  "'Only if I hold it.' Word for word, 'only from my hands'. The new owner keeps a firm grip on his prize. Arkady "
  "is not impressed."),
 (6, None,
  "'You're such a greedy little thing!' The little word after 'you' adds 'what a', so it's an exclamation, not a "
  "statement. And then he finds the contact."),
 (7, None,
  "'The governor... Here he is. Pig.' Yes: Arkady saved his own boss in his phone under the name 'Pig'. Slavik "
  "thinks it's very funny."),
 (8, None,
  "'Pig? That's Peppa Pig!' The cartoon pig is a little girl, so the boy uses the feminine word for a small pig. "
  "Arkady wants the number, not jokes."),
 (9, None,
  "'Don't laugh. Read me the number.' Two short commands. The second verb means to dictate, to read something out "
  "for someone to write down or dial."),
 (10, None,
  "'Eight, nine, six, six...' Russian mobile numbers start with eight. Arkady dials digit by digit on the old phone. "
  "Then he wants some privacy."),
 (11, None,
  "'Right, kids, go out of the room.' This time the command is for several people, so it ends in a different "
  "sound. After 'out of', the room gets the ending for 'of'."),
 (12, None,
  "'I need to talk to the governor.' The governor now has the ending for 'with', because in Russian you talk with "
  "someone. The children don't move."),
 (13, None,
  "'This is our room.' A fair point: it's the Samsonovs' room, and the mayor is a guest. Arkady tries his old "
  "authority."),
 (14, None,
  "'Doesn't the mayor's word mean anything any more?' Two negative words side by side, 'nothing' and 'not': in "
  "Russian they don't cancel out, they make the 'no' stronger. Yulia spots her chance."),
 (15, None,
  "'Will you give me an iPhone too?' The verb is the one for giving a present, in the future tense. She is polite "
  "to the grown-up. And Arkady will promise anything."),
 (16, None,
  "'I will, I'll give you everything!' The first word alone means 'I'll give it as a present'. A promise from a "
  "man who has no money left at all."),
]

TRANSITION = "Here's the whole scene again, from the start."

OUTRO = ("So the children leave the room, and Arkady is alone with an old phone and the governor's number. Whether "
         "the call goes well is another story; see you next time.")
CLOSING = ("anya", "Алло?")
