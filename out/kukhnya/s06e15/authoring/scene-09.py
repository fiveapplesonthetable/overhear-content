# Authoring module for kukhnya-s06e15-scene-09.
ID = 'kukhnya-s06e15-scene-09'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 15
SCENE = 9
TITLE = 'Звонок ресторатору  (Call to the Restaurateur)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.15'
SOURCE_FILE = 'sources/kukhnya/s06/e15.ru.srt'
INTRO = "Chef Barinov secretly takes the banknote with Tumanov's phone number and calls the restaurateur to claim that Lyova is not ready to be a head chef. Lyova walks into the office and catches Chef Barinov badmouthing him on the phone, while Tumanov tells Chef Barinov that his reluctance to let Lyova go is the best recommendation."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Furious at Chef Barinov's phone call, Lyova becomes even more determined to leave, while Kostya tries to play matchmaker at the bar. Until next time!"
CLOSING = ('guest', 'Всего хорошего!')
STORY = [
    ('barinov', 'Здравствуйте, меня зовут шеф Виктор Баринов.', 'Hello, my name is Chef Viktor Barinov.', [(136, 'здравствуйте'), (137, 'Это Виктор Баринов')], 'adapted'),
    ('guest', 'Очень приятно, чем я вам обязан?', 'Very nice to meet you, what do I owe the pleasure to?', [(138, 'Очень приятно. А чем обязан')], 'adapted'),
    ('barinov', 'Я хотел поговорить о нашем су-шефе.', 'I wanted to talk about our sous-chef.', [(139, 'Я хотел поговорить')], 'adapted'),
    ('guest', 'Очень интересно, я внимательно слушаю вас.', 'Very interesting, I am listening to you attentively.', [(140, 'Очень интересно'), (141, 'Слушаю вас')], 'adapted'),
    ('barinov', 'Мне кажется, что Лёва ещё молодой.', 'It seems to me that Lyova is still young.', [(141, 'мне кажется'), (142, 'что Лёва')], 'adapted'),
    ('lyova', 'Что это вы там про меня говорите?', 'What is that you are saying about me there?', [(144, 'Это что значит')], 'adapted'),
    ('barinov', 'Лёва, а ты что там делаешь?', 'Lyova, and what are you doing over there?', [(146, 'Лёва, ты что там делаешь')], 'adapted'),
    ('guest', 'Смотрю, вас очень не хотят отпускать.', 'I see they really do not want to let you go.', [(148, 'Я смотрю, вас очень не хотят отпускать')], 'adapted'),
    ('guest', 'А ведь это самая лучшая рекомендация!', 'And after all, that is the very best recommendation!', [(149, 'И это лучшая рекомендация')], 'adapted'),
    ('lyova', 'Пожалуйста, угощайтесь сегодня за счёт заведения.', 'Please, help yourself today on the house.', [(150, 'Пожалуйста, за счет заведения')], 'adapted'),
    ('lyova', 'Настя ведь сегодня уехала к родителям.', 'Nastya went to visit her parents today after all.', [(152, 'Настя же уехала к родителям')], 'adapted'),
    ('lyova', 'Вот я и подумал спокойно посидеть.', 'So I thought we could sit calmly together.', [(153, 'Вот я и подумал, посидим')], 'adapted'),
]
WALK = [
    (0, None, "'Hello, my name is Chef Viktor Barinov.' Claiming that his name is Chef Viktor Barinov sounds confident, even if the guest has doubts."),
    (1, None, "'Very nice to meet you, what do I owe the pleasure to?' Asking whether very nice to meet Barinov what do he owes the pleasure puts Barinov right on the defensive."),
    (2, None, "'I wanted to talk about our sous-chef.' Noting that he wanted to talk keeps Barinov's side of the story simple and clear."),
    (3, None, '\'Very interesting, I am listening to you attentively.\' Realizing that very interesting he is listening to Barinov attentively changes how the guest handles the situation. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (4, None, "'It seems to me that Lyova is still young.' Because it seems to him that Lyova is still young, Barinov treats the matter as settled."),
    (5, None, '\'What is that you are saying about me there?\' Wondering what that Barinov is saying about him there is is how Lyova puts Barinov on the spot. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, '\'Lyova, and what are you doing over there?\' By wondering what the guest doing over there is, Barinov presses the guest for a straight answer. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (7, None, "'I see they really do not want to let you go.' Because he sees they really do not want to let Barinov goes, the guest treats the matter as settled."),
    (8, None, '\'And after all, that is the very best recommendation!\' Because after all that is the very best recommendation, the guest does not bother softening the blow for Barinov. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, "'Please, help yourself today on the house.' Saying that Barinov should help themselves today on the house is how Lyova sets the tone with Barinov."),
    (10, None, "'Nastya went to visit her parents today after all.' Lyova tells Barinov that Nastya went to visit her parents today after all without dressing it up."),
    (11, None, "'So I thought we could sit calmly together.' Since he thought they could sit calmly together, Lyova does not waste words on excuses."),
]
