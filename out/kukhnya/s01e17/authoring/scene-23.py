# Authoring module for kukhnya-s01e17-scene-23.
ID = 'kukhnya-s01e17-scene-23'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 23
TITLE = 'Тайна паспорта  (The Secret of the Passport)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'The toast is interrupted. Barinov asks Max to show him his passport, and the date of birth in it is not what Max has been telling everyone. Listen to the passport scene in Russian first.'
OPENER = "Let's look at the passport scene line by line."
TRANSITION = 'Now the passport scene again, all the way through.'
OUTRO = 'Max has been caught out by his own passport. Keep "nelzya", not allowed, for every rule you\'ll ever need to state in Russian. See you next time!'
CLOSING = ('senya', 'Ну, пока, Макс!')
STORY = [
    ('barinov', 'Покажи мне свой паспорт, Макс.', 'Show me your passport, Max.', [(327, 'Паспорте!')], ''),
    ('max', 'Вот мой паспорт, шеф.', 'Here is my passport, chef.', [(327, 'Паспорте!')], ''),
    ('barinov', 'А почему день рождения в феврале?', 'And why is the birthday in February?', [(327, 'А что это тебе день рождения в феврале, а?')], ''),
    ('senya', 'Твой день рождения не сегодня?', 'Your birthday is not today?', [(327, 'день рождения в феврале')], ''),
    ('max', 'Я хотел сделать вам приятное.', 'I wanted to please you.', [(329, 'чтобы сделать тебе приятное')], ''),
    ('barinov', 'Ты соврал нам про праздник?', 'Did you lie to us about the holiday?', [(330, 'немножко соврать')], ''),
    ('max', 'Я хотел, чтобы все помирились.', 'I wanted everyone to make up.', [(328, 'забыть свои обиды')], ''),
    ('senya', 'Но врать друзьям нельзя.', 'But one must not lie to friends.', [(330, 'соврать')], ''),
    ('barinov', 'Любая ложь — это плохо.', 'Any lie is bad.', [(331, 'за любое вранье')], ''),
    ('max', 'Я очень виноват перед вами.', 'I am very guilty before you.', [(331, 'приходится платить')], ''),
    ('barinov', 'Ты должен был сказать правду.', 'You should have told the truth.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
    ('senya', 'Правда всегда выходит наружу.', 'The truth always comes out.', [(331, 'Правда')], ''),
    ('max', 'За любой обман приходится платить.', 'For any deceit one has to pay.', [(331, 'за любое вранье рано или поздно приходится платить.')], ''),
]
WALK = [
    (0, None, '\'Show me your passport, Max.\' "Pokazhi" is "show" to one person. "Svoy pasport" is "your own passport".'),
    (1, None, '\'Here\'s my passport, chef.\' "Vot" is what you say as you hand something over: here it is.'),
    (2, None, '\'And why is your birthday in February?\' "V fevrale" means in February, and months aren\'t capitalised in Russian.'),
    (3, None, '\'Your birthday isn\'t today?\' Senya checks the obvious: "ne segodnya", not today.'),
    (4, None, '\'I wanted to do something nice for you.\' "Sdelat priyatnoe" is literally "to do the pleasant", a fixed phrase for "do something nice".'),
    (5, None, '\'You lied to us about the party?\' "Sovral", lied, is a blunt, everyday word.'),
    (6, None, '\'I wanted everyone to make up.\' "Khotel, chtoby" is "wanted that", used when you want others to do something.'),
    (7, None, '\'But you mustn\'t lie to friends.\' "Nelzya", not allowed, is a word you\'ll see on signs everywhere.'),
    (8, None, '\'Any lie is bad.\' "Lozh", lie, takes "-aya" words like "lyubaya", any, even though it doesn\'t end in "-a".'),
    (9, None, '\'I\'m very much to blame.\' "Vinovat pered vami" is literally "guilty before you", how Russians admit they\'re in the wrong.'),
    (10, None, '\'You should have told the truth.\' "Dolzhen byl" means "should have", literally "was obliged".'),
    (11, None, '\'The truth always comes out.\' "Vykhodit naruzhu" is literally "goes out to the outside".'),
    (12, None, '\'Every lie has to be paid for.\' "Prikhoditsya platit" is "one has to pay", with no "one" in it. "Obman" means deceit.'),
]
