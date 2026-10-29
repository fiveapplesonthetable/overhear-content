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
    (0, None, '\'Chef, excuse us for this noise.\' "Izvinite nas" is "excuse us", a polite command. The reason follows "za": "za etot shum", for this noise.'),
    (1, None, '\'Do not worry, this pistol was not real.\' "Ne bespokoytes\'", don\'t worry, hides "bez pokoya", without peace. "Ne nastoyashchiy" is "not real".'),
    (2, None, '\'Here is generous money for these inconveniences.\' "Neudobstva" is "ne" plus "udobstva", comforts. "Den\'gi" is plural, so "shchedryye", generous, is plural too.'),
    (3, None, '\'Thank you, we are glad to help our guests.\' "Rady", glad, is plural for "we". "Nashim gostyam" is "to our guests", because Russians help "to" someone.'),
    (4, None, '\'Oguzok, come here right now!\' The nickname again. "Idi syuda" is "go to here", and "pryamo seychas" is "right now".'),
    (5, None, '\'Chef, do you want to fire me?\' "Khotite", you want, is the polite form. "Uvolit\'" is "to fire", and "menya" is "me".'),
    (6, None, '\'Let us sum up your first work week.\' "Podvedyom itogi" is "let\'s bring up the totals", the set phrase for summing up. "Nedelya", week, becomes "nedeli" for "of the week".'),
    (7, None, '\'On the first day you almost poisoned a guest.\' Russians say "v pervyy den\'", in the first day. "Chut\' ne otravil" is "barely not poisoned", and "gost\'" becomes "gostya".'),
    (8, None, '\'On the second day you started a brawl in the bar.\' It\'s "vo vtoroy", with "vo" instead of "v" before "vt". "Ustroil draku" is "arranged a fight".'),
    (9, None, '\'You angered our chief art director.\' "Razozlil", angered, has "zloy", angry, inside. "Glavnogo art-direktora" ends in -ogo and -a as the person angered.'),
    (10, None, '\'And today you were almost shot!\' "Tebya chut\' ne zastrelili" is "you barely not they shot". With no subject, the -li verb leaves the shooter unnamed.'),
    (11, None, '\'Chef, I promise to work much better.\' This promise is built like the English one: "obeshchayu", I promise, plus "rabotat\'", to work. "Namnogo", by a lot, goes in front of "luchshe", better, the way "much" does.'),
    (12, None, '\'Looks like you fit right into the team!\' "Pokhozhe" is "it looks like", from "pokhozhiy", similar. "Vpisyvayesh\'sya" is "you write yourself in", the Russian "fit in".'),
    (13, None, '\'Let us head quickly to work in our kitchen.\' "Poshli" is a past form used as "let\'s go". "Na nashu kukhnyu" is "onto our kitchen", with -u for heading there.'),
]
