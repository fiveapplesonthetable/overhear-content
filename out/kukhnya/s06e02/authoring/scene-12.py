# Authoring module for kukhnya-s06e02-scene-12.
ID = 'kukhnya-s06e02-scene-12'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 12
TITLE = 'Урок на роликах и звонок из «Смака»  (Rollerblade Lesson and the Call from Smak)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = "While Kostya demonstrates to Lyova how he first kissed Nastya while rollerblading, Mikhail secretly arranges a phone call from a supposed television producer inviting Barinov's restaurant onto the show Smak."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Barinov's eyes light up at the prospect of national television filming his signature dishes right in his kitchen. See you next time!"
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('kostya', 'Ну что, поцеловал Гулю?', 'Well, did you kiss Gulya?', [(199, 'Ну что, поцеловал Гулю?')], 'exact'),
    ('lyova', 'И ты уже знаешь.', 'Even you already know.', [(200, 'И ты уже знаешь')], 'exact'),
    ('kostya', 'Знаешь, как мы с Настей поцеловались первый раз?', 'Do you know how Nastya and I kissed for the first time?', [(202, 'Знаешь, как мы с Настей поцеловались первый раз?')], 'exact'),
    ('kostya', 'Мы на роликах катались.', 'We were skating on rollerblades.', [(203, 'Мы на роликах катались')], 'exact'),
    ('kostya', 'Я ее взял и наклонил.', 'I caught her and dipped her.', [(204, 'Я ее раз взял'), (205, 'Наклонил')], 'adapted'),
    ('lyova', 'Я все понял, я готов.', 'I understood everything, I am ready.', [(206, 'Я все. Я готов')], 'adapted'),
    ('barinov', 'Виктор Петрович, здравствуйте.', 'Viktor Petrovich, hello.', [(210, 'Виктор Петрович, здравствуйте')], 'exact'),
    ('kostya', 'Это продюсер программы, мы меняем концепцию нашей программы.', "This is the show's producer, we are changing the concept of our program.", [(211, 'продюсер программы'), (212, 'меняем концепцию нашей программы')], 'adapted'),
    ('kostya', 'И теперь будем снимать в реальных ресторанах.', 'And now we will film in real restaurants.', [(212, 'и теперь будем снимать'), (213, 'в реальных ресторанах')], 'adapted'),
    ('barinov', 'С чего это вдруг такая честь?', 'Why such an honor all of a sudden?', [(214, 'С чего это вдруг такая честь?')], 'exact'),
    ('kostya', 'До нас дошли слухи, что вы ввели новое авторское меню.', 'Rumors reached us that you introduced a new auteur menu.', [(216, 'И до нас дошли слухи, что вы ввели новое авторское меню')], 'exact'),
    ('kostya', 'Кто, если не вы, лучший повар страны?', 'Who, if not you, is the best chef in the country?', [(217, 'И кто, если не вы, лучший повар страны?')], 'exact'),
]
WALK = [
    (0, None, '\'Well, did you kiss Gulya?\' By asking whether Barinov kisses Gulya, Kostya presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Even you already know.' Between the work and the menu, Lyova gives Barinov a quick, grounded response."),
    (2, None, '\'Do you know how Nastya and I kissed for the first time?\' Asking whether Barinov knows how Nastya and he kissed for the first time is how Kostya puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'We were skating on rollerblades.' Noting that they were skating on rollerblades keeps Kostya's side of the story simple and clear."),
    (4, None, "'I caught her and dipped her.' Even though he caught her and dipped, Kostya keeps a steady face in front of Barinov."),
    (5, None, "'I understood everything, I am ready.' Admitting that he understood everything he is ready shows Lyova being honest for a change."),
    (6, None, "'Viktor Petrovich, hello.' With the point and menu in play, Barinov keeps this short reply brisk and direct."),
    (7, None, "'This is the show's producer, we are changing the concept of our program.' Once this is the show producer they are changing the concept of their program, Kostya can finally tell Barinov what he means."),
    (8, None, "'And now we will film in real restaurants.' Adding that they will film in real restaurants fills in the missing piece for Barinov."),
    (9, None, '\'Why such an honor all of a sudden?\' With the moment and menu hanging in the air, Barinov puts Kostya on the spot. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (10, None, "'Rumors reached us that you introduced a new auteur menu.' Around the point and menu, Kostya sets a calm, everyday tone with Barinov."),
    (11, None, '\'Who, if not you, is the best chef in the country?\' When Kostya asks if who if not Barinov is the best in the country, Barinov has to answer fast. Notice how he sticks to the formal "you", keeping a professional line between them.'),
]
