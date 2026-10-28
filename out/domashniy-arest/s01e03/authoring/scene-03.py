# domashniy-arest/s01e03/scene-03.py
ID = "domashniy-arest-s01e03-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 3
TITLE = "Надо поставить жучок  (We Need to Plant a Bug)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "lavrov": "anja", "zavarzin": "angelina"}
LABELS = {"lavrov": "Лавров", "zavarzin": "Заварзин"}
INTRO = "Across the street from the communal flat, a few minutes later. Now we check in on the two Moscow security-service agents, Major Lavrov and Captain Zavarzin, who are freezing in a bare room opposite the flat and trying to listen to Arkady with a directional microphone. Let's listen in Russian first."
STORY = [
    ("zavarzin", "Холодно тут! Даже печку поставить не могут.", "It's cold in here! They can't even put a heater in.", [(118, 'печку поставить не могут')], "cue 118 cleaned up"),
    ("lavrov", "Тихо! Сейчас всё прогреется.", "Quiet! Everything will warm up in a moment.", [(117, 'Все прогреется')], "'Тихо! Сейчас' added"),
    ("zavarzin", "О, наконец тепло! Слава богу. Сейчас ещё чай сделаю.", "Oh, it's warm at last! Thank goodness. Now I'll make some tea too.", [(125, 'Слава богу'), (126, 'Сейчас еще')], "slang 'пошла жара в хату' -> 'наконец тепло'; 'чайку' -> 'чай сделаю'"),
    ("lavrov", "Ты что, голову в Москве оставил?", "What, did you leave your head in Moscow?", [(127, 'Ты что, голову в Москве')], "cue 127 has the transcription slip 'ставил' for 'оставил'"),
    ("lavrov", "Я тебе сто раз говорил! Нельзя вместе включать обогреватель и чайник.", "I've told you a hundred times! You can't turn on the heater and the kettle together.", [(128, 'Я тебе сто раз говорил, нельзя вместе')], "'врубать' -> 'включать'; cue 128 garbles 'чайник' as 'чайки'"),
    ("zavarzin", "Сейчас, товарищ майор, всё нормально. Включаем микрофон.", "Just a moment, Comrade Major, everything's fine. Switching on the microphone.", [(130, 'Нормально'), (134, 'Товарищ майор'), (136, 'Сейчас'), (138, 'Включаем')], "'микрофон' added for clarity"),
    ("lavrov", "У нас ведь второй этаж, да? Давай, слушаем.", "Ours is the second floor, right? Go on, let's listen.", [(136, 'У нас ведь второй этаж, да')], "'Давай, слушаем' added"),
    ("zavarzin", "Алло, Танечка! В свои годы это нормально.", "Hello, Tanechka! At my age that's normal.", [(140, 'Танечка'), (142, 'Свои годы это нормально'), (144, 'Алло')], "overheard on the microphone: old Klavdia chatting to a friend on the phone"),
    ("zavarzin", "Чернослив я уже ела. Ничего не помогает!", "I've already eaten prunes. Nothing helps!", [(145, 'Чернослив я уже ела')], "'Ничего не помогает' added"),
    ("lavrov", "Так, ты можешь убрать весь этот шум? Нам нужен только Аникеев.", "Right, can you cut out all this noise? We only need Anikeev.", [(146, 'Так, ты можешь'), (146, 'весь этот'), (147, 'Нам'), (147, 'нужен')], "'отсечь весь этот мусор' -> 'убрать весь этот шум'; code name 'комар' -> 'Аникеев'"),
    ("zavarzin", "Товарищ майор, тут всё очень плохо слышно. Качества всё равно не будет.", "Comrade Major, you can barely hear anything here. There won't be any quality anyway.", [(134, 'Товарищ майор'), (148, 'качества все равно не будет')], "clean stand-in for cue 134 + cue 148"),
    ("lavrov", "Значит, надо жучок поставить.", "Then we need to plant a bug.", [(149, 'Надо жучок')], "cue 149 'вставить' -> 'поставить'"),
    ("zavarzin", "Понял. Марина Сергеевна нам поможет.", "Understood. Marina Sergeyevna will help us.", [], "new: sets up scene 5, where they hand the bug to Marina"),
]
OPENER = "Let's go back through the scene. Major Lavrov and Captain Zavarzin are sitting in a freezing room across from the communal flat, and Zavarzin is complaining."
WALK = [
    (0, None, "'It's cold in here! They can't even put a heater in.' The word he uses for 'heater' is the everyday word for a stove. Major Lavrov tells him to be patient, because they have plugged in an electric radiator."),
    (1, None, "'Quiet! Everything will warm up in a moment.' A moment later the heater starts working."),
    (2, None, "'Oh, it's warm at last! Thank goodness. Now I'll make some tea too.' And with that, Zavarzin switches on the electric kettle at the same time—and trips the fuse, plunging the room into darkness."),
    (3, None, "'What, did you leave your head in Moscow?' After 'in', the name Moscow takes the location ending."),
    (4, 'Я тебе сто раз говорил!', "'I've told you a hundred times!' Literally 'I to you a hundred of times said'."),
    (4, 'Нельзя вместе включать обогреватель и чайник.', "'You can't turn on the heater and the kettle together.' The first word means 'it is not allowed' or 'one cannot', followed by the basic verb form. Once the power is back on, Zavarzin aims their directional microphone at the windows of the communal flat."),
    (5, None, "'Just a moment, Comrade Major, everything's fine. Switching on the microphone.' Literally 'we switch on'."),
    (6, None, "'Ours is the second floor, right? Go on, let's listen.' First they catch a snippet of Marina telling her ex on the phone that she doesn't want to see him, and then they hear the old neighbour, Klavdia Viktorovna, discussing her digestion with a friend."),
    (7, None, "'Hello, Tanechka! At my age that's normal.' The word for 'hello' here is the one used only when answering the telephone."),
    (8, None, "'I've already eaten prunes. Nothing helps!' The verb 'ate' has the feminine past ending '-a', because Klavdia is a woman. Lavrov has heard quite enough about prunes."),
    (9, 'Так, ты можешь убрать весь этот шум?', "'Right, can you cut out all this noise?' Literally 'can you remove all this noise?'."),
    (9, 'Нам нужен только Аникеев.', "'We only need Anikeev.' Literally 'to us is needed only Anikeev', with the masculine short form of 'needed'."),
    (10, None, "'Comrade Major, you can barely hear anything here. There won't be any quality anyway.' After 'there won't be', the noun for 'quality' goes into the 'of' form. So Lavrov makes the call."),
    (11, None, "'Then we need to plant a bug.' The Russian word for a listening bug literally means 'little beetle'."),
    (12, None, "'Understood. Marina Sergeyevna will help us.' Remember that at the end of the last episode, Marina reluctantly agreed to help the security service."),
]
TRANSITION = "Let's hear the whole scene at the listening post once more."
OUTRO = "So the directional microphone only picks up prunes and phone calls, and the agents decide to send Marina into Arkady's room with a bug. Next we see what Pasha is offering Samson and Nina across town; see you then. See you next time!"
CLOSING = ("lavrov", "Пока!")
