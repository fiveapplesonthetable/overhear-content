ID = "domashniy-arest-s01e03-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 12
TITLE = "Страшный инструмент  (A Scarier Tool)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina"}
LABELS = {"anya": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, Arkady's Moscow lawyer abandoned him after a quiet threat from Pasha, leaving Arkady stuck with "
         "the stuttering public defender Golovkin. Meanwhile, Samson and Nina have gone to a hardware shop to buy "
         "something scary enough to make Arkady tell them where the money is — though Samson gets distracted by the "
         "fishing rods. Let's hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Нина, смотри, что я нашёл! Удочку!",
  "Nina, look what I found! A fishing rod!",
  [(390, "Смотри, что"), (392, "Удочку")],
  "slang 'нарыл' -> 'я нашёл'"),
 ("nina", "Первый раз вижу, чтобы людей удочкой пугали.",
  "It's the first time I've seen anyone scare people with a fishing rod.",
  [(393, "Первый раз вижу, чтобы людей удочкой")],
  "cue 393 'пытали' softened to 'пугали'"),
 ("anya", "Здесь леска и острый крючок. Это очень больно!",
  "There's fishing line and a sharp hook here. It's very painful!",
  [(395, "Здесь леска, крючок"), (397, "Это"), (397, "больно")],
  "cue 396 'зацепить за губу, как рыба, разорвет нафиг' cleaned and simplified"),
 ("nina", "Самсон, я не пойму. Ты квартиру не хочешь?",
  "Samson, I don't understand. Don't you want the flat?",
  [(397, "Самсон, я не пойму"), (398, "ты квартиру не хочешь")], ""),
 ("anya", "Я удочку хочу. И ту, и другую!",
  "I want a fishing rod. Both that one and the other one!",
  [(398, "Я удочку хочу"), (399, "и ту, и другую")], ""),
 ("nina", "Нельзя!",
  "No you can't!",
  [(400, "Нельзя")], ""),
 ("anya", "А если не будет этой квартиры?",
  "And what if there is no flat?",
  [(401, "А если не будет этой квартиры")], ""),
 ("nina", "С таким настроением, конечно, не будет.",
  "With an attitude like that, of course there won't be.",
  [(402, "С таким настроением, конечно, не будет")], ""),
 ("nina", "Прекрати! Будет у нас квартира.",
  "Stop it! We will have the flat.",
  [(402, "Прекрати"), (403, "Будет квартира")],
  "'у нас' added"),
 ("anya", "Ладно. Покажем это Аникееву?",
  "All right. Shall we show this to Anikeev?",
  [(404, "это покажем Аникееву")],
  "Samson holds up a small tool"),
 ("nina", "Ты с ума сошёл? Он не испугается!",
  "Have you lost your mind? He won't be scared!",
  [],
  "clean stand-in for cues 404-405 'Ты обалдел... Он сразу в штаны наложит'"),
 ("nina", "Так, мы не шутим, понял? Давай инструмент страшнее.",
  "Right, we are not joking, understood? Find a scarier tool.",
  [(406, "Так, мы не шутим. Понял"), (407, "Давай"), (407, "инструмент страшнее")], ""),
 ("anya", "О, смотри, и дёшево, и сердито!",
  "Oh, look, cheap and effective!",
  [(408, "О, смотри, и дешево, и сердито")], ""),
 ("anya", "Заодно ветки во дворе постригу.",
  "And at the same time I'll trim the branches in the yard.",
  [(408, "Заодно ветки во дворе постригу")], ""),
]

OPENER = ("Let's walk through it. Among the shelves of tools in the hardware shop, Samson beams like a kid in a toy "
          "store.")

WALK = [
 (0, "Нина, смотри, что я нашёл! Удочку!",
  "'Nina, look what I found! A fishing rod!' The noun for 'fishing rod' has the accusative '-u' ending because it's "
  "the object of 'found'. Nina is not impressed."),
 (1, "Первый раз вижу, чтобы людей удочкой пугали.",
  "'It's the first time I've seen anyone scare people with a fishing rod.' Notice the instrumental ending on 'with a "
  "fishing rod'. Samson tries to justify his choice."),
 (2, "Здесь леска и острый крючок. Это очень больно!",
  "'There's fishing line and a sharp hook here. It's very painful!' Nina sees right through him."),
 (3, "Самсон, я не пойму. Ты квартиру не хочешь?",
  "'Samson, I don't understand. Don't you want the flat?' Remember Pasha promised them a three-room flat with a "
  "balcony if they scare the truth out of Arkady. Samson answers honestly."),
 (4, "Я удочку хочу. И ту, и другую!",
  "'I want a fishing rod. Both that one and the other one!' Both pronouns are feminine accusative to match 'fishing "
  "rod'. Nina shuts that down with one word."),
 (5, None,
  "'No you can't!' Literally 'it is not allowed'. Then Samson voices his real doubt."),
 (6, "А если не будет этой квартиры?",
  "'And what if there is no flat?' With negative 'will not be', Russian puts 'this flat' into the genitive case."),
 (7, "С таким настроением, конечно, не будет.",
  "'With an attitude like that, of course there won't be.' The word for 'mood' or 'attitude' is in the instrumental "
  "case after 'with'."),
 (8, "Прекрати! Будет у нас квартира.",
  "'Stop it! We will have the flat.' Literally 'there will be by us a flat'. Samson picks up a tiny tool from the "
  "shelf."),
 (9, "Ладно. Покажем это Аникееву?",
  "'All right. Shall we show this to Anikeev?' The perfective future 'we will show' asks 'shall we show?'. Nina "
  "rolls her eyes."),
 (10, "Ты с ума сошёл? Он не испугается!",
  "'Have you lost your mind? He won't be scared!' Literally 'have you stepped down from your mind?' — a very common "
  "everyday idiom."),
 (11, "Так, мы не шутим, понял? Давай инструмент страшнее.",
  "'Right, we are not joking, understood? Find a scarier tool.' The last word is the comparative form: 'scarier' or "
  "'more frightening'. Then Samson spots a big pair of garden shears."),
 (12, "О, смотри, и дёшево, и сердито!",
  "'Oh, look, cheap and effective!' Word for word: 'both cheap and angry' — a famous Russian idiom for something "
  "inexpensive that really does the job."),
 (13, "Заодно ветки во дворе постригу.",
  "'And at the same time I'll trim the branches in the yard.' Practical to the end: even when buying a tool to "
  "frighten the mayor, Samson is thinking about yard work."),
]

TRANSITION = "Now let's hear the whole hardware shop conversation once more."

OUTRO = ("So Samson and Nina leave the shop with a pair of garden shears instead of a fishing rod. Listen for the "
         "fishing rod and the 'cheap and angry' idiom when you watch; see you next time.")
CLOSING = ("anya", "И дёшево, и сердито!")
