# Authoring module for domashniy-arest-s01e08-scene-28.
ID = 'domashniy-arest-s01e08-scene-28'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 28
TITLE = 'Диагноз доктора  (Medical Diagnosis)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша', 'tenenbaum': 'Доктор Тенинбаум'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "After Samsonov's friends refused to back him at the debates, we return to the communal flat. In Arkady's room, young Lyosha sits by the laptop while a foreign specialist, Dr. Tenenbaum, examines the boy over a video call. Listen to the Russian conversation first, and do not worry about catching every word."
OPENER = "Let's follow the online medical consultation line by line."
TRANSITION = "Let's listen to the doctor's diagnosis once again."
OUTRO = "Armed with the revelation that Lyosha only needs antibiotics, Arkady rushes to find Marina. But at the municipal hospital, Marina is already signing the surgeon's papers. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('tenenbaum', 'Доктор Тенинбаум слушает. Что случилось?', 'Doctor Tenenbaum is listening. What happened?', [(531, 'Доктор'), (539, 'Что случилось')], ''),
    ('arkady', 'Яков Григорьевич, у меня срочный вопрос к вам.', 'Yakov Grigoryevich, I have an urgent question for you.', [(538, 'Яков Григорьевич, у меня срочный вопрос к вам')], ''),
    ('arkady', 'Здесь мальчик, Лёха. Поговорите с ним.', 'There is a boy here, Lyokha. Speak with him.', [(544, 'здесь пацан есть, Леха'), (545, 'иди сюда')], ''),
    ('lyosha', 'Здравствуйте, доктор. У меня остеохондропатия.', 'Hello, doctor. I have osteochondropathy.', [(549, 'У меня')], "ASR 'осё хондропатия' restored to 'остеохондропатия'"),
    ('tenenbaum', 'Ну и как тебя лечат?', 'So how are they treating you?', [(551, 'Ну и как тебя лечат')], ''),
    ('lyosha', 'Мне назначили операцию.', 'They scheduled surgery for me.', [(552, 'назначило мне операцию')], ''),
    ('tenenbaum', 'Скажи мне, мальчик. Тебя когда-нибудь клещ кусал?', 'Tell me, boy. Did a tick ever bite you?', [(563, 'Скажи-ка мне, мальчик, тебя когда-нибудь клещ кусал')], ''),
    ('lyosha', 'Да, год назад. Потом всё прошло.', 'Yes, a year ago. Then everything went away.', [(564, 'Год назад'), (568, 'Потом прошло')], ''),
    ('tenenbaum', 'Ну что ж, беги, мальчик! Аркаша, слушай меня.', 'Well then, run along, boy! Arkasha, listen to me.', [(570, 'Ну что ж, беги, мальчик, беги'), (573, 'Аркаша, слушай меня')], ''),
    ('tenenbaum', 'У этого мальчика нет никакой остеохондропатии.', 'This boy has no osteochondropathy at all.', [(575, 'У этого мальчика нет никакой остеохондропатии')], ''),
    ('tenenbaum', 'У него боррелиоз от укуса клеща!', 'He has Lyme disease from a tick bite!', [(576, 'у него боррелиоз'), (577, 'Боррелиоз от укуса клеща')], ''),
    ('tenenbaum', 'И операция ему не нужна.', 'And he does not need surgery.', [(579, 'И операция ему не нужна')], ''),
    ('tenenbaum', 'Это заболевание лечится медикаментозно.', 'This condition is treated with medication.', [(580, 'Это заболевание лечится медикаментозно')], ''),
    ('arkady', 'Спасибо, доктор! Я всё понял.', 'Thank you, doctor! I understood everything.', [], 'new closing A1 line'),
]
WALK = [
    (0, 'Доктор Тенинбаум слушает.', "'Doctor Tenenbaum is listening.' The doctor answers the call from his foreign clinic."),
    (0, 'Что случилось?', "'What happened?' Dr. Tenenbaum gets straight to the point, asking what the emergency is."),
    (1, None, "'Yakov Grigoryevich, I have an urgent question for you.' Arkady addresses his old physician respectfully."),
    (2, 'Здесь мальчик, Лёха.', "'There is a boy here, Lyokha.' Lyokha is the informal nickname for Lyosha."),
    (2, 'Поговорите с ним.', "'Speak with him.' Arkady turns the laptop screen toward Lyosha so the specialist can talk to the boy directly."),
    (3, 'Здравствуйте, доктор.', "'Hello, doctor.' Lyosha introduces himself politely."),
    (3, 'У меня остеохондропатия.', "'I have osteochondropathy.' He recites the scary diagnosis from the local hospital."),
    (4, None, "'So how are they treating you?' The doctor asks about his current therapy."),
    (5, None, "'They scheduled surgery for me.' Lyosha explains that the local doctors already put him down for an operation."),
    (6, 'Скажи мне, мальчик.', "'Tell me, boy.' The doctor focuses on specific symptoms."),
    (6, 'Тебя когда-нибудь клещ кусал?', "'Did a tick ever bite you?' Instead of looking at the X-rays, the experienced professor asks a sharp question about tick bites."),
    (7, 'Да, год назад.', "'Yes, a year ago.' Lyosha remembers getting bitten by a tick the previous summer."),
    (7, 'Потом всё прошло.', "'Then everything went away.' The symptoms disappeared temporarily."),
    (8, 'Ну что ж, беги, мальчик!', "'Well then, run along, boy!' The doctor sends Lyosha out of the room so he can speak privately with Arkady."),
    (8, 'Аркаша, слушай меня.', "'Arkasha, listen to me.' He addresses Arkady by his familiar diminutive."),
    (9, None, "'This boy has no osteochondropathy at all.' Tenenbaum dismisses the local clinic's terrifying diagnosis as complete nonsense."),
    (10, None, "'He has Lyme disease from a tick bite!' The doctor identifies the real cause of the boy's joint problems."),
    (11, None, "'And he does not need surgery.' Best of all, there is no reason to put the child under the surgeon's knife."),
    (12, None, "'This condition is treated with medication.' A simple course of antibiotics is all Lyosha needs."),
    (13, 'Спасибо, доктор!', "'Thank you, doctor!' Arkady breathes a huge sigh of relief."),
    (13, 'Я всё понял.', "'I understood everything.' Now he must stop Marina before the hospital operates."),
]
