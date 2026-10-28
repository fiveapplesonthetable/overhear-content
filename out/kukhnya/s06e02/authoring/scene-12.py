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
    ('kostya', 'Виктор Петрович, здравствуйте.', 'Viktor Petrovich, hello.', [(210, 'Виктор Петрович, здравствуйте')], 'exact'),
    ('kostya', 'Это продюсер программы, мы меняем концепцию нашей программы.', "This is the show's producer, we are changing the concept of our program.", [(211, 'продюсер программы'), (212, 'меняем концепцию нашей программы')], 'adapted'),
    ('kostya', 'И теперь будем снимать в реальных ресторанах.', 'And now we will film in real restaurants.', [(212, 'и теперь будем снимать'), (213, 'в реальных ресторанах')], 'adapted'),
    ('barinov', 'С чего это вдруг такая честь?', 'Why such an honor all of a sudden?', [(214, 'С чего это вдруг такая честь?')], 'exact'),
    ('kostya', 'До нас дошли слухи, что вы ввели новое авторское меню.', 'Rumors reached us that you introduced a new auteur menu.', [(216, 'И до нас дошли слухи, что вы ввели новое авторское меню')], 'exact'),
    ('kostya', 'Кто, если не вы, лучший повар страны?', 'Who, if not you, is the best chef in the country?', [(217, 'И кто, если не вы, лучший повар страны?')], 'exact'),
]
WALK = [
    (0, None, "'Well, did you kiss Gulya?' Kostya quizzes wryly while looking straight at Lyova here."),
    (1, None, '\'Even you already know.\' Lyova reacts vividly to Kostya and brings in "uzhe" ("already, now") to make the meaning unmistakable.'),
    (2, None, '\'Do you know how Nastya and I kissed for the first time?\' Pressing on warmly during the talk, the "-sya" ending on "potselovalis" ("kissed") marks an action that unfolds mutually or turns back on the speaker.'),
    (3, None, "'We were skating on rollerblades.' Addressing the rollerblades watching Lyova, Kostya lets Lyova see exactly where things stand."),
    (4, None, '\'I caught her and dipped her.\' Kostya replies decisively at once and puts the weight on "naklonil" ("dipped, leaned", from "naklonit") as the exchange unfolds.'),
    (5, None, '\'I understood everything, I am ready.\' Describing how ready he is around Kostya, Lyova uses "gotov" ("ready", from "gotovyy") to make the point stick.'),
    (6, None, '\'Viktor Petrovich, hello.\' Kostya simply sends this formal greeting in one quick breath using "zdravstvuyte" ("hello") — the polite Russian greeting that literally wishes the other person good health.'),
    (7, None, '\'This is the show\'s producer, we are changing the concept of our program.\' Focusing on the concept in this beat, Kostya centers the thought on "kontseptsiyu" ("concept", from "kontseptsiya") without wasting a word.'),
    (8, None, '\'And now we will film in real restaurants.\' Touching on the restaurant with Barinov, Kostya lands on "restoranakh" ("restaurant", built on "restoran") to keep the statement grounded.'),
    (9, None, "'Why such an honor all of a sudden?' Barinov challenges promptly how Kostya expects that to work in practice."),
    (10, None, '\'Rumors reached us that you introduced a new auteur menu.\' Bringing up the rumors in front of Barinov, Kostya puts the weight on "avtorskoye" ("auteur, signature", from "avtorskiy") as the exchange unfolds.'),
    (11, None, '\'Who, if not you, is the best chef in the country?\' Confirming how best things are at once, Kostya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
]
