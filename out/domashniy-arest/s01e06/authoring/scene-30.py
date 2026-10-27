ID = "domashniy-arest-s01e06-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 30
TITLE = "Момент упущен  (The Moment Has Passed)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "olya": "anja", "marina": "angelina"}
LABELS = {"anya": "Аркадий", "olya": "Лёля", "marina": "Марина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 1089-1128. Colloquial 'Здрасте... Чемпотичненько' (1091, 1093) -> A1 'Здравствуйте! У вас тут очень мило.'; "
    "slang 'обиженку включил' (1109) -> 'на меня обиделся'; brand name 'шанель' (1118) -> 'духи'."
)

INTRO = (
    "In the hallway and Arkady's room late at night. Last time, Arkady and Marina were laughing over a card game and "
    "getting ready to drink a small bottle of Bulgarian rakia from her students, when the doorbell rang twice for "
    "Arkady. Opening the front door, Arkady finds his glamorous young girlfriend Lyolya standing on the landing. We'll "
    "hear it in Russian first; don't worry about catching every word."
)

STORY = [
 ("olya", "Привет, Аркаша! Я приехала сразу, как только смогла.",
  "Hi, Arkasha! I came as soon as I could.",
  [(1089, "Привет"), (1111, "Аркаша, я приехала сразу, как только смогла")], ""),
 ("olya", "Здравствуйте! У вас тут очень мило. Куда идти?",
  "Hello! It's very nice here. Where do I go?",
  [(1092, "куда идти")], "colloquial 'Здрасте... Чемпотичненько' (1091, 1093) -> 'Здравствуйте! У вас тут очень мило.'"),
 ("anya", "Да, сюда, в мою комнату.",
  "Yes, in here, into my room.",
  [(1095, "Да, сюда")], ""),
 ("olya", "А здесь нет тараканов? Я с детства их боюсь!",
  "Are there no cockroaches here? I've been afraid of them since childhood!",
  [(1096, "А нет тараканов"), (1098, "я"), (1098, "с детства их боюсь")], "'панически' dropped"),
 ("anya", "Слушай, Лёля, я очень ценю, что ты приехала.",
  "Listen, Lyolya, I really appreciate that you came.",
  [(1097, "Слушай"), (1099, "Я"), (1099, "ценю")], ""),
 ("anya", "Но сейчас не время. Не надо, не раздевайся!",
  "But now isn't the time. Don't, don't take your coat off!",
  [(1099, "но сейчас не время"), (1100, "не надо, не раздевайся")], ""),
 ("olya", "В смысле? Но я хочу остаться!",
  "What do you mean? But I want to stay!",
  [(1101, "В смысле"), (1103, "Но я хочу")], ""),
 ("anya", "Лёля, всё в порядке. Давай в другой раз!",
  "Lyolya, everything is fine. Let's do it another time!",
  [(1104, "все в порядке"), (1106, "Леля"), (1107, "В другой раз")], ""),
 ("olya", "Я не поняла, ты сейчас на меня обиделся?",
  "I don't get it, are you upset with me right now?",
  [(1109, "я не поняла"), (1109, "ты сейчас")], "slang 'обиженку включил' -> 'на меня обиделся'"),
 ("anya", "Нет, я не обижаюсь. Всё по-прежнему!",
  "No, I'm not upset. Everything is still the same!",
  [(1115, "Нет, не обижаюсь"), (1117, "Всё по-прежнему")], ""),
 ("anya", "Держи свои духи. Давай я тебя провожу. Пока!",
  "Here is your perfume. Let me walk you out. Bye!",
  [(1118, "Держи свою"), (1119, "Давай, я тебя провожу"), (1120, "Пока")], "'шанель' -> 'духи'"),
 ("anya", "Марина, послушайте, она ушла! Давайте пить ракию!",
  "Marina, listen, she has left! Let's drink the rakia!",
  [(1121, "Марина, послушайте, она ушла"), (1122, "Давайте пить ракию")], ""),
 ("marina", "А мне что-то уже не хочется. Момент упущен.",
  "Somehow I don't feel like it anymore. The moment has passed.",
  [(1123, "А мне что-то уже не хочется"), (1124, "Момент упущен")], ""),
 ("anya", "У нас с ней ничего не было, правда!",
  "Nothing happened between her and me, really!",
  [(1125, "У нас с ней ничего не было, правда")], ""),
 ("marina", "Ой, да мне всё равно.",
  "Oh, I don't care anyway.",
  [(1126, "Ой, да"), (1126, "мне всё равно")], ""),
 ("anya", "Но ведь между нами что-то промелькнуло!",
  "But surely a spark passed between us!",
  [(1127, "Но ведь между нами что-то промелькнуло")], ""),
 ("marina", "Это ваша самоуверенность промелькнула. Спокойной ночи!",
  "That was your overconfidence flashing by. Good night!",
  [(1128, "Это самоуверенность ваша промелькнула")], ""),
]

