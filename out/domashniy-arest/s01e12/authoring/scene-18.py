# Authoring module for domashniy-arest-s01e12-scene-18.
ID = 'domashniy-arest-s01e12-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 18
TITLE = 'Спецоперация на складе  (Special Operation at the Warehouse)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'governor': 'Губернатор', 'lavrov': 'Лавров'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "At an abandoned warehouse outside Sineozersk, FSB Major Lavrov and his tactical team launch a surprise raid. However, local police under Viktor Stepanovich also arrive on the scene, creating a tense standoff between agencies. Let's listen to how the two commanders negotiate in Russian."
OPENER = "Let's examine the dialogue sentence by sentence. Notice the formal vocabulary used in official negotiations."
TRANSITION = "Now let's listen to the entire exchange one more time at natural speed."
OUTRO = 'Major Lavrov and Viktor Stepanovich reach an understanding to conduct a joint operation. Great work practicing official conversational Russian! See you next time!'
CLOSING = ('lavrov', 'Пока!')
STORY = [
    ('lavrov', 'Внимание, всем оставаться на своих местах!', 'Attention, everyone remain in your places!', [(403, 'На полу работает СОБАР'), (408, 'Внимание')], 'tactical order'),
    ('lavrov', 'Работает специальная группа ФСБ, бросайте оружие!', 'The FSB special group is operating, drop weapons!', [(404, 'Работает ФСБ не стреляй'), (405, 'оружие на землю')], 'warning'),
    ('governor', 'Спокойно, майор, здесь работает областная полиция.', 'Calmly, major, regional police are operating here.', [(413, 'в моей области'), (415, 'Виктор Степанович')], 'intervening'),
    ('lavrov', 'Кто у вас здесь главный командир?', 'Who is your chief commander here?', [(410, 'Кто у вас там старше')], 'demanding identity'),
    ('governor', 'Говорит генерал-майор полиции Виктор Степанович.', 'Major General of Police Viktor Stepanovich is speaking.', [(402, 'товарищ генерал-майор'), (415, 'Виктор Степанович')], 'identifying himself'),
    ('lavrov', 'Мы проводим здесь секретную операцию.', 'We are conducting a secret operation here.', [(406, 'Это операция ФСБ')], 'justifying raid'),
    ('governor', 'Вы не должны действовать без моего ведома.', 'You must not act without my knowledge.', [(413, 'без моего ведома')], 'asserting jurisdiction'),
    ('lavrov', 'Мы ловим опасных коррупционеров уже полгода.', 'We have been catching dangerous corrupt officials for six months.', [(471, 'мы полгода всем этим занимались')], 'explaining mission'),
    ('governor', 'Давайте спокойно решим эту сложную проблему.', 'Let us calmly resolve this complex problem.', [(460, 'давайте решать как быть'), (461, 'Ситуация сложная')], 'de-escalating'),
    ('lavrov', 'У вас есть конкретные предложения?', 'Do you have specific proposals?', [(462, 'давайте так')], 'asking plan'),
    ('governor', 'Это будет наша общая совместная операция.', 'This will be our shared joint operation.', [(463, 'Это была ваша совместная операция')], 'proposing solution'),
    ('lavrov', 'Хорошо, оформляем задержание вместе.', 'Good, we are documenting the arrest together.', [(464, 'под четким контролем')], 'agreeing'),
]
WALK = [
    (0, None, "'Attention, everyone remain in your places!' Interjection demanding attention with an action verb expressing a command command."),
    (1, None, "'The FSB special group is operating, drop weapons!' Present tense verb governing a feminine subject followed by an command form."),
    (2, None, "'Calmly, major, regional police are operating here.' Adverb of manner with direct-address address and a feminine noun phrase."),
    (3, None, "'Who is your chief commander here?' Question word subject with a location pronoun and masculine nominal descriptive phrase."),
    (4, None, "'Major General of Police Viktor Stepanovich is speaking.' Third-person present verb with official rank and patronymic."),
    (5, None, "'We are conducting a secret operation here.' First-person plural verb governing an object-form feminine noun phrase."),
    (6, None, "'You must not act without my knowledge.' Plural modal adjective governing an ongoing-action form basic verb form and 'of'-form location phrase."),
    (7, None, "'We have been catching dangerous corrupt officials for six months.' Present ongoing-action form governing an animate object-form noun phrase."),
    (8, None, "'Let us calmly resolve this complex problem.' Hortative particle governing a future-tense form and object-form noun phrase."),
    (9, None, "'Do you have specific proposals?' Possessive construction governing plural subject-form subject."),
    (10, None, "'This will be our shared joint operation.' Demonstrative subject with future linking word governing a feminine descriptive phrase subject-form."),
    (11, None, "'Good, we are documenting the arrest together.' Affirmative adverb with a first-person plural verb and neuter direct object."),
]
