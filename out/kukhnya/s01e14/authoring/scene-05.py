# Authoring module for kukhnya-s01e14-scene-05.
ID = 'kukhnya-s01e14-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 5
TITLE = 'Пьяный шеф  (The Drunk Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'In the corridor of Claude Monet, Victoria intercepts a heavily intoxicated Chef Barinov. Furious at his unprofessional state, she explicitly forbids him from entering the dining room, but the drunk chef stubbornly insists on conducting an inspection of the bar. Let us listen to their argument in Russian first.'
OPENER = "Now let us examine Victoria and the chef's argument line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Despite Victoria's desperate attempts to hide the drunken chef from the VIP guests, Barinov stumbles off toward the bar, determined to cause more chaos. Next time you watch the episode, listen for the Russian expressions for 'what for' and 'strongly' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Шеф, зачем ты так сильно напился?', 'Chef, why did you get so drunk?', [(50, 'Ты зачем так нажирался?')], ''),
    ('barinov', 'Я не напился, а выпил немного аперитива.', 'I am not drunk, but drank a little aperitif.', [(51, 'Не нажался,'), (52, 'а употребил некоторое количество дежестива в качестве аперитива.')], ''),
    ('vika', 'Ты еле стоишь на своих ногах.', 'You can barely stand on your feet.', [], ''),
    ('barinov', 'Лицо ресторана прибыло, я готов встречать гостей!', 'The face of the restaurant arrived, I am ready to welcome guests!', [(53, 'Короче говоря, лицо ресторана доставлено, я готов вам торговать.')], ''),
    ('vika', 'В таком состоянии ты к гостям не выйдешь!', 'In this state you will not go out to the guests!', [(54, 'Нет, в таком состоянии ты к гостям не выйдешь.')], ''),
    ('barinov', 'А ты замуж никогда не выйдешь.', 'And you will never get married.', [(55, 'А ты замуж не выйдешь,')], ''),
    ('vika', 'Хватит за меня так грубо хвататься.', 'Stop grabbing me so roughly.', [(55, 'если будешь так хвататься.')], ''),
    ('barinov', 'Я должен лично проверить наш ресторан.', 'I must personally check our restaurant.', [], ''),
    ('vika', 'Сделайте что-нибудь с этим пьяным чудовищем!', 'Do something with this drunken monster!', [(59, 'Пожалуйста, сделай что-нибудь с этим пьяным чудовищем,')], ''),
    ('barinov', 'У меня появилась очень хорошая идея.', 'I had a very good idea.', [(60, 'Шеф, ну, а у меня идея.'), (62, 'У меня лучшая идея.')], ''),
    ('vika', 'Какая ещё может быть идея сейчас?', 'What other idea can there be now?', [], ''),
    ('barinov', 'А пойдёмте все вместе проинспектируем бар!', 'Let us all together inspect the bar!', [(61, 'Пойдемте проинспектируем бар.'), (63, 'А пойдем-ка проинспектируем бар.')], ''),
]
WALK = [
    (0, None, "'Chef, why did you get so drunk?' Vika is furious with the Chef. She demands to know why he is heavily intoxicated."),
    (1, None, "'I am not drunk, but drank a little aperitif.' Barinov denies being drunk. He claims he only had a tiny bit of alcohol."),
    (2, None, "'You can barely stand on your feet.' Vika points out his obvious state. She notes he can barely stand upright."),
    (3, None, "'The face of the restaurant arrived, I am ready to welcome guests!' Barinov proudly announces his arrival. He claims he is ready to greet the guests."),
    (4, None, "'In this state you will not go out to the guests!' Vika absolutely forbids it. She tells him he cannot be seen like this."),
    (5, None, "'And you will never get married.' Barinov delivers a drunken insult. He makes a rude comment about her personal life."),
    (6, None, "'Stop grabbing me so roughly.' Vika tells him to let go of her. She demands he stop grabbing her arm."),
    (7, None, "'I must personally check our restaurant.' Barinov insists on doing his job. He slurs that he needs to inspect the restaurant."),
    (8, None, "'Do something with this drunken monster!' Vika calls for help. She begs someone to deal with the drunk Chef."),
    (9, None, "'I had a very good idea.' Barinov suddenly gets a bright idea. He thinks he has a great plan."),
    (10, None, "'What other idea can there be now?' Vika is highly skeptical. She wonders what kind of idea he could possibly have now."),
    (11, None, "'Let us all together inspect the bar!' Barinov announces his grand plan. He suggests they all go inspect the bar together."),
]
