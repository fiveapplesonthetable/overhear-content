# Authoring module for kukhnya-s01e10-scene-42.
ID = 'kukhnya-s01e10-scene-42'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 42
TITLE = 'Щучья афера  (The Pike Roe Scam)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'Barinov has been caught. Nagiyev wants the truth, and the chef gives it, with a bit of spin. Then the owner passes sentence. Let the Russian wash over you first.'
OPENER = 'Time to look at it properly.'
TRANSITION = 'Now, from the top, in one go.'
OUTRO = "Barinov will work a month without pay, and he owes a fine as well. That's all for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Ладно, это обычная щучья икра, Дим.', 'Fine, it is ordinary pike roe, Dim.', [(299, 'Щучья.')], ''),
    ('barinov', 'Учёные говорят, что она даже полезнее чёрной!', 'Scientists say it is even healthier than black!', [(300, 'Ученые говорят, что она даже полезнее.')], ''),
    ('barinov', 'Извини, мы не смогли достать нормальную вовремя.', 'Sorry, we could not get decent one in time.', [(301, 'Ну, извини, Дим, не смогли достать нормальную.')], ''),
    ('barinov', 'Поэтому я решил немного покрасить её.', 'Therefore I decided to dye it a little.', [(302, 'Ну, я подумал, что если так...')], ''),
    ('nagiyev', 'Если твоя афера всплывёт, тебя просто убьют!', 'If your scam surfaces, they will simply kill you!', [(303, 'Если твоя афера всплывет, тебя, скорее всего, убьют.')], ''),
    ('nagiyev', 'Тебя убьют и закопают в лесу.', 'They will kill you and bury you in the woods.', [(304, 'Убьют и закопают.')], ''),
    ('nagiyev', 'Я даже не буду плакать на могиле.', 'I will not even weep at your grave.', [(304, 'Я даже не буду плакать на твоей могиле.')], ''),
    ('nagiyev', 'А если не всплывёт, ты настоящий везунчик.', 'And if it does not surface, you are a real lucky guy.', [(305, 'Если не всплывет, ты везунок.')], ''),
    ('nagiyev', 'Ты будешь целый месяц работать без зарплаты!', 'You will work an entire month without salary!', [(306, 'Ты просто будешь работать месяц без зарплаты.')], ''),
    ('nagiyev', 'Я штрафую тебя на двести тысяч рублей.', 'I am fining you two hundred thousand rubles.', [(307, 'Я тебя штрафую на двести тысяч.')], ''),
    ('barinov', 'Серьёзно? На что я буду жить месяц?!', 'Seriously? On what will I live for a month?!', [(308, 'Серьезно? Да. А как же я буду жить этот месяц?')], ''),
    ('nagiyev', 'Всё, иди на кухню и не зли меня!', 'That is all, go to the kitchen and do not make me angry!', [(309, 'Все, иди. Не зли меня.')], ''),
    ('barinov', 'Слушаюсь, Дмитрий Владимирович.', 'Yes, sir, Dmitry Vladimirovich.', [], ''),
]
WALK = [
    (0, None, '\'Fine, it is ordinary pike roe, Dim.\' Russians clip a name when they call someone: "Dima" becomes "Dim". "Obychnaya shchuchya ikra" is "ordinary pike roe". Barinov gives up the pretence.'),
    (1, None, '\'Scientists say it is even healthier than black!\' "Poleznee" is "more useful", "healthier", from "polezny". There is no word for "than": "chyornoy" takes the "of" ending instead. "Uchyonye" is "scientists".'),
    (2, None, '\'Sorry, we could not get decent one in time.\' "Dostat" is "to get hold of", something hard to find. "Normalnuyu" is "normal", here "decent". "Vovremya" is "in time", as in Senya\'s "Vsyo budet gotovo vovremya".'),
    (3, None, '\'Therefore I decided to dye it a little.\' To dye is "pokrasit", the kitchen\'s "krasit" with po-. "Poetomu" is "therefore", and "reshil" is "I decided".'),
    (4, None, '\'If your scam surfaces, they will simply kill you!\' A secret that "floats up" is "vsplyvyot", the Russian picture for something coming out. "Ubyut", "they\'ll kill", has no subject, the usual way to say "someone will". Senya said the singular, "ubyot", about the chef.'),
    (5, None, '\'They will kill you and bury you in the woods.\' "V lesu" is "in the woods", from "les", with a special ending -u. "Zakopayut" is "they will bury", literally "dig in".'),
    (6, None, '\'I will not even weep at your grave.\' Nagiyev says "dazhe ne budu plakat", "I will not even cry". "Na mogile", "at the grave", is literally "on the grave", from "mogila".'),
    (7, None, '\'And if it does not surface, you are a real lucky guy.\' "Vezunchik", "lucky guy", comes from the root of "povezlo", "got lucky", in the first scene: "Tebe povezlo, chto papa spit".'),
    (8, None, '\'You will work an entire month without salary!\' "Bez zarplaty" is "without salary"; "bez" is heard in Louis\'s "bez komochkov", "without lumps". "Zarplata" was in Nagiyev\'s "Ya tebe dve zarplaty uzhe vydal".'),
    (9, None, '\'I am fining you two hundred thousand rubles.\' From "shtraf", "a fine", comes the verb "shtrafovat", and "na" gives the amount: "na dvesti tysyach". It is the exact sum Timur asked for the caviar: "S tebya rovno dvesti tysyach rubley".'),
    (10, None, '\'Seriously? On what will I live for a month?!\' "Na chto" is "on what", meaning "on what money". "Zhit" is "to live", the root of "zhizn", "life". "Seryozno?" is "seriously?".'),
    (11, None, '\'That is all, go to the kitchen and do not make me angry!\' "Vsyo" here is "that\'s it". "Ne zli menya" is "don\'t anger me", from "zloy", "angry" or "wicked". "Idi na kukhnyu" is "go to the kitchen".'),
    (12, None, '\'Yes, sir, Dmitry Vladimirovich.\' "Slushayus" is "I am listening", with -sya, and means "yes, sir": the answer to an order. Barinov uses the owner\'s first name and father\'s name.'),
]
