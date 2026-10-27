ID = "domashniy-arest-s01e02-scene-22"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 22
TITLE = "Уволена  (Fired)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "dean": "anja", "student": "angelina"}
LABELS = {"anya": "Марина", "dean": "Эдуард Владимирович", "student": "Студентка"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
SOURCE_NOTE = ("Cues 671-709. Arkady is absent: Marina is the viewpoint character (`anya`, label Марина). The student "
               "she scolds is a girl (the garbled surname in cue 675 is feminine); her name is left out. As in s01e01, "
               "the dean says ты and Marina keeps вы (her ты in cues 680-685 is normalised). Marina's insult "
               "'Мерзавец' (688) and the dean's long phone call (703-709) are left out; the phone call is narrated.")

INTRO = ("Meanwhile, at the university, we're back with Marina, the history lecturer who lives in the communal flat "
         "with her sick son. Last time, the security service picked out people in that flat who might spy on "
         "Arkady, and Marina was on their list. Now she is in the middle of a lecture, and then her dean calls her "
         "out. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Наш с вами город очень старый. Почти четыре века здесь были набеги.",
  "Our town is very old. For almost four centuries there were raids here.",
  [(672, "наш с вами город")],
  "first sentence simplified from cue 672; second sentence new, sums up cues 673-674 (nomad raids for nearly four "
  "centuries)"),
 ("anya", "А ты почему не пишешь?", "And why aren't you writing?",
  [(676, "А ты почему не пишешь")], "the student's surname (garbled, cue 675) left out"),
 ("student", "А у меня диктофон включился.", "Well, my voice recorder is on.",
  [(677, "А у меня диктофон включился")], ""),
 ("anya", "А экзамен вместо тебя диктофон сдавать будет?", "And will the voice recorder take the exam for you?",
  [(678, "а экзамен вместо тебя диктофон сдавать будет")], "'Скажи,' dropped"),
 ("anya", "Так, не шумим. Я скоро вернусь.", "Right, no noise. I'll be back soon.",
  [(679, "Так"), (679, "не шумим. Я скоро вернусь")], "'остаёмся в аудитории' dropped"),
 ("anya", "Вы меня увольняете? Вы серьёзно?", "You're firing me? Are you serious?",
  [(681, "серьезно")], "adapted from cues 680-681 'Ты увольняешь меня? Ты серьёзно?': Marina keeps вы, as in s01e01"),
 ("dean", "Да. Прости.", "Yes. I'm sorry.", [(682, "Да. Прости")], ""),
 ("anya", "За поведение? Вы смеётесь надо мной?", "For my conduct? Are you laughing at me?",
  [(683, "За поведение"), (685, "надо мной")],
  "'несовместимое с педагогической этикой' (683) dropped, the narrator explains it; 'Ты что, издеваешься' (685) -> "
  "'Вы смеётесь' (plain word, polite form)"),
 ("dean", "Мне горько, мне плохо. У меня сердце.", "I feel bitter, I feel awful. I have a bad heart.",
  [(686, "Мне горько, мне плохо"), (687, "У меня сердце")],
  "cue 687 shortened: 'может, не выдержит' (might not take it) dropped"),
 ("anya", "У меня больной ребёнок. Где я найду работу?", "I have a sick child. Where will I find work?",
  [(688, "У меня больной ребенок"), (689, "Где я")],
  "'Мерзавец' (688) dropped; 'Где я устроюсь в Синеозерске?' (689) -> 'Где я найду работу?'"),
 ("dean", "Я уже подумал об этом. Вот.", "I've already thought about that. Here.",
  [(690, "Я уже"), (690, "об этом"), (691, "Вот")],
  "'позаботился' (took care of) -> 'подумал' (thought); the secretary Lenochka (691) left out"),
 ("anya", "Продавец в салоне связи?", "A sales assistant in a phone shop?",
  [(692, "в салоне связи")], "'Продавец-консультант' -> 'Продавец'"),
 ("dean", "А почему нет? Продавец получает больше, чем преподаватель.",
  "Why not? A sales assistant earns more than a lecturer.",
  [(693, "А почему нет"), (694, "получает больше, чем преподаватель")], "'Ну да' and 'между прочим' dropped"),
 ("dean", "Но это только работа. Марина, я люблю тебя.", "But that's only work. Marina, I love you.",
  [(697, "Марина, я люблю тебя")],
  "'Но это только работа' new: plain version of cues 695-696 (he ends only their working relationship)"),
 ("anya", "Как глупо и смешно.", "How stupid and ridiculous.",
  [], "adapted from cue 698 'Какое глупое и смешное...' (the last word is garbled), so not cited"),
 ("dean", "Тебе смешно, а мне очень грустно.", "You find it funny, but I'm very sad.",
  [(699, "тебе смешно"), (699, "а мне"), (699, "грустно")], "'это ... печально и' dropped"),
 ("dean", "Прости, я должен ответить. Да, Аллочка!", "Sorry, I have to answer this. Yes, Allochka!",
  [(700, "Прости"), (701, "я должен ответить"), (702, "Аллочка")],
  "'Это Алла Евгеньевна' dropped; he answers his phone and forgets Marina"),
]

