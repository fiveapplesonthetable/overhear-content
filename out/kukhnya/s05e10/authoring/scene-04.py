# Authoring module for kukhnya-s05e10-scene-04.
ID = 'kukhnya-s05e10-scene-04'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 10
SCENE = 4
TITLE = 'Удалённая база на ресепшене  (The Deleted Database at Reception)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'sveta': 'Света'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.10'
SOURCE_FILE = 'sources/kukhnya/s05/e10.ru.srt'
INTRO = 'While Mikhail leads the inspectors toward a luxury suite, Max and Kostya deduce that the moustached suspect must be a hotel guest. At the front desk, an impatient woman hypnotizes receptionist Sveta into wiping out the entire reservation database.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That concludes the scene at the reception desk. Pay attention to Max's shocked questions when he sees Sveta deleting the hotel database in a trance. See you next time!"
CLOSING = ('max', 'Хорошего дня!')
STORY = [
    ('max', 'А толщину ковра измерять будете?', 'Will you measure the thickness of the carpet too?', [(66, 'толщину ворса ковра измерять будете')], 'adapted'),
    ('kostya', 'Обязательно! Правильно.', 'Definitely! Quite right.', [(67, 'Обязательно. Правильно')], 'adapted'),
    ('max', 'Усатый в гардеробе не одевался, значит, он у нас живёт.', 'The moustached man did not use the cloakroom, so he stays with us.', [(68, 'Усатый очкарик в гардеробе не одевался, значит, он у нас живет')], 'adapted'),
    ('kostya', 'Может, не будем лучше с ним связываться?', 'Maybe we would do better not to mess with him?', [(69, 'может, не будем лучше с ним связываться')], 'adapted'),
    ('max', 'Света, поможешь?', 'Sveta, will you help?', [(71, 'помочь будешь')], 'adapted'),
    ('sveta', 'Одну минуту.', 'One minute.', [(71, 'Одну минуту')], 'adapted'),
    ('kostya', 'Вы ещё не закончили? Вы очень медленно всё делаете.', 'Have you not finished yet? You are doing everything very slowly.', [(72, 'Вы еще не закончили'), (73, 'Вы очень медленно все делаете')], 'adapted'),
    ('kostya', 'Я не могу больше ждать.', 'I cannot wait any longer.', [(73, 'Я не могу больше ждать')], 'adapted'),
    ('sveta', 'Я делаю, делаю.', 'I am doing it, I am doing it.', [(75, 'Я делаю, делаю')], 'adapted'),
    ('max', 'Ты зачем базу удаляешь? Ты что творишь?', 'Why are you deleting the database? What are you doing?', [(76, 'Ты зачем базу удаляешь'), (77, 'Ты что творишь')], 'adapted'),
    ('sveta', 'Я не знаю.', 'I do not know.', [(78, 'Я не знаю')], 'adapted'),
    ('max', 'Гипнотизёр ещё в отеле!', 'The hypnotist is still in the hotel!', [(79, 'Гипнотизер еще в отеле')], 'adapted'),
]
WALK = [
    (0, None, '\'Will you measure the thickness of the carpet too?\' Discussing the thickness to Kostya, Max puts the weight on "tolshchinu" ("thickness", from "tolshchina") as the exchange unfolds.'),
    (1, None, "'Definitely! Quite right.' Opening up frankly in the exchange, spoken Russian compresses the whole thought into just 2 words, skipping the extra helper words English needs."),
    (2, None, "'The moustached man did not use the cloakroom, so he stays with us.' Max speaks bluntly toward Kostya, leaving no doubt about where he stands."),
    (3, None, '\'Maybe we would do better not to mess with him?\' Kostya replies openly in the exchange and centers the remark on "svyazyvatsya" ("to mess with") without any extra fuss.'),
    (4, None, "'Sveta, will you help?' Reacting plainly at once, Max keeps normal statement word order here, turning the line into a question for Sveta purely through rising pitch."),
    (5, None, "'One minute.' Sveta chimes in promptly watching Max, watching Max's face to see how the news lands."),
    (6, None, '\'Have you not finished yet? You are doing everything very slowly.\' Kostya replies firmly in the exchange and chooses "zakonchili" ("to finish, to complete", from the root "zakonchit") so Sveta hears the exact meaning.'),
    (7, None, '\'I cannot wait any longer.\' Kostya counters candidly before Sveta and brings in "zhdat" ("to wait") to make the meaning unmistakable.'),
    (8, None, "'I am doing it, I am doing it.' Sveta replies promptly around Kostya, keeping the focus on what actually matters here."),
    (9, None, '\'Why are you deleting the database? What are you doing?\' Mentioning the database around Sveta, Max brings in "udalyayesh" ("delete", from "udalyat") as the key Russian word here.'),
    (10, None, "'I do not know.' Opening up openly around Max, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (11, None, "'The hypnotist is still in the hotel!' Max responds sharply with a shrug, so Sveta knows he is not just making small talk."),
]
