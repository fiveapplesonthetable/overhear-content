ID = "domashniy-arest-s01e02-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 9
TITLE = "Предложение Паши  (Pasha's Offer)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja"}
LABELS = {"anya": "Аркадий", "pasha": "Паша"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"

INTRO = ("Last time, Samson told Nina he would run for mayor in Arkady's place, and she just laughed at him. "
         "Meanwhile, the guards have brought Arkady to the town hall, to his old deputy Pasha, who now sits in the "
         "mayor's chair and wants something from him. We'll hear it in Russian first; don't worry about catching "
         "every word.")

STORY = [
 ("anya", "Паша, что всё это значит?", "Pasha, what does all this mean?", [],
  "Arkady has just been dragged in by the guards"),
 ("pasha", "Понимаешь, Аркаша, мы все скидываемся на этот кластер. Мне москвичам сегодня надо отдать сто пятьдесят.",
  "You see, Arkasha, we're all chipping in for this cluster. I have to give the Moscow people a hundred and fifty today.",
  [(230, "Понимаешь"), (230, "мы все скидываемся на этот кластер"), (231, "Мне москвичам сегодня")],
  "'Аркашенька' -> 'Аркаша'; cue 231 '150 отдавать надо' -> 'надо отдать сто пятьдесят'"),
 ("anya", "Ну и что?", "So what?", [], "Arkady's shrug"),
 ("pasha", "А без твоих сорока у меня только сто десять. Я на твои деньги рассчитывал.",
  "And without your forty I've only got a hundred and ten. I was counting on your money.",
  [(232, "А без твоих"), (233, "Я на твои деньги рассчитывал")], "'только' added"),
 ("anya", "А ты в следующий раз на мои деньги не рассчитывай. И всё будет хорошо.",
  "Well, next time don't count on my money. And everything will be fine.",
  [(234, "А ты в следующий раз на мои деньги не рассчитывай"), (235, "И все будет хорошо")], ""),
 ("anya", "Ты что, мафия? Ты же завхоз в третьем поколении.",
  "What are you, the mafia? You're a supply manager, third generation.",
  [(237, "Ты же завхоз в третьем поколении")],
  "cue 236 'Чего ты из себя мафиози строишь?' (why are you playing the mafia boss) simplified to 'Ты что, мафия?'"),
 ("pasha", "Значит, предложение такое. Ты мне говоришь, где твои сорок миллионов.",
  "So, here's the offer. You tell me where your forty million is.",
  [(240, "Значит, предложение такое"), (241, "Ты мне говоришь, где твои")], "slang 'лямов' -> 'миллионов'"),
 ("anya", "А ты мне что?", "And what do I get from you?", [], "a link between the two halves of cue 241"),
 ("pasha", "А я тебе делаю условный срок. Плюс ты забираешь все деньги Вики.",
  "And I get you a suspended sentence. Plus you take all of Vika's money.",
  [(241, "я тебе делаю"), (242, "Плюс ты забираешь все")],
  "slang 'условку' -> 'условный срок', 'бабки, которые в комоде лежат у Вики' -> 'деньги Вики'; "
  "cue 243 (Vika herself thrown in) left out"),
 ("anya", "Предложение, конечно, хорошее. Знаешь, что я тебе скажу?",
  "It's a good offer, of course. Do you know what I'll tell you?",
  [(245, "Предложение, конечно, хорошее"), (246, "Знаешь, что я тебе скажу")], ""),
 ("pasha", "Что?", "What?", [(247, "Что")], ""),
 ("anya", "Я выйду отсюда, меня оправдают. Аракелян заявление заберёт.",
  "I'll get out of here, they'll acquit me. Arakelyan will withdraw his statement.",
  [(249, "Я выйду отсюда, меня оправдают"), (250, "заявление заберет")],
  "the cue's 'Ракелян' is a slip for Arakelyan"),
 ("anya", "Ай! Больно, больно!", "Ow! It hurts, it hurts!", [(251, "больно, больно")],
  "'Ай!' added; the guards twist his hand"),
 ("pasha", "Значит так, срок у тебя до вечера, понял?", "Right then, you've got until tonight, understood?",
  [(252, "Значит так, срок у тебя до вечера, понял")], "'Аркадий Борисович' moved to the goodbye"),
 ("anya", "А если нет?", "And if not?", [],
  "a simpler stand-in for cue 254 'А если не приму?' (and if I don't [make that decision]?)"),
 ("pasha", "Тогда ребята с тобой поработают. До свидания, Аркадий Борисович.",
  "Then the boys will have a little word with you. Goodbye, Arkady Borisovich.",
  [(256, "с тобой поработают"), (259, "До свидания, Аркадий Борисович")],
  "cue 255 ('then we move on to physical threats') folded into 'Тогда'"),
 ("anya", "До свидания.", "Goodbye.", [(260, "До свидания")], ""),
]

OPENER = ("Let's go back through it. Arkady stands in Pasha's office, between two guards, and he wants an "
          "explanation.")

WALK = [
 (0, None,
  "'Pasha, what does all this mean?' Word for word: 'what all this means'. He still talks to Pasha as his junior, with the "
  "informal 'you'. Pasha explains, very sweetly."),
 (1, "Понимаешь, Аркаша, мы все скидываемся на этот кластер.",
  "'You see, Arkasha, we're all chipping in for this cluster.' The cluster is the big industrial project with "
  "partners from Moscow. The verb means 'to chip in', when everyone puts money together. Then the sum."),
 (1, "Мне москвичам сегодня надо отдать сто пятьдесят.",
  "'I have to give the Moscow people a hundred and fifty today.' He means a hundred and fifty million roubles. "
  "'I have to' is literally 'to me it's necessary'. Arkady doesn't care."),
 (2, None,
  "'So what?' Three small words, and a very handy shrug. Pasha does the maths."),
 (3, "А без твоих сорока у меня только сто десять.",
  "'And without your forty I've only got a hundred and ten.' 'Without' is followed by the form that means 'of': "
  "your forty. So that's where Arkady's missing forty million come in."),
 (3, "Я на твои деньги рассчитывал.",
  "'I was counting on your money.' A masculine past form, because Pasha is a man. Arkady gives him some advice."),
 (4, "А ты в следующий раз на мои деньги не рассчитывай.",
  "'Well, next time don't count on my money.' The same verb, now as a command with 'not': 'don't count'. "
  "Negative commands are almost always made from this kind of verb, the imperfective one."),
 (4, "И всё будет хорошо.",
  "'And everything will be fine.' A friendly phrase used as a weapon. Then he laughs at Pasha's tough-guy act."),
 (5, None,
  "'What are you, the mafia? You're a supply manager, third generation.' The little word after 'you' means 'after "
  "all'. A supply manager runs a storeroom: Arkady is saying Pasha is no gangster, just a petty official from a "
  "family of them. Pasha gets down to business."),
 (6, "Значит, предложение такое.",
  "'So, here's the offer.' Literally 'so, the offer is such'."),
 (6, "Ты мне говоришь, где твои сорок миллионов.",
  "'You tell me where your forty million is.' He uses the present tense for a plan, just as English can: "
  "'you tell me, I do this'. Arkady wants to hear his part."),
 (7, None,
  "'And what do I get from you?' Literally 'and you to me what?'. Russian is happy to drop the verb altogether."),
 (8, "А я тебе делаю условный срок.",
  "'And I get you a suspended sentence.' That means no prison, as long as you behave."),
 (8, "Плюс ты забираешь все деньги Вики.",
  "'Plus you take all of Vika's money.' 'Vika's' is just her name with the 'of' ending. Remember, the cash at "
  "home is in Vika's hands, and Pasha is the one who is with her now. Arkady pretends to think about it."),
 (9, "Предложение, конечно, хорошее.",
  "'It's a good offer, of course.' The word in the middle means 'of course'. But you can hear a 'but' coming."),
 (9, "Знаешь, что я тебе скажу?",
  "'Do you know what I'll tell you?' 'I'll tell' is perfective, so it points to the future. Pasha takes the bait."),
 (10, None,
  "'What?' Just one word."),
 (11, "Я выйду отсюда, меня оправдают.",
  "'I'll get out of here, they'll acquit me.' Both verbs are perfective futures. The second has no subject: "
  "'they'll acquit me', meaning the court."),
 (11, "Аракелян заявление заберёт.",
  "'Arakelyan will withdraw his statement.' The verb comes last here, for emphasis. Arakelyan is the businessman who handed him the bribe. Arkady thinks "
  "he can make him change his story. At that, a guard twists his hand."),
 (12, None,
  "'Ow! It hurts, it hurts!' A word you'll hopefully never need. Pasha gives him a deadline."),
 (13, None,
  "'Right then, you've got until tonight, understood?' 'Until' is followed by the 'of' form of 'evening'. And Arkady "
  "asks the obvious question."),
 (14, None,
  "'And if not?' Short and defiant."),
 (15, "Тогда ребята с тобой поработают.",
  "'Then the boys will have a little word with you.' Literally 'will work with you': a polite way to threaten a "
  "beating. And then, suddenly very formal."),
 (15, "До свидания, Аркадий Борисович.",
  "'Goodbye, Arkady Borisovich.' First name plus father's name: the respectful way. Coming from Pasha now, "
  "it's pure mockery. Arkady answers the only way he can."),
 (16, None,
  "'Goodbye.' The standard polite goodbye. Literally 'until we see each other again'."),
]

TRANSITION = "Let's listen to the whole conversation again from the top."

OUTRO = ("So Arkady has until evening to give up his forty million, and he isn't giving in. Listen for the deal "
         "and the deadline when you watch; see you next time.")
CLOSING = ("anya", "Ну, Паша, погоди!")
