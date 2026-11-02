# Authoring module for kukhnya-s01e01-scene-11.
ID = 'kukhnya-s01e01-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = 'В поисках укрытия  (Looking for Cover)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Max has just spotted Vika across the dining room, so he dives behind a pillar and hides his face behind a menu, held upside down. A waiter called Ilya notices, and politely tries to find out what is going on. Here's the conversation in Russian first."
OPENER = 'Back through the hiding attempt.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max has run out of ideas, so he heads for the bar. The good news is that you now know how to say "I\'ll go to the bar", and how to say you\'re simply reading the menu.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('ilya', 'Молодой человек, вам помочь?', 'Young man, can I help you?', [], ''),
    ('max', 'Нет, спасибо, я просто читаю меню.', 'No, thank you, I am simply reading the menu.', [], ''),
    ('ilya', 'Но вы держите меню вверх ногами.', 'But you are holding the menu upside down.', [], ''),
    ('max', 'Правда? Я изучаю оригинальный дизайн.', 'Really? I am studying the original design.', [], ''),
    ('ilya', 'Вы кого-то боитесь в зале?', 'Are you afraid of someone in the dining hall?', [], ''),
    ('max', 'Вовсе нет, я жду хозяина ресторана.', 'Not at all, I am waiting for the restaurant owner.', [], ''),
    ('ilya', 'Хозяин точно не стоит за этой колонной.', 'The owner definitely is not standing behind this pillar.', [], ''),
    ('max', 'Я понимаю, я просто отдыхаю здесь.', 'I understand, I am simply resting here.', [], ''),
    ('ilya', 'Пожалуйста, не загораживайте проход официантам.', 'Please do not block the walkway for the waiters.', [], ''),
    ('max', 'О нет, я не хочу никому мешать!', 'Oh no, I do not want to disturb anyone!', [(74, 'Дерьмо')], ''),
    ('ilya', 'Вы можете подождать за барной стойкой.', 'You can wait at the bar counter.', [], ''),
    ('max', 'Отличная идея, я пойду в бар!', 'Great idea, I will go to the bar!', [], ''),
    ('ilya', 'Бармен нальёт вам отличный напиток.', 'The bartender will pour you an excellent drink.', [], ''),
]
WALK = [
    (0, None, ['\'Young man, can I help you?\' ', ('ilya', 'Молодой человек'), ' is how a waiter addresses a man who isn\'t old, literally "young person". ', ('ilya', 'вам помочь?'), ' is "to you to help", and there\'s no "I" in it.']),
    (1, None, ['\'No, thank you, I am simply reading the menu.\' ', ('max', 'меню'), ' never changes its ending, like the word for coffee in the first scene. ', ('max', 'читаю'), ' is "I read", and ', ('max', 'просто'), ' gives the shrug.']),
    (2, None, ['\'But you are holding the menu upside down.\' ', ('ilya', 'вверх ногами'), ' is literally "up with legs", ', ('ilya', 'ногами'), ' being "legs" with the ending ', ('ilya', '-ами'), ', "with". So upside down is "legs up".']),
    (3, None, ['\'Really? I am studying the original design.\' ', ('max', 'Правда?'), ' is "truth?" once more. ', ('max', 'оригинальный дизайн'), ' is borrowed from English, so you can follow Max\'s excuse even with no Russian.']),
    (4, None, ['\'Are you afraid of someone in the dining hall?\' ', ('ilya', 'кого-то'), ' is ', ('ilya', 'кого'), ', whom, plus ', ('ilya', '-то'), ', which turns it into "someone". ', ('ilya', 'боитесь'), ', "you\'re afraid", wants that ', ('ilya', 'кого'), ' form: afraid of whom.']),
    (5, None, ['\'Not at all, I am waiting for the restaurant owner.\' There\'s no "for" in the Russian: Max says ', ('max', 'жду хозяина'), ', "I wait the owner", and the ', ('max', '-а'), ' on ', ('max', 'хозяина'), ' does the job. ', ('max', 'ресторана'), ' ends in ', ('max', '-а'), ' too, meaning "of the restaurant". ', ('max', 'Вовсе нет'), ' is a strong "not at all".']),
    (6, None, ['\'The owner definitely is not standing behind this pillar.\' Russian says a person "stands" somewhere, and doesn\'t just "be". ', ('ilya', 'Точно'), ' is "exactly", here "definitely", and ', ('ilya', 'за этой колонной'), ' is "behind this pillar".']),
    (7, None, ['\'I understand, I am simply resting here.\' ', ('max', 'понимаю'), ' is "I understand", the everyday present tense, where his earlier answer was "got it". ', ('max', 'отдыхаю'), ', "I\'m resting", comes from the word for a rest or a holiday.']),
    (8, None, ['\'Please, do not block the walkway for the waiters.\' ', ('ilya', 'Пожалуйста'), ' is "please", and also "you\'re welcome". ', ('ilya', 'загораживайте'), ' ends in ', ('ilya', '-те'), ', the polite-"you" ending, and ', ('ilya', 'официантам'), ' is "to the waiters".']),
    (9, None, ['\'Oh no, I do not want to disturb anyone!\' ', ('max', 'никому'), ' is "to nobody", and ', ('max', 'не'), ' stays in the sentence too: the double negative. ', ('max', 'мешать'), ' is "to disturb", the word Barinov used in "don\'t disturb me".']),
    (10, None, ['\'You can wait at the bar counter.\' ', ('ilya', 'можете'), ' is "you can", from the same verb as the word for maybe. ', ('ilya', 'стойкой'), ', the counter, comes from the verb to stand.']),
    (11, None, ['\'Great idea, I will go to the bar!\' In ', ('max', 'в бар'), ', ', ('max', 'бар'), ' stays as it is because he\'s heading there; sitting inside it would take a different ending. ', ('max', 'пойду'), ' is "I\'ll go", I\'ll head off.']),
    (12, None, ['\'The bartender will pour you an excellent drink.\' ', ('ilya', 'напиток'), ', drink, comes from the verb to drink, which you heard in the bar scene. ', ('ilya', 'нальёт'), ' is "will pour", and ', ('ilya', 'вам'), ' is "to you".']),
]
