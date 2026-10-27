"""Scene 33 — A mark against him (s01e07, 01:01:07–01:02:29)."""

ID = "domashniy-arest-s01e07-scene-33"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 33
TITLE = "Это же клеймо  (A Mark Against Him)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nina": "angelina",
    "pasha": "anja",
}

LABELS = {
    "anya": "Самсон",
    "nina": "Нина",
    "pasha": "Паша",
}

INTRO = (
    "Last time in the communal flat, Arkady slipped his healthy arms out of his casts to "
    "give Marina his grandmother's brooch and recite a love poem, until Ilona phoned on "
    "speakerphone and exposed his fake injury. Now at the hospital trauma room, surgeon "
    "Vakhtang Surenovich tends to lawyer Danya's injured finger while Nina scolds Samsonov, "
    "and at City Hall Major Lavrov delivers the German archive file to acting mayor Pasha "
    "Osipenko. Let's hear the scene in Russian first."
)

STORY = [
    ("nina", "Ничего, Вахтанг Суренович пришьёт тебе палец обратно!",
     "Never mind, Vakhtang Surenovich will sew your finger back on!",
     [(1268, "палец"), (1269, "Ничего"), (1269, "Суренович"), (1269, "пришьет обратно")], "Danya's opening line echoed by Nina"),
    ("nina", "Он у нас кудесник! Правда, Вахтанг Суренович?",
     "He's our miracle worker! Isn't that right, Vakhtang Surenovich?",
     [(1270, "Он у нас кудесник"), (1270, "Суренович")], "'Скажите' -> 'Правда'"),
    ("anya", "Подумаешь, что там у тебя, просто царапина?",
     "Big deal, what have you got there, just a scratch?",
     [(1274, "Что там у тебя"), (1274, "царапина")], ""),
    ("anya", "Что ты расплакался, как маленькая девочка?",
     "Why are you crying like a little girl?",
     [(1275, "Что ты расплакался, как"), (1275, "девочка")], ""),
    ("nina", "Самсонов, рот закрой! Зачем ты его обижаешь?",
     "Samsonov, shut your mouth! Why are you insulting him?",
     [(1276, "Самсонов, рот закрой")], ""),
    ("anya", "А чего он плачет? Я хотел подбодрить!",
     "Why is he crying? I wanted to cheer him up!",
     [(1277, "Чего")], "ASR 'Чего я его плачу? Пободрить?' -> 'А чего он плачет? Я хотел подбодрить!'"),
    ("nina", "Ты его уже подбодрил! Держись, Данюша, держись!",
     "You already cheered him up plenty! Hold on, Danyusha, hold on!",
     [(1278, "Ты"), (1278, "уже подбодрил"), (1279, "Держись, Данюша, держись")], ""),
    ("anya", "Даня, прости меня! Я правда не хотел.",
     "Danya, forgive me! I really didn't mean to.",
     [(1280, "Прости меня")], ""),
    ("pasha", "А откуда у вас эти архивные документы?",
     "And where did you get these archive documents from?",
     [(1282, "А откуда"), (1282, "эти документы")], ""),
    ("pasha", "Да какая разница! Спасибо вам большое, майор!",
     "What difference does it make! Thank you very much, Major!",
     [(1284, "Да какая разница")], "Lavrov's line echoed by Pasha"),
    ("pasha", "Подождите, это же всё не про него!",
     "Wait, none of this is about him!",
     [(1285, "Подождите, это же все не про него")], ""),
    ("pasha", "Но он внук полицая! Это же клеймо!",
     "But he's the grandson of a collaborator! That's a mark of shame!",
     [(1286, "внук полицая"), (1287, "клеймо")], ""),
    ("pasha", "Ему конец на выборах! Внук полицая!",
     "He's finished in the election! The grandson of a collaborator!",
     [(1286, "внук полицая"), (1288, "Ему конец")], ""),
]

OPENER = "Let's walk through the scene at the hospital trauma room and in the mayor's office."

WALK = [
    (0, None,
     "'Never mind, Vakhtang Surenovich will sew your finger back on!' In the hospital trauma room, trembling lawyer Danya fears the axe cut off his finger, and Nina comforts him."),
    (1, None,
     "'He's our miracle worker! Isn't that right, Vakhtang Surenovich?' The cautious surgeon simply answers 'We will see', making poor Danya stutter in alarm."),
    (2, None,
     "'Big deal, what have you got there, just a scratch?' Watching from the doorway, Samsonov awkwardly tries to downplay the injury."),
    (3, None,
     "'Why are you crying like a little girl?' Notice the reflexive prefix and suffix on the verb meaning 'to burst into tears'."),
    (4, None,
     "'Samsonov, shut your mouth! Why are you insulting him?' Furious with her husband, Nina snaps at Samsonov."),
    (5, None,
     "'Why is he crying? I wanted to cheer him up!' Samsonov protests that he was only trying to lift Danya's spirits."),
    (6, None,
     "'You already cheered him up plenty! Hold on, Danyusha, hold on!' Nina uses an affectionate diminutive of Danya's name."),
    (7, None,
     "'Danya, forgive me! I really didn't mean to.' Before stepping out, a chastened Samsonov quietly apologises to Danya."),
    (8, None,
     "'And where did you get these archive documents from?' Meanwhile at City Hall, Major Lavrov hands acting mayor Pasha Osipenko the German archive folder."),
    (9, None,
     "'What difference does it make! Thank you very much, Major!' When Lavrov shrugs that the source doesn't matter, Pasha eagerly agrees."),
    (10, None,
     "'Wait, none of this is about him!' Reading the wartime papers closely, Pasha realises the file is about Samsonov's grandfather, not Samsonov himself."),
    (11, "Но он внук полицая!",
     "'But he's the grandson of a collaborator!' Lavrov points out how voters will see a wartime collaborator's grandson."),
    (11, "Это же клеймо!",
     "'That's a mark of shame!' The noun literally means a brand or stigma that never washes off."),
    (12, None,
     "'He's finished in the election! The grandson of a collaborator!' Pasha grins in triumph, sure that Samsonov's campaign is over."),
]

TRANSITION = "Now let's listen to the whole scene again from the hospital to City Hall."

OUTRO = (
    "While surgeon Vakhtang Surenovich bandages Danya's finger at the hospital, Pasha "
    "Osipenko celebrates in his office, convinced the wartime archive file will destroy "
    "Samsonov's campaign."
)

CLOSING = ("pasha", "Но он внук полицая! Это же клеймо!")
