# Authoring module for kukhnya-s02e01-scene-05.
ID = 'kukhnya-s02e01-scene-05'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 5
TITLE = 'Букет цветов  (A Bouquet of Flowers)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the dining room of Claude Monet, Bartender Kostya refuses to pour alcohol for Chef Viktor. Meanwhile, Max sends Victoria a large bouquet of flowers and begs for her forgiveness, while Viktor chats with guests at their table. Let us listen to the scene in Russian first.'
OPENER = "Now let us examine Max's apology and Viktor's temptation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "While Victoria coldly rejects Max's flowers and apology, Chef Viktor finds a clever excuse to share a drink with appreciative restaurant guests. Next time you watch the episode, listen for the Russian expressions for 'why' and 'to pour' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Костя, почему ты налил мне простую воду?', 'Kostya, why did you pour me plain water?', [(103, 'Это что? Вода, Виктор Петрович.')], ''),
    ('barinov', 'Новый хозяин боится, что я буду пить.', 'The new owner is afraid that I will drink.', [(104, 'Новый хозяин заплатил мне его наливать, сказал, если налью — уволят.')], ''),
    ('vika', 'Посмотрите, кто прислал мне этот красивый букет?', 'Look, who sent me this beautiful bouquet?', [(105, 'Вам букет передали.'), (106, 'Да? Какой красивый.'), (107, 'От кого? От Макса.')], ''),
    ('max', 'Вика, это я подарил тебе свежие цветы.', 'Vika, it was I who gave you fresh flowers.', [(107, 'От кого? От Макса.')], ''),
    ('max', 'Подожди, пожалуйста, выслушай меня сейчас одну минуту.', 'Wait, please, listen to me right now for one minute.', [(108, 'Подождите, Виктория Сергеевна, понимаете, Макс, дело в том,'), (110, 'Секунду. Вика, я понимаю,')], ''),
    ('max', 'Я понимаю, что сделал вчера ужасный поступок.', 'I understand that I committed a terrible act yesterday.', [(111, 'что совершил ваш ужасный, ужас, ужасный поступок.')], ''),
    ('max', 'Я очень сильно жалею о своей глупости.', 'I very deeply regret my foolishness.', [(109, 'что он очень сильно, очень сожалеет и...')], ''),
    ('max', 'Пожалуйста, прости меня за эту плохую ночь!', 'Please, forgive me for that bad night!', [(112, 'Пожалуйста, прости меня, дурака.')], ''),
    ('vika', 'Я не хочу слушать твои пустые слова.', 'I do not want to listen to your empty words.', [], ''),
    ('barinov', 'Добрый день, я главный повар этого ресторана.', 'Good afternoon, I am the head chef of this restaurant.', [(113, 'Добрый день. Я шеф-повар этого ресторана.')], ''),
    ('barinov', 'Вам нравятся наши сегодняшние горячие блюда?', 'Do you like our hot dishes today?', [(114, 'Вам все нравится? Знаете, все великолепно, очень вкусно.')], ''),
    ('barinov', 'Гости предлагают мне выпить с ними вина.', 'The guests are offering me to drink wine with them.', [(115, 'Может, выпьете с нами?')], ''),
    ('barinov', 'На работе нельзя, но сегодня можно немного!', 'At work it is forbidden, but today a little is allowed!', [(117, 'Я ведь на работе.'), (119, 'Для вас я сделаю скачей.')], ''),
]
WALK = [
    (0, None, "'Kostya, why did you pour me plain water?' Barinov glares at his glass and asks Kostya why he poured plain water."),
    (1, None, "'The new owner is afraid that I will drink.' He grumbles that the new owner is terrified of letting him near a drink."),
    (2, None, "'Look, who sent me this beautiful bouquet?' Meanwhile, Vika admires a big bouquet and wonders who sent it to her."),
    (3, None, "'Vika, it was I who gave you fresh flowers.' Max steps forward and admits that the fresh flowers are from him."),
    (4, None, "'Wait, please, listen to me right now for one minute.' He begs her to pause and hear him out for just one minute."),
    (5, None, "'I understand that I committed a terrible act yesterday.' Max owns up to how terrible his behavior was the night before."),
    (6, None, "'I very deeply regret my foolishness.' He tells Vika how deeply he regrets being so foolish."),
    (7, None, "'Please, forgive me for that bad night!' He pleads with her to forgive him for that awful night."),
    (8, None, "'I do not want to listen to your empty words.' Vika coldly replies that she has no interest in his empty apologies."),
    (9, None, "'Good afternoon, I am the head chef of this restaurant.' Across the room, Barinov introduces himself to a table of guests as the head chef."),
    (10, None, "'Do you like our hot dishes today?' He charmingly asks the diners how they are enjoying today's hot dishes."),
    (11, None, "'The guests are offering me to drink wine with them.' Viktor happily notes that the guests are offering to share a glass of wine with him."),
    (12, None, "'At work it is forbidden, but today a little is allowed!' Even though drinking is banned on shift, he decides a tiny sip with guests counts as an exception."),
]
