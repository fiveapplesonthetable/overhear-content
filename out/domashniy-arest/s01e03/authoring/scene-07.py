# domashniy-arest/s01e03/scene-07.py
ID = "domashniy-arest-s01e03-scene-07"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = "Прогулка с Лютиком  (Walking Lyutik)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "judge": "anja"}
LABELS = {"judge": "Илья Олегович"}
INTRO = "Out in the park, while Samson was trying to scare Arkady in the flat. Pasha is walking with Judge Ilya Olegovich Berg, who is supposed to hear Arkady's appeal that evening, but the judge keeps running after his daughter's tiny white dog, Lyutik. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("judge", "А нельзя никак отменить это заседание?", "Is there no way to cancel this hearing?", [(264, 'А нельзя никак отменить это заседание')], ""),
    ("judge", "Ну как я его отменю? Это решение прокуратуры.", "Well, how can I cancel it? It's the prosecutor's decision.", [(265, 'как я его отменю')], "'если прокуратура постановила' simplified to 'Это решение прокуратуры'"),
    ("judge", "Лютик, Лютик! Фу! Что ты там делаешь? Лютик, стой!", "Lyutik, Lyutik! Drop it! What are you doing there? Lyutik, stop!", [(266, 'Лютик, Лютик'), (267, 'Фу'), (268, 'Что ты там делаешь'), (269, 'Лютик, стой')], ""),
    ("judge", "Илья Олегович, пожалуйста! Вы можете меня послушать две минуты?", "Ilya Olegovich, please! Can you listen to me for two minutes?", [(270, 'Илья Олегович, пожалуйста'), (271, 'Вы можете'), (271, 'послушать'), (271, 'две минуты')], "slip 'мне' in cue 271 corrected to 'меня'; 'хотя бы' dropped"),
    ("judge", "Да, конечно. Подождите, сейчас, секундочку.", "Yes, of course. Wait, just now, one little second.", [(272, 'Да, конечно'), (274, 'Подождите, сейчас, секундочку')], ""),
    ("judge", "Лютик, где ты это находишь? Что он опять съел?", "Lyutik, where do you find this stuff? What did he eat again?", [(276, 'Лютик'), (277, 'ты это находишь'), (281, 'Что он съел')], "'Где ж ... -то' simplified; 'опять' added; 'Что это за вонь?' dropped"),
    ("judge", "Илья Олегович! Я не могу гулять здесь целый день.", "Ilya Olegovich! I can't walk around here all day.", [(278, 'Илья Олегович'), (280, 'Я не могу'), (280, 'гулять целый день')], "'с тобой здесь' -> 'здесь'"),
    ("judge", "Простите, это собака дочери. Я с ней гуляю пока.", "Sorry, it's my daughter's dog. I'm walking her for now.", [(282, 'Простите, это собака дочери, я с ней гуляю пока')], "split into two sentences"),
    ("judge", "Да подожди ты со своей собакой!", "Oh, wait a minute with your dog!", [(283, 'Да подожди ты со своей собакой')], ""),
    ("judge", "Ты мне Аникеева оставь лучше под домашним арестом.", "You just keep Anikeev under house arrest for me.", [(284, 'Ты мне Аникеева оставь лучше под домашним арестом')], ""),
    ("judge", "Павел Юрьевич, я бы оставил. Но этот Мишкин нас просто раскатал.", "Pavel Yuryevich, I would keep him. But that Mishkin simply flattened us.", [(285, 'Павел Юрьевич, я бы оставил'), (286, 'Но этот Мишкин нас просто раскатал')], ""),
    ("judge", "Там столько ошибок! Мы же всё быстро делали.", "There are so many mistakes there! After all, we did everything in a hurry.", [(287, 'Там столько'), (287, 'мы же все'), (287, 'делали')], "'процессуальных нарушений' -> 'ошибок'; 'на скорую руку' -> 'быстро'"),
    ("judge", "Не волнуйся ты насчёт этого Мишкина. Работаем мы с ним.", "Don't you worry about that Mishkin. We're working on him.", [(289, 'Не волнуйся ты насчет этого Мишкина, работаем мы с ним')], "split into two sentences"),
    ("judge", "Ты, главное, оставь его дома.", "The main thing is, you keep him at home.", [(290, 'Ты главное')], "'меру пресечения не меняй' simplified to 'оставь его дома'"),
]
OPENER = "Let's take it line by line. Pasha is trying to talk about the evening court hearing, which Arkady's Moscow lawyer arranged in Scene 1."
WALK = [
    (0, None, "'Is there no way to cancel this hearing?' Literally, 'is it impossible in no way to cancel?'. Russian loves double negatives for emphasis. The judge shakes his head."),
    (1, 'Ну как я его отменю?', "'Well, how can I cancel it?' Literally, 'how will I cancel it?'. The pronoun 'him' refers to the hearing."),
    (1, 'Это решение прокуратуры.', "'It's the prosecutor's decision.' Before Pasha can answer, the little dog spots something in the grass."),
    (2, None, "'Lyutik, Lyutik! Drop it! What are you doing there? Lyutik, stop!' The dog's name means 'Buttercup'. The short command after his name is what Russian dog owners say for 'drop it, leave it alone!'. Pasha is losing patience."),
    (3, None, "'Ilya Olegovich, please! Can you listen to me for two minutes?' Notice that Pasha starts with the polite 'you' and the judge's name and father's name. After the number 'two', the feminine word 'minute' takes the singular 'of' ending."),
    (4, None, "'Yes, of course. Wait, just now, one little second.' The last word is a soft, affectionate form of 'second'. And he is off after the dog again."),
    (5, None, "'Lyutik, where do you find this stuff? What did he eat again?' First he talks to the dog as 'you', and then to Pasha about the dog as 'he'. Pasha has had enough of the walk."),
    (6, None, "'Ilya Olegovich! I can't walk around here all day.' 'All day' is literally 'a whole day', in the object form for how long something lasts. The judge apologises."),
    (7, 'Простите, это собака дочери.', "'Sorry, it's my daughter's dog.' Literally, 'dog of daughter'."),
    (7, 'Я с ней гуляю пока.', "'I'm walking her for now.' Even though Buttercup is a boy dog, the Russian word for 'dog' is feminine, so the judge says 'with her'. At that, Pasha drops the polite 'you' altogether."),
    (8, None, "'Oh, wait a minute with your dog!' Now it's the informal command 'wait' and the informal 'you': Pasha is showing who is really the boss here. And he gives the judge his order."),
    (9, None, "'You just keep Anikeev under house arrest for me.' Literally, 'you to me Anikeev leave better under house arrest'. The title of the show appears right here in the 'with/as' form after 'under'. The judge looks worried."),
    (10, 'Павел Юрьевич, я бы оставил.', "'Pavel Yuryevich, I would keep him.' Adding the little particle 'would' to a past-tense verb makes the conditional: 'I would leave him'."),
    (10, 'Но этот Мишкин нас просто раскатал.', "'But that Mishkin simply flattened us.' Literally, 'rolled us out flat', like pastry dough. Mishkin is the expensive Moscow lawyer from Scene 1."),
    (11, None, "'There are so many mistakes there! After all, we did everything in a hurry.' After 'so many', the word 'mistakes' takes the plural 'of' form. Pasha tells him not to worry about the Moscow lawyer."),
    (12, None, "'Don't you worry about that Mishkin. We're working on him.' Literally, 'we are working with him', an ominous way to say they are already dealing with the lawyer."),
    (13, None, "'The main thing is, you keep him at home.' The same command 'leave, keep' once again."),
]
TRANSITION = "Let's hear the whole conversation in the park once more."
OUTRO = "So Pasha promises to deal with the Moscow lawyer himself, as long as Judge Berg keeps Arkady locked up at home. Next we check back on Samson and Nina in the communal flat; see you then. See you next time!"
CLOSING = ("judge", "Пока!")
