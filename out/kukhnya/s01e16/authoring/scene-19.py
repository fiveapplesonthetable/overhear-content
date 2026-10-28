# Authoring module for kukhnya-s01e16-scene-19.
ID = 'kukhnya-s01e16-scene-19'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 19
TITLE = 'Проверка документов  (Document Check)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'fedya': 'Федя', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The inspector has seen through Fedya, and now he asks for the one paper a guest would never need: a work permit. Fedya has no good answer, and every reply makes things worse.'
OPENER = "Let's go through it line by line."
TRANSITION = 'Now the whole conversation once more, from start to finish.'
OUTRO = "The inspector politely marches Fedya off to see the chef. 'Proydyomte' is the formal 'come with me', the word officials use when you have no choice. See you next time!"
CLOSING = ('fedya', 'Всем пока!')
STORY = [
    ('inspector', 'Где ваше разрешение на работу?', 'Where is your work permit?', [], ''),
    ('fedya', 'Оно у меня дома.', "It's at home.", [], ''),
    ('inspector', 'Откуда вы приехали?', 'Where have you come from?', [], ''),
    ('fedya', 'Из Молдовы.', 'From Moldova.', [], ''),
    ('inspector', 'Значит, разрешение вам нужно.', 'So you do need a permit.', [], ''),
    ('fedya', 'Я просто не успел его сделать.', "I just haven't had time to get it done.", [], ''),
    ('inspector', 'Это большая проблема для ресторана.', 'This is a big problem for the restaurant.', [], ''),
    ('fedya', 'Я лучший повар на этой кухне!', "I'm the best cook in this kitchen!", [], ''),
    ('inspector', 'Закон один для всех.', 'The law is the same for everyone.', [], ''),
    ('fedya', 'Что вы теперь будете делать?', 'What are you going to do now?', [], ''),
    ('inspector', 'Мне нужно поговорить с вашим начальником.', 'I need to talk to your boss.', [], ''),
    ('inspector', 'Вставайте. Пройдёмте.', 'Get up. Come with me.', [(270, 'Пройдемте.')], ''),
    ('fedya', 'Ну, пойдёмте.', "Well, let's go.", [], ''),
]
WALK = [
    (0, None, "'Where is your work permit?' 'Razreshenie', 'permit', comes from 'razreshit', 'to allow'. 'Na rabotu', literally 'onto work', is the 'for work' part."),
    (1, None, "'It's at home.' 'U menya doma' is literally 'at me at home', the usual way to say 'at my place'. 'Ono', 'it', is neuter because 'razreshenie' is neuter."),
    (2, None, "'Where have you come from?' 'Otkuda' means 'from where', a single word. 'Priekhali' means 'came' by transport, not on foot, and it's what Russians ask a newcomer."),
    (3, None, "'From Moldova.' After 'iz', 'from', the country takes a new ending: 'Moldova' becomes 'Moldovy'. Many Russians still say the older name 'Moldaviya'."),
    (4, None, "'So you do need a permit.' 'Znachit', literally 'it means', is the everyday 'so' when you draw a conclusion. 'Vam nuzhno' is literally 'to you it is needed'."),
    (5, None, "'I just haven't had time to get it done.' 'Ne uspel' means 'didn't manage in time', from 'uspet', 'to make it in time'. English has no single word for it."),
    (6, None, "'This is a big problem for the restaurant.' 'Problema' is feminine, so 'bolshaya', 'big', ends in '-aya'. 'Dlya restorana', 'for the restaurant', adds '-a' after 'dlya', 'for'."),
    (7, None, "'I'm the best cook in this kitchen!' 'Luchshiy' means 'the best', a word that looks nothing like 'khoroshiy', 'good'. Russians work 'na kukhne', literally 'on the kitchen'."),
    (8, None, "'The law is the same for everyone.' 'Zakon odin' is literally 'the law is one', and it sounds like a saying. 'Dlya vsekh' means 'for all'."),
    (9, None, "'What are you going to do now?' 'Budete delat' is 'will be doing': the future of 'byt', 'to be', plus the plain verb. 'Teper' means 'now', in the sense of 'from now on'."),
    (10, None, "'I need to talk to your boss.' 'Mne nuzhno', 'to me it is needed', is the usual 'I need to'. 'Pogovorit' means 'to have a talk', and 'nachalnik' means 'boss'."),
    (11, None, "'Get up. Come with me.' 'Vstavayte', 'get up', speaks to him as 'vy'. 'Proydyomte' is literally 'let's go through', with the polite '-te' on the end, and it is what police and officials say."),
    (12, None, "'Well, let's go.' 'Poydyomte' is the ordinary 'let's go' with the polite '-te' ending, so Fedya stays formal with the officer. 'Nu', 'well', makes it sound like giving in."),
]
