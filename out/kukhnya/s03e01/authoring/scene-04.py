# Authoring module for kukhnya-s03e01-scene-04.
ID = 'kukhnya-s03e01-scene-04'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 1
SCENE = 4
TITLE = 'Конная прогулка  (The Horseback Ride)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.01'
SOURCE_FILE = 'sources/kukhnya/s03/e01.ru.srt'
INTRO = 'Meanwhile in the corridor, Kostya asks Nastya what her parents said about her pregnancy, only to learn she is still hiding the news from her father. Listen to the full conversation in Russian first, and then we will walk through every line together.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "That concludes the corridor conversation. Listen for Kostya's disbelief when Nastya has to turn down her father's horseback riding invitation. See you next time!"
CLOSING = ('kostya', 'Всего хорошего!')
STORY = [
    ('kostya', 'Что твои родители сказали?', 'What did your parents say?', [(49, 'Что твои родители сказали')], ''),
    ('nastya', 'Да так, ничего.', 'Oh, nothing much.', [(50, 'Да так, ничего')], ''),
    ('nastya', 'Я ещё не сказала.', "I haven't told them yet.", [(51, 'Я еще не сказала')], ''),
    ('kostya', 'Когда скажешь?', 'When will you tell them?', [(52, 'Когда скажешь')], ''),
    ('max', 'Шеф, будете искать молекулярного повара?', 'Chef, will you look for a molecular cook?', [(53, 'шеф, будете искать молекулярного повара')], 'adapted'),
    ('max', 'Все равно ты пойдешь со мной.', 'You will go out with me anyway.', [(56, 'Все равно ты пойдешь со мной')], 'adapted'),
    ('nastya', 'Завтра скажу.', 'I will tell them tomorrow.', [(57, 'Завтра скажу')], ''),
    ('nastya', 'Нет, папа, я не могу.', 'No, Dad, I cannot.', [(58, 'я не могу')], 'adapted'),
    ('nastya', 'Я уже брала выходные.', 'I already took days off.', [(59, 'Я уже брала выходные')], ''),
    ('nastya', 'Я не поеду на конную прогулку.', 'I am not going on a horseback ride.', [(60, 'я не поеду с тобой на конную прогулку')], 'adapted'),
    ('nastya', 'Все, ладно, мне пора. Пока.', 'Alright, I have to go. Bye.', [(61, 'Все, ладно, мне пора. Пока')], ''),
    ('kostya', 'Настя, какая конная прогулка?', 'Nastya, what horseback ride?', [(62, 'Настя, какая конная прогулка')], ''),
]
WALK = [
    (0, None, '\'What did your parents say?\' Emphasizing the parents to Nastya, Kostya centers the remark on "roditeli" ("parents") without any extra fuss.'),
    (1, None, "'Oh, nothing much.' Pushing back briskly before Kostya, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (2, None, "'I haven't told them yet.' Nastya jumps in briskly with a shrug, keeping the focus on what actually matters here."),
    (3, None, '\'When will you tell them?\' Kostya speaks up decisively to Max and uses "skazhesh" ("will you say", from "skazat") to make the point stick.'),
    (4, None, "'Chef, will you look for a molecular cook?' Touching on a molecular cook in front of Kostya, Max keeps normal statement word order here, turning the line into a question for Kostya purely through rising pitch."),
    (5, None, "'You will go out with me anyway.' Max steps in bluntly with a smile, grounding the moment in plain reality."),
    (6, None, '\'I will tell them tomorrow.\' Nastya opens up candidly to Max and brings in "zavtra" ("tomorrow") to make the meaning unmistakable.'),
    (7, None, '\'No, Dad, I cannot.\' Bringing up the dad before Max, Nastya lands on "papa" ("Dad") as the key everyday word here.'),
    (8, None, "'I already took days off.' Nastya counters lightly in their talk, leaving no doubt about where she stands."),
    (9, None, '\'I am not going on a horseback ride.\' Focusing on the walk right here, Nastya puts the weight on "progulku" ("walk, ride", from "progulka") as the exchange unfolds.'),
    (10, None, '\'Alright, I have to go. Bye.\' Opening up candidly in front of Kostya, Nastya leans on "pora" ("it is time to"), which carries the whole predicate in Russian without needing "it is".'),
    (11, None, "'Nastya, what horseback ride?' Focusing on the walk without a pause, Kostya brings the exchange with Nastya back to practical reality."),
]
