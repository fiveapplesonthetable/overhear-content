# Authoring module for kukhnya-s03e20-scene-06.
ID = 'kukhnya-s03e20-scene-06'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 20
SCENE = 6
TITLE = 'Куда ехать больному?  (Where Should the Patient Go?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'doctor': 'Врач', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.20'
SOURCE_FILE = 'sources/kukhnya/s03/e20.ru.srt'
INTRO = "Andrey demands three times what he paid for Claude Monet. Meanwhile at the hospital, the doctor warns that Kostya and Nastya's noisy apartment is bad for Max's recovery and suggests that Max live with Vika!"
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Cornered by the doctor's medical advice, Vika finds it impossible to turn Max out onto the street. See you next time!"
CLOSING = ('doctor', 'До свидания!')
STORY = [
    ('max', 'Это же в три раза больше, чем ты заплатил!', 'That is three times more than you paid!', [(105, 'Это в три раза больше, чем ты заплатил')], 'adapted'),
    ('max', 'А ты как хотел, Дима? Это же бизнес!', 'And what did you expect, Dima? It is business!', [(106, 'А ты как хотел. Это же бизнес')], 'adapted'),
    ('max', 'Всё, я полностью готов! Ну, куда я еду?', 'Alright, I am completely ready! Well, where am I going?', [(107, 'Все, готов'), (108, 'Ну, куда я еду')], 'adapted'),
    ('doctor', 'Извините, что вмешиваюсь, я услышал, что у вас свадьба.', 'Forgive me for interfering, I overheard that you are having a wedding.', [(109, 'Извините, что вмешиваюсь'), (110, 'подготовка к свадьбе')], 'adapted'),
    ('doctor', 'Значит, у вас дома сейчас родственников полный дом.', 'That means your house is full of relatives right now.', [(111, 'родственников полный дом')], 'adapted'),
    ('doctor', 'А нашему больному нужен хороший уход и главное — покой.', 'And our patient needs good care and above all peace and quiet.', [(113, 'А больному нужен хороший уход'), (114, 'И главное, покой')], 'adapted'),
    ('doctor', 'Это очень важно для его скорейшего выздоровления.', 'That is very important for his speedy recovery.', [(115, 'его скорейшего выздоровления')], 'adapted'),
    ('max', 'Подождите, а куда мне тогда сейчас ехать?', 'Wait a second, where should I go right now then?', [(116, 'А куда мне тогда ехать')], 'adapted'),
    ('doctor', 'Виктория Сергеевна, может быть, он у вас поживёт?', 'Viktoriya Sergeyevna, maybe he could stay at your place?', [(117, 'Виктория Сергеевна, может, он у вас поживет')], 'adapted'),
    ('vika', 'Нет, доктор, так совершенно точно не пойдёт!', 'No, Doctor, that will definitely not do!', [(118, 'Нет, так не пойдет')], 'adapted'),
    ('max', 'Вика, подожди, а разве я с тобой раньше жил?', 'Vika, wait, did I live with you before?', [(119, 'Я с тобой жил')], 'adapted'),
    ('doctor', 'В гостинице плохой уход, ему надо жить среди знакомых людей.', 'A hotel has poor care, he needs to live among familiar people.', [(122, 'Какой там уход'), (123, 'жить в обществе знакомых людей')], 'adapted'),
    ('vika', 'Костя, скажи, какие у нас ещё есть варианты?', 'Kostya, tell me, what other options do we have?', [(125, 'Какие у нас еще есть варианты')], 'adapted'),
]
WALK = [
    (0, None, '\'That is three times more than you paid!\' Because that is three times more than the doctor paid, Max does not bother softening the blow for the doctor. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, "'And what did you expect, Dima? It is business!' Wondering what the doctor expects Dima cuts straight through the tension between Max and the doctor."),
    (2, None, '\'Alright, I am completely ready! Well, where am I going?\' Asking whether Alright he is completely ready puts the doctor right on the defensive. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, '\'Forgive me for interfering, I overheard that you are having a wedding.\' The doctor explains that for interfering he overheard that Max is having a wedding, keeping his voice calm and direct. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (4, None, "'That means your house is full of relatives right now.' Realizing that that means Max's house is full of relatives right now changes how the doctor handles the situation."),
    (5, None, '\'And our patient needs good care and above all peace and quiet.\' Noting that their patient needs good care and above all peace and quiet keeps the doctor\'s side of the story simple and clear. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (6, None, '\'That is very important for his speedy recovery.\' Even though that is very important for his speedy recovery, the doctor keeps a steady face in front of Max. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (7, None, "'Wait a second, where should I go right now then?' Asking whether a second where should he goes right now then puts the doctor right on the defensive."),
    (8, None, '\'Viktoriya Sergeyevna, maybe he could stay at your place?\' Wondering if Viktoriya Sergeyevna maybe he could stay at Max\'s place shows the doctor caught off guard. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (9, None, "'No, Doctor, that will definitely not do!' Once doctor that will definitely not do, Vika makes sure the doctor hears every word. Russian puts the key word right up front so her emotion lands on the first beat."),
    (10, None, "'Vika, wait, did I live with you before?' Asking whether he lives with the doctor is how Max puts the doctor on the spot."),
    (11, None, '\'A hotel has poor care, he needs to live among familiar people.\' The doctor tells Max that a hotel has poor care he needs to live among familiar people without dressing it up. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (12, None, '\'Kostya, tell me, what other options do we have?\' Asking whether tell her what other options do they have puts the doctor right on the defensive. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
]
