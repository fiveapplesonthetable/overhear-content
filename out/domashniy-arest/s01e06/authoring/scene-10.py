ID = "domashniy-arest-s01e06-scene-10"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = "Я тебя на понт взяла  (I Called Your Bluff)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina"}
LABELS = {"anya": "Юля", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"

INTRO = ("Last time, at security headquarters, Major Lavrov suggested using short Lieutenant Lyova Sokolov in "
         "schoolboy clothes to provoke Samsonov, though Colonel Mikhail Mikhailovich flatly refused. Meanwhile, "
         "Ilona arrives at the local meatpacking plant to ask its wealthy owner Ignatyev for campaign funding and "
         "unexpectedly finds Samsonov's teenage daughter Yulya working at the reception desk. We'll hear it in "
         "Russian first; don't worry about catching every word.")

STORY = [
 ("ilona", "Юля, а что это мы тут делаем? Почему не в школе?",
  "Yulya, what is it we're doing here? Why aren't you in school?",
  [(360, "Юля, а что это мы тут делаем"), (361, "Почему не в школе")], ""),
 ("anya", "Я здесь работаю. Только, пожалуйста, родителям не говорите.",
  "I work here. Just please don't tell my parents.",
  [(362, "Я здесь работаю. Только"), (362, "пожалуйста, родителям не говорите")], ""),
 ("anya", "Мне деньги очень нужны. На операцию.",
  "I really need the money. For an operation.",
  [(363, "Мне деньги очень нужны"), (364, "На")],
  "cue 365 'На апорт' (на аборт) cleaned to 'На операцию'"),
 ("anya", "Это мои проблемы, я сама их решу.",
  "These are my problems, I'll solve them myself.",
  [(368, "Это мои проблемы, я сама их решу")], ""),
 ("ilona", "Руку дай. Руку дай, говорю!",
  "Give me your hand. Give me your hand, I say!",
  [(369, "Руку дай"), (371, "Руку дай, говорю")], ""),
 ("ilona", "Ты меня за идиотку принимаешь? Никакая ты не беременная!",
  "Do you take me for an idiot? You're not pregnant at all!",
  [(372, "меня за идиотку принимаешь"), (373, "небеременная")],
  "ASR 'Мне какая-то небеременная' -> 'Никакая ты не беременная'"),
 ("anya", "А как вы узнали?",
  "And how did you find out?",
  [(374, "А как вы узнали")], ""),
 ("ilona", "Никак, я тебя на понт взяла. А ты сейчас сама призналась.",
  "No way at all, I called your bluff. And you just confessed yourself.",
  [(375, "Никак, я тебя на понт взяла, а ты сейчас сама призналась")], ""),
 ("ilona", "Ладно, давай выкладывай. В чём дело?",
  "Alright, spill it. What's the matter?",
  [(376, "Ладно, давай"), (376, "В чем дело")],
  "ASR 'выкладываем' -> 'выкладывай'"),
 ("anya", "Мне надоело всё! Родителям на меня плевать.",
  "I'm sick of everything! My parents don't care about me.",
  [(378, "все"), (379, "родителям на меня"), (379, "плевать")],
  "crude 'я задолбала все' -> 'Мне надоело всё'; ASR 'не плевать' -> 'плевать'; 'дебилы' in 380 omitted"),
 ("anya", "Я уехать хочу.",
  "I want to leave.",
  [(381, "я уехать хочу")], ""),
 ("ilona", "Куда?",
  "Where to?",
  [(382, "Куда")], ""),
 ("anya", "В Москву. Я уже всё продумала.",
  "To Moscow. I've already thought everything through.",
  [(383, "В Москву"), (384, "я уже все продумала")], ""),
 ("anya", "Я буду работать официанткой. Буду ходить по кастингам и стану актрисой.",
  "I will work as a waitress. I'll go to auditions and become an actress.",
  [(385, "Я буду работать официанткой, буду ходить по кастингам и стану актрисой")],
  "split into two short sentences"),
 ("ilona", "Ну да, это понятно. Потом разберёмся.",
  "Well yes, that's understandable. We'll sort it out later.",
  [(386, "Ну да, это понятно"), (387, "потом разберемся")], ""),
 ("ilona", "Начальник у себя?",
  "Is the boss in his office?",
  [(388, "у себя")],
  "ASR 'Зачемник' -> 'Начальник'"),
 ("anya", "Да.",
  "Yes.",
  [(389, "Да")], ""),
]

OPENER = ("Let's walk through it. Ilona steps into the meatpacking plant reception and spots sixteen-year-old "
          "Yulya behind the desk during school hours.")

WALK = [
 (0, "Юля, а что это мы тут делаем?",
  "'Yulya, what is it we're doing here?' Notice how adults often say 'we' when catching a child or teenager up to "
  "something."),
 (0, "Почему не в школе?",
  "'Why aren't you in school?' Yulya panics and lowers her voice."),
 (1, "Я здесь работаю.",
  "'I work here,' she admits quietly."),
 (1, "Только, пожалуйста, родителям не говорите.",
  "'Just please don't tell my parents.' And she invents a dramatic excuse."),
 (2, "Мне деньги очень нужны.",
  "'I really need the money.' Literally 'to me money is very needed'."),
 (2, "На операцию.",
  "'For an operation.' She insists she can handle it on her own."),
 (3, None,
  "'These are my problems, I'll solve them myself.' Notice the feminine emphatic pronoun 'myself'. Ilona narrows "
  "her eyes."),
 (4, "Руку дай.",
  "'Give me your hand,' Ilona says."),
 (4, "Руку дай, говорю!",
  "'Give me your hand, I say!' Ilona holds Yulya's wrist for a moment as if checking her pulse, then drops it."),
 (5, "Ты меня за идиотку принимаешь?",
  "'Do you take me for an idiot?'"),
 (5, "Никакая ты не беременная!",
  "'You're not pregnant at all!' Yulya gasps in amazement."),
 (6, None,
  "'And how did you find out?' Ilona smirks."),
 (7, "Никак, я тебя на понт взяла.",
  "'No way at all, I called your bluff.' That colloquial idiom literally means 'I took you on a bluff'."),
 (7, "А ты сейчас сама призналась.",
  "'And you just confessed yourself.' Caught red-handed, Yulya has no choice."),
 (8, "Ладно, давай выкладывай.",
  "'Alright, spill it.' Literally 'come on, lay it out'."),
 (8, "В чём дело?",
  "'What's the matter?' All of Yulya's teenage frustration pours out."),
 (9, "Мне надоело всё!",
  "'I'm sick of everything!' Literally 'to me everything has become tiresome'."),
 (9, "Родителям на меня плевать.",
  "'My parents don't care about me.' Literally 'to my parents it is to spit on me'."),
 (10, None,
  "'I want to leave.' Notice she puts the infinitive 'to leave' before 'want' for emphasis. Ilona asks where."),
 (11, None,
  "'Where to?' Notice the directional 'where to', not 'where at'. Yulya answers proudly."),
 (12, "В Москву.",
  "'To Moscow,' she declares."),
 (12, "Я уже всё продумала.",
  "'I've already thought everything through.' And she shares her grand plan."),
 (13, "Я буду работать официанткой.",
  "'I will work as a waitress.' Both 'work as' and 'become' take the instrumental case."),
 (13, "Буду ходить по кастингам и стану актрисой.",
  "'I'll go to auditions and become an actress.' Having moved to Moscow from Sineozersk herself years ago, Ilona "
  "nods."),
 (14, "Ну да, это понятно.",
  "'Well yes, that's understandable.'"),
 (14, "Потом разберёмся.",
  "'We'll sort it out later.' Right now Ilona has a campaign sponsor to meet."),
 (15, None,
  "'Is the boss in his office?' Literally 'is the boss by himself?'. Yulya nods toward the door."),
 (16, None,
  "'Yes.' And Ilona heads into Ignatyev's office."),
]

TRANSITION = "Now let's hear the whole conversation again from the beginning."

OUTRO = ("So by pretending to read Yulya's pulse, Ilona calls her bluff and learns that Yulya is secretly working "
         "at the meatpacking plant to save money to run away to Moscow and become an actress. Listen for the "
         "instrumental case after 'work as' and 'become'; see you in the next scene.")
CLOSING = ("ilona", "Никак, я тебя на понт взяла.")
