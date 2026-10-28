# Authoring module for domashniy-arest-s01e01-scene-13.
ID = 'domashniy-arest-s01e01-scene-13'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 13
TITLE = 'Возьмите на работу Галилея  (Go and Hire Galileo)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'dean': 'Эдуард Владимирович', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Meanwhile, across town at the university, we meet Marina again, the lecturer who protested with her students to save the old monastery wall. Last time, Arkady was rushing off to meet a businessman in a café; now Marina hurries into her dean's office with what she thinks is wonderful news. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through it together. Marina bursts into the office, full of energy, before the dean can say a word."
TRANSITION = "Now let's hear the whole conversation once again."
OUTRO = "Well done for staying with it; there were some long words in this one. Remember Marina's last line, it's a great comeback, and we'll catch up with her soon. Goodbye for now. See you next time!"
CLOSING = ('marina', 'До свидания, Эдуард Владимирович.')
STORY = [
    ('marina', 'Эдуард Владимирович, я на минуточку. Я спасла монастырь!', "Eduard Vladimirovich, I'll only be a minute. I saved the monastery!", [(512, 'Я на минуточку'), (514, 'Я спасла'), (514, 'монастырь')], "the dean's name added as address; the town's name before 'монастырь' dropped"),
    ('dean', 'Марина Сергеевна, я уже знаю. Мне звонили из мэрии.', 'Marina Sergeyevna, I already know. The town hall called me.', [(517, 'Марина Сергеевна, я уже'), (518, 'мне звонили из мэрии')], "'в курсе этого всего' -> 'знаю'"),
    ('dean', 'Ты же знаешь, какие это мерзавцы.', 'You know what scoundrels they are.', [(520, 'Ты же знаешь, какие это мерзавцы')], ''),
    ('marina', 'Ну, что вы предлагаете?', 'So what do you suggest?', [(523, 'Ну, что')], "'предлагаешь' -> 'вы предлагаете': in the story she keeps the polite form with her dean"),
    ('dean', 'Ты преподавай. А они пусть строят свои торговые центры.', 'You teach. And let them build their shopping centres.', [(525, 'Ты преподавай'), (526, 'пусть строят свои торговые')], "'эти мерзавцы' -> 'они'; 'комплексы' -> 'центры'"),
    ('dean', 'Их накажет история.', 'History will punish them.', [(527, 'Их накажет история')], ''),
    ('marina', 'То есть просто стоять и смотреть?', 'So we just stand and watch?', [(528, 'То есть'), (528, 'просто стоять и смотреть')], 'the end of the question (how they demolish monuments) dropped'),
    ('dean', 'Марина, у нас нет выбора.', 'Marina, we have no choice.', [(529, 'Марина, у нас нет выбора')], ''),
    ('marina', 'Эдуард Владимирович, не этому вы нас учили.', "Eduard Vladimirovich, that's not what you taught us.", [(530, 'Эдуард Владимирович, не этому вы нас учили')], ''),
    ('dean', 'Марина, что ты делаешь?', 'Marina, what are you doing?', [(531, 'Марина, что ты делаешь')], ''),
    ('marina', 'А я глаза на это закрывать не буду. Я подниму людей!', "Well, I'm not going to close my eyes to this. I'll rally people!", [(532, 'глаза на это закрывать не буду'), (534, 'Я подниму')], "'Знаете, а я вот' -> 'А я'; 'общественность' (the public) -> 'людей'"),
    ('marina', 'Вы меня уволите?', 'Are you going to fire me?', [], "adapted from cue 536 'Уволишь меня?', switched to the polite form like her other lines"),
    ('dean', 'Я этого не хочу. Но вспомни, у тебя сын болеет.', "I don't want that. But remember, your son is ill.", [(539, 'Вспомни, у тебя сын')], "first sentence new (sums up cues 535-537); 'сын больной' -> 'сын болеет'"),
    ('dean', 'Я прошу тебя, отрекись, Марина. Галилей тоже отрёкся.', "I'm begging you, take it back, Marina. Galileo took it back too.", [(551, 'Я прошу тебя, отрекись, Марина'), (552, 'тоже отрекся')], "'Галилей, он тоже...' -> 'Галилей тоже...'; 'но остался великим ученым' dropped"),
    ('marina', 'Вот и возьмите на работу Галилея.', 'Then go and hire Galileo.', [(553, 'на работу Галилея')], "'возьми' -> 'возьмите': she keeps the polite form"),
]
WALK = [
    (0, 'Эдуард Владимирович, я на минуточку.', "'Eduard Vladimirovich, I'll only be a minute.' She uses his first name and his father's name, which is how you address a boss or a teacher. The last word is a tiny, friendly form of 'minute'. Then her big news."),
    (0, 'Я спасла монастырь!', "'I saved the monastery!' The verb is in the past, and it ends in the feminine form, because Marina is a woman. But the dean is not excited at all."),
    (1, None, "'Marina Sergeyevna, I already know. The town hall called me.' Literally, 'to me they called from the town hall'. Russian often says 'they' when nobody in particular is named. Then he warns her."),
    (2, None, "'You know what scoundrels they are.' He calls the officials scoundrels, but he still won't stand up to them. Notice that he uses the casual 'you' with her. Marina asks him straight out."),
    (3, None, "'So what do you suggest?' She answers with the polite 'you', because he is her boss. Here is his advice."),
    (4, 'Ты преподавай.', "'You teach.' A command, made friendlier by the 'you' in front: in other words, just do your job."),
    (4, 'А они пусть строят свои торговые центры.', "'And let them build their shopping centres.' The little word in the middle means 'let'. That's how you say 'let them do it' about other people. He adds a grand phrase to make it sound wise."),
    (5, None, "'History will punish them.' The order is 'them will punish history', so the one who punishes comes last. Russian word order is free, because the endings show who does what. Marina can't accept it."),
    (6, None, "'So we just stand and watch?' Two verbs in their dictionary form, 'to stand' and 'to watch'. The dean shrugs it off."),
    (7, None, "'Marina, we have no choice.' Literally, 'at us there is no choice'. It's the same pattern Russians use to say what they have, or don't have. Marina reminds him of who he used to be."),
    (8, None, "'Eduard Vladimirovich, that's not what you taught us.' He was once her teacher, so it really stings. Now the dean is worried about what she'll do next."),
    (9, None, "'Marina, what are you doing?' A simple question you'll hear all the time. She tells him."),
    (10, 'А я глаза на это закрывать не буду.', "'Well, I'm not going to close my eyes to this.' This is the future with the helping verb for 'will', plus the dictionary form, 'to close'. She means to tell everyone, on the internet and among her students."),
    (10, 'Я подниму людей!', "'I'll rally people!' The verb literally means 'I will lift'. Marina knows what this may cost her."),
    (11, None, "'Are you going to fire me?' Short and direct. The verb is in the future. He doesn't say yes, but he doesn't say no either."),
    (12, None, "'I don't want that. But remember, your son is ill.' The second sentence is the threat: she has a sick son and needs her job. Then he asks something that sounds very old-fashioned."),
    (13, None, "'I'm begging you, take it back, Marina. Galileo took it back too.' The verb means to renounce your words, the way Galileo did before his judges. Marina has the last word."),
    (14, None, "'Then go and hire Galileo.' Literally, 'then take Galileo to work'. That's how Russians say 'to hire someone'. And with that, she walks out."),
]
