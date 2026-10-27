ID = "domashniy-arest-s01e04-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 30
TITLE = "Ещё немного времени  (A Little More Time)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "stepan": "angelina"}
LABELS = {"anya": "Фёдор Григорьевич", "pasha": "Паша", "stepan": "Степан Геннадьевич"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1135-1170. Arkady is absent: the calm Moscow partner Fyodor Grigoryevich is `anya` (label Фёдор "
    "Григорьевич), Pasha on the phone is `pasha` (anja, label Паша), and angry Stepan Gennadyevich is `stepan` "
    "(angelina, label Степан Геннадьевич). Slang 'Вруби ... фон' (1136) -> 'Включи ... шум'; 'прикалываешься' (1138) "
    "-> 'шутишь'; 'Токийская биржа' (1137) -> 'Биржа в Токио'; 'Синьозерск наверху' (1144) -> 'Синеозерск ... в "
    "Москве'; 'готовы дать вам отсрочку' (1145) -> 'даём вам ещё немного времени'; 'средства' (1146) -> 'деньги'. "
    "Cues 1152-1170 are the closing song, omitted from story lines."
)

INTRO = (
    "Late at night in Moscow, inside a black car. Last time, Samson and Nina raced away from a police car through "
    "the courtyards of Sineozersk and launched their test-drive SUV over a ramp straight through the dealership "
    "window. Meanwhile, the two Moscow partners from the cluster deal, Stepan Gennadyevich and Fyodor Grigoryevich, "
    "decide to phone Pasha Osipenko. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("stepan", "А что с Осипенко?", "And what about Osipenko?",
  [(1135, "А что с Осипенко")], ""),
 ("stepan", "Мы ему только три дня дали.", "We only gave him three days.",
  [(1135, "Мы ему только три дня дали")], ""),
 ("anya", "Включи какой-нибудь шум.", "Put on some background noise.",
  [(1136, "какой-нибудь")], "slang 'Вруби ... фон' -> 'Включи ... шум'"),
 ("stepan", "Биржа в Токио подойдёт?", "Will the stock exchange in Tokyo do?",
  [(1137, "биржа подойдет")], "'Токийская биржа' -> 'Биржа в Токио'"),
 ("anya", "Ты что, шутишь? Включи аэропорт!", "Are you joking? Put on the airport!",
  [(1138, "Ты что"), (1139, "Аэропорт")], "slang 'прикалываешься' -> 'шутишь'; 'Включи' added"),
 ("pasha", "Да, я слушаю.", "Yes, I'm listening.",
  [(1140, "Да, я слушаю")], ""),
 ("anya", "Алло, Павел Юрьевич, это Фёдор Григорьевич.", "Hello, Pavel Yuryevich, this is Fyodor Grigoryevich.",
  [(1141, "Алло, Павел Юрьевич, Федор Григорьевич")], "'беспокоит' -> 'это'"),
 ("anya", "У меня хорошие новости для вас.", "I have good news for you.",
  [(1143, "новости для вас")], "'В общем, я приятные' -> 'У меня хорошие'"),
 ("anya", "Синеозерск понравился в Москве больше других мест.",
  "In Moscow they liked Sineozersk more than other places.",
  [(1144, "понравился больше других мест")], "mistranscribed 'Синьозерск наверху' -> 'Синеозерск ... в Москве'"),
 ("anya", "Мы даём вам ещё немного времени.", "We are giving you a little more time.",
  [(1145, "мы"), (1145, "вам")], "'Поэтому мы готовы дать вам отсрочку' -> 'Мы даём вам ещё немного времени'"),
 ("anya", "И мы начинаем готовить документы. Собирайте деньги!",
  "And we're starting to prepare the documents. Gather the money!",
  [(1145, "готовить документы"), (1146, "Собирайте")], "'средства' -> 'деньги'"),
 ("pasha", "Спасибо большое, я всё понял!", "Thank you very much, I understood everything!",
  [(1147, "Спасибо большое, я понял")], "'всё' added"),
 ("anya", "Ну тогда всё, до связи.", "All right then, we'll be in touch.",
  [(1148, "Ну тогда все")], "'на связи' -> 'до связи'"),
 ("stepan", "С женой Аникеева так просто не получится.", "It won't be that easy with Anikeev's wife.",
  [(1149, "с женой так просто не получится")], "'Аникеева' added for clarity"),
 ("anya", "Ладно, утром позвоню ей. Поехали спать.", "All right, I'll call her in the morning. Let's go to sleep.",
  [(1150, "Ладно, утром позвоню ей"), (1151, "Поехали спать")], ""),
]