OPENER = ("Let's go back through it slowly. Marina starts with a bit of local history for her students.")

WALK = [
 (0, "Наш с вами город очень старый.",
  "'Our town is very old.' Word for word, 'our-with-you town', a warm way for a teacher to say 'our town, yours "
  "and mine'. There's no word for 'is': in the present tense Russian simply leaves it out."),
 (0, "Почти четыре века здесь были набеги.",
  "'For almost four centuries there were raids here.' Nomad horsemen kept attacking the land where the town now "
  "stands. Then Marina notices a student who isn't taking notes."),
 (1, None,
  "'And why aren't you writing?' She uses the casual 'you' with her student. The student has a modern excuse."),
 (2, None,
  "'Well, my voice recorder is on.' Literally, 'at me the recorder switched itself on': the device does it all by "
  "itself. Marina is not impressed."),
 (3, None,
  "'And will the voice recorder take the exam for you?' The future here is built with the verb 'will be' plus a "
  "verb in its basic form, a very common pattern. Then Marina is called out of the room."),
 (4, None,
  "'Right, no noise. I'll be back soon.' Teachers often give orders with 'we': literally, 'we don't make noise'. "
  "In the dean's office she gets news she didn't expect."),
 (5, None,
  "'You're firing me? Are you serious?' She uses the polite 'you' with her boss, even now. The dean doesn't "
  "argue."),
 (6, None,
  "'Yes. I'm sorry.' The second word is the casual command 'forgive me'. He says it to her with the familiar "
  "'you': in the show they were once a couple."),
 (7, None,
  "'For my conduct? Are you laughing at me?' The official reason sounds grand: conduct unworthy of a teacher. "
  "After 'at', the word for 'me' changes its form. And then the dean says he is the one who suffers."),
 (8, None,
  "'I feel bitter, I feel awful. I have a bad heart.' Russian says 'to me it's bitter, to me it's bad' for how "
  "you feel. Marina has a real problem."),
 (9, None,
  "'I have a sick child. Where will I find work?' To say 'I have', Russian says 'at me there is'. Her son Lyosha "
  "walks on crutches. The dean has an answer ready."),
 (10, None,
  "'I've already thought about that. Here.' He hands her a sheet with job offers. She reads it out."),
 (11, None,
  "'A sales assistant in a phone shop?' The last two words mean a shop that sells phones and contracts. For a "
  "history lecturer it's an insult."),
 (12, "А почему нет?",
  "'Why not?' Literally, 'and why no?' Then he even makes it sound like a promotion."),
 (12, "Продавец получает больше, чем преподаватель.",
  "'A sales assistant earns more than a lecturer.' The word for 'more' and then 'than', just as in English. "
  "Sadly, in the town that is probably true. Then comes the strangest part."),
 (13, None,
  "'But that's only work. Marina, I love you.' He fires her and declares his love in the same breath. Marina "
  "can only laugh."),
 (14, None,
  "'How stupid and ridiculous.' Two short adverbs, both ending in the same sound. He takes it badly."),
 (15, None,
  "'You find it funny, but I'm very sad.' Literally, 'to you it's funny, and to me it's very sad'. The same "
  "pattern as before: the person who feels something takes the form for 'to'. Then his phone rings."),
 (16, None,
  "'Sorry, I have to answer this. Yes, Allochka!' The word for 'have to' is in the masculine form, because the "
  "dean is a man. Allochka is a fond form of the name Alla, a colleague, and Marina is forgotten at once."),
]

TRANSITION = "Here is the whole scene once more, from the lecture to the phone call."

OUTRO = ("So Marina has lost her job, with a sick child to look after and a phone shop as her only offer. Don't "
         "worry if some lines went by fast; you'll know them when you watch. See you next time.")
CLOSING = ("anya", "Всего хорошего!")
