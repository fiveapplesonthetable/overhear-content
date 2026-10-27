ID = "domashniy-arest-s01e08-scene-33"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 33
TITLE = "Никуда не поедете  (You're Not Going Anywhere)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "guide": "angelina", "samson": "anja"}
LABELS = {"anya": "Нина", "guide": "Экскурсовод", "samson": "Самсон"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = ("Cues 737-754. Arkady is absent -> anya = Нина (alisa), guide = Экскурсовод (angelina), "
               "samson = Самсон (anja). Slang 'ржать' (739) and ASR babble in 741-743 omitted for clean A1. "
               "Proverb 'Яблоко от яблони' (754) expanded to 'Яблоко от яблони недалеко падает'.")

INTRO = ("Outside by the tour bus a short time later. Last time, in the communal kitchen, Klavdia Viktorovna warned Nina that "
         "Vanya would ruin her life, sparking a furious argument. Now Nina and Samsonov are trying to board an organized family "
         "excursion to the War Glory memorial, but the strict tour organizer blocks their way. We'll hear it in Russian first; "
         "don't worry about catching every word.")

STORY = [
 ("guide", "Сейчас мы едем на курган воинской славы.",
  "We are now heading to the War Glory Memorial Mound.",
  [(737, "Сейчас мы едем на курган воинской славы")], ""),
 ("guide", "Во время экскурсии не кричать и не бегать!",
  "During the tour, no shouting and no running!",
  [(738, "Во время посещения экспозиции не кричать"), (740, "и не бегать")], ""),
 ("guide", "Не перебивать экскурсовода! Всем понятно?",
  "Do not interrupt the guide! Is that clear to everyone?",
  [(740, "не перебивать экскурсовода"), (741, "понятно")], ""),
 ("guide", "Все быстро садимся по автобусам!",
  "Everyone get on the buses quickly!",
  [(741, "все собрались и по автобусам быстро")], ""),
 ("anya", "Ваня, пойдём скорее! Где Славик?",
  "Vanya, let's go quickly! Where is Slavik?",
  [(744, "Приходи немедленно"), (746, "Я сказала")], ""),
 ("samson", "Сейчас, я уже иду. Не торопи меня.",
  "Coming, I'm already on my way. Don't rush me.",
  [(745, "Мама")], "Samsonov trailing behind with bags"),
 ("guide", "Самсонова! Стойте! Вы никуда не поедете!",
  "Samsonova! Stop! You're not going anywhere!",
  [(747, "Собсонова"), (748, "Никуда не поедете")],
  "ASR 'Собсонова' -> 'Самсонова'"),
 ("anya", "Что? Почему это мы не поедем?",
  "What? Why on earth wouldn't we go?",
  [(749, "Что"), (751, "Почему")], ""),
 ("guide", "Я сказала, никуда вы не поедете!",
  "I said, you are not going anywhere!",
  [(750, "Никуда не поедете")], ""),
 ("samson", "Послушайте, мы же купили билеты!",
  "Listen here, we bought tickets after all!",
  [(751, "Почему")], "Samson steps forward to argue"),
 ("guide", "Потому что сил с вами больше нет!",
  "Because I have no strength left dealing with you!",
  [(752, "Потому что сил с вами уже больше нет")], ""),
 ("anya", "Пожалуйста, пустите нас в автобус!",
  "Please, let us onto the bus!",
  [(753, "Пожалуйста")], ""),
 ("guide", "Правильно про вас люди говорят.",
  "People are right about your family.",
  [(754, "Правильно про вас говорят")], ""),
 ("guide", "Яблоко от яблони недалеко падает!",
  "The apple doesn't fall far from the tree!",
  [(754, "Яблоко от яблони")], ""),
]

OPENER = "Let's go through the scene line by line. First, the tour organizer shouts into a megaphone beside the parked bus."

WALK = [
 (0, None,
  "'We are now heading to the War Glory Memorial Mound.' The noun refers to an ancient burial mound or memorial hill."),
 (1, None,
  "'During the tour, no shouting and no running!' In Russian, negative infinitives are often used for strict official rules."),
 (2, None,
  "'Do not interrupt the guide! Is that clear to everyone?' The organizer insists on total discipline from the passengers."),
 (3, None,
  "'Everyone get on the buses quickly!' The prepositional phrase literally means 'into the buses'."),
 (4, None,
  "'Vanya, let's go quickly! Where is Slavik?' Nina rushes toward the bus door, trying to herd her family aboard."),
 (5, None,
  "'Coming, I'm already on my way. Don't rush me.' Samson trudges slowly through the snow, carrying picnic supplies."),
 (6, None,
  "'Samsonova! Stop! You're not going anywhere!' The guide steps in front of Nina and plants her feet firmly on the steps."),
 (7, None,
  "'What? Why on earth wouldn't we go?' Nina is taken completely by surprise by the sudden rejection."),
 (8, None,
  "'I said, you are not going anywhere!' The guide repeats herself with cold finality."),
 (9, None,
  "'Listen here, we bought tickets after all!' Samson tries to intervene with the organizer."),
 (10, None,
  "'Because I have no strength left dealing with you!' Literally, 'there are no forces left with you'."),
 (11, None,
  "'Please, let us onto the bus!' Nina pleads with the woman, pointing to her disappointed son."),
 (12, None,
  "'People are right about your family.' The organizer refuses to budge for the troublemaking mayoral candidate."),
 (13, None,
  "'The apple doesn't fall far from the tree!' This classic Russian proverb means children take after their parents' bad habits."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = ("Next time, back in the communal flat, Arkady's girlfriend Lyolya drops by his room with gossip about Osipenko. "
         "Well done following that confrontation at the bus stop in Russian. See you in the next scene.")
CLOSING = ("guide", "Никуда не поедете!")
