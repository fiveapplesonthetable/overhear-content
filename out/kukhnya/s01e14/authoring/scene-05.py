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
INTRO = 'Barinov has arrived, but he has had too much to drink. Vika catches him in the corridor and refuses to let him near the guests. Listen first.'
OPENER = 'Slowly, once more.'
TRANSITION = 'Here is the whole scene again.'
OUTRO = "Nobody manages to stop him, and he heads for the bar. Two set phrases from this one: 'in such a state', and 'to marry'. Bye for now."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('vika', 'Шеф, зачем ты так сильно напился?', 'Chef, why did you get so drunk?', [(50, 'Ты зачем так нажирался?')], ''),
    ('barinov', 'Я не напился, а выпил немного аперитива.', 'I did not get drunk, I had a little aperitif.', [(51, 'Не нажался,'), (52, 'а употребил некоторое количество дежестива в качестве аперитива.')], ''),
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
    (0, None, ["'Chef, why did you get so drunk?' Now we can break down the dialogue: ", ('vika', 'напился'), " builds on a word for drinking, adding pieces to mean 'drank himself full'. ", ('vika', 'зачем'), " means 'what for'."]),
    (1, None, ["'I did not get drunk, I had a little aperitif.' Now let's consider the dialogue: ", ('barinov', 'не'), ' and ', ('barinov', 'а'), " pair up to mean 'not this, but that'. After ", ('barinov', 'немного'), ", meaning 'a little', the drink changes its ending to ", ('barinov', 'аперитива'), '.']),
    (2, None, ["'You can barely stand on your feet.' We will inspect the dialogue: ", ('vika', 'еле'), " means 'barely'. The term for feet becomes ", ('vika', 'на'), ('vika', 'своих'), ('vika', 'ногах'), ", with a plural ending for 'on' and 'in'."]),
    (3, None, ["'The face of the restaurant arrived, I am ready to welcome guests!' Let us examine the words: ", ('barinov', 'прибыло'), " is an official word for 'arrived' used on station announcements, making him sound grand. It has a neuter ending to match ", ('barinov', 'Лицо'), ", meaning 'face'."]),
    (4, None, ["'In this state you will not go out to the guests!' We can examine the sentence: ", ('vika', 'В'), ('vika', 'таком'), ('vika', 'состоянии'), " is the set phrase 'in such a state'. ", ('vika', 'выйдешь'), " starts with a part meaning 'out', making it 'you will go out'."]),
    (5, None, ["'And you will never get married.' He plays on her wording: ", ('barinov', 'замуж'), " paired with the action means 'go out behind a husband', which is how a woman marries. ", ('barinov', 'никогда'), ('barinov', 'не'), ' keeps both negatives.']),
    (6, None, ["'Stop grabbing me so roughly.' We can focus on the dialogue: ", ('vika', 'Хватит'), ", meaning 'enough', and ", ('vika', 'хвататься'), ", meaning 'to grab hold', share a sound, making the line nearly rhyme. You grab hold by someone, leading to ", ('vika', 'за'), ('vika', 'меня'), '.']),
    (7, None, ["'I must personally check our restaurant.' Now we can inspect this part: ", ('barinov', 'лично'), ", meaning 'personally', comes from the term for 'face' we just heard. ", ('barinov', 'должен'), ' combined with ', ('barinov', 'проверить'), " creates 'must check'."]),
    (8, None, ["'Do something with this drunken monster!' She says ", ('vika', 'Сделайте'), ' with a plural ending, as she is asking everyone around her. ', ('vika', 'что'), '-', ('vika', 'нибудь'), " means 'something' or 'anything'."]),
    (9, None, ["'I had a very good idea.' This reads as 'at me appeared a very good idea'. ", ('barinov', 'появилась'), ", meaning 'appeared', has a feminine ending to match ", ('barinov', 'идея'), '.']),
    (10, None, ["'What other idea can there be now?' Now let's look at the dialogue: ", ('vika', 'Какая'), ('vika', 'ещё'), " reads as 'which else', the impatient 'what other'. The first word is feminine again to match the idea."]),
    (11, None, ["'Let us all together inspect the bar!' Let's inspect this line: ", ('barinov', 'пойдёмте'), " is 'let us go', and its ending makes it an invitation to a group. ", ('barinov', 'проинспектируем'), " is the English 'inspect' with a prefix and a 'we' ending."]),
]
