# Authoring module for kukhnya-s01e16-scene-10.
ID = 'kukhnya-s01e16-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 10
TITLE = 'Побег через зал  (Escape Through the Hall)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lanovsky': 'Лановский', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The migration inspectors are now inside Claude Monet, and Chef Barinov is trying to get the cooks without papers out through the back door and the dining room. Then a smiling officer walks in and introduces himself. Listen to how calm the major sounds next to the chef.'
OPENER = 'Now the escape and the visitor, line by line.'
TRANSITION = 'And the whole scramble once more, from the top.'
OUTRO = "The major says he will wait, and he sounds like a man with all day. The sentence 'I can't, unfortunately' is a good one to borrow for your own polite refusals. See you next time!"
CLOSING = ('lanovsky', 'До встречи!')
STORY = [
    ('barinov', 'Половина идёт через чёрный ход.', 'Half go through the back door.', [(95, 'Половина через черный ход.')], ''),
    ('barinov', 'Половина идёт через зал.', 'Half go through the dining room.', [(97, 'Половина через зал.')], ''),
    ('max', 'Шеф, чёрный ход закрыт!', 'Chef, the back door is blocked!', [(109, 'Творный закрыт.')], ''),
    ('barinov', 'Что вы за идиоты?', 'What kind of idiots are you?', [(110, 'Что вы за инвалиды?')], ''),
    ('barinov', 'Даже сбежать не можете!', "You can't even run away!", [(111, 'Даже сбежать нормально не можете.')], ''),
    ('barinov', 'Быстро ко мне в кабинет.', 'Quickly, to my office.', [(113, 'Ко мне в кабинет, только тихо.')], ''),
    ('lanovsky', 'Добрый день, Виктор Петрович.', 'Good afternoon, Viktor Petrovich.', [(117, 'О, Виктор Петрович, чрезвычайно рад с вами лично познакомиться.')], ''),
    ('lanovsky', 'Я майор миграционной службы.', 'I am a major of the migration service.', [(121, 'майор федеральной миграционной службы.')], ''),
    ('lanovsky', 'Мы можем пройти в ваш кабинет?', 'Can we go to your office?', [(124, 'Виктор Петрович, мы не могли бы пройти в ваш кабинет и обсудить все там?')], ''),
    ('barinov', 'К сожалению, я не могу.', 'Unfortunately, I cannot.', [(125, 'К сожалению, не могу.')], ''),
    ('barinov', 'Мне нужно готовить для гостей.', 'I need to cook for the guests.', [(127, 'Простите, мне нужно готовить для гостей нашего замечательного ареста.')], ''),
    ('lanovsky', 'Хорошо, я подожду вас здесь.', 'Alright, I will wait for you here.', [(131, 'Я, с вашего позволения, подожду вас здесь.')], ''),
]
WALK = [
    (0, None, "'Half go through the back door.' The back door is 'chyorny khod', literally 'the black way', the staff and delivery entrance. 'Polovina', 'half', takes a singular verb, 'idyot', 'goes'."),
    (1, None, "'Half go through the dining room.' 'Zal' means 'hall', and in a restaurant it is the dining room, where the guests sit. 'Cherez', 'through', is followed by the place unchanged."),
    (2, None, "'Chef, the back door is blocked!' Russian needs no 'is' here: 'khod zakryt' is literally 'door closed'. 'Zakryt' is the word on a shop sign that says 'closed'."),
    (3, None, "'What kind of idiots are you?' 'Chto za' means 'what kind of', and here the 'vy' is plural, for the whole group. The original line uses 'invalidy', 'cripples', an insult Barinov uses a lot."),
    (4, None, "'You can't even run away!' 'Dazhe', 'even', goes right in front of what fails, here 'sbezhat', 'to run away'. 'Mozhete', 'you can', is the plural 'vy' form."),
    (5, None, "'Quickly, to my office.' Russian leaves out 'go' and gives only the direction. 'Ko mne' means 'to me', and 'k' becomes 'ko' before 'mne' so it is easier to say."),
    (6, None, "'Good afternoon, Viktor Petrovich.' In Russian, the respectful way to address someone is first name plus father's name, and this one is made from 'Pyotr', so it means 'son of Pyotr'."),
    (7, None, "'I am a major of the migration service.' In Russian, the 'of' shows in the endings: 'migratsionnaya sluzhba' becomes 'migratsionnoy sluzhby'."),
    (8, None, "'Can we go to your office?' 'Proyti' means 'to go through' or 'to step into', and it's the polite word for moving to another room: 'proydite, pozhaluysta', 'come in, please'."),
    (9, None, "'Unfortunately, I cannot.' 'K sozhaleniyu' is literally 'to regret', and it's the polite way to soften a no. 'Ne mogu', 'I can't', is a whole answer by itself."),
    (10, None, "'I need to cook for the guests.' Russian says 'mne nuzhno', literally 'to me it is needed'. 'Dlya', 'for', changes 'gosti', 'guests', to 'gostey'."),
    (11, None, "'Alright, I will wait for you here.' 'Podozhdu' means 'I'll wait', from 'zhdat', 'to wait'. The 'po-' makes it a wait for a while, and the major is in no hurry."),
]
