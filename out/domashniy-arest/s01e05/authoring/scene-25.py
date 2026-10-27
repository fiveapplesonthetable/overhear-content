ID = "domashniy-arest-s01e05-scene-25"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 25
TITLE = "Пять килограммов травы  (Five Kilos of Weed)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "golovkin": "anja", "nina": "angelina"}
LABELS = {"anya": "Самсон", "golovkin": "Головкин", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 954-987. Because of the three-role limit (Samson, Golovkin, Nina), Yulia calling everyone to the TV in cues "
    "973-976 and the TV news report / Andryusha's interview in cues 956-962, 969-972, and 978-985 are folded into "
    "Golovkin's and Nina's lines as they watch the screen. 'А на жену с детьми тебе плевать, да?' (968) is softened "
    "to 'А о жене и детях ты подумал?' and 'наркотики / марихуана' to 'плохая трава / трава'."
)

INTRO = (
    "Back at Golovkin's wooden dacha. Last time, in the university corridor, Major Lavrov and Captain Zavarzin "
    "assured Marina that the debt collectors would never bother her again, though she nearly caught Zavarzin wearing "
    "Arkady's gold watch. At the dacha, Samson sits at the table in despair after learning from Yulia that he really "
    "crashed into the Society of the Blind. We'll hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("golovkin", "И что ты хочешь делать?",
  "And what do you want to do?",
  [(954, "И что ты хочешь делать")], ""),
 ("anya", "Ничего. Расскажу всё как было, пусть знают.",
  "Nothing. I'll tell everything as it was, let them know.",
  [(955, "Ничего, расскажу все как было, пусть знают")], ""),
 ("nina", "Они же тебя тогда в тюрьму посадят!",
  "They will put you in prison then!",
  [(963, "Они же тебя"), (964, "посадят")],
  "'заклюют потом. А может, вообще посадят' -> 'тогда в тюрьму посадят' (A1)"),
 ("anya", "Ну, посадят — значит, посадят. Значит, по делу.",
  "Well, if they lock me up, they lock me up. Means it's deserved.",
  [(965, "Ну, посадят, значит, посадят"), (966, "Значит, по делу")], ""),
 ("nina", "Прекрасно! А о жене и детях ты подумал?",
  "Wonderful! And did you think about your wife and children?",
  [(967, "Прекрасно"), (968, "А"), (968, "детьми")],
  "'на жену с детьми тебе плевать, да?' -> 'о жене и детях ты подумал?' (clean A1)"),
 ("golovkin", "Тихо! Смотрите, что по телевизору говорят!",
  "Quiet! Look what they are saying on television!",
  [], "Yulia calling the family to the TV in cues 973-976 folded into Golovkin's line"),
 ("golovkin", "Пишут, что преступники прятали у слепых плохую траву!",
  "They write that criminals were hiding bad herbs at the blind society!",
  [(959, "Преступники")], "TV news report in cues 957-959 summarised by Golovkin in clean A1"),
 ("nina", "И говорят, что наш кандидат сам уничтожил траву!",
  "And they say that our candidate himself destroyed the herbs!",
  [(961, "наш кандидат"), (961, "уничтожить")],
  "'принял решение самостоятельно уничтожить эту партию наркотиков' -> 'сам уничтожил траву' (clean A1)"),
 ("golovkin", "Полиция говорит: пять килограммов травы — это большой успех!",
  "The police say: five kilograms of herbs is a big success!",
  [(969, "полиция"), (970, "Пять килограммов"), (971, "это успех")],
  "police statement in cues 969-971 reported by Golovkin"),
 ("nina", "А слепые говорят: нас обманули! Мы господину Самсонову только благодарны!",
  "And the blind people say: we were deceived! We are only grateful to Mr. Samsonov!",
  [(981, "господину Самсонову мы только благодарны")],
  "Andryusha's TV interview in cues 980-981 reported by Nina ('ввели в заблуждение' -> 'обманули')"),
 ("anya", "Слышали? Они мне ещё спасибо сказали!",
  "Did you hear? They even said thank you to me!",
  [(987, "Спасибо")], "Samson reacting to the TV report"),
 ("anya", "А стыки, Даня, у тебя всё равно неровные! Понял?",
  "And your seams, Danya, are still uneven! Got it?",
  [(986, "А стыки, Даня, у тебя все равно неровные, понял")], ""),
]

OPENER = (
    "Let's go through the scene line by line. Ashamed of crashing into the Society of the Blind while drunk, Samson "
    "sits gloomily at the dacha table with Nina and Golovkin."
)

WALK = [
 (0, None,
  "'And what do you want to do?' Golovkin uses the informal 'you' form of 'to want' followed by the infinitive 'to "
  "do'."),
 (1, None,
  "'Nothing. I'll tell everything as it was, let them know.' The first-person future 'I will tell' needs no subject "
  "pronoun, and the particle 'let' with a third-person plural verb means 'let them know'."),
 (2, None,
  "'They will put you in prison then!' Literally, Russian says 'they will seat you into prison', using a third-person "
  "plural verb without 'they'."),
 (3, None,
  "'Well, if they lock me up, they lock me up. Means it's deserved.' Repeating a verb with 'means' in the middle is a "
  "classic Russian way to accept your fate."),
 (4, None,
  "'Wonderful! And did you think about your wife and children?' After the preposition 'about', both 'wife' and "
  "'children' stand in the prepositional case. Suddenly Yulia calls from the other room to look at the television."),
 (5, None,
  "'Quiet! Look what they are saying on television!' In Russian you watch something 'by television', using the "
  "preposition 'by, along' with the dative case."),
 (6, None,
  "'They write that criminals were hiding bad herbs at the blind society!' Ilona's trick has worked: the news channels "
  "are reporting that criminals were using the blind workers to pack illegal herbs as sage."),
 (7, None,
  "'And they say that our candidate himself destroyed the herbs!' According to the new story, Samson overheard the "
  "criminals in the restaurant and bravely rammed the building to destroy the stash himself!"),
 (8, None,
  "'The police say: five kilograms of herbs is a big success!' After 'five', both 'kilograms' and 'of herbs' stand in "
  "the genitive case."),
 (9, "А слепые говорят: нас обманули!",
  "'And the blind people say: we were deceived!' On screen, low-vision Andryusha explains that the workers had no idea "
  "what was in the boxes."),
 (9, "Мы господину Самсонову только благодарны!",
  "'We are only grateful to Mr. Samsonov!' The plural short adjective 'grateful' takes the dative case 'to Mr. "
  "Samsonov'. Samson's gloomy face instantly brightens."),
 (10, None,
  "'Did you hear? They even said thank you to me!' He is back to feeling like a hero."),
 (11, None,
  "'And your seams, Danya, are still uneven! Got it?' Now that he is no longer guilty, Samson goes right back to "
  "teasing Golovkin about the crooked wooden planks on his dacha walls."),
]

TRANSITION = "Now let's hear the whole scene again, from start to finish."

OUTRO = (
    "So thanks to Ilona's planted herbs, the television news turned Samson's drunken crash into a heroic raid, and "
    "even the Society of the Blind thanked him on the air. See you in the next scene."
)
CLOSING = ("anya", "А стыки, Даня, у тебя всё равно неровные!")
