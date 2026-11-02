# Authoring module for domashniy-arest-s01e01-scene-04.
ID = 'domashniy-arest-s01e01-scene-04'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 4
TITLE = 'Стена монастыря  (The Monastery Wall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина', 'pasha': 'Паша'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "We're still on the square in front of the town hall. Last time, Mayor Arkady told the crowd he grew up in a communal flat and announced he'll run for a second term. Now a young lecturer, Marina, and her students block his way: an old monastery wall is being knocked down, and they blame him. Let's listen in Russian first."
OPENER = "Let's take it slowly. Arkady stops his driver and turns to the woman with the papers."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = "So that's Arkady: one face for the crowd, and quite another for his deputy. When you watch, listen for Marina's 'Don't lie', you'll catch it now. See you next time!"
CLOSING = ('marina', 'До свидания!')
STORY = [
    ('arkady', 'Простите, вы кто?', 'Excuse me, who are you?', [(125, 'кто')], "'Вы, собственно, кто?' simplified; 'Простите' added"),
    ('marina', 'Я Марина Сергеевна. А это мои студенты.', "I'm Marina the directorevna. And these are my students.", [(126, 'Марина Сергеевна'), (128, 'А это мои студенты')], "surname 'Валинкина' dropped"),
    ('arkady', 'Очень приятно. А в чём дело?', "Pleased to meet you. So what's the matter?", [(129, 'Очень приятно'), (130, 'в чем')], "'И в чём, собственно, дело?' simplified"),
    ('marina', 'А вы не знаете?', "Don't you know?", [(131, 'А вы не знаете')], ''),
    ('arkady', 'Нет, я не знаю.', "No, I don't.", [(132, 'Нет, я не знаю')], ''),
    ('marina', 'Не надо врать. Стену монастыря сносят!', "Don't lie. They're pulling down the monastery wall!", [(133, 'Не надо врать'), (134, 'сносят'), (139, 'монастыря')], "cues 134 and 139 combined: 'сносят культурный памятник' + 'Стену ... монастыря'"),
    ('marina', 'Там хотят построить торговый центр.', 'They want to build a shopping centre there.', [(135, 'хотят построить торговый центр')], "'на его месте' -> 'Там'"),
    ('arkady', 'Этого не может быть. Это наша история.', "That can't be. It's our history.", [(145, 'Этого не может быть'), (147, 'Это наша история')], ''),
    ('arkady', 'Как странно, я ничего об этом не слышал.', "How strange, I've heard nothing about it.", [(152, 'Как странно, я ничего об этом не слышал')], ''),
    ('arkady', 'Павел Юрьевич, это что такое?', 'Pavel Yuryevich, what is this?', [(154, 'Павел Юрьевич, это что такое')], ''),
    ('pasha', 'Мы просто не хотели вас беспокоить. Всё отменим!', "We just didn't want to bother you. We'll cancel it all!", [(156, 'Просто не хотели вас беспокоить'), (164, 'Все отменим')], "'Мы' added"),
    ('arkady', 'Марина, я вам обещаю: со стеной ничего не случится.', 'Marina, I promise you: nothing will happen to the wall.', [(166, 'Марина, обещаю'), (167, 'ничего не случится')], "'с нашей исторической ценностью' -> 'со стеной'; 'я вам' word order made simple"),
    ('marina', 'Хорошо. Мы со студентами проследим.', 'All right. My students and I will keep an eye on it.', [(168, 'со студентами'), (169, 'мы проследим')], "'Хорошо.' new"),
    ('arkady', 'Это правильно. Я приглашаю вас в общественный совет.', "That's right. I'm inviting you onto the public council.", [(170, 'это правильно'), (171, 'я приглашаю вас'), (171, 'в общественный совет')], "'войти' dropped"),
    ('arkady', 'Спасибо вам, Марина. Извините, тороплюсь.', "Thank you, Marina. Sorry, I'm in a hurry.", [(174, 'Спасибо вам, Марина'), (175, 'Извините, тороплюсь')], ''),
    ('arkady', 'Паша, я больше не хочу о ней слышать. Понял?', "Pasha, I don't want to hear about her again. Understood?", [(177, 'понял')], "cue 177 'Сделай так, чтоб я о ней больше не слышал никогда' simplified; crude cue 176 dropped"),
    ('pasha', 'Сделаю.', "I'll take care of it.", [(178, 'Сделаю')], ''),
    ('arkady', 'И не тяни с торговым центром!', "And don't drag your feet with the shopping centre!", [(179, 'с торговым центром')], "'не затягивайтесь' -> 'не тяни' (ты, in private); crude cue 180 dropped"),
]
WALK = [
    (0, None, "'Excuse me, who are you?' \"Prostite\" politely says 'excuse me', followed by formal \"vy kto?\" ('you who?') since she's a stranger. She introduces herself."),
    (1, 'Я Марина Сергеевна.', "'I'm Marina the directorevna.' Russian needs no 'am' here: just \"ya\" ('I') plus her name and patronymic \"the directorevna\" ('daughter of the director'). Then she points at the young people."),
    (1, 'А это мои студенты.', "'And these are my students.' \"Eto\" ('this' or 'these') stays unchanged whether you introduce one person or a whole crowd. Arkady stays charming."),
    (2, None, "'Pleased to meet you. So what's the matter?' \"Ochen priyatno\" ('very pleasant') is the standard reply when meeting someone, and \"v chyom delo?\" asks 'what's going on?'. Marina can't believe he's asking."),
    (3, None, "'Don't you know?' Leading with \"a\" in \"a vy ne znayete?\" gives a sceptical edge, like 'oh, and you don't know?'. Arkady keeps a straight face."),
    (4, None, "'No, I don't.' Literally, 'No, I don't know' — Russian repeats \"ne znayu\" rather than stopping at 'I don't'. Marina isn't buying it."),
    (5, 'Не надо врать.', "'Don't lie.' \"Ne nado\" ('no need to') before \"vrat\" ('to lie') is a firm everyday way to tell someone to stop. Then comes the accusation."),
    (5, 'Стену монастыря сносят!', "'They're pulling down the monastery wall!' \"Snosyat\" has no 'they' in front — its plural ending alone means 'people are demolishing it', with \"stenu\" ('wall') thrust first."),
    (6, None, "'They want to build a shopping centre there.' Again \"khotyat\" ('they want') drops any pronoun, followed straight by \"postroit\" ('to build'). Now Arkady acts shocked."),
    (7, None, "'That can't be. It's our history.' \"Etogo ne mozhet byt\" is a fixed exclamation for 'that's impossible!'. Then he plays innocent."),
    (8, None, "'How strange, I've heard nothing about it.' Russian pairs \"nichego\" ('nothing') with \"ne slyshal\" ('didn't hear'), doubling the negative on purpose. Next he turns on his deputy in public."),
    (9, None, "'Pavel Yuryevich, what is this?' Calling Pasha by his full formal \"Pavel Yuryevich\" in front of the crowd lets the boss scold him theatrically. Pasha plays along."),
    (10, None, "'We just didn't want to bother you. We'll cancel it all!' \"Prosto\" softens it with 'just', and \"vsyo otmenim!\" promises 'we'll cancel everything!'. Arkady makes Marina a promise."),
    (11, None, "'Marina, I promise you: nothing will happen to the wall.' After \"so\" ('with'), \"stena\" ('wall') shifts to \"so stenoy\", paired once more with double-negative \"nichego ne sluchitsya\"."),
    (12, None, "'All right. My students and I will keep an eye on it.' Notice \"my so studentami\" — literally 'we with the students', which is how Russian says 'my students and I'."),
    (13, None, "'That's right. I'm inviting you onto the public council.' \"Priglashayu vas\" ('I invite you') sounds like an official honour while keeping a troublemaker close. Then he excuses himself."),
    (14, None, "'Thank you, Marina. Sorry, I'm in a hurry.' \"Toroplyus\" packs 'I'm in a hurry' into a single word. Once the crowd is behind him, though, his tone flips."),
    (15, None, "'Pasha, I don't want to hear about her again. Understood?' Now \"Pavel Yuryevich\" shrinks back to \"Pasha\", capped by sharp \"ponyal?\" ('got it?'). Pasha knows what that means."),
    (16, None, "'I'll take care of it.' single-word \"sdelayu\" literally says 'I'll get it done', completing \"delat\" ('to do') with an 's-' prefix. One last order follows."),
    (17, None, "'And don't drag your feet with the shopping centre!' \"Ne tyani\" literally means 'don't pull' or 'don't drag it out' — proof the wall was never safe at all."),
]
