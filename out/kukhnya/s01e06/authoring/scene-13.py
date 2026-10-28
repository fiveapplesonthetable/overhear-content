# Authoring module for kukhnya-s01e06-scene-13.
ID = 'kukhnya-s01e06-scene-13'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 13
TITLE = 'Неожиданная находка  (An Unexpected Find)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'rodion': 'Родион'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Behind Claude Monet, Max and Kostya are digging through the bins. The 'rotten potatoes' they threw out were the chef's truffles, and now a very polite stranger called Rodion is holding the box. It's in Russian first."
OPENER = 'Let\'s go through the meeting. Max is in a hurry and says "ty", Rodion takes his time and says "vy".'
TRANSITION = 'Once more, the whole meeting by the bins.'
OUTRO = 'Rodion shows you how to introduce yourself properly: "menya zovut", "ochen priyatno", and a name with the father\'s name after it. Russians use that full form with anyone older. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Где ты нашёл эту коробку?', 'Where did you find this box?', [(182, 'не это ищете')], ''),
    ('rodion', 'Вы искали дорогие трюфели на помойке.', 'You were looking for expensive truffles in the trash.', [(182, 'Вы, случайно, не это ищете?')], ''),
    ('max', 'Пожалуйста, отдай их нам скорее обратно!', 'Please, give them back to us quickly!', [(183, 'А ну-ка, дай сюда!')], ''),
    ('rodion', 'Сначала представьтесь вежливо, молодой человек.', 'First introduce yourself politely, young man.', [(185, 'Как грубо!')], ''),
    ('max', 'Меня зовут Макс, а это Костя.', 'My name is Max, and this is Kostya.', [(186, 'позволь')], ''),
    ('rodion', 'Очень приятно, а я Родион Сергеевич.', 'Very pleased, and I am Rodion Sergeyevich.', [(186, 'Меня зовут Родион Сергеевич')], ''),
    ('max', 'Что ты хочешь за эти грибы?', 'What do you want for these mushrooms?', [(187, 'А трюфели в надежном месте')], ''),
    ('rodion', 'Мне нужна одна небольшая дружеская услуга.', 'I need one small friendly favor.', [(189, 'обмен на маленькую услугу')], ''),
    ('max', 'Мы можем заплатить тебе немного денег.', 'We can pay you a little money.', [(178, 'денег')], ''),
    ('rodion', 'Нет, я хочу роскошный обед здесь.', 'No, I want a luxurious lunch here.', [(169, 'нет')], ''),
    ('max', 'Но охранники не пустят тебя внутрь!', "But the guards won't let you inside!", [(190, 'Его не пустят в зал')], ''),
    ('rodion', 'Тогда найдите мне подходящую чистую одежду.', 'Then find me suitable clean clothes.', [(192, 'Я гражданин мира')], ''),
    ('max', 'Хорошо, пойдём скорее в нашу раздевалку.', "Alright, let's go quickly into our locker room.", [(193, 'Это шкафчик')], ''),
]
WALK = [
    (0, None, '\'Where did you find this box?\' Max says "ty" to a total stranger, which is pushy, and Rodion will notice. "Nashyol", found, has no ending because the finder is a man.'),
    (1, None, '\'You were looking for expensive truffles in the trash.\' Rodion answers with "vy", the polite form, so he\'s already the better-mannered one. "Na pomoyke", at the dump, uses "na", \'on\', the way Russians talk about open places.'),
    (2, None, '\'Please, give them back to us quickly!\' "Otday", give back, adds ot-, away, to day, give. "Obratno", back, makes the \'return\' even clearer.'),
    (3, None, '\'First introduce yourself politely, young man.\' "Predstavtes", introduce yourself, ends in -tes, the polite command with -sya on it. "Molodoy" chelovek, young man, is how you address a man you don\'t know.'),
    (4, None, '\'My name is Max, and this is Kostya.\' "Menya zovut Maks" is \'me they call Max\', with no \'they\' ever said. "A eto", \'and this is\', is the way to present a friend.'),
    (5, None, '\'Very pleased, and I am Rodion Sergeyevich.\' "Ochen priyatno", \'very pleasant\', is what you say on meeting someone. Sergeyevich, the father\'s name, means his father was Sergey.'),
    (6, None, '\'What do you want for these mushrooms?\' Max calls the truffles "griby", mushrooms, which technically they are. "Za" here means \'in exchange for\', as in "za eti griby".'),
    (7, None, '\'I need one small friendly favour.\' "Mne nuzhna", \'to me needed\', gets its -a from "usluga", favour. "Nebolshaya", small, is just "ne", not, joined to "bolshaya", big.'),
    (8, None, '\'We can pay you a little money.\' After "nemnogo", a little, "dengi", money, turns into "deneg". "Tebe", to you, is the person being paid.'),
    (9, None, '\'No, I want a luxurious lunch here.\' "Obed" is the main meal of the Russian day, eaten around one or two. "Roskoshnyy", luxurious, comes from roskosh, luxury.'),
    (10, None, '\'But the guards won\'t let you inside!\' "Ne pustyat", they won\'t let him in, uses "pustit", to let go or let in. "Vnutr", inside, is used for going in; for being inside it\'s "vnutri".'),
    (11, None, '\'Then find me suitable clean clothes.\' "Odezhda", clothes, is a singular word, like \'clothing\'. "Naydite", find, is the "vy" command, because now Rodion is talking to both of them.'),
    (12, None, '\'Alright, let\'s go quickly into our locker room.\' "Poydyom", let\'s go, is \'we will go\' used as an invitation. "Razdevalka", changing room, grows out of "razdevatsya", to get undressed.'),
]
