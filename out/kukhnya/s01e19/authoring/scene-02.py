# Authoring module for kukhnya-s01e19-scene-02.
ID = 'kukhnya-s01e19-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 2
TITLE = 'Новые имена  (New names)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'artyom': 'Артём', 'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Chef Viktor is angry because Senya and Fedya got fired. He reassigns their names to the remaining cooks in the kitchen. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Now let's go back through the exchange around New names line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The cooks confusedly accept their new identities to avoid making the Chef even angrier. Next time you watch the episode, listen for the Russian expressions for 'sauce' and 'ready' — you will catch every word right away. See you next time!"
CLOSING = ('fedya', 'До свидания.')
STORY = [
    ('barinov', 'Сеня, соус готов?', 'Senya, is the sauce ready?', [(16, 'Сеня, соус готов?')], ''),
    ('artyom', 'А я не Сеня.', 'I am not Senya.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('artyom', 'Я Артем.', 'I am Artyom.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('barinov', 'Сеню уволили.', 'Senya got fired.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Мне плевать, кто ты.', 'I do not care who you are.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Сегодня ты Сеня.', 'Today you are Senya.', [(19, 'Сегодня ты Сеня.')], ''),
    ('barinov', 'Федя бы это быстро сделал.', 'Fedya would have done it fast.', [(21, 'Федя бы это за 10 секунд сделал.')], ''),
    ('fedya', 'Я тоже Федя, шеф.', 'I am Fedya too, Chef.', [(22, 'Я, кстати, тоже Федя, шеф.')], ''),
    ('barinov', 'Нет, ты не Федя.', 'No, you are not Fedya.', [(23, 'Нет, ты не Федя.')], ''),
    ('barinov', 'Имя Федя заслужить надо.', 'You have to earn the name Fedya.', [(24, 'Имя Федя заслужить надо.')], ''),
    ('barinov', 'Теперь ты Артем.', 'Now you are Artyom.', [(25, 'Теперь ты Артем.')], ''),
    ('fedya', 'Да, шеф.', 'Yes, Chef.', [(26, 'Да, шеф.')], ''),
]
WALK = [
    (0, None, "'Senya, is the sauce ready?' Barinov barks an order about the sauce, aggressively addressing his cook by the wrong name."),
    (1, None, "'I am not Senya.' Artyom tentatively corrects his boss, dropping the verb 'to be' as is standard in Russian."),
    (2, None, "'I am Artyom.' Artyom states his actual name simply and directly, omitting the present-tense verb."),
    (3, None, "'Senya got fired.' Barinov dismisses the correction, bluntly stating that the real Senya was just fired."),
    (4, None, "'I do not care who you are.' Barinov aggressively declares his indifference to his employee's true identity."),
    (5, None, "'Today you are Senya.' Barinov forces the new name upon him for the day, connecting the words directly without a verb."),
    (6, None, "'Fedya would have done it fast.' Barinov complains about the slow pace by comparing another cook to the recently fired Fedya."),
    (7, None, "'I am Fedya too, Chef.' Fedya chimes in to say that he is also named Fedya, pointing out the coincidence."),
    (8, None, "'No, you are not Fedya.' Barinov instantly strips him of his real name, aggressively denying his identity."),
    (9, None, "'You have to earn the name Fedya.' Barinov absurdly elevates the name to a title of honor that must be earned through hard work."),
    (10, None, "'Now you are Artyom.' Barinov reassigns the name Artyom to him, treating his staff completely interchangeably."),
    (11, None, "'Yes, Chef.' — Built around the key proper name meaning 'chef, boss'. Now listen to the whole scene again."),
]
