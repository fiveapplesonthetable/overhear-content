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
    (0, None, "'Where is your fire extinguisher?' The official demands to see the safety equipment once again."),
    (1, None, "'It was hanging here last time.' Vika sounds confused, pointing out where the item used to be."),
    (2, None, "'Are you laughing at me?' Frustrated by the disappearing equipment, the inspector feels he is being mocked."),
    (3, None, "'This one is not suitable.' He rejects the replacement they offer as completely inadequate."),
    (4, None, "'Here is a normal fire extinguisher.' Vika presents another option, hoping this one meets the standard."),
    (5, None, "'And where is its seal?' The official immediately finds another flaw, pointing out a missing safety marker."),
    (6, None, "'Good afternoon.' Nagiyev enters the scene smoothly, offering a polite daytime greeting."),
    (7, None, "'May I know one thing?' He asks for permission to bring up a specific question."),
    (8, None, "'Why do you have such an interest in the restaurant?' Nagiyev probes the official's unusually intense focus on their establishment."),
    (9, None, "'We are fighting with bad management.' The official justifies his harshness by claiming to crusade against poor leadership."),
    (10, None, "'There was a call to my boss.' He reveals that a complaint from higher up triggered the strict review."),
    (11, None, "'From the neighboring restaurant.' The source of the trouble is finally unmasked as a rival business."),
    (12, None, "'Everything is clear.' Nagiyev quickly connects the dots, understanding the true motive behind the harassment."),
    (13, None, "'Well then, until tomorrow.' The official leaves with a threatening promise to return the next day."),
]
