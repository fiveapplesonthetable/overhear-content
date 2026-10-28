# Authoring module for kukhnya-s01e10-scene-04.
ID = 'kukhnya-s01e10-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 4
TITLE = 'Низкий гонорар  (A Low Fee)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'girl': 'Девушка'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "In the dining room of Claude Monet, a representative from a television studio meets with Chef Viktor Barinov. Impressed by his past guest appearance, producers want him to become the permanent host of a weekly morning cooking program, but their proposed fee leads to immediate outrage. Let's listen to their conversation in Russian first."
OPENER = "Now let's examine the television negotiation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Furious at the insultingly modest payment offer, Chef Barinov turns his back on television stardom and returns to the comfort of his own high-end restaurant. Next time you watch the episode, listen for the Russian expressions for 'carefully' and 'broadcast' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Здравствуйте, я вас внимательно слушаю.', 'Hello, I am listening to you attentively.', [(7, 'Я вас слушаю. Здравствуйте, Виктор')], ''),
    ('girl', 'Вы отлично выступали в нашем кулинарном шоу.', 'You performed wonderfully on our culinary show.', [(8, 'кулинарном шоу?')], ''),
    ('barinov', 'И что решили ваши строгие продюсеры?', 'And what did your strict producers decide?', [(9, 'нашим продюсерам.')], ''),
    ('girl', 'Мы хотим предложить вам постоянную работу.', 'We want to offer you a permanent job.', [(10, 'хотят предложить вам')], ''),
    ('barinov', 'Во сколько вы оценили мою работу?', 'At how much did you value my work?', [(12, 'во сколько ваши продюсеры оценили мою работу?')], ''),
    ('girl', 'Десять тысяч за каждую новую передачу.', 'Ten thousand for each new broadcast.', [(14, 'Десять, десять одна программа.')], ''),
    ('barinov', 'Десять тысяч евро за один выпуск?', 'Ten thousand euros for one episode?', [(15, 'Евро?')], ''),
    ('girl', 'Нет, мы платим десять тысяч рублей.', 'No, we pay ten thousand rubles.', [(15, 'Рублей.')], ''),
    ('barinov', 'Тогда до свидания, а лучше прощайте!', 'Then goodbye, or rather farewell!', [(16, 'До свидания. Нет, лучше прощайте.')], ''),
    ('girl', 'Подождите, Виктор, давайте спокойно всё обсудим.', 'Wait, Viktor, let us calmly discuss everything.', [(17, 'Подождите. Давайте мы с вами обсудим.')], ''),
    ('barinov', 'Вы предлагаете работать в мой выходной день.', 'You propose that I work on my day off.', [(18, 'Вы мне предлагаете работать в мой выходной день')], ''),
    ('girl', 'Это сделает ваш ресторан очень известным.', 'This will make your restaurant very famous.', [], ''),
    ('barinov', 'Я не работаю за такие смешные копейки!', 'I do not work for such ridiculous kopecks!', [(19, 'да еще за копейки.')], ''),
]
WALK = [
    (0, None, "'Hello, I am listening to you attentively.' Putting on his polite professional manner, Barinov greets the television representative and invites her to speak."),
    (1, None, "'You performed wonderfully on our culinary show.' The young producer starts with flattery, praising how well Viktor performed on their cooking show."),
    (2, None, "'And what did your strict producers decide?' Flattered and intrigued, Barinov asks what her strict studio producers have decided."),
    (3, None, "'We want to offer you a permanent job.' Woman voices the thought smoothly and naturally."),
    (4, None, "'At how much did you value my work?' Getting straight to business, he asks how much the network is offering to pay him."),
    (5, None, "'Ten thousand for each new broadcast.' She names the studio's offer: ten thousand for each new episode of the morning show."),
    (6, None, "'Ten thousand euros for one episode?' Barinov's eyes light up, assuming the television network means ten thousand euros per broadcast."),
    (7, None, "'No, we pay ten thousand rubles.' Woman puts the idea across in a natural everyday manner."),
    (8, None, "'Then goodbye, or rather farewell!' Outraged to hear the offer is in rubles, Barinov dramatically bids her farewell on the spot."),
    (9, None, "'Wait, Viktor, let us calmly discuss everything.' Taken aback by his outburst, the producer asks Viktor to wait and discuss the offer calmly."),
    (10, None, "'You propose that I work on my day off.' Barinov articulates the point with simple everyday clarity."),
    (11, None, "'This will make your restaurant very famous.' She tries to sweeten the deal by arguing that television exposure will make his restaurant famous."),
    (12, None, "'I do not work for such ridiculous kopecks!' Insulted by the low pay, Barinov scoffs that a master chef does not work for mere pennies."),
]
