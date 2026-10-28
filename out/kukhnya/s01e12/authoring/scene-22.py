# Authoring module for kukhnya-s01e12-scene-22.
ID = 'kukhnya-s01e12-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 22
TITLE = 'Все в безопасности  (Everyone Is Safe)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'The fire next door is out, and Kostya has helped everyone get outside safely. Nastya is proud of him, and some hungry guests are looking for somewhere new to eat. The Russian first.'
OPENER = 'Slowly, from the relief to the rush of customers.'
TRANSITION = 'Here it is again, start to finish.'
OUTRO = "The neighbours' bad luck turns into a full house for Claude Monet. Count how many guests walk through the door. Speak soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, не бойся, огонь уже потушили.', 'Nastya, do not be afraid, they already put out the fire.', [], ''),
    ('kostya', 'Все люди здесь сейчас в безопасности.', 'All the people here are safe now.', [(281, 'Все здесь в безопасности.')], ''),
    ('nastya', 'Костя, огромное спасибо тебе за помощь.', 'Kostya, thank you so much for the help.', [(282, 'Спасибо тебе.')], ''),
    ('nastya', 'Ты у меня такой смелый парень!', 'You are such a brave guy to me!', [(282, 'Ты у меня такой смелый.')], ''),
    ('kostya', 'Я просто помог людям выйти на улицу.', 'I simply helped the people go outside.', [], ''),
    ('nastya', 'Ты настоящий герой нашего ресторана!', 'You are a real hero of our restaurant!', [], ''),
    ('guest', 'Просим прощения за эти неудобства.', 'We ask for forgiveness for this inconvenience.', [(283, 'неудобства.')], ''),
    ('guest', 'Соседнее кафе закрыто по техническим причинам.', 'The neighboring cafe is closed for technical reasons.', [(284, 'по техническим причинам.')], ''),
    ('guest', 'А где же нам теперь поужинать?', 'And where do we have dinner now?', [], ''),
    ('guest', 'Слушайте, пойдём лучше в тот ресторан!', "Hey, let's go to that other restaurant instead!", [(285, 'Слушайте, пойдем лучше в тот ресторан.')], ''),
    ('nastya', 'Все гости идут прямо к нам!', 'All the guests are coming straight to us!', [], ''),
    ('kostya', 'Сегодня наш зал будет полон людей.', 'Today our dining room will be full of people.', [], ''),
    ('nastya', 'Пойдём скорее на работу, любимый бармен!', "Let's go quickly to work, beloved bartender!", [], ''),
]
WALK = [
    (0, None, "'Nastya, do not be afraid, they already put out the fire.' 'Ne boysya' has the 'sya' in it, so fear is something you do to yourself. Nobody is named as putting the fire out, just 'they put out', and Russian happily does this."),
    (1, None, "'All the people here are safe now.' 'V bezopasnosti' is 'in safety'. 'Bezopasnost' is built from 'bez', 'without', and 'opasnost', 'danger'."),
    (2, None, "'Kostya, thank you so much for the help.' 'Ogromnoe' means 'huge', so 'huge thanks' is a warm 'thank you so much'. 'Za pomoshch' is 'for the help'."),
    (3, None, "'You are such a brave guy to me!' The phrase 'you at me' means 'in my eyes you are'. 'Brave' ends in 'y', and the word for a guy can also mean boyfriend."),
    (4, None, "'I simply helped the people go outside.' 'Pomog' is 'helped', and the people being helped take an ending: 'lyudi' becomes 'lyudyam'. 'Vyyti' is 'to go out'."),
    (5, None, "'You are a real hero of our restaurant!' 'Real' means genuine. 'Of our restaurant' gives 'restaurant' an ending that says 'of'."),
    (6, None, "'We ask for forgiveness for this inconvenience.' 'Inconvenience' is built from 'not' plus 'comfort'. A polite 'we ask forgiveness' opens it."),
    (7, None, "'The neighboring cafe is closed for technical reasons.' 'Zakryto' is 'closed' with an 'o' because 'kafe' counts as neuter. 'Po tekhnicheskim prichinam' is the standard way to say 'for technical reasons'."),
    (8, None, "'And where do we have dinner now?' 'Pouzhinat' is 'to have supper', from 'uzhin', supper. 'Gde zhe' is 'where, then'. 'Nam' is 'for us'."),
    (9, None, "'Hey, let's go to that other restaurant instead!' 'Slushayte' is 'listen', in the plural form. 'Luchshe' means 'better', but here it means 'instead', and 'tot' means 'that one over there'."),
    (10, None, "'All the guests are coming straight to us!' The little word for 'towards' sits in front of 'us', which turns into 'nam'. 'Straight' goes in front of it."),
    (11, None, "'Today our dining room will be full of people.' The 'of' in 'full of people' is hidden in the ending: 'lyudi' turns into 'lyudey'. English needs a word there, but Russian just changes the last syllable."),
    (12, None, "'Let's go quickly to work, beloved bartender!' 'Lyubimy' is 'beloved', from the action 'to love'. 'Skoree' is 'quickly'. 'Na rabotu' is 'to work', with 'u' for direction."),
]
