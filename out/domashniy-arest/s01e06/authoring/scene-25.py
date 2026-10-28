# Authoring module for domashniy-arest-s01e06-scene-25.
ID = 'domashniy-arest-s01e06-scene-25'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 25
TITLE = 'Я немножко преувеличил  (I Exaggerated a Little)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'dean': 'Эдуард Владимирович', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "In Marina's candlelit room in the communal flat. Now Marina welcomes her former dean Eduard to her table, believing he has finally left his wife for her. Let's listen in Russian first."
OPENER = "Let's go through the scene line by line. Marina has lit candles and set the table in her room to welcome Eduard."
TRANSITION = "Now let's hear the whole scene again, from start to finish."
OUTRO = "So a single phone call from the airport exposed Eduard's lie about leaving his wife, leaving Marina alone at her candlelit table with her cake and champagne. See you next time!"
CLOSING = ('dean', 'Пока!')
STORY = [
    ('marina', 'Я вообще не думала, что ты это сделаешь.', "I didn't think at all that you would do this.", [(893, 'Я вообще не думала, что ты')], "garbled 'этого делаешь' -> 'это сделаешь'"),
    ('dean', 'Я это сделал! Я всё сказал жене.', 'I did it! I told my wife everything.', [(894, 'Я это сделал')], "'Я всё сказал жене' added for context"),
    ('marina', 'Я торт приготовила. Ты любишь сладкое?', 'I made a cake. Do you like sweet things?', [(895, 'Ты любишь'), (897, 'Я')], "'тортик приготовлю' -> 'торт приготовила' (A1)"),
    ('dean', 'Ты, Марина, самый сладкий мой торт! Ой, телефон.', 'You, Marina, are my sweetest cake! Oh, the phone.', [(898, 'Ты'), (899, 'самый сладкий мой')], "'Мариночка ... тортик' -> 'Марина ... торт'"),
    ('dean', 'Да, Аллочка? Как ты не улетела? Почему?', "Yes, Allochka? What do you mean you didn't fly out? Why?", [(904, 'Да, Аллочка'), (905, 'Как'), (905, 'не улетела'), (906, 'Почему')], ''),
    ('dean', 'Ой, плохая еда? Живот болит?', 'Oh, bad food? Does your stomach hurt?', [(907, 'О')], "'отравилась?' (907) -> 'плохая еда? Живот болит?' (A1)"),
    ('dean', 'Нет, я дома! Я просто вышел в магазин.', "No, I'm at home! I just stepped out to the shop.", [(909, 'Нет'), (909, 'я'), (910, 'в магазин')], "'здесь ... выскочил' -> 'дома ... просто вышел' (A1)"),
    ('dean', 'Я сейчас буду! Может быть, в аптеке лекарство купить?', "I'll be right there! Maybe I should buy medicine at the pharmacy?", [(911, 'Я сейчас буду'), (913, 'Может быть, в аптеке'), (913, 'купить')], "'что-то' -> 'лекарство' (A1)"),
    ('dean', 'Хорошо, я бегу! Скоро буду.', "Okay, I'm running! I'll be there soon.", [(912, 'скоро буду'), (915, 'Хорошо, я бегу')], ''),
    ('dean', 'Марина, ну что ты так смотришь на меня?', 'Marina, why are you looking at me like that?', [(919, 'что ты так смотришь на меня')], "'Марин, ну, солнышко' -> 'Марина, ну'"),
    ('dean', 'Прости меня, я немножко преувеличил.', 'Forgive me, I exaggerated a little.', [(920, 'прости меня, я немножко преувеличил')], ''),
    ('dean', 'Но я ей скоро всё расскажу про нас!', 'But I will tell her everything about us soon!', [(921, 'но я ей все расскажу'), (922, 'Скоро все расскажу про нас')], ''),
    ('dean', 'Скажи быстро, что ты не сердишься на меня.', 'Say quickly that you are not angry with me.', [(923, 'быстро'), (923, 'что ты не сердишься на меня'), (924, 'скажи')], ''),
    ('marina', 'Не сержусь.', "I'm not angry.", [(925, 'Не')], "colloquial 'сердюсь' -> standard 'сержусь'"),
    ('dean', 'Ну, всё, прекрасно! Я побежал, Марина!', "Well, that's it, wonderful! I'm off, Marina!", [(926, 'Ну, все, прекрасно'), (927, 'Я побежал, Марина')], ''),
]
WALK = [
    (0, None, "'I didn't think at all that you would do this.' Russian uses the future tense 'you will do' inside the clause after a past-tense verb of thinking."),
    (1, None, "'I did it! I told my wife everything.' Eduard puffs out his chest, claiming he finally told his wife Alla that he is leaving her."),
    (2, None, "'I made a cake. Do you like sweet things?' The neuter singular adjective 'sweet' is used on its own as a noun meaning 'sweets, sweet things'."),
    (3, None, "'You, Marina, are my sweetest cake! Oh, the phone.' Just as he leans across the candlelit table, his mobile phone rings in his pocket."),
    (4, None, "'Yes, Allochka? What do you mean you didn't fly out? Why?' It is his wife Alla, using the affectionate diminutive of her name, and the verb 'flew away' has the prefix 'u-' for departing."),
    (5, None, "'Oh, bad food? Does your stomach hurt?' Alla had only gone to the airport for a trip, and now she is coming back home after getting food poisoning at the airport!"),
    (6, None, "'No, I'm at home! I just stepped out to the shop.' Eduard immediately panics and lies to his wife that he is right near home."),
    (7, None, "'I'll be right there! Maybe I should buy medicine at the pharmacy?' Literally, 'I now will be', the standard Russian way to say 'I'll be right there'."),
    (8, None, "'Okay, I'm running! I'll be there soon.' He puts his phone away and sees Marina staring at him in icy silence."),
    (9, None, "'Marina, why are you looking at me like that?' The verb 'to look' is followed by the preposition 'on, at' with the direct-object form."),
    (10, None, "'Forgive me, I exaggerated a little.' He hadn't left his wife at all—he had just taken advantage of her trip to spend a free evening with Marina!"),
    (11, None, "'But I will tell her everything about us soon!' After the colloquial preposition 'about', the pronoun 'us' stands in the direct-object form."),
    (12, None, "'Say quickly that you are not angry with me.' The self-action verb form 'to be angry' takes the preposition 'on, at' with the direct-object form."),
    (13, None, "'I'm not angry.' In the first-person singular, the stem consonant 'd' changes to 'zh'. Marina answers in a flat, heartbroken voice."),
    (14, None, "'Well, that's it, wonderful! I'm off, Marina!' Literally, 'I started running', and Eduard grabs his coat and bolts out the door back to his wife."),
]
