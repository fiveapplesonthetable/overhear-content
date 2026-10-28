# domashniy-arest/s01e05/scene-11.py
ID = "domashniy-arest-s01e05-scene-11"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 11
TITLE = "Операция «Золотой ярд»  (Operation Golden Billion)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
VOICES = {"narrator": "sky", "general": "angelina", "lavrov": "anja"}
LABELS = {"general": "Генерал Круглов", "lavrov": "Лавров"}
INTRO = "Last time, when Marina asked Dean Eduard Vladimirovich for help with the debt collectors, he claimed his wife gets a text alert whenever he uses his card and told Marina to hide in her mother's village for six months. Meanwhile, at security-service headquarters, Major Lavrov and regional chief Mikhail Mikhailovich report by video link to scatterbrained General Kruglov in Moscow. Let's listen in Russian first."
STORY = [
    ("lavrov", "Мы рассчитывали, что заместитель заберёт деньги у мэра.", "We counted on the deputy taking the money from the mayor.", [(397, 'Мы рассчитывали, что заместитель'), (397, 'деньги из мэра')], "'выбьет деньги из мэра' -> 'заберёт деньги у мэра'; second clause trimmed"),
    ("lavrov", "Но мэр придумал новый план. Сосед мэра теперь пойдёт в мэры.", "But the mayor came up with a new plan. The mayor's neighbour will now run for mayor.", [(399, 'Мэр придумал'), (399, 'сосед мэра теперь'), (399, 'в мэры')], "'будет баллотироваться в мэры' -> 'пойдёт в мэры'; split into two short sentences"),
    ("lavrov", "И заместителю пришлось переключиться на того соседа.", "And the deputy had to switch his focus to that neighbour.", [(401, 'И заместителю пришлось переключиться'), (401, 'на того соседа')], "'с мэра' trimmed for sentence length"),
    ("lavrov", "Ну и процесс остановился. Да арестовывать его надо, товарищ генерал!", "And so the process stalled. We just need to arrest him, Comrade General!", [(402, 'Ну и процесс'), (403, 'Да арестовывать его надо, товарищ генерал')], "'приостановился' -> 'остановился'; 'не убегу' trimmed"),
    ("general", "Флакон нашли? Этот синий пузырёк.", "Did you find the vial? That little blue bottle.", [(405, 'Флакон нашли'), (406, 'Этот синий пузырек')], ""),
    ("lavrov", "Какой пузырёк?", "What bottle?", [(407, 'Какой пузырек')], ""),
    ("general", "С ядом! А, это же на Урале! Это не у вас.", "With poison! Oh, that's in the Urals! That's not your case.", [(408, 'с ядом'), (411, 'А, это же на Урале'), (412, 'Это не у вас')], "oilman clause in 408 and 'Тупец я' in 409 omitted"),
    ("general", "Подожди, а что у вас?", "Wait, so what is your case?", [(413, 'Подожди, а что у вас')], ""),
    ("lavrov", "У нас фальшивый кластер. Операция «Золотой ярд».", "Ours is the fake cluster. Operation Golden Billion.", [(414, 'У нас фальшивый кластер. Операция «Золотой ярд»')], ""),
    ("general", "А, точно. Перепутал. Такое в стране творится! Продолжаем операцию.", "Oh, right. I mixed them up. So much is going on in the country! Continue the operation.", [(415, 'А, точно. Перепутал'), (416, 'Такое в стране творится'), (418, 'продолжаем операцию')], "'Зашиваемся' in 417 trimmed"),
    ("lavrov", "Есть.", "Yes, sir.", [(419, 'Есть')], ""),
    ("general", "А где этот маленький, который из архива? Это же у вас?", "And where is that short man from the archives? Is he at your branch?", [(420, 'А где этот'), (420, 'который из архива'), (421, 'Это же у вас')], "'карлик' -> 'маленький'"),
    ("lavrov", "Так точно, товарищ генерал.", "Yes indeed, Comrade General.", [(422, 'Так точно, товарищ генерал')], ""),
    ("general", "Я всё помню! Почему не было? Чтобы в следующий раз был!", "I remember everything! Why wasn't he at the meeting? Make sure he's there next time!", [(424, 'Я все помню'), (425, 'Почему не было'), (426, 'Чтобы в следующий раз был')], ""),
    ("general", "Всё, давайте. У меня перерыв на обед.", "Alright, carry on. I have my lunch break.", [(427, 'Все, давайте. У меня перерыв на обед')], ""),
]
OPENER = "Let's walk through it. Lavrov and Mikhail Mikhailovich stand at attention in front of the wall screen to explain why Osipenko still hasn't recovered the stolen billion from Arkady."
WALK = [
    (0, None, "'We counted on the deputy taking the money from the mayor.' Lavrov explains their original plan: let Osipenko squeeze Arkady for the money. Then came the twist."),
    (1, 'Но мэр придумал новый план.', "'But the mayor came up with a new plan.' The verb for 'came up with' is in the masculine past tense, marked by the '-l' ending."),
    (1, 'Сосед мэра теперь пойдёт в мэры.', "'The mayor's neighbour will now run for mayor.' Notice the repetition of 'mayor', ending with the plural 'into mayors' for 'run for mayor'."),
    (2, None, "'And the deputy had to switch his focus to that neighbour.' Literally 'to the deputy it fell to switch onto that neighbour'."),
    (3, 'Ну и процесс остановился.', "'And so the process stalled.' Mikhail Mikhailovich centres the line on the verb for 'stalled' alongside the noun for 'process'."),
    (3, 'Да арестовывать его надо, товарищ генерал!', "'We just need to arrest him, Comrade General!' Mikhail Mikhailovich wants to lock Arkady up again. On the screen, General Kruglov squints at them."),
    (4, 'Флакон нашли?', "'Did you find the vial?' Kruglov suddenly asks."),
    (4, 'Этот синий пузырёк.', "'That little blue bottle.' Both words mean a small bottle or vial. Mikhail Mikhailovich blinks."),
    (5, None, "'What bottle?' Kruglov gestures impatiently at the screen, and then he stops himself."),
    (6, 'С ядом!', "'With poison!' Notice the 'with/as' form after 'with'."),
    (6, 'А, это же на Урале! Это не у вас.', "'Oh, that's in the Urals! That's not your case.' Literally 'that is not by you'. He peers at his notes."),
    (7, None, "'Wait, so what is your case?' Literally 'wait, and what is by you?'. Lavrov reminds him."),
    (8, 'У нас фальшивый кластер.', "'Ours is the fake cluster.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'us' straight to 'cluster'."),
    (8, 'Операция «Золотой ярд».', "'Operation Golden Billion.' The slang noun 'yard' is short for 'milliard', a billion. Kruglov nods."),
    (9, 'А, точно. Перепутал.', "'Oh, right. I mixed them up.' In spoken Russian, word order is flexible: 'right' comes first to set the focus, followed by 'mixed up'."),
    (9, 'Такое в стране творится! Продолжаем операцию.', "'So much is going on in the country! Continue the operation.' Lavrov answers briskly."),
    (10, None, "'Yes, sir.' In the military, literally 'there is!'. Before signing off, Kruglov remembers someone else from their office."),
    (11, 'А где этот маленький, который из архива?', "'And where is that short man from the archives?' He means Major Sokolov, the short archivist who visited Moscow in Episode 2."),
    (11, 'Это же у вас?', "'Is he at your branch?' Literally 'that is by you, right?'."),
    (12, None, "'Yes indeed, Comrade General.' Literally that means 'so exact, exactly so', and Kruglov taps the side of his head proudly."),
    (13, 'Я всё помню!', "'I remember everything!' Kruglov boasts proudly."),
    (13, 'Почему не было?', "'Why wasn't he there?' The line opens with 'why' and lands on 'meeting' at the end for emphasis."),
    (13, 'Чтобы в следующий раз был!', "'Make sure he's there next time!' Literally 'so that in the next time he was!'. And with that, the general wraps up."),
    (14, 'Всё, давайте.', "'Alright, carry on.' He waves toward the camera."),
    (14, 'У меня перерыв на обед.', "'I have my lunch break.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'me' straight to 'lunch'."),
]
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = "So after confusing Sineozersk with a poisoning case in the Urals, General Kruglov orders Lavrov to continue Operation Golden Billion — and insists that the short officer from the archives attend the next briefing. See you next time!"
CLOSING = ("lavrov", "Пока!")
