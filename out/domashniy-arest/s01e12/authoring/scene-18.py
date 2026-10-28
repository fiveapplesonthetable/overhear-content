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
    (0, None, "'Attention, everyone remain in your places!' Major Lavrov takes control of the warehouse floor with the crisp authority of a career intelligence officer."),
    (1, None, "'The FSB special group is operating, drop weapons!' Why is he shouting this again? Because a second armed group—the governor's local police—has just walked in on his raid."),
    (2, None, "'Calmly, major, regional police are operating here.' Viktor Stepanovich strolls in wearing a general's uniform, trying to pull rank on the federal agents."),
    (3, None, "'Who is your chief commander here?' Lavrov isn't intimidated by local badges; he demands to know who is running this rival squad."),
    (4, None, "'Major General of Police Viktor Stepanovich is speaking.' Announcing himself in the third person with his full title is the governor's way of flexing every bit of muscle he has."),
    (5, None, "'We are conducting a secret operation here.' Federal security doesn't report to regional governors, and Lavrov makes that boundary clear."),
    (6, None, '\'You must not act without my knowledge.\' "Bez moyego vedoma" means "without my knowledge"—the phrase of a local tsar who thinks nothing in the province should happen behind his back.'),
    (7, None, "'We have been catching dangerous corrupt officials for six months.' Half a year of wiretaps and stakeouts went into this sting, and Lavrov refuses to let the governor spoil it."),
    (8, None, "'Let us calmly resolve this complex problem.' Realizing he cannot bully the FSB out of the building, Stepanovich switches to his smooth dealmaker voice."),
    (9, None, "'Do you have specific proposals?' Even a federal major knows when to listen to a political compromise."),
    (10, None, "'This will be our shared joint operation.' Here is the governor's clever pivot: instead of going down with Osipenko, he claims credit for catching him alongside the FSB."),
    (11, None, "'Good, we are documenting the arrest together.' Lavrov agrees to share the paperwork—for now—letting the governor think he has wiggled off the hook."),
]
