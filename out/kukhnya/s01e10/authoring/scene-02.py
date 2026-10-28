# Authoring module for kukhnya-s01e10-scene-02.
ID = 'kukhnya-s01e10-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 2
TITLE = 'Утренний рассол  (Morning Brine)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "Early in the morning in the kitchen of Claude Monet, Chef Viktor Barinov is suffering from an agonizing headache after an exhausting night. Seeing his boss in distress, line cook Senya rushes over with the ultimate traditional remedy: a cold glass of pickle brine. Let's listen to their short kitchen exchange in Russian first."
OPENER = "Now let's examine the morning hangover remedy line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "With his headache slowly easing thanks to Senya's timely brine, Chef Barinov readies himself to supervise the busy lunch service at Claude Monet. Next time you watch the episode, listen for the Russian expressions for 'to be ill' and 'more' — you will catch every word right away. See you next time!"
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, как ваше здоровье сегодня утром?', 'Chef, how is your health this morning?', [(4, 'Шеф!')], ''),
    ('barinov', 'Сеня, отойди, у меня болит голова.', 'Senya, step back, my head hurts.', [], ''),
    ('senya', 'Я принёс вам холодный свежий рассол.', 'I brought you cold fresh brine.', [(5, 'Рассольчик!')], ''),
    ('barinov', 'О, Сеня, ты настоящий верный друг.', 'Oh, Senya, you are a true loyal friend.', [], ''),
    ('senya', 'Выпей немного, сразу станет гораздо легче.', 'Drink a little, it will immediately become much easier.', [], ''),
    ('barinov', 'Этот напиток очень помогает мне.', 'This drink helps me very much.', [], ''),
    ('senya', 'Вчера Спартак снова проиграл важный матч?', 'Did Spartak lose an important match again yesterday?', [], ''),
    ('barinov', 'Не говори мне про этот кошмар.', 'Do not talk to me about that nightmare.', [], ''),
    ('senya', 'Понятно, шеф, больше никаких лишних слов.', 'Understood, chef, no more unnecessary words.', [], ''),
    ('barinov', 'Принеси мне ещё один стакан рассола.', 'Bring me one more glass of brine.', [], ''),
    ('senya', 'Сейчас быстро принесу из нашей кухни.', 'I will quickly bring it now from our kitchen.', [], ''),
    ('barinov', 'И начинайте готовить обед для гостей.', 'And begin preparing lunch for the guests.', [], ''),
    ('senya', 'Всё будет готово вовремя, шеф.', 'Everything will be ready on time, chef.', [], ''),
]
WALK = [
    (0, None, "'Chef, how is your health this morning?' Russian leaves out the word for 'to be' here, linking 'chef' directly with 'how', pairing it with 'health' and 'today'."),
    (1, None, "'Senya, step back, my head hurts.' Barinov uses the classic style — literally 'at me' rather than a word for 'to have', pairing it with 'step back' and 'hurts'."),
    (2, None, "'I brought you cold fresh brine.' Senya uses the word for 'brought' to focus on the completed action, pairing it with 'cold' and 'fresh'."),
    (3, None, "'Oh, Senya, you are a true loyal friend.' Russian leaves out the word for 'to be' here, linking 'oh' directly with 'true', pairing it with 'loyal' and 'friend'."),
    (4, None, "'Drink a little, it will immediately become much easier.' Senya leads with the direct word for 'drink', pairing it with 'a little' and 'immediately'."),
    (5, None, "'This drink helps me very much.' Barinov anchors the line on the word for 'drink' and builds the thought around 'very much' and 'helps'."),
    (6, None, "'Did Spartak lose an important match again yesterday?' Senya asks this purely through rising tone on the word for 'yesterday', pairing it with 'again' and 'lost'."),
    (7, None, "'Do not talk to me about that nightmare.' Barinov leads with the direct word for 'speak', followed by 'nightmare'."),
    (8, None, "'Understood, chef, no more unnecessary words.' Russian leaves out the word for 'to be' here, linking 'understood' directly with 'chef', pairing it with 'more' and 'unnecessary'."),
    (9, None, "'Bring me one more glass of brine.' Barinov leads with the direct word for 'bring', pairing it with 'more' and 'one'."),
    (10, None, "'I will quickly bring it now from our kitchen.' Senya opens with 'now' before bringing in 'quickly' and 'will bring' to make the point clear."),
    (11, None, "'And begin preparing lunch for the guests.' Barinov leads with the direct word for 'begin', pairing it with 'to cook' and 'lunch'."),
    (12, None, "'Everything will be ready on time, chef.' Senya chooses the word for 'will' for the ongoing action, followed by 'ready' and 'on time'."),
]