OPENER = "Let's walk through it slowly. The two Moscow partners are sitting in their car at night."

WALK = [
 (0, None,
  "'And what about Osipenko?' Osipenko is Pasha's surname; Ukrainian surnames ending in '-ko' never change their "
  "ending after a preposition. Stepan reminds his partner of the deadline."),
 (1, None,
  "'We only gave him three days.' Remember from Episode 2 that these two men aren't real government officials at "
  "all, but conmen after Arkady's millions. Fyodor Grigoryevich gets ready to call Pasha."),
 (2, None,
  "'Put on some background noise.' They play fake sound effects on a tablet so Pasha thinks they are busy men "
  "travelling the world. Stepan scrolls through his sound files."),
 (3, None,
  "'Will the stock exchange in Tokyo do?' The verb literally means 'will it come up and fit?'. Fyodor rolls his "
  "eyes."),
 (4, None,
  "'Are you joking? Put on the airport!' With airport announcements playing in the background, he dials Pasha's "
  "number, and Pasha answers right away."),
 (5, None,
  "'Yes, I'm listening.' This is a standard Russian way to answer the phone. Fyodor uses his smooth, official "
  "voice."),
 (6, None,
  "'Hello, Pavel Yuryevich, this is Fyodor Grigoryevich.' Both men address each other by first name and patronymic."),
 (7, None,
  "'I have good news for you.' In Russian, 'news' is plural here, 'good news-items'. And he explains."),
 (8, None,
  "'In Moscow they liked Sineozersk more than other places.' Literally, 'Sineozersk pleased in Moscow more than "
  "other places'. After 'more than', 'other places' takes the plural 'of' ending. So he offers Pasha a favour."),
 (9, None,
  "'We are giving you a little more time.' After 'a little', the word for 'time' takes its special 'of' form. And he "
  "hooks Pasha deeper."),
 (10, "И мы начинаем готовить документы.",
  "'And we're starting to prepare the documents.' After 'start', Russian uses the imperfective infinitive."),
 (10, "Собирайте деньги!",
  "'Gather the money!' A polite plural command. Pasha is thrilled."),
 (11, None,
  "'Thank you very much, I understood everything!' Literally, 'a big thank-you'. Fyodor wraps up the call."),
 (12, None,
  "'All right then, we'll be in touch.' He hangs up and turns off the airport noise. Stepan is thinking about "
  "Arkady's wife Vika, who actually has the money in her name."),
 (13, None,
  "'It won't be that easy with Anikeev's wife.' Literally, 'with the wife of Anikeev so simply it will not turn "
  "out'. Fyodor isn't worried."),
 (14, None,
  "'All right, I'll call her in the morning. Let's go to sleep.' And with that, the two conmen drive off into the "
  "night."),
]

TRANSITION = "Let's hear the whole scene once more, from the first line."

OUTRO = (
    "So while Ilona joins Arkady and Samson crashes through the car showroom, the Moscow conmen prepare to call Vika "
    "in the morning. That finishes Episode 4, with a Russian folk-style song about a nightingale at the close. "
    "Well done, and see you in Episode 5."
)
CLOSING = ("anya", "Поехали спать!")
