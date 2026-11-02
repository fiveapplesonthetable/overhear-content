# Authoring module for kukhnya-s01e03-scene-19.
ID = 'kukhnya-s01e03-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 19
TITLE = 'Итоги первой недели  (First Week Summary)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'The guest at the table is embarrassed by the commotion and hands the chef some money for the trouble. Then Barinov turns to Max and sums up his first week, one disaster at a time. This is the Russian first.'
OPENER = "Let's go back through the week."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max has survived his first week, and he\'s still employed. Notice how Russians count off days: "in the first day", "in the second day".'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('guest', 'Шеф, извините нас за этот шум.', 'Chef, excuse us for this noise.', [(321, 'Извините нас.')], ''),
    ('guest', 'Не беспокойтесь, этот пистолет был не настоящий.', 'Do not worry, this pistol was not real.', [(323, 'это был не настоящий пистолет.')], ''),
    ('guest', 'Вот вам щедрые деньги за эти неудобства.', 'Here is generous money for these inconveniences.', [(325, 'Вот возьмите, тут всем сотрудникам')], ''),
    ('barinov', 'Спасибо, мы рады помочь нашим гостям.', 'Thank you, we are glad to help our guests.', [(327, 'Договорились.')], ''),
    ('barinov', 'Огузок, иди сюда прямо сейчас!', 'Oguzok, come here right now!', [(328, 'Подведем итоги')], ''),
    ('max', 'Шеф, вы хотите меня уволить?', 'Chef, do you want to fire me?', [(328, 'Подведем итоги твоей первой рабочей недели.')], ''),
    ('barinov', 'Подведём итоги твоей первой рабочей недели.', 'Let us sum up your first work week.', [(328, 'Подведем итоги твоей первой рабочей недели.')], ''),
    ('barinov', 'В первый день ты чуть не отравил гостя.', 'On the first day you almost poisoned a guest.', [(329, 'В первый день ты чуть не отравил человека,')], ''),
    ('barinov', 'Во второй день ты устроил драку в баре.', 'On the second day you started a brawl in the bar.', [(330, 'во второй день подрался с барменом, разгромил весь бар.')], ''),
    ('barinov', 'Ты разозлил нашего главного арт-директора.', 'You angered our chief art director.', [(331, 'Викторию Сергеевну,')], ''),
    ('barinov', 'А сегодня тебя чуть не застрелили!', 'And today you were almost shot!', [(332, 'а сегодня тебя чуть вообще не пристрелили.')], ''),
    ('max', 'Шеф, я обещаю работать намного лучше.', 'Chef, I promise to work much better.', [(333, 'Похоже, ты вписываешься в наш коллектив.')], ''),
    ('barinov', 'Похоже, ты отлично вписываешься в коллектив!', 'Looks like you fit right into the team!', [(333, 'Похоже, ты вписываешься в наш коллектив.')], ''),
    ('barinov', 'Пошли скорее работать на нашу кухню.', 'Let us head quickly to work in our kitchen.', [(334, 'Пошли.')], ''),
]
WALK = [
    (0, None, ("'Chef, excuse us for this noise.' The word for \"excuse us\" is ", ('guest', 'извините нас'), ", a polite request. The reason follows ", ('guest', 'за'), ": ", ('guest', 'за этот шум.'), " translates to for this noise.")),
    (1, None, ("'Do not worry, this pistol was not real.' The word for \"don't worry\", ", ('guest', 'Не беспокойтесь,'), " hides the words for \"without peace\". ", ('guest', 'не настоящий.'), " translates to \"not real\".")),
    (2, None, ("'Here is generous money for these inconveniences.' The word for inconveniences, ", ('guest', 'неудобства.'), " is built from \"not\" plus comforts. Money, ", ('guest', 'деньги'), " is a shape for more than one, so generous, ", ('guest', 'щедрые'), " is also a shape for more than one.")),
    (3, None, ("'Thank you, we are glad to help our guests.' The word for glad, ", ('barinov', 'рады'), " takes the shape for more than one for \"we\". ", ('barinov', 'нашим гостям.'), " literally translates to \"to our guests\", because they help \"to\" someone.")),
    (4, None, ("'Oguzok, come here right now!' The nickname again. ", ('barinov', 'иди сюда'), " literally translates to \"go to here\", and ", ('barinov', 'прямо сейчас!'), " is the word for \"right now\".")),
    (5, None, ("'Chef, do you want to fire me?' The word for you want, ", ('max', 'хотите'), " is the polite shape. ", ('max', 'уволить?'), " translates to \"to fire\", and ", ('max', 'меня'), " is \"me\".")),
    (6, None, ("'Let us sum up your first work week.' ", ('barinov', 'Подведём итоги'), " literally translates to \"let's bring up the totals\", the set phrase for summing up. The word for week becomes ", ('barinov', 'недели.'), " to show it means \"of the week\".")),
    (7, None, ("'On the first day you almost poisoned a guest.' They say ", ('barinov', 'В первый день'), " literally \"in the first day\". ", ('barinov', 'чуть не отравил'), " translates to \"barely not poisoned\", and the word for guest becomes ", ('barinov', 'гостя.'))),
    (8, None, ("'On the second day you started a brawl in the bar.' The word for \"in the second\" is ", ('barinov', 'Во второй'), " with an extra letter before the starting sounds. ", ('barinov', 'устроил драку'), " literally translates to \"arranged a fight\".")),
    (9, None, ("'You angered our chief art director.' The action word for angered, ", ('barinov', 'разозлил'), " is built from the word for \"angry\" inside. ", ('barinov', 'главного арт-директора.'), " changes shape at the end because they are the person angered.")),
    (10, None, ("'And today you were almost shot!' ", ('barinov', 'тебя чуть не застрелили!'), " literally translates to \"you barely not they shot\". With no actor named, this shape for the action word leaves the shooter unnamed.")),
    (11, None, ("'Chef, I promise to work much better.' This promise is built from ", ('max', 'обещаю'), " \"I promise\", plus ", ('max', 'работать'), " \"to work\". The word for \"by a lot\", ", ('max', 'намного'), " goes in front of ", ('max', 'лучше.'), " \"better\", the way \"much\" does.")),
    (12, None, ("'Looks like you fit right into the team!' ", ('barinov', 'Похоже,'), " is built from the word for similar, and translates to \"it looks like\". The word for fit in, ", ('barinov', 'вписываешься'), " literally translates to \"you write yourself in\".")),
    (13, None, ("'Let us head quickly to work in our kitchen.' The word for \"let's go\", ", ('barinov', 'Пошли'), " is a shape of the action word from the past. ", ('barinov', 'на нашу кухню.'), " translates to \"onto our kitchen\", changing the ending for heading there.")),
]
