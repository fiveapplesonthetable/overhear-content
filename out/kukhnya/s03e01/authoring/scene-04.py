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
    (0, None, '\'What did your parents say?\' Kostya picks one memorable element at once: "roditeli" means "parents", and it carries the main weight of what Kostya is saying.'),
    (1, None, "'Oh, nothing much.' Nastya shapes that point without fuss: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (2, None, "'I haven't told them yet.' Nastya proceeds briskly during the talk, shifting the whole mood of the room in a single beat."),
    (3, None, '\'When will you tell them?\' Kostya features one memorable expression right here: "skazhesh" means "will you say" (from "skazat"), giving the line its exact edge.'),
    (4, None, "'Chef, will you look for a molecular cook?' Max hands over the comeback without pause: Russian keeps the exact word order of a normal statement here, turning it into a question for Kostya purely through rising pitch at the end."),
    (5, None, "'You will go out with me anyway.' Max steps in bluntly in this moment, letting the remark speak for itself."),
    (6, None, '\'I will tell them tomorrow.\' Nastya picks one memorable word with Kostya: "zavtra" means "tomorrow", and it carries the main weight of what Nastya is saying.'),
    (7, None, "'No, Dad, I cannot.' Nastya cuts in honestly watching Max, before Max can change the subject."),
    (8, None, "'I already took days off.' Nastya weighs in lightly in their talk, watching Kostya's face to see how the news lands."),
    (9, None, '\'I am not going on a horseback ride.\' Nastya picks this vivid piece toward Max: "progulku" means "walk, ride" (from "progulka"), giving the line its exact edge.'),
    (10, None, '\'Alright, I have to go. Bye.\' Nastya shapes that thought before Kostya: tacking on "ladno" ("okay, fine, deal") softens the edge and checks that Kostya is on board.'),
    (11, None, "'Nastya, what horseback ride?' Kostya tests curiously before Nastya can change the subject."),
]
