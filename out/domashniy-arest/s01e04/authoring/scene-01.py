ID = "domashniy-arest-s01e04-scene-01"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = "Страшный сон Аркадия  (Arkady's Nightmare)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lavrov": "anja", "zavarzin": "angelina"}
LABELS = {"anya": "Аркадий", "lavrov": "Лавров", "zavarzin": "Заварзин"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
SOURCE_NOTE = ("Cues 1-45. Ilona's brief taxi lines (7-10) are told by the narrator, and the opening song "
               "(33-45) is left out. Cue 1 garbles 'Самсон' as 'Самсун', and cues 4 and 6 garble 'Нина' as 'Маша'. "
               "Crude details in cues 14-17, 23, and 30 are omitted or cleaned up.")

INTRO = ("Welcome back to House Arrest. Its hero, Arkady Anikeev, was the mayor of the small Russian town of "
         "Sineozersk until he was caught taking a bribe and placed under house arrest in the noisy communal flat "
         "where he grew up, right next door to his childhood bully Samson. "
         "At the end of the third episode, Samson punched Arkady after finding out that Arkady had made his young "
         "son steal a judge's dog; in this fourth episode, a viral video of Samson makes him a town hero, and "
         "Arkady decides to run Samson for mayor against his scheming deputy Pasha. "
         "We open as a mysterious Moscow visitor takes a taxi into town while Arkady lies in hospital having a "
         "feverish nightmare, and the two security agents, Major Lavrov and Captain Zavarzin, listen in on him. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Самсон, не надо! Мне очень больно!",
  "Samson, don't! It hurts me so much!",
  [(1, "не надо"), (2, "Не надо, мне очень больно")],
  "cue 1 garbles 'Самсон' as 'Самсун'"),
 ("anya", "Я не скажу, где деньги! Нет!",
  "I won't tell you where the money is! No!",
  [(3, "Я не скажу, где деньги. Нет")], ""),
 ("anya", "Постой, Нина! Убери паяльник! Ой, как горячо!",
  "Wait, Nina! Put the soldering iron away! Ow, how hot!",
  [(4, "Постой"), (4, "Убери паяльник"), (5, "Ой, как горячо")],
  "cue 4 garbles 'Нина' as 'Маша'"),
 ("anya", "Нету у меня денег! Нету денег!",
  "I haven't got any money! No money!",
  [(6, "Нету. Нету денег")], "'Пошел ты' dropped; 'у меня' added"),
 ("lavrov", "Ну что, где тут туалет?",
  "So, where is the toilet around here?",
  [(11, "Ну что, где")], "'тут туалет' added for context"),
 ("zavarzin", "Тут рядом, за углом, чебуречная. Там нормально.",
  "Right nearby, round the corner, there's a cheburek café. It's fine there.",
  [(12, "Тут рядом, за углом"), (14, "нормально")],
  "cue 12 'чебуречка' -> 'чебуречная' (as in cue 17/28); crude toilet details in 14-17 omitted"),
 ("zavarzin", "А что у нас там?",
  "And what's going on over there?",
  [(18, "Что у нас там")], ""),
 ("lavrov", "Без изменений. Слушай.",
  "No change. Listen.",
  [(19, "Без изменений"), (21, "Слушайте")], "'Слушайте' -> 'Слушай'"),
 ("anya", "Не надо паяльник! Не надо паяльник!",
  "Not the soldering iron! Not the soldering iron!",
  [(22, "Не надо паяльник. Не надо паяльник")], ""),
 ("lavrov", "И так всю ночь! Ему снятся страшные сны.",
  "It's been like that all night! He's having terrible dreams.",
  [(23, "И так всю ночь")],
  "crude nightmare details in cue 23 replaced by 'Ему снятся страшные сны'"),
 ("zavarzin", "А где деньги, он не сказал?",
  "And didn't he say where the money is?",
  [(24, "А где деньги"), (24, "не сказал")], ""),
 ("lavrov", "Говорит, не скажу, и всё! Ничего не сказал.",
  "He says 'I won't tell', and that's it! He hasn't said a thing.",
  [(25, "Говорит, не скажу и все"), (25, "ничего не сказал")], ""),
 ("lavrov", "Вот партизан! Ну ничего, скоро всё скажет.",
  "What a partisan! Never mind, soon he'll tell us everything.",
  [(26, "Вот партизан. Ну ничего")], "'дозреет' -> 'скоро всё скажет'"),
 ("lavrov", "А ты куда опять пошёл? Сядь, ждём пятнадцать минут.",
  "And where are you off to again? Sit down, we wait fifteen minutes.",
  [(27, "А ты куда"), (31, "Ждем"), (31, "минут")], "cue 30 omitted; '15' written out as 'пятнадцать'"),
 ("anya", "Ой, голова болит! Ухо моё, ухо!",
  "Ow, my head hurts! My ear, my ear!",
  [(32, "Ухо мое, ухо")], "garbled 'Кровь у меня клещет' -> 'Ой, голова болит!'"),
]

