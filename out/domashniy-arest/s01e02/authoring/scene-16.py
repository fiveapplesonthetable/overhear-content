# Authoring module for domashniy-arest-s01e02-scene-16.
ID = 'domashniy-arest-s01e02-scene-16'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 16
TITLE = 'Золотой ярд  (Operation Golden Yard)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'chief': 'Михаил Михайлович', 'general': 'Генерал Круглов', 'lavrov': 'Лавров'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Back at security headquarters, the call to Moscow has come through. Last time, in the flat, Arkady swapped his new iPhone for Slavik's old phone, just to be able to make a call. Now General Kruglov is on the big screen, and the chief, Mikhail Mikhailovich, his nephew Lyova and Major Lavrov are sitting round the table. Let's listen in Russian first."
OPENER = "Let's go through it slowly. The general wants to know why the agents have come back empty-handed."
TRANSITION = "Let's hear the whole call one more time."
OUTRO = "So the arrest was only half the plan: Moscow is after a billion roubles, and Pasha's cluster is the bait. That was a tricky one, and you followed it. See you next time!"
CLOSING = ('chief', 'Пока!')
STORY = [
    ('general', 'Ну что, взяли их?', 'So, did you arrest them?', [], "new: the general's opening question (cue 461 is garbled: 'Вы везли их?')"),
    ('lavrov', 'Никак нет, товарищ генерал.', 'Negative, Comrade General.', [(462, 'Никак нет')], "'товарищ генерал' added as address"),
    ('general', 'Почему?', 'Why not?', [(463, 'Почему')], ''),
    ('lavrov', 'Мэр куда-то спрятал деньги. Местные чиновники не могут собрать нужную сумму.', "The mayor has hidden the money somewhere. The local officials can't put together the sum they need.", [(466, 'Мэр'), (467, 'не могут собрать')], "simplified from cues 466-467: 'перепрятал' -> 'спрятал', 'коррупционеры' -> 'чиновники', 'необходимую сумму и выйти на сделку' -> 'нужную сумму'"),
    ('general', 'Понятно. И что теперь?', 'I see. And what now?', [(468, 'Понятно')], "'Так и что?' (469) -> 'И что теперь?'"),
    ('lavrov', 'Мы дали объекту три дня.', 'We gave the target three days.', [(470, 'Мы дали объекту три дня')], "'на сбор денег' (to collect the money) dropped"),
    ('chief', 'Арестовать их надо, а деньги потом найдём.', "They should be arrested, and we'll find the money later.", [(473, 'а деньги потом найдем')], "the cue's 'Довязать' (garbled) -> 'Арестовать'"),
    ('lavrov', 'Товарищ генерал, операция называется Золотой ярд.', 'Comrade General, the operation is called Golden Yard.', [(476, 'Товарищ генерал, операция называется «Золотой ярд»')], 'guillemets dropped in the spoken line'),
    ('lavrov', 'Наша задача — взять у взяточников миллиард рублей.', 'Our task is to take a billion roubles from the bribe-takers.', [(479, 'у взяточников миллиард рублей')], "'изъять' (seize) -> 'взять'"),
    ('lavrov', 'Легенда с кластером отличная. Всё работает.', 'The cover story with the cluster is excellent. Everything works.', [(482, 'Легенда с кластером отличная'), (483, 'Все работает')], 'speaker of 481-483 not certain from the subtitles; given to Lavrov, who is arguing against an early arrest'),
    ('general', 'Да! Все деньги брать надо.', 'Yes! We have to take all the money.', [(484, 'Да'), (484, 'брать надо')], "slang 'бабки' -> 'деньги'"),
    ('general', 'Так, а это кто?', "Right, and who's this?", [(485, 'Так, а это кто')], ''),
    ('chief', 'Лейтенант Соколов, товарищ генерал. Работает у нас в архиве.', 'Lieutenant Sokolov, Comrade General. He works in our archive.', [(486, 'Лейтенант Соколов, товарищ генерал'), (487, 'Работает у нас в архиве')], ''),
    ('general', 'А почему он на секретном совещании?', 'And why is he at a secret meeting?', [(488, 'А почему он')], "'присутствует' (is present) dropped"),
    ('chief', 'А на секретном совещании он мой племянник.', 'And at the secret meeting, he is my nephew.', [(490, 'А на секретном совещании он мой')], "the cue's typo 'племенник' corrected to 'племянник'"),
    ('general', 'Так, операцию продолжаем. Михаил Михайлович, помогайте Лаврову.', 'Right, the operation goes on. Mikhail Mikhailovich, give Lavrov your help.', [(493, 'Так, операцию продолжаем'), (494, 'Михаил Михайлович')], "'оказывайте Лаврову полное содействие' (give Lavrov full cooperation) -> 'помогайте Лаврову'"),
    ('chief', 'Есть!', 'Yes, sir!', [(495, 'Есть')], ''),
]
WALK = [
    (0, None, "'So, did you arrest them?' Literally, 'well, what, did you take them?'. 'Take' is the everyday word for 'arrest' here. The major answers in military style."),
    (1, None, "'Negative, Comrade General.' The first two words, literally 'in no way not', are the army's way of saying a firm no. 'Comrade General' is how officers still address a general. The general asks one word."),
    (2, None, "'Why not?' Right then, Lavrov explains."),
    (3, 'Мэр куда-то спрятал деньги.', "'The mayor has hidden the money somewhere.' The mayor is Arkady, of course. The word for money is always plural in Russian, like 'funds'. And that causes a problem."),
    (3, 'Местные чиновники не могут собрать нужную сумму.', "'The local officials can't put together the sum they need.' 'Can't' is 'not' plus 'they can'. These are the people who were supposed to pay for the cluster deal. The general takes it in."),
    (4, None, "'I see. And what now?' The first word, 'it's clear', is a very common way to say 'I see' or 'got it'."),
    (5, None, "'We gave the target three days.' The target is Pasha, the acting mayor. 'To the target' takes the ending for giving something to someone. The chief has a simpler plan."),
    (6, None, "'They should be arrested, and we'll find the money later.' Literally, 'to arrest them is necessary'. Then 'we'll find' is a single-action verb, so it's future. Lavrov has to explain the whole point."),
    (7, None, "'Comrade General, the operation is called Golden Yard.' 'Yard' here is slang for a billion, a short way of saying the full word. So golden yard means 'a golden billion'. Then he spells it out."),
    (8, None, "'Our task is to take a billion roubles from the bribe-takers.' The short dash in the middle stands for 'is'. 'From' someone uses the same little word as 'at', with the ending for 'of'. That's why arresting them now would spoil everything."),
    (9, 'Легенда с кластером отличная.', "'The cover story with the cluster is excellent.' The word for legend is also the spy word for a cover story. The cluster, Pasha's big industrial project, is just bait. And it's working."),
    (9, 'Всё работает.', "'Everything works.' Now the general is convinced."),
    (10, None, "'Yes! We have to take all the money.' The verb 'take' comes before 'we have to', for emphasis. Then the general notices someone new at the table."),
    (11, None, "'Right, and who's this?' The first word, 'so' or 'right', is how Russians start a new point. The chief answers."),
    (12, 'Лейтенант Соколов, товарищ генерал.', "'Lieutenant Sokolov, Comrade General.' Rank, surname, and the title, as the army likes it."),
    (12, 'Работает у нас в архиве.', "'He works in our archive.' 'At us' means 'in our office'. The general isn't happy."),
    (13, None, "'And why is he at a secret meeting?' After the word for 'at', meeting takes the ending for place. The chief has an answer, of sorts."),
    (14, None, "'And at the secret meeting, he is my nephew.' He simply repeats the general's words and adds 'my nephew'. That's his whole explanation. Luckily, the general has bigger things on his mind."),
    (15, 'Так, операцию продолжаем.', "'Right, the operation goes on.' Literally, 'the operation we continue'. The object comes first here, because it's the thing everyone is talking about. Then an order for the chief."),
    (15, 'Михаил Михайлович, помогайте Лаврову.', "'Mikhail Mikhailovich, give Lavrov your help.' In this moment, Lavrov gets the ending for 'to', because in Russian you help to somebody. And the chief answers like a soldier."),
    (16, None, "'Yes, sir!' It's the ordinary word for 'there is', but in the army it means 'yes, sir, will do'."),
]
