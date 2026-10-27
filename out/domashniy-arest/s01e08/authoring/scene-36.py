ID = "domashniy-arest-s01e08-scene-36"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 36
TITLE = "Срочно в больницу  (Rush to the Hospital)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "klavdia": "angelina", "guard": "anja"}
LABELS = {"anya": "Аркадий", "klavdia": "Клавдия Викторовна", "guard": "Лёня"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.08"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = ("Cues 802-834. Arkady is present -> anya = Аркадий (alisa), klavdia = Клавдия Викторовна (angelina), "
               "guard = Лёня (anja). Colloquial 'блин' (803) and intercut nurse cues 823-825 narrated in WALK. "
               "Slang 'от ори' (811) -> 'не кричи'.")

INTRO = ("In the communal hallway and Arkady's bedroom moments later. Last time, Arkady realized with horror that Marina took "
         "Lyoshka for surgery on the wrong knee because of mixed-up X-rays. Now Arkady frantically tries to phone Marina to stop "
         "the operation before waking his bodyguard Lyonya to drive him to the hospital. We'll hear it in Russian first; "
         "don't worry about catching every word.")

STORY = [
 ("anya", "Клавдия Викторовна, дайте мне телефон Марины!",
  "Klavdia Viktorovna, give me Marina's phone number!",
  [(806, "телефон Марину дайте")],
  "ASR 'Марину' -> 'Марины'"),
 ("klavdia", "А тебе зачем её телефон?",
  "And what do you need her phone for?",
  [(807, "А тебе зачем")], ""),
 ("anya", "Нужно срочно отменить операцию Лёшке!",
  "We must cancel Lyoshka's surgery urgently!",
  [(808, "Операцию нужно срочно Лешке отменить")], ""),
 ("klavdia", "Как отменить? Не кричи на меня!",
  "How cancel it? Don't shout at me!",
  [(809, "Как"), (811, "Ну не ори")],
  "'не ори' -> 'не кричи' for A1"),
 ("anya", "Дайте скорее номер, пожалуйста!",
  "Give me the number quickly, please!",
  [(810, "Давайте быстрее телефон, пожалуйста")], ""),
 ("klavdia", "Сейчас посмотрю в своём телефоне.",
  "I'll look in my phone right now.",
  [(812, "Сейчас"), (814, "на мой нету")], ""),
 ("klavdia", "Вот, нашла её фамилию: Пылинкина.",
  "Here, I found her surname: Pylinkina.",
  [(818, "По фамилии тогда"), (821, "О, Пылинкина")], ""),
 ("anya", "Звоню! Абонент выключен! Какой кошмар!",
  "I'm calling! The subscriber is switched off! What a nightmare!",
  [(825, "Аппарат абонента выключен")], ""),
 ("anya", "В больнице запрещено включать телефон.",
  "In the hospital it is forbidden to turn on a phone.",
  [(823, "Женщина, телефон отключите"), (824, "Тут же оборудование")], ""),
 ("anya", "Лёня! Быстро вставай и одевайся!",
  "Lyonya! Get up and get dressed quickly!",
  [(827, "быстро одевайся"), (832, "вставай, вставай, вставай")], ""),
 ("guard", "Что случилось? Куда ты спешишь?",
  "What happened? Where are you rushing to?",
  [(829, "А что такое случилось с тобой")], ""),
 ("anya", "Быстро отвези меня в больницу!",
  "Drive me to the hospital quickly!",
  [(827, "отвезёшь меня в больницу")], ""),
 ("guard", "Я никуда без приказа не поеду.",
  "I won't go anywhere without an order.",
  [(833, "Куда я не поеду")], ""),
 ("anya", "Поехали скорее, там жизнь ребёнка!",
  "Let's go quickly, a child's life is at stake!",
  [(832, "Поехали")], ""),
 ("guard", "Сначала объясни мне, что произошло.",
  "First explain to me what has happened.",
  [(833, "пока ты мне не объяснишь, что случилось")], ""),
]

OPENER = "Let's go through the scene line by line. First, Arkady frantically paces back and forth in front of Klavdia Viktorovna."

WALK = [
 (0, None,
  "'Klavdia Viktorovna, give me Marina's phone number!' In Russian, 'telephone' often means both the phone number and the device itself."),
 (1, None,
  "'And what do you need her phone for?' Klavdia Viktorovna is reluctant to hand out personal phone numbers without a reason."),
 (2, None,
  "'We must cancel Lyoshka's surgery urgently!' Arkady's voice trembles with fear for the young boy."),
 (3, None,
  "'How cancel it? Don't shout at me!' The old woman dislikes being ordered around in her own apartment."),
 (4, None,
  "'Give me the number quickly, please!' Seconds count before the surgeon makes the first cut."),
 (5, None,
  "'I'll look in my phone right now.' She fumbles through her reading glasses and pulls out an old mobile phone."),
 (6, None,
  "'Here, I found her surname: Pylinkina.' Marina's official surname is Pylinkina, listed alphabetically under 'P'."),
 (7, None,
  "'I'm calling! The subscriber is switched off! What a nightmare!' The automated operator voice announces that the number is unavailable."),
 (8, None,
  "'In the hospital it is forbidden to turn on a phone.' Medical equipment in operating theatres requires all phones to be powered off."),
 (9, None,
  "'Lyonya! Get up and get dressed quickly!' Arkady bursts into his bodyguard's room and shakes him awake."),
 (10, None,
  "'What happened? Where are you rushing to?' The FSO guard rubs his sleepy eyes in confusion."),
 (11, None,
  "'Drive me to the hospital quickly!' The prefix 'ot-' on the verb indicates transporting someone to a destination."),
 (12, None,
  "'I won't go anywhere without an order.' Arkady is under strict home arrest, and leaving the apartment violates court bail conditions."),
 (13, None,
  "'Let's go quickly, a child's life is at stake!' Arkady pleads with his guard to put human life ahead of bureaucratic protocol."),
 (14, None,
  "'First explain to me what has happened.' Lyonya stands his ground until Arkady tells him the full truth."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = ("Next time, racing through the snowy city streets, Arkady and Lyonya try to reach the hospital before the surgeon begins. "
         "Well done following that tense kitchen and bedroom exchange in Russian. See you in the next scene.")
CLOSING = ("anya", "Срочно в больницу!")
