ID = "domashniy-arest-s01e06-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 20
TITLE = "Спокойно поговорила  (Had a Calm Talk)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina", "samson": "anja"}
LABELS = {"anya": "Юля", "nina": "Нина", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
SOURCE_NOTE = ("Cues 729-772. Arkady is absent -> anya = Юля (alisa). Classmate Kapustina's lines outside the building "
               "in cues 730-733 are narrated in WALK so Yulya, Nina, and Samson hold the three voices. ASR typo "
               "'маск-комбинат' (734) restored to 'мясокомбинат'; slang 'тачку' (735) -> 'машину'; 'аривидерчи' (736) "
               "-> 'пока'; ASR 'Дядь' (738) -> 'Ваня'; slang 'шариться' (753) -> 'смотреть'; crude accusations in "
               "763-767 ('наркотиками', 'девочка по вызову', 'проститутка') cleaned to 'Обманом? Украла?'.")

INTRO = ("Outside the communal flat and inside the Samsonov apartment a few minutes later. Last time, Ilona visited the "
         "ballet studio and learned that Ignatyev's daughter Galina freezes onstage from stage fright, before Ignatyev "
         "gave Yulya a ride home through the snowstorm. Now Yulya's classmate Kapustina spots her stepping out of the "
         "luxury car, and upstairs Nina and Samson are waiting for an explanation. We'll hear it in Russian first; "
         "don't worry about catching every word.")

STORY = [
 ("anya", "А что, завидно? У него свой мясокомбинат!",
  "What, are you jealous? He owns his own meatpacking plant!",
  [(732, "А что, завидно"), (734, "У него свой")],
  "ASR 'маск-комбинат' restored to 'мясокомбинат'"),
 ("anya", "Он мне машину скоро покупает. Так что пока!",
  "He's buying me a car soon. So bye!",
  [(735, "Он мне"), (735, "скоро покупает"), (736, "Так что")],
  "slang 'тачку' -> 'машину'; Italian 'аривидерчи' -> 'пока'"),
 ("nina", "Ваня, я сама с ней спокойно поговорю. Успокойся.",
  "Vanya, I'll talk to her calmly myself. Calm down.",
  [(738, "я сама с ней спокойно поговорю"), (741, "Успокойся")],
  "ASR 'Дядь' -> 'Ваня'"),
 ("anya", "Я дома! — Привет. Доченька, как дела в школе?",
  "I'm home! — Hi. Sweetie, how are things at school?",
  [(737, "Я дома"), (742, "Привет"), (743, "Доченька"), (743, "как"), (743, "дела в школе")], ""),
 ("anya", "Хорошо! Пятёрка по литературе, пятёрка по русскому.",
  "Good! A five in literature, a five in Russian.",
  [(744, "Хорошо"), (745, "Пятерка по литературе"), (746, "пятерка по русскому")], ""),
 ("anya", "Четыре по алгебре, зато по физкультуре пятёрка.",
  "A four in algebra, but a five in gym.",
  [(747, "четыре по алгебре"), (747, "зато по физкультуре пятерка")], ""),
 ("nina", "Доченька! А ты нам про все пятёрки рассказала?",
  "Sweetheart! Have you told us about all your fives?",
  [(748, "Доченька"), (749, "А ты нам про все"), (749, "рассказала")],
  "'-то' dropped for A1"),
 ("nina", "Может, ты забыла про какие-нибудь? — Какие? — Вот эти вот!",
  "Maybe you forgot about some? — Like what? — These right here!",
  [(750, "Может, ты забыла про какие-нибудь"), (751, "Какие"), (752, "Вот эти вот")], ""),
 ("anya", "Кто вам разрешил смотреть мои вещи?",
  "Who gave you permission to look through my things?",
  [(753, "кто разрешил")],
  "slang 'по моим вещам шариться' -> 'смотреть мои вещи'"),
 ("nina", "Тебя две недели в школе не было!",
  "You haven't been at school for two weeks!",
  [(754, "Тебя две недели в школе не было")], ""),
 ("nina", "Все думают, ты в больнице. Откуда деньги?",
  "Everyone thinks you're in the hospital. Where did the money come from?",
  [(755, "Все думают, ты в больнице"), (756, "Откуда деньги")], ""),
 ("anya", "Не твоё дело! — Это моё дело! — Я их заработала!",
  "None of your business! — It is my business! — I earned it!",
  [(757, "Не твое дело"), (758, "мое дело"), (759, "Я их заработала")], ""),
 ("nina", "Заработала? Расскажи нам тогда, как ты их заработала?",
  "Earned it? Then tell us how you earned it?",
  [(760, "Заработала"), (762, "расскажи нам тогда, как ты их")], ""),
 ("nina", "Обманом? Украла? — Сама ты украла!",
  "By cheating? Did you steal it? — You're the one who stole!",
  [(767, "Сама ты")],
  "crude accusations in cues 763-767 ('наркотиками', 'девочка по вызову', 'проститутка') cleaned to 'Обманом? Украла?'"),
 ("anya", "Я вас всех ненавижу!",
  "I hate all of you!",
  [(768, "Вас всех ненавижу")], ""),
 ("samson", "Молодец. Спокойно поговорила.",
  "Nice job. Had a calm talk with her.",
  [(770, "Молодец"), (771, "Спокойно поговорила")], ""),
]

OPENER = "Let's go through the scene line by line. First, outside the building, Yulya's classmate Kapustina asks if the older man in the big car is her dad."

WALK = [
 (0, None,
  "'What, are you jealous? He owns his own meatpacking plant!' Rather than admit she works there cleaning up, Yulya brags to her classmate."),
 (1, None,
  "'He's buying me a car soon. So bye!' She waves Kapustina off and heads upstairs."),
 (2, None,
  "'Vanya, I'll talk to her calmly myself. Calm down.' Inside the apartment, Nina promises Samson that she will handle their daughter gently."),
 (3, None,
  "'I'm home! — Hi. Sweetie, how are things at school?' Nina starts in an overly sweet voice, using the affectionate diminutive for 'daughter'."),
 (4, None,
  "'Good! A five in literature, a five in Russian.' In Russian schools, five is the top grade, like an A."),
 (5, None,
  "'A four in algebra, but a five in gym.' After the preposition 'by' or 'in', each school subject takes the dative case."),
 (6, None,
  "'Sweetheart! Have you told us about all your fives?' Nina's voice suddenly turns icy, playing on the double meaning of 'fives' as five-thousand-rouble banknotes."),
 (7, None,
  "'Maybe you forgot about some? — Like what? — These right here!' Nina pulls out the thick wad of cash she found hidden in Yulya's room."),
 (8, None,
  "'Who gave you permission to look through my things?' Yulya tries to go on the offensive."),
 (9, None,
  "'You haven't been at school for two weeks!' Literally, 'of you two weeks in school there was not': Russian uses the genitive case for someone who is absent."),
 (10, None,
  "'Everyone thinks you're in the hospital. Where did the money come from?' Nina demands an answer."),
 (11, None,
  "'None of your business! — It is my business! — I insists she earned it!' Literally, 'not your affair — this is my affair'."),
 (12, None,
  "'Earned it? Then tell us how you earned it?' Nina does not believe a sixteen-year-old could earn such a sum honestly."),
 (13, None,
  "'By cheating? Did you steal it? — You're the one who stole!' Furious at her mother's accusations, Yulya shouts back in tears."),
 (14, None,
  "'I hate all of you!' She grabs her bag, runs out of the flat, and slams the front door."),
 (15, None,
  "'Nice job. Had a calm talk with her.' Samson shakes his head at Nina's 'calm' conversation."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."

OUTRO = ("So Nina's 'calm talk' has driven Yulya out into the snowstorm in tears, and now Samson and Nina have to chase "
         "after her. Well done following that family blow-up in Russian. See you in the next scene.")
CLOSING = ("samson", "Спокойно поговорила.")
