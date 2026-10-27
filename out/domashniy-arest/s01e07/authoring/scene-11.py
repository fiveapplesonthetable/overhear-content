"""s01e07 scene 11: Мэр на коленях (hospital trauma office)."""

ID = "domashniy-arest-s01e07-scene-11"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 11
TITLE = "Мэр на коленях  (Mayor on His Knees)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "doctor": "anja", "ilona": "angelina"}
LABELS = {"anya": "Аркадий", "doctor": "Доктор", "ilona": "Илона"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 7"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = "Cues 444-482 (00:20:25-00:21:53). Arkady and Ilona try to get a fake cast from a trauma doctor."

INTRO = (
    "Previously, at the FSB office, Major Lavrov and Captain Zavarzin were assigned young Lieutenant Lyova Sokolov "
    "to help search the archives for information on Samsonov's grandparents. "
    "Now, at the hospital trauma clinic, Arkady pretends his arms are badly injured so the doctor will put casts on them, "
    "while Ilona stands beside him ready to pay."
)

STORY = [
    ("doctor", "А здесь?",
     "And here?",
     [(445, "А здесь?")], ""),
    ("anya", "Больно, больно! Очень больно, доктор!",
     "It hurts, it hurts! It hurts very much, Doctor!",
     [(446, "Больно, больно"), (448, "Очень больно"), (452, "Доктор, больно")],
     "combined cues 446, 448, and 452"),
    ("anya", "Доктор, мне срочно нужен гипс.",
     "Doctor, I urgently need a cast.",
     [(452, "Доктор"), (453, "Мне нужен гипс")], "added срочно"),
    ("doctor", "У вас даже синяка нет. Вы меня за идиота держите?",
     "You don't even have a bruise. Do you take me for an idiot?",
     [(455, "У вас даже"), (455, "нет"), (456, "Вы меня за")],
     "simplified гематомы to синяка; fixed ASR идиоты принимаете to идиота держите"),
    ("anya", "Тихо, вы правы. Да, я здоров.",
     "Quiet, you're right. Yes, I'm healthy.",
     [(458, "Тихо, вы правы"), (459, "Да, я здоров")], ""),
    ("anya", "Но мне всё равно нужен этот гипс. Так надо.",
     "But I still need this cast. It has to be this way.",
     [(460, "Но мне все равно нужен этот гипс. Так надо")], ""),
    ("doctor", "Он ненормальный.",
     "He is crazy.",
     [(461, "Он ненормальный")], ""),
    ("anya", "Я скоро освобожусь. И сразу сделаю вас главврачом этой больницы!",
     "I will be free soon. And I'll immediately make you chief doctor of this hospital!",
     [(463, "освобожусь, я сразу сделаю вас главврачом этой больницы")],
     "split into two short sentences"),
    ("ilona", "Давайте так. Мы поможем вам, а вы поможете нам.",
     "Let's do it this way. We'll help you, and you'll help us.",
     [(465, "давайте так. Мы поможем вам, а вы поможете нам")], ""),
    ("doctor", "Вы мне ещё и взятку предлагаете, да?",
     "You're offering me a bribe too, aren't you?",
     [(466, "Вы мне еще и взятку предлагаете, да?")], ""),
    ("ilona", "Нет, что вы! Это просто благодарность. Двадцать тысяч.",
     "No, not at all! This is just gratitude. Twenty thousand.",
     [(467, "Нет, что вы. Это просто благодарность. Двадцать тысяч")], ""),
    ("doctor", "Пожалуйста, покиньте кабинет!",
     "Please leave the office!",
     [(468, "Пожалуйста, покиньте кабинет")], ""),
    ("anya", "Я умоляю вас, доктор! Это всё ради любви!",
     "I beg you, Doctor! This is all for love!",
     [(469, "вас, доктор. Я умоляю"), (470, "Это все ради любви")],
     "combined cues 469-470"),
    ("anya", "Вы любили когда-нибудь? Смотрите, мэр стоит на коленях!",
     "Have you ever loved? Look, the mayor is on his knees!",
     [(470, "Вы любили когда-нибудь"), (473, "Мэр на коленях")],
     "combined cues 470 and 473"),
    ("doctor", "Аркадий Борисович, ну что же вы делаете? Прекратите этот спектакль!",
     "Arkady Borisovich, what are you doing? Stop this performance!",
     [(477, "Аркадий Борисович, ну что же вы делаете?"), (478, "это спектакль")],
     "fixed ASR Возвратите это спектакль to Прекратите этот спектакль"),
    ("doctor", "Ладно, вставайте! Пройдите в перевязочную.",
     "All right, get up! Go into the dressing room.",
     [(480, "Ладно"), (481, "Пройдите"), (481, "Перевязочную")],
     "restored preposition в before перевязочную"),
]

OPENER = "Let's unpack how Arkady begs the doctor for a fake cast."

WALK = [
    (1, "Больно, больно!",
     "'It hurts, it hurts!' Arkady cries out as the doctor touches his healthy arm."),
    (2, None,
     "'Doctor, I urgently need a cast.' He states the real reason for his visit to the clinic."),
    (3, "У вас даже синяка нет.",
     "'You do not even have a bruise.' The doctor sees right through the act."),
    (3, "Вы меня за идиота держите?",
     "'Do you take me for an idiot?' Literally, are you holding me for a fool."),
    (4, None,
     "'Quiet, you are right. Yes, I am healthy.' Arkady drops his voice and admits the truth."),
    (5, "Но мне всё равно нужен этот гипс.",
     "'But I still need this cast anyway.' He insists that he cannot leave without it."),
    (7, "И сразу сделаю вас главврачом этой больницы!",
     "'And I will immediately make you the chief doctor of this hospital!' Arkady promises a promotion."),
    (9, None,
     "'You are offering me a bribe too, aren't you?' The doctor is outraged when Ilona pulls out cash."),
    (10, "Это просто благодарность. Двадцать тысяч.",
     "'This is just gratitude. Twenty thousand.' Ilona offers twenty thousand rubles on the desk."),
    (11, None,
     "'Please leave the office!' The formal imperative tells them to get out at once."),
    (12, "Я умоляю вас, доктор! Это всё ради любви!",
     "'I beg you, Doctor! This is all for the sake of love!' Arkady pleads for sympathy."),
    (13, "Смотрите, мэр стоит на коленях!",
     "'Look, the mayor is standing on his knees!' Arkady drops to the floor in front of the doctor."),
    (14, "Прекратите этот спектакль!",
     "'Stop this performance!' Literally, put an end to this theatrical show."),
    (15, None,
     "'All right, get up! Go into the dressing room.' The embarrassed doctor finally gives in."),
]

TRANSITION = "Now listen to the whole trauma office scene again."
OUTRO = "The embarrassed doctor finally agrees to put casts on Arkady's healthy arms."
CLOSING = ("anya", "Спасибо, доктор!")
