# Authoring module for kukhnya-s06e04-scene-09.
ID = 'kukhnya-s06e04-scene-09'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 9
TITLE = 'Гулю принимают за домработницу  (Gulya Is Mistaken for a Housekeeper)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'gulya': 'Гуля', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "While Katya and Olivier laugh over how easily her parents believed the prank, Lyova's mother returns home while Lyova is at the restaurant and assumes Gulya is a housekeeper Lyova hired for her."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Afraid to offend Lyova's mother before Lyova gets back, polite Gulya plays along with every household chore Vera Ivanovna gives her. Until next time!"
CLOSING = ('gulya', 'Всего хорошего!')
STORY = [
    ('guest', 'Ну что, они поверили?', 'Well, did they believe it?', [(141, 'Ну что, они поверили?')], 'exact'),
    ('gulya', 'Я просто сказала им то, что они хотели услышать.', 'I simply told them what they wanted to hear.', [(142, 'Я просто сказала им то, что они хотели услышать')], 'exact'),
    ('katya', 'Через полчаса спускайся вниз вершить судьбу ресторана.', 'In half an hour come downstairs to decide the fate of the restaurant.', [(143, 'Через полчаса спускайся вниз'), (143, 'судьбу ресторана')], 'adapted'),
    ('gulya', 'Лёва, а может, мне тогда уйти?', 'Lyova, maybe I should leave then?', [(146, 'Лёва, а может мне тогда уйти?')], 'exact'),
    ('gulya', 'Ладно, подожду, постарайся побыстрее.', 'Fine, I will wait, try to make it fast.', [(147, 'Ладно, подожду'), (148, 'Постарайся побыстрее')], 'adapted'),
    ('guest', 'Здравствуйте, а вы кто?', 'Hello, and who are you?', [(152, 'Здравствуйте'), (153, 'А вы кто?')], 'adapted'),
    ('guest', 'А где наш Лёва?', 'And where is our Lyova?', [(154, 'А где Лев?')], 'adapted'),
    ('gulya', 'Его срочно на работу вызвали, а меня Гуля зовут.', 'They called him in to work urgently, and my name is Gulya.', [(155, 'Его срочно на работу вызвали'), (156, 'А меня'), (156, 'зовут')], 'adapted'),
    ('gulya', 'Пойдемте на кухню, там плов почти уже готов.', "Let's go to the kitchen, the pilaf is almost ready in there.", [(157, 'Пойдемте на кухню. Там плов почти уже готов')], 'exact'),
    ('gulya', 'Я сегодня утром сказала, что мне нужна помощница.', 'This morning I mentioned that I needed a helper.', [(158, 'Я сегодня утром'), (158, 'что мне нужна помощница')], 'adapted'),
    ('guest', 'А он это принял буквально и нанял домработницу!', 'And he took it literally and hired a housekeeper!', [(159, 'А он это принял буквально и нанял домработницу')], 'exact'),
    ('guest', 'Ты должна радоваться, что у тебя такой заботливый сын.', 'You should be glad that you have such a caring son.', [(160, 'ты должна радоваться, что у тебя такой заботливый сын')], 'exact'),
]
WALK = [
    (0, None, '\'Well, did they believe it?\' Asking whether they believe it cuts straight through the tension between the guest and Gulya. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'I simply told them what they wanted to hear.' Since she simply told them what they wanted to hear, Gulya does not waste words on excuses."),
    (2, None, "'In half an hour come downstairs to decide the fate of the restaurant.' With the restaurant and apartment in play, Katya keeps this short reply brisk and direct."),
    (3, None, '\'Lyova, maybe I should leave then?\' Wondering if maybe she should leave then shows Gulya caught off guard. In Russian, she does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (4, None, "'Fine, I will wait, try to make it fast.' Because fine she will wait try to make it fast, Gulya treats the matter as settled."),
    (5, None, '\'Hello, and who are you?\' Asking who Gulya is is how the guest puts Gulya on the spot. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (6, None, '\'And where is our Lyova?\' Wondering where their Lyova is is how the guest puts Gulya on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (7, None, "'They called him in to work urgently, and my name is Gulya.' Claiming that they called him in to work urgently and her name is Gulya sounds confident, even if the guest has doubts."),
    (8, None, "'Let's go to the kitchen, the pilaf is almost ready in there.' Gulya reminds the guest that they should go to the kitchen the pilaf is almost ready in there before the moment passes."),
    (9, None, "'This morning I mentioned that I needed a helper.' Gulya explains that this morning she mentioned that she needed a helper, keeping her voice calm and direct."),
    (10, None, "'And he took it literally and hired a housekeeper!' Declaring that he took it literally and hired a housekeeper brings the guest's temper right to the surface."),
    (11, None, '\'You should be glad that you have such a caring son.\' Noting that Gulya should be glad that Gulya has such a caring son keeps the guest\'s side of the story simple and clear. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
]
