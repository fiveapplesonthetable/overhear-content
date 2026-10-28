# Authoring module for kukhnya-s01e16-scene-02.
ID = 'kukhnya-s01e16-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 2
TITLE = 'Случайный звонок  (An Accidental Call)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'inspector': 'Инспектор', 'nagiyev': 'Нагиев', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = 'The fire inspector continues his strict check and rejects several fire extinguishers. The restaurant owner, Dmitry, arrives and demands to know the real reason behind this sudden and aggressive inspection. Let us listen to their conversation in Russian first.'
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The fire inspector returns repeatedly to find new faults with the extinguishers until Chef Barinov learns that the rival restaurant next door called in the tip. Next time you watch the episode, listen for the Russian expressions for 'fire extinguisher' and 'to hang' — you will catch every word right away. See you next time!"
CLOSING = ('inspector', 'Пока!')
STORY = [
    ('inspector', 'Где ваш огнетушитель?', 'Where is your fire extinguisher?', [(10, 'А где огнетушитель?')], ''),
    ('vika', 'Он висел здесь в прошлый раз.', 'It was hanging here last time.', [(11, 'Он же висел у вас в прошлый раз.')], ''),
    ('inspector', 'Вы что, смеётесь надо мной?', 'Are you laughing at me?', [(12, 'Вы что, издеваетесь, что ли?')], ''),
    ('inspector', 'Этот не подходит.', 'This one is not suitable.', [(14, 'Не годим.')], ''),
    ('vika', 'Вот нормальный огнетушитель.', 'Here is a normal fire extinguisher.', [(15, 'Браку! Ну вот, нормальный огнетушитель.')], ''),
    ('inspector', 'А где его пломба?', 'And where is its seal?', [(16, 'А пломба где?')], ''),
    ('nagiyev', 'Добрый день.', 'Good afternoon.', [], ''),
    ('nagiyev', 'Можно узнать одну вещь?', 'May I know one thing?', [(19, 'А можно узнать, чем вызван столь бурный интерес к пожарной безопасности моего')], ''),
    ('nagiyev', 'Почему у вас такой интерес к ресторану?', 'Why do you have such an interest in the restaurant?', [(20, 'ресторана? Можно.')], ''),
    ('inspector', 'Мы боремся с плохим руководством.', 'We are fighting with bad management.', [(21, 'Интерес вызван борьбой с халатностью руководства,')], ''),
    ('inspector', 'Был звонок моему начальнику.', 'There was a call to my boss.', [(22, 'а также с безобразным состоянием пожарной техники и звонком моему')], ''),
    ('inspector', 'Из соседнего ресторана.', 'From the neighboring restaurant.', [(23, 'начальнику из соседнего ресторана.')], ''),
    ('nagiyev', 'Всё понятно.', 'Everything is clear.', [(25, 'Понятно.')], ''),
    ('inspector', 'Ну что, до завтра.', 'Well then, until tomorrow.', [(26, 'Ну что, до завтра.')], ''),
]
WALK = [
    (0, None, "'Where is your fire extinguisher?' Russian omits the present-tense verb 'to be' here, linking 'where' directly with 'fire extinguisher', combining 'where' with 'fire extinguisher'."),
    (1, None, "'It was hanging here last time.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (2, None, "'Are you laughing at me?' the inspector chooses the action verb meaning 'are laughing' for the ongoing action, followed by 'it is necessary'."),
    (3, None, "'This one is not suitable.' the inspector delivers a punchy conversational reaction built around the Russian word meaning 'is coming up'."),
    (4, None, "'Here is a normal fire extinguisher.' Russian omits the present-tense verb 'to be' here, linking 'decent' directly with 'fire extinguisher', combining 'decent' with 'fire extinguisher'."),
    (5, None, "'And where is its seal?' Russian omits the present-tense verb 'to be', connecting 'and' directly with 'seal'."),
    (6, None, "'Good afternoon.' Russian omits the present-tense verb 'to be' here, linking 'good' directly with 'day', combining 'good' with 'day'."),
    (7, None, "'May I know one thing?' Russian forms this yes-or-no question without a question word, relying on rising pitch on 'thing'."),
    (8, None, "'Why do you have such an interest in the restaurant?' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (9, None, "'We are fighting with bad management.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (10, None, "'There was a call to my boss.' Notice how naturally this everyday Russian phrase expresses the speaker's point."),
    (11, None, "'From the neighboring restaurant.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'neighboring' straight to 'restaurant'. Dmitry answers straight away."),
    (12, None, "'Everything is clear.' Nagiyev delivers a punchy one-word reaction built around the Russian word meaning 'clear'."),
    (13, None, "'Well then, until tomorrow.' the inspector delivers a punchy conversational reaction built around the Russian word meaning 'tomorrow'."),
]
