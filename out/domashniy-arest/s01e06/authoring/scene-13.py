# Authoring module for domashniy-arest-s01e06-scene-13.
ID = 'domashniy-arest-s01e06-scene-13'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 13
TITLE = "Брал бы пример с сестры!  (You Should Follow Your Sister's Example!)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inga': 'Инга Евгеньевна', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "While Ilona learns at the meatpacking plant that Ignatyev has not spoken to his ballerina daughter Galina for a year, Samson and Nina are summoned to the school principal's office because of young Slavik. There English teacher Inga Evgenyevna shows them a prank picture Slavik brought to class, and accidentally lets slip a shocking secret about their daughter Yulya. Let's listen in Russian first."
OPENER = "Let's walk through what happens in the school office line by line."
TRANSITION = "Now let's listen to the whole scene in the school office again."
OUTRO = "Marching Slavik out of the school, Samson and Nina are furious to learn that Yulya has been faking a hospital stay for two weeks. Listen for 'real photograph', 'example', and 'operation' when you watch. See you next time!"
CLOSING = ('inga', 'До свидания!')
STORY = [
    ('inga', 'Понимаете, в чём дело? Вот вы посмотрите.', 'Do you understand what the matter is? Just look at this.', [(477, 'Понимаете, в чем дело?'), (479, 'Вот вы посмотрите')], 'skipped 478 for clean A1 retelling'),
    ('inga', 'Вот это он принёс в класс. И всем показывал.', 'He brought this into the classroom. And he was showing it to everyone.', [(480, 'Вот это он'), (480, 'в класс'), (481, 'И всем показывал')], "cue 480 'перенес' -> 'принёс'"),
    ('nina', 'Ой, а ты где это взял? Ты что, подглядывал за Ингой Евгеньевной?', 'Oh, and where did you get this? Were you spying on Inga Evgenyevna?', [(482, 'Ой, а ты где это взял'), (483, 'Ты что, подглядывал за Ингой Евгеньевной')], ''),
    ('inga', 'Вы что думаете, это настоящая фотография? Нет, тут только лицо моё.', 'Do you think this is a real photograph? No, only the face here is mine.', [(484, 'Вы что думаете, это настоящая фотография?'), (485, 'Нет, лицо мое')], ''),
    ('inga', 'Он это сделал в компьютере, в фотошопе. И он урок сорвал!', 'He made this on the computer, in Photoshop. And he disrupted the lesson!', [(490, 'Он это сделал'), (490, 'в компьютере, в фотошопе'), (492, 'Он урок сорвал')], "principal's lines in 492-514 folded into Inga's role"),
    ('samson', 'Славик, ты слышишь, что учителя говорят?', 'Slavik, do you hear what the teachers are saying?', [(493, 'Ты слышишь, что учителя')], ''),
    ('inga', 'Вот что с ним делать? У него уже два в четверти.', 'What are we to do with him? He already has a failing grade for the term.', [(495, 'Вот что с ним делать?'), (496, 'У него уже два в четверти')], ''),
    ('samson', 'Вы извините, мы всё исправим.', 'Excuse us, we will fix everything.', [(497, 'Вы извините, мы исправим')], ''),
    ('inga', 'Ты бы брал пример с сестры! Сестра умная, серьёзная, старательная.', "You should follow your sister's example! Your sister is smart, serious, and hardworking.", [(498, 'Ты бы брал пример'), (498, 'сестры'), (499, 'Сестра умная, серьезная, старательная')], "restored preposition 'с' before 'сестры'"),
    ('inga', 'Кстати, как её здоровье?', 'By the way, how is her health?', [(500, 'Кстати, как ее здоровье?')], ''),
    ('nina', 'Кто, Юля? Нормально, спасибо.', 'Who, Yulya? Fine, thank you.', [(501, 'Юля?'), (503, 'Нормально, спасибо')], "cue 501 'Че' -> 'Кто'"),
    ('inga', 'То есть операция прошла хорошо?', 'So the operation went well?', [(504, 'То есть операция прошла хорошо?')], ''),
    ('samson', 'Какая операция?', 'What operation?', [(505, 'Какая операция?')], ''),
    ('inga', 'Что-то серьёзное у вас. Девочка две недели лежит в областной клинике!', 'It must be something serious for you. The girl has been lying in the regional clinic for two weeks already!', [(506, 'что-то серьезное у вас'), (507, 'две недели лежит в областной клинике')], 'split 506-507 into two short sentences'),
    ('samson', 'Да, вы знаете, это очень серьёзная операция. Мы всё исправим. До свидания!', "Yes, you know, it is a very serious operation. We'll fix everything. Goodbye!", [(508, 'Да, вы знаете, это очень серьезная операция'), (513, 'исправим. До свидания')], ''),
    ('nina', 'Вставай, Славик! Отцу сам дома всё расскажешь.', "Get up, Slavik! You'll tell your father everything yourself at home.", [(516, 'Вставай. Отцу сам'), (516, 'расскажешь')], "cue 516 'дом' -> 'дома'"),
]
WALK = [
    (0, None, "Across the desk, English teacher Inga Evgenyevna hands a printed picture to Nina and Samson: 'Do you understand what the matter is? Just look at this.'"),
    (1, None, "'He brought this into the classroom. And he was showing it to everyone.' The teacher complains that Slavik brought the picture into class and kept showing it to everyone."),
    (2, 'Ой, а ты где это взял?', "Nina stares at the picture in shock and turns to her son: 'Oh, and where did you get this?'"),
    (2, 'Ты что, подглядывал за Ингой Евгеньевной?', "'Were you spying on Inga Evgenyevna?' Saying 'spying on' in Russian literally works as 'peeking behind' someone."),
    (3, 'Вы что думаете, это настоящая фотография?', "The teacher is indignant at Nina's naive question: 'Do you think this is a real photograph?'"),
    (3, 'Нет, тут только лицо моё.', "'No, only the face here is mine.' A short, punchy nominal phrase built around the Russian word for 'face'."),
    (4, 'Он это сделал в компьютере, в фотошопе.', "'He made this on the computer, in Photoshop.' Inga points out that he made the whole picture on the computer in an editing program."),
    (4, 'И он урок сорвал!', "'And he disrupted the lesson!' Literally he tore off or ruined the class."),
    (5, None, "Samson glares at his son: 'Slavik, do you hear what the teachers are saying?'"),
    (6, 'Вот что с ним делать?', "'What are we to do with him?' The exasperated teacher asks Samson what they are supposed to do with the boy now."),
    (6, 'У него уже два в четверти.', "'He already has a failing grade for the term.' In Russian schools, a two out of five is a failing mark."),
    (7, None, "Samson apologises to the teachers: 'Excuse us, we will fix everything.'"),
    (8, 'Ты бы брал пример с сестры!', "Then the teacher turns to Slavik: 'You should follow your sister's example!' Literally 'you would take an example from your sister'."),
    (8, 'Сестра умная, серьёзная, старательная.', "'Your sister is smart, serious, and hardworking.' She praises Yulia as smart, serious, and hardworking—which leads to an unexpected question."),
    (9, None, "'By the way, how is her health?' Russian leaves out 'am', 'is', or 'are' in the present, linking 'by the way' straight to 'health'."),
    (10, None, "Nina blinks in surprise: 'Who, Yulya? Fine, thank you.' After all, Yulya leaves the flat with her schoolbag every morning."),
    (11, None, "'So the operation went well?' Still believing Yulia's excuse, the teacher asks if her operation went well."),
    (12, None, "Samson is completely baffled: 'What operation?'"),
    (13, 'Что-то серьёзное у вас.', "'It's something serious for you.' The teacher says this sympathetically."),
    (13, 'Девочка две недели лежит в областной клинике!', "'The girl has been lying in the regional clinic for two weeks!' To cover for her, the teacher repeats the story that Yulia has been lying in the regional clinic for two weeks!"),
    (14, None, "Realising Yulya has been skipping school for two weeks behind their backs, Samson covers for her in front of the teacher: 'Yes, you know, it is a very serious operation. We'll fix everything. Goodbye!'"),
    (15, None, "Nina pulls Slavik up from his chair: 'Get up, Slavik! You'll tell your father everything yourself at home.'"),
]
