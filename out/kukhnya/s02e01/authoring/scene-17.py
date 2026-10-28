# Authoring module for kukhnya-s02e01-scene-17.
ID = 'kukhnya-s02e01-scene-17'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 17
TITLE = 'Секретный ингредиент  (The Secret Ingredient)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'The chef tastes the spiked tea and immediately recognizes the hidden alcohol. He praises his sous-chef for the clever trick while Kostya delivers a note to Victoria.'
OPENER = "Now let's go back through the exchange around The Secret Ingredient line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The kitchen staff successfully manages the boss's temper, allowing the restaurant service to continue smoothly without any further screaming. Next time you watch the episode, listen for the Russian expressions for 'excellent' and 'sencha' — you will catch every word right away. See you next time!"
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Отличный чай!', 'Excellent tea!', [(233, 'Чай. Чай.')], ''),
    ('barinov', 'А что это за чай-то?', 'And what kind of tea is this?', [(234, 'А что за чай-то')], ''),
    ('lyova', 'Это Сенча.', 'This is Sencha.', [(235, 'Сенча')], ''),
    ('barinov', 'Молодцы, действуем по нашему плану.', 'Good job, we are acting according to our plan.', [(236, 'Молодцы. Действуем по плану.')], ''),
    ('lyova', 'Давай, Костян, давай, давай!', 'Come on, Kostyan, come on, come on!', [(237, 'Давай, Костян, давай, давай, давай.')], ''),
    ('kostya', 'Всё понятно.', 'Everything is understood.', [(238, 'Понятно.')], ''),
    ('lyova', 'Займись седьмым столиком, пожалуйста.', 'Take care of the seventh table, please.', [(238, 'Займи седьмым столиком, пожалуйста.')], ''),
    ('kostya', 'Виктория Сергеевна, это записка вам.', 'Victoria Sergeyevna, this is a note for you.', [(239, 'Виктория Сергеевна, записка вам.')], ''),
    ('barinov', 'Этот чай очень хорошо успокаивает.', 'This tea calms very well.', [], ''),
    ('lyova', 'Я рад, что вам понравилось.', 'I am glad that you liked it.', [], ''),
    ('barinov', 'Заварите мне ещё одну чашку.', 'Brew me one more cup.', [], ''),
    ('lyova', 'Сейчас всё сделаем.', 'We will do everything now.', [], ''),
    ('kostya', 'А от кого эта записка?', 'And from whom is this note?', [], ''),
    ('lyova', 'Просто передай её Виктории Сергеевне.', 'Just pass it to Victoria Sergeyevna.', [], ''),
]
WALK = [
    (0, None, "'Excellent tea!' Tasting the cognac hidden in the cup, Barinov declares the tea excellent."),
    (1, None, "'And what kind of tea is this?' Playing along for the cameras, Viktor asks what variety of tea it is. Then Lyova responds."),
    (2, None, "'This is Sencha.' Lyova keeps a straight face and calls it 'Sencha' green tea."),
    (3, None, "'Good job, we are acting according to our plan.' Cheered up immediately, Viktor praises the team and says they will stick to this plan."),
    (4, None, "'Come on, Kostyan, come on, come on!' Meanwhile, Lyova urges Kostya to hurry up with Max's errand."),
    (5, None, "'Everything is understood.' Kostya nods that he knows exactly what to do."),
    (6, None, "'Take care of the seventh table, please.' To cover the handoff, Lyova tells Kostya to go serve table seven."),
    (7, None, "'Victoria Sergeyevna, this is a note for you.' In the dining room, Kostya hands Max's dramatic note to Victoria."),
    (8, None, "'This tea calms very well.' Back in the kitchen, Viktor jokes that this 'tea' is wonderfully soothing."),
    (9, None, "'I am glad that you liked it.' Lyova smiles and says he is glad the chef liked the brew."),
    (10, None, "'Brew me one more cup.' Viktor promptly orders another cup of the spiked tea."),
    (11, None, "'We will do everything now.' Lyova promises to fix a fresh cup right away."),
    (12, None, "'And from whom is this note?' Earlier at the bar, Kostya asks who the mysterious note is from."),
    (13, None, "'Just pass it to Victoria Sergeyevna.' Lyova tells him not to ask questions and just hand it to Victoria."),
]
