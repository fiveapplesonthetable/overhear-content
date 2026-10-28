# Authoring module for kukhnya-s03e19-scene-04.
ID = 'kukhnya-s03e19-scene-04'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 19
SCENE = 4
TITLE = "Спор о влиянии Нагиева  (The Bet About Nagiyev's Influence)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.19'
SOURCE_FILE = 'sources/kukhnya/s03/e19.ru.srt'
INTRO = 'In the kitchen, Eva asks Katya if there is anything between her and Max. Meanwhile, Chef Barinov goads Nagiyev into proving that he still has authority in Claude Monet by saving Rodion Sergeyevich from eviction.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Stung in his pride, Nagiyev marches off to Andrey Mikhailovich's office to prove who really runs the restaurant. See you next time!"
CLOSING = ('nagiyev', 'Всего хорошего!')
STORY = [
    ('max', 'Слушай, Катя, а у тебя с Максом что-то есть?', 'Listen, Katya, is there something going on between you and Max?', [(53, 'а у тебя с Максом что-то есть')], 'adapted'),
    ('max', 'Ничего у нас с ним нет и никогда не было.', 'There is nothing between us and there never was.', [(54, 'Ничего у нас нет. И не было')], 'adapted'),
    ('nagiyev', 'Приятного мне аппетита! Витя, чего ты хотел?', 'Bon appétit to me! Vitya, what did you want?', [(55, 'Приятного аппетита'), (56, 'Чего хотел')], 'adapted'),
    ('barinov', 'Да я хотел с тобой один вопросик решить.', 'Well, I wanted to settle one little question with you.', [(57, 'хотел с тобой один вопросик решить')], 'adapted'),
    ('barinov', 'Но потом вспомнил, что теперь всё Андрей решает.', 'But then I remembered that Andrey decides everything now.', [(58, 'что у нас теперь это все Андрей Михайлович решает')], 'adapted'),
    ('nagiyev', 'Садись за стол, что там у тебя за вопрос?', 'Sit down at the table, what is your question?', [(60, 'Чего за вопрос')], 'adapted'),
    ('barinov', 'Попроси его, чтобы он нашего бомжа не трогал.', 'Ask him not to touch our homeless man.', [(61, 'попроси его, чтобы он нашего бомжа не трогал')], 'adapted'),
    ('nagiyev', 'У нас есть бомж? Который во дворе живёт?', 'We have a homeless man? The one who lives in the courtyard?', [(62, 'во дворе живет')], 'adapted'),
    ('barinov', 'Он совсем не помнит, кто он и откуда.', 'He does not remember at all who he is or where he is from.', [(63, 'Не помнит, кто он, откуда')], 'adapted'),
    ('barinov', 'Ты не волнуйся, он здоровый, мы ему прививки делали.', 'Do not worry, he is healthy, we got him his shots.', [(64, 'Ты не волнуйся, он здоровый, мы ему прививки делали')], 'adapted'),
    ('barinov', 'Хотя вряд ли Андрей тебя вообще слушать будет.', 'Although Andrey is unlikely to listen to you at all.', [(65, 'вряд ли Андрей Михайлович тебя слушать будет')], 'adapted'),
    ('nagiyev', 'Что ты мне по нервам ходишь? Засекай время!', 'Why are you getting on my nerves? Check the clock!', [(66, 'по нервам-то'), (68, 'Засекай')], 'adapted'),
]
WALK = [
    (0, None, '\'Listen, Katya, is there something going on between you and Max?\' Max presses lightly on the spot, combining "u tebya" (literally "by you") with "slushay" ("listen") rather than a separate word for "have".'),
    (1, None, '\'There is nothing between us and there never was.\' Max offers an unhurried manner right away, joining "nikogda" ("never") to "bylo" ("was") so every word pulls its weight.'),
    (2, None, '\'Bon appétit to me! Vitya, what did you want?\' Nagiyev inquires firmly without a pause, weaving "priyatnogo" ("pleasant") together with "appetita" ("appetite") just the way native speakers do.'),
    (3, None, '\'Well, I wanted to settle one little question with you.\' Barinov maintains a grounded direction in the conversation, anchoring the Russian line on "khotel" ("wanted") and "voprosik" ("little question") without extra filler.'),
    (4, None, '\'But then I remembered that Andrey decides everything now.\' Barinov conveys a thoughtful tempo with Max, building the phrase around "potom" ("then") and "vspomnil" ("remembered") for a crisp, natural delivery.'),
    (5, None, '\'Sit down at the table, what is your question?\' Nagiyev probes honestly toward Max here, anchoring the Russian line on "sadis" ("sit down") and "stol" ("table") without extra filler.'),
    (6, None, '\'Ask him not to touch our homeless man.\' Barinov establishes an honest approach during the exchange, putting "poprosi" ("ask") alongside "bomzha" ("homeless man") in a tight, everyday turn of phrase.'),
    (7, None, '\'We have a homeless man? The one who lives in the courtyard?\' Nagiyev tests promptly with Max now, linking "yest" ("there is"), "bomzh" ("homeless man"), and "dvore" ("yard, courtyard") in one brisk exchange.'),
    (8, None, '\'He does not remember at all who he is or where he is from.\' Barinov picks a playful posture toward Max, anchoring the Russian line on "sovsem" ("at all") and "pomnit" ("remembers") without extra filler.'),
    (9, None, '\'Do not worry, he is healthy, we got him his shots.\' Barinov takes a candid course across the room, anchoring the Russian line on "volnuysya" ("worry") and "zdorovyy" ("healthy") without extra filler.'),
    (10, None, '\'Although Andrey is unlikely to listen to you at all.\' Barinov shows a lively direction on the spot, joining "vryad" ("hardly, unlikely") to "voobshche" ("at all") so every word pulls its weight.'),
    (11, None, '\'Why are you getting on my nerves? Check the clock!\' Nagiyev inquires openly as the beat lands, using "nervam" (from "nerv", "on the nerves") alongside "khodish" ("can walk, are walking") to shape the meaning.'),
]
