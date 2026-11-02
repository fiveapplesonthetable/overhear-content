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
OUTRO = "The neighbours' bad luck turns into a full house for Claude Monet. Next time you see a closed door in Russia, you will know it is closed for technical reasons. Speak soon."
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
    (0, None, ["'Nastya, do not be afraid, they already put out the fire.' Do not be afraid is ", ('kostya', 'не'), ('kostya', 'бойся'), '. They put out is ', ('kostya', 'потушили'), ', used without saying they.']),
    (1, None, ["'All the people here are safe now.' In safety is ", ('kostya', 'в'), ('kostya', 'безопасности'), ', built from without and danger.']),
    (2, None, ["'Kostya, thank you so much for the help.' Huge thanks, meaning thank you so much, is ", ('nastya', 'огромное'), ('nastya', 'спасибо'), '. For the help is ', ('nastya', 'за'), ('nastya', 'помощь'), '.']),
    (3, None, ["'You are such a brave guy to me!' We hear for to me is ", ('nastya', 'у'), ('nastya', 'меня'), '. Brave guy is ', ('nastya', 'смелый'), ('nastya', 'парень'), '.']),
    (4, None, ["'I simply helped the people go outside.' Helped is ", ('kostya', 'помог'), '. To go out is ', ('kostya', 'выйти'), '.']),
    (5, None, ["'You are a real hero of our restaurant!' Real is ", ('nastya', 'настоящий'), '. Of our restaurant is ', ('nastya', 'нашего'), ('nastya', 'ресторана'), '.']),
    (6, None, ["'They apologised to us there for the inconvenience.' In front of us is ", ('guest', 'Перед'), ('guest', 'нами'), ', and apologised is ', ('guest', 'извинились'), '. Inconvenience is ', ('guest', 'неудобства'), '.']),
    (7, None, ["'The restaurant next door is closed for technical reasons.' Closed is ", ('guest', 'закрыт'), '. For technical reasons is ', ('guest', 'по'), ('guest', 'техническим'), ('guest', 'причинам'), '.']),
    (8, None, ["'And where do we have dinner now?' To have supper is ", ('guest', 'поужинать'), '. Where then is ', ('guest', 'где'), ('guest', 'же'), '. For us is ', ('guest', 'нам'), '.']),
    (9, None, ["'Hey, let's go to that other restaurant instead!' Listen is ", ('guest', 'Слушайте'), '. Instead is ', ('guest', 'лучше'), ', and that one over there is ', ('guest', 'тот'), '.']),
    (10, None, ["'All the guests are coming straight to us!' To us is ", ('nastya', 'к'), ('nastya', 'нам'), '. Straight is ', ('nastya', 'прямо'), ', and are coming is ', ('nastya', 'идут'), '.']),
    (11, None, ["'Today our dining room will be full of people.' The of in full of people is hidden in the ending, as people becomes ", ('kostya', 'людей'), '.']),
    (12, None, ["'Let's go quickly to work, beloved bartender!' Beloved is ", ('nastya', 'любимый'), '. Quicker is ', ('nastya', 'скорее'), '. To work is ', ('nastya', 'на'), ('nastya', 'работу'), '.']),
]
