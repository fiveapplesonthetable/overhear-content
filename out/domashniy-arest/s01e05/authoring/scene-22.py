ID = "domashniy-arest-s01e05-scene-22"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 22
TITLE = "Папа, тебя обманывают!  (Dad, They're Fooling You!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "yulia": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "yulia": "Юля", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
SOURCE_NOTE = ("Cues 844-882. Arkady is absent -> anya = Самсон (alisa). Golovkin's single line in 850 is narrated "
               "within the three-role limit. Romantic/slang lines in 850-872 are kept light and clean for A1: 'Данчок, "
               "есть ли какое-нибудь романтическое местечко?' (848-849) -> 'Даня, есть ли здесь тихая комната?', "
               "'музлончик прищучит' (864) -> 'музыку найдём', 'обалдёшь' (868) -> 'Ты что', 'ты меня хочешь' (870) -> "
               "'Ты со мной'. Yulia's slang in 875-881 ('алкаш', 'разводят', 'бухой вписался', 'по телеку... гоняют', "
               "'заикала') is rendered in clean A1 Russian ('пьяница', 'обманывают', 'пьяный врезался', 'по телевизору "
               "... показывают').")

INTRO = ("At Golovkin's country house a little later. Still believing that he is a town hero who saved blind people from "
         "a gas explosion, Samson leads Nina upstairs to a quiet room, where he happens to switch on an old radio. When "
         "smoke from the oven brings them rushing back down to the kitchen, teenage Yulia finally snaps and tells her "
         "father the truth. We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "А что у нас полагается героям? — Чего?",
  "So what do heroes get around here? — What?",
  [(844, "А что у нас полагается героям"), (845, "Чего")], ""),
 ("anya", "Знаешь, что полагается! Даня, есть ли здесь тихая комната?",
  "You know what's owed! Danya, is there a quiet room here?",
  [(847, "Знаешь"), (847, "полагается"), (849, "есть ли")],
  "'Данчок, есть ли какое-нибудь романтическое местечко?' -> 'Даня, есть ли здесь тихая комната?'"),
 ("nina", "Ванюш, ну ты слабенький ещё. Может, не надо?",
  "Vanyush, come on, you're still weak. Maybe we shouldn't?",
  [(851, "Ванюш, ну ты слабенький еще"), (852, "может, не надо")], ""),
 ("anya", "Пойдём, слабенький! Я тебе покажу, какой я слабенький!",
  "Let's go, weakling! I'll show you how weak I am!",
  [(855, "Пойдем, слабенький"), (857, "Я тебе покажу, какой я слабенький")], ""),
 ("nina", "Вань, посмотри! — Смотри, работает! Сейчас музыку найдём.",
  "Vanya, look! — Look, it works! We'll find some music right now.",
  [(861, "Вань"), (862, "Посмотри"), (863, "Смотри"), (864, "Сейчас"), (865, "Работает")],
  "slang 'музлончик прищучит' -> 'музыку найдём'"),
 ("anya", "И сразу об Иване Самсонове!",
  "And right away it's about Ivan Samsonov!",
  [(867, "И сразу об Иване Самсонове")],
  "trailing 'который стал...' dropped as Nina switches off the radio"),
 ("nina", "Ты что, это же чужой! Ты со мной или хочешь слушать новости?",
  "What are you doing, that's someone else's! Are you with me or do you want to listen to the news?",
  [(869, "Это же чужой"), (870, "ты"), (870, "хочешь"), (871, "Или слушать новости")],
  "'ты меня хочешь' -> 'Ты со мной' for clean A1"),
 ("nina", "Представляешь, в духовке забыли! Юль, выйди.",
  "Can you believe it, they forgot it in the oven! Yul, step out.",
  [(873, "Представляешь, в духовке забыли"), (874, "Юль, выйди")], ""),
 ("yulia", "Папа, ты пьяница! Тебя просто здесь все обманывают целый день!",
  "Dad, you're a drunkard! Everyone here has just been fooling you all day!",
  [(875, "Папа, ты"), (876, "тебя просто здесь все"), (876, "целый день")],
  "'алкаш' -> 'пьяница'; 'разводят' -> 'обманывают'"),
 ("yulia", "Ты просто пьяный врезался в здание слепых! Ты не понимаешь?",
  "You just crashed into the building for the blind while drunk! Don't you understand?",
  [(877, "Ты просто"), (877, "в здание слепых"), (877, "ты не понимаешь")],
  "'бухой вписался' -> 'пьяный врезался'; split into two short sentences"),
 ("yulia", "Тебя по телевизору целый день показывают!",
  "They've been showing you on TV all day!",
  [(878, "Тебя по"), (878, "целый день")],
  "'по телеку... гоняют' -> 'по телевизору... показывают'"),
 ("yulia", "Мы выяснили это всё? Можем ехать домой?",
  "Have we sorted all this out? Can we go home?",
  [(879, "Мы выяснили это все"), (880, "Можем ехать домой")], ""),
 ("yulia", "И вашу посуду я тоже мыть больше не буду!",
  "And I won't be washing your dishes anymore either!",
  [(882, "И вашу посуду я тоже мыть больше не буду")], ""),
]

OPENER = "Let's go through the scene line by line. First, Samson grins at his wife Nina, expecting a hero's reward."

WALK = [
 (0, None,
  "'So what do heroes get around here? — What?' The reflexive verb literally means 'what is due to heroes among us'."),
 (1, None,
  "'You know what's owed! Danya, is there a quiet room here?' Golovkin gladly points Samson and Nina toward a bedroom upstairs."),
 (2, None,
  "'Vanyush, come on, you're still weak. Maybe we shouldn't?' Notice the affectionate diminutive of 'sickly' or 'weak'."),
 (3, None,
  "'Let's go, weakling! I'll show you how weak I am!' Samson marches her up the stairs."),
 (4, None,
  "'Vanya, look! — Look, it works! We'll find some music right now.' Samson turns on an old radio receiver in the bedroom, and a news announcer's voice comes through the speaker."),
 (5, None,
  "'And right away it's about Ivan Samsonov!' Notice how the preposition 'about' becomes two letters before a word starting with a vowel."),
 (6, None,
  "'What are you doing, that's someone else's! Are you with me or do you want to listen to the news?' Panicked that Samson will hear what he really did, Nina snaps the radio off. Just then, smoke drifts up from the kitchen oven and they rush back downstairs."),
 (7, None,
  "'Can you believe it, they forgot it in the oven! Yul, step out.' In the kitchen, sixteen-year-old Yulia is still standing at the sink with a stack of dirty plates. Being told to leave the room is the last straw."),
 (8, None,
  "'Dad, you're a drunkard! Everyone here has just been fooling you all day!' Yulia throws down her dish sponge and blurts out the truth."),
 (9, None,
  "'You just crashed into the building for the blind while drunk, don't you understand?' Samson freezes, staring at his daughter."),
 (10, None,
  "'They've been showing you on TV all day!' Literally, 'along television the whole day they show you'."),
 (11, None,
  "'Have we sorted all this out? Can we go home?' She asks if the charade is finally over."),
 (12, None,
  "'And I won't be washing your dishes anymore either!' With that, Yulia storms away from the sink, leaving Samson, Nina, and Arkady in stunned silence."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."

OUTRO = ("So Yulia has blown the cover off the entire lie, and Samson finally knows that he is no hero at all. Well done "
         "following that dramatic reveal in Russian. See you in the next scene.")
CLOSING = ("yulia", "Можем ехать домой?")
