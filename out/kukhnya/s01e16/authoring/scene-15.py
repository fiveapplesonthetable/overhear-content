# Authoring module for kukhnya-s01e16-scene-15.
ID = 'kukhnya-s01e16-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 15
TITLE = "Освобождение Феди  (Fedya's Release)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'fedya': 'Федя', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Focused on fedya's release, Fedya is released from the fridge after the inspection. Max continues to obsess over the pâté recipe. Let's listen closely to Chef Viktor and the staff's exchange in Russian first, and then walk through each line together."
OPENER = 'Now let us examine the conversation line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Fedya is released from the fridge after the inspection. Max continues to obsess over the pâté recipe. Next time you watch the episode, listen for the Russian expressions for 'to understand' and 'to add' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('fedya', 'Шеф, я понял.', 'Boss, I got it.', [(180, 'Шеф, я понял. Вы в паштет базилик добавили, да?')], ''),
    ('fedya', 'Вы добавили базилик, да?', 'You added basil, right?', [(180, 'Шеф, я понял. Вы в паштет базилик добавили, да?')], ''),
    ('inspector', 'Чист.', 'Clear.', [(181, 'Чист. Проверили.')], ''),
    ('inspector', 'Проверили.', 'Checked.', [(181, 'Чист. Проверили.')], ''),
    ('barinov', 'Я так и знал.', 'I knew it.', [(182, 'Я так и знал.')], ''),
    ('inspector', 'Виктор Петрович, ошибочка вышла.', 'Viktor Petrovich, a mistake happened.', [(183, 'Ну что же, Виктор Петрович, ошибочка вышла.')], ''),
    ('inspector', 'Мои люди проверили этого человека.', 'My people checked this person.', [(184, 'Оказывается, мои люди уже проверили этого человечка.')], ''),
    ('inspector', 'Абсолютно чист.', 'Completely clean.', [], ''),
    ('barinov', 'А я всегда знал.', 'And I always knew.', [], ''),
    ('barinov', 'Федя, ты как?', 'Fedya, how are you?', [(187, 'Федь, ты как? Нормально.')], ''),
    ('fedya', 'Нормально.', 'Fine.', [(187, 'Федь, ты как? Нормально.')], ''),
    ('fedya', 'Ты как меня вытащил?', 'How did you get me out?', [(188, 'Ты как меня оттуда вытащил?')], ''),
    ('fedya', 'Ключи только у шефа были.', 'Only the boss had keys.', [(189, 'Ключи же только у шефа были.')], ''),
    ('barinov', 'Пусть он так думает.', 'Let him think so.', [(190, 'Вот пусть он и дальше так думает.')], ''),
]
WALK = [
    (0, None, "'Boss, I got it.' Fedya eagerly reports back, showing that he comprehended the previous instructions."),
    (1, None, "'You added basil, right?' The cook asks for confirmation about a recipe detail, completely ignoring the tension of the raid."),
    (2, None, "'Clear.' The officer gives a crisp, one-word confirmation that the inspection revealed no problems."),
    (3, None, "'Checked.' Following up his previous statement, the official confirms that the examination is complete."),
    (4, None, "'I knew it.' Barinov smugly asserts that he was right all along, projecting total confidence."),
    (5, None, "'Viktor Petrovich, a mistake happened.' The disappointed guest admits that their raid was based on incorrect information."),
    (6, None, "'My people checked this person.' Explaining the process, the officer confirms that his team looked into the worker's background."),
    (7, None, "'Completely clean.' Reassuring the chef, the official declares the employee entirely free of any legal issues."),
    (8, None, "'And I always knew.' The boss repeats his smug claim of prior knowledge, rubbing his victory in the officer's face."),
    (9, None, "'Fedya, how are you?' Barinov checks in on his employee, asking about his well-being after the stressful event."),
    (10, None, "'Fine.' Fedya gives a short, casual response, brushing off the intensity of the situation."),
    (11, None, "'How did you get me out?' Puzzled by his sudden rescue, the cook asks his boss to explain the trick."),
    (12, None, "'Only the boss had keys.' The worker points out a logical flaw in the rescue, noting that access was restricted to one person."),
    (13, None, "'Let him think so.' Barinov slyly suggests allowing the inspector to believe a false version of events."),
]
