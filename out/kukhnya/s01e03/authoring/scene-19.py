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
    ('barinov', 'Огузок, иди сюда прямо сейчас!', 'Runt, come here right now!', [(328, 'Подведем итоги')], ''),
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
    (0, None, '\'Chef, excuse us for this noise.\' "Excuse us" is the polite command with "us". The reason follows after the little word "za".'),
    (1, None, '\'Do not worry, this pistol was not real.\' "Don\'t worry" is built on "bez pokoya", without peace. "Real" is the "true love" word.'),
    (2, None, '\'Here is generous money for these inconveniences.\' "Inconveniences" is "ne" plus "comforts", so it means "discomforts". "Generous" ends in the plural because "money" is plural in Russian.'),
    (3, None, '\'Thank you, we are glad to help our guests.\' "Glad" has a plural ending, "rady". "Guests" ends in "-am", which means "to".'),
    (4, None, '\'Runt, come here right now!\' The nickname again. And "go here" stands for "come here".'),
    (5, None, '\'Chef, do you want to fire me?\' "Do you want to fire" is two short words. "Me" takes the object form.'),
    (6, None, '\'Let us sum up your first work week.\' "Sum up" is literally "lead up the totals". "Week" changes to "nedeli" in this position.'),
    (7, None, '\'On the first day you almost poisoned a guest.\' Russians say "in the first day". "Almost" is "barely not", and the guest takes the animate ending, "-ya".'),
    (8, None, '\'On the second day you started a brawl in the bar.\' It\'s "vo vtoroy", with "vo" not "v", since "vt" is hard to say. "Started a brawl" is "arranged a fight".'),
    (9, None, '\'You angered our chief art director.\' "Angered" has "zloy", angry, inside. "Chief" is the "main" word.'),
    (10, None, '\'And today you were almost shot!\' With no subject, "they shot" is how Russians say it when the gunman is unnamed. "Almost" is the "chut\' ne" again.'),
    (11, None, '\'Chef, I promise to work much better.\' "I promise" is a single word. "Much better" is literally "by much better".'),
    (12, None, '\'Looks like you fit right into the team!\' Russians say "write yourself into" for "fit in". The first word is "looks like".'),
    (13, None, '\'Let us head quickly to work in our kitchen.\' "Went" is used as "let\'s go", a favorite trick of Russian. "To our kitchen" ends in -u.'),
]