OPENER = ("Let's go back through the scene step by step. Arkady is asleep in his hospital bed, tossing and "
          "turning in a nightmare about Samson and Nina.")

WALK = [
 (0, None,
  "'Samson, don't! It hurts me so much!' Literally 'to me it is very painful', using the dative case for the "
  "person who feels pain."),
 (1, None,
  "'I won't tell you where the money is! No!' Even in his sleep, Arkady is guarding his secret."),
 (2, "Постой, Нина! Убери паяльник!",
  "'Wait, Nina! Put the soldering iron away!' Both verbs are perfective commands: 'stop a moment' and 'take away'."),
 (2, "Ой, как горячо!",
  "'Ow, how hot!' And he shouts one more thing in his dream."),
 (3, None,
  "'I haven't got any money! No money!' He uses the colloquial spoken word for 'there isn't any', followed by "
  "the genitive plural of 'money'. Meanwhile, at the listening post, Captain Zavarzin comes back inside."),
 (4, None,
  "'So, where is the toilet around here?' Major Lavrov asks where Zavarzin went."),
 (5, None,
  "'Right nearby, round the corner, there's a cheburek café. It's fine there.' The preposition for 'behind' or "
  "'round' takes the instrumental case: 'round the corner'. A cheburek café is a little snack bar that sells "
  "fried meat pasties. Then Zavarzin points to the headphones."),
 (6, None,
  "'And what's going on over there?' Literally 'what is at us there?'."),
 (7, None,
  "'No change. Listen.' Literally 'without changes'. They both listen as Arkady mutters again."),
 (8, None,
  "'Not the soldering iron! Not the soldering iron!' Lavrov sighs."),
 (9, None,
  "'It's been like that all night! He's having terrible dreams.' In Russian, dreams appear 'to' you: literally "
  "'to him terrible dreams dream themselves'. Zavarzin asks the only question that matters."),
 (10, None,
  "'And didn't he say where the money is?' A compact expression built around 'where' and 'said'."),
 (11, None,
  "'He says I won't tell, and that's it! He hasn't said a thing.' Notice the double negative in the second "
  "sentence: 'nothing not said'."),
 (12, None,
  "'What a partisan! Never mind, soon he'll tell us everything.' Calling someone a partisan is the classic "
  "Russian joke for a person who refuses to talk under questioning. Then Lavrov catches Zavarzin heading for "
  "the door again."),
 (13, None,
  "'And where are you off to again? Sit down, we wait fifteen minutes.' And just then, Arkady wakes up in his "
  "hospital bed and touches his bandages."),
 (14, None,
  "'Ow, my head hurts! My ear, my ear!' Remember that in the last episode Nina nicked his ear and Samson "
  "punched him."),
]

TRANSITION = "Now let's hear the whole opening scene again from the start."

OUTRO = ("So Arkady didn't give away his money even in a nightmare, and now he is awake with a bandaged head. "
         "Next we'll see who that mysterious woman from Moscow is in the taxi; see you there.")
CLOSING = ("anya", "Ухо моё, ухо!")
