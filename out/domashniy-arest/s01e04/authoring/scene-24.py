# domashniy-arest/s01e04/scene-24.py
ID = "domashniy-arest-s01e04-scene-24"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 24
TITLE = "Звонок Лещенко  (Leshchenko's Call)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "klavdia": "angelina", "anya": "alisa"}
LABELS = {"klavdia": "Клавдия Викторовна", "anya": "Аркадий"}
INTRO = "Still in Klavdia Viktorovna's room a moment later. Last time, Ilona outbid Arkady's cemetery plot with a church decree for the city cathedral, and Arkady begged Klavdia to wait one second before giving up her phone. Now Arkady hurries back in holding out his own telephone: he has called his old acquaintance, Klavdia's lifelong favourite singer Lev Leshchenko. Let's listen in Russian first."
STORY = [
    ("anya", "Клавдия Викторовна, пожалуйста. С вами хотят поговорить.", "Klavdia Viktorovna, here you go. Someone wants to speak with you.", [(970, 'Клавдия Викторовна'), (971, 'Пожалуйста'), (972, 'С вами хотят поговорить')], ""),
    ("klavdia", "Лев Валерьянович! Вы меня что, помните?", "Lev Valeryanovich! Do you really remember me?", [(974, 'Лев Валерьянович'), (975, 'Вы меня что'), (976, 'помните')], ""),
    ("klavdia", "Спасибо вам! Лев Валерьянович, дорогой мой!", "Thank you! Lev Valeryanovich, my dear!", [(980, 'Спасибо'), (982, 'дорогой мой')], "cue 982 'Лев Ильянович' (subtitle slip) -> 'Лев Валерьянович'"),
    ("anya", "Спасибо, дорогой! Пока, обнимаю вас.", "Thank you, my dear! Bye, I embrace you.", [(990, 'Спасибо, дорогой'), (992, 'Пока. Обнимаю вас')], "Arkady thanks Leshchenko and hangs up"),
    ("klavdia", "Я всю жизнь работала на заводе. Всю жизнь!", "I worked my whole life at the factory. My whole life!", [(996, 'Всю жизнь работала'), (997, 'Всю жизнь')], "'на химкомбинате' -> 'на заводе' (A1)"),
    ("klavdia", "Муж тоже там работал. И рано умер.", "My husband worked there too. And he died young.", [(999, 'тоже')], "cue 999 ('Гришка тоже такой, овер в 49') simplified to A1"),
    ("klavdia", "И никто никогда мне не помогал!", "And nobody ever helped me!", [(1001, 'И никто никогда')], "'ничего' -> 'мне не помогал'"),
    ("klavdia", "Я сняла пьяного соседа на телефон. И сразу все мне помогают!", "I filmed a drunk neighbour on my phone. And right away everyone helps me!", [(1002, 'пьяного'), (1002, 'на телефон'), (1003, 'Сразу')], "cues 1002-1004 simplified into two short A1 sentences"),
    ("klavdia", "Вот он, телефон! Сами решайте, что делать. Без меня!", "Here it is, the phone! Decide for yourselves what to do. Without me!", [(1005, 'Вот он, телефон'), (1006, 'Сами решайте, что'), (1006, 'делать. Без меня')], "'с этим' dropped"),
    ("anya", "Даже мне сейчас как-то стыдно.", "Even I feel a bit ashamed right now.", [(1010, 'Даже мне сейчас как-то')], "crude cue 1009 dropped; 'трудно' (slip for 'стыдно') -> 'стыдно'"),
    ("klavdia", "И мне. Даже не понимаю, как мы так живём.", "Me too. I don't even understand how we live like this.", [(1011, 'И мне. Даже не понимаю, как мы')], "'доходим до такой жизни' -> 'так живём' (A1)"),
    ("anya", "Так, телефон! Быстро! Где телефон?", "Right, the phone! Quickly! Where is the phone?", [(1013, 'Так, телефон'), (1013, 'Телефон')], "'Живо!' -> 'Быстро! Где телефон?'"),
    ("anya", "Ты успела отправить видео?! Зачем ты это сделала?", "You managed to send the video?! Why did you do that?", [(1017, 'Ты успела')], "'переслать' -> 'отправить видео'; crude insults in 1017-1018 omitted"),
    ("klavdia", "Это моя работа. Возьмите свой телефон.", "It's my job. Take your phone.", [(1019, 'Возьмите свой телефон')], "'Это моя работа.' added"),
]
OPENER = "Let's take the scene line by line. Arkady holds out his telephone to Klavdia Viktorovna with a triumphant smile."
WALK = [
    (0, None, "'Klavdia Viktorovna, here you go. Someone wants to speak with you.' Literally, 'with you they want to talk', using the third person plural with no 'they' to mean 'someone wants to speak to you'. Klavdia hears the famous voice on the line."),
    (1, None, "'Lev Valeryanovich! Do you really remember me?' On the phone, the legendary singer warmly tells her that he remembers how she applauded at his concert and wishes her all the best."),
    (2, None, "'Thank you! Lev Valeryanovich, my dear!' Overwhelmed with emotion, she hands the phone back to Arkady."),
    (3, None, "'Thank you, my dear! Bye, I embrace you.' Arkady chats with the singer like an old friend and hangs up, sure that he has won. Instead, Klavdia Viktorovna sits down in tears."),
    (4, 'Я всю жизнь работала на заводе.', "'I worked my whole life at the factory.' The phrase 'the whole life' is in the direct-object form to show how long she worked, and 'at the factory' uses the preposition 'on'."),
    (4, 'Всю жизнь!', "'My whole life!' In the show she names the town's chemical plant, where the air ruined her lungs."),
    (5, None, "'My husband worked there too. And he died young.' Her husband Grisha died at forty-nine from the same hard work."),
    (6, None, "'And nobody ever helped me!' Notice the triple negative: 'nobody', 'never', and 'not' all stand together in a Russian negative sentence."),
    (7, 'Я сняла пьяного соседа на телефон.', "'I filmed a drunk neighbour on my phone.' The verb 'took, filmed' has the feminine past ending, and 'drunk neighbour' is in the animate object-form."),
    (7, 'И сразу все мне помогают!', "'And right away everyone helps me!' After decades of honest work that nobody noticed, one ugly video brought her two televisions, a cathedral crypt, and a phone call from her idol. She cannot bear it."),
    (8, None, "'Here it is, the phone! Decide for yourselves what to do. Without me!' She puts her phone down on the table and walks out of the room. For a quiet moment, even the two cynical politicians look ashamed."),
    (9, None, "'Even I feel a bit ashamed right now.' Again, feelings use the 'to/for' form: 'even to me now somehow it is shameful'."),
    (10, None, "'Me too. I don't even understand how we live like this.' Literally, 'and to me'. Then, in the same instant, both of them snap out of their guilt and lunge for the phone on the table."),
    (11, None, "'Right, the phone! Quickly! Where is the phone?' Ilona grabs it first, darts into the bathroom, and locks the door while she forwards the video to Pasha's headquarters. When she comes out, Arkady is furious."),
    (12, None, "'You managed to send the video?! Why did you do that?' The verb 'managed, had time to' is followed by the basic verb form 'to send'. Ilona calmly holds out the phone."),
    (13, None, "'It's my job. Take your phone.' She switches right back to the polite plural command."),
]
TRANSITION = "Let's listen to the whole scene once more, start to finish."
OUTRO = "So Klavdia Viktorovna walked away with her dignity, while Ilona managed to send the video of Samson to Pasha's headquarters. Next we see what Samson and Nina are doing that evening. See you then. See you next time!"
CLOSING = ("klavdia", "Пока!")
