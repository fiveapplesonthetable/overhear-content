# Authoring module for kukhnya-s01e01-scene-06.
ID = 'kukhnya-s01e01-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "Проигрыш Спартака  (Spartak's Loss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Back at Claude Monet, the kitchen is oddly silent. Nastya, a waitress, wants to know why, and Senya, one of the cooks, tells her: the chef is coming, and he is in a foul mood because of last night's football. This is the Russian first."
OPENER = 'Now the same scene, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So the rule of the kitchen is simple: when the chef\'s team loses, you keep your head down and work. Take away the phrase for "to work!", because you\'ll hear it again.'
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('nastya', 'Почему на кухне так тихо?', 'Why is the kitchen so quiet?', [], ''),
    ('senya', 'Шеф идёт. Опять злой.', 'Chef is coming. Angry again.', [(60, 'О, опять')], ''),
    ('nastya', 'Что случилось? Опять футбол?', 'What happened? Football again?', [(61, 'Вчера Спартак')], ''),
    ('senya', 'Да, вчера играл Спартак.', 'Yes, yesterday Spartak played.', [(61, 'Вчера Спартак')], ''),
    ('nastya', 'И сколько он проиграл?', 'And how much did he lose?', [(61, 'Сколько')], ''),
    ('senya', 'Сто штук.', 'A hundred grand.', [(62, 'Сто штук')], ''),
    ('nastya', 'Ничего себе! Сто тысяч рублей?', 'Unbelievable! A hundred thousand rubles?', [(63, 'Ничего себе')], ''),
    ('senya', 'Да, ровно сто тысяч.', 'Yes, exactly one hundred thousand.', [], ''),
    ('senya', 'Они всегда проигрывают перед сменой.', 'They always lose before his shift.', [(63, 'всегда перед моей сменой')], ''),
    ('nastya', 'И что теперь делать?', 'And what do we do now?', [], ''),
    ('senya', 'Молчи и просто работай.', 'Stay silent and just work.', [], ''),
    ('senya', 'Не зли шефа сегодня.', 'Do not anger the chef today.', [], ''),
    ('nastya', 'Понятно. Буду очень осторожной.', 'Understood. I will be very careful.', [], ''),
    ('senya', 'Вот и молодец. За работу!', 'Good job. To work!', [], ''),
]
WALK = [
    (0, None, ['\'Why is the kitchen so quiet?\' Russian says ', ('nastya', 'на кухне'), ', "on the kitchen", where English says "in", and it\'s what everyone says about a restaurant kitchen. ', ('nastya', 'тихо?'), ' is "quiet", for a voice or a room.']),
    (1, None, ['\'Chef is coming. Angry again.\' Russian covers "is coming" with ', ('senya', 'идёт.'), ', the on-foot kind. The second sentence has no "is" at all: just "again angry". ', ('senya', 'Шеф'), ' is borrowed from French "chef", meaning chief.']),
    (2, None, ['\'What happened? Football again?\' ', ('nastya', 'Что случилось?'), ' is "what happened", a question you\'ll need constantly. ', ('nastya', 'футбол?'), ' is borrowed whole, and ', ('nastya', 'Опять'), ', "again", is the word Senya used a moment ago.']),
    (3, None, ['\'Yes, yesterday Spartak played.\' ', ('senya', 'вчера'), ' is "yesterday", a handy single word. Russian puts the news first, so ', ('senya', 'играл'), ', "played", comes before the team. Spartak is a Moscow football club, and the chef takes it personally.']),
    (4, None, ['\'And how much did he lose?\' ', ('nastya', 'проиграл?'), ' is ', ('senya', 'играл'), ', played, with a prefix in front, and that prefix turns "played" into "lost". ', ('nastya', 'Сколько'), ', "how much", is the same word you\'d use to ask a price.']),
    (5, None, ['\'A hundred grand.\' ', ('senya', 'Сто штук.'), ' is slang: ', ('senya', 'сто'), ' is a hundred, and ', ('senya', 'штук.'), ' means "a piece", which is street slang for a thousand roubles. So it\'s literally "a hundred pieces".']),
    (6, None, ['\'Unbelievable! A hundred thousand rubles?\' ', ('nastya', 'Ничего себе!'), ', "nothing to oneself", is an exclamation of surprise like "wow". After a number like a hundred thousand, the word for "ruble" turns into ', ('nastya', 'рублей?'), '.']),
    (7, None, ['\'Yes, exactly one hundred thousand.\' ', ('senya', 'ровно'), ' means "exactly", and it also means "even" or "level". Senya adds it because the amount is the whole point.']),
    (8, None, ['\'They always lose before his shift.\' ', ('senya', 'проигрывают'), ' is the verb for losing stretched out in the middle, which makes it a habit: "they keep losing". ', ('senya', 'перед сменой.'), ' is "before the shift".']),
    (9, None, ['\'And what do we do now?\' There\'s no "we" in Russian. ', ('nastya', 'что теперь делать?'), ' is "what to do", the plain "to do" with nothing else, and that\'s how people ask for advice.']),
    (10, None, ['\'Stay silent and just work.\' ', ('senya', 'Молчи'), ' and ', ('senya', 'работай.'), ' are both commands, and both are short. ', ('senya', 'просто'), ' is the shrug from earlier: just work, don\'t make it complicated.']),
    (11, None, ['\'Do not anger the chef today.\' ', ('senya', 'Не зли'), ' has the word for angry inside it, which Senya used a moment ago: "don\'t make him angry". ', ('senya', 'шефа'), ' has an -a on the end because the chef is the one being angered. And ', ('senya', 'сегодня.'), ' is spelled with a g but said like a v.']),
    (12, None, ['\'Understood. I will be very careful.\' ', ('nastya', 'Понятно.'), ' does the job of "understood". Nastya is a woman, so "careful" ends in the feminine, ', ('nastya', 'осторожной.'), ': the "as a" ending.']),
    (13, None, ['\'Good job. To work!\' ', ('senya', 'Вот и молодец.'), ' is "there you go, well done". ', ('senya', 'молодец.'), ' is the praise word from the soup scene. ', ('senya', 'За работу!'), ', "for work", is how you say "let\'s get going".']),
]
