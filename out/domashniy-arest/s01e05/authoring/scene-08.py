ID = "domashniy-arest-s01e05-scene-08"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = "Совет Аркадия  (Arkady's Advice)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "marina": "angelina"}
LABELS = {"anya": "Аркадий", "marina": "Марина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"

INTRO = ("Last time, out on the stairs, Uncle Grisha scolded Kostik for only making a scary face and decided they "
         "would come back after lunch to smash some furniture. Inside the communal kitchen, a shaken Marina asks "
         "Arkady whether the debt collectors' threats are serious. We'll hear the scene in Russian first; don't worry "
         "about catching every word.")

STORY = [
 ("marina", "Извините, вы думаете, они серьёзно?",
  "Excuse me, do you think they are serious?",
  [(274, "Извините"), (275, "Вы думаете, они серьезно")], ""),
 ("anya", "Что серьёзно?",
  "Serious about what?",
  [(276, "Что серьезно")], ""),
 ("marina", "Ну, эти люди серьёзно угрожали?",
  "Well, were those men seriously threatening us?",
  [(277, "Ну, эти"), (277, "серьезно угрожали")],
  "'люди' added"),
 ("anya", "Да откуда я знаю?",
  "How would I know?",
  [(278, "Да откуда я знаю")], ""),
 ("marina", "Ну что мне делать?",
  "Well, what should I do?",
  [(279, "Ну, что мне делать")], ""),
 ("anya", "Отдайте им деньги.",
  "Give them the money.",
  [(280, "отдайте им деньги")],
  "colloquial 'раз уж вы вляпались' omitted"),
 ("marina", "Интересно! Я деньги не печатаю!",
  "How interesting! I don't print money!",
  [(281, "Интересно"), (281, "не печатаю")],
  "'их' -> 'деньги'"),
 ("anya", "Ну, продайте что-нибудь.",
  "Well, sell something.",
  [(282, "Ну, продайте что-нибудь")], ""),
 ("marina", "Да что продать? Часов золотых у меня тоже нет!",
  "Sell what? I don't have a gold watch either!",
  [(283, "Да что продать"), (283, "часов золотых у меня тоже нет")], ""),
 ("anya", "Слушайте, что вы кричите на меня и мои часы? У меня тоже денег нет.",
  "Listen, why are you shouting at me and my watch? I have no money either.",
  [(284, "Слушайте, что вы"), (284, "на меня и мои часы"), (285, "У меня тоже денег нет")],
  "colloquial 'орёте' -> 'кричите'"),
 ("anya", "Пусть друг ваш платит!",
  "Let your friend pay!",
  [(286, "ваш платит")],
  "crude 'хахаль' -> 'друг'"),
 ("marina", "Эдуард Владимирович учёный, и он живёт на зарплату.",
  "Eduard Vladimirovich is a scholar, and he lives on a salary.",
  [(287, "Эдуард"), (287, "ученый"), (288, "И он живет на зарплату")],
  "cue 287 slip 'Валентинович' -> 'Владимирович'"),
 ("anya", "Да? А спросите у него, куда он дел компьютерный класс.",
  "Really? Then ask him where he put the computer lab.",
  [(289, "Да? А спросите у него"), (290, "куда он"), (290, "компьютерный класс")],
  "cue 290 'подевал' -> 'дел'"),
 ("anya", "Который ему город подарил! И откуда у Аллы Евгеньевны новая шуба!",
  "Which the city gave him! And where Alla Yevgenyevna got her new fur coat!",
  [(291, "который ему город подарил"), (292, "И откуда у Аллы Евгеньевны"), (292, "шуба")],
  "cue 292 garbled 'соваленная шуба в пол' -> 'новая шуба'"),
 ("marina", "Слушайте, не надо всех мерить по себе!",
  "Listen, don't judge everyone by yourself!",
  [(294, "Слушайте, не надо всех мерить по себе")],
  "crude cues 296-299 omitted"),
]

OPENER = ("Let's break it down. Marina brave-faced the collectors in the corridor, but now in the kitchen her hands "
          "are trembling.")

WALK = [
 (0, "Извините, вы думаете, они серьёзно?",
  "'Excuse me, do you think they are serious?' Even when asking Arkady for advice, Marina stays on the polite 'you'."),
 (1, None,
  "'Serious about what?' Arkady is calmly eating his breakfast."),
 (2, "Ну, эти люди серьёзно угрожали?",
  "'Well, were those men seriously threatening us?' Arkady just shrugs at her."),
 (3, "Да откуда я знаю?",
  "'How would I know?' Literally 'from where do I know?' — a very common everyday reply."),
 (4, None,
  "'Well, what should I do?' Arkady offers the most obvious answer."),
 (5, "Отдайте им деньги.",
  "'Give them the money.' Marina flares up."),
 (6, "Интересно! Я деньги не печатаю!",
  "'How interesting! I don't print money!' Arkady takes another sip of tea."),
 (7, "Ну, продайте что-нибудь.",
  "'Well, sell something.' Marina glances at the expensive gold watch gleaming on Arkady's wrist."),
 (8, "Да что продать? Часов золотых у меня тоже нет!",
  "'Sell what? I don't have a gold watch either!' Notice that 'watch' in Russian is always plural — like 'glasses' or "
  "'scissors' — and takes the genitive plural after 'there is no'. Arkady covers his wrist indignantly."),
 (9, "Слушайте, что вы кричите на меня и мои часы?",
  "'Listen, why are you shouting at me and my watch?' Here 'what' is used colloquially to mean 'why'."),
 (9, "У меня тоже денег нет.",
  "'I have no money either.' Then he thinks of Marina's former lover, the university dean."),
 (10, "Пусть друг ваш платит!",
  "'Let your friend pay!' The particle at the start makes a third-person command: 'let him pay'. Marina defends the "
  "dean's honesty."),
 (11, "Эдуард Владимирович учёный, и он живёт на зарплату.",
  "'Eduard Vladimirovich is a scholar, and he lives on a salary.' As mayor, Arkady knows the inside story of everyone "
  "in Sineozersk, and he laughs."),
 (12, "Да? А спросите у него, куда он дел компьютерный класс.",
  "'Really? Then ask him where he put the computer lab.' And he adds two more details."),
 (13, "Который ему город подарил! И откуда у Аллы Евгеньевны новая шуба!",
  "'Which the city gave him! And where Alla Yevgenyevna got her new fur coat!' Alla Yevgenyevna is the university "
  "rector — and the dean's wife. Marina refuses to believe it, though she decides to go and ask the dean for help."),
 (14, "Слушайте, не надо всех мерить по себе!",
  "'Listen, don't judge everyone by yourself!' Literally 'do not measure everyone by yourself'."),
]

TRANSITION = "Let's hear the whole kitchen conversation again from the beginning."

OUTRO = ("So Arkady's cynical advice sends Marina off to the university to ask Dean Eduard Vladimirovich for help "
         "with the hundred and fifty thousand roubles. See you next time.")
CLOSING = ("marina", "Я деньги не печатаю!")
