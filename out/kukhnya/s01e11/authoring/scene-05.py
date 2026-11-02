# Authoring module for kukhnya-s01e11-scene-05.
ID = 'kukhnya-s01e11-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 5
TITLE = 'В поисках критика  (In Search of the Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'The critic could be anyone in the room. Kostya and Max stand at the bar and size up the guests, one table at a time. Have a listen first.'
OPENER = "Let's slow it down."
TRANSITION = "Now let's hear it once more, start to finish."
OUTRO = 'They have a suspect, and she is sitting at table seven. Whether she is the critic or not, the staff will treat her like a queen. Enjoy the rest of the episode.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, смотри внимательно на зал!', 'Max, look carefully at the dining room!', [], ''),
    ('max', 'Кто же из них может быть критиком?', 'Which one of them could be the critic?', [(66, 'Кто же из них может быть критиком?')], ''),
    ('kostya', 'Эти двое работают в соседнем банке.', 'Those two work at the bank next door.', [(67, 'работают в соседнем банке.')], ''),
    ('max', 'Да, они наши постоянные гости.', 'Yes, they are our regular guests.', [(67, 'Эти двое постоянные гости')], ''),
    ('kostya', 'А тот мужчина у окна?', 'And that man by the window?', [], ''),
    ('max', 'Он заказал рыбу и красное вино.', 'He ordered fish and red wine.', [(68, 'Рыба и красное вино.')], ''),
    ('kostya', 'Нет, настоящий критик такого не закажет.', 'No, a real critic will not order that.', [(69, 'Нет.')], ''),
    ('max', 'А парень за столиком номер три?', 'What about the guy at table number three?', [], ''),
    ('kostya', 'Он слишком молод для ресторанного критика.', 'He is too young for a restaurant critic.', [(70, 'Слишком молод')], ''),
    ('max', 'Критики обычно сидят в одиночестве.', 'Critics usually sit in solitude.', [], ''),
    ('kostya', 'И записывают всё в блокнот.', 'And write down everything in a notepad.', [], ''),
    ('max', 'Смотри, женщина за седьмым столиком!', 'Look, the woman at table seven!', [], ''),
    ('kostya', 'Она очень строго смотрит на меню.', 'She is looking very strictly at the menu.', [], ''),
    ('max', 'Кажется, мы нашли нашего критика!', 'It seems we found our critic!', [], ''),
]
WALK = [
    (0, None, ["'Max, look carefully at the dining room!' Now we can analyze the speech: ", ('kostya', 'смотри'), " is a command to one friend, the familiar form of 'to look'. Then ", ('kostya', 'на'), ('kostya', 'зал'), " points that look at the room, with the preposition for 'at'. Kostya speaks in a conspirator's voice."]),
    (1, None, ["'Which one of them could be the critic?' The expression is ", ('max', 'Кто'), ('max', 'же'), ('max', 'из'), ('max', 'них'), ", 'who then of them', and ", ('max', 'может'), ('max', 'быть'), " is 'can be'. After 'be', the noun for critic gets a new ending, becoming ", ('max', 'критиком'), '.']),
    (2, None, ["'Those two work at the bank next door.' Two people here are called ", ('kostya', 'двое'), ', the term you use for a pair of people. After the preposition, the bank takes an ending, and ', ('kostya', 'соседнем'), ", 'neighbouring', grows from the noun for 'neighbour'."]),
    (3, None, ["'Yes, they are our regular guests.' You call regulars ", ('max', 'постоянные'), ('max', 'гости'), ", 'constant guests'. Max agrees with Kostya's logic: regulars cannot be mystery visitors."]),
    (4, None, ["'And that man by the window?' Let's focus on the words: ", ('kostya', 'у'), ('kostya', 'окна'), " is 'at the window': after the preposition, the window takes a new ending. ", ('kostya', 'мужчина'), ", 'man', is close to the noun for 'husband'. Kostya moves on to the next suspect."]),
    (5, None, ["'He ordered fish and red wine.' Listen to the fish: it turns into ", ('max', 'рыбу'), " because it's the thing he ordered. And ", ('max', 'красное'), " takes a matching ending for 'wine'. Max reads the table like a detective."]),
    (6, None, ["'No, a real critic will not order that.' We can inspect the phrase: ", ('kostya', 'такого'), ('kostya', 'не'), ('kostya', 'закажет'), " is 'of such not will order', with the term for 'such' changed after 'not'. ", ('kostya', 'закажет'), " is 'will order'. Kostya is sure of his rules for critics."]),
    (7, None, ["'What about the guy at table number three?' The opening word means 'and what about'. ", ('max', 'за'), ('max', 'столиком'), " is 'at the little table': the noun is a small version of the usual word for a restaurant table."]),
    (8, None, ["'He is too young for a restaurant critic.' We can analyze the dialogue: ", ('kostya', 'молод'), " is a short form of 'young', used to describe someone in the moment. ", ('kostya', 'для'), ('kostya', 'ресторанного'), ('kostya', 'критика'), " is 'for a restaurant critic', with new endings."]),
    (9, None, ["'Critics usually sit in solitude.' It sounds grand, but ", ('max', 'в'), ('max', 'одиночестве'), " is just the usual way to say someone sits alone, and it's built on the term for 'one'. ", ('max', 'обычно'), ", 'usually', comes first, as a general rule."]),
    (10, None, ["'And write down everything in a notepad.' Now let's inspect the words: ", ('kostya', 'записывают'), " is 'write down', using a prefix on the verb 'to write'. ", ('kostya', 'блокнот'), ", 'notepad', was borrowed from French. ", ('kostya', 'в'), ('kostya', 'блокнот'), " is 'into the notepad'."]),
    (11, None, ["'Look, the woman at table seven!' The table is ", ('max', 'за'), ('max', 'седьмым'), ('max', 'столиком'), ", 'at the seventh little table', using a counting word. ", ('max', 'женщина'), " is 'woman'. The suspect is a lady alone, so she fits."]),
    (12, None, ["'She is looking very strictly at the menu.' We will look at the phrase: ", ('kostya', 'строго'), ", 'strictly', takes an adverb ending. ", ('kostya', 'меню'), ' never changes its ending here. Kostya is drawing a conclusion from a frown, which is hardly proof.']),
    (13, None, ["'It seems we found our critic!' Now we can break down this line: ", ('max', 'Кажется'), ", 'it seems', is a single word. ", ('max', 'нашли'), ", 'found', ends in a plural suffix for 'we'. ", ('max', 'нашего'), ('max', 'критика'), " is 'our critic' as the one found."]),
]
