ID = "domashniy-arest-s01e03-scene-23"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 23
TITLE = "Скальпель медсестры  (The Nurse's Scalpel)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "nina": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Swearing and crude lines cleaned: 'бабки' (756) -> 'деньги', 'разводят' (759) -> 'обманывают', "
               "'дебил' (757, 778, 784) -> dropped / 'глупый', 'Блин' (781) dropped, crude 802 ('обоссался от "
               "страха') and 814 ('ты дура') dropped. Transcription slip 'Очконавт' (796) -> 'очкарик'.")

INTRO = ("Back in the communal flat, Arkady is still tied to a chair in front of Samson and Nina. Last time, at "
         "security headquarters, the chief told Marina that Arkady would be away at court for two hours, not knowing "
         "that Arkady hasn't left the flat at all. Here, Samson tries to look scary so Arkady will tell them where "
         "the money is, but things quickly go wrong. We'll hear it in Russian first; don't worry about catching "
         "every word.")

STORY = [
 ("samson", "Ну что, успокоился? Где деньги?",
  "Well, have you calmed down? Where's the money?",
  [(754, "Успокоился"), (756, "Где")], "'Ну что' added; slang 'бабки' -> 'деньги'"),
 ("anya", "Я тебе говорю, у меня нет никаких денег. Вас обманывают!",
  "I'm telling you, I don't have any money. They're tricking you!",
  [(758, "Я тебе говорю, у меня нет никаких денег"), (759, "Вас")],
  "slang 'разводят' -> 'обманывают'; insult in 757 dropped"),
 ("samson", "Ну всё. Я сейчас сжимаю палец!",
  "Right, that's it. I'm squeezing your finger right now!",
  [(760, "Ну все"), (765, "Я сейчас сжимаю"), (766, "палец")], ""),
 ("anya", "Нет, не надо! Не надо, мне больно!",
  "No, don't! Don't, it hurts!",
  [(762, "Нет, не надо"), (763, "Не надо мне больно")], ""),
 ("samson", "Ну всё, хватит. Я так не могу.",
  "Okay, that's enough. I can't do this.",
  [(770, "Ну всё")], "'хватит. Я так не могу' sums up Samson letting go and sitting down in 767-770"),
 ("nina", "Ваня, ты что? Он только начал бояться, а ты остановился!",
  "Vanya, what is wrong with you? He just started getting scared, and you stopped!",
  [(779, "Он только начал бояться, а ты остановился")],
  "cue 778 'Ты чё дебил что ли, Вань?' -> 'Ваня, ты что?'"),
 ("samson", "Ну что мне делать? Мы договорились его просто напугать!",
  "Well, what am I supposed to do? We agreed to just scare him!",
  [(781, "ну что мне"), (782, "Мы договорились его просто напугать")],
  "'Блин' dropped; 'палец ему откусить что ли' -> 'делать'"),
 ("nina", "Ваня, ты глупый? Зачем ты сейчас это при нём сказал?",
  "Vanya, are you stupid? Why did you just say that in front of him?",
  [(785, "зачем ты сейчас это при нем сказал")],
  "cue 784 'Вань, ты чё дебил?' -> 'Ваня, ты глупый?'"),
 ("nina", "Теперь он уже всё понял!",
  "Now he has worked everything out!",
  [(786, "Теперь он уже все понял")], ""),
 ("anya", "Я всё понял! Развяжите меня, пожалуйста.",
  "I get it now! Untie me, please.",
  [(789, "Я все понял"), (791, "Развяжите меня, пожалуйста")], ""),
 ("anya", "Самсон, я устал. Мне сегодня ещё в суд идти!",
  "Samson, I'm tired. I still have to go to court today!",
  [(793, "Самсон"), (793, "я устал"), (804, "мне сегодня еще в суд идти")], ""),
 ("nina", "Послушай ты, очкарик! Если он тряпка, то я нет.",
  "Listen here, four-eyes! If he's a pushover, I'm not.",
  [(796, "Послушай ты"), (797, "Если он тряпка"), (798, "то я нет")],
  "cue 796 'Очконавт' is a transcription slip for 'очкарик'"),
 ("nina", "Я медицинский работник. Вот это скальпель.",
  "I'm a medical worker. This right here is a scalpel.",
  [(800, "Я медицинский работник"), (808, "Вот это скальпель")], ""),
 ("nina", "Я тебе сейчас отрежу ухо!",
  "I'm going to cut off your ear right now!",
  [(809, "я тебе сейчас отрежу ухо")], ""),
 ("anya", "Ой, два лузера! Быстро развязали меня!",
  "Oh, two losers! Untie me, fast!",
  [(813, "Ой, два лузера"), (803, "быстро развязали меня")],
  "crude 802 and insult in 814 dropped"),
 ("anya", "Что это? Это кровь?",
  "What is this? Is this blood?",
  [(817, "Что это"), (818, "Это кровь")], ""),
]

