# Authoring module for kukhnya-s01e17-scene-18.
ID = 'kukhnya-s01e17-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 18
TITLE = 'Ты труп  (You Are Dead Meat)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "Barinov has come back to Claude Monet furious. He has found Senya's veal rolls on the menu of the rival restaurant, and he is sure there has been a leak. He goes straight for Senya. Here are Barinov's questions in Russian first."
OPENER = "Now the questions Barinov fires at Senya, slowly."
TRANSITION = "Here's Barinov and Senya again, from the top."
OUTRO = 'Senya blames Fedya, and Barinov isn\'t buying it. Hold on to "ne ponimayu", I don\'t understand, which might be the most useful phrase there is. See you next time!'
CLOSING = ('senya', 'До свидания!')
STORY = [
    ('barinov', 'Ты был там?', 'Were you there?', [(290, 'Ты что, был там в Аркабалена?')], ''),
    ('senya', 'Нет, конечно.', 'No, of course not.', [(291, 'Нет, конечно.')], ''),
    ('barinov', 'Рулеты из телятины с ветчиной.', 'Veal rolls with ham.', [(292, 'рулеты из телятины с')], ''),
    ('senya', 'Я не понимаю.', 'I do not understand.', [], ''),
    ('barinov', 'Ты отдал им наш рецепт.', 'You gave them our recipe.', [], ''),
    ('senya', 'Я ничего им не давал.', "I didn't give them anything.", [], ''),
    ('barinov', 'Ну, Сеня, ты труп.', 'Well, Senya, you are dead meat.', [(293, 'Ну, Сеня, ты труп')], ''),
    ('senya', 'Шеф, это не я!', 'Chef, it is not me!', [], ''),
    ('barinov', 'Кто тогда?', 'Who then?', [], ''),
    ('senya', 'Может быть, Федя.', 'Maybe Fedya.', [], ''),
    ('barinov', 'Я тебе не верю.', 'I do not believe you.', [], ''),
    ('senya', 'Честное слово!', 'Word of honor!', [], ''),
]
WALK = [
    (0, None, '\'Were you there?\' "Byl" is "was" for a man. "Ty byl tam?" is a plain statement turned into a question by the voice.'),
    (1, None, '\'No, of course not.\' "Konechno" is "of course", and the "net" in front turns it into "of course not".'),
    (2, None, '\'Veal rolls with ham.\' "Iz telyatiny" is "made of veal": "telyatina" becomes "telyatiny" after "iz".'),
    (3, None, '\'I don\'t understand.\' "Ne ponimayu" is a phrase worth having ready, with "ne" right before the action.'),
    (4, None, '\'You gave them our recipe.\' "Otdal" means "handed over". "Im" is "to them", the rival kitchen.'),
    (5, None, '\'I didn\'t give them anything.\' Senya answers "otdal" with "ne daval": he denies giving them anything, ever.'),
    (6, None, '\'Well, Senya, you\'re dead meat.\' "Ty trup" is literally "you\'re a corpse", the same threat as in English.'),
    (7, None, '\'Chef, it wasn\'t me!\' "Eto ne ya" is literally "it not I", with no "was" needed.'),
    (8, None, '\'Who, then?\' "Togda" means "then", in the sense of "in that case".'),
    (9, None, '\'Maybe Fedya.\' "Mozhet byt", literally "may be", is the everyday "maybe".'),
    (10, None, '\'I don\'t believe you.\' Russian believes "to" a person: "veryu tebe", I believe to you.'),
    (11, None, '\'Word of honour!\' "Chestnoe slovo", literally "honest word", is how Russians swear they\'re telling the truth.'),
]
