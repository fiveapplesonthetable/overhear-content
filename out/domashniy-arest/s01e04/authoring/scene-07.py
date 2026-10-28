ID = "domashniy-arest-s01e04-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = "Биржа труда  (The Job Centre)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "clerk": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "clerk": "Инспектор", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = ("Cues 178-209 (cue 177 belongs to Pasha's table at the end of Scene 6). Arkady is absent, so Samson is "
               "the viewpoint character (anya, label Самсон). Chain name 'Пятёрочки' (188) -> 'в магазине'; slang "
               "'Да нафиг, Нина, я вафли не буду' (196) -> 'Нина, я вафлей не буду!'; numbers in 199 written out as "
               "words; garbled cues 205 and 209 left out.")

INTRO = ("Back at the employment centre, while Arkady was learning his lawyer's secret and sitting down with "
         "Pasha. Samson and Nina have finally reached the front of the queue, and the tired clerk looks over "
         "Samson's documents to see what jobs she can offer him. We'll hear it in Russian first; don't worry about "
         "catching every word.")

STORY = [
 ("clerk", "Самсонов!",
  "Samsonov!",
  [(178, "Самсонов")], ""),
 ("anya", "Да, здесь. Здравствуйте. Паспорт, трудовая.",
  "Yes, here. Hello. Passport, work book.",
  [(179, "Да, здесь"), (182, "Здравствуйте"), (184, "Паспорт, трудовая")], "'ИНН' in cue 184 dropped"),
 ("clerk", "Здравствуйте. Могу предложить вам две вакансии.",
  "Hello. I can offer you two vacancies.",
  [(183, "Здравствуйте"), (187, "Могу предложить вам две вакансии")], ""),
 ("clerk", "Первая — грузчик в магазине.",
  "The first one is a loader in a shop.",
  [(188, "Первая – грузчик")], "supermarket name 'Пятерочки' -> 'в магазине'"),
 ("nina", "Грузчик не надо. Ему нельзя, у него спина.",
  "No loader. He's not allowed, he has a bad back.",
  [(189, "Грузчик не надо"), (190, "ему нельзя, у него спина")], "'Ну' dropped"),
 ("clerk", "Ну, тогда вторая — промоутер.",
  "Well, then the second one is a promoter.",
  [(192, "Ну, тогда вторая – промоутер")], ""),
 ("nina", "Промоутер — нормально. А что делать надо?",
  "Promoter is fine. And what does he have to do?",
  [(193, "Промоутер, нормально"), (194, "делать надо")], "'А чё' -> 'А что'"),
 ("clerk", "Звать клиентов в детское кафе. В костюме вафельного рожка.",
  "Call customers into a children's café. In a waffle-cone costume.",
  [(195, "клиентов в детское кафе"), (195, "костюме вафельного рожка")],
  "'Зазывать ... в ростовом костюме' simplified to A1 'Звать ... В костюме'"),
 ("anya", "Нина, я вафлей не буду!",
  "Nina, I'm not going to be a waffle!",
  [(196, "Нина, я"), (196, "не буду")], "slang 'Да нафиг' dropped; slip 'вафли' -> instrumental 'вафлей'"),
 ("nina", "А сколько платят?",
  "And how much do they pay?",
  [(197, "А сколько платят")], ""),
 ("clerk", "В будни семьсот рублей. В выходные — полторы тысячи.",
  "On weekdays seven hundred roubles. On weekends, fifteen hundred.",
  [(199, "Будни"), (199, "выходные полторы")],
  "cue 199 ('Будни 700, выходные полторы') written out as Russian words"),
 ("nina", "Мы согласны, оформляйте!",
  "We agree, do the paperwork!",
  [(202, "оформляйте")], "'Ну согласна' -> 'Мы согласны'"),
 ("clerk", "Сейчас выпишу направление. Где я вас могла видеть?",
  "I'll write out a referral right now. Where could I have seen you?",
  [(203, "Сейчас выпишу направление"), (204, "Где я вас могла видеть")], ""),
 ("anya", "Что?",
  "What?",
  [], "standard form of cue 206 'Че?'"),
 ("clerk", "Ну, значит, ошиблась. Всё.",
  "Well, I must have mistaken you for someone else. That's all.",
  [(207, "Ну, значит"), (208, "Все")], "rare 'обозналась' -> 'ошиблась'"),
]

