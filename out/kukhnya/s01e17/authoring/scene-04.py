# Authoring module for kukhnya-s01e17-scene-04.
ID = 'kukhnya-s01e17-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 4
TITLE = 'Дисциплина в зале  (Discipline in the Hall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = "In the dining room, Vika is in a bad mood. She scolds Nastya and Kostya for chatting at work, and then Max comes over to ask what's wrong, and to invite her out. Here is the telling-off in Russian first."
OPENER = "Now slowly, from Vika's first order."
TRANSITION = "Here's the whole telling-off again."
OUTRO = 'Vika doesn\'t say yes or no, which is just how she wants it. "Posmotrim" is a good word to borrow when you don\'t want to commit, since it means "we\'ll see". See you next time!'
CLOSING = ('max', 'До встречи, Вика!')
STORY = [
    ('vika', 'Настя, быстро убери пятый столик!', 'Nastya, quickly clear the fifth table!', [(48, 'Настя, убери пятый столик.')], ''),
    ('vika', 'Вы совсем обнаглели на этой работе?', 'Have you completely lost your nerve at this job?', [(50, 'На работе вы должны работать')], ''),
    ('vika', 'Здесь надо работать, а не обжиматься.', 'One must work here, not cuddle.', [(50, 'На работе вы должны работать, а не обжиматься и ржать.')], ''),
    ('kostya', 'Мы просто спокойно разговаривали, Виктория Сергеевна.', 'We were just calmly talking, Viktoria Sergeevna.', [], ''),
    ('vika', 'У нас строго запрещены любые отношения!', 'Any relationships are strictly forbidden here!', [(51, 'Или вам напомнить, что у нас запрещены отношения?')], ''),
    ('kostya', 'Мы ничего плохого не сделали.', 'We did nothing bad.', [(55, 'Да мы ничего такого и не сделали.')], ''),
    ('vika', 'Быстро идите работать в зал.', 'Quickly go work in the hall.', [(56, 'Настя, быстро в зал.')], ''),
    ('max', 'Вика, почему ты такая напряжённая?', 'Vika, why are you so tense?', [(58, 'Мне кажется, какая-то напряженная.')], ''),
    ('vika', 'У меня очень много сложных дел.', 'I have very many difficult matters.', [], ''),
    ('max', 'Пойдём сегодня вечером в классное место?', 'Shall we go to an awesome place tonight?', [(59, 'вечером мы с тобой идем в одно офигенное место?')], ''),
    ('vika', 'Макс, я слишком сильно устала.', 'Max, I am too tired.', [(60, 'Я как-то устала.')], ''),
    ('max', 'Там ты отлично отдохнёшь со мной.', 'There you will rest wonderfully with me.', [(60, 'Ну, ты отдохнешь?')], ''),
    ('vika', 'Посмотрим, мне надо подумать об этом.', 'We will see, I need to think about this.', [], ''),
]
WALK = [
    (0, None, '\'Nastya, clear table five, quickly!\' "Stolik" is a little "stol", table, and restaurants number them: "pyatyy stolik", the fifth table. "Uberi" means "clear away".'),
    (1, None, '\'Have you completely lost all shame at this job?\' "Obnagleli" comes from "naglyy", cheeky. "Sovsem" means "completely".'),
    (2, None, '\'You\'re here to work, not to cuddle.\' "Nado rabotat" is "one has to work". "A ne" means "and not", and "obzhimatsya" is a slangy word for hugging and squeezing.'),
    (3, None, '\'We were just quietly talking, Viktoria Sergeevna.\' Kostya uses her first name and her father\'s name, "Viktoriya Sergeevna", which is how staff address a boss.'),
    (4, None, '\'Any relationships are strictly forbidden here!\' "U nas", literally "at us", means "here, at our place". "Zapreshcheny", forbidden, is plural to match "otnosheniya", relationships.'),
    (5, None, '\'We didn\'t do anything wrong.\' "Nichego plokhogo" is literally "nothing of bad", and "ne" still comes before the action.'),
    (6, None, '\'Quick, go and work in the dining room.\' "Zal" is the dining room of a restaurant. "Idite" ends in "-ite" because she\'s sending both of them.'),
    (7, None, '\'Vika, why are you so tense?\' "Takaya" ends in "-aya" to match Vika; about a man Max would say "takoy".'),
    (8, None, '\'I have so many difficult things to deal with.\' After "mnogo", a lot, the words change shape: "dela" becomes "del", and "slozhnye" becomes "slozhnykh".'),
    (9, None, '\'Shall we go somewhere cool tonight?\' "Klassnyy" is casual praise, like "cool". "Segodnya vecherom" is literally "today in the evening".'),
    (10, None, '\'Max, I\'m far too tired.\' "Ustala" ends in "-a" because Vika is a woman; Max would say "ustal". "Slishkom" means "too".'),
    (11, None, '\'You\'ll get a really good rest there with me.\' "Otdokhnyosh" comes from "otdykhat", to rest, which is also what Russians say for going on holiday. "S" grows to "so" before "mnoy".'),
    (12, None, '\'We\'ll see, I need to think about it.\' "Posmotrim", we\'ll see, is the classic way to say neither yes nor no. "O", about, grows to "ob" before the vowel in "etom".'),
]
