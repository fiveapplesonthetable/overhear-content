"""Scene 31 — German archive sources (s01e07, 00:55:33–00:57:18)."""

ID = "domashniy-arest-s01e07-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 31
TITLE = "Немецкие источники  (German Archive Sources)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "general": "anja",
    "lyova": "angelina",
}

LABELS = {
    "anya": "Лавров",
    "general": "Генерал Круглов",
    "lyova": "Лёва",
}

INTRO = (
    "Last time at the forest picnic, Samsonov showed off his axe-throwing skills, "
    "kicked the tree trunk, and knocked the axe straight down onto lawyer Danya's hand. "
    "Meanwhile at the security office, Major Lavrov and Colonel Mikhail Mikhailovich "
    "report on a video call to General Kruglov in Moscow that Samsonov's family record "
    "is spotless, until young archive lieutenant Lyova Sokolov steps forward with a thick "
    "folder. Let's hear the conversation in Russian first, then walk through it together."
)

STORY = [
    ("anya", "К сожалению, компромата на него нет.",
     "Unfortunately, there is no compromising material on him.",
     [(1187, "К сожалению"), (1187, "компромата на него")], ""),
    ("anya", "Нам придётся искать другие методы.",
     "We will have to look for other methods.",
     [(1188, "придется"), (1188, "методам")], "'прибегнуть к менее корректным методам' -> 'искать другие методы'"),
    ("general", "А вы все архивные документы посмотрели?",
     "Did you look through all the archive documents?",
     [(1190, "А вы все архивные документы посмотрели")], ""),
    ("anya", "Так точно, товарищ генерал! Мы вторые сутки не спим.",
     "Yes, sir, Comrade General! We haven't slept for two days.",
     [(1191, "Так точно"), (1192, "Товарищ генерал, мы вторые сутки не спим")], "Colonel's line folded into Lavrov"),
    ("general", "Двое суток они не спят! Мы годами не спим.",
     "Two days they haven't slept! We go years without sleeping.",
     [(1193, "Двое суток они не спят"), (1194, "Мы годами не спим")], ""),
    ("anya", "На родственников ничего нет. Оба деда воевали.",
     "There's nothing on his relatives. Both grandfathers fought in the war.",
     [(1196, "На родственников ничего. Оба деда воевали")], ""),
    ("anya", "Один из них погиб на войне. Бабушки обыкновенные.",
     "One of them died in the war. The grandmothers are ordinary.",
     [(1197, "Один из них"), (1197, "погиб"), (1198, "Бабушки обыкновенные")], "'партизанил' -> 'на войне'"),
    ("lyova", "А у меня есть другая информация!",
     "Wait, I have different information!",
     [(1200, "А у меня есть другая информация")], ""),
    ("lyova", "Дед Самсонова по линии матери не был героем.",
     "Samsonov's grandfather on his mother's side was no hero.",
     [(1201, "Дед Самсонова по линии матери")], "'Вовсе не партизанил' -> 'не был героем'"),
    ("lyova", "Он был полицаем под Брянском! Осторожно, это архив.",
     "He was a collaborator policeman near Bryansk! Careful, this is an archive file.",
     [(1203, "был полицаем"), (1204, "Под Брянском"), (1205, "Осторожно, архив")], ""),
    ("general", "Соколов проявил инициативу и нашёл документы.",
     "Sokolov showed initiative and found the documents.",
     [(1208, "Соколов проявил инициативу, нашел документы")], ""),
    ("lyova", "Нужно смотреть не только наши источники! Есть и немецкие.",
     "One must check not only our sources! There are German ones too.",
     [(1212, "Не только наши источники нужно смотреть"), (1212, "немецкие")], "ASR 'Мы маму' omitted"),
    ("general", "Спасибо, лейтенант Соколов! У него здоровые амбиции.",
     "Thank you, Lieutenant Sokolov! He has healthy ambitions.",
     [(1213, "спасибо, лейтенант Соколов"), (1215, "У него здоровые амбиции")], ""),
    ("general", "Соколов переходит в вашу группу. Вот и договорились!",
     "Sokolov is transferring to your group. Then it's settled!",
     [(1216, "Соколов"), (1216, "в вашу группу"), (1219, "Вот и договорились")], "'прикреплен' -> 'переходит'"),
]

OPENER = "Now let's break down how Lieutenant Lyova Sokolov surprises everyone on the video call."

WALK = [
    (0, None,
     "'Unfortunately, there is no compromising material on him.' Major Lavrov begins with bad news for Moscow while Colonel Mikhail Mikhailovich nods beside him."),
    (1, None,
     "'We will have to look for other methods.' The impersonal future verb takes a dative pronoun to express 'we will have to'."),
    (2, None,
     "'Did you look through all the archive documents?' On the big wall screen, General Kruglov asks whether they checked the archives thoroughly."),
    (3, "Так точно, товарищ генерал!",
     "'Yes, sir, Comrade General!' That two-word military formula is the standard Russian answer for 'yes, sir'."),
    (3, "Мы вторые сутки не спим.",
     "'We haven't slept for a second straight day.' The plural noun for a twenty-four-hour period is used when counting whole days and nights."),
    (4, None,
     "'Two days they haven't slept! We go years without sleeping.' General Kruglov scoffs at their complaint, using the instrumental plural of 'year' to mean 'for years on end'."),
    (5, None,
     "'There is nothing on his relatives. Both grandfathers fought in the war.' Lavrov summarises what they found on Samsonov's family."),
    (6, None,
     "'One of them died in the war. The grandmothers are ordinary.' Even his great-grandfathers have nothing suspicious in the Soviet files."),
    (7, None,
     "'Wait, I have different information!' Suddenly young Lieutenant Lyova Sokolov speaks up from the back with a heavy archive binder."),
    (8, None,
     "'Samsonov's grandfather on his mother's side was no hero.' The phrase literally means 'along the mother's line'."),
    (9, None,
     "'He was a collaborator policeman near Bryansk! Careful, this is an archive file.' Lyova lays the fragile wartime folder on the table."),
    (10, None,
     "'Sokolov showed initiative and found the documents.' General Kruglov smiles on the screen, revealing that Lyova already sent him scans."),
    (11, None,
     "'One must check not only our sources! There are German ones too.' Lyova proudly explains how he uncovered the wartime record."),
    (12, None,
     "'Thank you, Lieutenant Sokolov! He has healthy ambitions.' When Colonel Mikhail Mikhailovich protests that his nephew went over their heads, the general cuts him off."),
    (13, None,
     "'Sokolov is transferring to your group. Then it's settled!' Before signing off, Kruglov officially assigns Lyova to Lavrov's team."),
]

TRANSITION = "Now let's listen to the whole archive report again from start to finish."

OUTRO = (
    "Thanks to his German archive discovery, young Lyova Sokolov is officially assigned to "
    "Major Lavrov's team, and Lavrov now has the wartime scandal he needs against Samsonov."
)

CLOSING = ("lyova", "А у меня есть другая информация!")
