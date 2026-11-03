# Authoring module for kukhnya-s01e06-scene-11.
ID = 'kukhnya-s01e06-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 11
TITLE = "Визит инспектора  (The Inspector's Visit)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "The sanitary inspector has finished with the dining room at Claude Monet, and Vika, the manager, walks him through to the kitchen. She is polite and confident. He is polite and very, very thorough. It's in Russian first, with a lot of formal language."
OPENER = 'Let\'s go back through it. Both of them use the polite "vy", and both talk like an official letter.'
TRANSITION = 'And now the tour from the start, without stopping.'
OUTRO = "After all the shouting at the pass, Vika's poised, formal welcome at the kitchen doors sets up a tense clash with a very thorough inspector. See you next time."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Проходите, пожалуйста, вот и наша кухня.', 'Come in, please, here is our kitchen.', [(157, 'А вот и наша кухня'), (158, 'Прошу вас')], ''),
    ('inspector', 'По залу у меня претензий нет.', 'Regarding the hall, I have no complaints.', [(158, 'по залу у меня никаких претензий нет')], ''),
    ('vika', 'Мы строго следим за чистотой везде.', 'We strictly monitor cleanliness everywhere.', [], ''),
    ('inspector', 'Теперь посмотрим на вашу кухню внимательно.', "Now let's look at your kitchen carefully.", [(159, 'Посмотрим вашу кухню')], ''),
    ('vika', 'У нас здесь работают лучшие повара.', 'We have the best cooks working here.', [], ''),
    ('inspector', 'Меня интересуют только санитарные правила.', 'I am interested only in sanitary rules.', [], ''),
    ('vika', 'Все сотрудники носят чистую форму.', 'All employees wear a clean uniform.', [], ''),
    ('inspector', 'Я сам проверю каждое рабочее место.', 'I myself will check every workstation.', [], ''),
    ('vika', 'Наш шеф-повар лично всё контролирует.', 'Our head chef personally oversees everything.', [], ''),
    ('inspector', 'На кухне нельзя нарушать правила.', 'In the kitchen one must not violate rules.', [], ''),
    ('vika', 'Вы можете увидеть всё сами.', 'You can see everything yourself.', [], ''),
    ('inspector', 'Тогда начинаем полную санитарную проверку.', 'Then we begin a full sanitary inspection.', [], ''),
    ('vika', 'Добро пожаловать на нашу кухню!', 'Welcome to our kitchen!', [], ''),
]
WALK = [
    (0, None, ["'Come in, please, here is our kitchen.' Let's focus on the word ", ('vika', 'Проходите'), ", which means 'come in', extending a formal invitation to step inside."]),
    (1, None, ["'Regarding the hall, I have no complaints.' He says, 'Regarding the hall, I have no complaints.' In this sentence, we hear ", ('inspector', 'претензий'), ", meaning 'complaints', showing that he is satisfied so far."]),
    (2, None, ["'We strictly monitor cleanliness everywhere.' She tells him, 'We strictly monitor cleanliness everywhere.' Pay attention to ", ('vika', 'чистотой'), ", which means 'cleanliness', an important focus in any restaurant."]),
    (3, None, ["'Now let's look at your kitchen carefully.' Here we can clearly notice ", ('inspector', 'внимательно'), ", meaning 'carefully', signaling that he will be very thorough."]),
    (4, None, ["'We have the best cooks working here.' To defend her team, she notes, 'We have the best cooks working here.' It is worth highlighting ", ('vika', 'лучшие'), ", meaning 'the best', to emphasize the quality."]),
    (5, None, ["'I am interested only in sanitary rules.' Let us look closely at ", ('inspector', 'только'), ", meaning 'only', showing his narrow and strict focus."]),
    (6, None, ["'All employees wear a clean uniform.' She continues, 'All employees wear a clean uniform.' This formal phrase features ", ('vika', 'сотрудники'), ", which translates to 'employees' or 'staff members'."]),
    (7, None, ["'I myself will check every workstation.' Note the use of the word ", ('inspector', 'каждое'), ", meaning 'every', showing that no corner will be missed."]),
    (8, None, ["'Our head chef personally oversees everything.' She assures him, 'Our head chef personally oversees everything.' Listen for the word ", ('vika', 'лично'), ", which translates to 'personally', emphasizing his direct involvement."]),
    (9, None, ["'In the kitchen one must not violate rules.' This strict sentence includes ", ('inspector', 'нельзя'), ", which is a strong way to say 'must not'."]),
    (10, None, ["'You can see everything yourself.' She invites him, 'You can see everything yourself.' The speaker is using ", ('vika', 'сами'), ", meaning 'yourself', encouraging him to look around personally."]),
    (11, None, ["'Then we begin a full sanitary inspection.' We can point out the word ", ('inspector', 'полную'), ", meaning 'full' or 'complete', reiterating his thoroughness."]),
    (12, None, ["'Welcome to our kitchen!' To conclude the exchange, 'Welcome to our kitchen!' Finally, she warmly says ", ('vika', 'Добро'), ", which helps form the standard way to say 'welcome'."]),
]
