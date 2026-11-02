# Authoring module for kukhnya-s01e15-scene-09.
ID = 'kukhnya-s01e15-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 9
TITLE = 'Без Макса  (Without Max)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'The cooks in the kitchen are enjoying an unusually peaceful day. Senya comments on it, and Fedya tells him exactly why. Hear it in Russian first.'
OPENER = 'Line by line, once more.'
TRANSITION = 'Now the quiet kitchen again, uncut.'
OUTRO = "Fedya and Senya get back to work in a kitchen with no Max in it. Enjoy the quiet while it lasts."
CLOSING = ('fedya', 'Пока!')
STORY = [
    ('senya', 'Я не думал, что тут так классно.', "I didn't think it was so great here.", [(170, 'Я не думал, что на кухне так классно.')], ''),
    ('fedya', 'Везде классно, когда нет Макса.', 'It is great everywhere when there is no Max.', [(171, 'Без Макса везде классно.')], ''),
    ('senya', 'Да, сегодня очень тихо.', 'Yes, it is very quiet today.', [], ''),
    ('fedya', 'Нам надо работать.', 'We need to work.', [], ''),
    ('senya', 'Я просто отдыхаю.', 'I am just resting.', [], ''),
    ('fedya', 'Шеф может прийти.', 'The chef can come.', [], ''),
    ('senya', 'Шеф сейчас занят.', 'The chef is busy now.', [], ''),
    ('fedya', 'Всё равно, давай работать.', "Anyway, let's work.", [], ''),
    ('senya', 'Хорошо, я иду.', 'Good, I am coming.', [], ''),
    ('fedya', 'Где мой нож?', 'Where is my knife?', [], ''),
    ('senya', 'Он на столе.', 'It is on the table.', [], ''),
    ('fedya', 'Спасибо, я вижу.', 'Thank you, I see it.', [], ''),
]
WALK = [
    (0, None, ["'I didn't think it was so great here.' Now we can consider the dialogue: ", ('senya', 'классно'), " is everyday slang for 'great'. ", ('senya', 'не'), ('senya', 'думал'), ', ', ('senya', 'что'), " is 'did not think that', and ", ('senya', 'думал'), ' has the ending for a man speaking about the past.']),
    (1, None, ["'It is great everywhere when there is no Max.' Now we can examine this part: ", ('fedya', 'нет'), ('fedya', 'Макса'), ", meaning 'there is no Max', puts the name in the 'of' form with a new ending. ", ('fedya', 'Везде'), " is 'everywhere'."]),
    (2, None, ["'Yes, it is very quiet today.' We will focus on this part: ", ('senya', 'тихо'), " is 'quiet' and needs no action word. ", ('senya', 'сегодня'), " comes from an old phrase for 'of this day', squeezed into one word."]),
    (3, None, ["'We need to work.' Let's consider the phrase: ", ('fedya', 'Нам'), ('fedya', 'надо'), ", meaning 'to us necessary', works the same way for anyone. The action after it stays in its basic form."]),
    (4, None, ["'I am just resting.' Let us look at the speech: ", ('senya', 'отдыхаю'), " is 'I rest', and ", ('senya', 'просто'), " means 'just'. Senya doesn't bother with a long excuse."]),
    (5, None, ["'The chef can come.' Let's focus on this line: ", ('fedya', 'может'), ('fedya', 'прийти'), " is 'can come'. ", ('fedya', 'прийти'), ' is the action word for moving on foot, with a start that means arriving.']),
    (6, None, ["'The chef is busy now.' Let us consider this part: ", ('senya', 'занят'), " for 'busy' grows out of the term for 'to occupy', and a man's form has no extra ending."]),
    (7, None, ["'Anyway, let's work.' We can inspect the phrase: ", ('fedya', 'Всё'), ('fedya', 'равно'), " means 'everything equal', Russian for 'anyway'. ", ('fedya', 'давай'), ' makes it a suggestion.']),
    (8, None, ["'Good, I am coming.' Let's break down the words: ", ('senya', 'иду'), " means 'I go' and 'I am coming' in one word. Senya has given in."]),
    (9, None, ["'Where is my knife?' Let us inspect the phrase: ", ('fedya', 'нож'), ' is the Russian word for knife, and ', ('fedya', 'мой'), " is masculine to match. There is no word for 'is'."]),
    (10, None, ["'It is on the table.' Let's break down the sentence: ", ('senya', 'на'), ('senya', 'столе'), " puts an extra ending on the word for table. 'It' is 'he', because a knife is masculine in Russian."]),
    (11, None, ["'Thank you, I see it.' Let's look at the dialogue: ", ('fedya', 'вижу'), " is an action word meaning 'I see', and no word for 'it' is needed. Fedya has found the knife."]),
]
