# Authoring module for domashniy-arest-s01e03-scene-13.
ID = 'domashniy-arest-s01e03-scene-13'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 13
TITLE = 'Восемь лет вместо двенадцати  (Eight Years Instead of Twelve)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'golovkin': 'Головкин'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Last time, in a hardware shop, Nina scolded Samson for wanting a fishing rod and made him pick garden shears to scare Arkady. Back in Arkady's room in the communal flat, his new stuttering public defender, Danila Golovkin, has finished reading the case file and gives his legal opinion. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's walk through it. Public defender Golovkin has just looked through Arkady's papers, and his news is bleak."
TRANSITION = "Now let's hear the whole conversation again from the beginning."
OUTRO = "So eight years in prison is Golovkin's best offer, until Arkady hears the judge's name and remembers his neighbour Ilya Olegovich. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('golovkin', 'Свидетель обвинения надёжный. Нарушений я не нашёл.', 'The prosecution witness is reliable. I found no errors.', [(409, 'обвинения надежный'), (410, 'нарушений я не нашел')], "cue 409 'Свидетелю' is a slip for 'Свидетель'; 'Процессуальных' dropped"),
    ('golovkin', 'Шансов на подписку о невыезде у вас нет.', 'You have no chance of a travel ban.', [(411, 'на подписку о невыезде у вас')], "'шансы ... отсутствуют' -> 'Шансов ... нет'"),
    ('arkady', 'Скажите, а вы всегда так разговариваете?', 'Tell me, do you always talk like that?', [(412, 'Скажите, а вы всегда так разговариваете')], ''),
    ('golovkin', 'Да. Я заикаюсь.', 'Yes. I stutter.', [(413, 'Да')], "cue 413 'Я за...' completed to 'Я заикаюсь'"),
    ('arkady', 'Так вы плохой адвокат!', "Then you're a bad lawyer!", [(415, 'Так вы')], "cue 415 'профнепригодный' (professionally unfit) simplified to 'плохой адвокат'"),
    ('golovkin', 'Главное в нашем деле — умение работать с документами.', 'The main thing in our work is knowing how to work with documents.', [(417, 'Главное в нашем деле'), (418, 'умение'), (419, 'работать с документами')], ''),
    ('golovkin', 'И вообще я могу уйти. Мне за вас мало платят.', 'And anyway, I can leave. They pay me very little for you.', [(421, 'И вообще я'), (422, 'могу уйти'), (426, 'Мне за вас')], "cue 426 'гроши' (peanuts) -> 'мало платят'"),
    ('arkady', 'Послушайте, сядьте. Сядьте, пожалуйста.', 'Listen, sit down. Sit down, please.', [(423, 'Послушайте, сядьте'), (424, 'Сядьте')], "'пожалуйста' added"),
    ('arkady', 'Так, ладно. Что делать будем, Головкин?', 'Right, fine. What are we going to do, Golovkin?', [(427, 'Так, ладно'), (428, 'Что делать будем, Головкин')], ''),
    ('arkady', 'Как будем строить нашу защиту?', 'How are we going to build our defence?', [(429, 'Как будем строить нашу защиту')], ''),
    ('golovkin', 'Предлагаю чистосердечное признание. Дадут всего восемь лет.', "I suggest a full confession. They'll give you only eight years.", [(430, 'Предлагаю чистосердечное признание')], "cue 431 '8 лет' written out as words"),
    ('arkady', 'Ты что, смеёшься надо мной? Какие восемь лет?', 'What, are you laughing at me? What do you mean, eight years?', [(432, 'смеешься надо мной')], "'Ты' added; cue 433 '8 лет' written out as words"),
    ('golovkin', 'Это гораздо лучше, чем двенадцать лет. Согласитесь?', "That's much better than twelve years. Don't you agree?", [(434, 'гораздо лучше, чем'), (435, 'Согласитесь')], "cue 434 '12 лет' written out as words"),
    ('arkady', 'Подождите. А кто судья?', 'Wait. And who is the judge?', [(436, 'Кто судья')], "'Подождите. А' added"),
    ('golovkin', 'Председатель городского суда. Илья Олегович Берг.', 'The chairman of the city court. Ilya Olegovich Berg.', [(437, 'Председатель'), (439, 'Илья Олегович')], "abbrev. 'горсуда' -> 'городского суда'; 'Берг' from cue 438"),
    ('arkady', 'Берг? Илюша? Так это же мой сосед!', "Berg? Ilyusha? Why, that's my neighbour!", [(438, 'Берг? Илюша'), (440, 'Так это же мой сосед')], ''),
]
WALK = [
    (0, 'Свидетель обвинения надёжный.', "'The prosecution witness is reliable.' Literally 'the witness of the accusation'. That second word is in the 'of' form, the 'of'-form."),
    (0, 'Нарушений я не нашёл.', "'I found no errors.' Literally 'of violations I did not find'. Because the action word is negated, 'violations' goes into the plural 'of' form, and he puts it first for emphasis."),
    (1, None, "'You have no chance of a travel ban.' Again, 'no chances' uses the plural 'of' form with the word for 'there is not'. A signed promise not to leave town is what Arkady was hoping for instead of house arrest. Instead of arguing law, Arkady mocks the way Golovkin speaks."),
    (2, None, "'Tell me, do you always talk like that?' He uses the polite 'you', but the question is rude. Golovkin answers plainly."),
    (3, None, "'Yes. I stutter.' The action word has the '-sya' form at the end. Arkady pounces on it."),
    (4, None, "'Then you're a bad lawyer!' In response, Golovkin defends his profession with quiet dignity."),
    (5, None, "'The main thing in our work is knowing how to work with documents.' In Russian a dash stands in for 'is' between two words. Then Golovkin gets up to leave."),
    (6, 'И вообще я могу уйти.', "'And anyway, I can leave.' 'I can' is followed by the dictionary form 'to leave'."),
    (6, 'Мне за вас мало платят.', "'They pay me very little for you.' Because he is a state-appointed defender, the state pays him tiny fees. Arkady realises he has no other lawyer and quickly changes his tone."),
    (7, None, "'Listen, sit down. Sit down, please.' Both commands carry the polite plural ending. Then Arkady sits down to business."),
    (8, None, "'Right, fine. What are we going to do, Golovkin?' Literally 'what to do will we'. He continues."),
    (9, None, "'How are we going to build our defence?' Notice how Russian forms the future of an ongoing action: the future of 'to be' plus the dictionary form 'to build'. Golovkin gives his grand strategy."),
    (10, 'Предлагаю чистосердечное признание.', "'I suggest a full confession.' The long describing word literally means 'pure-hearted' — the standard legal phrase for confessing everything."),
    (10, 'Дадут всего восемь лет.', "'They'll give you only eight years.' 'Only' here is a little word that means 'in total, merely'. After numbers from five upwards, 'years' takes the special plural 'of' form form. Arkady is outraged and drops straight to the informal 'you'."),
    (11, 'Ты что, смеёшься надо мной?', "'What, are you laughing at me?' The action word 'to laugh' takes the little word 'over' plus the 'with/as' form: 'over me'."),
    (11, 'Какие восемь лет?', "'What do you mean, eight years?' Literally 'what kind of eight years?'. Golovkin stays calm."),
    (12, None, "'That's much better than twelve years. Don't you agree?' 'Much better' uses a word that strengthens comparisons. Then Arkady thinks of another angle."),
    (13, None, "'Wait. And who is the judge?' Arkady answers."),
    (14, None, "'The chairman of the city court. Ilya Olegovich Berg.' 'Of the city court' is in the 'of' form after 'chairman'. And suddenly Arkady's face lights up."),
    (15, None, "'Berg? Ilyusha? Why, that's my neighbour!' 'Ilyusha' is the warm diminutive of Ilya. In their rich cottage village, the judge lives right next door to Arkady."),
]
