ID = "domashniy-arest-s01e03-scene-08"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = "Детский лепет  (Childish Nonsense)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
SOURCE_NOTE = ("Cues 291-305. Arkady is absent, so Samson is the viewpoint character (anya, label Самсон) and Nina is "
               "nina (angelina, label Нина). Rare 'выковырю' (294) -> 'достану'; slang 'лыбится' (295) -> "
               "'и улыбается'; cues 296-297 simplified with 'таким голосом'; 'сурово' (298) -> 'строго'. "
               "Cue 305 ('Чё?') is expanded to 'Что сделать? Пойдём в магазин.' to set up Scene 12.")

INTRO = ("Back in the communal flat, in the Samsonovs' room. Last time, in the park, Pasha ordered Judge Berg to "
         "keep Arkady under house arrest and promised to deal with his Moscow lawyer. Meanwhile, Samson has come "
         "back from Arkady's room empty-handed, and Nina is waiting to hear how it went. We'll hear it in Russian "
         "first; don't worry about catching every word.")

STORY = [
 ("nina", "Ну что, ты его напугал?",
  "Well then, did you scare him?",
  [(291, "Его напугал")], "'Ну что, ты' added"),
 ("anya", "Я ему всё сказал! Сказал, что ухо отрежу.",
  "I told him everything! I told him I'd cut his ear off.",
  [(293, "ему сказал"), (293, "ухо отрежу")],
  "cues 292-293 ('Че только не говорил. Я вообще ему сказал, там эти ухо отрежу') simplified"),
 ("anya", "И ложкой глаз достану.",
  "And take his eye out with a spoon.",
  [(294, "Ложкой глаз")], "rare 'выковырю' (gouge out) -> 'достану'"),
 ("nina", "И что он?",
  "And what did he do?",
  [], "link between Samson's threat and Arkady's reaction"),
 ("anya", "Ничего! Сидит и улыбается.",
  "Nothing! He just sits there smiling.",
  [(295, "Сидит")], "slang 'лыбится' (grins) -> 'и улыбается'"),
 ("nina", "А ты таким голосом его и пугал?",
  "And did you try to scare him in that voice?",
  [(297, "пугал")], "cues 296-297 ('А че-то вот с этой вот интонацией / Ей пугал что ли?') simplified"),
 ("anya", "Нет, я нормально его пугал, строго!",
  "No, I scared him properly, sternly!",
  [(298, "Нормально его пугал, нет")], "'сурово' -> 'строго'"),
 ("nina", "Вот она, наша новая квартира, Самсон, понимаешь?",
  "There it is, our new flat, Samson, do you understand?",
  [(299, "Вот она"), (299, "понимаешь")], "'квартирка, вот Самсонов' -> 'наша новая квартира, Самсон'"),
 ("nina", "А ты ничего сделать не можешь!",
  "And you can't do a thing!",
  [(300, "А ты ничего сделать не можешь")], ""),
 ("nina", "Какой-то детский лепет несёшь.",
  "You're talking some kind of childish nonsense.",
  [(301, "Какой-то детский лепет несешь")], ""),
 ("anya", "А что ты предлагаешь? Чтобы я ему правда ухо отрезал?",
  "Well, what are you suggesting? That I really cut his ear off?",
  [(302, "ты"), (302, "предлагаешь, чтобы"), (302, "ему ухо"), (302, "отрезал")],
  "'Че ... вообще' -> 'А что'; 'по-настоящему' -> 'правда'"),
 ("anya", "Ты же у нас такая умная! Скажи, что сделать, я сделаю.",
  "You're the clever one here! Tell me what to do, and I'll do it.",
  [(303, "Такая умная"), (304, "Скажи, что сделать, я сделаю")], "'Ты же у нас' added"),
 ("nina", "Что сделать? Пойдём в магазин.",
  "What to do? Let's go to the shop.",
  [], "expands cue 305 ('Чё?') to point to their hardware-shop trip in Scene 12"),
]

OPENER = ("Let's go back through the conversation. Nina has been waiting by the door, hoping the new flat is "
          "already theirs.")

WALK = [
 (0, None,
  "'Well then, did you scare him?' The prefix on the verb makes it perfective: did you actually manage to frighten "
  "him? Samson boasts about his terrible threats."),
 (1, "Я ему всё сказал!",
  "'I told him everything!' Literally, 'I to him everything said', masculine past tense."),
 (1, "Сказал, что ухо отрежу.",
  "'I told him I'd cut his ear off.' Just as in English, Russian keeps the future tense inside 'told him that I "
  "will cut off'. And he didn't stop at the ear."),
 (2, None,
  "'And take his eye out with a spoon.' The first word is 'spoon' in the instrumental case, which means 'with a "
  "spoon, using a spoon'. Nina wants to know the result."),
 (3, None,
  "'And what did he do?' Literally, 'and what he?'. Three tiny words do the whole job. Samson looks deflated."),
 (4, None,
  "'Nothing! He just sits there smiling.' Both verbs are in the present tense, making the picture vivid: he sits "
  "and smiles. Nina hears Samson's sheepish tone."),
 (5, None,
  "'And did you try to scare him in that voice?' Now the verb 'scared' has no prefix, so it is imperfective: 'how "
  "you were trying to scare him'. 'In that voice' uses the instrumental case again. Samson defends himself."),
 (6, None,
  "'No, I scared him properly, sternly!' Both adverbs end in 'o', the usual ending for Russian words that tell how "
  "you do something. Nina thinks of the three-room flat with the balcony."),
 (7, None,
  "'There it is, our new flat, Samson, do you understand?' Literally, 'here she is, our new flat', because the "
  "word for 'flat' is feminine. It is right within reach."),
 (8, None,
  "'And you can't do a thing!' Again, Russian uses a double negative: 'nothing to do not can'."),
 (9, None,
  "'You're talking some kind of childish nonsense.' Literally, 'carrying some kind of baby babble', the idiom "
  "Russian uses for talking nonsense. Samson throws his hands up."),
 (10, "А что ты предлагаешь?",
  "'Well, what are you suggesting?' Present tense, second person singular."),
 (10, "Чтобы я ему правда ухо отрезал?",
  "'That I really cut his ear off?' After 'that, in order that', the verb is in the past-tense form. And then he "
  "hands the problem over to his wife."),
 (11, "Ты же у нас такая умная!",
  "'You're the clever one here!' Literally, 'you after all among us are so clever', feminine ending on both words."),
 (11, "Скажи, что сделать, я сделаю.",
  "'Tell me what to do, and I'll do it.' Notice the pair: the infinitive 'what to do', and then the future 'I "
  "will do it'. Nina takes him at his word."),
 (12, None,
  "'What to do? Let's go to the shop.' And in a few scenes we'll see what kind of shop she means."),
]

TRANSITION = "Now let's listen to the whole scene again, start to finish."

OUTRO = ("So Samson's bloodthirsty threats only made Arkady smile, and now Nina is taking charge of the "
         "intimidation herself. Next we'll follow Slavik to school; see you then.")
CLOSING = ("anya", "Скажи, что сделать, я сделаю.")
