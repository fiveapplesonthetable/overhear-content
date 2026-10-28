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
INTRO = 'Nastya arrives at the kitchen of restaurant Claude Monet on a very tense morning. The cooks are whispering nervously because Chef Viktor Barinov is approaching in a terrible mood. Listen to the Russian dialogue first, and then we will review the phrases together in English.'
OPENER = "Let's break down this tense kitchen conversation sentence by sentence."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "In Kukhnya, Chef Barinov's football obsession and terrible temper are legendary, and the kitchen staff quickly learns when to stay out of his way. Next time you watch the episode, listen for the Russian expressions for 'to be' and 'always' — you will catch every word right away. See you next time!"
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
    (0, None, "'Why is the kitchen so quiet?' Nastya wonders about the unusual silence among the kitchen staff this morning."),
    (1, None, "'Chef is coming.' Senya quietly warns her that their terrifying boss is on his way."),
    (2, None, "'Angry again.' He adds that the boss is in one of his notorious bad moods."),
    (3, None, "'What happened?' She asks what triggered the boss's fury this time."),
    (4, None, "'Football again?' Nastya guesses that sports betting might be the cause again."),
    (5, None, "'Yes, yesterday Spartak played.' Senya confirms that a match involving a specific team took place the night before."),
    (6, None, "'And how much did he lose?' She inquires about the financial damage the boss suffered."),
    (7, None, "'A hundred grand.' He reveals the massive sum of money lost on the bet."),
    (8, None, "'Unbelievable!' Nastya is stunned by the sheer size of the gambling loss."),
    (9, None, "'A hundred thousand rubles?' She repeats the amount just to make sure she heard it correctly."),
    (10, None, "'Yes, exactly one hundred thousand.' Senya confirms the exact devastating figure without hesitation."),
    (11, None, "'They always lose before his shift.' He points out the recurring pattern of bad luck right before work."),
    (12, None, "'And what do we do now?' She asks for advice on how to survive the upcoming storm."),
    (13, None, "'Stay silent and just work.' Senya recommends keeping their heads down and focusing purely on tasks."),
    (14, None, "'Do not anger the chef today.' He specifically warns against doing anything that might set the boss off."),
    (15, None, "'Understood.' Nastya acknowledges the survival strategy for the day."),
    (16, None, "'I will be very careful.' She promises to tread lightly around the explosive head cook."),
    (17, None, "'To work!' Senya abruptly ends the chat to get back to his station before disaster strikes."),
]
