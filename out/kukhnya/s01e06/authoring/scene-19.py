# Authoring module for kukhnya-s01e06-scene-19.
ID = 'kukhnya-s01e06-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 19
TITLE = 'Заказ на трюфели  (The Truffle Order)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet, Barinov needs a truffle for table seven, and Max knows exactly where the truffles are not: they went out with the rubbish. He grabs Nastya, the waitress, and begs her to talk the guest out of it. It's in Russian first."
OPENER = "Let's replay it. Barinov shouts, Max panics, and Nastya keeps her head."
TRANSITION = 'And now the panic over the truffle, straight through.'
OUTRO = 'Max gave you "mne nuzhna pomoshch", I need help, and "skazhi gostyu", tell the guest, and Nastya gave you "ne mogu", I can\'t. Useful when you\'re covering up a mistake. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('barinov', 'Огузок, тащи сюда скорее один трюфель!', 'Rump, bring one truffle here quickly!', [(238, 'Агузок, тащи сюда один трюфель')], ''),
    ('barinov', 'Седьмой столик заказал салат с трюфелями.', 'Table seven ordered a salad with truffles.', [(237, 'салат с трюфелями за седьмой столик')], ''),
    ('max', 'Шеф, я сейчас всё быстро принесу.', 'Chef, I will bring everything quickly now.', [], ''),
    ('max', 'Настя, стой, мне срочно нужна помощь!', 'Nastya, stop, I urgently need help!', [(239, 'Слушай, Настя')], ''),
    ('nastya', 'Что случилось, Макс? Что такое?', 'What happened, Max? What is it?', [], ''),
    ('max', 'Скажи гостю, что трюфели сегодня плохие.', 'Tell the guest that the truffles are bad today.', [(239, 'трюфеля сегодня не очень')], ''),
    ('max', 'Пусть он закажет любое другое блюдо!', 'Let him order any other dish!', [(240, 'что-нибудь другое заказали')], ''),
    ('nastya', 'Нет, я не могу так сказать.', 'No, I cannot say that.', [(241, 'Не, не могу')], ''),
    ('nastya', 'Гость пришёл специально ради этого салата.', 'The guest came especially for this salad.', [(241, 'пришел сюда специально ради этого блюда')], ''),
    ('max', 'Но у меня нет этого трюфеля!', 'But I do not have this truffle!', [], ''),
    ('nastya', 'Он очень строгий и важный человек.', 'He is a very strict and important person.', [], ''),
    ('nastya', 'Кстати, он просил передать тебе записку.', 'By the way, he asked to give you a note.', [(242, 'просил тебе вот это передать')], ''),
    ('max', 'О нет, это катастрофа для кухни!', 'Oh no, this is a disaster for the kitchen!', [], ''),
    ('nastya', 'Торопись, шеф уже очень сильно злится.', 'Hurry, the chef is already getting very angry.', [], ''),
]
WALK = [
    (0, None, ["'Rump, bring one truffle here quickly!' Listen how the chef demands action with ", ('barinov', 'тащи'), ', meaning to haul or drag.']),
    (1, None, ["'Table seven ordered a salad with truffles.' Notice how they number tables using ", ('barinov', 'Седьмой'), ', which actually translates to seventh.']),
    (2, None, ["'Chef, I will bring everything quickly now.' See the way he promises action with ", ('max', 'принесу'), ', meaning he will carry it over.']),
    (3, None, ["'Nastya, stop, I urgently need help!' Pay attention to the desperate plea with ", ('max', 'срочно'), ', showing he needs it right this second.']),
    (4, None, ["'What happened, Max? What is it?' Watch out for the standard asking phrase ", ('nastya', 'случилось'), ', questioning what took place.']),
    (5, None, ["'Tell the guest that the truffles are bad today.' Catch how he shifts the blame with ", ('max', 'плохие'), ', describing them as terrible quality.']),
    (6, None, ["'Let him order any other dish!' Check out the word for any, ", ('max', 'любое'), ', giving the customer absolute freedom.']),
    (7, None, ["'No, I cannot say that.' Hear how she flatly refuses to speak, using ", ('nastya', 'сказать'), ', meaning to tell him.']),
    (8, None, ["'The guest came especially for this salad.' It is interesting that she points out ", ('nastya', 'ради'), ', meaning for the sake of.']),
    (9, None, ["'But I do not have this truffle!' You can hear his panic when admitting ", ('max', 'нет'), ', showing it is completely gone.']),
    (10, None, ["'He is a very strict and important person.' The waitress describes the serious guest as ", ('nastya', 'строгий'), ', meaning he is demanding.']),
    (11, None, ["'By the way, he asked to give you a note.' Observe the smooth subject change starting with ", ('nastya', 'Кстати'), ', bringing up a new point.']),
    (12, None, ["'Oh no, this is a disaster for the kitchen!' Feel the complete despair when he cries ", ('max', 'катастрофа'), ', which sounds exactly like what it is.']),
    (13, None, ["'Hurry, the chef is already getting very angry.' We catch the final warning to move fast with ", ('nastya', 'Торопись'), ', pushing him to speed up.']),
]