OPENER = "Let's take the scene line by line. Lyolya steps into the hallway in her fur coat."

WALK = [
 (0, None,
  "'Hi, Arkasha! I came as soon as I could.' Days ago Arkady begged her to visit him, and she has picked the worst "
  "possible moment to show up. Passing Marina in the corridor, Lyolya smiles brightly."),
 (1, None,
  "'Hello! It's very nice here. Where do I go?' Marina watches in silence as Arkady hurries Lyolya into his room."),
 (2, None,
  "'Yes, in here, into my room.' Lyolya looks around the tiny room behind the wardrobe."),
 (3, None,
  "'Are there no cockroaches here? I've been afraid of them since childhood!' And she starts unbuttoning her coat. "
  "Arkady immediately stops her."),
 (4, None,
  "'Listen, Lyolya, I really appreciate that you came.' He holds her coat on her shoulders."),
 (5, "Не надо, не раздевайся!",
  "'But now isn't the time. Don't, don't take your coat off!' The reflexive verb means 'to undress' or 'to take off "
  "one's coat' when coming indoors. Lyolya stares at him."),
 (6, None,
  "'What do you mean? But I want to stay!' Literally, 'in what sense?'. Arkady gently steers her back toward the door."),
 (7, None,
  "'Lyolya, everything is fine. Let's do it another time!' All Arkady can think about is getting back to his evening "
  "with Marina. Lyolya narrows her eyes."),
 (8, None,
  "'I don't get it, are you upset with me right now?' She thinks he is sulking because she didn't visit sooner."),
 (9, None,
  "'No, I'm not upset. Everything is still the same!' The adverb at the end means 'as before' or 'as always'."),
 (10, None,
  "'Here is your perfume. Let me walk you out. Bye!' He hands her a box of French perfume he bought for her and "
  "practically pushes her out the front door. Then he hurries straight to Marina's room."),
 (11, None,
  "'Marina, listen, she has left! Let's drink the rakia!' He beams expectantly, holding the bottle. But Marina's face "
  "is cool and distant."),
 (12, "Момент упущен.",
  "'Somehow I don't feel like it anymore. The moment has passed.' Literally, 'the moment is let slip'. Seeing his "
  "glamorous young girlfriend walk in broke the spell completely."),
 (13, None,
  "'Nothing happened between her and me, really!' Literally, 'by us with her nothing was'."),
 (14, None,
  "'Oh, I don't care anyway.' Literally, 'to me it is all the same'. Arkady tries one last plea."),
 (15, None,
  "'But surely a spark passed between us!' The verb means 'flashed by' or 'flickered for a moment'."),
 (16, None,
  "'That was your overconfidence flashing by. Good night!' And with that, Marina closes the door in his face."),
]

TRANSITION = "Now let's hear the whole scene once more, start to finish."

OUTRO = (
    "So Arkady sends his girlfriend Lyolya away in record time just to get back to Marina, only to discover that the "
    "moment has already passed. Next time, in our final scene of the episode, we see how the evening news reports "
    "Samson's rescue at the river. See you then."
)
CLOSING = ("marina", "А мне что-то уже не хочется. Момент упущен.")