OPENER = ("Let's go back through the scene. Arkady has stopped shouting for the neighbours, and Samson asks if he "
          "is ready to talk.")

WALK = [
 (0, None,
  "'Well, have you calmed down? Where's the money?' The verb has the masculine past ending plus the reflexive "
  "tail at the end. Arkady gives the same answer as before."),
 (1, "Я тебе говорю, у меня нет никаких денег.",
  "'I'm telling you, I don't have any money.' After 'there isn't', both 'any' and 'money' take the genitive "
  "plural ending. Then he warns both of them."),
 (1, "Вас обманывают!",
  "'They're tricking you!' Literally 'they are deceiving you', using the third-person plural with no subject "
  "to mean 'Pasha is playing you'. Samson decides to act tough and grabs Arkady's bandaged finger."),
 (2, None,
  "'Right, that's it. I'm squeezing your finger right now!' He barely touches it, but Arkady screams anyway."),
 (3, None,
  "'No, don't! Don't, it hurts!' Literally 'to me it is painful'. That is enough to make big Samson lose his "
  "nerve."),
 (4, None,
  "'Okay, that's enough. I can't do this.' He lets go at once and sits down, looking upset himself. Nina is "
  "furious with her husband."),
 (5, "Ваня, ты что?",
  "'Vanya, what is wrong with you?' She tells him he didn't even squeeze Arkady's finger."),
 (5, "Он только начал бояться, а ты остановился!",
  "'He just started getting scared, and you stopped!' Both verbs are masculine past forms, because both Arkady "
  "and Samson are men. And then Samson blurts out the one thing he shouldn't say."),
 (6, "Ну что мне делать?",
  "'Well, what am I supposed to do?' Literally 'what to me to do?'."),
 (6, "Мы договорились его просто напугать!",
  "'We agreed to just scare him!' He says it right in front of the man tied to the chair. Nina can't believe "
  "her ears."),
 (7, "Ваня, ты глупый?",
  "'Vanya, are you stupid?' A short masculine adjective."),
 (7, "Зачем ты сейчас это при нём сказал?",
  "'Why did you just say that in front of him?' Notice the little preposition before 'him': it means 'in the "
  "presence of', 'in front of'. And Nina knows the game is up."),
 (8, None,
  "'Now he has worked everything out!' Literally 'now he already everything understood'. Arkady's fear vanishes "
  "on the spot."),
 (9, "Я всё понял!",
  "'I get it now!' The exact same masculine past verb: 'I understood everything'."),
 (9, "Развяжите меня, пожалуйста.",
  "'Untie me, please.' He starts politely, addressing the two of them with the plural command. When they don't "
  "move, he gets impatient."),
 (10, "Самсон, я устал.",
  "'Samson, I'm tired.' Literally 'I got tired'."),
 (10, "Мне сегодня ещё в суд идти!",
  "'I still have to go to court today!' Remember, the evening hearing with Judge Berg is today. That's when "
  "Nina steps forward."),
 (11, "Послушай ты, очкарик!",
  "'Listen here, four-eyes!' She uses Samson's old schoolyard nickname for Arkady, from the word for glasses."),
 (11, "Если он тряпка, то я нет.",
  "'If he's a pushover, I'm not.' The word for 'pushover' literally means 'a rag'—someone soft and spineless. "
  "And Nina reminds him of her job."),
 (12, "Я медицинский работник.",
  "'I'm a medical worker.' She works as a nurse at the hospital, and she has brought something from work."),
 (12, "Вот это скальпель.",
  "'This right here is a scalpel.' She holds up a real surgical blade in front of Arkady's face."),
 (13, None,
  "'I'm going to cut off your ear right now!' Literally 'to you right now I will cut off the ear'. Arkady still "
  "thinks they are bluffing."),
 (14, "Ой, два лузера!",
  "'Oh, two losers!' He uses the borrowed English word 'loser' with a Russian plural ending after 'two'."),
 (14, "Быстро развязали меня!",
  "'Untie me, fast!' Here he uses the plural past tense as a barked order—a bossy Russian way to say 'get it "
  "done this instant!'. As he jerks his head and mocks her, the scalpel slips and nicks his ear."),
 (15, None,
  "'What is this? Is this blood?' He feels something warm on his neck, and all three of them freeze."),
]

TRANSITION = "Let's listen to the whole scene again from the beginning."

OUTRO = ("So Samson gave the bluff away, and then Nina's scalpel drew real blood from Arkady's ear. Next time we'll "
         "check in on the surveillance post across the courtyard, and then see how Samson reacts to the blood.")
CLOSING = ("anya", "Это кровь?")