OPENER = ("Let's go back through the scene slowly. The clerk calls out Samson's surname from her desk, and Samson "
          "steps forward with Nina right behind him.")

WALK = [
 (0, None,
  "'Samsonov!' Just his surname, in official style. Samson hurries up to the desk and hands over his papers."),
 (1, None,
  "'Yes, here. Hello. Passport, work book.' In Russia, every employee has an official work book that records every "
  "job they have ever held. The clerk looks at her computer."),
 (2, None,
  "'Hello. I can offer you two vacancies.' After the number 'two', the feminine word 'vacancy' takes the singular "
  "'of' ending. She reads out the first one."),
 (3, None,
  "'The first one is a loader in a shop.' Because the word 'vacancy' is feminine, 'first' has the feminine ending "
  "too. A loader carries heavy boxes, so Nina steps in immediately."),
 (4, "Грузчик не надо.",
  "'No loader.' Literally, 'loader not needed', blunt and practical."),
 (4, "Ему нельзя, у него спина.",
  "'He's not allowed, he has a bad back.' Literally, 'to him it is forbidden, at him is a back'. In Russian, just "
  "saying 'he has a back' or 'he has a heart' means that part of the body gives him trouble. The clerk checks the "
  "second option."),
 (5, None,
  "'Well, then the second one is a promoter.' Another English word borrowed into Russian for someone who hands out "
  "leaflets on the street. Nina likes the sound of that."),
 (6, None,
  "'Promoter is fine. And what does he have to do?' Literally, 'what to do is necessary?'. The clerk reads out the "
  "job description without blinking."),
 (7, "Звать клиентов в детское кафе.",
  "'Call customers into a children's café.' Because 'customers' are people, the accusative plural looks just like "
  "the 'of' form."),
 (7, "В костюме вафельного рожка.",
  "'In a waffle-cone costume.' Literally, 'in a costume of a waffle horn'. Picture big, burly Samson dressed as an "
  "ice-cream cone. Samson is outraged."),
 (8, None,
  "'Nina, I'm not going to be a waffle!' After 'will not be', the noun 'waffle' goes into the instrumental case. "
  "Nina doesn't care about his pride; she wants to know the pay."),
 (9, None,
  "'And how much do they pay?' Third person plural with no subject: 'how much do they pay?'."),
 (10, "В будни семьсот рублей.",
  "'On weekdays seven hundred roubles.' Notice the word order: 'weekdays' comes first, and 'roubles' finishes the sentence."),
 (10, "В выходные — полторы тысячи.",
  "'On weekends, fifteen hundred.' Literally, 'one and a half thousands'. That settles it for Nina."),
 (11, None,
  "'We agree, do the paperwork!' The plural short form 'agreed' covers both of them, whether Samson likes it or "
  "not. As the clerk writes the slip, she looks closely at Samson's face."),
 (12, "Сейчас выпишу направление.",
  "'I'll write out a referral right now.' Here 'right now' sets up the idea, while 'referral slip' comes at the end for emphasis."),
 (12, "Где я вас могла видеть?",
  "'Where could I have seen you?' Remember the viral video on the morning news: half the country has already seen "
  "Samson throwing the mayor out the window. Samson just stares at her."),
 (13, None,
  "'What?' the speaker puts 'what' up front so the listener immediately catches the tone, followed by 'what'."),
 (14, None,
  "'Well, I must have mistaken you for someone else. That's all.' The feminine past verb ends in 'a' before the "
  "reflexive ending because the clerk is a woman."),
]

TRANSITION = "Now let's listen to the whole conversation at the job centre again."

OUTRO = ("So Samson is signed up to stand on the street in a giant waffle-cone costume, and the clerk almost "
         "recognises him from the viral video. Next we return to Arkady and Pasha at the investigator's table; see "
         "you then.")
CLOSING = ("anya", "Нина, я вафлей не буду!")
