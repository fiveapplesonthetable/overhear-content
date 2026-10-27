ID = "domashniy-arest-s01e02-scene-18"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = "Губернатор не поможет  (The Governor Won't Help)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "governor": "anja"}
LABELS = {"anya": "Аркадий", "governor": "Виктор Степанович"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
SOURCE_NOTE = ("Arkady is `anya` (label Аркадий); the governor speaks (`governor`, label Виктор Степанович). The "
               "judo coach, the secretary who puts the second call through and the aide are not voiced. The "
               "governor's crude lines (548, 551, 576, 584, 591, 595) are retold cleanly or left out; Arkady's "
               "self-insults (570-571) and the sewage (583) are told by the narrator. Merged scenes 19 (the staged "
               "judo photo) and 20 (Slavik calls a friend on the iPhone) are told in the OUTRO.")

INTRO = ("Still in the Samsonovs' room, Arkady has the number at last. Last time, he sent the children out and "
         "dialled the governor, Viktor Stepanovich, whom he once saved in his phone under the name 'Pig'. The "
         "governor answers in the middle of a judo session with his coach, and he already knows a few things about "
         "Arkady. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Виктор Степанович, Аникеев беспокоит.", "Viktor Stepanovich, it's Anikeev calling.",
  [(539, "Виктор Степанович, Аникеев беспокоит")], "'вас' dropped"),
 ("governor", "Ой, какие люди! Ну, Аркаша, как дела?", "Well, look who it is! So, Arkasha, how are things?",
  [(540, "Ой, какие люди"), (541, "Ну, Аркаша, как дела")], ""),
 ("anya", "Плохо. Очень плохо, Виктор Степанович.", "Bad. Very bad, Viktor Stepanovich.",
  [(542, "Плохо"), (543, "очень плохо, Виктор Степанович")], "'К сожалению' (unfortunately) dropped"),
 ("governor", "Я знаю. А зачем ты мне звонишь?", "I know. So why are you calling me?",
  [(544, "Я знаю")], "second sentence: plain version of cue 545 'А мне-то чего звонишь?'"),
 ("anya", "Мне очень нужна ваша помощь.", "I really need your help.",
  [(546, "Мне очень")], "cue 546 'Мне очень помощь ваша нужна' in standard word order"),
 ("governor", "Как интересно! А в Москве ты про меня гадости рассказываешь.",
  "How interesting! And in Moscow you go around saying nasty things about me.",
  [(547, "как интересно"), (549, "про меня"), (549, "гадости рассказываешь")],
  "'всякие' dropped; the crude insults of cues 548 and 551 left out"),
 ("governor", "Я знаю, как я у тебя в телефоне записан. Свин.", "I know what I'm saved as in your phone. 'Pig'.",
  [(552, "Я знаю, как я у тебя в телефоне записан"), (553, "Свин")], ""),
 ("anya", "Это неправда! Вы у меня записаны как Батя.", "That's not true! I have you saved as 'Dad'.",
  [(557, "Вы у меня"), (557, "записаны")],
  "'Это неправда' replaces 'это поклёп' (slander, garbled 'поклёб' in cues 555-556); 'как' added"),
 ("governor", "Мне некогда.", "I haven't got time.", [(560, "Мне некогда")], ""),
 ("anya", "Не бросайте трубку, умоляю вас! Я перед вами стою на коленях.",
  "Don't hang up, I'm begging you! I'm on my knees in front of you.",
  [(568, "не бросайте трубку, умоляю вас"), (569, "перед вами стою на коленях")],
  "Arkady calls back after being cut off (cues 561-567)"),
 ("anya", "Простите меня. Вы самый эффективный!", "Forgive me. You're the most effective of all!",
  [(570, "простите меня"), (573, "Вы самый эффективный")], "the self-insults of cues 570-571 left out"),
 ("governor", "Ну всё. Что ты хочешь?", "All right, that's enough. What do you want?",
  [(576, "Ну все"), (577, "хочешь")], "'Чего хочешь?' -> 'Что ты хочешь?' (standard)"),
 ("anya", "Меня жена бросила. Два пальца сломаны.", "My wife has left me. Two of my fingers are broken.",
  [(581, "Меня жена бросила"), (582, "два пальца сломаны")], ""),
 ("governor", "Правильно.", "Serves you right.", [(584, "Правильно")], "the rest of cue 584 left out"),
 ("anya", "Помогите мне! Я в долгу не останусь.", "Help me! I'll pay you back, I promise.",
  [(587, "Я в долгу не останусь")], "'Помогите мне!' new: plain version of cue 586 (get me out of here)"),
 ("governor", "Ты у Третьякова под личным контролем.", "You're under Tretyakov's personal control.",
  [(590, "Ты у Третьякова под личным контролем")], ""),
 ("anya", "А может быть, вы ему сами позвоните?", "But maybe you could call him yourself?",
  [(593, "а может быть, вы ему сами")], "'наберёте' -> 'позвоните' (plain word)"),
 ("governor", "Позвонить Третьякову? Я что, с ума сошёл?", "Call Tretyakov? What, have I lost my mind?",
  [(594, "Позвонить Третьякову"), (594, "Я что, с ума")], "'что ли' dropped"),
]

