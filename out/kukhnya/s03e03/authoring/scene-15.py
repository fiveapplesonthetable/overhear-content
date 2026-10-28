ID = 'kukhnya-s03e03-scene-15'
SHOW = "kukhnya"
SEASON = 3
EPISODE = 3
SCENE = 15
TITLE = 'Две новости  (Two Pieces of News)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'katya': 'angelina', 'chef': 'anja'}
LABELS = {'anya': 'Федя', 'katya': 'Катя', 'chef': 'Шеф'}
SOURCE_NAME = "Кухня (Kukhnya) S3.03"
SOURCE_FILE = 'sources/kukhnya/s03/e03.ru.srt'

INTRO = 'Katya marches into the kitchen to announce that Barinov is her father, but when Barinov glares at her, she stops mid-sentence—convincing all the cooks that she is actually his secret mistress.'

STORY = [
    ('katya', 'Внимание всем! У меня для вас две новости.', 'Attention everyone! I have two pieces of news for you.', [(255, 'Внимание'), (255, 'у меня для вас две новости')], 'adapted'),
    ('katya', 'Первая новость — я не лесбиянка.', 'The first piece of news is I am not a lesbian.', [(256, 'Первая новость, я не лесбиянка')], ''),
    ('katya', 'А вторая новость — Виктор Петрович мой...', 'And the second piece of news is Viktor Petrovich is my...', [(257, 'А вторая новость, Виктор Петрович, мой')], ''),
    ('chef', 'Твой кто?', 'Your who?', [(258, 'Мой')], 'adapted'),
    ('anya', 'Он её любовник!', 'He is her lover!', [(259, 'Он ее любовник')], ''),
    ('anya', 'Точно любовник! Ну не отец же.', "Definitely her lover! Well, he's not her father.", [(260, 'любовник. Ну не отец же')], 'adapted'),
    ('anya', 'Вот почему он так бесился, когда мы все вокруг неё бегали.', 'That is why he was so furious when we were all running around her.', [(261, 'Вот почему он так бесился, когда мы все вокруг неё бегали')], ''),
    ('anya', 'Зачем тогда она меня поцеловала?', 'Why did she kiss me then?', [(262, 'Зачем тогда она меня поцеловала')], ''),
    ('anya', 'Для конспирации!', 'For cover!', [(263, 'Для конспирации')], ''),
    ('anya', 'А я сразу прямо догадался.', 'And I figured it out right away.', [(264, 'А я сразу'), (264, 'догадался')], 'adapted'),
    ('anya', 'Вот прямо сразу!', 'Right away!', [(265, 'Вот прямо сразу')], ''),
    ('anya', 'Они прямо сейчас там разговаривают.', 'They are in there talking right now.', [(267, 'прямо сейчас там')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Attention everyone! I have two pieces of news for you.' The meaning hinges on 'attention' working together with 'piece of news' in spoken Russian."),
    (1, None, "'The first piece of news is I am not a lesbian.' Katya brings out the contrast between 'first' and 'news' in a few short words."),
    (2, None, "'And the second piece of news is Viktor Petrovich is my...' Katya anchors the line on 'and', while 'my' completes the thought."),
    (3, None, "'Your who?' Chef Barinov addresses the listener with the informal singular 'you' alongside 'who'. Fedya answers right away."),
    (4, None, "'He is her lover!' The meaning hinges on 'he' working together with 'lover' in spoken Russian."),
    (5, None, "'Definitely her lover! Well, he's not her father.' In Russian, the idea of 'exactly' flows naturally into 'but' without extra filler words."),
    (6, None, "'That is why he was so furious when we were all running around her.' Here the Russian phrasing highlights 'here' before landing on 'ran around'."),
    (7, None, "'Why did she kiss me then?' The '-a' ending on the past-tense verb for 'kissed' marks a female speaker or subject."),
    (8, None, "'For cover!' Here the Russian phrasing highlights 'for' before landing on 'secrecy'."),
    (9, None, "'And I figured it out right away.' The '-l' ending on the verb meaning 'guessed' places the action in the masculine past tense."),
    (10, None, "'Right away!' Fedya anchors the line on 'here', while 'immediately' completes the thought."),
    (11, None, "'They are in there talking right now.' The grammar packs 'they' and 'to talk' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes Scene Fifteen. Listen for the irony of Fedya saying 'Definitely her lover—well, he's not her father!'"
CLOSING = ('anya', 'Я сразу догадался!')
