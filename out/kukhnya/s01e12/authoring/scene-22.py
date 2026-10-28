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
OUTRO = "The neighbours' bad luck turns into a full house for Claude Monet. Next time you see a closed door in Russia, you'll know 'po tekhnicheskim prichinam'. Speak soon."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, не бойся, огонь уже потушили.', 'Nastya, do not be afraid, they already put out the fire.', [], ''),
    ('kostya', 'Все люди здесь сейчас в безопасности.', 'All the people here are safe now.', [(281, 'Все здесь в безопасности.')], ''),
    ('nastya', 'Костя, огромное спасибо тебе за помощь.', 'Kostya, thank you so much for the help.', [(282, 'Спасибо тебе.')], ''),
    ('nastya', 'Ты у меня такой смелый парень!', 'You are such a brave guy to me!', [(282, 'Ты у меня такой смелый.')], ''),
    ('kostya', 'Я просто помог людям выйти на улицу.', 'I simply helped the people go outside.', [], ''),
    ('nastya', 'Ты настоящий герой нашего ресторана!', 'You are a real hero of our restaurant!', [], ''),
    ('guest', 'Перед нами там извинились за неудобства.', 'They apologised to us there for the inconvenience.', [(283, 'неудобства.')], 'adapted: in the source staff next door make the apology; here a guest reports it'),
    ('guest', 'Соседний ресторан закрыт по техническим причинам.', 'The restaurant next door is closed for technical reasons.', [(284, 'по техническим причинам.')], ''),
    ('guest', 'А где же нам теперь поужинать?', 'And where do we have dinner now?', [], ''),
    ('guest', 'Слушайте, пойдём лучше в тот ресторан!', "Hey, let's go to that other restaurant instead!", [(285, 'Слушайте, пойдем лучше в тот ресторан.')], ''),
    ('nastya', 'Все гости идут прямо к нам!', 'All the guests are coming straight to us!', [], ''),
    ('kostya', 'Сегодня наш зал будет полон людей.', 'Today our dining room will be full of people.', [], ''),
    ('nastya', 'Пойдём скорее на работу, любимый бармен!', "Let's go quickly to work, beloved bartender!", [], ''),
]
WALK = [
    (0, None, "'Nastya, do not be afraid, they already put out the fire.' 'Ne boysya' is 'don't be afraid', from 'boyatsya', a verb that always carries 'sya'. 'Potushili' is 'they put out' with no 'they' at all: Russian often leaves out who did it."),
    (1, None, "'All the people here are safe now.' 'V bezopasnosti' is 'in safety'. 'Bezopasnost' is built from 'bez', 'without', and 'opasnost', 'danger'."),
    (2, None, "'Kostya, thank you so much for the help.' 'Ogromnoe' means 'huge', so 'huge thanks' is a warm 'thank you so much'. 'Za pomoshch' is 'for the help'."),
    (3, None, "'You are such a brave guy to me!' The phrase 'you at me' means 'in my eyes you are'. 'Smelyy paren' is 'brave guy', and 'paren' with 'moy', my, is how you say 'my boyfriend'."),
    (4, None, "'I simply helped the people go outside.' 'Pomog' is 'helped', and the people being helped take an ending: 'lyudi' becomes 'lyudyam'. 'Vyyti' is 'to go out'."),
    (5, None, "'You are a real hero of our restaurant!' 'Nastoyashchiy geroy' is 'a real hero'. 'Nashego restorana' is 'of our restaurant', both words with the 'of' ending, 'ego' and 'a'."),
    (6, None, "'They apologised to us there for the inconvenience.' Russian apologises 'pered', in front of, someone: 'pered nami', literally 'in front of us'. No 'they' is said. 'Neudobstva' is 'ne', not, plus 'udobstvo', convenience, here in the plural."),
    (7, None, "'The restaurant next door is closed for technical reasons.' 'Zakryt' is 'closed', in the short form with no ending, to match masculine 'restoran'. 'Po tekhnicheskim prichinam' is the standard notice-on-the-door way to say 'for technical reasons'."),
    (8, None, "'And where do we have dinner now?' 'Pouzhinat' is 'to have supper', from 'uzhin', supper. 'Gde zhe' is 'where, then'. 'Nam' is 'for us'."),
    (9, None, "'Hey, let's go to that other restaurant instead!' 'Slushayte' is 'listen', in the plural form. 'Luchshe' means 'better', but here it means 'instead', and 'tot' means 'that one over there'."),
    (10, None, "'All the guests are coming straight to us!' 'K nam' is 'to us', literally 'towards us', with 'my' turning into 'nam'. 'Pryamo' is 'straight', and 'idut' is 'are coming', on foot."),
    (11, None, "'Today our dining room will be full of people.' The 'of' in 'full of people' is hidden in the ending: 'lyudi' turns into 'lyudey'. English needs a word there, but Russian just changes the last syllable."),
    (12, None, "'Let's go quickly to work, beloved bartender!' 'Lyubimyy' is 'beloved', from 'lyubit', to love, and it's a common way to say 'darling'. 'Skoree' is 'quicker'. 'Na rabotu' is 'to work', with 'u' for direction."),
]