OPENER = ("Let's go through the call slowly. Arkady starts very politely, the way you'd speak to a powerful man.")

WALK = [
 (0, None,
  "'Viktor Stepanovich, it's Anikeev calling.' He uses the governor's first name and father's name, the polite "
  "Russian way to address a boss. The verb literally means 'is disturbing you', the humble way to introduce "
  "yourself on the phone. The governor sounds almost cheerful."),
 (1, "Ой, какие люди!",
  "'Well, look who it is!' Word for word, 'oh, what people!', said when someone important, or someone unexpected, "
  "turns up."),
 (1, "Ну, Аркаша, как дела?",
  "'So, Arkasha, how are things?' He uses the childish form of Arkady's name, a little mocking. Arkady doesn't "
  "pretend."),
 (2, None,
  "'Bad. Very bad, Viktor Stepanovich.' Notice he repeats the full polite name, again and again, all through the "
  "call. The governor isn't surprised."),
 (3, None,
  "'I know. So why are you calling me?' The governor says 'you' in the familiar form, while Arkady keeps to the "
  "polite one. That tells you who is the boss here."),
 (4, None,
  "'I really need your help.' Literally, 'to me your help is very needed'. The word for 'needed' is feminine, "
  "to match 'help'. And now the governor shows what he knows."),
 (5, "Как интересно!",
  "'How interesting!' Said coldly, it means quite the opposite. Then comes the accusation."),
 (5, "А в Москве ты про меня гадости рассказываешь.",
  "'And in Moscow you go around saying nasty things about me.' After 'in', Moscow takes the ending for places. "
  "And there's worse."),
 (6, None,
  "'I know what I'm saved as in your phone. Pig.' So word has reached him about that contact name. Arkady denies "
  "everything."),
 (7, None,
  "'That's not true! I have you saved as Dad.' The word he uses is a warm, folksy way to say 'dad', and also "
  "'the big boss'. 'I have' is said as 'at me', the usual Russian pattern. The governor has had enough."),
 (8, None,
  "'I haven't got time.' Literally, 'to me, there's no time'. And he hangs up, back to his judo. "
  "Arkady rings again."),
 (9, "Не бросайте трубку, умоляю вас!",
  "'Don't hang up, I'm begging you!' Literally, 'don't throw down the receiver'. A polite negative command, for "
  "someone you call 'you' formally."),
 (9, "Я перед вами стою на коленях.",
  "'I'm on my knees in front of you.' And in that small room, he really is kneeling. Then flattery."),
 (10, None,
  "'Forgive me. You're the most effective of all!' He even calls himself a young fool, and worse. The word for "
  "'the most' makes any adjective into the very best, here the governor's favourite quality. It works, a little."),
 (11, None,
  "'All right, that's enough. What do you want?' The first two words cut someone off politely, or not so "
  "politely. Arkady lists his troubles: he slept in his clothes on a bare bed frame, and pipe water poured all "
  "over him."),
 (12, None,
  "'My wife has left me. Two of my fingers are broken.' In the first sentence, 'me' comes first and 'wife' comes "
  "after: the word order is free, the endings show who did what. The governor's sympathy is limited."),
 (13, None,
  "'Serves you right.' The word usually means 'correct' or 'right'. Here it's harsh. Arkady swallows it and asks "
  "straight out."),
 (14, None,
  "'Help me! I'll pay you back, I promise.' The second sentence literally says 'I won't stay in debt', a fixed "
  "phrase for 'I'll return the favour'. But there's a problem."),
 (15, None,
  "'You're under Tretyakov's personal control.' Tretyakov is the fearsome official in Moscow. Unless he gives the "
  "go-ahead, the governor won't lift a finger. So Arkady has one more idea."),
 (16, None,
  "'But maybe you could call him yourself?' The word for 'yourself' here is a plural form, to go with the polite "
  "'you'. The governor nearly drops the phone."),
 (17, None,
  "'Call Tretyakov? What, have I lost my mind?' Literally, 'have I gone off my mind'. Even the governor is afraid "
  "of the man in Moscow."),
]

TRANSITION = "Now listen to the whole call once more."

OUTRO = ("After the call, the governor tells his staff not to put Arkady through again, poses for a staged judo "
         "photo with the slogan 'We are all crazy about judo', and back in the flat Slavik proudly calls a friend on "
         "the iPhone, which only needed mobile data switched on. Poor Arkady; see you next time.")
CLOSING = ("governor", "Всё, давай.")
