# Authoring module for kukhnya-s06e02-scene-14.
ID = 'kukhnya-s06e02-scene-14'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 2
SCENE = 14
TITLE = 'Ложь для мамы и подготовка к съёмкам  (A Lie for Mom and Preparing for the Shoot)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.02'
SOURCE_FILE = 'sources/kukhnya/s06/e02.ru.srt'
INTRO = 'On his day off, Lyova tells his mother on the phone that he was called in for an urgent banquet so he can secretly go rollerblading with Gulya, while the kitchen prepares for the TV shoot.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "With the dining room locked for the supposed television crew, Nikita steps up to the bar to help Denis's romantic troubles. See you next time!"
CLOSING = ('senya', 'Увидимся!')
STORY = [
    ('lyova', 'Да, мама, я не дома.', 'Yes, Mom, I am not at home.', [(234, 'Да, мам'), (235, 'Нет, не дома')], 'adapted'),
    ('lyova', 'Вызвали на работу, срочный банкет.', 'They called me in to work, an urgent banquet.', [(236, 'Вызвали на работу. Срочный банкет')], 'exact'),
    ('lyova', 'Все, пока, мама.', 'Alright, bye, Mom.', [(237, 'Все, пока')], 'adapted'),
    ('lyova', 'Ну, ты готова кататься?', 'Well, are you ready to skate?', [(240, 'Ну, я готова')], 'adapted'),
    ('lyova', 'Это оказывается сложнее, чем я думал.', 'This turns out to be harder than I thought.', [(241, 'это оказывается сложнее, чем я думал')], 'exact'),
    ('senya', 'Как жизнь, Денис?', 'How is life, Denis?', [(242, 'Как жизнь?')], 'adapted'),
    ('denis', 'Не удалась жизнь.', 'Life did not work out.', [(242, 'Не удалась')], 'adapted'),
    ('denis', 'А где все гости?', 'And where are all the guests?', [(244, 'А где все?')], 'adapted'),
    ('denis', 'С похмелья работать некому?', 'Is there nobody to work because of a hangover?', [(244, 'С похмелья работать некому?')], 'exact'),
    ('senya', 'Нет, ресторан закрыли, шефа будут снимать.', 'No, they closed the restaurant, they are going to film the chef.', [(245, 'Нет, ресторан закрыли')], 'adapted'),
    ('senya', 'Мы вот овощи отобрали самые красивые.', 'We selected the most beautiful vegetables here.', [(247, 'вот овощи отобрала самые')], 'adapted'),
    ('denis', 'Хорошо, понял.', 'Alright, got it.', [(248, 'Хорошо')], 'adapted'),
]
WALK = [
    (0, None, "'Yes, Mom, I am not at home.' Explaining that Mom he is not at home lays the cards on the table for Denis."),
    (1, None, "'They called me in to work, an urgent banquet.' Lyova explains that they called him in to work an urgent banquet, keeping his voice calm and direct."),
    (2, None, "'Alright, bye, Mom.' With the truth and banquet in play, Lyova keeps this short reply brisk and direct."),
    (3, None, '\'Well, are you ready to skate?\' Checking whether Denis ready to skate cuts straight through the tension between Lyova and Denis. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, '\'This turns out to be harder than I thought.\' Even though this turns out to be harder than he thought, Lyova keeps a steady face in front of Denis. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (5, None, "'How is life, Denis?' Here asking how life is shows Senya looking for the real truth."),
    (6, None, "'Life did not work out.' Saying that life did not work out is how Denis sets the tone with Lyova."),
    (7, None, '\'And where are all the guests?\' Asking where all the guests are cuts straight through the tension between Denis and Lyova. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'Is there nobody to work because of a hangover?' Checking whether there nobody to work because of a hangover is how Denis puts Lyova on the spot."),
    (9, None, "'No, they closed the restaurant, they are going to film the chef.' Senya tells Denis that they closed the restaurant they are going to film without dressing it up."),
    (10, None, "'We selected the most beautiful vegetables here.' With the restaurant and phone in play, Senya keeps this short reply brisk and direct."),
    (11, None, "'Alright, got it.' Mentioning that Alright got it moves the talk in a new direction."),
]
