ID = 'kukhnya-s06e02-scene-12'
SHOW = "kukhnya"
SEASON = 6
EPISODE = 2
SCENE = 12
TITLE = 'Урок на роликах и звонок из «Смака»  (Rollerblade Lesson and the Call from Smak)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'kostya': 'anja', 'lyova': 'angelina'}
LABELS = {'anya': 'Шеф', 'kostya': 'Костя', 'lyova': 'Лёва'}
SOURCE_NAME = "Кухня (Kukhnya) S6.02"
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'

INTRO = "While Kostya demonstrates to Lyova how he first kissed Nastya while rollerblading, Mikhail secretly arranges a phone call from a supposed television producer inviting Barinov's restaurant onto the show Smak."

STORY = [
    ('kostya', 'Ну что, поцеловал Гулю?', 'Well, did you kiss Gulya?', [(199, 'Ну что, поцеловал Гулю?')], 'exact'),
    ('lyova', 'И ты уже знаешь.', 'Even you already know.', [(200, 'И ты уже знаешь')], 'exact'),
    ('kostya', 'Знаешь, как мы с Настей поцеловались первый раз?', 'Do you know how Nastya and I kissed for the first time?', [(202, 'Знаешь, как мы с Настей поцеловались первый раз?')], 'exact'),
    ('kostya', 'Мы на роликах катались.', 'We were skating on rollerblades.', [(203, 'Мы на роликах катались')], 'exact'),
    ('kostya', 'Я ее взял и наклонил.', 'I caught her and dipped her.', [(204, 'Я ее раз взял'), (205, 'Наклонил')], 'adapted'),
    ('lyova', 'Я все понял, я готов.', 'I understood everything, I am ready.', [(206, 'Я все. Я готов')], 'adapted'),
    ('anya', 'Виктор Петрович, здравствуйте.', 'Viktor Petrovich, hello.', [(210, 'Виктор Петрович, здравствуйте')], 'exact'),
    ('kostya', 'Это продюсер программы, мы меняем концепцию нашей программы.', "This is the show's producer, we are changing the concept of our program.", [(211, 'продюсер программы'), (212, 'меняем концепцию нашей программы')], 'adapted'),
    ('kostya', 'И теперь будем снимать в реальных ресторанах.', 'And now we will film in real restaurants.', [(212, 'и теперь будем снимать'), (213, 'в реальных ресторанах')], 'adapted'),
    ('anya', 'С чего это вдруг такая честь?', 'Why such an honor all of a sudden?', [(214, 'С чего это вдруг такая честь?')], 'exact'),
    ('kostya', 'До нас дошли слухи, что вы ввели новое авторское меню.', 'Rumors reached us that you introduced a new auteur menu.', [(216, 'И до нас дошли слухи, что вы ввели новое авторское меню')], 'exact'),
    ('kostya', 'Кто, если не вы, лучший повар страны?', 'Who, if not you, is the best chef in the country?', [(217, 'И кто, если не вы, лучший повар страны?')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Well, did you kiss Gulya?' Notice how Russian expresses 'come on' and 'Gulya' with crisp inflection rather than helper words. Lyova answers right away."),
    (1, None, "'Even you already know.' Lyova anchors the line on 'and', while 'know' completes the thought."),
    (2, None, "'Do you know how Nastya and I kissed for the first time?' Notice how Russian expresses 'know' and 'time' with crisp inflection rather than helper words."),
    (3, None, "'We were skating on rollerblades.' Here the Russian phrasing highlights 'we' before landing on 'skated'."),
    (4, None, "'I caught her and dipped her.' Notice how Russian expresses 'I' and 'dipped' with crisp inflection rather than helper words."),
    (5, None, "'I understood everything, I am ready.' The meaning hinges on 'I' working together with 'ready' in spoken Russian."),
    (6, None, "'Viktor Petrovich, hello.' Notice how Russian expresses 'hello' and 'hello' with crisp inflection rather than helper words. Kostya answers right away."),
    (7, None, "'This is the show's producer, we are changing the concept of our program.' Here the Russian phrasing highlights 'this' before landing on 'our'."),
    (8, None, "'And now we will film in real restaurants.' Kostya brings out the contrast between 'and' and 'now' in a few short words."),
    (9, None, "'Why such an honor all of a sudden?' Spoken Russian keeps this brisk, leaning on 'with' and finishing on 'honor'. Kostya answers right away."),
    (10, None, "'Rumors reached us that you introduced a new auteur menu.' The plural past ending '-li' on the verb for 'introduced' covers a group or the polite 'you'."),
    (11, None, "'Who, if not you, is the best chef in the country?' Here the Russian phrasing highlights 'who' before landing on 'country'."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Barinov's eyes light up at the prospect of national television filming his signature dishes right in his kitchen. See you in the next scene."
CLOSING = ('anya', 'Хотят снимать здесь у нас!')
