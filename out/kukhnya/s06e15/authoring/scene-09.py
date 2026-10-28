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
    (0, None, "'Hello, my name is Chef Viktor Barinov.' Barinov proceeds wryly across the room, testing the guest's reaction in the middle of the exchange."),
    (1, None, '\'Very nice to meet you, what do I owe the pleasure to?\' The guest jumps in quietly before Barinov and reaches for the Russian word "obyazan" ("obliged, owing", built from "obyazannyy") right at the center of the line.'),
    (2, None, '\'I wanted to talk about our sous-chef.\' Barinov follows up vividly on the spot and centers the thought on "su-shefe" ("sous-chef", from "su-shef") without wasting a word.'),
    (3, None, "'Very interesting, I am listening to you attentively.' The guest answers steadily watching Barinov, bringing things back to earth after the buildup."),
    (4, None, '\'It seems to me that Lyova is still young.\' Noting how young things are to Lyova, Barinov reaches for the Russian word "molodoy" ("young") right at the heart of the line.'),
    (5, None, '\'What is that you are saying about me there?\' Leaning in openly before Barinov, Lyova puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (6, None, "'Lyova, and what are you doing over there?' Barinov asks briskly before Lyova can change the subject."),
    (7, None, '\'I see they really do not want to let you go.\' The guest fires back naturally in the exchange and uses "otpuskat" ("to let go, to release") to carry the main weight of the thought.'),
    (8, None, '\'And after all, that is the very best recommendation!\' Mentioning the recommendation on the spot, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (9, None, "'Please, help yourself today on the house.' Mentioning the establishment without a pause, Lyova makes it clear to the guest that he means every word."),
    (10, None, '\'Nastya went to visit her parents today after all.\' Bringing up the parents beside the guest, Lyova puts the weight on "roditelyam" ("to parents", from "roditeli") as the exchange unfolds.'),
    (11, None, '\'So I thought we could sit calmly together.\' Lyova weighs in promptly in the exchange and centers the remark on "spokoyno" ("calmly") without any extra fuss.'),
]
